---
name: caso
description: >-
  This skill should be used when the user asks to "escribir un caso clínico",
  "formatear un caso", "registrar un caso de guardia", "caso clínico de [patología]",
  "documentar un caso", or wants to save a clinical case for the portfolio.
  Formats user-provided clinical data into a structured case presentation and saves to the vault.
---

# /caso — Registro de Caso Clínico

Formatea datos clínicos del usuario en una presentación de caso estructurada y la guarda en el vault.

## Usage

```
/caso
/caso <descripción breve del caso>
```

Sin argumentos lanza modo interactivo. Con descripción, usa esos datos como punto de partida.

## Steps

### 1. Recoger datos clínicos

Si el usuario no proporcionó datos suficientes, preguntar por:

- **Edad/sexo** (anónimo: "Varón de 67 años", nunca nombre ni NHC)
- **Motivo de consulta**
- **Antecedentes relevantes**
- **Enfermedad actual**
- **Exploración física**
- **Pruebas complementarias** (analítica, imagen, ECG...)
- **Juicio clínico / diagnóstico diferencial**
- **Plan terapéutico**
- **Servicio y fecha**

Aceptar lo que el usuario dé — no exigir todos los campos. Si falta algo crítico (al menos motivo de consulta + juicio clínico), preguntar una sola vez.

### 2. Crear el archivo

Destino: `40_Casos clinicos/Caso - [Dx Principal] [YYYY-MM-DD].md`

Si el directorio no existe:
```
Bash: mkdir -p "/home/arenas/Obsidian/MIR/40_Casos clinicos"
```

Frontmatter:
```yaml
---
tags:
  - caso-clinico
  - <specialty>       # lowercase, sin acentos (cardio, neuro, digest, etc.)
aliases:
  - <dx principal abreviado>
fecha: YYYY-MM-DD
servicio: <servicio donde se vio el caso>
---
```

Body structure:
```markdown
# Caso — [Dx Principal]

## Motivo de consulta
[...]

## Antecedentes personales
[...]

## Enfermedad actual
[...]

## Exploración física
[...]

## Pruebas complementarias
[...]

## Juicio clínico
[...]

## Diagnóstico diferencial
[...]

## Plan terapéutico
[...]

## Reflexión / Learning points
[...]
```

Omitir secciones para las que no hay datos. No inventar contenido.

### 3. Cross-reference con el vault

Buscar entidades mencionadas (patologías, fármacos) en el vault:

```
Grep: 10_Patologias/**/*.md y 20_farmacos/*.md
```

Para cada coincidencia, añadir `[[wikilinks]]` en el body (NUNCA en YAML). Ejemplo: si el caso menciona "furosemida" y existe `20_farmacos/Furosemida.md`, reemplazar con `[[Furosemida]]`.

### 4. Git commit

```
Bash: cd /home/arenas/Obsidian/MIR && git add "40_Casos clinicos/Caso - [Dx Principal] [YYYY-MM-DD].md" && git commit -m "caso: [Dx Principal] [fecha]"
```

### 5. Confirmar al usuario

Mostrar:
- Ruta del archivo creado
- Número de wikilinks añadidos
- Secciones incluidas

Ofrecer: "¿Quieres añadir algo más al caso o enlazarlo desde algún MOC?"

## Constraints

- **NUNCA generar contenido clínico** que el usuario no haya proporcionado. Solo formatear y estructurar lo dado.
- **Anonimización obligatoria**: si el usuario incluye nombre, NHC, o datos identificativos, eliminarlos y sustituir por descriptores genéricos (edad/sexo).
- **Tags canónicos**: lowercase, sin acentos, según la lista en CLAUDE.md.
- **NUNCA poner wikilinks en YAML frontmatter.**
- **Secciones vacías**: omitir, no dejar placeholders.
