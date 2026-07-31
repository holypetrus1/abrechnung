const weekConfigs = {
  current: {
    label: "Woche 2",
    dataPath: "data/buchungen_woche2_web.json",
    protocolPath: "data/protokoll_woche2.md",
    excelPath: "exports/Urlaubskasse_Woche2.xlsx",
    excelName: "Urlaubskasse_Woche2.xlsx",
    isArchive: false,
  },
  archive: {
    label: "Woche 1",
    dataPath: "data/buchungen.json",
    protocolPath: "data/protokoll.md",
    excelPath: "exports/Urlaubskasse_Woche1.xlsx",
    excelName: "Urlaubskasse_Woche1.xlsx",
    isArchive: true,
  },
};

const state = {
  config: new URLSearchParams(location.search).get("woche") === "1"
    ? weekConfigs.archive
    : weekConfigs.current,
};

const euro = new Intl.NumberFormat("de-DE", { style: "currency", currency: "EUR" });
const fullDate = new Intl.DateTimeFormat("de-DE", { day: "2-digit", month: "2-digit", year: "numeric" });
const shortDate = new Intl.DateTimeFormat("de-DE", { day: "2-digit", month: "short" });

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function inlineMarkdown(value) {
  return escapeHtml(value)
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\*([^*]+)\*/g, "<em>$1</em>");
}

function splitTableRow(line) {
  return line.trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map((cell) => cell.trim());
}

function isTableDivider(line) {
  const cells = splitTableRow(line);
  return cells.length > 0 && cells.every((cell) => /^:?-{3,}:?$/.test(cell));
}

function renderMarkdown(markdown) {
  const lines = markdown.replace(/\r/g, "").split("\n");
  const html = [];
  let index = 0;
  let listType = null;

  const closeList = () => {
    if (listType) html.push(`</${listType}>`);
    listType = null;
  };

  while (index < lines.length) {
    const line = lines[index].trim();
    if (!line) {
      closeList();
      index += 1;
      continue;
    }

    if (line.includes("|") && index + 1 < lines.length && isTableDivider(lines[index + 1])) {
      closeList();
      const headers = splitTableRow(line);
      const rows = [];
      index += 2;
      while (index < lines.length && lines[index].trim().includes("|")) {
        rows.push(splitTableRow(lines[index]));
        index += 1;
      }
      html.push('<div class="table-scroll"><table><thead><tr>');
      headers.forEach((header) => html.push(`<th>${inlineMarkdown(header)}</th>`));
      html.push("</tr></thead><tbody>");
      rows.forEach((row) => {
        html.push("<tr>");
        headers.forEach((_, cellIndex) => html.push(`<td>${inlineMarkdown(row[cellIndex] ?? "")}</td>`));
        html.push("</tr>");
      });
      html.push("</tbody></table></div>");
      continue;
    }

    const heading = line.match(/^(#{1,3})\s+(.+)$/);
    if (heading) {
      closeList();
      const level = heading[1].length;
      html.push(`<h${level}>${inlineMarkdown(heading[2])}</h${level}>`);
      index += 1;
      continue;
    }

    if (/^---+$/.test(line)) {
      closeList();
      html.push("<hr>");
      index += 1;
      continue;
    }

    const unordered = line.match(/^[-*]\s+(.+)$/);
    const ordered = line.match(/^\d+\.\s+(.+)$/);
    if (unordered || ordered) {
      const desiredType = unordered ? "ul" : "ol";
      if (listType !== desiredType) {
        closeList();
        listType = desiredType;
        html.push(`<${desiredType}>`);
      }
      html.push(`<li>${inlineMarkdown((unordered || ordered)[1])}</li>`);
      index += 1;
      continue;
    }

    closeList();
    html.push(`<p>${inlineMarkdown(line)}</p>`);
    index += 1;
  }

  closeList();
  return html.join("");
}

function applyWeekConfig() {
  const { config } = state;
  document.title = `Urlaubskasse · ${config.label}`;
  document.querySelector("#week-title").textContent = config.label;
  document.querySelector("#view-mode").textContent = config.isArchive ? "Archiv · abgeschlossen" : "Aktive Woche";
  document.querySelector("#protocol-link").href = config.protocolPath;

  const weekSwitch = document.querySelector("#week-switch");
  weekSwitch.href = config.isArchive ? (location.pathname || "./") : "?woche=1";
  weekSwitch.textContent = config.isArchive ? "Zur aktuellen Woche" : "Archiv · Woche 1";

  document.querySelector("#excel-title").textContent = `Urlaubskasse ${config.label}`;
  document.querySelector("#excel-description").textContent = "Die vollständige Excel-Datei mit dem aktuellen Datenstand steht hier zum Download bereit.";
  const excelDownload = document.querySelector("#excel-download");
  excelDownload.href = config.excelPath;
  excelDownload.setAttribute("download", "");
  excelDownload.removeAttribute("aria-disabled");
  excelDownload.classList.remove("is-disabled");
  excelDownload.textContent = "Excel-Datei herunterladen";
  document.querySelector("#excel-meta").textContent = `Dateiname: ${config.excelName}`;
}

function renderSummary(data) {
  document.querySelector("#total-expenses").textContent = euro.format(data.balances.total_holiday_expenses);
  const count = data.transactions.length;
  document.querySelector("#transaction-count").textContent = `${count} ${count === 1 ? "Vorgang" : "Vorgänge"}`;
  const updated = new Date(data.updated_at);
  document.querySelector("#updated-at").textContent = Number.isNaN(updated.getTime())
    ? "Aktueller Datenstand"
    : `Stand ${fullDate.format(updated)}`;
}

function renderPurchases(data) {
  const list = document.querySelector("#purchase-list");
  if (!data.transactions.length) {
    list.innerHTML = '<p class="empty-state">Noch keine Ausgaben erfasst.</p>';
    return;
  }

  const transactions = [...data.transactions].sort((left, right) => {
    if (!left.purchase_at && !right.purchase_at) return 0;
    if (!left.purchase_at) return 1;
    if (!right.purchase_at) return -1;
    return new Date(right.purchase_at) - new Date(left.purchase_at);
  });

  list.innerHTML = transactions.map((transaction) => {
    const hasDate = Boolean(transaction.purchase_at);
    const date = hasDate ? new Date(transaction.purchase_at) : null;
    const validDate = date && !Number.isNaN(date.getTime());
    const dateBlock = validDate
      ? `<strong>${shortDate.format(date)}</strong>${date.getFullYear()}`
      : "<strong>ohne</strong>Datum";
    const statusLabel = transaction.status === "corrected" ? "korrigiert" : "Urlaubskasse";
    return `
      <article class="purchase-row">
        <p class="purchase-date">${dateBlock}</p>
        <div class="purchase-main">
          <h3>${escapeHtml(transaction.merchant)}</h3>
          <p>Gezahlt von: ${escapeHtml(transaction.payment_source)}</p>
        </div>
        <p class="purchase-amount">${euro.format(transaction.holiday_total)}<small>${statusLabel}</small></p>
      </article>`;
  }).join("");
}

function renderBalances(data) {
  document.querySelector("#balance-grid").innerHTML = data.balances.persons.map((person) => {
    const balanceClass = person.balance > 0 ? "is-positive" : person.balance < 0 ? "is-negative" : "";
    const prefix = person.balance > 0 ? "+" : "";
    return `
      <article class="balance-card ${balanceClass}">
        <p class="balance-person">${escapeHtml(person.person)}</p>
        <p class="balance-value">${prefix}${euro.format(person.balance)}</p>
        <p class="balance-detail">Anteil ${euro.format(person.charge)}<br>Bezahlt ${euro.format(person.payment_credit)}</p>
      </article>`;
  }).join("");

  const transfers = data.balances.suggested_transfers || [];
  document.querySelector("#transfer-list").innerHTML = transfers.length
    ? transfers.map((transfer) => `
        <div class="transfer-row">
          <div class="transfer-route">${escapeHtml(transfer.from)} <span>überweist an</span> ${escapeHtml(transfer.to)}</div>
          <div class="transfer-amount">${euro.format(transfer.amount)}</div>
        </div>`).join("")
    : '<p class="transfer-empty">Aktuell sind keine Überweisungen erforderlich.</p>';
}

function activateView(viewName, updateHash = true) {
  document.querySelectorAll(".tab").forEach((tab) => {
    const active = tab.dataset.view === viewName;
    tab.classList.toggle("is-active", active);
    tab.setAttribute("aria-selected", String(active));
    tab.tabIndex = active ? 0 : -1;
  });
  document.querySelectorAll(".view").forEach((view) => {
    const active = view.id === `view-${viewName}`;
    view.classList.toggle("is-active", active);
    view.hidden = !active;
  });
  if (updateHash) history.replaceState(null, "", `${location.pathname}${location.search}#${viewName}`);
}

function initNavigation() {
  const validViews = ["protokoll", "einkaeufe", "excel", "ausgleich"];
  activateView(validViews.includes(location.hash.slice(1)) ? location.hash.slice(1) : "protokoll", false);
  const tabs = [...document.querySelectorAll(".tab")];
  tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => activateView(tab.dataset.view));
    tab.addEventListener("keydown", (event) => {
      if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
      event.preventDefault();
      let next = index;
      if (event.key === "ArrowLeft") next = (index - 1 + tabs.length) % tabs.length;
      if (event.key === "ArrowRight") next = (index + 1) % tabs.length;
      if (event.key === "Home") next = 0;
      if (event.key === "End") next = tabs.length - 1;
      tabs[next].focus();
      activateView(tabs[next].dataset.view);
    });
  });
}

async function loadData() {
  const [dataResponse, protocolResponse] = await Promise.all([
    fetch(state.config.dataPath, { cache: "no-store" }),
    fetch(state.config.protocolPath, { cache: "no-store" }),
  ]);
  if (!dataResponse.ok) throw new Error(`Datenbestand nicht gefunden (${dataResponse.status}).`);
  if (!protocolResponse.ok) throw new Error(`Protokoll nicht gefunden (${protocolResponse.status}).`);
  const data = await dataResponse.json();
  const protocol = await protocolResponse.text();
  renderSummary(data);
  renderPurchases(data);
  renderBalances(data);
  document.querySelector("#protocol-content").innerHTML = renderMarkdown(protocol);
}

function showError(error) {
  document.querySelector("#error-card").hidden = false;
  document.querySelector("#error-detail").textContent = String(error?.message || error);
}

applyWeekConfig();
initNavigation();
loadData().catch(showError);
