#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "buchungen.json"
STATUS_PATH = ROOT / "data" / "status.md"
PROTOCOL_PATH = ROOT / "data" / "protokoll.md"
XLSX_PATH = ROOT / "exports" / "Urlaubskasse_Woche1.xlsx"

PAYLOAD_PATH = ROOT / "scripts" / "update_20260718_payload.json"
PAYLOAD = json.loads(PAYLOAD_PATH.read_text(encoding="utf-8"))
UPDATED_AT = PAYLOAD["updated_at"]
NEW_TRANSACTIONS = PAYLOAD["transactions"]
BALANCES = PAYLOAD["balances"]

def euro(value: float) -> str:
    return f"{value:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")


def display_dt(value: str) -> str:
    return f"{value[8:10]}.{value[5:7]}.{value[0:4]} {value[11:16]}" if len(value) >= 16 else value


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    existing = {tx.get("id") for tx in data.get("transactions", [])}
    for tx in NEW_TRANSACTIONS:
        if tx["id"] not in existing:
            data["transactions"].append(tx)
    data["updated_at"] = UPDATED_AT
    data["balances"] = BALANCES
    DATA_PATH.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    STATUS_PATH.write_text(build_status(), encoding="utf-8")
    old_protocol = PROTOCOL_PATH.read_text(encoding="utf-8")
    PROTOCOL_PATH.write_text(update_protocol(old_protocol, data), encoding="utf-8")

    XLSX_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_xlsx(data, XLSX_PATH)


def build_status() -> str:
    return """# Urlaubskasse Woche 1 – Arbeitsstatus

Stand: 18.07.2026 nach sechs erfassten Einkäufen, einer Ausgabe ohne Bon und einer Gutschrift.

## Verbindliche Regeln

- Abrechnungskonten: Simon, Katrin, Onkel, Tante, Oma, Großvater.
- Kinder werden nicht als eigene Abrechnungskonten belastet.
- Normale laufende Urlaubsausgaben tragen Simon, Katrin, Onkel und Tante zu je 25 %.
- Oma und Großvater tragen laufende Ausgaben standardmäßig nicht, da sie die Unterkunft bezahlt haben.
- Abweichungen gelten nur, wenn sie beim jeweiligen Vorgang ausdrücklich genannt werden.
- Zahlende Person beziehungsweise Zahlungsquelle wird personenscharf erfasst.
- Zahlungen vom Gemeinschaftskonto von Simon und Katrin werden hälftig beiden als Vorleistung zugerechnet.
- Pfand wird wie eine normale Ausgabe behandelt.
- Bonweite Rabatte werden anteilig nach Warenwert auf Urlaubs- und Privatpositionen verteilt.
- Kaufdatum und Erfassungszeitpunkt werden getrennt protokolliert.
- Jeder Bon wird positionsgenau gespeichert. Korrekturen werden dokumentiert und nicht still überschrieben.
- Keine Kreditkarten-, Konto- oder Gutscheinnummern und keine Originalbelege im Repo.

## Aktueller Abrechnungsstand

- Anrechenbare Urlaubsausgaben gesamt: 219,91 €
- Belastung:
  - Simon: 54,98 €
  - Katrin: 54,98 €
  - Onkel: 54,98 €
  - Tante: 54,97 € (Rundungscent)
- Zahlungsguthaben:
  - Simon: 127,46 €
  - Katrin: 92,45 €
- Salden:
  - Simon: +72,48 €
  - Katrin: +37,47 €
  - Onkel: −54,98 €
  - Tante: −54,97 €
- Vorgeschlagener Ausgleich:
  - Onkel überweist Simon 54,98 €
  - Tante überweist Simon 17,50 €
  - Tante überweist Katrin 37,47 €

## Zuletzt verarbeitete Vorgänge

- BON-20260718-001 – Netto Marken-Discount, Gramzow
  - Kauf: 18.07.2026, 16:57 Uhr
  - Belegsumme und Urlaubsausgabe: 71,43 €
  - Keine Abzüge
  - Gezahlt vom Gemeinschaftskonto Katrin & Simon; Simon 35,72 €, Katrin 35,71 € Zahlungsguthaben
- AUS-20260718-001 – Hofladen Marmelade & more
  - Kauf: 18.07.2026; ohne Bon, 10,00 €
  - Gezahlt von Simon

## Offener Vorgang

- BON-20260717-001 – Barracuda Fisch, Matjesfilets 25,00 €
- Vorläufig als Sammelposition erfasst; Originalbon steht noch aus.

## Fortsetzung in einem neuen Chat

Den aktuellen Stand zuerst aus `data/status.md`, `data/buchungen.json` und `data/protokoll.md` laden. Danach neue Belege ergänzen und alle drei Dateien sowie den Excel-Export aktualisieren.
"""


def summary_block() -> str:
    return """## Aktueller Gesamtstand

| Person | Belastung | Zahlungsguthaben | Saldo |
|---|---:|---:|---:|
| Simon | 54,98 € | 127,46 € | +72,48 € |
| Katrin | 54,98 € | 92,45 € | +37,47 € |
| Onkel | 54,98 € | 0,00 € | −54,98 € |
| Tante | 54,97 € | 0,00 € | −54,97 € |
| Oma | 0,00 € | 0,00 € | 0,00 € |
| Großvater | 0,00 € | 0,00 € | 0,00 € |

**Anrechenbare Urlaubsausgaben gesamt:** 219,91 €

**Vorgeschlagener Ausgleich:**

- Onkel überweist Simon 54,98 €.
- Tante überweist Simon 17,50 €.
- Tante überweist Katrin 37,47 €.

---

## Bisherige Vorgänge"""


def transaction_section(tx: dict) -> str:
    lines = [
        f"## {tx['id']} – {tx['merchant']}",
        "",
        f"- Kauf: {display_dt(tx['purchase_at'])} Uhr" if tx["type"] == "receipt" else "- Kauf: 18.07.2026; genaue Uhrzeit nicht angegeben",
        f"- Belegsumme: **{euro(tx['receipt_total'])}**",
        f"- Urlaubsausgabe: **{euro(tx['holiday_total'])}**",
        f"- Ausgeschlossen: **{euro(tx.get('excluded_total', 0.0))}**",
        f"- Zahlung: {tx['payment_source']}",
    ]
    credits = ", ".join(f"{c['person']} {euro(c['amount'])}" for c in tx.get("payment_credits", []))
    if credits:
        lines.append(f"- Zahlungsguthaben: {credits}")
    lines.extend(["", "### Positionen", "", "| Pos. | Artikel | Brutto | Netto | Zuordnung |", "|---:|---|---:|---:|---|"])
    for item in tx.get("items", []):
        lines.append(
            f"| {item.get('position','')} | {item.get('name','')} | "
            f"{euro(float(item.get('gross',0)))} | {euro(float(item.get('net',0)))} | Urlaub |"
        )
    return "\n".join(lines)


def update_protocol(text: str, data: dict) -> str:
    had_netto = "BON-20260718-001" in text
    had_hof = "AUS-20260718-001" in text
    text = re.sub(r"\*\*Stand:\*\*.*?  \n", "**Stand:** 18.07.2026, 17:56:24 Uhr  \n", text, count=1)
    text = re.sub(
        r"## Aktueller Gesamtstand.*?## Bisherige Vorgänge",
        summary_block(),
        text,
        count=1,
        flags=re.S,
    )

    if not had_netto:
        marker = "| BON-20260717-002 | 17.07.2026 | BIO COMPANY Rathauscenter | 73,41 € | 69,44 € | 3,97 € | Gemeinschaftskonto Katrin & Simon |"
        additions = (
            marker
            + "\n| BON-20260718-001 | 18.07.2026 | Netto Marken-Discount | 71,43 € | 71,43 € | 0,00 € | Gemeinschaftskonto Katrin & Simon |"
            + "\n| AUS-20260718-001 | 18.07.2026 | Hofladen Marmelade & more | 10,00 € | 10,00 € | 0,00 € | Simon |"
        )
        text = text.replace(marker, additions, 1)

    sections = []
    if not had_netto:
        sections.append(transaction_section(NEW_TRANSACTIONS[0]))
    if not had_hof:
        sections.append(transaction_section(NEW_TRANSACTIONS[1]))
    if sections:
        insertion = "\n\n---\n\n".join(sections) + "\n\n---\n\n"
        text = text.replace("## Änderungsprotokoll", insertion + "## Änderungsprotokoll", 1)

    if not had_netto:
        text = text.rstrip() + (
            "\n6. **18.07.2026 – Netto Marken-Discount:** Bon über 71,43 € vollständig und ohne Abzüge "
            "als Urlaubsausgabe aufgenommen; Zahlung vom Gemeinschaftskonto hälftig gutgeschrieben.\n"
        )
    if not had_hof:
        text = text.rstrip() + (
            "\n7. **18.07.2026 – Hofladen:** Ausgabe ohne Bon über 10,00 € als von Simon bezahlt aufgenommen.\n"
        )
    text = text.rstrip() + (
        "\n8. **18.07.2026 – Salden:** Gesamtstand auf 219,91 € aktualisiert; Rundungscent der Belastung Tante zugeordnet.\n"
    )
    return text


def col_name(n: int) -> str:
    result = ""
    while n:
        n, rem = divmod(n - 1, 26)
        result = chr(65 + rem) + result
    return result


def cell_xml(row: int, col: int, value, style: int = 0) -> str:
    ref = f"{col_name(col)}{row}"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return f'<c r="{ref}" s="{style}"><v>{value}</v></c>'
    escaped = html.escape("" if value is None else str(value))
    return f'<c r="{ref}" s="{style}" t="inlineStr"><is><t>{escaped}</t></is></c>'


def sheet_xml(rows: list[list], currency_cols: set[int] | None = None) -> str:
    currency_cols = currency_cols or set()
    body = []
    for r_idx, row in enumerate(rows, start=1):
        cells = []
        for c_idx, value in enumerate(row, start=1):
            style = 1 if r_idx == 1 else (2 if c_idx in currency_cols and isinstance(value, (int, float)) else 0)
            cells.append(cell_xml(r_idx, c_idx, value, style))
        body.append(f'<row r="{r_idx}">{"".join(cells)}</row>')
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<sheetData>' + "".join(body) + '</sheetData></worksheet>'
    )


def write_xlsx(data: dict, path: Path) -> None:
    persons = data["balances"]["persons"]
    transfers = data["balances"]["suggested_transfers"]
    overview = [["Urlaubskasse Woche 1", "Stand", UPDATED_AT], ["Urlaubsausgaben gesamt", data["balances"]["total_holiday_expenses"]], [], ["Person", "Belastung", "Guthaben", "Saldo"]]
    overview += [[p["person"], p["charge"], p["payment_credit"], p["balance"]] for p in persons]
    overview += [[], ["Ausgleich von", "an", "Betrag"]] + [[t["from"], t["to"], t["amount"]] for t in transfers]

    transactions = [["Vorgang", "Datum", "Händler", "Zahlung", "Belegsumme", "Urlaub", "Privat", "Status"]]
    positions = [["Vorgang", "Datum", "Händler", "Pos.", "Artikel", "Menge", "Einheit", "Brutto", "Rabatt", "Netto", "Urlaub", "Privat", "Zuordnung", "Notiz"]]
    for tx in data.get("transactions", []):
        transactions.append([
            tx.get("id", ""), display_dt(tx.get("purchase_at", "")), tx.get("merchant", ""),
            tx.get("payment_source", ""), tx.get("receipt_total", 0), tx.get("holiday_total", 0),
            tx.get("excluded_total", 0), tx.get("status", "")
        ])
        for item in tx.get("items", []):
            positions.append([
                tx.get("id", ""), display_dt(tx.get("purchase_at", "")), tx.get("merchant", ""),
                item.get("position", ""), item.get("name", ""), item.get("quantity", 1),
                item.get("unit", ""), item.get("gross", 0), item.get("discount", 0),
                item.get("net", 0), item.get("holiday_amount", 0), item.get("excluded_amount", 0),
                item.get("classification", ""), item.get("note", "")
            ])
    settlement = [["Von", "An", "Betrag"]] + [[t["from"], t["to"], t["amount"]] for t in transfers]

    sheets = [
        ("Übersicht", overview, {2, 3, 4}),
        ("Vorgänge", transactions, {5, 6, 7}),
        ("Positionen", positions, {8, 9, 10, 11, 12}),
        ("Ausgleich", settlement, {3}),
    ]
    content_types = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
        '<Default Extension="xml" ContentType="application/xml"/>',
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>',
        '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>',
    ]
    for i in range(1, len(sheets) + 1):
        content_types.append(f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>')
    content_types.append('</Types>')

    workbook_sheets = "".join(
        f'<sheet name="{html.escape(name)}" sheetId="{i}" r:id="rId{i}"/>'
        for i, (name, _, _) in enumerate(sheets, start=1)
    )
    workbook = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f'<sheets>{workbook_sheets}</sheets></workbook>'
    )
    rels = "".join(
        f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>'
        for i in range(1, len(sheets) + 1)
    ) + f'<Relationship Id="rId{len(sheets)+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
    workbook_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        + rels + '</Relationships>'
    )
    root_rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
        '</Relationships>'
    )
    styles = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<numFmts count="1"><numFmt numFmtId="164" formatCode="#,##0.00 [$€-407]"/></numFmts>'
        '<fonts count="2"><font><sz val="11"/><name val="Aptos"/></font><font><b/><color rgb="FFFFFFFF"/><sz val="11"/><name val="Aptos"/></font></fonts>'
        '<fills count="3"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill><fill><patternFill patternType="solid"><fgColor rgb="FF1F4E78"/><bgColor indexed="64"/></patternFill></fill></fills>'
        '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>'
        '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
        '<cellXfs count="3"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
        '<xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1"/>'
        '<xf numFmtId="164" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/></cellXfs>'
        '</styleSheet>'
    )

    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", "".join(content_types))
        z.writestr("_rels/.rels", root_rels)
        z.writestr("xl/workbook.xml", workbook)
        z.writestr("xl/_rels/workbook.xml.rels", workbook_rels)
        z.writestr("xl/styles.xml", styles)
        for i, (_, rows, currency_cols) in enumerate(sheets, start=1):
            z.writestr(f"xl/worksheets/sheet{i}.xml", sheet_xml(rows, currency_cols))


if __name__ == "__main__":
    main()
