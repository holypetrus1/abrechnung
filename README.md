# Urlaubskasse Woche 1

Dieses Repository ist der verbindliche, versionierte Datenspeicher für die Urlaubsabrechnung.

## Maßgebliche Dateien

- `data/buchungen.json` – vollständiger maschinenlesbarer Datenbestand mit Bons, Einzelpositionen, Ausschlüssen, Zahlungsguthaben und Salden
- `data/status.md` – kompakter Übergabestand für die Fortsetzung in einem neuen Chat
- `data/protokoll.md` – lesbare chronologische Dokumentation einschließlich Korrekturen
- `exports/Urlaubskasse_Woche1.xlsx` – aktueller bereinigter Excel-Export

## Arbeitsweise

Die Datenerfassung erfolgt ausschließlich im Chat. Vor einem neuen Eintrag wird der aktuelle Repo-Stand eingelesen. Danach werden Daten, Protokoll, Status und Excel-Export gemeinsam aktualisiert und als neuer Commit gespeichert.

Ein neuer Chat kann ohne Datei-Upload fortsetzen, indem er zuerst `data/status.md` und `data/buchungen.json` aus diesem Repository lädt.

## Datenschutz

- Keine Originalbelege im Repository
- Keine Kreditkarten-, Konto-, Gutschein- oder sonstigen Zahlungsnummern
- Zahlungsquellen nur als neutrale Bezeichnung, zum Beispiel `Gemeinschaftskonto Katrin & Simon`
- Personenbezeichnungen bleiben in der vereinbarten anonymisierten Form

## Verteilungsregel

Normale laufende Urlaubsausgaben werden standardmäßig zu je 25 % auf Simon, Katrin, Onkel und Tante verteilt. Oma und Großvater werden nur bei ausdrücklich genannten Abweichungen belastet.
