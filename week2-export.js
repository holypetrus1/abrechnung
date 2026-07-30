const originalFetch = window.fetch.bind(window);

window.fetch = async (input, init) => {
  const url = typeof input === "string" ? input : input.url;
  const isWeek2Data = url.endsWith("data/buchungen_woche2.json");

  if (!isWeek2Data) {
    return originalFetch(input, init);
  }

  const [baseResponse, supplementResponse, correctionResponse, eveningResponse] = await Promise.all([
    originalFetch(input, init),
    originalFetch("data/buchungen_woche2_nachtrag.json", { cache: "no-store" }),
    originalFetch("data/buchungen_woche2_korrektur_20260730.json", { cache: "no-store" }),
    originalFetch("data/buchungen_woche2_nachtrag_20260730_abends.json", { cache: "no-store" }),
  ]);

  if (!baseResponse.ok) {
    return baseResponse;
  }

  const baseData = await baseResponse.json();
  const supplement = supplementResponse.ok ? await supplementResponse.json() : {};
  const correction = correctionResponse.ok ? await correctionResponse.json() : {};
  const eveningSupplement = eveningResponse.ok ? await eveningResponse.json() : {};

  const replacements = new Map(
    (correction.replace_transactions || []).map((replacement) => [replacement.id, replacement]),
  );

  const applyReplacement = (transaction) => {
    const replacement = replacements.get(transaction.id);
    if (!replacement) return transaction;

    const itemUpdate = replacement.item_cost_group_updates;
    const updatedPositions = new Set(itemUpdate?.positions || []);
    const items = (transaction.items || []).map((item) => (
      updatedPositions.has(item.position)
        ? { ...item, cost_group: itemUpdate.cost_group }
        : item
    ));

    return {
      ...transaction,
      status: replacement.status || transaction.status,
      notes: replacement.notes || transaction.notes,
      cost_groups: replacement.cost_groups || transaction.cost_groups,
      items,
    };
  };

  const initialTransactions = [
    ...(baseData.transactions || []),
    ...(supplement.transactions || []),
  ].map(applyReplacement);

  const combinedAdditional = [
    ...(correction.transactions || []),
    ...(eveningSupplement.transactions || []),
  ];

  const transactions = [...initialTransactions];
  const existingIds = new Set(transactions.map((transaction) => transaction.id));
  combinedAdditional.forEach((transaction) => {
    if (!existingIds.has(transaction.id)) {
      transactions.push(transaction);
      existingIds.add(transaction.id);
    }
  });

  const mergedData = {
    ...baseData,
    updated_at: eveningSupplement.updated_at || correction.updated_at || supplement.updated_at || baseData.updated_at,
    transactions,
    balances: eveningSupplement.balances || correction.balances || supplement.balances || baseData.balances,
  };

  return new Response(JSON.stringify(mergedData), {
    status: 200,
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
};

function markUndatedPurchaseRows() {
  document.querySelectorAll("#purchase-list .purchase-row").forEach((row) => {
    const title = row.querySelector(".purchase-main h3")?.textContent || "";
    if (!title.startsWith("Undatierte Ausgabe")) return;

    const date = row.querySelector(".purchase-date");
    if (date) date.innerHTML = "<strong>ohne</strong>Datum";
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const isArchive = new URLSearchParams(location.search).get("woche") === "1";
  if (isArchive) return;

  const excelDescription = document.querySelector("#excel-description");
  const excelDownload = document.querySelector("#excel-download");
  const excelMeta = document.querySelector("#excel-meta");

  if (excelDescription && excelDownload && excelMeta) {
    excelDescription.textContent = "Die vollständige Excel-Datei mit dem aktuellen Datenstand steht hier zum Download bereit.";
    excelDownload.href = "exports/Urlaubskasse_Woche2.xlsx";
    excelDownload.setAttribute("download", "");
    excelDownload.removeAttribute("aria-disabled");
    excelDownload.classList.remove("is-disabled");
    excelDownload.textContent = "Excel-Datei herunterladen";
    excelMeta.textContent = "Dateiname: Urlaubskasse_Woche2.xlsx";
  }

  const purchaseList = document.querySelector("#purchase-list");
  if (purchaseList) {
    const observer = new MutationObserver(markUndatedPurchaseRows);
    observer.observe(purchaseList, { childList: true, subtree: true });
    markUndatedPurchaseRows();
  }
});
