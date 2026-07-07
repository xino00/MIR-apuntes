# /organize — Audit and Clean the Vault

Audit the MIR vault structure, fix common issues, and report findings.

## Usage

```
/organize
```

No arguments. Runs a full audit of the vault at `/home/arenas/Obsidian/MIR`.

## Steps

### 1. Triage Inbox

List all files in `00_Inbox/`:
```
Glob: 00_Inbox/*.md
```

For each file:
- Read its content and frontmatter
- Determine the correct destination folder based on content:
  - Pathology → `10_Patologias/<specialty>/`
  - Drug → `20_farmacos/`
  - Urgency protocol → `30_Urgencias/Patologia_Aguda/`
- If clearly classifiable:
  1. Ensure the file has proper frontmatter (add if missing)
  2. Move it: `mv "00_Inbox/<name>.md" "<target_folder>/<name>.md"`
  3. Update the relevant MOC with a wikilink
- If ambiguous: leave in inbox and tag with `review_needed` in frontmatter

Track: files moved, files left in inbox.

### 2. Check frontmatter completeness

Scan all notes in `10_Patologias/`, `20_farmacos/`, and `30_Urgencias/`:
```
Glob: 10_Patologias/**/*.md, 20_farmacos/*.md, 30_Urgencias/**/*.md
```

For each file, read the first 10 lines and check:
- Has YAML frontmatter (`---` delimiters)?
- Has `tags` field? If missing, add based on folder location
- Has `aliases` field? If missing, add common abbreviations

Track: files with frontmatter added or updated.

### 3. Normalize non-canonical tags

Scan all notes in `10_Patologias/`, `20_farmacos/`, and `30_Urgencias/` for tags that contain uppercase letters or accented characters.

Apply this deterministic mapping:

| Non-canonical | Canonical |
|---|---|
| farmacología | farmaco |
| cardiología | cardio |
| neurología | neuro |
| neumología | neumo |
| nefrología | nefro |
| reumatología | reuma |
| hematología | hemato |
| endocrinología | endocrino |
| AEMPS | *(remove)* |
| 12Octubre | *(remove)* |

For any other non-canonical tag not in the table: strip accents and lowercase (e.g., `betalactámico` → `betalactamico`, `diurético` → `diuretico`).

Process:
1. Grep all `tags:` lines in `10_Patologias/`, `20_farmacos/`, `30_Urgencias/`
2. Build a change table: `| File | Current tags | Proposed tags | Changes |`
3. **Present the table to the user and WAIT for confirmation before editing**
4. Apply edits via Edit tool
5. Track: files with tags normalized

### 4. Detect wikilinks in YAML (Quartz compatibility)

Search for `[[` inside frontmatter across the entire vault:
```
Grep: pattern "\[\[" inside YAML blocks (between --- delimiters)
```

For each violation:
- Read the file
- Replace the wikilink in YAML with plain text (e.g., `[[Drug]]` becomes `Drug`)
- Preserve the wikilink in the note body — only fix YAML

Track: files with Quartz issues fixed.

### 4. Verify MOC links

For each specialty folder in `10_Patologias/`:
- List all `.md` files in the folder
- Read the corresponding MOC file from `90_MOCs/`
- For each note NOT mentioned in the MOC:
  - Add `- [[Note Name]]` to the appropriate section

Also check `20_farmacos/` against `MOC - FARMACOS.md` and `30_Urgencias/` against `MOC - Urgencias.md`.

Track: wikilinks added to MOCs.

### 5. Report

Print a summary table:

```
Vault Organization Report
---
Files scanned:        <N>
Inbox triaged:        <N moved> / <N total in inbox>
Frontmatter fixed:    <N>
Quartz issues fixed:  <N>
MOC links added:      <N>
Needs manual review:  <N> (tagged review_needed)
---
```

If any files need manual review, list them with the reason.

## Constraints

- Do NOT delete any files — only move or edit
- Do NOT modify note body content — only frontmatter and MOC files
- Always ask before moving a file if the classification is uncertain
- Use canonical tags from CLAUDE.md (lowercase, no accents)
- NEVER put wikilinks inside YAML frontmatter
