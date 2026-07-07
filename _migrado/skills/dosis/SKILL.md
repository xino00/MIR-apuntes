---
name: dosis
description: >-
  This skill should be used when the user asks for "dosis de [fármaco]",
  "posología de [fármaco]", "cuánto dar de [fármaco]", "dosis IV",
  "ajuste renal de [fármaco]", or needs a quick drug dose reference during a shift.
  Returns compact dosing info from vault drug files. Never fabricates doses.
---

# /dosis — Consulta Rápida de Dosis

Lookup rápido de posología desde las fichas de fármacos del vault. Diseñado para consultas al pie de cama durante guardia.

## Usage

```
/dosis <nombre-fármaco>
```

Acepta nombres parciales: `furo` → Furosemida, `amoxi` → Amoxicilina.

## Steps

### 1. Find the drug file

Search `20_farmacos/*.md` for the closest filename match (case-insensitive):

```
Glob: 20_farmacos/*<query>*.md
```

If multiple matches, list them and ask the user to clarify. If zero matches, report:

> No hay ficha de **[nombre]** en el vault. Usa `/newnote` para crearla.

Then STOP. Never fabricate dosing information.

### 2. Extract dosing section

Read the matched file. Locate the Posología section by searching for:
- `## 5. Posología y Administración` (most common format)
- `## Posología` (alternative format)

Read from that heading until the next `##` heading or end of file.

Also read:
- Lines 5-8 of the file (contains **Clase:** and **Fuente:**)
- Any `> [!WARNING]` or `> [!DANGER]` callout within or immediately after the Posología section

### 3. Format compact output

Present dosing in this exact format:

```
**[Nombre del fármaco]** — [Clase terapéutica]

| Vía | Dosis | Frecuencia | Notas |
|-----|-------|------------|-------|
| VO  | ...   | ...        | ...   |
| IV  | ...   | ...        | ...   |

⚠️ [Key warning if present]

📎 Fuente: [source from file]
```

Rules for the table:
- Include only routes mentioned in the file
- If renal adjustment exists, add a row or note
- If max daily dose is mentioned, include it
- Keep each cell concise (max 15 words)

### 4. Offer follow-up

After presenting the dose, offer:
- "¿Quieres ver la ficha completa?" → Read and present full file
- "¿Ajuste en insuficiencia renal/hepática?" → Search for those keywords in the file

## Constraints

- **NEVER fabricate doses.** Only report what the vault file contains. If the section is empty or unclear, say so.
- **Read-only.** This skill does not modify any files.
- **Speed over completeness.** Return the minimum useful information. The user is at bedside.
- **Source policy.** If the drug file doesn't have dosing info, do NOT supplement from general knowledge. Report the gap and suggest `/research` to fill it.
