---
title: Log del wiki
type: log
---
# 📓 Log del wiki

Registro cronológico **append-only**. Una entrada por operación, orden inverso (lo nuevo arriba).

Formato: `## [YYYY-MM-DD] <op> | <título>` — donde `<op>` ∈ `ingest` · `query` · `lint` · `refactor` · `contradiction`.
Parseable: `grep "^## \[" log.md` lista todas las operaciones.

---

## [2026-07-06] refactor | Schema — jerarquía de evidencia, etiquetas, casos/ y gaps.md
- `CLAUDE.md`: jerarquía de evidencia explícita (protocolo local/Manual 12O > CIMA > guías de sociedades > RCTs > apuntes); ante conflicto entre niveles, callout de contradicción, nunca fusión silenciosa.
- Etiquetas evidencia/interpretación en el cuerpo (`**Fuente:**` / `**Síntesis:**` / `**Confirmar localmente:**` / `> Fuente pendiente.`) + veto al lenguaje absoluto no respaldado.
- Convención de casos clínicos de-identificados (`casos/`, `type: caso`; la carpeta se crea con el primer caso).
- Nuevo `gaps.md`: acumula lagunas de fuente y cobertura detectadas en lint; sembrado con las 13 síntesis pendientes.

## [2026-07-01] refactor | Cimientos — schema + retiro de organización antigua
- `CLAUDE.md` reescrito como schema del LLM Wiki (capas, ingest/query/lint, contradicciones, borrado seguro).
- MOCs (`90_MOCs/`), skills y agentes → `_migrado/` (recuperable; purga final la confirma el usuario).
- Quartz: homepage = `index.md` (eliminado el paso que copiaba `000_INICIO`); `_migrado` excluido del build; gate `check-calidad.sh` ampliado a las carpetas nuevas.

## [2026-07-01] refactor | Neumología — Bronquitis + EPOC consolidados
- Bronquitis: refundida (entidad + plantilla, antibiótico deduplicado).
- EPOC exacerbación: reubicada + callout ⚡ Guardia; **stub "EPOC reagudizado" absorbido** (alias fundidos → el link sigue resolviendo).
- **Borrado seguro (sin git):** los originales refundidos → `_migrado/` (papelera visible), no `rm`. Purga final = una acción confirmada por ti.

## [2026-07-01] refactor | Piloto Neumología — NAC/sCAP refundidas
- `patologias/neumologia/Neumonía Adquirida en la Comunidad (NAC).md`: refundida. **Deduplicado**: el original repetía el régimen antibiótico 3× (secciones clínica, policlínica y boxes) con inconsistencias; ahora una sola versión de referencia. Plantilla de guardia separada a `plantillas/`.
- sCAP reubicada a `patologias/neumologia/` (contenido ERS/ESICM 2023 preservado).

## [2026-07-01] refactor | Inicio de la migración a LLM Wiki
Reconstrucción del vault al patrón LLM Wiki (refundir contenido clínico en páginas nuevas; retirar la organización antigua de MOCs).
- Andamiaje: `patologias/<14 especialidades>/`, `farmacos/`, `urgencias/` (+ `MUST/`), `presentaciones/`, `sintesis/`, `plantillas/`.
- Espina navegable: `index.md` + `log.md`.
- Fuentes nuevas en `Libros y referencias/`: guías **ERS/ESICM/ESCMID/ALAT sCAP**, **IDSA24** (gram-negativos resistentes), **Manual Urgencias COT**.
- Piloto: **Neumología** (clúster NAC/sCAP).
