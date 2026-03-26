# Create Medical Note

1. Ask the user for:
   - Topic name
   - Note type (choose one): fármaco, patología, urgencia, caso clínico, guardia
   - Source (PDF path, existing note, or describe content)

2. Determine the correct folder based on note type:
   - **fármaco** → `20_farmacos/<Nombre>.md`
   - **patología cardio** → `10_Patologias/01_Cardio/<Nombre>.md`
   - **patología neuro** → `10_Patologias/02_Neuro/<Nombre>.md`
   - **patología infecciosas** → `10_Patologias/03_Infecciosas/<Nombre>.md`
   - **patología digestivo** → `10_Patologias/04_Digestivo/<Nombre>.md`
   - **patología neumología** → `10_Patologias/05_Neumologia/<Nombre>.md`
   - **patología nefrología** → `10_Patologias/06_Nefrologia/<Nombre>.md`
   - **patología reumatología** → `10_Patologias/07_Reumatologia/<Nombre>.md`
   - **urgencia** → `30_Urgencias/Patologia_Aguda/<Nombre>.md`
   - **caso clínico** → `40_Casos clinicos/<Nombre>.md`
   - **guardia** → `50_Guardias/<Nombre>.md`

3. Before creating the note, check if the target folder exists. If it doesn't, create it with `mkdir -p <folder>`. This applies to both standard folders (e.g. a new especialidad under `10_Patologias/`) and any subfolder that may be missing.

4. Create the note with YAML frontmatter:
   - Include `tags` and `aliases` fields
   - **NEVER use wikilinks (`[[...]]`) inside frontmatter** — plain text only

5. Use standard sections based on type:
   - **Patología / Urgencia:** Definición, Etiología, Fisiopatología, Diagnóstico, Tratamiento, Enlaces relacionados
   - **Fármaco:** use `99_Plantillas/TPL - Farmaco.md` as reference for structure
   - **Caso clínico:** use `99_Plantillas/TPL - Casos clinicos.md` as reference
   - **Guardia:** use `99_Plantillas/TPL - Guardia.md` as reference

6. Add wikilinks to related notes throughout the body (drug names, related conditions, MOCs).

7. Update the relevant hub/MOC note to include a wikilink to the new note:
   - Fármacos → no hub update needed
   - Patología → update the corresponding `90_MOCs/MOC - <ESPECIALIDAD>.md`
   - Urgencia → update `90_MOCs/MOC - Urgencias.md` if the condition belongs there

8. Verify there are no broken wikilinks introduced by the new note.

9. Git add, commit with a descriptive message, and push.
