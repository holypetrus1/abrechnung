import json
from pathlib import Path

DATA = Path('data/buchungen.json')
STATUS = Path('data/status.md')
PROTOCOL = Path('data/protokoll.md')

NEW_TRANSACTIONS = [
    {
        'id': 'BON-20260716-003',
        'type': 'receipt',
        'purchase_at': '2026-07-16T13:37:00+02:00',
        'entered_at': '2026-07-21T17:28:54+02:00',
        'merchant': 'BIO COMPANY Turmstraße',
        'location': 'Turmstraße 42, 10551 Berlin',
        'receipt_total': 24.74,
        'holiday_total': 24.74,
        'allocated_total': 24.74,
        'community_total': 24.74,
        'excluded_total': 0.0,
        'payment_source': 'Onkel',
        'status': 'active',
        'notes': ['Vollständig als Gemeinschaftsausgabe erfasst; keine Abzüge', 'Foto des Originalbons vorhanden'],
        'cost_groups': [
            {
                'id': 'community',
                'label': 'Gemeinschaft',
                'amount': 24.74,
                'shares': {'Simon': 0.25, 'Katrin': 0.25, 'Onkel': 0.25, 'Tante': 0.25, 'Oma': 0.0, 'Großvater': 0.0},
                'allocations': {'Simon': 6.19, 'Katrin': 6.19, 'Onkel': 6.18, 'Tante': 6.18, 'Oma': 0.0, 'Großvater': 0.0},
            }
        ],
        'items': [
            {
                'position': 1,
                'name': 'BIO-COMPANY-Einkauf laut Bonfoto',
                'quantity': 1,
                'unit': 'Sammelposition',
                'gross': 24.74,
                'net': 24.74,
                'holiday_amount': 24.74,
                'excluded_amount': 0.0,
                'classification': 'holiday',
                'cost_group_id': 'community',
                'note': 'Gesamter Bon ohne Abzüge; Einzelpositionen sind auf dem Bonfoto dokumentiert',
            }
        ],
        'payment_credits': [{'person': 'Onkel', 'amount': 24.74}],
    },
    {
        'id': 'BON-20260716-004',
        'type': 'receipt',
        'purchase_at': '2026-07-16T14:14:25+02:00',
        'entered_at': '2026-07-21T17:28:54+02:00',
        'merchant': 'E-Center Berlin-Moabit',
        'location': 'Stephanstraße 37-43, 10559 Berlin',
        'receipt_total': 81.96,
        'holiday_total': 81.96,
        'allocated_total': 81.96,
        'community_total': 81.96,
        'excluded_total': 0.0,
        'payment_source': 'Onkel',
        'status': 'active',
        'notes': ['Vollständig als Gemeinschaftsausgabe erfasst; keine Abzüge', 'Foto des Originalbons vorhanden'],
        'cost_groups': [
            {
                'id': 'community',
                'label': 'Gemeinschaft',
                'amount': 81.96,
                'shares': {'Simon': 0.25, 'Katrin': 0.25, 'Onkel': 0.25, 'Tante': 0.25, 'Oma': 0.0, 'Großvater': 0.0},
                'allocations': {'Simon': 20.49, 'Katrin': 20.49, 'Onkel': 20.49, 'Tante': 20.49, 'Oma': 0.0, 'Großvater': 0.0},
            }
        ],
        'items': [
            {
                'position': 1,
                'name': 'E-Center-Einkauf laut Bonfoto',
                'quantity': 1,
                'unit': 'Sammelposition',
                'gross': 81.96,
                'net': 81.96,
                'holiday_amount': 81.96,
                'excluded_amount': 0.0,
                'classification': 'holiday',
                'cost_group_id': 'community',
                'note': 'Gesamter Bon ohne Abzüge; Einzelpositionen sind auf dem Bonfoto dokumentiert',
            }
        ],
        'payment_credits': [{'person': 'Onkel', 'amount': 81.96}],
    },
    {
        'id': 'AUS-20260721-001',
        'type': 'expense_without_receipt',
        'purchase_at': '2026-07-21T17:28:54+02:00',
        'entered_at': '2026-07-21T17:28:54+02:00',
        'merchant': 'REWE',
        'receipt_total': 35.0,
        'holiday_total': 35.0,
        'allocated_total': 35.0,
        'community_total': 35.0,
        'excluded_total': 0.0,
        'payment_source': 'Onkel',
        'status': 'active',
        'notes': ['Ohne Bon nach Nutzerangabe erfasst', 'Vollständig als Gemeinschaftsausgabe; keine Abzüge'],
        'cost_groups': [
            {
                'id': 'community',
                'label': 'Gemeinschaft',
                'amount': 35.0,
                'shares': {'Simon': 0.25, 'Katrin': 0.25, 'Onkel': 0.25, 'Tante': 0.25, 'Oma': 0.0, 'Großvater': 0.0},
                'allocations': {'Simon': 8.75, 'Katrin': 8.75, 'Onkel': 8.75, 'Tante': 8.75, 'Oma': 0.0, 'Großvater': 0.0},
            }
        ],
        'items': [
            {
                'position': 1,
                'name': 'REWE-Einkauf ohne Bon',
                'quantity': 1,
                'unit': 'Sammelposition',
                'gross': 35.0,
                'net': 35.0,
                'holiday_amount': 35.0,
                'excluded_amount': 0.0,
                'classification': 'holiday',
                'cost_group_id': 'community',
            }
        ],
        'payment_credits': [{'person': 'Onkel', 'amount': 35.0}],
    },
]

FINAL_PERSONS = [
    {'person': 'Simon', 'charge': 166.13, 'payment_credit': 444.76, 'balance': 278.63},
    {'person': 'Katrin', 'charge': 199.72, 'payment_credit': 116.56, 'balance': -83.16},
    {'person': 'Onkel', 'charge': 168.60, 'payment_credit': 141.70, 'balance': -26.90},
    {'person': 'Tante', 'charge': 168.57, 'payment_credit': 0.0, 'balance': -168.57},
    {'person': 'Oma', 'charge': 0.0, 'payment_credit': 0.0, 'balance': 0.0},
    {'person': 'Großvater', 'charge': 0.0, 'payment_credit': 0.0, 'balance': 0.0},
]
FINAL_TRANSFERS = [
    {'from': 'Katrin', 'to': 'Simon', 'amount': 83.16},
    {'from': 'Onkel', 'to': 'Simon', 'amount': 26.90},
    {'from': 'Tante', 'to': 'Simon', 'amount': 168.57},
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

data['schema_version'] = max(2, int(data.get('schema_version', 1)))
data['week'] = 'Woche 1'
data['week_status'] = 'open'
data['updated_at'] = '2026-07-21T17:28:54+02:00'

balances = data.setdefault('balances', {})
balances['total_holiday_expenses'] = 703.02
balances['total_allocated_expenses'] = 703.02
balances['total_receipt_expenses'] = 760.99
balances['total_excluded_expenses'] = 57.97
balances['persons'] = FINAL_PERSONS
balances['suggested_transfers'] = FINAL_TRANSFERS

DATA.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')

transactions = data['transactions']
rows = []
for t in transactions:
    rows.append(
        f"| {t['id']} | {date_de(t['purchase_at'])} | {t['merchant']} | {de(float(t['receipt_total']))} | "
        f"{de(float(t.get('allocated_total', t.get('holiday_total', 0))))} | {de(float(t.get('excluded_total', 0)))} | {t['payment_source']} |"
    )

balance_rows = []
for p in FINAL_PERSONS:
    prefix = '+' if p['balance'] > 0 else ''
    balance_rows.append(f"| {p['person']} | {de(p['charge'])} | {de(p['payment_credit'])} | {prefix}{de(p['balance'])} |")

protocol = f'''# Urlaubskasse Woche 1

**Stand:** 21.07.2026, 17:28 Uhr  
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

**Verrechnete Ausgaben gesamt:** {de(703.02)}  
**Beleg- und Ausgabensumme einschließlich ausgeschlossener Positionen:** {de(760.99)}  
**Ausgeschlossen:** {de(57.97)}

**Vorgeschlagener Ausgleich:**

- Katrin überweist Simon {de(83.16)}.
- Onkel überweist Simon {de(26.90)}.
- Tante überweist Simon {de(168.57)}.

---

## Bisherige Vorgänge

| Vorgang | Datum | Händler | Belegsumme | Verrechnet | Ausgeschlossen | Zahlung |
|---|---|---|---:|---:|---:|---|
{chr(10).join(rows)}

---

## Neu erfasst am 21.07.2026

- **BIO COMPANY Turmstraße:** Bon vom 16.07.2026 über {de(24.74)}, vollständig Gemeinschaft, bezahlt von Onkel.
- **E-Center Berlin-Moabit:** Bon vom 16.07.2026 über {de(81.96)}, vollständig Gemeinschaft, bezahlt von Onkel.
- **REWE:** Einkauf vom 21.07.2026 ohne Bon über {de(35.00)}, vollständig Gemeinschaft, bezahlt von Onkel.

Die drei neuen Ausgaben ergeben zusammen **{de(141.70)}**.

## Offener Vorgang

- `BON-20260717-001` – Barracuda Fisch, Matjesfilets {de(25.00)}; weiterhin als Sammelposition, bis der Originalbon vorliegt.
'''
PROTOCOL.write_text(protocol, encoding='utf-8')

status = f'''# Urlaubskasse Woche 1 – Arbeitsstatus

Stand: 21.07.2026 nach {len(transactions)} erfassten Vorgängen.

## Verbindliche Regeln

- Woche 1 bleibt geöffnet, bis der Nutzer ausdrücklich den Beginn von Woche 2 nennt.
- Normale Gemeinschaftsausgaben tragen Simon, Katrin, Onkel und Tante zu je 25 %.
- Ein Vorgang kann mehrere Kostenblöcke mit eigenen Verteilungsschlüsseln enthalten.
- Zahlende Person und Kostentragung werden getrennt erfasst.
- Pfand wird wie eine normale Ausgabe behandelt.
- Keine Zahlungsnummern oder Originalbelege im Repo.

## Aktueller Abrechnungsstand

- Verrechnete Ausgaben: {de(703.02)}
- Beleg-/Ausgabensumme: {de(760.99)}
- Ausgeschlossen: {de(57.97)}
- Simon: +{de(278.63)}
- Katrin: −{de(83.16)}
- Onkel: −{de(26.90)}
- Tante: −{de(168.57)}

## Vorgeschlagener Ausgleich

- Katrin überweist Simon {de(83.16)}.
- Onkel überweist Simon {de(26.90)}.
- Tante überweist Simon {de(168.57)}.

## Zuletzt verarbeitet

- BIO COMPANY Turmstraße, 16.07.2026: {de(24.74)}, bezahlt von Onkel, vollständig Gemeinschaft.
- E-Center Berlin-Moabit, 16.07.2026: {de(81.96)}, bezahlt von Onkel, vollständig Gemeinschaft.
- REWE ohne Bon, 21.07.2026: {de(35.00)}, bezahlt von Onkel, vollständig Gemeinschaft.

## Fortsetzung

Neue Belege weiterhin Woche 1 zuordnen, bis der Nutzer ausdrücklich Woche 2 startet. Danach `data/buchungen.json`, `data/protokoll.md`, `data/status.md`, Excel und Website gemeinsam aktualisieren.
'''
STATUS.write_text(status, encoding='utf-8')
