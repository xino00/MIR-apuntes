# /research — Research a Medical Topic

Research a clinical topic using PubMed and the web, then create a structured Obsidian note in the vault.

## Usage

```
/research <TOPIC> [--specialty <code>]
```

- `TOPIC`: clinical question or subject (e.g., "Fibrilacion auricular criterios ESC 2024")
- `--specialty`: optional folder routing code (cardio, neuro, infecciosas, digestivo, neumologia, nefrologia, reumatologia, hematologia, endocrino, orl, urologia, traumatologia, dermatologia, urgencias, farmacos)

If the specialty is omitted, save to `00_Inbox/`. If the topic clearly belongs to a specialty, ask the user before assuming.

## Steps

### 1. Check vault for existing notes

Before researching, check if a note on this topic already exists:

```
Glob: 10_Patologias/**/*.md, 20_farmacos/**/*.md, 30_Urgencias/**/*.md
Grep: search for the topic name across all .md files
```

If a close match exists, ask the user whether to update the existing note or create a new one.

### 2. Research the topic

**PubMed (use MCP tools):**
- `mcp__claude_ai_PubMed__search_articles` — search for recent clinical articles (prefer 2022-2026)
- `mcp__claude_ai_PubMed__get_article_metadata` — get abstracts and details for the top results
- `mcp__claude_ai_PubMed__get_full_text_article` — retrieve full text from PMC if available (for guidelines, systematic reviews)
- `mcp__claude_ai_PubMed__find_related_articles` — find related articles if initial results are thin

**Web (for guidelines and drug data):**
- Use WebSearch to find current clinical guidelines (ESC, AHA, SEPAR, NICE, GEMA, GOLD, Surviving Sepsis, etc.)
- Use WebSearch for AEMPS ficha tecnica if the topic involves drugs
- Use WebFetch to read guideline pages or AEMPS drug monographs when found

**Extract from each source:**
- Diagnostic criteria and red flags (signos de alarma)
- Current treatment guidelines with drug names in Spanish INN
- Emergency doses (IV/IM) and standard maintenance doses (oral)
- Relevant scoring scales (CHA2DS2-VASc, Wells, CURB-65, qSOFA, etc.)
- Recent guideline updates that differ from older sources

### 3. Create the Obsidian note

**Determine file path:**
- If specialty given: save to the corresponding folder under `10_Patologias/`, `20_farmacos/`, or `30_Urgencias/`
- If no specialty: save to `00_Inbox/`
- Filename: plain Spanish, no accents in filename (e.g., `Fibrilacion Auricular.md`)

**YAML frontmatter** (no wikilinks inside — breaks Quartz):
```yaml
---
aliases:
  - "<abbreviation or alternative name>"
tags:
  - patologia
  - <specialty-tag>
fuente: "<primary guideline or source cited>"
fecha: <today's date YYYY-MM-DD>
---
```

Use canonical tags from CLAUDE.md: `cardio`, `neuro`, `neumo`, `nefro`, `reuma`, `hemato`, `endocrino`, `orl`, `uro`, `trauma`, `dermato`, `infecciosas`, `digestivo`, `urgencias`, `patologia`, `farmaco`.

**Note body** (in Spanish):

```markdown
# <Topic Name>

> [!warning] SIGNOS DE ALARMA
> - Red flag 1 (criteria for immediate action / admission)
> - Red flag 2

## Definicion

Brief clinical definition.

## Etiologia / Factores de riesgo

## Clinica

Key clinical presentation.

## Diagnostico

Diagnostic criteria, relevant scales, lab values.

## Tratamiento

### Urgencias / Agudo

Emergency management with drug names as wikilinks: [[Drug Name]]
Include IV/IM doses in a table when available.

### Mantenimiento / Alta

Chronic management and follow-up.

> [!tip] Perla clinica
> High-yield exam or guardia pearl.

## Referencias

- [[Related Pathology Note]]
- [[Related Drug Note]]
- [[MOC - ESPECIALIDAD]]
- PubMed sources cited (PMID when available)
```

**For drug notes** (if the topic is a drug), use this structure instead:
1. Mecanismo de Accion
2. Indicaciones Clinicas Principales (with wikilinks to pathologies)
3. Posologia y Administracion (dose table)
4. Contraindicaciones y Precauciones (`> [!danger]` callout)
5. Reacciones Adversas (RAM)
6. Perlas Clinicas (`> [!tip]` callout)
7. Relacionados (wikilinks)

### 4. Add wikilinks to existing vault notes

Scan the vault for note filenames that match drugs, conditions, or scales mentioned in the new note. Replace plain text references with `[[wikilinks]]`. Use pipe syntax for display text when needed: `[[Note Name|display text]]`.

### 5. Update the MOC

Read the corresponding MOC file in `90_MOCs/` and add a wikilink `[[New Note Title]]` under the appropriate section. If unsure which section, add it at the end of the pathology list.

MOC mapping:
- cardio → `MOC - CARDIOLOGIA.md`
- neuro → `MOC - NEUROLOGIA.md`
- infecciosas → `MOC - INFECCIOSAS.md`
- digestivo → `MOC - DIGESTIVO.md`
- neumologia → `MOC - NEUMOLOGIA.md`
- nefrologia → `MOC - NEFROLOGIA.md`
- reumatologia → `MOC - REUMATOLOGIA.md`
- hematologia → `MOC - HEMATOLOGIA.md`
- endocrino → `MOC - ENDOCRINO.md`
- orl → `MOC - ORL.md`
- urologia → `MOC - UROLOGIA.md`
- traumatologia → `MOC - TRAUMATOLOGIA.md`
- dermatologia → `MOC - DERMATOLOGIA.md`
- urgencias → `MOC - Urgencias.md`
- farmacos → `MOC - FARMACOS.md`

### 6. Verify wikilinks

For every `[[wikilink]]` in the new note, check that a corresponding `.md` file exists in the vault. Report any broken links and offer to fix them (remove the link or create a stub note).

### 7. Commit and push

```bash
cd /home/arenas/Obsidian/MIR
git add <new note> <modified MOC>
git commit -m "feat: add <note title> — researched from PubMed/guidelines"
git push
```

## Constraints

- Write everything in Spanish
- NEVER put wikilinks inside YAML frontmatter
- Use Spanish INN drug names (not brand names)
- Prefer 2022-2026 sources; cite the guideline name and year
- Always cite PubMed article PMIDs when used as source
- If PubMed MCP tools are unavailable, fall back to WebSearch only
