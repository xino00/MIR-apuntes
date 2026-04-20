---
tags: [auditoria, fact-check, indice]
fecha_auditoria: 2026-04-20
auditor: Claude Opus 4.7
description: "Índice maestro del fact-check del vault 10_Patologias - estado por especialidad"
---

# Fact-check del vault — INDEX

**Fecha:** 2026-04-20
**Scope total:** 14 especialidades · ~178 notas en `10_Patologias/`
**Estado:** ✅ **Fase 2 COMPLETA**. 14/14 especialidades auditadas · 173 notas · **353 hallazgos · 41🔴**.

## Cómo leer este informe

Cada especialidad tiene su propio archivo. Cada hallazgo lleva:

- **Severidad** con código de color
- **Cita literal en la nota** (texto y línea aproximada)
- **Cita literal en la fuente** (página/sección)
- **Cambio sugerido** (texto exacto a aplicar)

| Color | Severidad | Significado clínico |
|---|---|---|
| 🔴 | Crítico | Dosis incorrectas, criterios de emergencia mal, contraindicaciones omitidas, recomendaciones obsoletas con riesgo |
| 🟠 | Moderado | Cutoffs diagnósticos desactualizados, algoritmos terapéuticos simplificados o con orden equivocado, indicación quirúrgica con timing erróneo |
| 🟢 | Menor | Clasificación obsoleta sin impacto en manejo, año de guía mal citado, definición incompleta |
| ⚪ | Informativo | Falta `fuente:` en frontmatter, oportunidades de mejora, `[OUTDATED-MANUAL]` informativo |

`[OUTDATED-MANUAL]` = el Manual 12 Octubre 2022 ha quedado desactualizado por una guía posterior; prevalece la guía nueva.

## Estado por especialidad

| # | Especialidad | Notas | Estado | Hallazgos | Informe |
|---|---|---|---|---|---|
| 01 | Cardiología | **36/36** | ✅✅ **Aplicado 2026-04-20 (95/105 ✅ · 7 ⚠ · 2 ❌ · 1 ❓ · 13🔴 al 100%)** | **105 (13🔴 · 46🟠 · 30🟢 · 16⚪)** | [[01_Cardio]] · recheck → [[_recheck_cardio]] |
| 02 | Neurología | **18/18** | ✅ Fase 2 Ola 1 | **14 (2🔴 · 6🟠 · 3🟢 · 3⚪)** | [[02_Neuro]] |
| 03 | Infecciosas | **15/15** | ✅ Fase 2 Ola 1 | **26 (1🔴 · 11🟠 · 10🟢 · 4⚪)** | [[03_Infecciosas]] |
| 04 | Digestivo | **18/18** | ✅✅ **Aplicado 2026-04-21 (24/27 ✅ · 2 ⚠ · 0 ❌ · 1 ❓ · 5🔴 al 100%)** | **27 (5🔴 · 9🟠 · 6🟢 · 7⚪)** | [[04_Digestivo]] · recheck → [[_recheck_digestivo]] |
| 05 | Neumología | **17/17** | ✅ Fase 2 Ola 1 | **16 (0🔴 · 7🟠 · 5🟢 · 4⚪)** | [[05_Neumologia]] |
| 06 | Nefrología | **9/9** | ✅ Fase 2 Ola 1 | **22 (1🔴 · 9🟠 · 9🟢 · 3⚪)** | [[06_Nefrologia]] |
| 07 | Reumatología | **10/10** | ✅ Fase 2 Ola 3 | **34 (5🔴 · 12🟠 · 9🟢 · 8⚪)** | [[07_Reumatologia]] |
| 08 | Hematología | **9/9** | ✅ Fase 2 Ola 2 | **16 (3🔴 · 7🟠 · 4🟢 · 2⚪)** | [[08_Hematologia]] |
| 09 | Endocrinología | **3/3** auditadas¹ | ✅ Fase 2 Ola 1 | **16 (4🔴 · 6🟠 · 4🟢 · 2⚪)** | [[09_Endocrino]] |
| 10 | ORL | **9/9** | ✅ Fase 2 Ola 2 | **14 (2🔴 · 5🟠 · 4🟢 · 3⚪)** | [[10_ORL]] |
| 11 | Urología | **4/4** | ✅ Fase 2 Ola 2 | **16 (1🔴 · 5🟠 · 6🟢 · 4⚪)** | [[11_Urologia]] |
| 12 | Traumatología | **15/15** | ✅ Fase 2 Ola 2 | **21 (3🔴 · 9🟠 · 4🟢 · 5⚪)** | [[12_Traumatologia]] |
| 13 | Dermatología | **3/3** | ✅✅ **Aplicado 2026-04-21 (18/19 ✅ · 1 ⚠ · 0 ❌ · 1🔴 al 100%)** | **12 (1🔴 · 5🟠 · 4🟢 · 2⚪)** | [[13_Dermatologia]] · recheck → [[_recheck_dermato]] |
| 14 | Psiquiatría | **7/7** | ✅ Fase 2 Ola 2 | **14 (0🔴 · 3🟠 · 4🟢 · 7⚪)** | [[14_Psiquiatria]] |

¹ Endocrino: el subagente auditó solo 3 notas porque CAD y SHH están **vacías** (apuntan a "imágenes del archivo original" sin contenido clínico). Las 4 críticas son de notas que existen pero requieren reescritura completa.

**Subtotales:**
- ✅ Cardio (Fase 1.5): 36 notas · 105 hallazgos · 13🔴 (46🟠 · 30🟢 · 16⚪)
- ✅ Ola 1 (Fase 2): 62 notas · 94 hallazgos · 8🔴 (39🟠 · 31🟢 · 16⚪)
- ✅ Ola 2 (Fase 2): 44 notas · 81 hallazgos · 9🔴 (29🟠 · 22🟢 · 21⚪)
- ✅ Ola 3 (Fase 2): 31 notas · 73 hallazgos · 11🔴 (26🟠 · 19🟢 · 17⚪)
- **TOTAL VAULT**: **173 notas · 353 hallazgos · 41🔴 (140🟠 · 102🟢 · 70⚪)**

## Hallazgos críticos de Fase 2 Ola 1 (8)

### Endocrinología (4)
1. **🔴 [[Cetoacidosis Diabética (CAD)]]** — Nota **vacía** (solo apunta a "imágenes del archivo original"). Urgencia vital sin contenido clínico utilizable. Reescribir completa con Manual 12 Oct cap 51 + ADA-EASD 2024.
2. **🔴 [[Síndrome Hiperglucémico Hiperosmolar (SHH)]]** — Nota **vacía** (idéntico a CAD). Mortalidad 10-20% sin contenido. Reescribir completa.
3. **🔴 [Endocrino — hallazgo H3]** — ver `09_Endocrino.md` para detalle (criterios diagnósticos CAD desactualizados: ADA-EASD 2024 baja glucemia a ≥200 mg/dl y elimina anión gap).
4. **🔴 [Endocrino — hallazgo H4]** — ver `09_Endocrino.md` (umbral K para retrasar insulina: Manual 3,3 → ADA 2024 3,5 mmol/l; resolución CAD: HCO3 ≥18 vs 15 + β-OHB <0,6).

### Infecciosas (1)
5. **🔴 [[Sepsis - Antiinfecciosos y Soporte Vital]]** — **Recomendación 72 SSC 2026 invertida**: nota dice "4 a <6 mL/kg IBW (volumen más bajo)" para insuficiencia respiratoria sin SDRA; SSC 2026 dice exactamente lo contrario: "6-8 mL/kg IBW sobre 4 a <6 mL/kg IBW". Riesgo clínico real en críticos.

### Nefrología (1)
6. **🔴 [[FRA - Diagnóstico y Manejo]]** — Cita "KDIGO 2023/2024" que **no existe**: la guía AKI vigente es **KDIGO 2012**. Resto de la nota debe revisarse para validar criterios.

### Neurología (2)
7. **🔴 [[Migraña - Guía Terapéutica Completa]]** — Lasmiditán: nota dice "máximo 1 dosis/24h"; ficha técnica española y SEN 2026 permiten **2ª dosis a ≥2h si no respuesta** (máx 200 mg/24h). Restricción priva al paciente de rescate eficaz.
8. **🔴 [[TCE Leve-Moderado]]** — Lenguaje informal/no profesional ("SE LO CASCAS SEGURO" para indicar TC) — compromete utilidad clínica formal. Reescribir antes de uso compartido o web.

### Neumología
Sin críticos 🔴 — 7🟠 moderados, mayoría sobre umbrales eosinófilos en biológicos AGNC y dosis Salbutamol en crisis adulto (4-10 puls vs GEMA 2-8 puls).

---

## Hallazgos críticos de Fase 2 Ola 2 (9)

### Hematología (3)
1. **🔴 [[Sdme Hemofagocitico]]** — Nota **vacía** (una sola línea: "Calcular SCORE HEMOFAGOCITICO"). HLH es urgencia con mortalidad ≈41%. Reescribir completa con criterios HLH-2004 (Manual 12 Oct p.1284, Tabla 5) y H-Score.
2. **🔴 [[Sdme Hemofagocitico]]** — Sin esquema terapéutico (dexametasona + etopósido HLH-94). Las notas de Pancitopenia y Hemolítica enlazan aquí asumiendo contenido inexistente.
3. **🔴 [[Anemia Ferropénica]]** — Dosis y umbral de transfusión cardíaca discrepan de Manual 12 Oct (p.1242-1243, p.509+1287). Ver detalle en `08_Hematologia.md`.

### ORL (2)
4. **🔴 [[Faringoamigdalitis Aguda]]** — Penicilina V pautada cada 12 h; PROA FJD 2025 indica **500 mg/6 h** (semivida ~30 min — riesgo real de fracaso de erradicación estreptocócica).
5. **🔴 [[Otitis Externa]]** — No menciona **otitis externa maligna** en diabéticos/inmunosuprimidos (entidad potencialmente mortal). Omisión que puede demorar diagnóstico.

### Urología (1)
6. **🔴 [[Escroto Agudo y Orquiepididimitis]]** — La nota desarrolla orquiepididimitis pero NO incluye torsión testicular como DDx obligatorio (ventana isquémica >6 h, eco-Doppler urgente, signos: teste ascendido/horizontalizado, ausencia reflejo cremastérico). Riesgo asistencial real. Manual 12 Oct cap.7 Tabla 2 (p.88-89).

### Traumatología (3)
7. **🔴 [[Esguince de Tobillo]]** — Cita "criterios Ottawa" pero NO los enumera. Para una nota de guardia es omisión grave.
8. **🔴 [[Heridas y Suturas]]** — Sin profilaxis tetánica (esquema vacunal Td + IGT por tipo de herida).
9. **🔴 [[Heridas y Suturas]]** — Sin profilaxis antibiótica de mordeduras (amox/clav, riesgo Capnocytophaga, antirrábica).

### Psiquiatría
Sin críticos 🔴 — la mayoría del contenido es transcripción fiel del Manual 12 Oct cap. 11 + NEJM 2014/2025; 3🟠 moderados sobre Delirium Tremens (CIWA-Ar 9+1 ítems, atribución 3-5% convulsiones, magnesio).

---

## Hallazgos críticos de Fase 2 Ola 3 (11)

### Digestivo (5)
1. **🔴 [[Complicaciones de la Cirrosis Hepática]]** — Sección "PROFILAXIS PBE" **vacía**. Manual 12 Oct cap.42 Tabla 9 da el régimen completo (norfloxacino 400/24h o ceftriaxona en sangrado).
2. **🔴 [[Complicaciones de la Cirrosis Hepática]]** — Antibioterapia empírica PBE sin pauta. Manual cap.42 Tabla 8: **ceftriaxona 2 g/24h IV × 5 días**.
3. **🔴 [[Hemorragia Digestiva Alta (HDA)]]** — Algoritmo HDA por hipertensión portal **ausente**. Falta: terlipresina/somatostatina + ceftriaxona 1 g/24h + endoscopia <12 h (Baveno VII).
4. **🔴 [[Pancreatitis Aguda]]** — Timing CPRE omite "**<12 h en shock séptico**" (Manual cap.39 p.561).
5. **🔴 [[Colangitis Aguda]]** — Falta **drenaje biliar urgente <24 h** como pilar terapéutico (Manual cap.73 p.1101).

### Reumatología (5)
6. **🔴 [[Gota - Artritis Gotosa Aguda]]** — Pauta colchicina **excede el máximo del Manual** (2 mg/día durante 4 días, cap.91 p.1378).
7. **🔴 [[EAS - 3. Urgencias y Banderas Rojas Reumatológicas]]** — Afirmación absoluta "**PROHIBIDOS corticoides en crisis renal esclerodérmica**" contradice Manual: solo prednisona >15 mg/día está proscrita; los pulsos NO se asocian al desencadenamiento (cap.92 p.1408).
8. **🔴 [[EAS - 3. Urgencias y Banderas Rojas Reumatológicas]]** — Umbral líquido sinovial séptico marcado en **>50.000 leucocitos** cuando Manual indica **>100.000**.
9. **🔴 [[Sarcoidosis - Diagnóstico y Manejo]]** — Prosa ilegible (bloque sin saltos) + **% Scadding incorrectos** (estadio II marcado al 30%, Manual dice 5%).
10. **🔴 [[Vasculitis - 2. Pequeño Vaso y ANCA]]** — Uso de epónimos "**Wegener / Churg-Strauss**" como nomenclatura primaria, contraviniendo Chapel Hill 2012 (GPA / EGPA).

### Dermatología (1)
11. **🔴 [[Sarna - Escabiosis]]** — Aislamiento ropa **72 h en la nota vs 1 semana en Manual 12 Oct cap.69 p.1038**. Discrepancia con impacto epidemiológico real.

---

## Hallazgos críticos de Cardiología (Top 13)

Resumen para acción inmediata si se decide aplicar antes de Fase 2:

1. **🔴 [[Fibrilación Auricular (FA)]]** — Migrar de **CHA₂DS₂-VASc** a **CHA₂DS₂-VA** (sexo eliminado, umbral universal ≥2). ESC AF 2024 §6.1.1 p.3341.
2. **🔴 [[Escala CHA2DS2-VASc y HAS-BLED]]** — Toda la nota basada en escala obsoleta + columnas hombre/mujer; reescribir con CHA₂DS₂-VA. ESC AF 2024.
3. **🔴 [[Insuficiencia cardiaca]]** — iSGLT2 en HFmrEF/HFpEF debe figurar como **Clase I-A** (Focused Update 2023 p.3633), no como recomendación condicionada.
4. **🔴 [[Endocarditis Infecciosa]]** — Cefazolina 6 g/día en MSSA → especificar **"en 3 dosis (2 g/8h)"**. ESC 2023.
5. **🔴 [[Endocarditis Infecciosa]]** — Añadir dosis específicas de **Penicilina G (12-18 MU/día)** y **Amoxicilina (12 g/día en 4-6 dosis)** en *Streptococcus*.
6. **🔴 [[Cardiopatía isquémica]]** — Cambiar "AAS 300 mg" por **162-325 mg masticada** (ACC/AHA 2025 SCA).
7. **🔴 [[Síndrome Coronario Agudo]]** — ACV isquémico como CI absoluta de fibrinolisis: la nota dice <6 meses; ACC/AHA 2025 SCA Tabla 14 dice **<3 meses**.
8. **🔴 [[Tratamiento Farmacológico de la Hipertensión]] / [[HTA - Medición y Diagnóstico]]** — Umbrales **MAPA invertidos** (la nota usa día ≥140/90, noche ≥120/80; ESC 2024 Tabla 5: día ≥135/85, 24h ≥130/80, noche ≥120/70).
9. **🔴 [[HTA - Riesgo Cardiovascular]]** — SCORE2 con cutoffs antiguos por edad (<50/50-69/≥70); ESC HTA 2024 usa **umbral único ≥10%** para iniciar tratamiento.
10. **🔴 [[Valvulopatías]]** — Indicación TAVI debe actualizarse: VHD 2025 admite TAVI en **≥70 años** (no ≥75); además faltan criterios cuantitativos PMR (EROA/Vol regurgitante).
11. **🔴 [[Síndrome Cardiorrenal]]** — Tiazidas como añadido sin advertencia: estudio **CLOROTIC** mostró **+46.5% Cr** con clortalidona; añadir warning explícito.
12. **🔴 [[Insuficiencia cardiaca aguda]]** — Algoritmo de descongestión sin secuencia clara de doblar furosemida + asociar tiazida (DOSE/CLOROTIC); revisar dosis y timing.
13. **🔴 [[SCA - Reperfusión]]** — Tiempo objetivo "puerta-balón" sin matiz de transferencia: ACC/AHA 2025 establece **PCI primaria ≤90 min** si centro PCI; **≤120 min** si transferencia, sino fibrinolisis ≤30 min.

## Próximos pasos sugeridos

- [ ] **Aplicar correcciones críticas** (41🔴 acumulados): priorizar antes de la rotación de junio 2026.
  - **Cardio: 13🔴** — cambios de guía (ESC AF 2024 → CHA₂DS₂-VA, ESC HTA 2024 MAPA, ACC/AHA 2025 SCA, VHD 2025 TAVI ≥70a).
  - **Endocrino: 4🔴** — CAD y SHH **vacías**, ADA-EASD 2024 cutoffs.
  - **Hemato: 3🔴** — HLH **vacío**, ferropenia dosis/transfusión.
  - **ORL: 2🔴** — Penicilina V intervalo (12h→6h) + otitis externa maligna ausente.
  - **Trauma: 3🔴** — Ottawa Ankle no enumerado, profilaxis tetánica + mordeduras ausentes.
  - **Digestivo: 5🔴** — Cirrosis (PBE×2), HDA varices, pancreatitis CPRE, colangitis drenaje.
  - **Reumato: 5🔴** — Colchicina dosis, corticoides crisis renal, líquido séptico cutoff, Sarcoidosis %, nomenclatura Chapel Hill.
  - **Dermato: 1🔴** — Sarna aislamiento ropa.
  - **Resto (Infecciosas, Nefro, Neuro, Uro): 5🔴** puntuales.
- [ ] **Notas vacías a reescribir** (4): `Cetoacidosis Diabética (CAD)`, `Síndrome Hiperglucémico Hiperosmolar (SHH)`, `Sdme Hemofagocitico`, secciones vacías en `Complicaciones de la Cirrosis Hepática` (PBE).
- [ ] **Re-auditoría con WebFetch autorizado**: 8 especialidades de Fase 2 tienen verificación parcial por denegación de WebFetch en sandbox. Especialmente importante para Reumato (EULAR/ACR/KDIGO 2024) y Dermato (AEDV Shingrix, EAACI urticaria, CDC escabiosis).
- [ ] Considerar añadir `last_fact_checked: 2026-04-20` al frontmatter de las notas auditadas como trazabilidad.

## Limitaciones metodológicas

- Auditoría comparativa contra guías citadas, no validación clínica independiente.
- Para algunos PDFs (ESC HF, ESC EI) WebFetch devolvió solo landing pages — ciertas verificaciones literales son parciales y se marcan como tales en el informe.
- No se han cruzado con UpToDate ni DynaMed.
- El Manual 12 Octubre 2022 está desactualizado en varias áreas; los hallazgos `[OUTDATED-MANUAL]` lo señalan explícitamente.

## Fuentes consultadas (Fase 1 + 1.5 + Fase 2 completa)

PDFs locales en `Libros y referencias/`:

**Cardiología (15 guías):**
- Manual de diagnóstico y terapéutica médicas H 12 Octubre 2022
- ACC/AHA/ACEP/NAEMSP/SCAI 2025 ACS Guideline (Rao et al, Circulation 2025;151:e771-e862)
- AHA/ACC 2026 Acute Pulmonary Embolism Guideline (Creager et al)
- ESC 2024 Elevated BP and Hypertension
- ESC 2024 Atrial Fibrillation
- ESC 2024 Peripheral Arterial and Aortic Diseases
- ESC 2023 Endocarditis (Eur Heart J 2023;44:3948-4042)
- ESC 2023 Cardiomyopathies
- ESC 2023 Heart Failure Focused Update
- ESC 2022 Ventricular Arrhythmias / SCD Prevention
- ESC/ERS 2022 Pulmonary Hypertension
- ESC 2021 Heart Failure
- ESC 2020 Adult Congenital Heart Disease
- ESC 2018 Syncope
- ESC 2015 Pericardial Diseases
- ESC/EACTS 2025 Valvular Heart Disease
- ESC 2025 Myocarditis and Pericarditis (Focused Update)

**Fase 2 — guías adicionales por especialidad:**

- **Neurología**: Manual Cefaleas SEN 2026; AHA/ASA stroke (cita interna)
- **Infecciosas**: PROA Antibióticos FJD 2025; PROA FJD; SEPSIS 2026 (Prescott et al, SSC); Surviving Sepsis 2021 (Evans et al)
- **Neumología**: GEMA 5.5; GOLD 2026
- **Nefrología**: KDIGO 2024 CKD; KDIGO 2012 AKI; UpToDate hiperK ×3
- **Hematología**: UpToDate Anemia of Chronic Disease + Diagnostic Approach to Anemia
- **Endocrinología**: ADA-EASD 2024 (Diabetes Care 47:1257); ADA SoC 2026
- **ORL**: Protocolos ORL Urgencias FJD 2024 (10 PDFs)
- **Urología**: Protocolo HUFJD Hematuria + RAO (2022); PROA FJD 2025
- **Traumatología**: HUFJD Politrauma v0
- **Psiquiatría**: GPC Trastorno Mental Grave + Sustancias; Schuckit NEJM 2014; Haber NEJM 2025
- **Digestivo, Reumatología, Dermatología**: Manual 12 Octubre 2022 (sin PDFs dedicados)

Web (autoritativa, parcial):
- escardio.org · secardiologia.es · ahajournals.org · WebFetch denegado en sandbox para Fase 2 Olas 2-3 (limitación documentada por especialidad)

## Glosario de tags

- `auditoria` · `fact-check` — toda nota de este informe
- `cardio`, `neuro`, `neumo`, etc. — especialidad
- `indice` — solo este archivo INDEX
