import json
from pathlib import Path

DATA=Path('data/buchungen.json')
STATUS=Path('data/status.md')
PROTOCOL=Path('data/protokoll.md')
ID='AUS-20260724-001'

data=json.loads(DATA.read_text(encoding='utf-8'))
if ID not in {t['id'] for t in data['transactions']}:
    tx={
      'id':ID,
      'type':'expense_without_receipt',
      'purchase_at':'2026-07-24T16:00:00+02:00',
      'entered_at':'2026-07-24T16:00:00+02:00',
      'merchant':'Ponyreiten',
      'receipt_total':65.0,
      'holiday_total':65.0,
      'allocated_total':65.0,
      'community_total':0.0,
      'excluded_total':0.0,
      'payment_source':'Simon',
      'status':'active',
      'notes':['Ohne Bon nach Nutzerangabe erfasst','Individuelle Verteilung: Simon 12,50 €, Katrin 12,50 €, Onkel 20,00 €, Tante 20,00 €'],
      'cost_groups':[{
        'id':'custom','label':'Ponyreiten – individuelle Verteilung','amount':65.0,
        'shares':{'Simon':12.5/65,'Katrin':12.5/65,'Onkel':20/65,'Tante':20/65,'Oma':0.0,'Großvater':0.0},
        'allocations':{'Simon':12.5,'Katrin':12.5,'Onkel':20.0,'Tante':20.0,'Oma':0.0,'Großvater':0.0}
      }],
      'items':[{
        'position':1,'name':'Ponyreiten','quantity':1,'unit':'Sammelposition','gross':65.0,'net':65.0,
        'holiday_amount':65.0,'excluded_amount':0.0,'classification':'holiday','cost_group_id':'custom'
      }],
      'payment_credits':[{'person':'Simon','amount':65.0}]
    }
    data['transactions'].append(tx)
    data['updated_at']='2026-07-24T16:00:00+02:00'
    b=data['balances']
    b['total_holiday_expenses']=901.87
    b['total_allocated_expenses']=901.87
    b['total_receipt_expenses']=964.24
    b['total_excluded_expenses']=62.37
    final=[
      ('Simon',212.10,588.79,376.69),
      ('Katrin',245.69,116.56,-129.13),
      ('Onkel',222.06,180.52,-41.54),
      ('Tante',222.02,0.0,-222.02),
      ('Oma',0.0,0.0,0.0),
      ('Großvater',0.0,16.0,16.0)
    ]
    b['persons']=[{'person':p,'charge':c,'payment_credit':pay,'balance':bal} for p,c,pay,bal in final]
    b['suggested_transfers']=[
      {'from':'Katrin','to':'Simon','amount':129.13},
      {'from':'Onkel','to':'Simon','amount':41.54},
      {'from':'Tante','to':'Simon','amount':206.02},
      {'from':'Tante','to':'Großvater','amount':16.0}
    ]
    DATA.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')

status='''# Urlaubskasse Woche 1 – Arbeitsstatus

Stand: 24.07.2026 nach 20 erfassten Vorgängen.

## Verbindliche Regeln

- Woche 1 bleibt geöffnet, bis der Nutzer ausdrücklich den Beginn von Woche 2 nennt.
- Normale Gemeinschaftsausgaben tragen Simon, Katrin, Onkel und Tante zu je 25 %.
- Ein Vorgang kann mehrere Kostenblöcke mit eigenen Verteilungsschlüsseln enthalten.
- Zahlende Person und Kostentragung werden getrennt erfasst.
- Pfand wird wie eine normale Ausgabe behandelt.
- Keine Zahlungsnummern oder Originalbelege im Repo.

## Aktueller Abrechnungsstand

- Verrechnete Ausgaben: 901,87 €
- Beleg-/Ausgabensumme: 964,24 €
- Ausgeschlossen: 62,37 €
- Simon: +376,69 €
- Katrin: −129,13 €
- Onkel: −41,54 €
- Tante: −222,02 €
- Großvater: +16,00 €

## Vorgeschlagener Ausgleich

- Katrin überweist Simon 129,13 €.
- Onkel überweist Simon 41,54 €.
- Tante überweist Simon 206,02 €.
- Tante überweist Großvater 16,00 €.

## Zuletzt verarbeitet

- Ponyreiten, 24.07.2026: 65,00 €, bezahlt von Simon.
- Verteilung: Simon 12,50 €, Katrin 12,50 €, Onkel 20,00 €, Tante 20,00 €.

## Fortsetzung

Neue Belege weiterhin Woche 1 zuordnen, bis der Nutzer ausdrücklich Woche 2 startet. Danach `data/buchungen.json`, `data/protokoll.md`, `data/status.md`, Excel und Website gemeinsam aktualisieren.
'''
STATUS.write_text(status,encoding='utf-8')

protocol=PROTOCOL.read_text(encoding='utf-8')
protocol += '''\n\n---\n\n## AUS-20260724-001 – Ponyreiten\n\n- Datum: 24.07.2026\n- Betrag: **65,00 €**\n- Bezahlt von: Simon\n- Ohne Bon nach Nutzerangabe erfasst\n- Verteilung: Simon **12,50 €**, Katrin **12,50 €**, Onkel **20,00 €**, Tante **20,00 €**\n'''
PROTOCOL.write_text(protocol,encoding='utf-8')
