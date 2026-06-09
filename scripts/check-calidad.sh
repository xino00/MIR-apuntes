#!/bin/bash
# check-calidad.sh — Verificación rápida de calidad del vault MIR
#
# Detecta los dos fallos que rompen el vault o la confianza clínica:
#   1. Wikilinks [[...]] dentro del frontmatter YAML  → ROMPE el build de Quartz
#   2. Texto corrupto del generador defectuoso         → fichas ilegibles/peligrosas
#
# Uso:   ./scripts/check-calidad.sh
# Salida: lista de archivos sospechosos. Código de salida 1 si hay hallazgos críticos.
#
# Pensado para correr antes de un push (manualmente o desde sync.sh).

cd "$(dirname "$0")/.." || exit 2
fail=0

echo "== 1. Wikilinks en frontmatter YAML (rompen Quartz) =="
yaml_bad=$(python3 - <<'PYEOF'
import pathlib
bad = []
for p in pathlib.Path('.').rglob('*.md'):
    s = str(p)
    if '/.git/' in s or '/quartz/' in s:
        continue
    t = p.read_bytes().decode('utf-8-sig', 'replace')
    if not t.startswith('---'):
        continue
    end = t.find('\n---', 3)
    if end < 0:
        continue
    if '[[' in t[:end]:
        bad.append(s)
print('\n'.join(bad))
PYEOF
)
if [ -n "$yaml_bad" ]; then
  echo "$yaml_bad" | sed 's/^/  ✗ /'
  fail=1
else
  echo "  ✓ ninguno"
fi

echo
echo "== 2. Texto corrupto (palabras inventadas / placeholder roto) =="
# Señales del lote defectuoso: palabras agramaticales interpoladas + placeholder "Ver tasgs"
corrupt=$(grep -rlE 'craso|mortaloide|letaloide|histonatural|Insuificiencia|Alterección|rápida general|puro letal|letal general|sistémico puro|Ver tasgs' \
  10_Patologias 20_farmacos 30_Urgencias 2>/dev/null)
if [ -n "$corrupt" ]; then
  echo "$corrupt" | sed 's/^/  ✗ /'
  fail=1
else
  echo "  ✓ ninguno"
fi

echo
if [ "$fail" -eq 1 ]; then
  echo "RESULTADO: hallazgos que requieren revisión antes de publicar."
  exit 1
else
  echo "RESULTADO: vault limpio."
fi
