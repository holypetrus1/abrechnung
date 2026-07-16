const state = {
  data: null,
  protocol: "",
};

const euro = new Intl.NumberFormat("de-DE", {
  style: "currency",
  currency: "EUR",
});

const dateFormat = new Intl.DateTimeFormat("de-DE", {
  day: "2-digit",
  month: "2-digit",
  year: "numeric",
});

const shortDateFormat = new Intl.DateTimeFormat("de-DE", {
  day: "2-digit",
  month: "short",
});

function escapeHtml(value) {
  return String(value)
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
  return line
    .trim()
    .replace(/^\|/, "")
    .replace(/\|$/, "")
    .split("|")
    .map((cell) => cell.trim());
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
    if (listType) {
      html.push(`</${listType}>`);
      listType = null;
    }
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
      index += 2;
      const rows = [];
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
    html.push(`<p>${inlineMarkdown(line).replace(/ {2}$/, "<br>")}</p>`);
    index += 1;
  }

  closeList();
  return html.join("");
}

function activateView(viewName, updateHash = true) {
  document.querySelectorAll(".tab").forEach((tab) => {
    const isActive = tab.dataset.view === viewName;
    tab.classList.toggle("is-active", isActive);
    tab.setAttribute("aria-selected", String(isActive));
    tab.tabIndex = isActive ? 0 : -1;
  });

  document.querySelectorAll(".view").forEach((view) => {
    const isActive = view.id === `view-${viewName}`;
    view.classList.toggle("is-active", isActive);
    view.hidden = !isActive;
  });

  if (updateHash) {
    history.replaceState(null, "", `#${viewName}`);
  }
}

function renderSummary(data) {
  document.querySelector("#total-expenses").textContent = euro.format(data.balances.total_holiday_expenses);
  const transactionLabel = data.transactions.length === 1 ? "Vorgang" : "Vorgänge";
  document.querySelector("#transaction-count").textContent = `${data.transactions.length} ${transactionLabel}`;

  const updatedAt = new Date(data.updated_at);
  document.querySelector("#updated-at").textContent = `Stand ${dateFormat.format(updatedAt)}`;
}

function renderPurchases(data) {
  const list = document.querySelector("#purchase-list");
  const transactions = [...data.transactions].sort(
    (left, right) => new Date(right.purchase_at) - new Date(left.purchase_at),
  );

  list.innerHTML = transactions.map((transaction) => {
    const date = new Date(transaction.purchase_at);
    const isCredit = transaction.holiday_total < 0;
    const typeLabel = transaction.type === "credit_note" ? "Gutschrift" : "Urlaubskasse";
    return `
      <article class="purchase-row${isCredit ? " is-credit" : ""}">
        <p class="purchase-date"><strong>${shortDateFormat.format(date)}</strong>${date.getFullYear()}</p>
        <div class="purchase-main">
          <h3>${escapeHtml(transaction.merchant)}</h3>
          <p>Gezahlt von: ${escapeHtml(transaction.payment_source)}</p>
        </div>
        <p class="purchase-amount">${euro.format(transaction.holiday_total)}<small>${typeLabel}</small></p>
      </article>
    `;
  }).join("");
}

function renderBalances(data) {
  const grid = document.querySelector("#balance-grid");
  grid.innerHTML = data.balances.persons.map((person) => {
    const balanceClass = person.balance > 0 ? "is-positive" : person.balance < 0 ? "is-negative" : "";
    const prefix = person.balance > 0 ? "+" : "";
    return `
      <article class="balance-card ${balanceClass}">
        <p class="balance-person">${escapeHtml(person.person)}</p>
        <p class="balance-value">${prefix}${euro.format(person.balance)}</p>
        <p class="balance-detail">Anteil ${euro.format(person.charge)}<br>Bezahlt ${euro.format(person.payment_credit)}</p>
      </article>
    `;
  }).join("");

  const transferList = document.querySelector("#transfer-list");
  const transfers = data.balances.suggested_transfers;
  if (!transfers.length) {
    transferList.innerHTML = '<p class="transfer-empty">Aktuell sind keine Überweisungen erforderlich.</p>';
    return;
  }

  transferList.innerHTML = transfers.map((transfer) => `
    <div class="transfer-row">
      <div class="transfer-route">
        ${escapeHtml(transfer.from)} <span>überweist an</span> ${escapeHtml(transfer.to)}
      </div>
      <div class="transfer-amount">${euro.format(transfer.amount)}</div>
    </div>
  `).join("");
}

function showError(error) {
  document.querySelector("#error-card").hidden = false;
  document.querySelector("#error-detail").textContent = String(error?.message || error);
}

async function loadData() {
  const [dataResponse, protocolResponse] = await Promise.all([
    fetch("data/buchungen.json", { cache: "no-store" }),
    fetch("data/protokoll.md", { cache: "no-store" }),
  ]);

  if (!dataResponse.ok) {
    throw new Error(`Datenbestand nicht gefunden (${dataResponse.status}).`);
  }
  if (!protocolResponse.ok) {
    throw new Error(`Protokoll nicht gefunden (${protocolResponse.status}).`);
  }

  state.data = await dataResponse.json();
  state.protocol = await protocolResponse.text();

  renderSummary(state.data);
  renderPurchases(state.data);
  renderBalances(state.data);
  document.querySelector("#protocol-content").innerHTML = renderMarkdown(state.protocol);
}

function initNavigation() {
  const validViews = ["protokoll", "einkaeufe", "excel", "ausgleich"];
  const initialView = validViews.includes(location.hash.slice(1)) ? location.hash.slice(1) : "protokoll";
  activateView(initialView, false);

  const tabs = [...document.querySelectorAll(".tab")];
  tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => activateView(tab.dataset.view));
    tab.addEventListener("keydown", (event) => {
      if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
      event.preventDefault();
      let nextIndex = index;
      if (event.key === "ArrowLeft") nextIndex = (index - 1 + tabs.length) % tabs.length;
      if (event.key === "ArrowRight") nextIndex = (index + 1) % tabs.length;
      if (event.key === "Home") nextIndex = 0;
      if (event.key === "End") nextIndex = tabs.length - 1;
      tabs[nextIndex].focus();
      activateView(tabs[nextIndex].dataset.view);
    });
  });

  window.addEventListener("hashchange", () => {
    const view = location.hash.slice(1);
    if (validViews.includes(view)) activateView(view, false);
  });
}

initNavigation();
loadData().catch(showError);
