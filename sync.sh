#!/bin/bash

cd "$(dirname "$0")"

echo "Sincronizando apuntes MIR con GitHub..."

git add .

if git diff --cached --quiet; then
    echo "No hay cambios nuevos."
    exit 0
fi

FECHA=$(date "+%Y-%m-%d %H:%M")
git commit -m "Actualización: $FECHA"
git push

echo "Sincronización completada."
