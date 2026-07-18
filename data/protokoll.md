# Urlaubskasse Woche 1

**Stand:** 18.07.2026, 17:56:24 Uhr  
**Verbindliche Datenquelle:** `data/buchungen.json`

## Standardlogik

- Simon, Katrin, Onkel und Tante tragen laufende Urlaubsausgaben zu je 25 %.
- Oma und Großvater tragen standardmäßig 0 %, da sie die Unterkunft bezahlt haben.
- Zahlende Person oder Zahlungsquelle wird getrennt von der Kostenverteilung erfasst.
- Das Gemeinschaftskonto Katrin & Simon wird hälftig beiden gutgeschrieben.
- Bonweite Rabatte werden anteilig nach Warenwert auf Urlaubs- und Privatpositionen verteilt.
- Einzelpositionen und vollständige Rechendaten stehen in `data/buchungen.json` und im Excel-Export.

## Aktueller Gesamtstand

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

## Bisherige Vorgänge

| Vorgang | Datum | Händler | Belegsumme | Urlaub | Ausgeschlossen | Zahlung |
|---|---|---|---:|---:|---:|---|
| BON-20260716-001 | 16.07.2026 | Kaufland | 63,28 € | 34,83 € | 28,45 € | Gemeinschaftskonto Katrin & Simon |
| BON-20260716-002 | 16.07.2026 | BIO COMPANY via Wolt | 38,37 € | 12,82 € | 25,55 € | Gemeinschaftskonto Katrin & Simon |
| GUT-20260716-001 | 16.07.2026 | Wolt / BIO COMPANY | −3,61 € | −3,61 € | 0,00 € | Gemeinschaftskonto Katrin & Simon |
| BON-20260717-001 | 17.07.2026 | Barracuda Fisch | 25,00 € | 25,00 € | 0,00 € | Simon |
| BON-20260717-002 | 17.07.2026 | BIO COMPANY Rathauscenter | 73,41 € | 69,44 € | 3,97 € | Gemeinschaftskonto Katrin & Simon |
| BON-20260718-001 | 18.07.2026 | Netto Marken-Discount | 71,43 € | 71,43 € | 0,00 € | Gemeinschaftskonto Katrin & Simon |
| AUS-20260718-001 | 18.07.2026 | Hofladen Marmelade & more | 10,00 € | 10,00 € | 0,00 € | Simon |

**Offen:** Der Barracuda-Fisch-Vorgang bleibt bis zum Originalbon als Sammelposition „Matjesfilets“ geführt.

---

## BON-20260717-002 – BIO COMPANY Rathauscenter

- Kauf: 17.07.2026, 09:48:59 Uhr
- Erfasst: 18.07.2026, 14:16:28 Uhr
- Ort: Breite Straße 20, 13187 Berlin
- Warenwert vor Bonus: **80,85 €**
- Bon-Rabatt: **−7,44 €**
- Belegsumme: **73,41 €**
- Nicht für den Urlaub nach Rabatt: **3,97 €**
- Urlaubsausgabe: **69,44 €**
- Zahlung: Gemeinschaftskonto Katrin & Simon
- Zahlungsguthaben: Simon 34,72 €, Katrin 34,72 €

### Positionen

| Pos. | Artikel | Brutto | Rabatt | Netto | Zuordnung |
|---:|---|---:|---:|---:|---|
| 1 | Kembrot | 16,79 € | −1,54 € | 15,25 € | Urlaub |
| 2 | Laugenbrezel | 0,99 € | −0,09 € | 0,90 € | privat |
| 3 | Saatenbrötchen | 1,49 € | −0,14 € | 1,35 € | privat |
| 4 | Dinkel-Früchtebrötchen | 1,89 € | −0,17 € | 1,72 € | privat |
| 5 | Vollkorn Kruste | 5,99 € | −0,55 € | 5,44 € | Urlaub |
| 6 | Gouda jung | 3,25 € | −0,30 € | 2,95 € | Urlaub |
| 7 | Saatenbrot | 5,49 € | −0,51 € | 4,98 € | Urlaub |
| 8 | Hugo | 4,87 € | −0,45 € | 4,42 € | Urlaub |
| 9 | Allgäuer Tilsiter | 3,01 € | −0,28 € | 2,73 € | Urlaub |
| 10 | Schweizer Alpiko | 5,92 € | −0,54 € | 5,38 € | Urlaub |
| 11 | Koriander Käse | 5,26 € | −0,48 € | 4,78 € | Urlaub |
| 12 | Brie Petit Norma | 3,54 € | −0,33 € | 3,21 € | Urlaub |
| 13 | Brie Petit Norma | 3,76 € | −0,35 € | 3,41 € | Urlaub |
| 14 | Emmentaler | 4,96 € | −0,46 € | 4,50 € | Urlaub |
| 15 | Griekenschmied | 4,54 € | −0,42 € | 4,12 € | Urlaub |
| 16 | Rote Zwiebeln, 0,546 kg | 1,63 € | −0,15 € | 1,48 € | Urlaub |
| 17 | Salatgurke | 1,99 € | −0,18 € | 1,81 € | Urlaub |
| 18 | Rucola-Salat | 1,99 € | −0,18 € | 1,81 € | Urlaub |
| 19 | Radieschen | 1,99 € | −0,18 € | 1,81 € | Urlaub |
| 20 | Ramiro Tüte | 1,50 € | −0,14 € | 1,36 € | Urlaub |

Der Rabatt von 7,44 € wurde proportional nach dem Bruttowarenwert verteilt. Auf die drei Privatpositionen entfallen zusammen 0,40 € Rabatt.

---

## BON-20260718-001 – Netto Marken-Discount

- Kauf: 18.07.2026 16:57 Uhr
- Belegsumme: **71,43 €**
- Urlaubsausgabe: **71,43 €**
- Ausgeschlossen: **0,00 €**
- Zahlung: Gemeinschaftskonto Katrin & Simon
- Zahlungsguthaben: Simon 35,72 €, Katrin 35,71 €

### Positionen

| Pos. | Artikel | Brutto | Netto | Zuordnung |
|---:|---|---:|---:|---|
| 1 | Grey Grauburgunder 0,75 l | 4,99 € | 4,99 € | Urlaub |
| 2 | Macho Mas Tinto 0,75 l | 5,99 € | 5,99 € | Urlaub |
| 3 | Coca-Cola 1 × 1,25 l | 1,59 € | 1,59 € | Urlaub |
| 4 | EW-Pfand 0,25 EUR | 0,25 € | 0,25 € | Urlaub |
| 5 | Coca-Cola Zero 1 × 1,25 l | 1,59 € | 1,59 € | Urlaub |
| 6 | EW-Pfand 0,25 EUR | 0,25 € | 0,25 € | Urlaub |
| 7 | BioBio Joghurt 3,8 % 500 g | 2,06 € | 2,06 € | Urlaub |
| 8 | BioBio Eier 10 St. | 7,18 € | 7,18 € | Urlaub |
| 9 | Discount Cookies sortiert 200 g | 1,79 € | 1,79 € | Urlaub |
| 10 | BioBio Beeren sortiert 300 g | 7,38 € | 7,38 € | Urlaub |
| 11 | Mikado sortiert 75 g | 1,49 € | 1,49 € | Urlaub |
| 12 | Artikelrabatt | -0,20 € | -0,20 € | Urlaub |
| 13 | Bautz'ner Senf mittelscharf 200 ml | 0,55 € | 0,55 € | Urlaub |
| 14 | BioBio Gouda 200 g | 1,61 € | 1,61 € | Urlaub |
| 15 | Junge Erbsen 1 kg | 2,39 € | 2,39 € | Urlaub |
| 16 | Langnese Kids Mix 393 ml | 4,49 € | 4,49 € | Urlaub |
| 17 | Lindt Chocolate Macadamia Sea Salt 150 g | 2,99 € | 2,99 € | Urlaub |
| 18 | Zetti Schokolade 100 g | 2,49 € | 2,49 € | Urlaub |
| 19 | Schokolade 100 g | 1,89 € | 1,89 € | Urlaub |
| 20 | Schokolierte Mini-Schaumküsse 266 g | 2,49 € | 2,49 € | Urlaub |
| 21 | Discount Schoko-Kekse sortiert 125 g | 1,59 € | 1,59 € | Urlaub |
| 22 | Mini Laugenmix 763 g | 3,49 € | 3,49 € | Urlaub |
| 23 | Gratis-Aktion Mini Laugenmix | -3,49 € | -3,49 € | Urlaub |
| 24 | Bio Naturland Speisezwiebeln 1 kg | 1,97 € | 1,97 € | Urlaub |
| 25 | Bio Paprika Mix 400 g | 2,06 € | 2,06 € | Urlaub |
| 26 | Eisbergsalat | 0,99 € | 0,99 € | Urlaub |
| 27 | Mairübchen | 1,29 € | 1,29 € | Urlaub |
| 28 | Preisänderung Mairübchen | -0,65 € | -0,65 € | Urlaub |
| 29 | Mini-Romanasalat GS | 0,65 € | 0,65 € | Urlaub |
| 30 | Bio Gurken | 2,50 € | 2,50 € | Urlaub |
| 31 | Bio Knoblauch 150 g | 1,34 € | 1,34 € | Urlaub |
| 32 | Radieschen | 0,65 € | 0,65 € | Urlaub |
| 33 | Dill 25 g | 0,99 € | 0,99 € | Urlaub |
| 34 | Bio Naturland Kräutertopf | 3,04 € | 3,04 € | Urlaub |
| 35 | Johannisbeeren | 2,69 € | 2,69 € | Urlaub |
| 36 | Jagdwurst 350 g | 2,79 € | 2,79 € | Urlaub |
| 37 | 5 % Rabatt Warenkorb | -3,73 € | -3,73 € | Urlaub |

---

## AUS-20260718-001 – Hofladen Marmelade & more

- Kauf: 18.07.2026; genaue Uhrzeit nicht angegeben
- Belegsumme: **10,00 €**
- Urlaubsausgabe: **10,00 €**
- Ausgeschlossen: **0,00 €**
- Zahlung: Simon
- Zahlungsguthaben: Simon 10,00 €

### Positionen

| Pos. | Artikel | Brutto | Netto | Zuordnung |
|---:|---|---:|---:|---|
| 1 | Hofladen Marmelade & more | 10,00 € | 10,00 € | Urlaub |

---

## Änderungsprotokoll

1. **16.07.2026 – Einrichtung und Kaufland:** Regeln angelegt, Kaufland-Bon aufgenommen und nach Nutzerkorrektur beide Feta ausgeschlossen sowie Harzbube Handkäse einbezogen.
2. **16.07.2026 – Wolt:** BIO-COMPANY-Rechnung aufgenommen; nur Quark, Kinder-Äpfel und Linsenchips als Urlaub markiert. Servicegebühr und Rabatt anteilig verteilt; Apfel-Gutschrift von −3,61 € zugeordnet.
3. **17.07.2026 – Barracuda Fisch:** Matjesfilets über 25,00 € vorläufig als von Simon bezahlte Urlaubsausgabe aufgenommen; Originalbon steht aus.
4. **18.07.2026 – BIO COMPANY Rathauscenter:** Bon über 73,41 € mit 20 Positionen aufgenommen. Laugenbrezel, Saatenbrötchen und Dinkel-Früchtebrötchen ausgeschlossen; Bon-Rabatt proportional verteilt.
5. **18.07.2026 – Salden:** Gesamtstand auf 138,48 € und Belastung je zahlendem Erwachsenen auf 34,62 € aktualisiert.
6. **18.07.2026 – Netto Marken-Discount:** Bon über 71,43 € vollständig und ohne Abzüge als Urlaubsausgabe aufgenommen; Zahlung vom Gemeinschaftskonto hälftig gutgeschrieben.
7. **18.07.2026 – Hofladen:** Ausgabe ohne Bon über 10,00 € als von Simon bezahlt aufgenommen.
8. **18.07.2026 – Salden:** Gesamtstand auf 219,91 € aktualisiert; Rundungscent der Belastung Tante zugeordnet.
