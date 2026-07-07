---
name: score
description: >-
  This skill should be used when the user asks for "calcula el [score]",
  "score de [nombre]", "puntuación CHA2DS2-VA", "Wells", "qSOFA", "GRACE",
  "CURB-65", "FINE", "MELD", "Child-Pugh", "HAS-BLED", or any clinical
  scoring system during a shift. Calculates the score using the definition
  stored in the vault. Never fabricates criteria from general knowledge —
  if the score isn't documented in the vault, instructs the user to create
  the note first.
---

# /score — Calculadora de Scores Clínicos

Calcula scores clínicos durante guardia leyendo la definición desde notas del vault. Diseñado para uso al pie de cama.

## Usage

```
/score <nombre-score> [variables del paciente]
```

Ejemplos:
- `/score CHA2DS2-VA mujer 75a HTA DM ictus previo`
- `/score Wells TVP edema unilateral encamado neoplasia activa`
- `/score qSOFA TAS 95 FR 24 obnubilado`
- `/score GRACE` *(sin variables → preguntas guiadas)*

Acepta el nombre con o sin subíndices Unicode: `CHA2DS2-VA` ≡ `CHA₂DS₂-VA`.

## Steps

### 1. Resolver el score en el vault

Buscar el archivo que define el score (case-insensitive, tolerante a acentos y subíndices):

```
Glob: 10_Patologias/**/*.md
Glob: 30_Urgencias/**/*.md
```

Estrategia de matching:
1. **Por filename:** `Escala <nombre>*.md`, `<nombre>.md`, archivos que contengan el nombre del score.
2. **Por aliases:** leer frontmatter de candidatos y comprobar `aliases:` (allí está la forma ASCII como `CHA2DS2-VA`).
3. **Por contenido:** si los anteriores fallan, `Grep` el nombre del score en `10_Patologias/` para encontrar notas que lo embeban (ej: `H2FPEF` está dentro de `Insuficiencia cardiaca.md`).

Si **no se encuentra** ninguna nota fuente, parar y devolver:

> **Score `<nombre>` no documentado en el vault.**
> Crea la nota con `/research <nombre>` o `/newnote` y vuelve a intentarlo.
> No voy a calcular criterios desde conocimiento general (source policy).

**Nunca fabricar la definición del score.** Si el archivo existe pero no contiene tabla de puntuación clara, reportar la ambigüedad y parar.

### 2. Extraer la tabla de puntuación

Leer la nota fuente. Localizar la tabla con formato:

```
| Letra/Variable | Factor | Puntos |
|---|---|---|
```

o variantes (`| Variable | Puntos |`, `| Criterio | Pts |`).

Extraer también:
- Tabla de **interpretación clínica** (rangos de puntuación → actitud).
- Cualquier **callout** (`> [!warning]`, `> [!info]`) con matices clínicos relevantes (cambios de guía, casos especiales).
- Línea **`fuente:`** del frontmatter.

### 3. Decidir input mode (híbrido por longitud)

**Modo A — Prompt libre** (scores con ≤6 variables):
- CHA2DS2-VA, HAS-BLED, Wells (TVP/TEP), qSOFA, CURB-65, Centor, Alvarado.
- Parsear las variables del prompt del usuario contra la tabla extraída.
- Para cada variable de la tabla, decidir si está presente:
  - Match explícito por palabra clave: "HTA", "diabetes", "ictus", "75a" → A₂.
  - Si una variable de la tabla **no se menciona en el prompt**, tratarla como ausente (puntos = 0) y listarla aparte como "asumido ausente".

**Modo B — Preguntas guiadas con `AskUserQuestion`** (scores con >6 variables, o cuando el usuario invoca sin datos):
- GRACE, FINE/PSI, MELD-Na, Child-Pugh, APACHE II, SOFA completo.
- Para cada variable, plantear pregunta con opciones (presente/ausente, rangos numéricos, categoría). Máximo 4 preguntas por bloque (límite de la tool); agrupar variables relacionadas.
- Para variables numéricas continuas (creatinina, bilirrubina, edad), pedir el valor en formato libre.

Si el usuario invoca un score corto sin datos, también usar Modo B.

### 4. Calcular y formatear output

Sumar puntos según la tabla extraída. Buscar la fila de interpretación que aplica al total.

Output **compacto, una sola pantalla**, listo para guardia:

```
**[Nombre del score]** — [puntuación] / [máximo]

| Variable | Presente | Puntos |
|---|---|---|
| [Variable 1] | ✅ / ❌ | [pts] |
| ...           | ...    | ...   |

**Total: [N] puntos**

🎯 **Interpretación:** [actitud según tabla del vault]

⚠️ [Callout relevante si aplica — ej: "MCH/amiloidosis: anticoagular siempre, independiente del score"]

📎 **Fuente:** [valor de `fuente:` del frontmatter]
🔗 [[Nombre exacto de la nota fuente]]
```

### 5. Trazabilidad obligatoria

Cada cálculo debe terminar con:
- Wikilink **exacto** al archivo fuente (sin inventar el nombre — usar el filename real sin la extensión `.md`).
- Cita literal del campo `fuente:` del frontmatter si existe.
- Si la nota fuente no tiene `fuente:`, marcar: *"sin campo `fuente:` en la nota — verificar contra guía oficial"*.

## Constraints

- **NUNCA fabricar criterios o puntos** desde conocimiento general. Si la nota no está en el vault, parar y pedir crear la nota.
- **NUNCA inferir umbrales** que no estén en la tabla del vault. Si el vault dice "≥2 puntos → anticoagular", no recalcular el cutoff.
- **Read-only.** No modifica notas, no escribe en MOCs, no crea archivos.
- **Velocidad sobre completitud.** Una pantalla, sin párrafos largos. El residente está en boxes.
- **Source policy.** Alineada con `memory/feedback_source_policy.md`: el vault es la única fuente de verdad clínica.
- **Subíndices Unicode.** Tolerar matching ASCII ↔ Unicode (`CHA2DS2-VA` ≡ `CHA₂DS₂-VA`, `H2FPEF` ≡ `H₂FPEF`).
- **Ambigüedad explícita.** Si una variable del prompt es ambigua (ej: usuario dice "anciano" sin edad concreta), preguntar antes de asumir.
