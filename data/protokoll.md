# Urlaubskasse Woche 1

**Stand:** 18.07.2026, 14:16:28 Uhr  
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
| Simon | 34,62 € | 81,74 € | +47,12 € |
| Katrin | 34,62 € | 56,74 € | +22,12 € |
| Onkel | 34,62 € | 0,00 € | −34,62 € |
| Tante | 34,62 € | 0,00 € | −34,62 € |
| Oma | 0,00 € | 0,00 € | 0,00 € |
| Großvater | 0,00 € | 0,00 € | 0,00 € |

**Anrechenbare Urlaubsausgaben gesamt:** 138,48 €

**Vorgeschlagener Ausgleich:**

- Onkel überweist Simon 34,62 €.
- Tante überweist Simon 12,50 €.
- Tante überweist Katrin 22,12 €.

---

## Bisherige Vorgänge

| Vorgang | Datum | Händler | Belegsumme | Urlaub | Ausgeschlossen | Zahlung |
|---|---|---|---:|---:|---:|---|
| BON-20260716-001 | 16.07.2026 | Kaufland | 63,28 € | 34,83 € | 28,45 € | Gemeinschaftskonto Katrin & Simon |
| BON-20260716-002 | 16.07.2026 | BIO COMPANY via Wolt | 38,37 € | 12,82 € | 25,55 € | Gemeinschaftskonto Katrin & Simon |
| GUT-20260716-001 | 16.07.2026 | Wolt / BIO COMPANY | −3,61 € | −3,61 € | 0,00 € | Gemeinschaftskonto Katrin & Simon |
| BON-20260717-001 | 17.07.2026 | Barracuda Fisch | 25,00 € | 25,00 € | 0,00 € | Simon |
| BON-20260717-002 | 17.07.2026 | BIO COMPANY Rathauscenter | 73,41 € | 69,44 € | 3,97 € | Gemeinschaftskonto Katrin & Simon |

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

## Änderungsprotokoll

1. **16.07.2026 – Einrichtung und Kaufland:** Regeln angelegt, Kaufland-Bon aufgenommen und nach Nutzerkorrektur beide Feta ausgeschlossen sowie Harzbube Handkäse einbezogen.
2. **16.07.2026 – Wolt:** BIO-COMPANY-Rechnung aufgenommen; nur Quark, Kinder-Äpfel und Linsenchips als Urlaub markiert. Servicegebühr und Rabatt anteilig verteilt; Apfel-Gutschrift von −3,61 € zugeordnet.
3. **17.07.2026 – Barracuda Fisch:** Matjesfilets über 25,00 € vorläufig als von Simon bezahlte Urlaubsausgabe aufgenommen; Originalbon steht aus.
4. **18.07.2026 – BIO COMPANY Rathauscenter:** Bon über 73,41 € mit 20 Positionen aufgenommen. Laugenbrezel, Saatenbrötchen und Dinkel-Früchtebrötchen ausgeschlossen; Bon-Rabatt proportional verteilt.
5. **18.07.2026 – Salden:** Gesamtstand auf 138,48 € und Belastung je zahlendem Erwachsenen auf 34,62 € aktualisiert.
