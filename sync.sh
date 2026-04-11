#!/bin/bash

cd "$(dirname "$0")"

echo "Sincronizando apuntes MIR con GitHub..."

# Descargar posibles cambios hechos desde otros dispositivos primero (usando rebase)
git pull --rebase

git add .

# Comprobar si hay cambios para guardar
if git diff --cached --quiet; then
    echo "No hay cambios nuevos locales que subir."
    exit 0
fi

FECHA=$(date "+%Y-%m-%d %H:%M")
git commit -m "Actualización: $FECHA"

# Intentar subir los cambios y avisar si hay error
if git push; then
    echo "✅ Sincronización completada con éxito."
else
    echo "❌ Error: No se pudieron subir los cambios. Revisa tu conexión a internet o posibles conflictos."
    exit 1
fi
