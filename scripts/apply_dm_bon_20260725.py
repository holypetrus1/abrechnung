from pathlib import Path
import json

DATA = Path("data/buchungen_woche2.json")
PROTOCOL = Path("data/protokoll_woche2.md")
STATUS = Path("data/status.md")

transaction_id = "BON-20260725-002"
data = json.loads(DATA.read_text(encoding="utf-8"))

if any(t.get("id") == transaction_id for t in data.get("transactions", [])):
    raise SystemExit("dm-Bon bereits erfasst")

items = [
    ("Sanft & Sicher DP 2x50 St", 1, "Packung", 2.95, 0.00, 2.95, "excluded", None),
    ("dmBio Barista Hafer Drink", 3, "Stk.", 4.05, 4.05, 0.00, "holiday", 1.35),
    ("dmBio Mandeln 200 g", 1, "Packung", 2.55, 0.00, 2.55, "excluded", None),
    ("dmBio Pinienkerne 60 g", 1, "Packung", 4.95, 4.95, 0.00, "holiday", None),
    ("dmBio Hanfsamen geschält 200 g", 1, "Packung", 2.95, 0.00, 2.95, "excluded", None),
    ("dmBio Leinsamen ganz 500 g", 1, "Packung", 1.55, 0.00, 1.55, "excluded", None),
    ("dmBio Spirelli 500 g", 1, "Packung", 0.85, 0.85, 0.00, "holiday", None),
    ("dmBio Gemüsebrühwürfel 66 g", 1, "Packung", 0.75, 0.00, 0.75, "excluded", None),
    ("Coupon dmBio Gemüsebrühwürfel", 1, "Coupon", -0.75, 0.00, -0.75, "excluded", None),
    ("dmBio Haferflocken Feinblatt 1000 g", 1, "Packung", 1.55, 0.00, 1.55, "excluded", None),
    ("Mivolis Vitamin C Brausetabletten", 1, "Packung", 0.50, 0.00, 0.50, "excluded", None),
]

json_items = []
for pos, (name, quantity, unit, gross, holiday, excluded, classification, unit_price) in enumerate(items, 1):
    item = {
        "position": pos,
        "name": name,
        "quantity": quantity,
        "unit": unit,
        "gross": gross,
        "net": gross,
        "holiday_amount": holiday,
        "excluded_amount": excluded,
        "classification": classification,
        "cost_group": "Gemeinschaft" if classification == "holiday" else "Ausgeschlossen",
    }
    if unit_price is not None:
        item["unit_price"] = unit_price
    json_items.append(item)

transaction = {
    "id": transaction_id,
    "type": "receipt",
    "purchase_at": "2026-07-25T11:24:31+02:00",
    "entered_at": "2026-07-27T13:45:00+02:00",
    "merchant": "dm-drogerie markt",
    "location": None,
    "receipt_total": 21.90,
    "holiday_total": 9.85,
    "allocated_total": 9.85,
    "excluded_total": 12.05,
    "payment_source": "Gemeinschaftskonto Katrin & Simon",
    "status": "active",
    "notes": [
        "Nur 3x dmBio Barista Hafer Drink, dmBio Pinienkerne und dmBio Spirelli berücksichtigt",
        "Alle übrigen Positionen einschließlich des Coupons für Gemüsebrühwürfel ausgeschlossen",
        "Verrechneter Anteil 9,85 € zu je 25 % auf alle vier Personen verteilt; Rundungscent bei Simon",
        "Zahlungsguthaben des Gemeinschaftskontos auf den verrechneten Anteil begrenzt: Simon 4,93 €, Katrin 4,92 €",
    ],
    "cost_groups": [{
        "id": "gemeinschaft",
        "label": "3x Barista Hafer, Pinienkerne und Spirelli",
        "amount": 9.85,
        "shares": {"Simon": 2.47, "Katrin": 2.46, "Hummel W": 2.46, "Hummel M": 2.46},
    }],
    "items": json_items,
    "payment_credits": [
        {"person": "Simon", "amount": 4.93},
        {"person": "Katrin", "amount": 4.92},
    ],
}

data["transactions"].append(transaction)
data["updated_at"] = "2026-07-27T13:45:00+02:00"
data["balances"] = {
    "total_receipt_expenses": 205.10,
    "total_holiday_expenses": 193.05,
    "total_excluded": 12.05,
    "persons": [
        {"person": "Simon", "charge": 45.68, "payment_credit": 188.13, "balance": 142.45},
        {"person": "Katrin", "charge": 45.66, "payment_credit": 4.92, "balance": -40.74},
        {"person": "Hummel W", "charge": 44.82, "payment_credit": 0.0, "balance": -44.82},
        {"person": "Hummel M", "charge": 56.89, "payment_credit": 0.0, "balance": -56.89},
    ],
    "suggested_transfers": [
        {"from": "Katrin", "to": "Simon", "amount": 40.74},
        {"from": "Hummel W", "to": "Simon", "amount": 44.82},
        {"from": "Hummel M", "to": "Simon", "amount": 56.89},
    ],
    "control_sum": 0.0,
}
DATA.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")

protocol = PROTOCOL.read_text(encoding="utf-8")
replacements = {
    "**Stand:** 27.07.2026, 13:30 Uhr": "**Stand:** 27.07.2026, 13:45 Uhr",
    "| Simon | 43,21 € | 183,20 € | +139,99 € |": "| Simon | 45,68 € | 188,13 € | +142,45 € |",
    "| Katrin | 43,20 € | 0,00 € | −43,20 € |": "| Katrin | 45,66 € | 4,92 € | −40,74 € |",
    "| Hummel W | 42,36 € | 0,00 € | −42,36 € |": "| Hummel W | 44,82 € | 0,00 € | −44,82 € |",
    "| Hummel M | 54,43 € | 0,00 € | −54,43 € |": "| Hummel M | 56,89 € | 0,00 € | −56,89 € |",
    "**Verrechnete Ausgaben gesamt:** 183,20 €": "**Verrechnete Ausgaben gesamt:** 193,05 €",
    "**Beleg- und Ausgabensumme:** 183,20 €": "**Beleg- und Ausgabensumme:** 205,10 €",
    "**Ausgeschlossen:** 0,00 €": "**Ausgeschlossen:** 12,05 €",
    "- Katrin überweist Simon 43,20 €.": "- Katrin überweist Simon 40,74 €.",
    "- Hummel W überweist Simon 42,36 €.": "- Hummel W überweist Simon 44,82 €.",
    "- Hummel M überweist Simon 54,43 €.": "- Hummel M überweist Simon 56,89 €.",
}
for old, new in replacements.items():
    if old not in protocol:
        raise RuntimeError(f"Erwarteter Protokolltext fehlt: {old}")
    protocol = protocol.replace(old, new, 1)

protocol += """

---

## BON-20260725-002 – dm-drogerie markt

- Kauf: **25.07.2026, 11:24 Uhr**
- Belegsumme: **21,90 €**
- Verrechnet: **9,85 €**
- Ausgeschlossen: **12,05 €**
- Bezahlt vom **Gemeinschaftskonto Katrin & Simon**

### Berücksichtigte Positionen

- 3 × dmBio Barista Hafer Drink: 4,05 €
- dmBio Pinienkerne: 4,95 €
- dmBio Spirelli: 0,85 €

Die 9,85 € werden auf alle vier Personen verteilt: Simon **2,47 €**, Katrin **2,46 €**, Hummel W **2,46 €**, Hummel M **2,46 €**. Der Rundungscent liegt bei Simon.

Dem Gemeinschaftskonto werden für den verrechneten Anteil Simon **4,93 €** und Katrin **4,92 €** gutgeschrieben. Sämtliche übrigen Positionen einschließlich des Coupons für die Gemüsebrühwürfel bleiben ausgeschlossen.
"""
PROTOCOL.write_text(protocol, encoding="utf-8")

STATUS.write_text("""# Urlaubskasse Woche 2 – Arbeitsstatus

Stand: 27.07.2026, 13:45 Uhr; 3 Vorgänge erfasst.

## Verbindliche Regeln

- Woche 2 ist die aktive Abrechnungsperiode.
- Normale Gemeinschaftsausgaben tragen Simon, Katrin, Hummel W und Hummel M zu je 25 %.
- Haushalte: Simon & Katrin sowie Hummel W & Hummel M.
- Die Standardverteilung erfolgt pro Person, nicht pro Haushalt.
- Ausgaben nur für einen Haushalt werden hälftig auf dessen Mitglieder verteilt; Rundungscent werden dokumentiert.
- Zahlende Person und Kostentragung werden getrennt erfasst.
- Gemeinsame Zahlungskonten werden den beiden Mitgliedern des jeweiligen Haushalts hälftig gutgeschrieben.
- Bei teilweise berücksichtigten Bons wird nur der verrechnete Anteil als Zahlungsguthaben angesetzt.
- Ein Vorgang kann mehrere Kostenblöcke mit eigenen Verteilungsschlüsseln enthalten.
- Pfand wird wie eine normale Ausgabe behandelt.
- Keine Zahlungsnummern oder Originalbelege im Repository.
- Korrekturen werden nachvollziehbar und append-only dokumentiert.

## Aktueller Abrechnungsstand

- Verrechnete Ausgaben: 193,05 €
- Beleg-/Ausgabensumme: 205,10 €
- Ausgeschlossen: 12,05 €
- Simon: +142,45 €
- Katrin: −40,74 €
- Hummel W: −44,82 €
- Hummel M: −56,89 €

## Vorgeschlagener Ausgleich

- Katrin überweist Simon 40,74 €.
- Hummel W überweist Simon 44,82 €.
- Hummel M überweist Simon 56,89 €.

## Zuletzt verarbeitet

- `BON-20260725-002` – dm-drogerie markt, 25.07.2026, Belegsumme 21,90 €.
- Verrechnet: 3x Barista Hafer, Pinienkerne und Spirelli = 9,85 €.
- Ausgeschlossen: 12,05 €.
- Bezahlt vom Gemeinschaftskonto Katrin & Simon; Guthaben Simon 4,93 €, Katrin 4,92 €.

## Archiv Woche 1

Woche 1 ist abgeschlossen und über die Archivfunktion der Website erreichbar.

## Fortsetzung

Vor jedem neuen Beleg zuerst `data/status.md` und `data/buchungen_woche2.json` lesen. Danach Woche-2-Daten, Protokoll, Status, Website und Excel-Export gemeinsam aktualisieren.
""", encoding="utf-8")
