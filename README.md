# Urlaubskasse

Dieses Repository ist der verbindliche, versionierte Datenspeicher für die Urlaubsabrechnung.

## Aktive Abrechnung

Seit dem 26.07.2026 ist **Woche 2** aktiv. Die vier Teilnehmenden sind Simon, Katrin, Hummel W und Hummel M. Simon und Katrin bilden einen Haushalt; Hummel W und Hummel M bilden den Haushalt „Hummeln“.

Normale Gemeinschaftsausgaben werden standardmäßig zu je 25 % auf alle vier Personen verteilt. Die Haushaltszuordnung dient insbesondere der Zuordnung gemeinsamer Zahlungskonten und ersetzt nicht die personenbezogene Kostenverteilung.

## Weboberfläche

Die statische Familienansicht wird über GitHub Pages veröffentlicht:

- Woche 2 erscheint als saubere Standardansicht.
- Woche 1 ist über den dezenten Archiv-Klick im Kopfbereich erreichbar.
- Protokoll, Einkäufe, Salden und Ausgleich werden für die ausgewählte Woche angezeigt.
- Der Abschluss-Excel-Export von Woche 1 bleibt im Archiv verfügbar.

Die Oberfläche ist ausschließlich lesend. Konzept und technische Struktur sind unter `docs/web-konzept.md` dokumentiert.

## Maßgebliche Dateien

### Woche 2 – aktiv

- `data/buchungen_woche2.json` – vollständiger maschinenlesbarer Datenbestand mit Regeln, Haushalten, Bons, Einzelpositionen und Salden
- `data/protokoll_woche2.md` – lesbare chronologische Dokumentation
- `data/status.md` – kompakter Übergabestand für die Fortsetzung in einem neuen Chat

### Woche 1 – archiviert

- `data/buchungen.json` – eingefrorener vollständiger Datenbestand einschließlich Abrechnungslogik
- `data/protokoll.md` – konsolidiertes Abschlussprotokoll
- `exports/Urlaubskasse_Woche1.xlsx` – finaler Excel-Export
- `archive/woche1/README.md` – Archivhinweise und Abschlusswerte

## Arbeitsweise

Die Datenerfassung erfolgt ausschließlich im Chat. Vor einem neuen Eintrag werden `data/status.md` und `data/buchungen_woche2.json` eingelesen. Danach werden Daten, Protokoll, Status, Website und der Excel-Export gemeinsam aktualisiert und als neuer Commit gespeichert.

## Datenschutz

- Keine Originalbelege im Repository
- Keine Kreditkarten-, Konto-, Gutschein- oder sonstigen Zahlungsnummern
- Zahlungsquellen nur als neutrale Bezeichnungen
- Personenbezeichnungen bleiben in der vereinbarten anonymisierten Form
