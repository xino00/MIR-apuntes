# Recheck fact-check Hematología — 2026-05-19

## Resumen

- **Total hallazgos del informe:** 18
- **APLICADOS verificados:** 9/9 ✅
- **SKIPPED intactos:** 9/9 ✅
- **🔴 Crítico pendiente (esperado):** 1/1 (H18 HLH)

---

## Tabla APLICADOS (los 9 que sí se intentaron aplicar)

| # | Sev | Nota | Estado | Evidencia |
|---|---|---|---|---|
| 1 | 🟢 | Anemia - Abordaje General | ✅ APLICADO | Líneas 20-22: tabla embarazo con 3 trimestres (1T <11, 2T <10.5, 3T <11) — exactamente como en informe |
| 2 | ⚪ | Anemia - Abordaje General | ✅ APLICADO | Líneas 31-32: callout "Adultos mayores (>70 años)" con P5 11.7 g/dL (♂) y 10.9 g/dL (♀) |
| 3 | 🟢 | Anemia - Abordaje General | ✅ APLICADO | Línea 29: "en estado estable: ~25.000-100.000/µL (1-2%)" — presente en callout de reticulocitos |
| 7 | ⚪ | Anemia Microcítica | ✅ NO VERIFICABLE | Líneas 55-57: "Índice de Mentzer = MCV/RBC: <13 → talasemia" — concordancia exacta, sin cambio necesario (verificación positiva) |
| 11 | 🟢 | Anemia Hemolítica - Abordaje | ✅ NO VERIFICABLE | Línea 33: "Combinación LDH normal + haptoglobina normal → 92% sensibilidad" — exacto de la fuente, sin cambio |
| 13 | 🟢 | Anemia Normocítica | ✅ APLICADO | Línea 78: "objetivo Hb 10-11,5 g/dL (KDIGO 2024 — evitar normalización por ↑ mortalidad/IAM/ACV en CHOIR/CREATE/TREAT)" — contiene todos los elementos del cambio sugerido |
| 14 | 🟠 | ACD-AI | ✅ APLICADO | Línea 56: "Hb 10-11 g/dL (leve); 8-10 g/dL (moderada). Hb <8 g/dL en ~20%..." — cambio aplicado de 10-12 → 10-11 |
| 15 | 🟢 | ACD-AI | ✅ NO VERIFICABLE | Línea 58: "Reticulocitos absolutos frecuentemente <25.000/µL" — exacto de la fuente, sin cambio |
| 16 | 🟢 | ACD-AI | ✅ APLICADO | Línea 97: "Ferritina >200 mcg/L excluye ferropenia... en algunos países umbral hasta 400 mcg/L. En diálisis: <500 mcg/L + TSAT <30% como criterio funcional para hierro IV (KDIGO 2024)" — todos los elementos presentes |

---

## Tabla SKIPPED (los 9 que NO se aplicaron — verificar que están intactos)

| # | Sev | Nota | Cita original presente? | Frontmatter modificado? | Comentario |
|---|---|---|---|---|---|
| 4 | 🟠 | Anemia Ferropénica | ✅ Presente | ❌ NO | L78: "reticulocitosis a los **5-10 días**" — intacta como en informe. Sin modificar frontmatter. |
| 5 | 🟢 | Anemia Ferropénica | ✅ Presente | ❌ NO | L75: "**Sulfato ferroso:** 325 mg/8 h (contiene 65 mg de hierro elemental)" — intacta. Nota: frontmatter sin `last_fact_checked` (correcto). |
| 6 | 🟢 | Anemia Ferropénica | ✅ Presente | ❌ NO | L101: "Hb <7-8 g/dL, o <10 g/dL con cardiopatía isquémica" — intacta. |
| 8 | 🟢 | Anemia Macrocítica | ✅ Presente | ❌ NO | L72: "Cianocobalamina 1000 µg/día v.o. (igual de efectivo que IM si mucosa intacta)" — intacta. |
| 9 | 🟠 | Anemia Macrocítica | ✅ Presente | ❌ NO | L63-64: "Nivel de B12 equívoco (200-400 pg/mL): Medir **ácido metilmalónico (AMM)** y **homocisteína**" — intacta como estaba. |
| 10 | 🟠 | Anemia Hemolítica - Abordaje | ✅ Presente | ❌ NO | L20: "**Crisis hemolítica grave (Hb <6-7 g/dL, anemia sintomática)** → transfusión urgente" — intacta. |
| 12 | 🟢 | Anemia Hemolítica - Abordaje | ✅ Presente | ❌ NO | L113: "**AIHA caliente** \| Prednisona 1 mg/kg/día; refractaria: rituximab, esplenectomía, ciclosporina" — intacta. |
| 17 | 🟢 | Pancitopenia | ✅ Presente | ❌ NO | L83: "**Aplasia:** médula hipocelular (<25% celularidad), predominio grasa" — intacta. |
| **18** | **🔴** | **Sdme Hemofagocitico** | ✅ Nota sigue vacía | ❌ NO | **Como esperado:** L11 solo contiene "Calcular SCORE HEMOFAGOCITICO" — sin contenido. Frontmatter intacto sin `last_fact_checked`. Fallback fallido por ausencia de PDF. |

---

## Frontmatter de las 5 notas MODIFICADAS

| Nota | `last_fact_checked` | `fuente` |
|---|---|---|
| Anemia - Abordaje General | ✅ 2026-05-19 | ✅ `"UpToDate – Diagnostic approach to anemia in adults (Means & Brodsky, Nov 2025)"` |
| Anemia Normocítica | ✅ 2026-05-19 | ✅ `"UpToDate – Diagnostic approach to anemia in adults (Means & Brodsky, Nov 2025) + KDIGO 2024 (Anemia ERC)"` |
| Anemia de Enfermedad Crónica (ACD-AI) | ✅ 2026-05-19 | ✅ `"UpToDate – Anemia of chronic disease/anemia of inflammation (Camaschella & Weiss, Feb 2026) + KDIGO 2024"` |
| Anemia Microcítica | ✅ 2026-05-19 | ✅ `"UpToDate – Diagnostic approach to anemia in adults (Means & Brodsky, Nov 2025)"` |
| Anemia Hemolítica - Abordaje | ✅ 2026-05-19 | ✅ `"UpToDate – Diagnostic approach to anemia in adults (Means & Brodsky, Nov 2025)"` |

---

## Frontmatter de las 4 notas NO MODIFICADAS

| Nota | `last_fact_checked` | Coherencia |
|---|---|---|
| Anemia Ferropénica | ❌ Ausente | ✅ Correcto — no se modificó |
| Anemia Macrocítica | ❌ Ausente | ✅ Correcto — no se modificó |
| Pancitopenia | ❌ Ausente | ✅ Correcto — no se modificó |
| Sdme Hemofagocitico | ❌ Ausente | ✅ Correcto — no se modificó (nota vacía) |

---

## Verificación contra _applied_discrepancies_hemato.md

| Aspecto | Estado |
|---|---|
| ✅ 9 APLICADOS enumerados correctamente en discrepancias | Verificado: H1, H2, H3, H7, H11, H13, H14, H15, H16 |
| ✅ 9 SKIPPED enumerados con razones | Verificado: H4, H5, H6, H8, H9, H10, H12, H17, H18 |
| ✅ Coherencia en plan propuesto | Verificado: "Prioridad 1 (🔴) H18 HLH; Prioridad 2 (🟠) H4/H9/H10; Prioridad 3 (🟢) H5/H6/H8/H12/H17" |
| ✅ Notas "con cambios reales aplicados" listadas | Verificado: Anemia - Abordaje, Normocítica, ACD-AI, Microcítica (frontmatter), Hemolítica (frontmatter) |
| ✅ Notas "sin tocar" listadas | Verificado: Ferropénica, Macrocítica, Pancitopenia, Sdme Hemofagocitico |

---

## Observaciones Específicas

### Cambios aplicados — conformidad

1. **H1, H2, H3** (Anemia - Abordaje): Las tres modificaciones están presentes, literal en la mayoría de casos o en paráfrasis clara. El orden de trimestres en la tabla es exacto (1T <11, 2T <10.5, 3T <11).

2. **H7, H11** (verificaciones positivas): Anemia Microcítica e Anemia Hemolítica ya tenían la información correcta en la nota — no requerían cambio, solo verificación.

3. **H13** (Anemia Normocítica): El cambio sugerido era "Inicio ESA si Hb <10 g/dL; objetivo Hb 10-11.5 g/dL (KDIGO); evitar normalización con cita a CHOIR/CREATE/TREAT". Está aplicado en L78 con completitud y claridad.

4. **H14** (ACD-AI leve Hb): Cambio de "10-12" a "10-11" está presente. El contexto de "~20% Hb<8 descartar componente" también está.

5. **H15** (ACD-AI reticulocitos): Ya estaba correcto, sin cambio necesario.

6. **H16** (ACD-AI ferritina): El cambio agregó "hasta 400 mcg/L en algunos países" y "diálisis <500+TSAT<30% KDIGO" — ambos presentes en L97.

### Notas SKIPPED — confirmación de integridad

- **Anemia Ferropénica:** Las 3 citas que fueron skipped (H4 5-10d, H5 325mg/8h, H6 Hb <7-8) permanecen intactas.
- **Anemia Macrocítica:** Las 2 citas (H8 1000µg/día, H9 200-400 pg/mL) permanecen intactas.
- **Anemia Hemolítica:** Las 2 citas (H10 <6-7 g/dL, H12 Prednisona 1mg/kg) permanecen intactas.
- **Pancitopenia:** La 1 cita (H17 <25% celularidad) permanece intacta.
- **Sdme Hemofagocitico:** Como esperado, sigue siendo una nota vacía (solo placeholder de score) — sin intento de edición.

### Coherencia con _applied_discrepancies_hemato.md

El archivo de discrepancias está alineado. Reporta correctamente:
- 9 APLICADOS con razones de por qué se aplicaron
- 9 SKIPPED con razones específicas de falta de PDF
- H18 como PRIORIDAD ALTA (🔴) por ser nota crítica vacía con mortalidad >50% sin tratamiento

---

## Conclusión

**9/9 aplicados correctamente; 9/9 skipped intactos; H18 (🔴 HLH) sigue vacío por falta de PDF — requiere UpToDate HLH + HLH-2004 para futuro rewrite.**

Métrica de calidad:
- ✅ **Cambios aplicados con exactitud textual o paráfrasis clara**
- ✅ **Frontmatter consistente: todas las 5 notas modificadas tienen `last_fact_checked: 2026-05-19`**
- ✅ **Frontmatter `fuente` con strings entre comillas (no wikilinks raw)**
- ✅ **Todas las 4 notas no modificadas mantienen ausencia de `last_fact_checked`**
- ✅ **Citas SKIPPED intactas, sin edición accidental**
- ✅ **H18 sigue vacía — como esperado, fallback fallido por PDF ausente**
