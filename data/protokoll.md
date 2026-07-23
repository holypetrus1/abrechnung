# Urlaubskasse Woche 1

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
| Simon | 189,89 € | 523,79 € | +333,90 € |
| Katrin | 223,48 € | 116,56 € | -106,92 € |
| Onkel | 192,36 € | 141,70 € | -50,66 € |
| Tante | 192,32 € | 0,00 € | -192,32 € |
| Oma | 0,00 € | 0,00 € | 0,00 € |
| Großvater | 0,00 € | 16,00 € | +16,00 € |

**Verrechnete Ausgaben gesamt:** 798,05 €  
**Beleg- und Ausgabensumme einschließlich ausgeschlossener Positionen:** 856,02 €  
**Ausgeschlossen:** 57,97 €

**Vorgeschlagener Ausgleich:**

- Katrin überweist Simon 106,92 €.
- Onkel überweist Simon 50,66 €.
- Tante überweist Simon 176,32 €.
- Tante überweist Großvater 16,00 €.

---

## Bisherige Vorgänge

| Vorgang | Datum | Händler | Belegsumme | Verrechnet | Ausgeschlossen | Zahlung |
|---|---|---|---:|---:|---:|---|
| BON-20260716-001 | 16.07.2026 | Kaufland | 63,28 € | 34,83 € | 28,45 € | Gemeinschaftskonto Katrin & Simon |
| BON-20260716-002 | 16.07.2026 | BIO COMPANY via Wolt | 38,37 € | 12,82 € | 25,55 € | Gemeinschaftskonto Katrin & Simon |
| GUT-20260716-001 | 16.07.2026 | Wolt / BIO COMPANY | -3,61 € | -3,61 € | 0,00 € | Gemeinschaftskonto Katrin & Simon |
| BON-20260717-001 | 17.07.2026 | Barracuda Fisch | 25,00 € | 25,00 € | 0,00 € | Simon |
| BON-20260717-002 | 17.07.2026 | BIO COMPANY Rathauscenter | 73,41 € | 69,44 € | 3,97 € | Gemeinschaftskonto Katrin & Simon |
| BON-20260718-001 | 18.07.2026 | Netto Marken-Discount | 71,43 € | 71,43 € | 0,00 € | Gemeinschaftskonto Katrin & Simon |
| AUS-20260718-001 | 18.07.2026 | Hofladen Marmelade & more | 10,00 € | 10,00 € | 0,00 € | Simon |
| BON-20260720-001 | 20.07.2026 | Gut Kerkow Fleischmanufaktur | 116,22 € | 116,22 € | 0,00 € | Simon |
| BON-20260720-002 | 20.07.2026 | Lidl Angermünde | 128,80 € | 128,80 € | 0,00 € | Simon |
| BON-20260720-003 | 20.07.2026 | REWE Angermünde | 48,16 € | 48,16 € | 0,00 € | Simon |
| AUS-20260720-001 | 20.07.2026 | Gut Kerkow Bauernmarkt | 48,23 € | 48,23 € | 0,00 € | Gemeinschaftskonto Katrin & Simon |
| BON-20260716-003 | 16.07.2026 | BIO COMPANY Turmstraße | 24,74 € | 24,74 € | 0,00 € | Onkel |
| BON-20260716-004 | 16.07.2026 | E-Center Berlin-Moabit | 81,96 € | 81,96 € | 0,00 € | Onkel |
| AUS-20260721-001 | 21.07.2026 | REWE | 35,00 € | 35,00 € | 0,00 € | Onkel |
| AUS-20260721-002 | 21.07.2026 | Bezahlung Großvater | 16,00 € | 16,00 € | 0,00 € | Großvater |
| BON-20260723-001 | 23.07.2026 | Frischemarkt Boitzenburg | 59,03 € | 59,03 € | 0,00 € | Simon |
| AUS-20260721-003 | 21.07.2026 | Tierpark Angermünde | 20,00 € | 20,00 € | 0,00 € | Simon |

---

## Neu erfasst am 23.07.2026

- **Frischemarkt Boitzenburg:** Bon vom 23.07.2026 über 59,03 €, vollständig Gemeinschaft, bezahlt von Simon.
- **Tierpark Angermünde:** Ausgabe ohne Bon vom Dienstag, 21.07.2026, über 20,00 €, vollständig Gemeinschaft, bezahlt von Simon.

Die beiden neuen Ausgaben ergeben zusammen **79,03 €**.

## Offener Vorgang

- `BON-20260717-001` – Barracuda Fisch, Matjesfilets 25,00 €; weiterhin als Sammelposition, bis der Originalbon vorliegt.
