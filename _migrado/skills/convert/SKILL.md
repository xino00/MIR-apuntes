# /convert — Convert a Document to an Obsidian Note

Convert a single document (PDF, DOCX, PPTX, HTML) into one formatted Obsidian note and save to the vault.

For splitting a PDF into **multiple** notes (one per topic), use `/notes` instead.

## Usage

```
/convert <FILE_PATH> [--output "Note Name"] [--specialty <code>]
```

- `FILE_PATH`: path to the document (absolute or relative, supports `~`)
- `--output`: optional custom note title (without .md extension)
- `--specialty`: optional folder routing code (cardio, neuro, etc.)

If arguments are missing, ask the user.

## Steps

### 1. Convert to raw markdown

Run markitdown via Bash:
```bash
markitdown "<FILE_PATH>"
```

Capture the stdout output. If markitdown fails, try reading the file directly (for .md, .txt) or report the error.

For large documents (>50KB output), warn the user that the resulting note will be long and ask if they want to proceed or use `/notes` to split it instead.

### 2. Determine file location

Based on the specialty code or content analysis:
- Pathology → `10_Patologias/<specialty>/`
- Drug → `20_farmacos/`
- Urgency → `30_Urgencias/Patologia_Aguda/`
- No specialty → `00_Inbox/`

Filename: use `--output` value if given, otherwise derive from the source filename.
No accents in filename. Use sentence case.

### 3. Reformat as Obsidian note

Transform the raw markdown:

**Add YAML frontmatter** (no wikilinks inside):
```yaml
---
aliases:
  - "<alternative name>"
tags:
  - <content-type tag: patologia, farmaco, protocolo, guia>
  - <specialty tag>
fuente: "<source document name>"
fecha: <today's date YYYY-MM-DD>
---
```

**Format the body:**
- Clean up conversion artifacts (broken tables, orphaned headers, encoding issues)
- Preserve ALL clinical content — do not summarize or omit
- Convert relevant sections to Obsidian callouts:
  - Warnings, contraindications, red flags → `> [!warning]` or `> [!danger]`
  - Clinical tips, pearls → `> [!tip]`
  - Key definitions, important info → `> [!important]`
- Standardize heading levels (H1 for title, H2 for main sections, H3 for subsections)

**Add wikilinks:**
- Scan the vault for existing note filenames:
  ```
  Glob: 10_Patologias/**/*.md, 20_farmacos/*.md, 30_Urgencias/**/*.md
  ```
- For each existing note name that appears as plain text in the converted content, replace with `[[wikilink]]`
- Use pipe syntax for accented display: `[[Fibrilacion Auricular|Fibrilación Auricular]]`

### 4. Save to vault

Write the formatted note to the target path using the Write tool.

### 5. Update MOC

Read the corresponding MOC file and add a wikilink to the new note. MOC mapping:
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

Check every `[[wikilink]]` in the new note against existing vault files. Report any broken links.

### 7. Commit and push

```bash
cd /home/arenas/Obsidian/MIR
git add <new note> <modified MOC>
git commit -m "feat: convert <source filename> to vault note"
git push
```

## Constraints

- Write note content in Spanish
- NEVER put wikilinks inside YAML frontmatter
- Preserve ALL content from the source — this is a conversion, not a summary
- Use canonical tags from CLAUDE.md (lowercase, no accents)
- If the document is very large (>100KB), ask the user before proceeding
