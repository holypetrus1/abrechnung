# Urlaubskasse Woche 1

**Stand:** 17.07.2026, 11:04:53 Uhr  
**Verbindliche Datenquelle:** `data/buchungen.json`

## Standardlogik

- Simon, Katrin, Onkel und Tante tragen normale laufende Urlaubsausgaben zu je 25 %.
- Oma und Großvater tragen standardmäßig 0 %, da sie die Unterkunft bezahlt haben.
- Kinder werden nicht als eigene Abrechnungskonten belastet.
- Die zahlende Person beziehungsweise Zahlungsquelle wird getrennt von der Kostenverteilung erfasst.
- Zahlungen vom Gemeinschaftskonto Simon/Katrin werden hälftig beiden gutgeschrieben; Rundungscent werden dokumentiert.
- Pfand und Leergut werden wie normale Ausgaben beziehungsweise Gutschriften behandelt.
- Kaufdatum und Erfassungszeitpunkt werden getrennt gespeichert.
- Korrekturen bleiben im Änderungsprotokoll sichtbar.
- Kreditkarten-, Konto-, Gutschein- und sonstige Zahlungsnummern werden nicht im Repo gespeichert.

## Aktueller Gesamtstand

| Person | Belastung | Zahlungsguthaben | Saldo |
|---|---:|---:|---:|
| Simon | 17,26 € | 47,02 € | +29,76 € |
| Katrin | 17,26 € | 22,02 € | +4,76 € |
| Onkel | 17,26 € | 0,00 € | −17,26 € |
| Tante | 17,26 € | 0,00 € | −17,26 € |
| Oma | 0,00 € | 0,00 € | 0,00 € |
| Großvater | 0,00 € | 0,00 € | 0,00 € |

**Anrechenbare Urlaubsausgaben gesamt:** 69,04 €

**Vorgeschlagener Ausgleich:**

- Onkel überweist Simon 17,26 €.
- Tante überweist Simon 12,50 €.
- Tante überweist Katrin 4,76 €.

---

## BON-20260716-001 – Kaufland

- Kauf: 16.07.2026, 08:03 Uhr
- Erfasst: 16.07.2026, 20:41:17 Uhr
- Händler: Kaufland, Breite Straße 19–21 A, Berlin
- Belegsumme: **63,28 €**
- Nicht für den Urlaub: **28,45 €**
- Urlaubsausgabe: **34,83 €**
- Zahlung: Gemeinschaftskonto Katrin & Simon
- Zahlungsguthaben: Simon 17,42 €, Katrin 17,41 €
- Status: korrigiert; beide Feta ausgeschlossen, Harzbube Handkäse enthalten

### Positionen

| Pos. | Artikel | Netto | Urlaub | Ausgeschlossen | Status |
|---:|---|---:|---:|---:|---|
| 1 | KBio Naturjoghurt, 3 Stück | 5,97 € | 1,99 € | 3,98 € | teilweise; 2 Stück ausgeschlossen |
| 2 | KBio ESL-Milch 3,8 %, 2 Stück | 2,29 € | 2,29 € | 0,00 € | Urlaub |
| 3 | KBio Bio-Frischkäse, 2 Stück | 2,06 € | 0,00 € | 2,06 € | ausgeschlossen |
| 4 | KBio Leinsamen ganz | 1,55 € | 0,00 € | 1,55 € | ausgeschlossen |
| 5 | Lindt Lindor Tafel | 2,79 € | 2,79 € | 0,00 € | Urlaub |
| 6 | KBio Bananen | 1,46 € | 0,00 € | 1,46 € | ausgeschlossen |
| 7 | Katjes | 0,89 € | 0,89 € | 0,00 € | Urlaub |
| 8 | KBio Bandnudeln 500 g, 2 Packungen | 2,32 € | 2,32 € | 0,00 € | Urlaub |
| 9 | KBio Äpfel rot 1 kg | 3,49 € | 3,49 € | 0,00 € | Urlaub |
| 10 | KBio Feta, 2 Packungen | 4,30 € | 0,00 € | 4,30 € | ausgeschlossen |
| 11 | LM Penne Rigate | 1,19 € | 0,00 € | 1,19 € | ausgeschlossen |
| 12 | LM Mezzi Rigatoni | 1,19 € | 0,00 € | 1,19 € | ausgeschlossen |
| 13 | KBio Fusilli Vollkorn, 2 Packungen | 1,36 € | 1,36 € | 0,00 € | Urlaub |
| 14 | KBio Tomaten 500 g | 2,79 € | 2,79 € | 0,00 € | Urlaub |
| 15 | K-free Schlagsahne | 0,99 € | 0,00 € | 0,99 € | ausgeschlossen |
| 16 | Leibniz Black'n White | 1,99 € | 0,00 € | 1,99 € | ausgeschlossen |
| 17 | KLC Chips leicht gesalzen | 1,39 € | 1,39 € | 0,00 € | Urlaub |
| 18 | KLC American Cookies | 1,29 € | 0,00 € | 1,29 € | ausgeschlossen |
| 19 | K-Bio Honig cremig | 1,99 € | 0,00 € | 1,99 € | ausgeschlossen |
| 20 | Harzbube Handkäse | 1,99 € | 1,99 € | 0,00 € | Urlaub; nach Korrektur enthalten |
| 21 | St. Mang Limburger | 1,89 € | 1,89 € | 0,00 € | Urlaub |
| 22 | KBio Birnen 500 g | 2,23 € | 2,23 € | 0,00 € | Urlaub |
| 23 | KBio Zitronen 500 g, 2 Packungen | 3,98 € | 0,00 € | 3,98 € | ausgeschlossen |
| 24 | Avocado RTE, 2 Stück | 1,79 € | 0,00 € | 1,79 € | ausgeschlossen |
| 25 | Romatomaten 500 g | 2,79 € | 2,79 € | 0,00 € | Urlaub |
| 26 | Apostels Zaziki | 0,69 € | 0,00 € | 0,69 € | ausgeschlossen |
| 27 | KBio Kartoffeln 1,5 kg, 2 Packungen | 4,98 € | 4,98 € | 0,00 € | Urlaub |
| 28 | Leergut Mopro | −0,15 € | −0,15 € | 0,00 € | Urlaubsgutschrift |
| 29 | KBio Möhren 1 kg | 1,79 € | 1,79 € | 0,00 € | Urlaub |

---

## BON-20260716-002 – BIO COMPANY via Wolt

- Kauf/Lieferung: 16.07.2026, 14:16 Uhr
- Erfasst: 16.07.2026, 20:54:50 Uhr
- Rechnungssumme: **38,37 €**
- Nicht für den Urlaub: **25,55 €**
- Urlaubsausgabe vor Gutschrift: **12,82 €**
- Zahlung: Gemeinschaftskonto Katrin & Simon
- Zahlungsguthaben: Simon 6,41 €, Katrin 6,41 €
- Für den Urlaub zählen nur Quark, Kinder-Äpfel und Linsenchips.
- Servicegebühr und Bestellrabatt wurden anteilig nach Warenwert verteilt.

### Positionen

| Pos. | Artikel | Netto | Urlaub | Ausgeschlossen | Status |
|---:|---|---:|---:|---:|---|
| 1 | Schrozberg Kefir, 2 Stück | 3,58 € | 0,00 € | 3,58 € | ausgeschlossen |
| 2 | Pfand Kefir, 2 Stück | 0,30 € | 0,00 € | 0,30 € | ausgeschlossen |
| 3 | Paul Söbbeke Bio Magerquark, 2 Stück | 3,98 € | 3,98 € | 0,00 € | Urlaub |
| 4 | Salatgurke | 1,99 € | 0,00 € | 1,99 € | ausgeschlossen |
| 5 | Söbbeke Speisequark 20 %, 2 Stück | 3,58 € | 3,58 € | 0,00 € | Urlaub |
| 6 | La Selva Polpa, 5 Stück | 16,45 € | 0,00 € | 16,45 € | ausgeschlossen |
| 7 | Kinder-Apfel Elstar | 3,99 € | 3,99 € | 0,00 € | Urlaub; Gutschrift separat |
| 8 | BIO COMPANY Linsenchips Falafel | 1,89 € | 1,89 € | 0,00 € | Urlaub |
| 9 | BIO COMPANY Grissini Sesam | 1,99 € | 0,00 € | 1,99 € | ausgeschlossen |
| 10 | Dinkel-Knusperbrezeln | 2,49 € | 0,00 € | 2,49 € | ausgeschlossen |
| 11–14 | Lieferung und vollständige Lieferrabatte | 0,00 € netto | 0,00 € | 0,00 € | neutralisiert |
| 15 | Servicegebühr 7 % | 3,56 € | 1,19 € | 2,37 € | anteilig |
| 16 | Servicegebühr 19 % | 0,03 € | 0,01 € | 0,02 € | anteilig |
| 17 | Wolt+ Servicegebühr-Rabatt 7 % | −1,43 € | −0,48 € | −0,95 € | anteilig |
| 18 | Wolt+ Servicegebühr-Rabatt 19 % | −0,01 € | 0,00 € | −0,01 € | ausgeschlossen |
| 19 | Bestellrabatt | −4,02 € | −1,34 € | −2,68 € | anteilig |

---

## GUT-20260716-001 – Gutschrift Kinder-Äpfel

- Ausgestellt: 16.07.2026, 14:58 Uhr
- Betrag: **−3,61 €**
- Vollständig der zuvor als Urlaub erfassten Kinder-Apfel-Position zugeordnet
- Gutschrift auf das Gemeinschaftskonto
- Minderung des Zahlungsguthabens: Simon −1,81 €, Katrin −1,80 €

**Netto-Urlaubsausgabe aus Wolt-Rechnung und Gutschrift:** 9,21 €

---

## BON-20260717-001 – Barracuda Fisch

- Kauf: 17.07.2026
- Erfasst: 17.07.2026, 11:04:53 Uhr
- Belegsumme: **25,00 €**
- Urlaubsausgabe: **25,00 €**
- Zahlung: Simon
- Zahlungsguthaben: Simon 25,00 €
- Status: vorläufig erfasst; Originalbon folgt
- Derzeit als eine Sammelposition geführt und nach Eingang des Bons positionsgenau zu ergänzen.

### Positionen

| Pos. | Artikel | Netto | Urlaub | Ausgeschlossen | Status |
|---:|---|---:|---:|---:|---|
| 1 | Matjesfilets | 25,00 € | 25,00 € | 0,00 € | Urlaub; vorläufige Sammelposition |

---

## Änderungsprotokoll

1. **16.07.2026, 20:41:17 Uhr – Einrichtung:** Regeln und personenscharfe Konten angelegt.
2. **16.07.2026, 20:41:17 Uhr – Bon erfasst:** Kaufland-Bon mit 29 Positionen aufgenommen.
3. **16.07.2026, 20:41:17 Uhr – Ausschlüsse:** Genannte Nicht-Urlaubspositionen und artikelbezogene Rabatte zugeordnet.
4. **16.07.2026, 20:41:17 Uhr – Erstinterpretation:** „Käse“ zunächst als Harzbube Handkäse interpretiert.
5. **16.07.2026, 20:45:14 Uhr – Korrektur:** Beide Feta ausgeschlossen; Harzbube Handkäse als Urlaubsausgabe aufgenommen. Urlaubssumme Bon 1 von 32,84 € auf 34,83 € korrigiert.
6. **16.07.2026, 20:54:50 Uhr – Wolt-Rechnung:** Rechnung mit 19 Positionen aufgenommen; nur Quark, Kinder-Äpfel und Linsenchips als Urlaub markiert.
7. **16.07.2026, 20:54:50 Uhr – Verteilung:** Servicegebühr und Bestellrabatt proportional nach Warenwert verteilt.
8. **16.07.2026, 20:54:50 Uhr – Gutschrift:** Apfel-Gutschrift von −3,61 € vollständig dem Urlaub zugeordnet.
9. **16.07.2026, 20:54:50 Uhr – Salden:** Gesamtstand auf 44,04 € aktualisiert; vorgeschlagener Ausgleich zweimal 11,01 €.
10. **17.07.2026, 11:04:53 Uhr – Vorläufiger Bon:** Barracuda Fisch mit Matjesfilets über 25,00 € als von Simon bezahlte Urlaubsausgabe aufgenommen; Originalbon steht noch aus.
11. **17.07.2026, 11:04:53 Uhr – Salden:** Gesamtstand auf 69,04 € aktualisiert; Belastung je zahlendem Erwachsenen 17,26 €.
