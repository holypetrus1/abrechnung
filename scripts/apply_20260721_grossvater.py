import json
from pathlib import Path

DATA = Path('data/buchungen.json')
STATUS = Path('data/status.md')
PROTOCOL = Path('data/protokoll.md')

transaction = {
    'id': 'AUS-20260721-002',
    'type': 'expense_without_receipt',
    'purchase_at': '2026-07-21T19:53:27+02:00',
    'entered_at': '2026-07-21T19:53:27+02:00',
    'merchant': 'Bezahlung Großvater',
    'receipt_total': 16.0,
    'holiday_total': 16.0,
    'allocated_total': 16.0,
    'community_total': 16.0,
    'excluded_total': 0.0,
    'payment_source': 'Großvater',
    'status': 'active',
    'notes': ['Ohne Bon nach Nutzerangabe erfasst', 'Vollständig als Gemeinschaftsausgabe'],
    'cost_groups': [{
        'id': 'community',
        'label': 'Gemeinschaft',
        'amount': 16.0,
        'shares': {'Simon': 0.25, 'Katrin': 0.25, 'Onkel': 0.25, 'Tante': 0.25, 'Oma': 0.0, 'Großvater': 0.0},
        'allocations': {'Simon': 4.0, 'Katrin': 4.0, 'Onkel': 4.0, 'Tante': 4.0, 'Oma': 0.0, 'Großvater': 0.0},
    }],
    'items': [{
        'position': 1,
        'name': 'Bezahlung Großvater',
        'quantity': 1,
        'unit': 'Sammelposition',
        'gross': 16.0,
        'net': 16.0,
        'holiday_amount': 16.0,
        'excluded_amount': 0.0,
        'classification': 'holiday',
        'cost_group_id': 'community',
    }],
    'payment_credits': [{'person': 'Großvater', 'amount': 16.0}],
}

persons = [
    {'person': 'Simon', 'charge': 170.13, 'payment_credit': 444.76, 'balance': 274.63},
    {'person': 'Katrin', 'charge': 203.72, 'payment_credit': 116.56, 'balance': -87.16},
    {'person': 'Onkel', 'charge': 172.60, 'payment_credit': 141.70, 'balance': -30.90},
    {'person': 'Tante', 'charge': 172.57, 'payment_credit': 0.0, 'balance': -172.57},
    {'person': 'Oma', 'charge': 0.0, 'payment_credit': 0.0, 'balance': 0.0},
    {'person': 'Großvater', 'charge': 0.0, 'payment_credit': 16.0, 'balance': 16.0},
]
transfers = [
    {'from': 'Katrin', 'to': 'Simon', 'amount': 87.16},
    {'from': 'Onkel', 'to': 'Simon', 'amount': 30.90},
    {'from': 'Tante', 'to': 'Simon', 'amount': 156.57},
    {'from': 'Tante', 'to': 'Großvater', 'amount': 16.0},
]

def de(amount):
    return f'{amount:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.') + ' €'

def date_de(timestamp):
    y, m, d = timestamp[:10].split('-')
    return f'{d}.{m}.{y}'

data = json.loads(DATA.read_text(encoding='utf-8'))
if transaction['id'] not in {t['id'] for t in data['transactions']}:
    data['transactions'].append(transaction)

data['updated_at'] = '2026-07-21T19:53:27+02:00'
data['week'] = 'Woche 1'
data['week_status'] = 'open'
data['balances']['total_holiday_expenses'] = 719.02
data['balances']['total_allocated_expenses'] = 719.02
data['balances']['total_receipt_expenses'] = 776.99
data['balances']['total_excluded_expenses'] = 57.97
data['balances']['persons'] = persons
data['balances']['suggested_transfers'] = transfers
DATA.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')

rows = []
for t in data['transactions']:
    rows.append(
        f"| {t['id']} | {date_de(t['purchase_at'])} | {t['merchant']} | {de(float(t['receipt_total']))} | "
        f"{de(float(t.get('allocated_total', t.get('holiday_total', 0))))} | {de(float(t.get('excluded_total', 0)))} | {t['payment_source']} |"
    )

balance_rows = []
for p in persons:
    prefix = '+' if p['balance'] > 0 else ''
    balance_rows.append(f"| {p['person']} | {de(p['charge'])} | {de(p['payment_credit'])} | {prefix}{de(p['balance'])} |")

protocol = f'''# Urlaubskasse Woche 1

**Stand:** 21.07.2026, 19:53 Uhr  
**Status:** Woche 1 bleibt geöffnet, bis der Beginn von Woche 2 ausdrücklich genannt wird.  
**Verbindliche Datenquelle:** `data/buchungen.json`

## Standardlogik

- Normale Gemeinschaftsausgaben tragen Simon, Katrin, Onkel und Tante zu je 25 %.
- Oma und Großvater tragen standardmäßig keinen Kostenanteil, können aber als Zahlende ein Guthaben erhalten.
- Abweichende Kostenblöcke werden je Vorgang separat geführt.
- Zahlende Person und Kostenverteilung werden getrennt erfasst.

## Aktueller Gesamtstand

| Person | Belastung | Zahlungsguthaben | Saldo |
|---|---:|---:|---:|
{chr(10).join(balance_rows)}

**Verrechnete Ausgaben gesamt:** {de(719.02)}  
**Beleg- und Ausgabensumme einschließlich ausgeschlossener Positionen:** {de(776.99)}  
**Ausgeschlossen:** {de(57.97)}

**Vorgeschlagener Ausgleich:**

- Katrin überweist Simon {de(87.16)}.
- Onkel überweist Simon {de(30.90)}.
- Tante überweist Simon {de(156.57)}.
- Tante überweist Großvater {de(16.00)}.

---

## Bisherige Vorgänge

| Vorgang | Datum | Händler | Belegsumme | Verrechnet | Ausgeschlossen | Zahlung |
|---|---|---|---:|---:|---:|---|
{chr(10).join(rows)}

---

## Neu erfasst am 21.07.2026

- **Bezahlung Großvater:** {de(16.00)}, vollständig Gemeinschaftsausgabe, bezahlt vom Großvater.
- Kostenanteil: Simon, Katrin, Onkel und Tante jeweils {de(4.00)}.
- Zahlungsguthaben Großvater: {de(16.00)}.
'''
PROTOCOL.write_text(protocol, encoding='utf-8')

status = f'''# Urlaubskasse Woche 1 – Arbeitsstatus

Stand: 21.07.2026 nach {len(data['transactions'])} erfassten Vorgängen.

## Verbindliche Regeln

- Woche 1 bleibt geöffnet, bis der Nutzer ausdrücklich den Beginn von Woche 2 nennt.
- Normale Gemeinschaftsausgaben tragen Simon, Katrin, Onkel und Tante zu je 25 %.
- Oma und Großvater tragen standardmäßig keinen Kostenanteil, erhalten aber Guthaben für eigene Zahlungen.
- Zahlende Person und Kostentragung werden getrennt erfasst.

## Aktueller Abrechnungsstand

- Verrechnete Ausgaben: {de(719.02)}
- Beleg-/Ausgabensumme: {de(776.99)}
- Ausgeschlossen: {de(57.97)}
- Simon: +{de(274.63)}
- Katrin: −{de(87.16)}
- Onkel: −{de(30.90)}
- Tante: −{de(172.57)}
- Großvater: +{de(16.00)}

## Vorgeschlagener Ausgleich

- Katrin überweist Simon {de(87.16)}.
- Onkel überweist Simon {de(30.90)}.
- Tante überweist Simon {de(156.57)}.
- Tante überweist Großvater {de(16.00)}.

## Zuletzt verarbeitet

- AUS-20260721-002 – Bezahlung Großvater, {de(16.00)}, bezahlt vom Großvater, vollständig Gemeinschaft.

## Fortsetzung

Neue Belege weiterhin Woche 1 zuordnen, bis der Nutzer ausdrücklich Woche 2 startet. Danach Daten, Protokoll, Status, Excel und Website gemeinsam aktualisieren.
'''
STATUS.write_text(status, encoding='utf-8')
