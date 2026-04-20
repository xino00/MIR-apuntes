---
tags: [handoff, fact-check, continuacion]
fecha: 2026-04-20
description: "Handoff para próxima sesión de Claude — estado del fact-check del vault"
---

# Handoff — continuar fact-check del vault

**Última sesión cerrada:** 2026-04-20
**Estado:** ✅ **Fase 2 COMPLETA** (14/14 especialidades, 173 notas, 353 hallazgos, 41🔴)

---

## Lo que está hecho ✅

### Sub-fase 2a — reorganización de `Libros y referencias/`
- 51 PDFs reorganizados en 9 subcarpetas por especialidad (`01_General` … `09_Urgencias_FJD/ORL`) + `_archive/` con 9 duplicados/.txt/.md.
- `Libros y referencias/00_INDEX.md` creado (mapeo PDF → especialidad → notas).
- Git LFS preservado, 0 PDFs perdidos.

### Sub-fase 2b — auditoría 13 especialidades
3 olas de subagentes paralelos completadas. Informes consolidados en `00_Inbox/FACT_CHECK_2026-04-20/`:

| Archivo | Notas | Hallazgos |
|---|---|---|
| `01_Cardio.md` | 36 | 105 (13🔴) — Fase 1.5 previa |
| `02_Neuro.md` | 18 | 14 (2🔴) |
| `03_Infecciosas.md` | 15 | 26 (1🔴) |
| `04_Digestivo.md` | 18 | 27 (5🔴) |
| `05_Neumologia.md` | 17 | 16 (0🔴) |
| `06_Nefrologia.md` | 9 | 22 (1🔴) |
| `07_Reumatologia.md` | 10 | 34 (5🔴) |
| `08_Hematologia.md` | 9 | 16 (3🔴) |
| `09_Endocrino.md` | 3¹ | 16 (4🔴) |
| `10_ORL.md` | 9 | 14 (2🔴) |
| `11_Urologia.md` | 4 | 16 (1🔴) |
| `12_Traumatologia.md` | 15 | 21 (3🔴) |
| `13_Dermatologia.md` | 3 | 12 (1🔴) |
| `14_Psiquiatria.md` | 7 | 14 (0🔴) |
| **INDEX.md** | **173** | **353 (41🔴)** |

¹ Endocrino: solo 3 notas auditadas porque CAD y SHH están **vacías**.

---

## Pendiente para próximas sesiones ⏳

### Prioridad ALTA — antes de rotación cardio junio 2026

1. ✅✅ **Cardio aplicado 2026-04-20** — 95/105 hallazgos ✅ (90.5%), **13/13 🔴 críticos al 100%**. Recheck en `_recheck_cardio.md`. Pendiente solo revisar 7 ⚠ parciales y 2 ❌ no críticos.
2. ✅✅ **Dermato aplicado 2026-04-21** — 18/19 hallazgos ✅ (95%), **1/1 🔴 crítico al 100%**. Recheck en `_recheck_dermato.md`. Primera aplicación usando `/factcheck-apply`.
3. ✅✅ **Digestivo aplicado 2026-04-21** — 24/27 hallazgos ✅ (88.9%), **5/5 🔴 críticos al 100%**. Recheck en `_recheck_digestivo.md`. Sección PBE de Cirrosis rellenada.
4. **Aplicar correcciones críticas del resto de especialidades** (22🔴 restantes). Ver `INDEX.md` para top por ola.

5. **Reescribir 3 notas vacías** (urgencias vitales sin contenido):
   - `[[Cetoacidosis Diabética (CAD)]]` — Manual cap.51 + ADA-EASD 2024
   - `[[Síndrome Hiperglucémico Hiperosmolar (SHH)]]` — Manual cap.51
   - `[[Sdme Hemofagocitico]]` — Manual p.1284 Tabla 5 (HLH-2004) + H-Score + dexa+etopósido

### Prioridad MEDIA

3. **Revisar ⚠ parciales / ❌ pendientes de cardio** (9 en total, 0 críticos). Ver `_recheck_cardio.md` sección "Pendientes y parciales".
4. **Re-auditoría con WebFetch autorizado** — 8 especialidades de Fase 2 tienen verificación parcial:
   - Reumato (EULAR/ACR/KDIGO 2024)
   - Dermato (AEDV Shingrix, EAACI urticaria, CDC escabiosis)
   - Trauma (Ottawa Ankle/Knee, profilaxis tetánica MSC España)
   - Psiq (FDA citalopram, NICE autolesión, APA)
   - Otras: Neuro, Infecciosas, Nefro, Endo (parcial)

5. **Trazabilidad**: añadir `last_fact_checked: 2026-04-20` al frontmatter de las 173 notas auditadas (cardio ya tiene las 36 ✅).

### Prioridad BAJA

6. Considerar skill `/factcheck` reutilizable si se quiere reauditar periódicamente.
7. Cruzar con UpToDate/DynaMed las áreas con guías más volátiles (oncohematología, terapias dirigidas).

---

## Cómo retomar en próxima sesión

**Si el residente dice "aplicar críticos cardio":**
1. Leer `01_Cardio.md` — los 13🔴 están listados al principio.
2. Para cada nota mencionada, abrir el archivo en `10_Patologias/01_Cardio/`, aplicar el "Cambio sugerido" tal cual.
3. Commit por bloque (FA, HTA, SCA, IC, etc.).

**Si el residente dice "reescribir CAD/SHH":**
1. Leer `09_Endocrino.md` — el subagente ya redactó el "Contenido clínico mínimo que debe figurar" con citas literales del Manual.
2. Crear notas nuevas con esa estructura, frontmatter completo, wikilinks al MOC.

**Si el residente dice "re-auditar X con web":**
1. Verificar que WebFetch está autorizado en la sesión actual.
2. Leer `<NN>_<Especialidad>.md` para ver hallazgos preliminares y limitaciones.
3. Lanzar subagente con instrucción explícita de cubrir las verificaciones que se marcaron como "no realizadas por WebFetch denegado".

**Si el residente dice "git commit":**
- Cambios pendientes:
  - `00_Inbox/FACT_CHECK_2026-04-20/` (15 archivos nuevos + INDEX actualizado)
  - `Libros y referencias/` (reorganización completa)
  - `Libros y referencias/00_INDEX.md` (nuevo)
  - **No hay cambios en `10_Patologias/`** (política "solo informe").

---

## Reglas vinculantes que se han respetado

- **Source policy** (`feedback_source_policy`): cada hallazgo con cita literal + página/sección. Sin cita, no entra al informe.
- **No tocar `10_Patologias/`**: solo informes en `00_Inbox/`.
- **Severidades**: 🔴 Crítico · 🟠 Moderado · 🟢 Menor · ⚪ Informativo.
- **`[OUTDATED-MANUAL]`**: Manual 12 Oct desactualizado por guía posterior.
- **YAML sin wikilinks raw**: comprobado en todos los informes.

---

## Métricas de la sesión 2026-04-20

- Subagentes lanzados: 13 (5 ola 1 + 5 ola 2 + 3 ola 3) en background paralelo.
- Tiempo total estimado: ~3 horas reloj (incluye reorganización filesystem).
- PDFs movidos: 51 (0 perdidos, LFS preservado).
- Líneas de informe generadas: ~7.000 entre los 14 archivos de especialidad.
