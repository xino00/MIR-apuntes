# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Obsidian medical notes vault using wikilinks (`[[Note Name]]`). When creating or editing notes, always use wikilink syntax for internal links, never standard markdown links. Ensure YAML frontmatter never contains raw wikilinks — use plain text or quoted strings in frontmatter fields.

## Contexto

Vault de Obsidian de un residente de Medicina de Familia en Madrid. Rotaciones por todos los servicios del hospital + guardias de urgencias de puerta. Uso principal: referencia clínica durante rotaciones y protocolos de guardia.

## Estructura del Vault

```
10_Patologias/          ~167 notas de patología por especialidad
  01_Cardio/            02_Neuro/       03_Infecciosas/   04_Digestivo/
  05_Neumologia/        06_Nefrologia/  07_Reumatologia/  08_Hematologia/
  09_Endocrino/         10_ORL/         11_Urologia/      12_Traumatologia/
  13_Dermatologia/

20_farmacos/            ~128 fichas de fármacos (una por archivo)

30_Urgencias/           ~26 notas — hub central de guardia
  Patologia_Aguda/      Shock, SDRA, IRA, Dolor torácico, Disnea
  Ionico_AcidoBase/     Iones, equilibrio ácido-base
  Exploracion_Fisica/   Exploración de Rodilla, Tobillo y Antepié

50_Guardias/            Plantillas y registros de guardia
90_MOCs/                Índices de navegación (15 MOCs + checklist)

00_Inbox/               Notas entrantes sin clasificar (incluye stubs y recordatorios)
assets/                 Attachments pegados desde Obsidian (PXL_*.jpg, pastes)
referencias/            Imágenes y esquemas médicos inline (SVG, JPG de pizarra clínica)
Libros y referencias/   PDFs (Manual 12 Octubre, KDIGO 2024, Sepsis 2026, etc.) — Git LFS
```

El **MOC - Urgencias** actúa como vista transversal: agrega las urgencias de cada especialidad (que siguen viviendo en `10_Patologias/`) más el contenido propio de `30_Urgencias/`.

## MOCs y Navegación

`90_MOCs/000_INICIO.md` es el hub central (y homepage de Quartz). Todos los MOCs siguen el patrón `MOC - ESPECIALIDAD.md` (MAYÚSCULAS):

| MOC                   | Especialidad                     |
| --------------------- | -------------------------------- |
| `MOC - CARDIOLOGIA`   | Cardiología                      |
| `MOC - NEUMOLOGIA`    | Neumología                       |
| `MOC - INFECCIOSAS`   | Infecciosas                      |
| `MOC - NEUROLOGIA`    | Neurología                       |
| `MOC - HEMATOLOGIA`   | Hematología                      |
| `MOC - DIGESTIVO`     | Digestivo                        |
| `MOC - NEFROLOGIA`    | Nefrología                       |
| `MOC - REUMATOLOGIA`  | Reumatología                     |
| `MOC - ENDOCRINO`     | Endocrinología                   |
| `MOC - ORL`           | ORL                              |
| `MOC - UROLOGIA`      | Urología                         |
| `MOC - TRAUMATOLOGIA` | Traumatología                    |
| `MOC - DERMATOLOGIA`  | Dermatología                     |
| `MOC - FARMACOS`      | Fármacos (por clase terapéutica) |
| `MOC - Urgencias`     | Hub transversal de urgencias     |

`Checklist - Manual 12 Octubre.md` — checklist de capítulos del Manual del 12 de Octubre vs notas existentes (~52% cubierto). Enlazado desde `000_INICIO.md`.

Al crear una nota nueva, **siempre** añadir su wikilink al MOC correspondiente.

## Taxonomía de Tags

Tags canónicos (lowercase, sin acentos, forma corta):

| Tag | Uso |
|---|---|
| `cardio`, `neuro`, `neumo`, `nefro`, `reuma`, `hemato` | Especialidades médicas |
| `endocrino`, `orl`, `uro`, `trauma`, `dermato` | Especialidades quirúrgicas/mixtas |
| `infecciosas`, `digestivo` | Sin abreviar |
| `urgencias` | Nota relevante para guardia |
| `patologia` | Nota de patología (no fármaco) |
| `farmaco` | Nota de fármaco |
| `moc` | Índice de navegación |
| `guardia`, `plantilla` | Registros y plantillas |

Formato YAML: `tags: [urgencias, cardio, patologia]` (inline) o multi-línea con `- tag`. Nunca usar mayúsculas ni acentos en tags.

## Note Creation Conventions

When creating medical Obsidian notes, follow this structure:
1. YAML frontmatter: `aliases`, `tags` (canonical), optional `description`
2. Definición
3. Etiología
4. Diagnóstico
5. Tratamiento
6. Links to related hub/MOC notes (`[[000_INICIO]]`, `[[MOC - ESPECIALIDAD]]`)

Use the `/newnote` skill for guided note creation — it handles folder routing, frontmatter, MOC updates, and git commit.

### Diagramas Mermaid

Quartz renderiza bloques ` ```mermaid ` con mermaid 11.x (estricto). Reglas para que rendericen igual en Obsidian y en Quartz:

- Texto de un nodo con `(`, `)`, `:`, `,`, `#`: envolver en comillas → `A["Nodo (con paréntesis)"]`.
- Etiquetas de arista con `<` o `>`: usar la sintaxis con pipes y comillas → `A -->|"< 120 min"| B`. Evitar `A -- < 120 min --> B`.
- Bloques mermaid dentro de listas numeradas: sacarlos del item (a nivel raíz, 0 espacios de indentación) o indentarlos 4 espacios — con 3 espacios el parser no detecta el code fence.

## Skills disponibles

### Skills (slash commands)

| Skill | Uso |
|---|---|
| `/newnote` | Crear nota médica guiada (folder routing, frontmatter, MOC update, git commit) |
| `/research` | Investigar un tema médico |
| `/organize` | Auditar y limpiar el vault |
| `/convert` | Convertir documento a nota de Obsidian |
| `/notes` | Pipeline PDF → múltiples notas de Obsidian |
| `/dosis` | Consulta rápida de dosis desde fichas de fármacos del vault |
| `/caso` | Formatear y registrar caso clínico para el portfolio |

### Agentes

| Agente | Uso |
|---|---|
| `note-reviewer` | Revisar calidad clínica y formal de una nota |
| `differential-diagnosis` | Diagnóstico diferencial estructurado desde presentación clínica |
| `clinical-linker` | Detectar wikilinks faltantes y notas huérfanas |
| `guardia-prep` | Resumen de referencia rápida para guardia o rotación |
| `vault-tracker` | Cobertura del vault, preparación para rotación, roadmap priorizado |
| `repaso` | Viñetas clínicas MIR y estudio activo desde notas del vault |

## Plantillas

Los archivos de plantilla (`99_Plantillas/`) fueron eliminados del repositorio. El plugin Templater sigue activo en Obsidian pero las notas nuevas se crean con el skill `/newnote`, que aplica la estructura estándar (frontmatter, secciones, MOC update) sin depender de archivos de plantilla.

## Git LFS (Large File Storage)

Los PDFs en `Libros y referencias/` se versionan con **Git LFS** (ver `.gitattributes`).

```bash
git lfs install     # una sola vez
git lfs pull        # descargar PDFs tras clonar
```

## Obsidian Local REST API

Plugin activo. Token en variable de entorno `OBSIDIAN_API_TOKEN` (nunca en git).
Puerto HTTP: 27123 · Puerto HTTPS: 27124

## Sincronización con GitHub

Repo privado: `git@github.com:xino00/MIR-apuntes.git`

```bash
~/Obsidian/MIR/sync.sh   # commit + push con fecha automática
```

Cron configurado: sync automático cada día a las 22:00.

## Web pública (Quartz)

URL: **https://mirapuntes.pages.dev**

Cada `git push` lanza automáticamente GitHub Actions → construye Quartz → despliega en Cloudflare Pages.

- Config: `.github/quartz.config.ts` (colores estilo Claude, locale es-ES, SPA, popovers, KaTeX)
- Workflow: `.github/workflows/deploy.yml`
- Homepage: `90_MOCs/000_INICIO.md` se copia como `index.md` antes del build
- Quartz se clona en `./quartz` (dentro del workspace del runner)
- Secrets: `CF_API_TOKEN`, `CF_ACCOUNT_ID` (Cloudflare Pages project: `mirapuntes`)
- Build cache activo (GitHub Actions cache v4), `NODE_ENV=production`, 4GB heap
- Optimizaciones documentadas en `.github/QUARTZ_OPTIMIZATIONS.md`
- Dependabot activo para GitHub Actions (`.github/dependabot.yml`)

**Verificar antes de push:** `npx quartz build` — nunca usar wikilinks en YAML frontmatter (rompe el build).

## Archivos excluidos

Estos archivos **NUNCA** deben subirse a git (están en `.gitignore`):

- `.obsidian/workspace.json`, `cache/`, `sync.json`, REST API `data.json` — estado local y credenciales (el resto de `.obsidian/` sí está en git para backup de plugins)
- `.claude/settings.local.json` — configuración local de Claude Code
- Tokens, credenciales, archivos `.env`

## Git Operations

When working with git operations, ALWAYS check `git status` and `git diff --staged` before committing. Never commit files without explicitly confirming what's being added. If unsure, ask the user before pushing.

## Shell Scripting

When writing shell scripts that process filenames, always handle spaces and special characters (use `find -print0 | xargs -0` or proper quoting). Many vault files have UTF-8 BOM (`ef bb bf`) — account for this when parsing frontmatter with shell tools.

## Agent & Parallel Task Rules

- When spawning parallel subagents, ensure they have Bash tool permissions before launching
- Place custom agents in `.claude/agents/` not `agents/`
- Never overwrite CLAUDE.md when creating new agents
- If a task can be done sequentially in under 5 minutes, prefer sequential over parallel
