import json
from pathlib import Path

DATA=Path('data/buchungen.json'); STATUS=Path('data/status.md'); PROTOCOL=Path('data/protokoll.md')
ID='BON-20260723-002'
data=json.loads(DATA.read_text(encoding='utf-8'))
if ID not in {t['id'] for t in data['transactions']}:
    tx={
      'id':ID,'type':'receipt','purchase_at':'2026-07-23T13:41:00+02:00','entered_at':'2026-07-23T14:10:00+02:00',
      'merchant':'Netto Marken-Discount Gramzow','location':'Schulzenstraße 30, 17291 Gramzow',
      'receipt_total':16.44,'holiday_total':12.04,'allocated_total':12.04,'community_total':12.04,'excluded_total':4.40,
      'payment_source':'Onkel','status':'active','notes':['Zeitschrift über 4,40 € ausgeschlossen','Übrige Positionen vollständig Gemeinschaft'],
      'cost_groups':[{'id':'community','label':'Gemeinschaft','amount':12.04,'shares':{'Simon':0.25,'Katrin':0.25,'Onkel':0.25,'Tante':0.25,'Oma':0.0,'Großvater':0.0},'allocations':{'Simon':3.01,'Katrin':3.01,'Onkel':3.01,'Tante':3.01,'Oma':0.0,'Großvater':0.0}}],
      'items':[
        {'position':1,'name':'Zeitschriften 7 %','quantity':1,'unit':'Stk.','gross':4.40,'net':4.40,'holiday_amount':0.0,'excluded_amount':4.40,'classification':'excluded'},
        {'position':2,'name':'GL Frische Butter 250 g','quantity':1,'unit':'Packung','gross':1.89,'net':1.89,'holiday_amount':1.89,'excluded_amount':0.0,'classification':'holiday','cost_group_id':'community'},
        {'position':3,'name':'Kartoffeln blau Pfanni 2,5 kg','quantity':1,'unit':'Packung','gross':2.99,'net':2.99,'holiday_amount':2.99,'excluded_amount':0.0,'classification':'holiday','cost_group_id':'community'},
        {'position':4,'name':'Lieblings Avocado','quantity':3,'unit':'Stk.','unit_price':1.79,'gross':5.37,'net':5.37,'holiday_amount':5.37,'excluded_amount':0.0,'classification':'holiday','cost_group_id':'community'},
        {'position':5,'name':'Bio Heidelbeeren 125 g','quantity':1,'unit':'Packung','gross':1.79,'net':1.79,'holiday_amount':1.79,'excluded_amount':0.0,'classification':'holiday','cost_group_id':'community'}],
      'payment_credits':[{'person':'Onkel','amount':12.04}]
    }
    data['transactions'].append(tx)
    data['updated_at']='2026-07-23T14:10:00+02:00'
    b=data['balances']; b['total_holiday_expenses']=810.09; b['total_allocated_expenses']=810.09; b['total_receipt_expenses']=872.46; b['total_excluded_expenses']=62.37
    final=[('Simon',192.90,523.79,330.89),('Katrin',226.49,116.56,-109.93),('Onkel',195.37,153.74,-41.63),('Tante',195.33,0.0,-195.33),('Oma',0.0,0.0,0.0),('Großvater',0.0,16.0,16.0)]
    b['persons']=[{'person':p,'charge':c,'payment_credit':pay,'balance':bal} for p,c,pay,bal in final]
    b['suggested_transfers']=[{'from':'Katrin','to':'Simon','amount':109.93},{'from':'Onkel','to':'Simon','amount':41.63},{'from':'Tante','to':'Simon','amount':179.33},{'from':'Tante','to':'Großvater','amount':16.0}]
    DATA.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')

status='''# Urlaubskasse Woche 1 – Arbeitsstatus

Stand: 23.07.2026 nach 18 erfassten Vorgängen.

## Verbindliche Regeln

- Woche 1 bleibt geöffnet, bis der Nutzer ausdrücklich den Beginn von Woche 2 nennt.
- Normale Gemeinschaftsausgaben tragen Simon, Katrin, Onkel und Tante zu je 25 %.
- Ein Vorgang kann mehrere Kostenblöcke mit eigenen Verteilungsschlüsseln enthalten.
- Zahlende Person und Kostentragung werden getrennt erfasst.
- Pfand wird wie eine normale Ausgabe behandelt.
- Keine Zahlungsnummern oder Originalbelege im Repo.

## Aktueller Abrechnungsstand

- Verrechnete Ausgaben: 810,09 €
- Beleg-/Ausgabensumme: 872,46 €
- Ausgeschlossen: 62,37 €
- Simon: +330,89 €
- Katrin: −109,93 €
- Onkel: −41,63 €
- Tante: −195,33 €
- Großvater: +16,00 €

## Vorgeschlagener Ausgleich

- Katrin überweist Simon 109,93 €.
- Onkel überweist Simon 41,63 €.
- Tante überweist Simon 179,33 €.
- Tante überweist Großvater 16,00 €.

## Zuletzt verarbeitet

- Netto Marken-Discount Gramzow, 23.07.2026: Bon 16,44 €, davon 4,40 € Zeitschrift ausgeschlossen; 12,04 € Gemeinschaft, bezahlt von Onkel.

## Fortsetzung

Neue Belege weiterhin Woche 1 zuordnen, bis der Nutzer ausdrücklich Woche 2 startet. Danach `data/buchungen.json`, `data/protokoll.md`, `data/status.md`, Excel und Website gemeinsam aktualisieren.
'''
STATUS.write_text(status,encoding='utf-8')

protocol=PROTOCOL.read_text(encoding='utf-8')
protocol=protocol.replace('**Stand:** 23.07.2026, 13:41 Uhr','**Stand:** 23.07.2026, 14:10 Uhr') if '**Stand:** 23.07.2026, 13:41 Uhr' in protocol else protocol
protocol += '\n\n---\n\n## BON-20260723-002 – Netto Marken-Discount Gramzow\n\n- Kauf: 23.07.2026, 13:41 Uhr\n- Belegsumme: **16,44 €**\n- Ausgeschlossen: **4,40 €** (Zeitschrift)\n- Gemeinschaftsausgabe: **12,04 €**\n- Bezahlt von: Onkel\n- Verteilung: Simon, Katrin, Onkel und Tante je **3,01 €**\n'
PROTOCOL.write_text(protocol,encoding='utf-8')
