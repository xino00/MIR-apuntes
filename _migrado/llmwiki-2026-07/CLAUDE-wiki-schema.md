# CLAUDE.md — Wiki Clínica MIR (patrón LLM Wiki)

Guía para Claude Code al trabajar en este repositorio.

## Qué es esto

Un **LLM Wiki médico**: una base de conocimiento clínico persistente y compuesta que **el LLM crea y mantiene** sobre fuentes autorizadas. Usuario: residente de Medicina de Familia (Madrid), rotaciones por todo el hospital + guardias de puerta. Uso principal: referencia clínica en guardia y rotación.

Tres capas:
1. **Raw (inmutable)** — `Libros y referencias/`: PDFs de guías en Git LFS + su `.md` extraído (cache local). El LLM **lee** de aquí, nunca lo edita. Es la fuente de verdad.
2. **Wiki (lo genera/mantiene el LLM)** — las páginas markdown (`patologias/`, `farmacos/`, …). El LLM es dueño total de esta capa.
3. **Schema** — este archivo. Define estructura, convenciones y flujos.

> El usuario trata esto como **una carpeta, no un repositorio git**. No hacer commits, branches, ni pushes salvo petición explícita. Ver "Borrado seguro".

## 🔴 Regla de oro — fuentes

**NUNCA inventar contenido clínico.** Solo reorganizar, deduplicar o sintetizar lo que ya está respaldado por las fuentes existentes (`Libros y referencias/`, Manual del 12 de Octubre, guías ESC/AHA/sociedades oficiales). Toda dosis/cifra/tabla lleva **atribución de fuente**. Conservar `fuente:` y `last_fact_checked:` al refundir. Ante duda: **marcar, no rellenar**. Evitar fuentes terciarias (ecgwaves, LITFL, Medscape).

### Jerarquía de evidencia (ante conflicto entre fuentes)

1. Protocolo local del hospital / Manual del 12 de Octubre
2. Fichas técnicas oficiales (CIMA/AEMPS) — para posología
3. Guías de sociedades (ESC, AHA, GOLD, ERS, IDSA…) — la más reciente
4. Revisiones sistemáticas / RCTs citados por las guías
5. Manuales generales y apuntes propios

Ante conflicto entre niveles, **no fusionar en silencio**: callout de contradicción (ver abajo) indicando el nivel de cada claim.

## Estructura del wiki

```
index.md            homepage + catálogo global por categoría
log.md              registro cronológico append-only  (## [YYYY-MM-DD] op | título)
CLAUDE.md           este schema
patologias/<esp>/   páginas-ENTIDAD: 1 por enfermedad/síndrome  (14 especialidades)
farmacos/           páginas-ENTIDAD: 1 por fármaco (posología primero)
urgencias/          protocolos de manejo agudo;  urgencias/MUST/ = TEXTO PLANO PURO
presentaciones/     entradas sindrómicas (disnea, dolor torácico, síncope, shock…)
sintesis/           síntesis por especialidad (SUSTITUYEN a los MOCs) + comparativas
plantillas/         plantillas de documentación de guardia (policlínica, boxes)
casos/              casos clínicos DE-IDENTIFICADOS (se crea con el primer caso)
gaps.md             lagunas de conocimiento pendientes de fuente (alimenta el lint)
Libros y referencias/   RAW inmutable (PDF en LFS + .md cache)
_migrado/           papelera de migración: originales refundidos + organización antigua.
                    NO se publica. La purga definitiva la confirma el usuario.
```

Navegación = `index.md` + tags + wikilinks + páginas `sintesis/<esp>.md`. **No hay MOCs** (retirados a `_migrado/`; su rol lo cumplen las síntesis, que integran en vez de solo listar).

## Frontmatter (schema de página)

```yaml
title: Nombre legible
aliases: [sinónimos, abreviaturas]
type: patologia          # patologia | farmaco | concepto | presentacion | sintesis | plantilla | caso
tags: [neumo, infecciosas, patologia]   # canónicos (ver tabla)
fuente: "Guía/Manual + capítulo"        # atribución
sources: ["Libros y referencias/…​.pdf"] # qué raw alimenta la página (opcional, para lint/Dataview)
last_fact_checked: YYYY-MM-DD            # si se verificó contra guía
updated: YYYY-MM-DD
contradiction: false                     # true si hay un callout de contradicción sin resolver
```

**NUNCA wikilinks `[[ ]]` dentro del YAML** — rompe el build de Quartz. Lo veta `scripts/check-calidad.sh`. Wikilinks solo en el cuerpo, y **siempre** wikilinks (nunca links markdown) para enlaces internos.

## Taxonomía de tags (canónicos, lowercase, sin acentos)

| Tag | Uso |
|---|---|
| `cardio`, `neuro`, `neumo`, `nefro`, `reuma`, `hemato` | Especialidades médicas |
| `endocrino`, `orl`, `uro`, `trauma`, `dermato` | Especialidades quirúrgicas/mixtas |
| `infecciosas`, `digestivo`, `psiquiatria` | Sin abreviar |
| `hta`, `epoc`, `cot` | Áreas/subtemas |
| `urgencias` | Relevante para guardia |
| `patologia`, `farmaco`, `plantilla`, `caso` | Tipo de nota |

## Cuerpo de la página — pragmático

Sigue la estructura de la **guía-fuente**, no un molde rígido. Prioridades:
- **Accionable arriba:** en notas de urgencias o largas, empezar con `> [!danger] ⚡ Guardia` (acción inmediata, dosis clave, criterio ingreso/alta) antes de la teoría.
- **Fichas de fármacos: posología primero.** Orden: Posología y administración → Indicaciones → Contraindicaciones → RAM → Mecanismo → Relacionados.
- **Dosis con fuente** entre paréntesis: `(Manual p. X)` / `(CIMA)` / `(GOLD 2026)`.
- **Evidencia vs. interpretación** — cuando la distinción importe, marcar en el cuerpo:
  - `**Fuente:**` claim directo de la guía/manual (con cita, como siempre).
  - `**Síntesis:**` integración/comparación elaborada por el LLM a partir de las fuentes.
  - `**Confirmar localmente:**` dosis, criterios de ingreso/alta o antibiótico donde el protocolo del hospital puede diferir de la guía.
  - `> Fuente pendiente.` claim clínicamente relevante sin respaldo en el raw actual → registrarlo también en `gaps.md`.
  - **Sin lenguaje absoluto no respaldado** en contenido clínico ("siempre", "nunca", "descarta por completo"); preferir "se recomienda en…", "según [fuente]…".
- **MUST (`urgencias/MUST/`): texto plano puro** — sin frontmatter, sin wikilinks, sin callouts. Son guías para compartir con otros R1; no "corregir" su formato.

### Mermaid (Quartz, mermaid 11.x estricto)
- Nodo con `(` `)` `:` `,` `#`: entre comillas → `A["Nodo (con paréntesis)"]`.
- Label de arista con `>` al inicio: rompe (blockquote). Prefijar con texto (`"ICP > 120 min"`) o usar `≤`/`≥`.
- Mermaid en lista numerada: sacarlo a nivel raíz (0 espacios) o indentar 4.

## Las tres operaciones

### Ingest — fuente nueva → wiki
1. Colocar el PDF en `Libros y referencias/<esp>/` (LFS). Convertir a `.md` cache (marker / markitdown).
2. Leer, extraer y comentar los puntos clave con el usuario.
3. **Crear o ACTUALIZAR** las páginas de entidad + la síntesis afectadas (solo contenido con fuente).
4. **Flag de contradicciones** contra lo existente (ver abajo).
5. Actualizar `index.md` y **append** a `log.md`: `## [fecha] ingest | Título`.

### Query — preguntar al wiki
Leer `index.md` → páginas relevantes → responder **con citas**. Las buenas respuestas (comparativas, diferenciales, síntesis) **se archivan** como página en `sintesis/` + `index.md` + `log.md`. Así las exploraciones se acumulan, no se pierden en el chat.

### Lint — revisión periódica
Buscar: contradicciones página↔página, claims obsoletos (vs `last_fact_checked` o raw más reciente), páginas huérfanas, conceptos citados sin página, cross-refs faltantes, gaps de cobertura. Los gaps detectados se **acumulan en `gaps.md`** (fecha + página de origen); se retiran al resolverse con el ingest de la fuente que faltaba. Registrar en `log.md`: `## [fecha] lint | …`.

## Contradicciones (la pieza que faltaba)

Al ingerir o lintar, comparar el contenido nuevo con las páginas existentes. Si una fuente contradice a una página:
1. Insertar en el cuerpo `> [!warning] Contradicción` con **ambos** claims + fechas + fuentes.
2. Poner `contradiction: true` en el frontmatter (Dataview puede listar "contradicciones a resolver").
3. Append a `log.md`: `## [fecha] contradiction | tema`.

Severidad orientativa 🔴 (peligrosa) / 🟠 (relevante) / 🟢 (matiz). Resolver es decisión clínica del usuario.

## Casos clínicos — de-identificación obligatoria

Los casos vividos en guardia/rotación van a `casos/` (la carpeta se crea con el primero). **Nunca almacenar información identificable del paciente.** Antes de guardar, eliminar o generalizar:
- Nombre, iniciales, nº de historia, fechas exactas, hospital/centro concreto.
- Edad exacta si no aporta (→ "anciano", "joven"); combinaciones raras de rasgos que identifiquen.
- Nombres de familiares o clínicos.

Títulos genéricos: `Caso — Disnea aguda en anciano.md`. Frontmatter `type: caso` + tag de especialidad + `caso`. Si el material que aporta el usuario parece identificable → **parar y pedirle que lo de-identifique** antes de añadirlo.

## Borrado seguro (sin git como red)

Como el usuario no usa git aquí, **no hay backup automático**. Para no destruir contenido clínico:
- **Refundir una nota** = crear la(s) página(s) nueva(s) y **MOVER el original a `_migrado/`**, nunca `rm`.
- **Reubicar una nota limpia** (sin reestructurar) = `mv` directo a la carpeta nueva.
- La **purga definitiva de `_migrado/`** la ejecuta el usuario con una confirmación explícita, al final.
- Comillas siempre: los nombres tienen espacios, acentos y paréntesis.

## Publicación (Quartz)

URL: **https://mirapuntes.pages.dev**. Cada push → GitHub Actions → Cloudflare Pages.
- Config `.github/quartz.config.ts`; workflow `.github/workflows/deploy.yml`.
- **Homepage = `index.md`** (en la raíz). Ignorar `_migrado`, `Libros y referencias`, `CLAUDE.md`, `AGENTS.md`.
- **Gate antes de publicar:** `bash scripts/check-calidad.sh` (detecta wikilinks-en-YAML + texto corrupto). Verificar build con `npx quartz build`.
- ⚠️ Hay un **cron a las 22:00 que hace push** (`sync.sh`) → publicaría trabajo a medias. Pausarlo durante migraciones grandes.

## Otros

- **Git LFS** para los PDFs de `Libros y referencias/` (ver `.gitattributes`): `git lfs pull` tras clonar.
- **Obsidian Local REST API** activa; token en `OBSIDIAN_API_TOKEN` (nunca en git). Puertos 27123 (HTTP) / 27124 (HTTPS).
- **Shell:** manejar nombres con espacios/acentos con comillas o `find -print0 | xargs -0`. Muchos `.md` tienen BOM UTF-8.

## Estado de la migración (2026-07)

Reconstrucción al patrón LLM Wiki en curso. **Refundido:** núcleo de Neumología (NAC, sCAP, Bronquitis, EPOC exacerbación, IRA, SDRA). **Retirado a `_migrado/`:** MOCs, skills y agentes antiguos. Pendiente: resto de especialidades, fármacos, urgencias, presentaciones, y la purga final de `_migrado/`. Ver `log.md` para el detalle cronológico.
