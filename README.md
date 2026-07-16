# Urlaubskasse Woche 1

Statische, mobile Leseansicht der Urlaubskasse für den Sommerurlaub 2026.

## Ansichten

- **Protokoll:** rendert den vollständigen Markdown-Datenstand.
- **Einkäufe:** zeigt alle erfassten Bons und Gutschriften mit Datum, Urlaubssumme und Zahlungsquelle.
- **Excel:** stellt die aktuelle Arbeitsmappe zum Download bereit.
- **Salden:** zeigt personenscharfe Salden und vorgeschlagene Ausgleichszahlungen.

Die Website verwendet keine Datenbank und keine externen JavaScript-Bibliotheken. Alle Daten werden beim Build statisch erzeugt.

## Aktualisierung

Der Datensatz wird ausschließlich im Chat gepflegt. Bei einer Aktualisierung wird das statische Datenpaket im Repository ersetzt. Der vorhandene GitHub-Actions-Workflow erzeugt die Website und die Excel-Datei anschließend neu.

## Einmalige Veröffentlichung

Im Repository unter **Settings → Pages → Build and deployment → Source** einmal **GitHub Actions** auswählen. Danach veröffentlicht jeder neue Datenstand automatisch unter:

`https://holypetrus1.github.io/abrechnung/`

## Datenschutz

Das Repository ist öffentlich. Deshalb werden keine Originalbelege hochgeladen; die veröffentlichte Excel-Datei enthält außerdem keine Karten-Endziffern.
