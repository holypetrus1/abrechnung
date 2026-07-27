# Urlaubskasse Woche 2 – Arbeitsstatus

Stand: 27.07.2026, 13:30 Uhr; 2 Vorgänge erfasst.

## Verbindliche Regeln

- Woche 2 ist die aktive Abrechnungsperiode.
- Normale Gemeinschaftsausgaben tragen Simon, Katrin, Hummel W und Hummel M zu je 25 %.
- Haushalte: Simon & Katrin sowie Hummel W & Hummel M.
- Die Standardverteilung erfolgt pro Person, nicht pro Haushalt.
- Ausgaben nur für einen Haushalt werden hälftig auf dessen Mitglieder verteilt; Rundungscent werden dokumentiert.
- Zahlende Person und Kostentragung werden getrennt erfasst.
- Gemeinsame Zahlungskonten werden den beiden Mitgliedern des jeweiligen Haushalts hälftig gutgeschrieben.
- Ein Vorgang kann mehrere Kostenblöcke mit eigenen Verteilungsschlüsseln enthalten.
- Pfand wird wie eine normale Ausgabe behandelt.
- Keine Zahlungsnummern oder Originalbelege im Repository.
- Korrekturen werden nachvollziehbar und append-only dokumentiert.

## Aktive Datenquellen

- `data/buchungen_woche2.json` – erster Woche-2-Vorgang und Grundregeln
- `data/buchungen_woche2_nachtrag.json` – REWE-Vorgang vom 25.07.2026 und aktueller Gesamtsaldo

## Aktueller Abrechnungsstand

- Verrechnete Ausgaben: 183,20 €
- Beleg-/Ausgabensumme: 183,20 €
- Ausgeschlossen: 0,00 €
- Simon: +139,99 €
- Katrin: −43,20 €
- Hummel W: −42,36 €
- Hummel M: −54,43 €

## Vorgeschlagener Ausgleich

- Katrin überweist Simon 43,20 €.
- Hummel W überweist Simon 42,36 €.
- Hummel M überweist Simon 54,43 €.

## Zuletzt verarbeitet

- `BON-20260725-001` – REWE Beelitz-Heilstätten, 25.07.2026, 95,41 €, bezahlt von Simon.
- Laugenstange und Pirulo Watermelo: 1,69 € nur Haushalt Simon & Katrin; Simon 0,85 €, Katrin 0,84 €.
- Restlicher Bon: 93,72 €, je 23,43 € für alle vier Personen.

## Archiv Woche 1

Woche 1 ist abgeschlossen und über die Archivfunktion der Website erreichbar. Der vollständige Datenbestand und die darin eingebettete Abrechnungslogik bleiben unverändert erhalten.

## Fortsetzung

Vor jedem neuen Beleg `data/status.md`, `data/buchungen_woche2.json` und `data/buchungen_woche2_nachtrag.json` lesen. Danach Woche-2-Daten, Protokoll, Status, Website und Excel-Export gemeinsam aktualisieren.
