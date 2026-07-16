# Konzept: Weboberfläche Urlaubskasse Woche 1

## Ziel

Die Website ist ein zusätzlicher, ausschließlich lesender Ausgabekanal für die Familienmitglieder. Die Datenerfassung und alle Korrekturen erfolgen weiterhin nur im Chat. Das Repository bleibt der verbindliche Datenbestand.

## Aufbau

Die Oberfläche besteht aus vier klar getrennten Ansichten:

1. **Protokoll** – rendert `data/protokoll.md` als gut lesbare Chronik.
2. **Einkäufe** – zeigt alle Vorgänge in einer langen Liste mit Datum, für die Urlaubskasse anrechenbarer Summe und Zahlungsquelle. Einzelpositionen und Detailberechnungen werden bewusst nicht angezeigt.
3. **Excel** – stellt `exports/Urlaubskasse_Woche1.xlsx` direkt zum Download bereit.
4. **Ausgleich** – zeigt die aktuellen Salden aller Abrechnungskonten und die vorgeschlagenen Überweisungen.

## Technische Architektur

- reine statische Website ohne Datenbank, Login oder Bearbeitungsfunktionen
- `index.html`, `styles.css` und `app.js` bilden die Oberfläche
- `app.js` liest ausschließlich die statischen Dateien `data/buchungen.json` und `data/protokoll.md`
- der Excel-Download verweist direkt auf die versionierte Exportdatei im Repository
- responsive Darstellung für Smartphone, Tablet und Desktop
- keine externen JavaScript-Bibliotheken und keine externen Trackingdienste

## Aktualisierungslogik

Bei neuen Belegen wird der Datensatz wie bisher im Chat gepflegt. Anschließend werden gemeinsam aktualisiert:

- `data/buchungen.json`
- `data/status.md`
- `data/protokoll.md`
- `exports/Urlaubskasse_Woche1.xlsx`

Die Website übernimmt den neuen Stand automatisch aus diesen Dateien. Es ist keine zusätzliche Pflege der Oberfläche nötig.

## Veröffentlichung

Der Workflow `.github/workflows/pages.yml` baut aus den Dateien im Hauptzweig ein sauberes GitHub-Pages-Artefakt. Jede Änderung an Website, Daten oder Excel-Export veröffentlicht dadurch automatisch den aktuellen Lesestand.

## Datenschutz

Die bestehende Datenschutzlogik des Repositories bleibt unverändert: keine Originalbelege sowie keine Kreditkarten-, Konto-, Gutschein- oder sonstigen Zahlungsnummern. Die Website zeigt nur die bereits freigegebenen anonymisierten Personenbezeichnungen und Zahlungsquellen.
