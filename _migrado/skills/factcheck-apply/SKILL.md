# /factcheck-apply — Aplicar informe de fact-check al vault

Aplica un informe de `00_Inbox/FACT_CHECK_<fecha>/NN_<Especialidad>.md` a las notas del vault, con commits atómicos por bloque, recheck automático y cierre de estado.

Diseñada para reproducir el workflow validado el 2026-04-20 en cardiología (95/105 ✅ · 13/13 🔴 al 100%).

## Usage

```
/factcheck-apply <especialidad>           # Resuelve NN_<Esp>.md en la auditoría más reciente
/factcheck-apply <ruta/al/informe.md>     # Informe específico
/factcheck-apply <especialidad> --dry     # Muestra el plan sin aplicar
```

Ejemplos:
- `/factcheck-apply cardio` → aplica `00_Inbox/FACT_CHECK_2026-04-20/01_Cardio.md`
- `/factcheck-apply nefro` → aplica `06_Nefrologia.md`
- `/factcheck-apply 00_Inbox/FACT_CHECK_2026-04-20/04_Digestivo.md` → ruta directa
- `/factcheck-apply reumato --dry` → solo reporta

## Contrato con el formato del informe

El parser asume el siguiente patrón (producido por el agente `factcheck-auditor`):

```
# Fact-check — <Especialidad> (N/N notas)
...
# Sección N — <bloque temático> (<M> notas)
## [[Nombre Nota]]
### Hallazgo N · 🔴/🟠/🟢/⚪ Crítico/Moderado/Menor/Informativo
- **Hallazgo:** <descripción>
- **Cita en la nota:** "<texto literal>" (línea NN)
- **Cita en la fuente:** "<texto literal>" (página/sección)
- **Cambio sugerido:** <texto literal aplicable>
```

Si el informe no sigue esta estructura, la skill aborta y pide al residente regenerarlo con el agente.

## Steps

### 1. Resolver informe

Si el argumento no acaba en `.md`:
- Mapea la especialidad a su prefijo numérico:
  - `cardio`→`01`, `neuro`→`02`, `infecciosas`→`03`, `digestivo`→`04`, `neumo`/`neumologia`→`05`, `nefro`→`06`, `reuma`/`reumato`→`07`, `hemato`→`08`, `endo`/`endocrino`→`09`, `orl`→`10`, `uro`/`urologia`→`11`, `trauma`→`12`, `dermato`→`13`, `psiq`→`14`.
- Glob `00_Inbox/FACT_CHECK_*/<NN>_*.md`. Toma la fecha más reciente (ordena por nombre descendente, las carpetas son `FACT_CHECK_YYYY-MM-DD`).
- Si hay 0 matches: error `"No se encontró informe para <especialidad>. Lanza el agente factcheck-auditor primero."`.
- Si hay >1 (misma fecha, distintos prefijos): avisa y pide ruta explícita.

Si el argumento es una ruta: valida que existe con `Read` de las primeras 10 líneas.

### 2. Parsear

Lee el informe completo con `Read`. Extrae:

- **Metadatos**: nombre de especialidad, fuente principal (del encabezado o primera mención de "Fuente primaria"), fecha del informe (de la carpeta `FACT_CHECK_<fecha>`).
- **Bloques**: cada `# Sección N — <nombre> (<M> notas)` abre bloque N; cierra al siguiente `#` de nivel 1 o EOF. Guarda nombre, fuente asociada (si la línea siguiente dice `Fuente: ...`) y rango de líneas.
- **Notas por bloque**: cada `## [[<Nombre>]]` dentro del bloque. Guarda nombre sin los `[[]]`.
- **Hallazgos por nota**: cada `### Hallazgo N · <emoji> <nivel>`. Para cada uno, extrae los 4 campos:
  - `- **Hallazgo:** ...`
  - `- **Cita en la nota:** ...`
  - `- **Cita en la fuente:** ...`
  - `- **Cambio sugerido:** ...`

Normaliza el emoji → severidad:
- 🔴 → `critico`
- 🟠 → `moderado`
- 🟢 → `menor`
- ⚪ → `informativo`

### 3. Clasificar cada hallazgo

Dos categorías:

**AUTO** (aplica con `Edit` directo) si se cumplen TODOS:
- `Cita en la nota` es un texto literal entre comillas ≤2 líneas (no "Ver sección completa", no "Toda la nota").
- `Cambio sugerido` es texto literal aplicable (no empieza con "Reescribir", "Renombrar", "Eliminar sección", "Añadir nueva sección", "Reformatear tabla").
- Al hacer `Read` de la nota destino, el `old_string` aparece **exactamente una vez**.

**AMBIGUO** (pausa y pregunta al usuario) si cualquiera de:
- Cambio sugerido pide reescritura, renombrado, nueva sección, eliminación de tabla/sección.
- `old_string` aparece 0 veces (texto ya cambiado o nota editada localmente).
- `old_string` aparece >1 veces (no único → `Edit` fallaría).
- La nota destino no existe (wikilink roto).
- Severidad ⚪ cuyo "Cambio sugerido" sea solo "Añadir `fuente:` al frontmatter" (se resuelve en paso 4.d, no aquí).

Caso especial: si el hallazgo es "Sin cambio" / "Verificación positiva" / "Alineación correcta", omite el hallazgo (ni AUTO ni AMBIGUO — solo cuenta para el informe final).

### 4. Aplicar por bloques

En modo `--dry`: solo muestra el resumen del paso 3 (AUTO/AMBIGUO/SKIP por bloque) y termina. No edita nada, no commitea.

En modo normal, por cada bloque en orden:

#### 4.a — Preparar
Lista notas afectadas. Para cada una, haz `Read` una sola vez (evita re-reads dentro del mismo bloque).

#### 4.b — Aplicar AUTO
Para cada hallazgo AUTO:
- `Edit` con `old_string` = texto literal de "Cita en la nota" (sin las comillas envolventes ni el " (línea NN)" final), `new_string` = texto literal de "Cambio sugerido".
- Si falla (muy raro, old_string dejó de ser único tras Edits previos del mismo bloque): marca como `PENDIENTE_MANUAL` y continúa.

#### 4.c — Resolver AMBIGUOS
Para cada hallazgo AMBIGUO del bloque, usa `AskUserQuestion` con contexto:
- Pregunta: `"<Nota>: ¿qué hacer con <severidad> hallazgo N?"` + citas completas en la pregunta.
- Opciones (máx 4):
  1. **Aplicar sugerido** (reemplazo literal — incluso si es reescritura larga, hazlo con Edit o Write según tamaño)
  2. **Saltar** (marca como PENDIENTE_MANUAL)
  3. **Editar manualmente después** (registra y continúa)
  4. **Ver contexto** (si el usuario pide más info → muestra 20 líneas de la nota y pregunta de nuevo).

Para renombres de nota: requiere confirmación extra ("¿renombrar archivo + actualizar wikilinks globalmente?"). Si confirma, usa `git mv` + `Grep` + `Edit` para propagar el wikilink nuevo.

#### 4.d — Trazabilidad en frontmatter
Para cada nota tocada en el bloque:
- Si el YAML ya tiene `fuente:`, respeta el existente (a menos que el informe pida cambiarlo explícitamente).
- Si falta `fuente:`, añade `fuente: "<guía principal del bloque del informe>"` (string, entre comillas, nunca wikilinks raw).
- Añade/actualiza `last_fact_checked: <fecha_hoy_ISO>`.
- Normaliza tags a canónicos si no lo están (lowercase, sin acentos, sin underscores). Taxonomía en `CLAUDE.md`.

Aplica con `Edit` sobre el bloque YAML entero si hay múltiples cambios.

#### 4.e — Commit atómico
```
git add <paths exactos de las notas tocadas en el bloque>
git commit -m "fix(<esp>): aplicar fact-check bloque N - <nombre> (<Nα>🔴 <Nβ>🟠 <Nγ>🟢 <Nδ>⚪)

<resumen de 2-4 bullets con los cambios clave>

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

`git add` con rutas explícitas — NUNCA `git add -A` (puede arrastrar archivos no relacionados como `sync.log` o inbox sin triaje).

### 5. Discrepancias

Si hay hallazgos `PENDIENTE_MANUAL` (Edit falló, usuario saltó), escribe `00_Inbox/FACT_CHECK_<fecha>/_applied_discrepancies_<esp>.md` con tabla:

```markdown
# Discrepancias al aplicar fact-check de <Esp> — <fecha>

| Hallazgo | Nota | Severidad | Razón | Acción propuesta |
|---|---|---|---|---|
| N | [[Nota]] | 🔴 | old_string no único | Editar manualmente buscando con contexto |
| N | [[Nota]] | 🟠 | usuario saltó | Revisar cuando haya contexto clínico |
```

Commit aparte: `docs(fact-check): discrepancias <esp> - N hallazgos pendientes manual`.

### 6. Recheck

Lanza subagente `Explore` con thoroughness `medium`. Prompt canónico:

> Verifica la aplicación del fact-check de <Especialidad>. NO es una re-auditoría contra los PDFs; es una verificación de si los "Cambio sugerido" del informe aparecen ahora en las notas.
>
> **Input (fuente de verdad):** `00_Inbox/FACT_CHECK_<fecha>/<NN>_<Esp>.md`
> **Notas auditadas:** `10_Patologias/<NN>_<Especialidad>/`
>
> Para cada hallazgo: leer el "Cambio sugerido", leer la nota, marcar con uno de 4 estados:
> - ✅ APLICADO — cambio presente (literal o paráfrasis clara)
> - ⚠ PARCIAL — cambio aplicado con variaciones menores
> - ❌ PENDIENTE — cita original sigue ahí
> - ❓ NO VERIFICABLE — cambio interpretativo/estructural
>
> Las notas llevan `last_fact_checked: <fecha>` y `fuente: ...` — evidencia adicional de aplicación.
>
> **Output:** `00_Inbox/FACT_CHECK_<fecha>/_recheck_<esp>.md` con:
> - Resumen global (total, %)
> - Por severidad (tabla 4×5)
> - Por bloque (tabla)
> - Detalle por hallazgo: `[severidad] [estado] Hallazgo N: <descripción corta>` + evidencia (1 línea)
> - Sección "❌ Pendientes y ⚠ parciales" al final
> - "Observaciones adicionales" si detecta inconsistencias colaterales (YAML con wikilinks, tags no canónicos).
>
> Objetivo: ≥95% APLICADO y 0 🔴 en ❌. No edites ninguna nota.

### 7. Cierre

Actualiza dos archivos de la auditoría:

**`00_Inbox/FACT_CHECK_<fecha>/INDEX.md`:**
Localiza la fila de la especialidad en "Estado por especialidad". Cambia la columna `Estado`:
- De `✅ Fase X` o similar → `✅✅ Aplicado <hoy> (X/N ✅ · Y ⚠ · Z ❌)` con enlace `· recheck → [[_recheck_<esp>]]`.

**`00_Inbox/FACT_CHECK_<fecha>/NEXT_SESSION.md`:**
Localiza mención de la especialidad en "Prioridad ALTA" y márcala como aplicada (con ✅✅ y métrica resumida). Si era el único ítem de Prioridad ALTA, mueve la sección a "Prioridad MEDIA" (revisar ⚠ parciales).

Commit final:
```
git add <INDEX.md> <NEXT_SESSION.md> <_recheck_<esp>.md>
git commit -m "docs(fact-check): cierre <esp> <hoy> - X/N ✅ (N_critico/N_critico_total 🔴 al 100%)

<resumen de 2-3 bullets clave>

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

### 8. Reporte final al usuario

Imprime en chat (≤200 palabras):

```
✅ Fact-check <Especialidad> aplicado — <fecha>

Resumen:
- N notas modificadas en M bloques
- X/N hallazgos APLICADO (%), Y PARCIAL, Z PENDIENTE
- K/K 🔴 críticos aplicados al 100%
- Commits: <N bloques> + 1 cierre (+ 1 discrepancias si aplica)

Recheck: 00_Inbox/FACT_CHECK_<fecha>/_recheck_<esp>.md

Pendientes manuales (si los hay):
- [[Nota]] — razón — acción propuesta
```

Si hay algún 🔴 en ❌, **destácalo al principio** en rojo/warning — requiere atención inmediata.

## Constraints (reglas vinculantes)

- **Nunca inventar texto clínico.** El `Cambio sugerido` del informe es la única fuente de verdad. Si no se puede aplicar literalmente, va a AMBIGUO o PENDIENTE_MANUAL.
- **Nunca wikilinks `[[...]]` en frontmatter YAML** — rompe Quartz.
- **Tags canónicos** (lowercase, sin acentos, sin underscores): `cardio`, `neuro`, `neumo`, `nefro`, `reuma`, `hemato`, `endocrino`, `orl`, `uro`, `trauma`, `dermato`, `infecciosas`, `digestivo`, `urgencias`, `patologia`, `farmaco`, `moc`, `guardia`, `plantilla`.
- **Un commit por bloque.** Nunca bundlear bloques. Facilita revertir.
- **`git add` con rutas explícitas.** Nunca `git add -A` o `git add .`.
- **No amendear commits.** Si algo falla, commit nuevo con corrección.
- Respetar cambios locales sin commitear en las notas destino: leer la versión en disco, no asumir el último commit.
- Si el informe marca una nota como "vacía" o "provisional", NO reescribirla — solo aplicar los hallazgos listados y dejar el resto como gap estructural.
- El script de sync automático corre a las 22:00 — no hace falta `git push` manual al final.

## Tests rápidos de validación

Antes de declarar una sesión como exitosa:
- `git status` solo muestra los archivos esperados.
- `git diff --stat <carpeta especialidad>/` cuenta las notas tocadas coincide con lo reportado.
- Ningún `[[wikilink]]` dentro de bloques YAML (grep pattern `^---$\n.*\[\[` multiline).
- Recheck reporta ≥95% ✅ y 0 🔴 en ❌.
