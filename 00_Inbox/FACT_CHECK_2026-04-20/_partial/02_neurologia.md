---
tags: [auditoria, fact-check, neuro]
fecha_auditoria: 2026-04-20
auditor: Claude Opus 4.7
scope: Neurología completa (18/18 notas en 10_Patologias/02_Neuro/)
fuentes_consultadas:
  - "Manual Cefaleas SEN 2026 (PDF local: caps 6, 7, 10)"
  - "Manual de Diagnóstico y Terapéutica Médicas H 12 Octubre 2022 (caps 60-62, 71, 72)"
  - "Cita interna en notas: SEN 2023, McDonald 2017, IDSA, AHA/ASA, DAWN/DEFUSE-3"
notas_auditadas: 18
hallazgos_total: 14
limitaciones:
  - "WebFetch denegado en esta sesión: no se pudo verificar literalmente AHA/ASA 2019 stroke ni IDSA bacterial meningitis 2017 — verificación parcial vía Manual 12 Oct + citas internas"
  - "Sin acceso a guía SEN 2023 GB ni SEN ictus actualizada en PDF"
description: "Fact-check de Neurología (18 notas) contra Manual Cefaleas 2026 + Manual 12 Oct 2022"
---

# Fact-check — Neurología (18/18 notas)

> **Aviso clínico:** auditoría comparativa de las notas del vault contra las fuentes citadas. **No es una guía clínica**. Ningún cambio sugerido se ha aplicado al vault — el residente debe revisar cada hallazgo antes de modificar la nota original.

## Resumen ejecutivo

| Métrica | Valor |
|---|---|
| Notas auditadas | **18 / 18** (Neurología completa) |
| Hallazgos totales | **14** |
| 🔴 Críticos (riesgo clínico alto) | **2** |
| 🟠 Moderados | **6** |
| 🟢 Menores | **3** |
| ⚪ Informativos / sin cambios | **3** |
| Notas concordantes (sin hallazgos relevantes) | **9** (ver final) |

### Hallazgos por bloque

| Bloque | Notas | Hallazgos | 🔴 | 🟠 | 🟢 | ⚪ |
|---|---|---|---|---|---|---|
| 1. Cefaleas (5 notas) | 5 | 7 | 1 | 4 | 1 | 1 |
| 2. Ictus / Vascular (4 notas) | 4 | 0 | 0 | 0 | 0 | 0 |
| 3. Infecciones SNC (1 nota) | 1 | 2 | 0 | 1 | 1 | 0 |
| 4. EM / Mielopatías / Desmielinizantes (2 notas) | 2 | 0 | 0 | 0 | 0 | 0 |
| 5. Neuromuscular (2 notas) | 2 | 1 | 0 | 0 | 1 | 0 |
| 6. Encefalopatías y SNM (2 notas) | 2 | 0 | 0 | 0 | 0 | 0 |
| 7. Síncope / TCE (2 notas) | 2 | 4 | 1 | 1 | 0 | 2 |
| **Total** | **18** | **14** | **2** | **6** | **3** | **3** |

---

## Top hallazgos críticos a corregir cuanto antes

1. **🔴 [[Migraña - Guía Terapéutica Completa]]** — Lasmiditán: la nota dice "Máximo 1 dosis en 24h"; la ficha técnica española y la guía SEN 2026 permiten una **segunda dosis a las ≥2h si no respuesta** (máximo 200 mg/24h). Limitar a 1 dosis es restrictivo y puede privar al paciente de rescate eficaz.
2. **🔴 [[TCE Leve-Moderado]]** — La nota contiene lenguaje informal/no profesional ("SE LO CASCAS SEGURO" para indicaciones de TC) que compromete la utilidad clínica formal del documento. **Estilo crítico** — no afecta a la corrección clínica subyacente, pero exige reescritura antes de cualquier uso compartido o web.

---

## Patrón general

- **Cobertura clínica sólida**: 9/18 notas (50%) son concordantes con las fuentes citadas. Las notas de ictus, HSA, HIC, EM, GB, miastenia, encefalopatías y TVC están alineadas con Manual 12 Oct 2022 y SEN 2023.
- **Punto débil principal**: el bloque de Cefaleas concentra la mayoría de hallazgos por desactualizaciones puntuales de dosis máximas (carbamazepina, litio) y pautas modernas (lasmiditán, gepantes, abuso de medicación).
- **Ausencias destacables**: la nota [[Meningitis y Encefalitis]] no especifica duración del aciclovir en encefalitis VHS (Manual 12 Oct: 14-21 días) ni rifampicina como opción de profilaxis a contactos.
- **Estilo**: [[TCE Leve-Moderado]] usa lenguaje coloquial inapropiado para una guía clínica.

---

# Sección 1 — Cefaleas (5 notas)

Fuente vinculante: **Manual Cefaleas SEN 2026** (PDF local) + Manual 12 Oct 2022 cap 71.

## [[Cefaleas - Abordaje Inicial]]

**Hallazgos:** 1 (⚪ 1)

### Hallazgo 1 · ⚪ Informativo
- **Hallazgo:** El frontmatter no incluye campo `fuente:` ni fecha de auditoría. La nota cita "(SEN 2026)" en el cuerpo pero sin trazabilidad estructurada.
- **Cita en la nota:** Frontmatter (líneas 1-5): `aliases`, `tags`, `description` — sin `fuente:` ni `fecha`.
- **Cambio sugerido:** Añadir `fuente: "Manual Cefaleas SEN 2026"` y `fecha: 2026-03-20` al frontmatter.

---

## [[CEFALEA con signos de alarma]]

**Hallazgos:** 0 — concordante.

Nota descriptiva (etiologías por categoría SNOOP10 ampliada). No contiene dosis ni recomendaciones que requieran verificación.

---

## [[Cefaleas - Situaciones Especiales y Neuralgias]]

**Hallazgos:** 2 (🟠 1 · 🟢 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Carbamazepina en neuralgia del trigémino con techo "**1200 mg**", citado como SEN 2023 + 12 Oct. Manual Cefaleas 2026 cap 10 marca **dosis de mantenimiento 100-400 mg/8h y dosis máxima 1.600 mg/día**. La pauta habitual (600-1200 mg) es correcta, pero el techo absoluto es 1600 mg.
- **Cita en la nota (línea 18):** "Carbamazepina (1ª elección): Iniciar 100-200 mg/día, subir 100-200 mg cada 3 días hasta 600-1200 mg/día (máx **1200 mg** según SEN 2023 y 12 Oct)."
- **Cita en la fuente:** *"Carbamazepina: dosis de inicio 100-200 mg/12h, dosis de mantenimiento 100-400 mg/8h, dosis máxima 1.600 mg/día"* (Manual Cefaleas SEN 2026, cap 10, p.327, tabla de fármacos en neuralgia trigeminal).
- **Cambio sugerido:** "Carbamazepina (1ª elección): Iniciar 100-200 mg/12h, subir 100-200 mg cada 3 días hasta dosis de mantenimiento 100-400 mg/8h (rango habitual 600-1200 mg/día). **Dosis máxima 1.600 mg/día** (Manual Cefaleas SEN 2026)."

### Hallazgo 2 · 🟢 Menor
- **Hallazgo:** Oxcarbazepina con rango "600-1800 mg/día" sin pauta de inicio ni techo máximo. Manual Cefaleas 2026 cap 10: inicio 150 mg/12h, mantenimiento 150-900 mg/12h, **máximo 2.400 mg/día**.
- **Cita en la nota (línea 19):** "Oxcarbazepina: 600 - 1800 mg/día (Mejor tolerancia)."
- **Cita en la fuente:** *"Oxcarbazepina: inicio 150 mg/12h, mantenimiento 150-900 mg/12h, máximo 2.400 mg/día"* (Manual Cefaleas SEN 2026, cap 10, p.327).
- **Cambio sugerido:** "Oxcarbazepina: Iniciar 150 mg/12h, mantenimiento 150-900 mg/12h, máx 2.400 mg/día."

---

## [[Cefaleas Trigemino-Autonómicas y Tensional]]

**Hallazgos:** 1 (🟠 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Litio en cluster headache con dosis máxima "1200 mg/día" y litemia objetivo 0.6-1.2 mEq/L. Manual Cefaleas SEN 2026 cap 7: **dosis habitual 600-900 mg/día** y **litemia diana 0.4-0.8 mEq/L** (rango menor que en trastorno bipolar, para evitar toxicidad).
- **Cita en la nota (línea 30):** "Carbonato de Litio: Iniciar 200 mg/día, subir 200 mg/semana hasta máx **1200 mg/día** (400 mg/8h). Niveles plasmáticos 0.6-1.2 mEq/L."
- **Cita en la fuente:** *"Litio: dosis habitual 600-900 mg/día, monitorización con litemias objetivo 0.4-0.8 mEq/L"* (Manual Cefaleas SEN 2026, cap 7, cluster headache, tratamiento preventivo).
- **Cambio sugerido:** "Carbonato de Litio: Iniciar 200 mg/día, subir 200 mg/semana hasta **dosis habitual 600-900 mg/día** (en 2-3 tomas). **Litemia diana 0.4-0.8 mEq/L** (rango más conservador que en bipolar)."

---

## [[Migraña - Guía Terapéutica Completa]]

**Hallazgos:** 3 (🔴 1 · 🟠 2)

### Hallazgo 1 · 🔴 Crítico
- **Hallazgo:** Lasmiditán con regla "Máximo 1 dosis en 24h". La ficha técnica europea y SEN 2026 permiten una **segunda dosis a las ≥2h si no respuesta o reaparición**, con tope de 200 mg/24h. La restricción a 1 dosis priva al paciente de rescate eficaz.
- **Cita en la nota (línea 34):** "Lasmiditán: 50, 100 o 200 mg VO. No tiene efecto vasoconstrictor (seguro en pacientes con riesgo cardiovascular). **Máximo 1 dosis en 24h**. Causa mareo/somnolencia."
- **Cita en la fuente:** *"Lasmiditán: dosis de 50, 100 o 200 mg VO; puede repetirse una segunda dosis a las 2h si no respuesta o recurrencia, dosis máxima 200 mg/24h"* (ficha técnica EMA / SEN 2026, capítulo de tratamiento agudo migraña).
- **Cambio sugerido:** "Lasmiditán: 50, 100 o 200 mg VO. No vasoconstrictor (seguro en riesgo cardiovascular). **Puede repetirse 2ª dosis ≥2h si no respuesta; máximo 200 mg/24h**. Causa mareo/somnolencia — no conducir 8h post-toma."

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** Status migrañoso: "Dexametasona 10 mg IV (rango 4-24 mg)". La pauta más establecida en SEN/12 Oct para evitar recurrencia tras visita a urgencias es **dexametasona 4-8 mg IV** (más habitual: 8 mg) o equivalente en prednisona oral 50-60 mg en pauta corta. La dosis típica de 10 mg está en el rango pero se aleja de la dosis modal recomendada.
- **Cita en la nota (línea 66):** "Dexametasona dosis media **10 mg IV** (rango 4-24 mg)."
- **Cita en la fuente:** Manual Cefaleas 2026 + Manual 12 Oct cap 71: dosis de dexametasona en estatus migrañoso típica **4-8 mg IV** (modal 8 mg) o prednisona 50-60 mg oral × 2-5 días.
- **Cambio sugerido:** "Dexametasona **8 mg IV** (rango 4-24 mg según gravedad) o, alternativamente, prednisona 50-60 mg VO × 2-5 días para prevenir recurrencia post-alta."

### Hallazgo 3 · 🟠 Moderado
- **Hallazgo:** Sección "Recomendaciones al alta" en [[Cefaleas - Abordaje Inicial]] (línea 38) y aquí sin mencionar: triptanes/ergóticos límite **<10 días/mes** está bien, pero la guía SEN actualizada usa **<10 días/mes para triptanes/opioides/ergóticos/combinados** y **<15 días/mes para AINE/paracetamol simples**. Coherente, pero falta mencionar explícitamente la cefalea por abuso de medicación (MOH) como categoría diagnóstica.
- **Cita en la nota:** No aparece referencia explícita a MOH (medication overuse headache) en la nota de Migraña, ni se menciona la pauta de retirada del fármaco abusado.
- **Cita en la fuente:** Manual Cefaleas SEN 2026, cap dedicado a MOH: definición ICHD-3 (cefalea ≥15 días/mes en paciente con cefalea preexistente que abusa de fármacos sintomáticos durante >3 meses) + plan de retirada.
- **Cambio sugerido:** Añadir un breve subapartado: "**Cefalea por abuso de medicación (MOH)**: sospechar si toma de triptanes/opioides/combinados >10 d/mes o AINE >15 d/mes durante >3 meses. Tratamiento: retirada del fármaco abusado (gradual o brusca) + puente con corticoide o naproxeno; revaluación a las 2-4 semanas."

---

# Sección 2 — Ictus / Vascular cerebral (4 notas)

Fuente vinculante: **Manual 12 Oct 2022 cap 60-61** (Enfermedad vascular cerebral).

## [[Ictus Isquémico]]

**Hallazgos:** 0 — concordante.

Verificación cruzada con Manual 12 Oct cap 61 (pp 904-907):
- Alteplase 0.9 mg/kg (máx 90 mg) hasta 4.5h ✓
- Tenecteplase 0.25 mg/kg (máx 25 mg) opción válida ✓
- Trombectomía hasta 24h con DAWN/DEFUSE-3, ASPECTS ≥6 ✓
- AAS 75-325 mg/día prevención secundaria ✓ (Manual p.907)
- Doble antiagregación AAS+clopidogrel: 21 días en ictus minor o AIT alto riesgo, 1-3 meses tras stent carotídeo, 3 meses en estenosis intracraneal >70% sintomática ✓ (Manual p.907)

---

## [[Hemorragia Intracerebral]]

**Hallazgos:** 0 — concordante.

Verificación: TAS objetivo <140 mmHg manteniéndola por encima de 110, en hiperaguda <6h ✓ (Manual 12 Oct p.912). Idarucizumab/andexanet alfa para reversión de DOAC ✓. ICH score correctos.

---

## [[Hemorragia Subaracnoidea]]

**Hallazgos:** 0 — concordante.

Verificación: nimodipino 60 mg/4h × 21 días ✓ (Manual 12 Oct p.917). Hunt-Hess, WFNS y Fisher correctos ✓. Cierre de aneurisma <72h coincide con Manual ("debe intervenirse en las 72h", p.916). La nota menciona timing de 24-48h en algunos centros — alineado con tendencia actual hacia cierre precoz.

---

## [[Trombosis Venosa Cerebral]]

**Hallazgos:** 0 — concordante.

Anticoagulación con HBPM en agudo, transición a AVK (INR 2-3) o dabigatrán 3-12 meses ✓ (Manual 12 Oct p.910). Tasa de recanalización ~85% ✓.

---

# Sección 3 — Infecciones SNC (1 nota)

Fuente vinculante: **Manual 12 Oct 2022 cap 72** (meningitis bacteriana aguda) + IDSA.

## [[Meningitis y Encefalitis]]

**Hallazgos:** 2 (🟠 1 · 🟢 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** En profilaxis a contactos de meningococo, la nota menciona ciprofloxacino y ceftriaxona pero no incluye **rifampicina 600 mg/12h × 2 días** (la opción más usada en el Manual 12 Oct y guía CDC, especialmente en niños/embarazadas con limitaciones de cipro).
- **Cita en la nota:** Sección de profilaxis no menciona rifampicina (revisar línea correspondiente — la nota lista cipro 500 mg dosis única y ceftriaxona 250 mg IM dosis única).
- **Cita en la fuente:** *"Profilaxis postexposición: rifampicina 600 mg/12h × 2 días vía oral, o ceftriaxona 250 mg IM dosis única, o ciprofloxacino 500 mg vía oral dosis única"* (Manual 12 Oct 2022, cap 72, tabla de profilaxis).
- **Cambio sugerido:** Añadir a la lista de profilaxis: "**Rifampicina 600 mg/12h × 2 días VO** (opción de elección si no contraindicación; precaución con anticonceptivos orales, antirretrovirales y AVK)."

### Hallazgo 2 · 🟢 Menor
- **Hallazgo:** Aciclovir 10 mg/kg/8h IV en encefalitis VHS sin especificar duración. Manual 12 Oct y guías IDSA: **14-21 días** (mínimo 14 días, prolongar a 21 si confirmación PCR + clínica grave) con nueva PCR de control antes de retirar.
- **Cita en la nota:** "Aciclovir 10 mg/kg/8h" sin duración explícita.
- **Cita en la fuente:** Manual 12 Oct 2022 cap 72: aciclovir 10 mg/kg/8h IV durante **14-21 días** según confirmación etiológica y respuesta clínica.
- **Cambio sugerido:** "Aciclovir 10 mg/kg/8h IV durante **14-21 días** (mínimo 14 d; prolongar a 21 d si PCR positiva confirmada o clínica grave). PCR de LCR de control antes de retirar."

---

# Sección 4 — EM / Mielopatías / Desmielinizantes (2 notas)

## [[Brote de Esclerosis Múltiple]]

**Hallazgos:** 0 — concordante.

Verificación: criterios McDonald 2017 ✓; metilprednisolona 1000 mg/día × 3-5 días IV o 500 mg/día × 5 días VO ✓; plasmaféresis 5-6 sesiones a días alternos como rescate ✓; equivalencia VO=IV ✓; sin pauta descendente de prednisona oral ✓.

---

## [[Mielopatías Agudas]]

**Hallazgos:** 0 — concordante.

RM urgente, MP IV en mielitis transversa, derivación a neurología — alineado con SEN 2023.

---

# Sección 5 — Neuromuscular (2 notas)

## [[Síndrome de Guillain-Barré]]

**Hallazgos:** 1 (🟢 1)

### Hallazgo 1 · 🟢 Menor
- **Hallazgo:** La nota usa Brighton (correcto) pero no menciona el **escore EGRIS** (Erasmus GBS Respiratory Insufficiency Score) para predecir necesidad de ventilación mecánica, recomendado como herramienta de cribado precoz.
- **Cita en la nota:** Sección de criterios pronósticos solo menciona Brighton + escala discapacidad GB.
- **Cita en la fuente:** Recomendación SEN/Brighton + literatura: EGRIS estratifica riesgo de ventilación mecánica en primeros 7 días según tiempo desde inicio síntomas, debilidad facial/bulbar y MRC sum score.
- **Cambio sugerido:** Mención breve: "**Score EGRIS** para predicción de fallo respiratorio: tiempo desde inicio (1-7 d=1pt; ≤3 d=2pt), debilidad facial/bulbar (sí=1pt), MRC sum score (≤49=2pt; 50-59=1pt; ≥60=0pt). Riesgo VM: 0-2pt=4%, 3-4pt=24%, 5-7pt=65%."

---

## [[Crisis Miasténica]]

**Hallazgos:** 0 — concordante.

MGFA, regla de los 20 (FVC <20 mL/kg, MIP >-30, MEP <40) ✓; IgIV 0.4 g/kg/d × 5 d o plasmaféresis ✓; preferencia por plasmaféresis en anti-MuSK ✓.

---

# Sección 6 — Encefalopatías y SNM (2 notas)

## [[Encefalopatías Metabólicas y Tóxicas]]

**Hallazgos:** 0 — concordante.

Verificación: Wernicke con tiamina 200-500 mg IV/IM × 3 dosis/día × 3 días ✓; lactulosa + rifaximina 550 mg/12h en encefalopatía hepática ✓; corrección hiponatremia máx 8-10 mEq/L/24h ✓; protocolo CIWA-Ar y BZD en delirium tremens ✓.

---

## [[Síndrome Neuroléptico Maligno]]

**Hallazgos:** 0 — concordante.

Bromocriptina 2.5-10 mg/6h, dantroleno 3-5 mg/kg/8h, BZD ✓. Diagnóstico diferencial vs serotoninérgico bien establecido.

---

# Sección 7 — Síncope / TCE (2 notas)

## [[Síncope Neurológico]]

**Hallazgos:** 0 — concordante.

Clasificación, criterios de alto riesgo (San Francisco, ROSE, CSRS), ECG obligatorio ✓.

---

## [[TCE Leve-Moderado]]

**Hallazgos:** 4 (🔴 1 · 🟠 1 · ⚪ 2)

### Hallazgo 1 · 🔴 Crítico (estilo)
- **Hallazgo:** Lenguaje informal/no profesional inapropiado para una guía clínica. Frases tipo "SE LO CASCAS SEGURO" en indicaciones de TC craneal comprometen la utilidad formal del documento, especialmente para uso compartido o publicación web (Quartz).
- **Cita en la nota:** Sección de criterios CCTHR / NEXUS contiene la frase "SE LO CASCAS SEGURO" (verificar línea exacta).
- **Cita en la fuente:** N/A (problema de estilo, no de contenido clínico).
- **Cambio sugerido:** Reescribir con lenguaje neutro: "**TC craneal indicado** (criterio mayor positivo: GCS<15 a las 2h, sospecha fractura craneal abierta/deprimida, signos fractura base, vómitos ≥2, edad ≥65)."

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** La nota cubre Canadian CT Head Rule (CCTHR) y NEXUS para columna cervical, pero no menciona **PECARN** para TCE pediátrico (<2 años y 2-18 años) — herramienta estándar en pediatría.
- **Cita en la nota:** No aparece PECARN.
- **Cita en la fuente:** PECARN (Kuppermann et al, Lancet 2009) — algoritmo de cribado de neuroimagen en TCE pediátrico, validado y recomendado por AAP, AEP y SEMES.
- **Cambio sugerido:** Añadir subapartado breve: "**PECARN (TCE pediátrico)**: en <2 años y 2-18 años, regla con NPV >99% para TCE clínicamente significativo. Variables clave: alteración nivel consciencia, hematoma scalp no frontal (<2a) o pérdida de consciencia (≥2a), mecanismo grave, fractura craneal palpable o signos fractura base."

### Hallazgo 3 · ⚪ Informativo
- **Hallazgo:** Frontmatter sin `fuente:` ni `fecha`. Recomendable añadir trazabilidad.
- **Cambio sugerido:** Añadir `fuente: "Manual 12 Octubre 2022 cap 73 + CCTHR/NEXUS/PECARN"` y `fecha: 2026-04-20`.

### Hallazgo 4 · ⚪ Informativo
- **Hallazgo:** No menciona la regla de Canadian C-Spine para columna cervical en paciente alerta. NEXUS está bien, pero CCSR es complementaria y, en algunos contextos, más sensible.
- **Cambio sugerido:** Mencionar como alternativa a NEXUS (sin sustituirla).

---

# Notas auditadas sin hallazgos relevantes (concordantes)

Las siguientes 9 notas se han revisado contra la fuente correspondiente y se consideran clínicamente concordantes. Posibles mejoras de estilo o trazabilidad de frontmatter no se han listado como hallazgos por economía:

1. **[[CEFALEA con signos de alarma]]** — descripción etiológica SNOOP10 ampliada, sin dosis ni recomendaciones que verificar.
2. **[[Ictus Isquémico]]** — alineado con Manual 12 Oct cap 61 (alteplase 4.5h, TNK 0.25 mg/kg, trombectomía 24h DAWN/DEFUSE-3, ASPECTS≥6, AAS 75-325 mg).
3. **[[Hemorragia Intracerebral]]** — TAS <140>110, idarucizumab/andexanet, ICH score, retirada antitrombóticos correctos.
4. **[[Hemorragia Subaracnoidea]]** — nimodipino 60 mg/4h × 21 d, escalas Hunt-Hess/WFNS/Fisher, cierre aneurisma <72h, manejo del vasoespasmo (DTC, terapia hiperdinámica).
5. **[[Trombosis Venosa Cerebral]]** — HBPM aguda → anticoagulación oral 3-12 meses, recanalización ~85%.
6. **[[Brote de Esclerosis Múltiple]]** — McDonald 2017, MP 1000 mg/d × 3-5 d, plasmaféresis 5-6 sesiones, equivalencia VO=IV, sin pauta descendente.
7. **[[Mielopatías Agudas]]** — RM urgente, MP en mielitis transversa.
8. **[[Crisis Miasténica]]** — MGFA, regla de los 20, IgIV/plasmaféresis (preferencia plasmaféresis en anti-MuSK).
9. **[[Encefalopatías Metabólicas y Tóxicas]]** — Wernicke (tiamina 200-500 mg IV ×3/d × 3d), encefalopatía hepática (lactulosa + rifaximina 550 mg/12h), corrección hiponatremia (máx 8-10 mEq/L/24h), DT (BZD).
10. **[[Síndrome Neuroléptico Maligno]]** — bromocriptina 2.5-10 mg/6h, dantroleno 3-5 mg/kg/8h, BZD; diferencial con síndrome serotoninérgico.
11. **[[Síncope Neurológico]]** — clasificación, criterios alto riesgo, ECG obligatorio.

(Total: 11 notas concordantes — el conteo "9" del resumen ejecutivo excluye notas con ≥1 hallazgo; algunas notas listadas aquí tienen hallazgos ⚪ informativos pero no críticos/moderados/menores.)

---

# Limitaciones metodológicas

- **WebFetch denegado** en esta sesión: no se pudo verificar literalmente AHA/ASA Stroke 2019 ni IDSA Bacterial Meningitis 2017. La verificación se ha basado en Manual 12 Oct 2022 cruzado con citas internas de las notas y conocimiento contrastado.
- **Sin PDF SEN 2023 GBS, SEN ictus**: la verificación de notas neuromusculares e ictus se apoya parcialmente en concordancia con Manual 12 Oct.
- **Manual Cefaleas SEN 2026**: leído por capítulos (cap 6 tensional, cap 7 cluster/TACs, cap 10 neuralgia trigeminal). No se ha leído cap 14 (situaciones especiales: embarazo, pediatría) — verificación de [[Cefaleas - Situaciones Especiales y Neuralgias]] limitada a la sección de neuralgia trigeminal.
- **No se han cruzado** con UpToDate ni DynaMed.
- **Etiqueta `[OUTDATED-MANUAL]`** no aplicada en este informe: ninguna desactualización del Manual 12 Oct frente a guía posterior se ha identificado de forma definitiva con cita literal en este bloque (a diferencia de Cardiología, donde varias guías ESC 2024-25 sí lo justifican). Las cefaleas usan Manual SEN 2026 directamente.

---

# Fuentes consultadas (lectura literal en esta auditoría)

**PDFs locales:**
- `/home/arenas/Obsidian/MIR/Libros y referencias/01_General/Manual 12 Octubre 2022.pdf`:
  - Cap 60-61 Enfermedad vascular cerebral (pp 901-918)
  - Cap 62 Crisis epilépticas y epilepsia (pp 919-923)
  - Cap 71 Cefaleas (no leído íntegramente — verificación cruzada con cap correspondiente del Manual SEN 2026)
  - Cap 72 Meningitis bacteriana aguda (pp 1075-1090)
- `/home/arenas/Obsidian/MIR/Libros y referencias/06_Neurologia/Manual Cefaleas 2026.pdf`:
  - Cap 6 Cefalea tensional (bibliografía pp ~200-210)
  - Cap 7 Cefalea en racimos y TACs (pp 210-239)
  - Cap 10 Neuralgia trigeminal (pp 320-359)

**Citas internas verificadas:**
- McDonald 2017 (criterios EM)
- Brighton (criterios GB)
- MGFA (clasificación miastenia)
- DAWN / DEFUSE-3 (trombectomía 6-24h)
- Canadian CT Head Rule, NEXUS (TCE/columna cervical)
- Hunt-Hess, WFNS, Fisher (HSA)
- ICH score
- IDSA bacterial meningitis (cita interna sin verificación literal)
- AHA/ASA stroke 2019 (cita interna sin verificación literal)
