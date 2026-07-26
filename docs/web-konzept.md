# Konzept: Weboberfläche Urlaubskasse

## Ziel

Die Website ist ein zusätzlicher, ausschließlich lesender Ausgabekanal für die Familienmitglieder. Die Datenerfassung und alle Korrekturen erfolgen weiterhin nur im Chat. Das Repository bleibt der verbindliche Datenbestand.

## Wochenstruktur

- **Woche 2** ist die aktive Standardansicht.
- **Woche 1** ist abgeschlossen und über einen dezenten Archiv-Klick im Kopfbereich erreichbar.
- Die Archivansicht lädt den eingefrorenen vollständigen Datenbestand, das Abschlussprotokoll und den finalen Excel-Export von Woche 1.
- Neue Belege werden ausschließlich im getrennten Datenbestand von Woche 2 erfasst.

## Aufbau

Die Oberfläche besteht je ausgewählter Woche aus vier klar getrennten Ansichten:

1. **Protokoll** – rendert das zur Woche gehörende Markdown-Protokoll als gut lesbare Chronik.
2. **Einkäufe** – zeigt alle Vorgänge mit Datum, anrechenbarer Summe und Zahlungsquelle. Einzelpositionen und Detailberechnungen werden bewusst nicht angezeigt.
3. **Excel** – stellt vorhandene Excel-Exporte direkt zum Download bereit. Für eine neu gestartete Woche bleibt der Bereich bis zum ersten Export deaktiviert.
4. **Ausgleich** – zeigt die aktuellen Salden aller Abrechnungskonten und die vorgeschlagenen Überweisungen.

## Technische Architektur

- reine statische Website ohne Datenbank, Login oder Bearbeitungsfunktionen
- `index.html`, `styles.css` und `app.js` bilden die Oberfläche
- `app.js` wählt anhand des Parameters `?woche=1` zwischen aktiver Woche und Archiv
- Woche 2: `data/buchungen_woche2.json` und `data/protokoll_woche2.md`
- Woche 1: `data/buchungen.json`, `data/protokoll.md` und `exports/Urlaubskasse_Woche1.xlsx`
- responsive Darstellung für Smartphone, Tablet und Desktop
- keine externen JavaScript-Bibliotheken und keine externen Trackingdienste

## Aktualisierungslogik Woche 2

Bei neuen Belegen werden gemeinsam aktualisiert:

- `data/buchungen_woche2.json`
- `data/status.md`
- `data/protokoll_woche2.md`
- ein Woche-2-Excel-Export, sobald der erste Vorgang vorliegt

Der Datenbestand von Woche 1 bleibt dabei unverändert.

## Veröffentlichung

Der Workflow `.github/workflows/pages.yml` baut aus den Dateien im Hauptzweig ein GitHub-Pages-Artefakt. Jede Änderung an Website, aktiven Daten oder Exporten veröffentlicht dadurch automatisch den aktuellen Lesestand.

## Datenschutz

Die bestehende Datenschutzlogik des Repositories bleibt unverändert: keine Originalbelege sowie keine Kreditkarten-, Konto-, Gutschein- oder sonstigen Zahlungsnummern. Die Website zeigt nur die vereinbarten anonymisierten Personenbezeichnungen und Zahlungsquellen.
