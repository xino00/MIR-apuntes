# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Obsidian medical notes vault using wikilinks (`[[Note Name]]`). When creating or editing notes, always use wikilink syntax for internal links, never standard markdown links. Ensure YAML frontmatter never contains raw wikilinks — use plain text or quoted strings in frontmatter fields.

## Contexto

Vault de Obsidian de un residente de Medicina de Familia en Madrid. Rotaciones por todos los servicios del hospital + guardias de urgencias de puerta. Uso principal: referencia clínica durante rotaciones, protocolos de guardia y registro de casos clínicos anónimos.

## Estructura del Vault

```
10_Patologias/          Patología crónica/electiva por especialidad
  01_Cardio/            02_Neuro/  03_Infecciosas/  04_Digestivo/
  05_Neumologia/        06_Nefrologia/  07_Reumatologia/  08_Hematologia/

20_farmacos/            ~130 fichas de fármacos (una por archivo)

30_Urgencias/           Hub central de guardia
  Patologia_Aguda/      Shock, SDRA, IRA, Dolor torácico, Disnea
  Ionico_AcidoBase/     Iones, equilibrio ácido-base
  Exploracion_Fisica/   Exploración de Rodilla, Tobillo y Antepié

40_Casos clinicos/      Casos clínicos anónimos (vacío, plantilla disponible)
50_Guardias/            Registros de guardia por fecha
60_Pase de planta/      Notas de pase (vacío, plantilla disponible)
90_MOCs/                Índices de navegación por especialidad
99_Plantillas/          Plantillas Templater
Libros y referencias/   PDFs (Manual 12 Octubre, KDIGO 2024, Sepsis 2026, etc.)
```

El **MOC - Urgencias** actúa como vista transversal: agrega las urgencias de cada especialidad (que siguen viviendo en `10_Patologias/`) más el contenido propio de `30_Urgencias/`.

## Git LFS (Large File Storage)

Los PDFs en `Libros y referencias/` se versionan con **Git LFS** para mantener el repositorio ligero.

**Requisitos:**
```bash
# 1. Instalar Git LFS
sudo dnf install git-lfs    # Fedora
sudo apt-get install git-lfs # Ubuntu/Debian
brew install git-lfs         # macOS

# 2. Inicializar Git LFS (una sola vez)
git lfs install
```

**Clonar con Git LFS:**
```bash
git clone git@github.com:xino00/MIR-apuntes.git
cd MIR-apuntes
git lfs pull    # Descargar PDFs
```

**Si ya clonaste sin LFS:**
```bash
git lfs pull    # Ahora descarga los PDFs correctamente
```

Los PDFs nuevos en `Libros y referencias/` se rastrean automáticamente con LFS (ver `.gitattributes`).

## Obsidian Local REST API

El vault tiene el plugin **Local REST API** activo. Para usar con scripts:

⚠️ **IMPORTANTE:** El token es una credencial sensible - **NUNCA lo guardes en git** (incluso en repos privados/públicos).

```bash
# 1. Generar token en Obsidian:
#    Settings → Community plugins → Local REST API → Generate new API token

# 2. Guardar en variable de entorno (en tu máquina, NO en git):
export OBSIDIAN_API_TOKEN="<tu_token_aqui>"

# 3. Usar en comandos:
curl http://localhost:27123/active/ \
  -H "Authorization: Bearer $OBSIDIAN_API_TOKEN"

curl -X POST "http://localhost:27123/open/ruta%2Fnota.md" \
  -H "Authorization: Bearer $OBSIDIAN_API_TOKEN"
```

**Para guardar permanentemente:**
```bash
echo 'export OBSIDIAN_API_TOKEN="<tu_token>"' >> ~/.bashrc
source ~/.bashrc
```

Puerto HTTP: 27123 · Puerto HTTPS: 27124

## Sincronización con GitHub

Repo privado: `git@github.com:xino00/MIR-apuntes.git`

```bash
~/Obsidian/MIR/sync.sh   # commit + push con fecha automática
```

Cron configurado: sync automático cada día a las 22:00.

## Web pública (Quartz)

URL: **https://mirapuntes.pages.dev**

Cada `git push` lanza automáticamente GitHub Actions → construye Quartz → despliega en Cloudflare Pages. No requiere ninguna acción manual.

Configuración en `.github/quartz.config.ts` (colores estilo Claude, locale es-ES).
El workflow está en `.github/workflows/deploy.yml` (nombre: "Deploy Quartz to Cloudflare").
La homepage se genera copiando `90_MOCs/000_INICIO.md` como `index.md` antes del build.

Quartz se clona en `./quartz` (dentro del workspace del runner), no en `/tmp/quartz`, para que `actions/setup-node` pueda resolver el cache de npm con ruta relativa.

Secrets necesarios en GitHub: `CF_API_TOKEN` y `CF_ACCOUNT_ID` (Cloudflare Pages project: `mirapuntes`).

## Archivos excluidos del repositorio

Estos archivos **NUNCA** deben subirse a git (están en `.gitignore`):

- `.obsidian/workspace.json` — estado de UI local de Obsidian
- `.claude/settings.local.json` — configuración local de Claude Code
- Tokens, credenciales, archivos `.env`

Antes de hacer commit, verificar que `git status` no incluya estos archivos. Usar siempre el `.gitignore` del repo.

## Note Creation Conventions

When creating medical Obsidian notes, follow this structure: 1) YAML frontmatter with tags, 2) Definición, 3) Etiología, 4) Diagnóstico, 5) Tratamiento, 6) Links to related hub/MOC notes. Always add the new note's wikilink to the relevant hub note.

## Deployment

The vault is deployed via Quartz on Cloudflare Pages at mirapuntes.pages.dev. After making changes, run `npx quartz build` to verify the build succeeds before committing. Never use wikilinks inside YAML frontmatter as this breaks Quartz builds.

## Plantillas disponibles

| Plantilla | Uso |
|---|---|
| `TPL - Farmaco.md` | Nueva ficha de fármaco |
| `TPL - Patologia.md` | Nueva nota de patología |
| `TPL - Casos clinicos.md` | Caso clínico anónimo |
| `TPL - Guardia.md` | Registro de guardia |
| `TPL - PASE DE PLANTA.md` | Pase de planta |
