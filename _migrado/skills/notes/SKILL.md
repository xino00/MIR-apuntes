# /notes — PDF to Obsidian Notes Pipeline

Split a large PDF (guideline, manual chapter, protocol collection) into **multiple** individual Obsidian notes — one per topic/pathology/drug.

For converting a single document into **one** note, use `/convert` instead.

## Usage

```
/notes <PDF_PATH> [--specialty <code>] [--type patologia|farmaco|protocolo]
```

- `PDF_PATH`: path to the PDF (absolute or relative, supports `~`)
- `--specialty`: folder routing code (cardio, neuro, infecciosas, digestivo, neumologia, nefrologia, reumatologia, hematologia, endocrino, orl, urologia, traumatologia, dermatologia, urgencias, farmacos)
- `--type`: note type for all extracted notes (default: patologia)

If arguments are missing, ask the user.

## Steps

### 1. Extract PDF content

Read the PDF using the Read tool (for PDFs, use `pages` parameter to read in chunks of 15-20 pages).

For large PDFs (>20 pages), read in batches:
```
Read: file_path=<PDF>, pages="1-20"
Read: file_path=<PDF>, pages="21-40"
...
```

### 2. Identify individual topics

Analyze the extracted content and identify distinct topics that should become separate notes. Typical splits:

- **Manual chapters**: each section/subsection → one pathology note
- **Protocol collections**: each protocol → one note
- **Drug guides**: each drug monograph → one drug note
- **Guideline PDFs**: each major recommendation section → one note

Present the proposed topic list to the user in a numbered table:

```
| # | Tema propuesto | Tipo | Carpeta destino |
|---|----------------|------|-----------------|
| 1 | Endocarditis Infecciosa | patología | 10_Patologias/01_Cardio/ |
| 2 | Fiebre Reumática | patología | 10_Patologias/01_Cardio/ |
| 3 | Amoxicilina | fármaco | 20_farmacos/ |
```

**Wait for user confirmation** before creating notes. The user may want to:
- Remove topics they don't need
- Rename topics
- Change the type or specialty
- Add topics you missed

### 3. Create each note

For each confirmed topic, create the note following the `/newnote` structure:

**Determine file path:**
- Pathology → `10_Patologias/<specialty_folder>/<Topic Name>.md`
- Drug → `20_farmacos/<Drug Name>.md`
- Urgency → `30_Urgencias/Patologia_Aguda/<Topic Name>.md`
- Protocol → `10_Patologias/<specialty_folder>/<Protocol Name>.md`

Filename: Spanish, no accents (e.g., `Endocarditis Infecciosa.md`).

**YAML frontmatter** (NEVER put wikilinks inside):
```yaml
---
aliases:
  - "<abbreviation or alternative name>"
tags:
  - <content-type: patologia, farmaco, protocolo>
  - <specialty tag>
fuente: "<PDF source filename>"
fecha: <today's date YYYY-MM-DD>
---
```

**Note body** (in Spanish), standard sections by type:

- **Patología:** Definición, Etiología, Fisiopatología, Clínica, Diagnóstico, Tratamiento (Agudo + Mantenimiento), Referencias
- **Fármaco:** Mecanismo de Acción, Indicaciones, Posología, Contraindicaciones, RAM, Perlas Clínicas, Relacionados
- **Urgencia:** Signos de alarma (callout), Definición, Evaluación inicial, Diagnóstico diferencial, Tratamiento urgente, Criterios de ingreso

Use callouts:
- `> [!warning]` for red flags, contraindications
- `> [!tip]` for clinical pearls
- `> [!important]` for key criteria, dosing

**Add wikilinks** to drugs, related pathologies, and scales that exist in the vault:
```
Glob: 10_Patologias/**/*.md, 20_farmacos/*.md, 30_Urgencias/**/*.md
```

### 4. Update MOCs

For each created note, add its wikilink to the corresponding MOC in `90_MOCs/`:

| Specialty | MOC file |
|---|---|
| cardio | `MOC - CARDIOLOGIA.md` |
| neuro | `MOC - NEUROLOGIA.md` |
| infecciosas | `MOC - INFECCIOSAS.md` |
| digestivo | `MOC - DIGESTIVO.md` |
| neumologia | `MOC - NEUMOLOGIA.md` |
| nefrologia | `MOC - NEFROLOGIA.md` |
| reumatologia | `MOC - REUMATOLOGIA.md` |
| hematologia | `MOC - HEMATOLOGIA.md` |
| endocrino | `MOC - ENDOCRINO.md` |
| orl | `MOC - ORL.md` |
| urologia | `MOC - UROLOGIA.md` |
| traumatologia | `MOC - TRAUMATOLOGIA.md` |
| dermatologia | `MOC - DERMATOLOGIA.md` |
| urgencias | `MOC - Urgencias.md` |
| farmacos | `MOC - FARMACOS.md` |

Read each MOC before editing. Add the wikilink under the appropriate section.

### 5. Verify wikilinks

For every `[[wikilink]]` in all new notes, check that a corresponding `.md` file exists. Report broken links.

### 6. Summary and commit

Show a summary table:

```
| Nota | Ruta | Estado |
|------|------|--------|
| Endocarditis Infecciosa | 10_Patologias/01_Cardio/ | ✅ Creada |
| Fiebre Reumática | 10_Patologias/01_Cardio/ | ✅ Creada |
```

Then commit all new notes and MOC updates:

```bash
cd /home/arenas/Obsidian/MIR
git add <all new notes> <all modified MOCs>
git commit -m "feat: add N notes from <PDF source filename>"
git push
```

## Constraints

- Write all note content in Spanish
- NEVER put wikilinks inside YAML frontmatter (breaks Quartz build)
- Preserve ALL clinical content from the PDF — do not summarize or omit details
- Use canonical tags from CLAUDE.md (lowercase, no accents)
- Always wait for user confirmation of the topic list before creating notes
- Use Spanish INN drug names (not brand names)
- If the PDF is very large (>50 pages), process in batches of 15-20 pages and create notes incrementally
- Use subagents (Agent tool with model: sonnet) for parallel note creation when there are >3 notes to create
