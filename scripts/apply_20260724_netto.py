import json
from pathlib import Path

DATA = Path('data/buchungen.json')
STATUS = Path('data/status.md')
PROTOCOL = Path('data/protokoll.md')

TX_ID = 'BON-20260724-001'

data = json.loads(DATA.read_text(encoding='utf-8'))
existing = {t['id'] for t in data.get('transactions', [])}

if TX_ID not in existing:
    transaction = {
        'id': TX_ID,
        'type': 'receipt',
        'purchase_at': '2026-07-24T14:32:00+02:00',
        'entered_at': '2026-07-24T14:32:00+02:00',
        'merchant': 'Netto Marken-Discount Gramzow',
        'location': 'Schulzenstraße 30, 17291 Gramzow',
        'receipt_total': 26.78,
        'holiday_total': 26.78,
        'allocated_total': 26.78,
        'community_total': 26.78,
        'excluded_total': 0.0,
        'payment_source': 'Onkel',
        'status': 'active',
        'notes': [
            'Vollständig als Gemeinschaftsausgabe erfasst; keine Abzüge',
            'Bonfoto zeigt kein lesbares Kaufdatum; nach Eingang am 24.07.2026 diesem Datum zugeordnet'
        ],
        'cost_groups': [{
            'id': 'community',
            'label': 'Gemeinschaft',
            'amount': 26.78,
            'shares': {'Simon': 0.25, 'Katrin': 0.25, 'Onkel': 0.25, 'Tante': 0.25, 'Oma': 0.0, 'Großvater': 0.0},
            'allocations': {'Simon': 6.70, 'Katrin': 6.70, 'Onkel': 6.69, 'Tante': 6.69, 'Oma': 0.0, 'Großvater': 0.0}
        }],
        'items': [
            {'position': 1, 'name': 'BioBB Mozzarella-HF 125 g', 'quantity': 3, 'unit': 'Stk.', 'unit_price': 1.29, 'gross': 3.87, 'net': 3.87, 'holiday_amount': 3.87, 'excluded_amount': 0.0, 'classification': 'holiday', 'cost_group_id': 'community'},
            {'position': 2, 'name': 'Katjes Wunderland sauer 210 g', 'quantity': 1, 'unit': 'Packung', 'gross': 0.99, 'net': 0.99, 'holiday_amount': 0.99, 'excluded_amount': 0.0, 'classification': 'holiday', 'cost_group_id': 'community'},
            {'position': 3, 'name': 'RTL Spendentasche', 'quantity': 1, 'unit': 'Stk.', 'gross': 0.35, 'net': 0.35, 'holiday_amount': 0.35, 'excluded_amount': 0.0, 'classification': 'holiday', 'cost_group_id': 'community'},
            {'position': 4, 'name': 'BioD Kuer Frischkäse 200 g', 'quantity': 1, 'unit': 'Packung', 'gross': 1.79, 'net': 1.79, 'holiday_amount': 1.79, 'excluded_amount': 0.0, 'classification': 'holiday', 'cost_group_id': 'community'},
            {'position': 5, 'name': 'Hemme Frischmilch 3,7 % 1 l', 'quantity': 1, 'unit': 'Flasche', 'gross': 1.59, 'net': 1.59, 'holiday_amount': 1.59, 'excluded_amount': 0.0, 'classification': 'holiday', 'cost_group_id': 'community'},
            {'position': 6, 'name': 'Seeberger Studentenfutter 150 g', 'quantity': 1, 'unit': 'Packung', 'gross': 3.59, 'net': 3.59, 'holiday_amount': 3.59, 'excluded_amount': 0.0, 'classification': 'holiday', 'cost_group_id': 'community'},
            {'position': 7, 'name': 'BO-Puddingbrezel', 'quantity': 2, 'unit': 'Stk.', 'unit_price': 1.29, 'gross': 2.58, 'net': 2.58, 'holiday_amount': 2.58, 'excluded_amount': 0.0, 'classification': 'holiday', 'cost_group_id': 'community'},
            {'position': 8, 'name': 'BO-Wohnschmetterling', 'quantity': 2, 'unit': 'Stk.', 'unit_price': 1.29, 'gross': 2.58, 'net': 2.58, 'holiday_amount': 2.58, 'excluded_amount': 0.0, 'classification': 'holiday', 'cost_group_id': 'community'},
            {'position': 9, 'name': 'Bio Mini-Romanasalat', 'quantity': 2, 'unit': 'Stk.', 'unit_price': 1.69, 'gross': 3.38, 'net': 3.38, 'holiday_amount': 3.38, 'excluded_amount': 0.0, 'classification': 'holiday', 'cost_group_id': 'community'},
            {'position': 10, 'name': 'Rucola 125 g', 'quantity': 1, 'unit': 'Packung', 'gross': 0.99, 'net': 0.99, 'holiday_amount': 0.99, 'excluded_amount': 0.0, 'classification': 'holiday', 'cost_group_id': 'community'},
            {'position': 11, 'name': 'Bio Paprika Mix 400 g', 'quantity': 2, 'unit': 'Packung', 'unit_price': 2.29, 'gross': 4.58, 'net': 4.58, 'holiday_amount': 4.58, 'excluded_amount': 0.0, 'classification': 'holiday', 'cost_group_id': 'community'},
            {'position': 12, 'name': 'Radieschen', 'quantity': 1, 'unit': 'Bund', 'gross': 0.49, 'net': 0.49, 'holiday_amount': 0.49, 'excluded_amount': 0.0, 'classification': 'holiday', 'cost_group_id': 'community'}
        ],
        'payment_credits': [{'person': 'Onkel', 'amount': 26.78}]
    }
    data['transactions'].append(transaction)

    data['updated_at'] = '2026-07-24T14:32:00+02:00'
    balances = data['balances']
    balances['total_holiday_expenses'] = 836.87
    balances['total_allocated_expenses'] = 836.87
    balances['total_receipt_expenses'] = 899.24
    balances['total_excluded_expenses'] = 62.37
    balances['persons'] = [
        {'person': 'Simon', 'charge': 199.60, 'payment_credit': 523.79, 'balance': 324.19},
        {'person': 'Katrin', 'charge': 233.19, 'payment_credit': 116.56, 'balance': -116.63},
        {'person': 'Onkel', 'charge': 202.06, 'payment_credit': 180.52, 'balance': -21.54},
        {'person': 'Tante', 'charge': 202.02, 'payment_credit': 0.0, 'balance': -202.02},
        {'person': 'Oma', 'charge': 0.0, 'payment_credit': 0.0, 'balance': 0.0},
        {'person': 'Großvater', 'charge': 0.0, 'payment_credit': 16.0, 'balance': 16.0}
    ]
    balances['suggested_transfers'] = [
        {'from': 'Katrin', 'to': 'Simon', 'amount': 116.63},
        {'from': 'Onkel', 'to': 'Simon', 'amount': 21.54},
        {'from': 'Tante', 'to': 'Simon', 'amount': 186.02},
        {'from': 'Tante', 'to': 'Großvater', 'amount': 16.0}
    ]

    DATA.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')

status = '''# Urlaubskasse Woche 1 – Arbeitsstatus

Stand: 24.07.2026 nach 19 erfassten Vorgängen.

## Verbindliche Regeln

- Woche 1 bleibt geöffnet, bis der Nutzer ausdrücklich den Beginn von Woche 2 nennt.
- Normale Gemeinschaftsausgaben tragen Simon, Katrin, Onkel und Tante zu je 25 %.
- Ein Vorgang kann mehrere Kostenblöcke mit eigenen Verteilungsschlüsseln enthalten.
- Zahlende Person und Kostentragung werden getrennt erfasst.
- Pfand wird wie eine normale Ausgabe behandelt.
- Keine Zahlungsnummern oder Originalbelege im Repo.

## Aktueller Abrechnungsstand

- Verrechnete Ausgaben: 836,87 €
- Beleg-/Ausgabensumme: 899,24 €
- Ausgeschlossen: 62,37 €
- Simon: +324,19 €
- Katrin: −116,63 €
- Onkel: −21,54 €
- Tante: −202,02 €
- Großvater: +16,00 €

## Vorgeschlagener Ausgleich

- Katrin überweist Simon 116,63 €.
- Onkel überweist Simon 21,54 €.
- Tante überweist Simon 186,02 €.
- Tante überweist Großvater 16,00 €.

## Zuletzt verarbeitet

- Netto Marken-Discount Gramzow: 26,78 €, vollständig Gemeinschaft, bezahlt von Onkel.
- Das Kaufdatum war auf dem Bonfoto nicht sichtbar und wurde dem Eingangstag 24.07.2026 zugeordnet.

## Fortsetzung

Neue Belege weiterhin Woche 1 zuordnen, bis der Nutzer ausdrücklich Woche 2 startet. Danach `data/buchungen.json`, `data/protokoll.md`, `data/status.md`, Excel und Website gemeinsam aktualisieren.
'''
STATUS.write_text(status, encoding='utf-8')

protocol = PROTOCOL.read_text(encoding='utf-8')
protocol += '''

---

## BON-20260724-001 – Netto Marken-Discount Gramzow

- Erfasst/Kaufdatum: 24.07.2026 (Datum auf Foto nicht sichtbar; dem Eingangstag zugeordnet)
- Belegsumme: **26,78 €**
- Gemeinschaftsausgabe: **26,78 €**
- Ausgeschlossen: **0,00 €**
- Bezahlt von: Onkel
- Verteilung: Simon 6,70 €, Katrin 6,70 €, Onkel 6,69 €, Tante 6,69 €
- Keine Abzüge.
'''
PROTOCOL.write_text(protocol, encoding='utf-8')
