---
name: interaccion
description: >-
  This skill should be used when the user asks for "interacciones de [fármacos]",
  "interacción entre A y B", "puedo dar A con B", "compatibilidad farmacológica",
  "X + Y + Z interacciones", or wants to verify drug-drug interactions before
  prescribing. Cross-references the drug files in 20_farmacos/ first; falls
  back to CIMA AEMPS (ficha técnica oficial) when the vault has no data.
  Always marks the source of each interaction (vault vs AEMPS).
---

# /interaccion — Verificador de Interacciones Farmacológicas

Cruza fichas de fármacos del vault para detectar interacciones documentadas y consulta CIMA AEMPS como fuente oficial cuando el vault no aporta datos.

## Usage

```
/interaccion <fármaco1> + <fármaco2> [+ <fármaco3> …]
```

Ejemplos:
- `/interaccion claritromicina + simvastatina`
- `/interaccion warfarina + amiodarona + omeprazol`
- `/interaccion enalapril + espironolactona + ibuprofeno`

Acepta nombres parciales (igual que `/dosis`): `claritro` → Claritromicina.

## Steps

### 1. Resolver cada fármaco

Para cada nombre del input:

```
Glob: 20_farmacos/*<query>*.md
```

Casos:
- **Match único** → guardar la ruta de la ficha y el nombre canónico (filename sin `.md`).
- **Match múltiple** → mostrar opciones y pedir aclaración antes de continuar.
- **Sin match** → marcar como `⚠️ no en vault` y continuar (la verificación AEMPS sigue siendo posible para ese fármaco).

Mostrar al usuario un resumen breve de qué fármacos se han resuelto:

```
Resueltos:
- claritromicina → 20_farmacos/Claritromicina.md
- simvastatina → 20_farmacos/Simvastatina.md
- amiodarona → ⚠️ no en vault (se consultará AEMPS)
```

### 2. Cruce vault — búsqueda bidireccional

Para cada par ordenado (A, B) de fármacos resueltos en el vault:

1. `Grep` el nombre canónico de **B** dentro del archivo de **A**, case-insensitive, también probar variantes ASCII.
2. Capturar **3 líneas de contexto** alrededor de cada hit (con `-B 1 -A 2` o equivalente).
3. Filtrar hits relevantes por sección o callout:
   - Bajo `## 3. Contraindicaciones` o `## Contraindicaciones`
   - Bajo `## 4. RAM` / `Reacciones adversas`
   - Bajo `## 1. Mecanismo` / `Farmacocinética` (CYP3A4, P-gp, eliminación renal)
   - Dentro de `> [!WARNING]`, `> [!DANGER]`, `> [!CAUTION]`
   - Bajo cualquier heading que contenga "interaccion" / "interacción"

Repetir para el par inverso (B, A) — las interacciones suelen documentarse solo en una de las dos fichas.

Para cada hallazgo, registrar:
- **Par:** A ↔ B
- **Cita literal** (línea del archivo)
- **Sección/callout** donde aparece
- **Wikilink** a la ficha origen del hallazgo

### 3. Fallback CIMA AEMPS — solo para pares sin hallazgo en vault

Para cada par sin hits en el paso 2, consultar la ficha técnica oficial española vía `WebFetch`:

1. URL base: `https://cima.aemps.es/cima/publico/lista.html?nombre=<fármaco-principal>`
2. Localizar el código nacional de un medicamento que contenga el principio activo.
3. Acceder a la ficha técnica HTML/PDF y buscar la sección **"4.5 Interacción con otros medicamentos"**.
4. Extraer cualquier mención del segundo fármaco (por nombre o por mecanismo: "inhibidores potentes de CYP3A4", "diuréticos ahorradores de potasio", etc.).

Si CIMA tampoco aporta datos: marcar el par como **"no documentado en vault ni AEMPS"** y sugerir consultar Stockley o UpToDate.

**Importante:** marcar siempre la fuente de cada hallazgo. No mezclar AEMPS con vault sin distinción.

### 4. Output — tabla compacta

Formato fijo:

```
## Interacciones — [Fármaco1] + [Fármaco2] [+ ...]

| Par | Severidad | Mecanismo / Efecto | Fuente | Cita |
|-----|-----------|---------------------|--------|------|
| A ↔ B | 🔴 Contraindicado | Inhibición CYP3A4 → ↑↑ niveles B → rabdomiolisis | vault | "CONTRAINDICADO con [B]" — [[A]] |
| A ↔ C | 🟠 Precaución | Hiperpotasemia | AEMPS §4.5 | "vigilar potasio sérico..." |
| B ↔ C | ⚪ Sin datos | — | — | No documentado en vault ni AEMPS |

**Resumen:** [N pares analizados] · [N hallazgos vault] · [N hallazgos AEMPS] · [N sin datos]
```

Severidad determinada por palabras clave en la cita:
- 🔴 **Contraindicado** — "contraindicado", "no asociar", "evitar"
- 🟠 **Precaución** — "vigilar", "ajustar dosis", "monitorizar", "precaución"
- 🟡 **Informativo** — "puede aumentar", "considerar"
- ⚪ **Sin datos** — sin hallazgos en ninguna fuente

Si la cita no permite clasificar la severidad sin ambigüedad, marcar 🟡 y dejar la cita literal para que el usuario decida.

### 5. Cierre con próximos pasos

Tras la tabla, sugerir según hallazgos:
- Si hay 🔴: *"Considera reemplazo del fármaco o consulta con farmacia hospitalaria."*
- Si hay ⚪ (sin datos): *"Para combinaciones críticas, valida en Stockley/UpToDate antes de prescribir."*
- Si todas las fichas resueltas → ofrecer *"¿Quieres que revise dosis ajustadas? → `/dosis <fármaco>`."*

## Constraints

- **NUNCA fabricar interacciones** desde conocimiento general. Toda fila de la tabla debe tener fuente: vault o AEMPS, con cita literal.
- **Marcar fuente explícitamente** en cada fila. No mezclar.
- **Read-only.** No modifica fichas, no añade campos al frontmatter, no toca MOCs.
- **AEMPS solo como fallback.** Vault primero. Si vault dice algo, no se complementa con AEMPS — se usa el vault como fuente de verdad.
- **Source policy.** Alineada con `memory/feedback_source_policy.md`. Si vault y AEMPS callan, decirlo y parar.
- **Velocidad.** El residente está prescribiendo. Una tabla, una pantalla, severidad visible al primer vistazo.
- **Limitación conocida.** Las fichas actuales mencionan interacciones inline sin campo estandarizado en frontmatter. El recall mejorará si en el futuro se añade `interacciones_criticas: [...]` — esta skill funciona sin ello.
