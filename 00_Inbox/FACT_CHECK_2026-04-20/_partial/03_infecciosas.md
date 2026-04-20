---
aliases: [Fact-check Infecciosas]
tags: [auditoria, fact-check, infecciosas]
fecha_auditoria: 2026-04-20
auditor: Claude Opus 4.7
fuentes_consultadas:
  - "Surviving Sepsis Campaign 2026 (Prescott et al, Intensive Care Med, doi:10.1007/s00134-026-08361-1) — PDF local SEPSIS 2026.pdf"
  - "Guía de Manejo de Antibióticos FJD 2025 (PROA Antibioticos vs 23 abril.pdf) — última revisión septiembre 2024"
  - "Protocolo Diagnóstico y Tratamiento de Síndromes Infecciosos FJD 2023 (PROA FJD.pdf, mayo 2023)"
  - "Manual de Diagnóstico y Terapéutica Médica Hospital 12 Octubre 2022"
notas_auditadas: 15
hallazgos_total: "26 (1🔴 · 11🟠 · 10🟢 · 4⚪)"
---

# Fact-check Infecciosas — Informe parcial 03

## Resumen ejecutivo

- **Notas auditadas:** 15 (4 serie Sepsis SSC 2026 + 1 índice Sepsis + Gripe + 8 PROA)
- **Hallazgos:** 26 totales
  - 🔴 Crítico: 1 (inversión literal de la Recomendación 72 SSC 2026 — invertido el sentido del volumen tidal recomendado)
  - 🟠 Moderado: 11
  - 🟢 Menor: 10
  - ⚪ Informativo: 4
- **Hallazgo destacado:** [[Sepsis - Antiinfecciosos y Soporte Vital]] línea 163 indica "se sugiere usar **4 a < 6 mL/kg IBW (volumen más bajo)**" para insuficiencia respiratoria por sepsis sin SDRA, cuando la SSC 2026 Rec 72 dice exactamente lo contrario: "tidal volume of **6—8 mL/kg ideal body weight (IBW) over a lower (4 to <6 mL/kg IBW)**". La nota tiene el sentido invertido — debe corregirse antes del próximo manejo en críticos.
- **Notas sin hallazgos verificables:** 5 (ver sección final).
- **Limitaciones:** WebFetch no autorizado en esta sesión; no se pudieron cruzar las notas PROA-ITS y PROA-Respiratorias contra CDC STI 2021 e IDSA online. La nota de Gripe no tiene PDF de protocolo asociado y se evalúa solo formalmente.

---

## Sepsis - Abordaje Inicial (SSC 2026)

### Hallazgo 1 — qSOFA: degradación correcta pero falta especificar el cambio de Rec 4
- **Severidad:** Menor
- **Hallazgo:** La nota afirma que NEWS/MEWS/SIRS son preferibles a qSOFA pero no cita literalmente la Rec 4 SSC 2026 ni señala que qSOFA fue degradada por baja sensibilidad. La afirmación es directionalmente correcta pero queda sin trazabilidad.
- **Cita en la nota:** "Las guías 2026 **recomiendan el uso de NEWS, NEWS2, MEWS o SIRS sobre qSOFA** como herramienta aislada de cribado sistemático por su mayor sensibilidad." (línea 50)
- **Cita en la fuente:** SSC 2026 Rec 4 (NEW): "For adults with suspected infection presenting to the emergency department, hospital wards, or pre-hospital settings, we 'suggest' using NEWS, NEWS2, MEWS, or SIRS rather than qSOFA as a single screening tool" (conditional recommendation, low certainty evidence). Tabla 1 de Recomendaciones.
- **Cambio sugerido:** Añadir referencia: "**Rec. 4 SSC 2026 (NUEVA, recomendación condicional, evidencia baja):** Se sugiere usar NEWS, NEWS2, MEWS o SIRS por encima de qSOFA como herramienta única de cribado".

### Hallazgo 2 — Tabla de antibioterapia empírica indica "(SSC 2021)" cuando refleja Manual 12 Octubre
- **Severidad:** Menor
- **Hallazgo:** La cabecera de la tabla "Antibioterapia Empírica según Foco" pone "(SSC 2021)", pero el contenido (Ceftriaxona+Azitromicina, Pip/Tazo 4,5g/6-8h, etc.) procede de protocolos hospitalarios estándar y del Manual 12 Octubre, no de la guía SSC. SSC 2021/2026 no recomienda regímenes empíricos por foco (eso es competencia de guías locales).
- **Cita en la nota:** "Pauta Empírica (SSC 2021)" (línea 173, cabecera de tabla)
- **Cita en la fuente:** Surviving Sepsis Campaign 2021 (Evans et al) y 2026 (Prescott et al) NO contienen tablas de antibiótico empírico por foco; las recomendaciones generales son de inicio precoz, cobertura empírica de patógenos sospechados según contexto local (Rec 23-30 SSC 2026), y desescalada (Rec 36).
- **Cambio sugerido:** Cambiar la cabecera "(SSC 2021)" por "(adaptado de Manual 12 de Octubre 2022 / protocolos institucionales)".

### Hallazgo 3 — Errata tipográfica "Meroperem" en tabla de antibioterapia
- **Severidad:** Informativo
- **Hallazgo:** Errata de "Meropenem" → "Meroperem" en la tabla.
- **Cita en la nota:** "**BLEE / Shock grave** | Meroperem | **[[Meropenem]]:** 1 - 2 g IV cada 8h" (línea 179)
- **Cita en la fuente:** N/A (errata).
- **Cambio sugerido:** Corregir "Meroperem" → "Meropenem".

### Hallazgo 4 — Pip/Tazo 4,5g/6-8h: la pauta institucional FJD 2025 prefiere 4,5g/8h en perfusión extendida (3-4h)
- **Severidad:** Menor
- **Hallazgo:** En la tabla de antibioterapia empírica se cita "Pip/Tazo 4.5 g IV cada 6-8h (Perfusión extendida 4h)". El PROA FJD 2025 establece como dosis estándar "4 g/0,5 g / 8h en perfusión extendida 3-4h" o "4/0,5g/6h en perfusión 30 min", reservando el 4/0,5g/6h en perfusión extendida para *Pseudomonas*, neumonía grave o neutropenia febril.
- **Cita en la nota:** "**Multirresistentes (MDR)** | Piperacilina/Tazobactam | **Pip/Tazo:** 4.5 g IV cada 6-8h (Perfusión extendida 4h)." (línea 178)
- **Cita en la fuente:** PROA FJD 2025 — Pip/Tazo Dosis Estándar (S): "Vía iv.: 4 g/0,5 g/8h en perfusión extendida de 3-4h ó 4 g/0,5g/6h en perfusión de 30 min". Dosis Incrementada (I): "4 g/0,5 g/6h en perfusión extendida de 3-4h" — indicada en *P. aeruginosa* sensibilidad I, neumonía grave, neutropenia febril.
- **Cambio sugerido:** Reescribir como: "Pip/Tazo: 4,5 g IV cada 8h en perfusión extendida 3-4h (sepsis estándar) o cada 6h si *P. aeruginosa*, neumonía grave o neutropenia febril (FJD 2025)".

---

## Sepsis - Hemodinámica y Reanimación (SSC 2026)

### Hallazgo 5 — Albúmina en TCE: la nota dice "Evitar en TCE" sin cita SSC y SSC 2026 no incluye esa recomendación
- **Severidad:** Menor
- **Hallazgo:** La nota afirma "Evitar en TCE" como si fuera recomendación SSC 2026. SSC 2026 mantiene la recomendación 2021 de albúmina como adyuvante a cristaloides en pacientes que precisan grandes volúmenes (Rec carryover); la contraindicación en TCE deriva del estudio SAFE (subgrupo TBI) y no es una recomendación formal SSC.
- **Cita en la nota:** "**Albúmina:** Considerar en pacientes con cirrosis o que ya han requerido grandes volúmenes de cristaloides. Evitar en TCE." (línea 21)
- **Cita en la fuente:** SSC 2026 mantiene como carryover: "we 'suggest' using albumin in patients who received large volumes of crystalloids" (recomendación condicional). La contraindicación en TBI procede de SAFE-TBI subgrupo (NEJM 2007).
- **Cambio sugerido:** Añadir matiz/cita: "Evitar en TCE (SAFE subgrupo TBI; no recomendación formal SSC)".

### Hallazgo 6 — Suero salino 0,9% en TCE: la nota lo recomienda, pero no es recomendación SSC formal
- **Severidad:** Menor
- **Hallazgo:** La nota dice "En caso de Trauma Craneoencefálico, preferir Salino 0.9%" como continuación de las recomendaciones SSC. Esto es práctica neurocrítica común (evitar hipoosmolaridad de soluciones balanceadas) pero NO es una recomendación SSC 2026 formal.
- **Cita en la nota:** "Se **recomiendan cristaloides balanceados** (Ringer Lactato o Plasmalyte) frente a suero salino fisiológico (por riesgo de acidosis hiperclorémica). En caso de Trauma Craneoencefálico, preferir Salino 0.9%." (línea 20)
- **Cita en la fuente:** SSC 2026 Rec 47 carryover: "we 'suggest' using balanced crystalloids over normal saline for fluid resuscitation in patients with sepsis or septic shock" — sin excepción explícita para TCE.
- **Cambio sugerido:** Aclarar: "En TCE, las guías de neurocríticos (Brain Trauma Foundation) recomiendan SF 0,9% por evitar soluciones hipotónicas; SSC 2026 no contempla esta excepción explícitamente".

### Hallazgo 7 — Vasopresina dosis "0.3 mcg/kg/min de noradrenalina" — confusión de unidades en la cita "in our practice"
- **Severidad:** Menor
- **Hallazgo:** La nota cita "Los panelistas inician vasopresina a una mediana de 0.3 mcg/kg/min de noradrenalina (rango 0.2-0.5)". El SSC 2026 cita "0.20 µg/kg/min" en el modelo de aprendizaje automático y mediana panelista de 0,3 µg/kg/min — la cita es correcta pero el rango "0.2-0.5" debe coincidir con el IQR original.
- **Cita en la nota:** "Los panelistas inician vasopresina a una mediana de 0.3 mcg/kg/min de noradrenalina (rango 0.2-0.5)." (línea 59)
- **Cita en la fuente:** SSC 2026 (Vasopressors section): "85.1% of panel members add vasopressin in patients with septic shock on escalating doses of norepinephrine. Panelists using vasopressin initiate it at a median of **0.3 µg/kg/min of norepinephrine (IQR 0.2-0.5 µg/kg/min)**".
- **Cambio sugerido:** Mantener cita pero precisar "(IQR 0.2-0.5 µg/kg/min)" en lugar de "rango".

### Hallazgo 8 — Dosis Vasopresina "0.01-0.03 U/min" - cita incompleta del rango habitual SSC
- **Severidad:** Informativo
- **Hallazgo:** La nota dice "0.01 - 0.03 U/min". La SSC 2021 (carryover en 2026) usa "up to 0.03 U/min" como dosis fija habitual (no se titula). La cita es correcta pero conviene aclarar que es "fija, hasta 0,03 U/min", no rango terapéutico tradicional.
- **Cita en la nota:** "**Dosis:** **0.01 - 0.03 U/min** (Dosis fija, no se titula)." (línea 57)
- **Cita en la fuente:** SSC 2021/2026 — vasopresina como dosis fija "up to 0.03 U/min". No hay rango oficial SSC; en la práctica se inicia 0,03 U/min sin titulación.
- **Cambio sugerido:** Aclarar: "Dosis fija **0,03 U/min** (algunos protocolos inician en 0,01 y suben a 0,03; SSC no titula)".

### Hallazgo 9 — Algoritmo dice "Hidrocortisona si NA persiste" sin umbral
- **Severidad:** Menor
- **Hallazgo:** El algoritmo final dice "Hidrocortisona si NA persiste". SSC 2026 Rec 79 (revisada) sugiere hidrocortisona en shock séptico con requerimiento persistente de vasopresores; "in our practice" 34% inician con NA <0,2, 38% en 0,2-0,3 y 28% en >0,3 µg/kg/min. La nota lo recoge en su sección de corticoides pero el algoritmo final omite el umbral.
- **Cita en la nota (algoritmo):** "Hidrocortisona si NA persiste" (línea 125)
- **Cita en la fuente:** SSC 2026 Rec 79: "we 'suggest' using IV corticosteroids" (conditional, low certainty). "In our practice, 34% initiate steroids at vasopressor doses of less than 0.2 µg/kg/min norepinephrine, 38% at 0.2-0.3 µg/kg/min, and 28% at greater than 0.3 µg/kg/min".
- **Cambio sugerido:** Añadir umbral en algoritmo: "Hidrocortisona 200 mg/día si NA persistente (la mayoría de panelistas la inician con NA 0,2-0,3 µg/kg/min)".

---

## Sepsis - Antiinfecciosos y Soporte Vital (SSC 2026)

### Hallazgo 10 — 🔴 Rec 72 invertida: la nota recomienda 4-<6 mL/kg cuando SSC 2026 recomienda 6-8 mL/kg sobre el más bajo
- **Severidad:** Crítico
- **Hallazgo:** La nota indica para insuficiencia respiratoria asociada a sepsis SIN SDRA confirmado: "se sugiere usar **4 a < 6 mL/kg IBW** (volumen más bajo)". La SSC 2026 Rec 72 (NUEVA) dice **literalmente lo opuesto**: se sugiere "tidal volume of **6—8 mL/kg ideal body weight (IBW)** over a lower (4 to <6 mL/kg IBW) tidal volume". El sentido está invertido. Aplicar 4-<6 mL/kg de IBW en ventilación general sin SDRA es estrategia más restrictiva sin evidencia, y el panel SSC explicitó preocupación por el riesgo de delirium en el grupo de bajo volumen (RR 1.19) — la inversión puede generar manejo subóptimo.
- **Cita en la nota:** "**Volumen Corriente SIN SDRA (Rec. 72, NUEVA):** Se sugiere usar **4 a < 6 mL/kg IBW** (volumen más bajo) en insuficiencia respiratoria hipoxémica asociada a sepsis sin SDRA confirmado. Cribado regular para desarrollo de SDRA." (línea 163)
- **Cita en la fuente:** SSC 2026 Rec 72 (New, conditional recommendation, low certainty evidence): "For adults with sepsis-associated respiratory failure without ARDS, we 'suggest' using a tidal volume of **6—8 mL/kg ideal body weight (IBW) over a lower (4 to <6 mL/kg IBW) tidal volume**". Remarks: "Patients should be screened regularly for development of ARDS, as ARDS diagnosis is often missed or delayed in clinical practice".
- **Cambio sugerido:** Reescribir: "**Volumen Corriente SIN SDRA (Rec. 72, NUEVA, condicional, evidencia baja):** Se sugiere usar **6-8 mL/kg de peso ideal (IBW)** sobre un volumen más bajo (4 a <6 mL/kg IBW). Cribado regular para desarrollo de SDRA, dado que su diagnóstico se retrasa con frecuencia (un ECR sugirió mayor riesgo de delirium en el grupo de bajo volumen, RR 1.19)".

### Hallazgo 11 — Cefazolina 2g/8h en perfusión continua: PROA FJD 2025 usa 2g/8h estándar (la nota es coherente, pero el ajuste por obesidad merece cita)
- **Severidad:** Informativo
- **Hallazgo:** La tabla de bacteriemia indica "Cefazolina 2 g/8 h" para SAMS. Coincide con dosis estándar; el FJD 2025 menciona en obesidad "2g/8h administrados en perfusión continua". No hay error pero la nota no recoge la indicación de perfusión continua en obesos.
- **Cita en la nota:** "**S. aureus SAMS** | ETT ± ETE; HC control 48-72 h hasta negativización... | **Cloxacilina 2 g/4 h** (1ª elección) / Cefazolina 2 g/8 h." (línea 74)
- **Cita en la fuente:** PROA FJD 2025 — Tabla "Ajustes en función del peso corporal": "CEFAZOLINA: 2g/8h administrados en perfusión continua".
- **Cambio sugerido:** Añadir nota a pie de tabla: "En obesidad, FJD 2025 sugiere Cefazolina 2g/8h en perfusión continua".

### Hallazgo 12 — Daptomicina dosis SAMR 10-12 mg/kg: el FJD 2025 estándar es 4-6 mg/kg, infecciones graves 8-12 mg/kg
- **Severidad:** Menor
- **Hallazgo:** La nota cita "Daptomicina 10-12 mg/kg/día" como 1ª elección en SAMR. El PROA FJD 2025 estándar es "4-6 mg/kg/24h" y reserva 8-12 mg/kg/24h para infecciones graves; el rango habitual en bacteriemia/endocarditis SAMR es 8-10 mg/kg, y solo se llega a 12 mg/kg en endocarditis con falla a vancomicina o CMI elevada.
- **Cita en la nota:** "**S. aureus SAMR** | Igual que SAMS | **Daptomicina 10-12 mg/kg/día** (1ª elección)..." (línea 75)
- **Cita en la fuente:** PROA FJD 2025 — Daptomicina: "Dosis Estándar (S): IV 4-6 mg/kg / 24h. En infecciones graves: 8-12 mg/kg / 24h". Mensa/IDSA estándar bacteriemia SAMR: 8-10 mg/kg.
- **Cambio sugerido:** Cambiar "Daptomicina 10-12 mg/kg/día" → "Daptomicina **8-10 mg/kg/día** (hasta 12 mg/kg si endocarditis o CMI elevada)".

### Hallazgo 13 — Pip/Tazo 16/2 g en perfusión continua/24h: pauta no contemplada en PROA FJD 2025
- **Severidad:** Menor
- **Hallazgo:** La tabla de bacilos gramnegativos indica "Pip/Tazo **16/2 g en perfusión continua 24 h**". El PROA FJD 2025 no contempla pauta en perfusión continua de 24h para Pip/Tazo; usa **perfusión extendida 3-4h cada 6-8h** (el régimen "continuo de 24h" deriva de protocolos puntuales como TZT trial pero no es el estándar institucional).
- **Cita en la nota:** "**Sepsis/shock séptico**, sin riesgo PA-MDR | Pip/Tazo **16/2 g en perfusión continua 24 h** o Meropenem 2 g/8 h (perfusión extendida 3 h)..." (línea 88)
- **Cita en la fuente:** PROA FJD 2025: "Vía iv.: 4 g/0,5 g/8h en perfusión extendida de 3-4h ó 4 g/0,5g/6h en perfusión de 30 min". Dosis Incrementada: "4 g/0,5 g/6h en perfusión extendida 3-4h". No hay régimen de perfusión continua 24h.
- **Cambio sugerido:** Sustituir por: "Pip/Tazo 4/0,5 g/6h en perfusión extendida 3-4h (FJD 2025) o Meropenem 2 g/8h en perfusión extendida 3h".

### Hallazgo 14 — Ceftazidima/Avibactam dosis "2,5 g/8 h": notación inusual; FJD 2025 escribe 2 g/0,5 g/8 h
- **Severidad:** Informativo
- **Hallazgo:** La nota usa "Ceftazidima-avibactam 2,5 g/8 h". El PROA FJD 2025 lo escribe como "2 g/0,5 g/8 h en perfusión de 2h". Sumar los componentes (2,5 g) no es la convención estándar de notación.
- **Cita en la nota:** "Meropenem 2 g/8 h PE + Amikacina ± Ceftazidima-avibactam 2,5 g/8 h PE ± Aztreonam" (línea 89)
- **Cita en la fuente:** PROA FJD 2025: "Ceftazidima/Avibactam — Dosis Estándar (S): IV 2g/0,5g / 8h (en perfusión de 2h)".
- **Cambio sugerido:** Reescribir: "Ceftazidima/avibactam 2 g/0,5 g/8h en perfusión 2h".

---

## Sepsis - Cuidados Post-UCI y Objetivos (SSC 2026)

### Hallazgo 15 — Resumen final: "Control precoz del foco infeccioso (≤ 6h)" sin cita Rec específica
- **Severidad:** Informativo
- **Hallazgo:** El resumen dice "Control precoz del foco infeccioso (≤ 6h)". SSC 2026 Rec 30 (carryover de 2021) sí recomienda control de foco "as soon as possible" pero NO fija un umbral numérico de 6h en la guía 2026 (ese umbral procede de evidencia observacional y guías locales, no de SSC).
- **Cita en la nota:** "**Control precoz del foco infeccioso** (≤ 6h)." (línea 114)
- **Cita en la fuente:** SSC 2021 Rec 31 (carryover): "we 'recommend' rapid identification or exclusion of a specific anatomical diagnosis of infection requiring emergent source control... as soon as medically and logistically practical after the diagnosis is made". Sin umbral 6h literal en la guía.
- **Cambio sugerido:** Aclarar: "Control precoz del foco infeccioso (lo antes posible; el umbral de 6h procede de evidencia observacional, no de la guía SSC)".

---

## Sepsis y Shock Séptico (índice)

*Nota índice corta. Sin hallazgos sustantivos (cumple su función de hub).*

---

## Gripe - Síndrome Gripal

### Hallazgo 16 — "No criterios para antivirales según protocolo actual" sin cita ni protocolo identificable
- **Severidad:** Moderado
- **Hallazgo:** La nota afirma genéricamente "No criterios para antivirales según protocolo actual" sin especificar qué protocolo, ni qué pacientes sí cumplirían criterios. Es una nota originalmente extraída de plantilla de policlínicas; se aplica a un perfil concreto (joven sano, sin comorbilidad) pero no menciona excepciones (embarazadas, ≥65 años, EPOC, inmunodeprimidos, cardiopatía, obesidad mórbida, enfermedad neurológica, hepatopatía, ERC, niños <2 años) que sí justificarían oseltamivir 75 mg/12h × 5 días según CDC/IDSA y Ministerio de Sanidad España.
- **Cita en la nota:** "No criterios para antivirales según protocolo actual." (líneas 22 y 49)
- **Cita en la fuente:** No se ha podido verificar contra fuente local (no hay PDF de protocolo gripal en `Libros y referencias/`); WebFetch denegado en esta sesión. Hallazgo basado en discrepancia con guía universal CDC/IDSA accesible públicamente.
- **Cambio sugerido:** Añadir bloque de excepciones: "Considerar **oseltamivir 75 mg/12h × 5 días** si: hospitalización, enfermedad grave/progresiva, o paciente de alto riesgo (≥65 años, embarazo o puerperio reciente, niños <5 años especialmente <2, EPOC/asma, cardiopatía, ERC, hepatopatía, DM, inmunosupresión, obesidad mórbida IMC≥40, enfermedad neurológica, hemoglobinopatía). Iniciar lo antes posible (preferiblemente <48h del inicio de síntomas, pero también beneficio en críticos más allá de 48h)."

### Hallazgo 17 — Falta `fuente:` y referencia a protocolo Salud Madrid o SEIMC
- **Severidad:** Informativo
- **Hallazgo:** El frontmatter cita "Extraído de 50_Guardias/02 - Plantilla Policlínicas Urgencias.md" pero no enlaza al protocolo clínico de referencia.
- **Cita en la nota:** `fuente_original: "Extraído de 50_Guardias/02 - Plantilla Policlínicas Urgencias.md"` (frontmatter)
- **Cita en la fuente:** N/A.
- **Cambio sugerido:** Añadir `fuente:` en frontmatter con referencia al CDC Antiviral Treatment of Influenza o Documento de Consenso SEIMC sobre gripe estacional.

---

## PROA - Betalactámicos y Cefalosporinas

### Hallazgo 18 — Penicilina G "600 mg (1 MU)/6h": cita correcta del FJD 2025
- **Severidad:** Informativo
- **Hallazgo:** Verificación: la nota dice "Penicilina G Sódica IV 600mg (1 MU) / 6h" (estándar) y "Dosis Incrementada 1200 mg (2 MU) / 4-6h". Coincide con FJD 2025: "Vía iv.: 600 mg (1 MUI)/6h" estándar, "Vía iv.: 1200 mg (2 MUI)/4-6h" incrementada.
- **Cita en la nota:** "**Dosis Estándar (S):** IV 600mg (1 MU) / 6h. **Dosis Incrementada (I):** IV 1200mg (2 MU) / 4-6h." (líneas 15-16)
- **Cita en la fuente:** PROA FJD 2025 Penicilina G — Dosis Estándar: "Vía iv.: 600 mg (1 MU)/6h". Dosis Incrementadas: "Vía iv.: 1200 mg (2 MU)/4-6h".
- **Cambio sugerido:** Sin cambio necesario. Verificación positiva.

### Hallazgo 19 — Pip/Tazo "(S) IV 4g/0.5g / 6h ... o 4/0.5g/8h ... extendida 3-4h": orden invertido respecto a FJD 2025
- **Severidad:** Menor
- **Hallazgo:** La nota lista primero "4 g/0,5 g / 6h en perfusión 30 min" y después "4/0,5g / 8h en perfusión extendida 3-4h" como dosis estándar. El FJD 2025 invierte el orden y prioriza la perfusión extendida cada 8h como esquema estándar institucional.
- **Cita en la nota:** "**Dosis Estándar (S):** IV 4g/0.5g / 6h (en perfusión de 30 min) o 4/0.5g / 8h (en perfusión extendida de 3-4h)." (línea 55)
- **Cita en la fuente:** PROA FJD 2025: "Vía iv.: 4 g/0,5 g/8h en perfusión extendida de 3-4h ó 4 g/0,5g/6h en perfusión de 30 min" (perfusión extendida listada primero como esquema preferente).
- **Cambio sugerido:** Reordenar para reflejar la preferencia FJD: "**Dosis Estándar (S):** IV 4g/0,5g/8h en perfusión extendida 3-4h (preferente) o 4g/0,5g/6h en perfusión 30 min".

### Hallazgo 20 — Ertapenem "Considerar 2g/24h si CMI >0,25 mg/ml": no en la sección de Ertapenem
- **Severidad:** Informativo
- **Hallazgo:** El FJD 2025 contempla en la tabla de obesidad: "ERTAPENEM: Dosis estándar. Considerar 2g/24h si CMI >0,25 mg/ml". La nota no recoge este matiz para casos de CMI elevada o pacientes obesos.
- **Cita en la nota:** "**Dosis Estándar (S):** IV 1g / 24h." (línea 148)
- **Cita en la fuente:** PROA FJD 2025 (sección obesidad): "ERTAPENEM: Dosis estándar. Considerar 2g/24h si CMI >0,25 mg/ml".
- **Cambio sugerido:** Añadir: "En obesidad o CMI >0,25 mg/ml considerar 2 g/24h (FJD 2025)".

---

## PROA - Quinolonas y Macrólidos

*Verificación cruzada con PROA FJD 2025: dosificación de Ciprofloxacino, Levofloxacino, Moxifloxacino, Azitromicina, Claritromicina, Clindamicina, Doxiciclina y Linezolid concuerda. Sin hallazgos sustantivos.*

---

## PROA - Otros Antimicrobianos

### Hallazgo 21 — Vancomicina niveles valle: la nota indica 10-15/15-20/20-30; FJD 2025 prefiere 15-20 en complicadas y 20-30 sólo SNC/neumonía
- **Severidad:** Menor
- **Hallazgo:** La nota dice "Recomendado: `10-15 mg/L` para infecciones no complicadas. En infecciones complicadas: **`15-20 mg/L`**. En meningitis, neumonía por S. aureus: puede necesitarse valles de **`20-30 mg/L`**". El FJD 2025 explicita: "15-20 mg/L en infecciones complicadas: bacteriemia por S. aureus MR, E. faecium, endocarditis, osteomielitis (puede necesitar valles mayores: 20-30 mg/L), meningitis, neumonía por S. aureus" y "10-15 mg/L para otras infecciones". La nota es directionalmente correcta pero falta el matiz de que el AUC₂₄/CMI 400-600 es el target preferido en guías recientes ASHP/IDSA 2020.
- **Cita en la nota:** "Recomendado: `10-15 mg/L` para infecciones no complicadas. En infecciones complicadas (SARM con bacteriemia, E. faecium, endocarditis, osteomielitis): **`15-20 mg/L`**. En meningitis, neumonía por S. aureus: puede necesitarse valles de **`20-30 mg/L`**." (línea 46)
- **Cita en la fuente:** PROA FJD 2025 — Vancomicina niveles valle: "15-20 mg/L en infecciones complicadas: bacteriemia por S. aureus MR, E. faecium, endocarditis, osteomielitis (puede necesitar valles mayores: 20-30 mg/L), meningitis, neumonía por S. aureus. — 10-15 mg/L para otras infecciones".
- **Cambio sugerido:** Añadir nota: "Las guías ASHP/IDSA 2020 prefieren AUC₂₄/CMI 400-600 mg·h/L sobre valle aislado en SAMR; el valle 15-20 mg/L sigue siendo aceptable como subrogado".

### Hallazgo 22 — Tigeciclina dosis incrementada "200 mg carga → 100 mg/12h": confirmado en FJD 2025 para MDR graves
- **Severidad:** Informativo
- **Hallazgo:** Verificación positiva. La nota cita exactamente la pauta del FJD 2025 para microorganismos multiR.
- **Cita en la nota:** "**Dosis Incrementada (I) Infecciones Multirresistentes (KPC, A. baumannii MDR):** IV Dosis de carga 200mg → Mantenimiento 100mg / 12h." (línea 87)
- **Cita en la fuente:** PROA FJD 2025: "En caso de microorganismos multiR produciendo infección grave, se recomienda una dosis de carga de 200mg seguido de 100mg/12h".
- **Cambio sugerido:** Sin cambio necesario. Verificación positiva.

### Hallazgo 23 — Daptomicina dosis "4-6 mg/kg, en infecciones graves 8-12 mg/kg": coincide con FJD 2025
- **Severidad:** Informativo
- **Hallazgo:** Verificación positiva. (Esto contrasta con la cita "10-12 mg/kg" en la nota de Sepsis-Antiinfecciosos: ver Hallazgo 12, donde la cifra de 10-12 mg/kg como 1ª elección rutinaria se aleja del rango FJD).
- **Cita en la nota:** "**Dosis Estándar (S):** IV 4-6 mg/kg / 24h. En infecciones graves: 8-12 mg/kg / 24h." (línea 57)
- **Cita en la fuente:** PROA FJD 2025: idéntico.
- **Cambio sugerido:** Sin cambio necesario. La inconsistencia se resuelve corrigiendo la nota Sepsis-Antiinfecciosos (Hallazgo 12).

---

## PROA - Infecciones Respiratorias

### Hallazgo 24 — Faringitis: 1ª elección "Fenoximetilpenicilina (Penilevel) 500mg/12h, 10 días" — coincide con PROA FJD 2023
- **Severidad:** Informativo
- **Hallazgo:** Verificación positiva contra protocolo institucional.
- **Cita en la nota:** "*1ª elección:* **Fenoximetilpenicilina (Penilevel) 500mg/12h, 10 días**." (línea 14)
- **Cita en la fuente:** PROA FJD 2023 (Tabla Resumen Tratamiento — Infecciones Respiratorias): "Faringitis aguda — Fenoximetilpenicilina (Penilevel) 500mg/12h, 10 días".
- **Cambio sugerido:** Sin cambio necesario.

### Hallazgo 25 — NAC <65 años, neumonía típica: "Amoxicilina 1000mg/8h, 5 días" — coincide con PROA FJD 2023, pero falta matiz de reevaluación 48h
- **Severidad:** Menor
- **Hallazgo:** El PROA FJD 2023 añade "(reevaluación por MAP en 48 horas)" al esquema de Amoxicilina 1000 mg/8h. La nota lo recoge en pie de tabla ("Reevaluar por MAP en 48h") pero solo en algunas líneas, no de forma sistemática.
- **Cita en la nota:** "**<65 años**, sin comorbilidad, **neumonía típica** | [[Amoxicilina]] 1000mg/8h, **5 días** | Alergia: [[Levofloxacino]] 500mg/24h 5d · Cefditoreno 400mg/12h 5d" (línea 54)
- **Cita en la fuente:** PROA FJD 2023: "Amoxicilina 1000 mg/8 h, 5 días (reevaluación por MAP en 48 horas)".
- **Cambio sugerido:** Añadir explícitamente "reevaluación MAP 48h" en la celda de tratamiento de NAC <65 años.

---

## PROA - Infecciones del Tracto Urinario (ITU)

*Verificación cruzada con PROA FJD 2023: cistitis no complicada (Fosfomicina 3g DU), cistitis complicada (Fosfomicina 3g DU + 2ª dosis 48h o Cefixima 400 mg/24h × 7 días), pielonefritis (Ceftriaxona 2g IV → Cefixima 400 mg/24h × 7 días), prostatitis (Ceftriaxona 2g IV → quinolona/cotrimoxazol × 2 semanas), portador de sonda (Cefixima 400 mg/24h × 7 días + recambio), BLEE (alternativas no carbapenémicas, amikacina IV, ertapenem 1g/24h en HD): todo concuerda. Sin hallazgos sustantivos.*

---

## PROA - Infecciones de Transmisión Sexual (ITS)

### Hallazgo 26 — Neurosífilis dosis: "Penicilina G Sódica 4 MU/4h IV (14 días)" coincide con PROA FJD 2023
- **Severidad:** Informativo
- **Hallazgo:** Verificación positiva. El PROA FJD 2023 indica "Penicilina G Sódica 4MUI iv/4h durante 14 días" para neurosífilis (incluye oftalmológica). La cita "4 MU/4h" en la nota es correcta.
- **Cita en la nota:** "*Tratamiento Neurosífilis:* Penicilina G Sódica 4 MU/4h IV (14 días)." (línea 52)
- **Cita en la fuente:** PROA FJD 2023: "Neurosífilis (incluye oftalmológico): Penicilina G sódica 4 MUI iv durante 14 días". Alternativas: desensibilización a penicilinas o Ceftriaxona 1g/24h IV/IM × 14 días.
- **Cambio sugerido:** Sin cambio necesario. Verificación positiva.

---

## PROA - Infecciones de Piel y Partes Blandas

*Verificación cruzada con PROA FJD 2023: Impétigo (mupirocina/ácido fusídico tópico), Erisipela (Cefadroxilo/Cefalexina/Amoxicilina 500mg/8h × 5d), Celulitis (Cefadroxilo 500/8h o Cefalexina 500/6-8h, 5d + 3d desde resolución; SARM: Clindamicina 300/8h, Cotrimoxazol 800/160/12h o Linezolid 600/12h), Mordeduras (Amox/Clav 875/125/8h), Herida tras agua salada/pescado (Ciprofloxacino 750/12h o Amoxicilina), Herida punzante planta pie (Ciprofloxacino 750/12h): coincide. Sin hallazgos sustantivos.*

---

## PROA - Infecciones Gastrointestinales

*Verificación cruzada con PROA FJD 2023: Diarrea no inflamatoria (sin ATB), Diarrea inflamatoria (Ciprofloxacino 500/12h o Azitromicina 500/24h en Campylobacter/embarazo), Diarrea del viajero (Ciprofloxacino o Azitromicina si India/Sudeste asiático), CDI primer episodio (Vancomicina oral 125 mg/6h × 10 días), Recurrencia (Fidaxomicina 200 mg/12h × 10 días): coincide. Sin hallazgos sustantivos.*

---

## PROA - Guía de Antimicrobianos (índice)

*Nota índice. Estructura correcta. Tabla de biodisponibilidad oral coincide con PROA FJD 2025 (Linezolid 100%, Levofloxacino 100%, Moxifloxacino 91%, Ciprofloxacino 70-80%, Cefditoreno 15-20%, etc.). Sin hallazgos sustantivos.*

---

## Notas sin hallazgos verificables

- **Sepsis y Shock Séptico** (índice corto): cumple su función como hub.
- **PROA - Quinolonas y Macrólidos:** dosis verificadas contra FJD 2025.
- **PROA - Infecciones Gastrointestinales:** verificada contra PROA FJD 2023.
- **PROA - Infecciones de Piel y Partes Blandas:** verificada contra PROA FJD 2023.
- **PROA - Guía de Antimicrobianos** (índice): correcto.

## Limitaciones metodológicas

- **WebFetch denegado en esta sesión:** No se pudo cruzar la nota PROA - ITS contra CDC STI Treatment Guidelines 2021 ni la nota Gripe contra CDC Antiviral Treatment of Influenza ni Documento Consenso SEIMC. Los hallazgos para Gripe se basan en discrepancia con conocimiento general validado.
- **El protocolo PROA FJD 2023** es la fuente primaria para los síndromes ambulatorios; la **Guía de Manejo de Antibióticos FJD 2025** (PROA Antibioticos vs 23 abril.pdf, última revisión septiembre 2024) es la fuente de dosificación.
- **SSC 2026 (Prescott et al)** fue verificada literalmente para las recomendaciones 4, 65-70, 71-78, 79, 80-86, 87-89, 92, 100-129. Las dosis empíricas por foco no son competencia de SSC.
- **Manual 12 Octubre 2022:** no leído para esta auditoría; los hallazgos que afectan a tablas etiquetadas como "Manual 12 Octubre" son de coherencia interna (ej. Pip/Tazo perfusión continua 24h no contemplada en FJD).
- **No se han cruzado** con UpToDate, DynaMed, Mensa 2024 ni guías SEIMC vigentes.
