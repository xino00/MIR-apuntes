---
title: MIR · Wiki Clínica
type: index
updated: 2026-07-01
---
# 🏥 Wiki Clínica MIR — Índice

Referencia clínica para guardia y rotaciones (Medicina de Familia). Wiki mantenido por LLM sobre fuentes autorizadas (`Libros y referencias/`). **Cada página cita su fuente**; el campo `last_fact_checked` marca lo verificado contra guía.

> [!danger] ⚡ Supervivencia en guardia
> [[presentaciones/disnea-aguda|Disnea aguda]] · [[presentaciones/dolor-toracico|Dolor torácico]] · [[presentaciones/shock|Shock]] · [[presentaciones/sincope|Síncope]]

## 📚 Especialidades (páginas de síntesis)

Las síntesis sustituyen a los antiguos MOCs: no son listas de enlaces, sino la visión integrada de cada especialidad con los enlaces embebidos.

- 🫁 [[Neumología]]  ·  ❤️ [[Cardiología]]  ·  🦠 [[Infecciosas]]
- 🧠 [[Neurología]]  ·  🩸 [[Hematología]]  ·  🍽️ [[Digestivo]]
- 🫘 [[Nefrología]]  ·  🦴 [[Reumatología]]  ·  🧬 [[Endocrino]]
- 👂 [[ORL]]  ·  🚹 [[Urología]]  ·  🦵 [[Traumatología]]
- 🧴 [[Dermatología]]  ·  🧩 [[Psiquiatría]]

*(Las síntesis en rojo aún no existen — se poblarán durante la migración.)*

## 🗂️ Categorías

| Capa | Carpeta | Contenido |
|---|---|---|
| Patologías (entidad) | `patologias/<especialidad>/` | Una página por enfermedad/síndrome |
| Fármacos (entidad) | `farmacos/` | Una ficha por fármaco (posología primero) |
| Urgencias / protocolos | `urgencias/` | Manejo agudo; `urgencias/MUST/` = texto plano puro |
| Presentaciones | `presentaciones/` | Entradas sindrómicas (disnea, dolor torácico…) |
| Síntesis y comparativas | `sintesis/` | Visión integrada por especialidad + comparativas |
| Plantillas de guardia | `plantillas/` | Plantillas de documentación clínica |
| Casos clínicos | `casos/` | Casos **de-identificados** (se crea con el primero) |
| Fuentes (raw, inmutables) | `Libros y referencias/` | PDFs de guías; el LLM lee, nunca edita |

## 🔧 Cómo funciona este wiki

- **Ingest:** una fuente nueva → se lee → se crean/actualizan páginas → se marcan contradicciones → se registra en [[log]].
- **Query:** se pregunta al wiki; las buenas respuestas se archivan como página de `sintesis/`.
- **Lint:** revisión periódica (contradicciones, huérfanas, claims obsoletos) registrada en [[log]]; las lagunas detectadas se acumulan en [[gaps]].

Convenciones y flujos completos en `CLAUDE.md`. Registro cronológico en [[log]].

## 🚧 Estado de la migración
Piloto en curso: **Neumología** (clúster NAC/sCAP). Ver [[log]].
