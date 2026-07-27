const originalFetch = window.fetch.bind(window);

window.fetch = async (input, init) => {
  const url = typeof input === "string" ? input : input.url;
  const isWeek2Data = url.endsWith("data/buchungen_woche2.json");

  if (!isWeek2Data) {
    return originalFetch(input, init);
  }

  const [baseResponse, supplementResponse] = await Promise.all([
    originalFetch(input, init),
    originalFetch("data/buchungen_woche2_nachtrag.json", { cache: "no-store" }),
  ]);

  if (!baseResponse.ok || !supplementResponse.ok) {
    return baseResponse;
  }

  const [baseData, supplement] = await Promise.all([
    baseResponse.json(),
    supplementResponse.json(),
  ]);

  const mergedData = {
    ...baseData,
    updated_at: supplement.updated_at || baseData.updated_at,
    transactions: [
      ...(baseData.transactions || []),
      ...(supplement.transactions || []),
    ],
    balances: supplement.balances || baseData.balances,
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
