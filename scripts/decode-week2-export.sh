#!/usr/bin/env bash
set -euo pipefail
base64 --decode exports/Urlaubskasse_Woche2_aktuell.xlsx.b64 > "$1"
