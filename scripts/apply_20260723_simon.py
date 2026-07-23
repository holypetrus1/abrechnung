import json
from pathlib import Path

DATA = Path('data/buchungen.json')
STATUS = Path('data/status.md')
PROTOCOL = Path('data/protokoll.md')

NEW_TRANSACTIONS = [
    {
        'id': 'BON-20260723-001',
        'type': 'receipt',
        'purchase_at': '2026-07-23T10:12:54+02:00',
        'entered_at': '2026-07-23T13:09:13+02:00',
        'merchant': 'Frischemarkt Boitzenburg',
        'location': 'Wegguner Straße 10, 17268 Boitzenburg',
        'receipt_total': 59.03,
        'holiday_total': 59.03,
        'allocated_total': 59.03,
        'community_total': 59.03,
        'excluded_total': 0.0,
        'payment_source': 'Simon',
        'status': 'active',
        'notes': ['Vollständig als Gemeinschaftsausgabe erfasst; keine Abzüge', 'Foto des Originalbons vorhanden'],
        'cost_groups': [
            {
                'id': 'community',
                'label': 'Gemeinschaft',
                'amount': 59.03,
                'shares': {'Simon': 0.25, 'Katrin': 0.25, 'Onkel': 0.25, 'Tante': 0.25, 'Oma': 0.0, 'Großvater': 0.0},
                'allocations': {'Simon': 14.76, 'Katrin': 14.76, 'Onkel': 14.76, 'Tante': 14.75, 'Oma': 0.0, 'Großvater': 0.0},
            }
        ],
        'items': [
            {
                'position': 1,
                'name': 'Frischemarkt-Einkauf laut Bonfoto',
                'quantity': 1,
                'unit': 'Sammelposition',
                'gross': 59.03,
                'net': 59.03,
                'holiday_amount': 59.03,
                'excluded_amount': 0.0,
                'classification': 'holiday',
                'cost_group_id': 'community',
                'note': 'Gesamter Bon ohne Ausnahmen; Einzelpositionen sind auf dem Bonfoto dokumentiert',
            }
        ],
        'payment_credits': [{'person': 'Simon', 'amount': 59.03}],
    },
    {
        'id': 'AUS-20260721-003',
        'type': 'expense_without_receipt',
        'purchase_at': '2026-07-21T12:00:00+02:00',
        'entered_at': '2026-07-23T13:09:13+02:00',
        'merchant': 'Tierpark Angermünde',
        'receipt_total': 20.0,
        'holiday_total': 20.0,
        'allocated_total': 20.0,
        'community_total': 20.0,
        'excluded_total': 0.0,
        'payment_source': 'Simon',
        'status': 'active',
        'notes': ['Ohne Bon nach Nutzerangabe erfasst', 'Vollständig als Gemeinschaftsausgabe; keine Abzüge', 'Kaufdatum Dienstag, 21.07.2026'],
        'cost_groups': [
            {
                'id': 'community',
                'label': 'Gemeinschaft',
                'amount': 20.0,
                'shares': {'Simon': 0.25, 'Katrin': 0.25, 'Onkel': 0.25, 'Tante': 0.25, 'Oma': 0.0, 'Großvater': 0.0},
                'allocations': {'Simon': 5.0, 'Katrin': 5.0, 'Onkel': 5.0, 'Tante': 5.0, 'Oma': 0.0, 'Großvater': 0.0},
            }
        ],
        'items': [
            {
                'position': 1,
                'name': 'Tierpark Angermünde',
                'quantity': 1,
                'unit': 'Sammelposition',
                'gross': 20.0,
                'net': 20.0,
                'holiday_amount': 20.0,
                'excluded_amount': 0.0,
                'classification': 'holiday',
                'cost_group_id': 'community',
            }
        ],
        'payment_credits': [{'person': 'Simon', 'amount': 20.0}],
    },
]

FINAL_PERSONS = [
    {'person': 'Simon', 'charge': 189.89, 'payment_credit': 523.79, 'balance': 333.90},
    {'person': 'Katrin', 'charge': 223.48, 'payment_credit': 116.56, 'balance': -106.92},
    {'person': 'Onkel', 'charge': 192.36, 'payment_credit': 141.70, 'balance': -50.66},
    {'person': 'Tante', 'charge': 192.32, 'payment_credit': 0.0, 'balance': -192.32},
    {'person': 'Oma', 'charge': 0.0, 'payment_credit': 0.0, 'balance': 0.0},
    {'person': 'Großvater', 'charge': 0.0, 'payment_credit': 16.0, 'balance': 16.0},
]
FINAL_TRANSFERS = [
    {'from': 'Katrin', 'to': 'Simon', 'amount': 106.92},
    {'from': 'Onkel', 'to': 'Simon', 'amount': 50.66},
    {'from': 'Tante', 'to': 'Simon', 'amount': 176.32},
    {'from': 'Tante', 'to': 'Großvater', 'amount': 16.0},
]

def de(amount):
    return f'{amount:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.') + ' €'

def date_de(timestamp):
    y, m, d = timestamp[:10].split('-')
    return f'{d}.{m}.{y}'

data = json.loads(DATA.read_text(encoding='utf-8'))
existing = {t['id'] for t in data.get('transactions', [])}
for transaction in NEW_TRANSACTIONS:
    if transaction['id'] not in existing:
        data['transactions'].append(transaction)

data['week'] = 'Woche 1'
data['week_status'] = 'open'
data['updated_at'] = '2026-07-23T13:09:13+02:00'

balances = data.setdefault('balances', {})
balances['total_holiday_expenses'] = 798.05
balances['total_allocated_expenses'] = 798.05
balances['total_receipt_expenses'] = 856.02
balances['total_excluded_expenses'] = 57.97
balances['persons'] = FINAL_PERSONS
balances['suggested_transfers'] = FINAL_TRANSFERS

DATA.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')

rows = []
for t in data['transactions']:
    rows.append(
        f"| {t['id']} | {date_de(t['purchase_at'])} | {t['merchant']} | {de(float(t['receipt_total']))} | "
        f"{de(float(t.get('allocated_total', t.get('holiday_total', 0))))} | {de(float(t.get('excluded_total', 0)))} | {t['payment_source']} |"
    )

balance_rows = []
for p in FINAL_PERSONS:
    prefix = '+' if p['balance'] > 0 else ''
    balance_rows.append(f"| {p['person']} | {de(p['charge'])} | {de(p['payment_credit'])} | {prefix}{de(p['balance'])} |")

protocol = f'''# Urlaubskasse Woche 1

**Stand:** 23.07.2026, 13:09 Uhr  
**Status:** Woche 1 bleibt geöffnet, bis der Beginn von Woche 2 ausdrücklich genannt wird.  
**Verbindliche Datenquelle:** `data/buchungen.json`

## Standardlogik

- Normale Gemeinschaftsausgaben tragen Simon, Katrin, Onkel und Tante zu je 25 %.
- Abweichende Kostenblöcke werden je Vorgang mit eigenem Verteilungsschlüssel geführt.
- Zahlende Person und Kostenverteilung werden getrennt erfasst.
- Zahlungen vom Gemeinschaftskonto Katrin & Simon werden beiden hälftig gutgeschrieben.
- Pfand zählt wie eine normale Ausgabe.

## Aktueller Gesamtstand

| Person | Belastung | Zahlungsguthaben | Saldo |
|---|---:|---:|---:|
{chr(10).join(balance_rows)}

**Verrechnete Ausgaben gesamt:** {de(798.05)}  
**Beleg- und Ausgabensumme einschließlich ausgeschlossener Positionen:** {de(856.02)}  
**Ausgeschlossen:** {de(57.97)}

**Vorgeschlagener Ausgleich:**

- Katrin überweist Simon {de(106.92)}.
- Onkel überweist Simon {de(50.66)}.
- Tante überweist Simon {de(176.32)}.
- Tante überweist Großvater {de(16.00)}.

---

## Bisherige Vorgänge

| Vorgang | Datum | Händler | Belegsumme | Verrechnet | Ausgeschlossen | Zahlung |
|---|---|---|---:|---:|---:|---|
{chr(10).join(rows)}

---

## Neu erfasst am 23.07.2026

- **Frischemarkt Boitzenburg:** Bon vom 23.07.2026 über {de(59.03)}, vollständig Gemeinschaft, bezahlt von Simon.
- **Tierpark Angermünde:** Ausgabe ohne Bon vom Dienstag, 21.07.2026, über {de(20.00)}, vollständig Gemeinschaft, bezahlt von Simon.

Die beiden neuen Ausgaben ergeben zusammen **{de(79.03)}**.

## Offener Vorgang

- `BON-20260717-001` – Barracuda Fisch, Matjesfilets {de(25.00)}; weiterhin als Sammelposition, bis der Originalbon vorliegt.
'''
PROTOCOL.write_text(protocol, encoding='utf-8')

status = f'''# Urlaubskasse Woche 1 – Arbeitsstatus

Stand: 23.07.2026 nach {len(data['transactions'])} erfassten Vorgängen.

## Verbindliche Regeln

- Woche 1 bleibt geöffnet, bis der Nutzer ausdrücklich den Beginn von Woche 2 nennt.
- Normale Gemeinschaftsausgaben tragen Simon, Katrin, Onkel und Tante zu je 25 %.
- Ein Vorgang kann mehrere Kostenblöcke mit eigenen Verteilungsschlüsseln enthalten.
- Zahlende Person und Kostentragung werden getrennt erfasst.
- Pfand wird wie eine normale Ausgabe behandelt.
- Keine Zahlungsnummern oder Originalbelege im Repo.

## Aktueller Abrechnungsstand

- Verrechnete Ausgaben: {de(798.05)}
- Beleg-/Ausgabensumme: {de(856.02)}
- Ausgeschlossen: {de(57.97)}
- Simon: +{de(333.90)}
- Katrin: −{de(106.92)}
- Onkel: −{de(50.66)}
- Tante: −{de(192.32)}
- Großvater: +{de(16.00)}

## Vorgeschlagener Ausgleich

- Katrin überweist Simon {de(106.92)}.
- Onkel überweist Simon {de(50.66)}.
- Tante überweist Simon {de(176.32)}.
- Tante überweist Großvater {de(16.00)}.

## Zuletzt verarbeitet

- Frischemarkt Boitzenburg, 23.07.2026: {de(59.03)}, bezahlt von Simon, vollständig Gemeinschaft.
- Tierpark Angermünde, 21.07.2026: {de(20.00)}, bezahlt von Simon, vollständig Gemeinschaft, ohne Bon.

## Fortsetzung

Neue Belege weiterhin Woche 1 zuordnen, bis der Nutzer ausdrücklich Woche 2 startet. Danach `data/buchungen.json`, `data/protokoll.md`, `data/status.md`, Excel und Website gemeinsam aktualisieren.
'''
STATUS.write_text(status, encoding='utf-8')
