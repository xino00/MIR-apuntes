---
tags: [fact-check, auditoria]
fecha: 2026-04-20
auditor: Claude (Opus 4.7)
fuentes: ESC AF 2024, ESC VA/SCD 2022, ESC HF 2021, ESC HF Focused Update 2023, KDIGO 2024, ESC Syncope 2018, ESC/EACTS VHD 2025
---

# Parcial D — Arritmias + IC/Cardiorrenal + Síncope + VHD

## Resumen
- Notas auditadas: 6
- Hallazgos totales: 14 (5 Crítico · 5 Moderado · 2 Menor · 2 Informativo)
- Fuentes: ESC AF 2024, ESC VA/SCD 2022, ESC HF 2021/2023, KDIGO 2024, ESC Syncope 2018, ESC/EACTS VHD 2025

| Severidad | N |
|---|---|
| Crítico | 5 |
| Moderado | 5 |
| Menor | 2 |
| Informativo | 2 |

---

## [[Escala CHA2DS2-VASc y HAS-BLED]]

> Esta nota concentra los hallazgos críticos por el cambio de paradigma de la guía ESC AF 2024 (CHA₂DS₂-VASc → CHA₂DS₂-VA, eliminando el componente sexo).

### Hallazgo 1
- **Severidad:** Crítico
- **Hallazgo:** El score y el título usan la versión obsoleta CHA₂DS₂-VASc. La ESC AF 2024 sustituye el score por **CHA₂DS₂-VA**, eliminando el componente "Sc" (sexo femenino) como factor de puntuación.
- **Cita en la nota:** "# CHA₂DS₂-VASc — Riesgo tromboembólico en FA" (línea 10) y la fila "**Sc** | Sexo femenino | 1" (línea 21).
- **Cita en la fuente:** "Table 10 Updated definitions for the CHA2DS2-VA score […] CHA2DS2-VA, congestive heart failure, hypertension, age ≥75 years (2 points), diabetes mellitus, prior stroke/transient ischaemic attack/arterial thromboembolism (2 points), vascular disease, age 65–74 years" (ESC AF 2024, sección 6.1, p. 3343).
- **Cambio sugerido:** Renombrar score a CHA₂DS₂-VA (máximo 7 puntos), eliminar fila Sc, actualizar título y todas las referencias.

### Hallazgo 2
- **Severidad:** Crítico
- **Hallazgo:** Los umbrales de anticoagulación están estratificados por sexo (columnas Hombres/Mujeres). En ESC AF 2024 el umbral es **universal sin diferencia por sexo**: ≥2 = Clase I; =1 = Clase IIa.
- **Cita en la nota:** "| 0 | 1 (solo sexo) | Sin anticoagulación | / | 1 | 2 | Considerar anticoagulación | / | ≥2 | ≥3 | **Anticoagulación recomendada** (Clase I)" (líneas 29-31).
- **Cita en la fuente:** "A CHA2DS2-VA score of 2 or more is recommended as an indicator of elevated thromboembolic risk for decisions on initiating oral anticoagulation. (Class I)" / "A CHA2DS2-VA score of 1 should be considered an indicator of elevated thromboembolic risk for decisions on initiating oral anticoagulation. (Class IIa)" (Recommendation Table 6, p. 3342).
- **Cambio sugerido:** Tabla única de umbrales: 0 = no anticoagular; 1 = considerar (IIa); ≥2 = recomendado (I), sin distinción por sexo.

### Hallazgo 3
- **Severidad:** Moderado
- **Hallazgo:** Falta la indicación específica de anticoagulación en miocardiopatía hipertrófica y amiloidosis cardiaca **independientemente del CHA₂DS₂-VA**.
- **Cita en la nota:** Sin mención del tema (sección "Indicación de anticoagulación").
- **Cita en la fuente:** "Oral anticoagulation is recommended in all patients with AF and hypertrophic cardiomyopathy or cardiac amyloidosis, regardless of CHA2DS2-VA score, to prevent ischaemic stroke and thromboembolism. (Class I, B)" (Recommendation Table 6, p. 3342).
- **Cambio sugerido:** Añadir nota que en MCH/amiloidosis se anticoagula independientemente del score.

### Hallazgo 4
- **Severidad:** Menor
- **Hallazgo:** Anticoagulación post-cardioversión: la guía 2024 recomienda 4 semanas de OAC tras CVE para todos los pacientes (incluso CHA₂DS₂-VA = 0), salvo si <24h y bajo riesgo.
- **Cita en la nota:** No se aborda este punto (la nota se limita al score basal).
- **Cita en la fuente:** "Short-term OAC after cardioversion (4 weeks) for all patients, even if CHA2DS2-VA = 0 (optional if AF onset definitely <24 h and low thromboembolic risk)" (Figure 12, p. 3355).
- **Cambio sugerido:** Añadir referencia cruzada al algoritmo de cardioversión para evitar confusión entre OAC perioperatoria y crónica.

---

## [[Arritmias]]

### Hallazgo 5
- **Severidad:** Informativo
- **Hallazgo:** La nota declara como única fuente "Manual 12 de Octubre, Cap. 16" (2022). Existe guía ESC actualizada (ESC AF 2024 + ESC VA/SCD 2022) que aporta clases y dosis específicas no recogidas.
- **Cita en la nota:** "**Fuente:** Manual 12 de Octubre, Cap. 16." (línea 7).
- **Cita en la fuente:** "Table on antiarrhythmic drugs […] Adenosine: 6–18 mg bolus" (ESC VA/SCD 2022, Table 14 Antiarrhythmic drug doses, p. 4036–4037).
- **Cambio sugerido:** Añadir fuentes ESC 2022/2024 y marcar como `[OUTDATED-MANUAL]` partes que dependan exclusivamente del Manual.

### Hallazgo 6
- **Severidad:** Menor
- **Hallazgo:** La afirmación "Cardioversión Eléctrica… Energías Sincronizadas: 50-100 J (Flutter o TV monomorfa)" es razonable, pero la guía ESC VA/SCD 2022 no fija umbrales numéricos universales (depende del desfibrilador bifásico/monofásico). No es un error pero la regla numérica proviene del Manual.
- **Cita en la nota:** "**Energías Sincronizadas (CVE):** 50-100 J (Arritmias organizadas como Flutter o TV monomorfa)." (línea 22).
- **Cita en la fuente:** No se encuentra esta cifra explícita en ESC VA/SCD 2022 (el documento remite a recomendaciones generales de RCP para energías).
- **Cambio sugerido:** Marcar la cifra como recomendación práctica del Manual; si se quiere referencia ESC, citar protocolo local.

### Hallazgo 7
- **Severidad:** Moderado
- **Hallazgo:** En TV monomorfa estable la nota cita amiodarona "300 mg i.v. en 30-60 min + perfusión 900 mg/24 h". La ESC VA/SCD 2022 prescribe **5 mg/kg en 20 min – 2 h** (loading), y no menciona régimen fijo de 300 mg.
- **Cita en la nota:** "[[Amiodarona]]: **300 mg i.v. en 30-60 min** + perfusión 900 mg a 24h." (línea 42).
- **Cita en la fuente:** "Amiodarone […] Loading dose: 5 mg/kg in 20 min–2 h, 2–3 times in 24 h, then 600–1200 mg/24 h 8–10 days" (ESC VA/SCD 2022, Table 14, p. 4036).
- **Cambio sugerido:** Anotar que la dosis fija "300 mg" procede del régimen RCP/ACLS; añadir dosis ESC ajustada por peso para uso en TV monomorfa fuera de parada.

---

## [[Manejo Diurético Deterioro Renal ICA]]

### Hallazgo 8
- **Severidad:** Informativo
- **Hallazgo:** La nota no cita explícitamente la fuente ESC HF 2021 ni el Focused Update 2023. Las recomendaciones que da (bloqueo secuencial, mantener iSGLT2, "permissive WRF") son consistentes con dichas guías, pero sin trazabilidad.
- **Cita en la nota:** Sin sección "Fuente" / "Bibliografía". Sólo aparece "title: Manejo del Tratamiento Diurético y Deterioro Renal en ICA".
- **Cita en la fuente:** Concepto de descongestión sobre WRF: ESC HF 2021, sección 11.3.3, Figure 13 y Table 24 (p. 3654).
- **Cambio sugerido:** Añadir bloque "Fuentes" con ESC HF 2021 (sección 11.3) + ESC HF Focused Update 2023 (ADVOR/EMPULSE).

### Hallazgo 9
- **Severidad:** Moderado
- **Hallazgo:** No se menciona la **dosis máxima de furosemida i.v. en ICA (400-600 mg/día, hasta 1000 mg en ERC severa)** que es referencia explícita de ESC HF 2021. La nota habla de "intensificar" sin techo.
- **Cita en la nota:** "**¡Mantener o intensificar la terapia depletiva!**" (línea 29) — sin dosis tope.
- **Cita en la fuente:** "The maximal daily dose for i.v. loop diuretics is generally considered furosemide 400–600 mg though up to 1000 mg may be considered in patients with severely impaired kidney function" (ESC HF 2021, Figure 13 footnote, p. 3654).
- **Cambio sugerido:** Especificar techo 400-600 mg/día (o hasta 1000 mg si ERC severa) y los criterios de respuesta (Na+ urinario ≥50-70 mEq/L a 2h, diuresis ≥100-150 mL/h en 6h).

---

## [[Síndrome Cardiorrenal]]

### Hallazgo 10
- **Severidad:** Menor
- **Hallazgo:** La nota cita el ensayo ADVOR con dosis de acetazolamida correcta ("500 mg i.v."), pero no precisa que es **dosis única diaria** y que el beneficio es exclusivamente sobre **descongestión a 3 días**, sin impacto sobre rehospitalización o mortalidad.
- **Cita en la nota:** "Añadir **Inhibidores de la Anhidrasa Carbónica** (Acetazolamida), apoyado por estudio ADVOR (+ 500 mg i.v.)." (línea 55).
- **Cita en la fuente:** "intravenous (i.v.) acetazolamide (500 mg once daily) […] Rehospitalization for HF or all-cause death occurred in 76 patients (29.7%) in the acetazolamide group and in 72 patients (27.8%) in the placebo group (HR 1.07, 95% CI 0.78–1.48)" (ESC HF Focused Update 2023, sección 4.1.1, p. 3635).
- **Cambio sugerido:** Especificar "500 mg i.v. una vez al día" + matiz: "mejora descongestión, sin impacto en mortalidad/reingresos a 3 meses".

### Hallazgo 11
- **Severidad:** Crítico
- **Hallazgo:** En "Bloqueo Secuencial de la Nefrona" la nota recomienda hidroclorotiazida y clortalidona, pero NO cita el ensayo CLOROTIC ni que el efecto se limita a pérdida de peso, con **incremento significativo de creatinina** (46.5% vs 17.2%, p<0.001) y sin mejora clínica. Es un matiz relevante para guardia.
- **Cita en la nota:** "Añadir **Tiazidas** (ej. Hidroclorotiazida o Clortalidona) para bloquear el TCD." (línea 54).
- **Cita en la fuente:** "An increase in serum creatinine occurred more frequently in patients on hydrochlorothiazide (46.5%) compared with those on placebo (17.2%) (P < .001). The rates of HF rehospitalization and all-cause death were similar between groups" (ESC HF Focused Update 2023, sección 4.1.1, p. 3635).
- **Cambio sugerido:** Añadir advertencia: vigilar creatinina y K+ al añadir tiazida; el efecto es sobre peso, no sobre disnea ni reingresos (CLOROTIC).

---

## [[Síncope]]

### Hallazgo 12
- **Severidad:** Moderado
- **Hallazgo:** La nota describe el "Tilt training" como recomendación estándar para síncope reflejo. La ESC Syncope 2018 lo clasifica como **Clase IIb B** (puede considerarse), mientras que las maniobras de contrapresión isométrica son IIa B.
- **Cita en la nota:** "**Entrenamiento con mesa basculante** (*tilt training*) para prevenir recurrencias." (línea 154) y previamente "Maniobras de contrapresión isométrica … (nivel de evidencia alto)" (línea 153).
- **Cita en la fuente:** "Isometric PCM should be considered in patients with prodromes who are <60 years of age. (IIa, B)" / "Tilt training may be considered for the education of young patients. (IIb, B)" (ESC Syncope 2018, Recomendaciones de tratamiento de síncope reflejo, p. 1923).
- **Cambio sugerido:** Marcar tilt training como IIb (uso seleccionado en jóvenes) y restringir PCM a <60 años con pródromos.

### Hallazgo 13
- **Severidad:** Moderado
- **Hallazgo:** Falta indicación explícita del **Holter implantable (ILR)** en síncope recurrente de origen incierto sin criterios de alto riesgo (Clase I A, ESC 2018). La nota habla de "DAI" en arritmias malignas pero no cita ILR.
- **Cita en la nota:** Sección "Síncopes cardíacos" (líneas 165-170) — sin mención de ILR.
- **Cita en la fuente:** "ILR is indicated in an early phase of evaluation in patients with recurrent syncope of uncertain origin, absence of high-risk criteria, and a high likelihood of recurrence within the battery life of the device. (Class I, A)" (ESC Syncope 2018, Recommendation Table p. 1907).
- **Cambio sugerido:** Añadir párrafo sobre ILR (indicaciones I A: síncope recurrente sin diagnóstico ni alto riesgo; síncope con alto riesgo sin diagnóstico tras estudio completo).

---

## [[Valvulopatías]]

### Hallazgo 14
- **Severidad:** Crítico
- **Hallazgo:** La nota no refleja el cambio crítico de la ESC/EACTS VHD 2025: **TAVI ahora se recomienda a partir de ≥70 años** (no ≥75 como en 2021), y SAVR queda para <70 años. La nota solo menciona "SAVR o TAVI" sin discriminar edad.
- **Cita en la nota:** "**Tratamiento:** Su indicación principal es la aparición de síntomas… (Cirugía de Reemplazo Valvular - SAVR o Percutáneo - TAVI)." (línea 47).
- **Cita en la fuente:** "TAVI is recommended in patients ≥70 years of age with tricuspid AV stenosis, if the anatomy is suitable. (Class I, A)" / "SAVR is recommended in patients <70 years of age, if the surgical risk is low. (Class I, B)" (ESC/EACTS VHD 2025, Recomendaciones modo de intervención EAo sintomática severa, sección 8.5, p. 4646).
- **Cambio sugerido:** Actualizar criterios edad: TAVI ≥70 años (válvula tricúspide, anatomía favorable); SAVR <70 si bajo riesgo. Citar fuente ESC/EACTS VHD 2025.

### Hallazgo 15
- **Severidad:** Crítico
- **Hallazgo:** En IM primaria asintomática, la nota carece de los nuevos cutoffs de la ESC/EACTS VHD 2025: **LVESD <40 mm + LVESDi <20 mm/m² + FEVI >60%** + dilatación AI (LAVI ≥60 mL/m² o diámetro AI ≥55 mm). La nota solo cita "NYHA II-IV con FEVI >30%" como criterio quirúrgico.
- **Cita en la nota:** "**Cirugía:** Reparación valvular de elección sobre el recambio protésico, si afecta la clase funcional (NYHA II-IV con FEVI > 30%)." (línea 30).
- **Cita en la fuente:** "Surgical MV repair should be considered in low-risk asymptomatic patients with severe PMR without LV dysfunction (LVESD <40 mm, LVESDi <20 mm/m², and LVEF >60%) in the presence of significant LA dilatation (LAVI ≥60 mL/m² or LA diameter ≥55 mm), when performed in a Heart Valve Centre and a durable repair is likely. (Class IIa, B)" (ESC/EACTS VHD 2025, sección 9.1.4, p. 4647).
- **Cambio sugerido:** Añadir criterios cuantitativos para asintomáticos (LVESD/LVESDi, LAVI/diámetro AI, FEVI, PH, FA secundaria). Citar VHD 2025.

### Hallazgo 16
- **Severidad:** Moderado
- **Hallazgo:** No se menciona la EAo de **bajo flujo / bajo gradiente con FEVI conservada**, escenario clínicamente común. ESC/EACTS VHD 2025 redefine SVi ≤35 mL/m² como criterio en este perfil.
- **Cita en la nota:** Solo se cita EAo severa "Área valvular < 1 cm², Gradiente medio > 40 mmHg, Velocidad máxima > 4 m/s." (línea 45).
- **Cita en la fuente:** "Intervention should be considered in symptomatic patients with low-flow (SVi ≤35 mL/m²), low-gradient (<40 mmHg) AS with normal LVEF (≥50%) after careful confirmation that AS is severe. (IIa, B)" (ESC/EACTS VHD 2025, sección 8.4.1, p. 4646).
- **Cambio sugerido:** Añadir párrafo sobre EAo paradójica bajo flujo/bajo gradiente con LVEF conservada (criterio SVi ≤35 mL/m²) y necesidad de confirmar severidad.

---

## Notas sin hallazgos críticos adicionales

- [[Arritmias]] tiene hallazgos informativos/menores (ya listados); resto del contenido es coherente con la ESC VA/SCD 2022 y AHA en su uso de adenosina/procainamida.
- [[Manejo Diurético Deterioro Renal ICA]]: la regla "permissive WRF" (incremento Cr 30-50% si descongestión adecuada) es consistente con la literatura; no se halla cita explícita en ESC HF 2021/2023 (concepto recogido en literatura adyacente, no en clase de recomendación), por lo que se deja como concepto sin clase formal.

---

## Métricas globales del parcial

| Nota | Hallazgos | Críticos | Moderados | Menores | Informativos |
|---|---|---|---|---|---|
| Escala CHA2DS2-VASc y HAS-BLED | 4 | 2 | 1 | 1 | 0 |
| Arritmias | 3 | 0 | 1 | 1 | 1 |
| Manejo Diurético Deterioro Renal ICA | 2 | 0 | 1 | 0 | 1 |
| Síndrome Cardiorrenal | 2 | 1 | 0 | 1 | 0 |
| Síncope | 2 | 0 | 2 | 0 | 0 |
| Valvulopatías | 3 | 2 | 1 | 0 | 0 |
| **Total** | **16** | **5** | **6** | **3** | **2** |
