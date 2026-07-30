const originalFetch = window.fetch.bind(window);

window.fetch = async (input, init) => {
  const url = typeof input === "string" ? input : input.url;
  const isWeek2Data = url.endsWith("data/buchungen_woche2.json");

  if (!isWeek2Data) {
    return originalFetch(input, init);
  }

  const [baseResponse, supplementResponse, correctionResponse] = await Promise.all([
    originalFetch(input, init),
    originalFetch("data/buchungen_woche2_nachtrag.json", { cache: "no-store" }),
    originalFetch("data/buchungen_woche2_korrektur_20260730.json", { cache: "no-store" }),
  ]);

  if (!baseResponse.ok) {
    return baseResponse;
  }

  const baseData = await baseResponse.json();
  const supplement = supplementResponse.ok ? await supplementResponse.json() : {};
  const correction = correctionResponse.ok ? await correctionResponse.json() : {};

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

  const existingTransactions = [
    ...(baseData.transactions || []),
    ...(supplement.transactions || []),
  ].map(applyReplacement);

  const existingIds = new Set(existingTransactions.map((transaction) => transaction.id));
  const additionalTransactions = (correction.transactions || []).filter(
    (transaction) => !existingIds.has(transaction.id),
  );

  const mergedData = {
    ...baseData,
    updated_at: correction.updated_at || supplement.updated_at || baseData.updated_at,
    transactions: [...existingTransactions, ...additionalTransactions],
    balances: correction.balances || supplement.balances || baseData.balances,
  };

  return new Response(JSON.stringify(mergedData), {
    status: 200,
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
};

document.addEventListener("DOMContentLoaded", () => {
  const isArchive = new URLSearchParams(location.search).get("woche") === "1";
  if (isArchive) return;

  const excelDescription = document.querySelector("#excel-description");
  const excelDownload = document.querySelector("#excel-download");
  const excelMeta = document.querySelector("#excel-meta");

  if (!excelDescription || !excelDownload || !excelMeta) return;

  excelDescription.textContent = "Die vollständige Excel-Datei mit dem aktuellen Datenstand steht hier zum Download bereit.";
  excelDownload.href = "exports/Urlaubskasse_Woche2.xlsx";
  excelDownload.setAttribute("download", "");
  excelDownload.removeAttribute("aria-disabled");
  excelDownload.classList.remove("is-disabled");
  excelDownload.textContent = "Excel-Datei herunterladen";
  excelMeta.textContent = "Dateiname: Urlaubskasse_Woche2.xlsx";
});
