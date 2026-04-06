#!/bin/bash
# sync.sh — commit + push del vault MIR con fecha automática
# Uso: bash sync.sh [mensaje opcional]

cd "$(dirname "$0")"

MSG=${1:-"sync: $(date '+%Y-%m-%d %H:%M')"}

git add -A
git commit -m "$MSG" 2>&1 | grep -v "^$" || echo "Nada nuevo que commitear."
git push origin master:main && echo "✓ Push completado." || echo "✗ Error en el push."
