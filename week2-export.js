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
