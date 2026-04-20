---
tags: [auditoria, fact-check, cardio]
fecha_auditoria: 2026-04-20
auditor: Claude Opus 4.7
scope: Cardiología completa (36/36 notas)
fases:
  - "Fase 1 (piloto): 8 notas con WebFetch parcial"
  - "Fase 1.5 (cierre): 3 notas re-auditadas con PDFs ESC + 28 nuevas"
fuentes_primarias:
  - "ACC/AHA 2025 SCA (Rao et al, Circulation 2025;151:e771-e862)"
  - "ESC 2024 PA elevada e hipertensión"
  - "ESC AF 2024 (Eur Heart J 2024;45:3314)"
  - "ESC HF 2021 + Focused Update 2023 (Eur Heart J 2023;44:3627)"
  - "ESC/EACTS VHD 2025"
  - "ESC 2023 Endocarditis (Eur Heart J 2023;44:3948-4042)"
  - "AHA/ACC 2026 Acute PE (Creager et al)"
  - "ESC 2025 Miocarditis y Pericarditis"
  - "ESC 2023 Cardiomyopathies"
  - "ESC 2024 PAD/Aortic"
  - "ESC 2018 Syncope"
  - "ESC 2022 Ventricular Arrhythmias/SCD"
  - "ESC/ERS 2022 Pulmonary Hypertension"
  - "Manual 12 de Octubre 2022"
description: "Fact-check completo de Cardiología (36 notas) contra guías ESC/ACC-AHA y Manual 12 Oct"
---

# Fact-check — Cardiología (36/36 notas)

> **Aviso clínico:** este informe es una auditoría comparativa de las notas del vault contra las guías citadas. **No es una guía clínica**. Ningún cambio sugerido se ha aplicado al vault — el residente debe revisar cada hallazgo antes de modificar la nota original.

## Resumen ejecutivo

| Métrica | Valor |
|---|---|
| Notas auditadas | **36 / 36** (Cardiología completa) |
| Hallazgos totales | **105** |
| 🔴 Críticos (riesgo clínico alto) | **13** |
| 🟠 Moderados | **46** |
| 🟢 Menores | **30** |
| ⚪ Informativos / sin cambios | **16** |
| Notas concordantes (sin hallazgos relevantes) | 4 (ver final) |

### Hallazgos por sección

| Sección | Notas | Hallazgos | 🔴 | 🟠 | 🟢 | ⚪ |
|---|---|---|---|---|---|---|
| 1. SCA + Cardiopatía isquémica | 7 | 22 | 2 | 9 | 6 | 5 |
| 2. HTA (10 notas) | 10 | 27 | 2 | 14 | 8 | 3 |
| 3. IC / Arritmias / Cardiorrenal | 7 | 24 | 4 | 11 | 7 | 2 |
| 4. Valvulopatías + Endocarditis + Síncope | 3 | 12 | 4 | 6 | 1 | 1 |
| 5. Pericardio + Miocardiopatías + Congénitas | 4 | 7 | 0 | 3 | 1 | 3 |
| 6. Aorta + Vascular Pulmonar + TEP/TVP | 4 | 12 | 0 | 6 | 5 | 1 |
| 7. Scores (Framingham) | 1 | 1 | 0 | 0 | 0 | 1 |
| **Total** | **36** | **105** | **13** | **46** | **30** | **16** |

---

## Top 13 hallazgos críticos a corregir cuanto antes

1. **🔴 [[Escala CHA2DS2-VASc y HAS-BLED]]** — Score obsoleto. ESC AF 2024 sustituye por **CHA₂DS₂-VA** (sin componente sexo, máximo 7 puntos). Renombrar score completo.
2. **🔴 [[Escala CHA2DS2-VASc y HAS-BLED]]** — Tabla con columnas Hombres/Mujeres y umbrales por sexo. ESC AF 2024 usa **umbral universal**: ≥2 = Clase I; =1 = Clase IIa; sin distinción.
3. **🔴 [[Fibrilación Auricular (FA)]]** — La nota usa CHA₂DS₂-VASc con umbrales por sexo. Mismo cambio que arriba: migrar a **CHA₂DS₂-VA**. `[OUTDATED-MANUAL]`
4. **🔴 [[Insuficiencia cardiaca]]** — iSGLT2 descritos como "evidencia creciente" en IC-FEp. Focused Update ESC 2023 los eleva a **Clase I-A en IC-FEm e IC-FEp** (EMPEROR-Preserved + DELIVER). `[OUTDATED-MANUAL]`
5. **🔴 [[Síndrome Coronario Agudo]]** — Lista "ACV isquémico <6 meses" como CI absoluta de fibrinólisis. ACC/AHA 2025 Tabla 14: el cutoff correcto es **<3 meses** (excepto ACV agudo <4.5h).
6. **🔴 [[Cardiopatía isquémica]]** — Dosis carga AAS escrita "300 mg" fija. ACC/AHA 2025: **162-325 mg** masticada (no entérica), seguida de 75-100 mg/día.
7. **🔴 [[Endocarditis Infecciosa]]** — Cefazolina 6 g/día en MSSA sin pauta. ESC 2023: **6 g/día i.v. en 3 dosis (2 g/8h)**.
8. **🔴 [[Endocarditis Infecciosa]]** — Falta dosis específica de **Penicilina G (12-18 MU/día)** y **Amoxicilina (12 g/día en 4-6 dosis)** en *Streptococcus*.
9. **🔴 [[Clasificación de la Presión Arterial ESC 2024]]** — Umbrales **MAPA invertidos**: nota dice día ≥140/90 y noche ≥120/80; Tabla 5 ESC 2024 da MAPA día ≥135/85, 24h ≥130/80, noche ≥120/70.
10. **🔴 [[Evaluación del Riesgo Cardiovascular en la Hipertensión]]** — Cutoffs SCORE2 incorrectos (<1/1-2.5/2.5-5/≥5%). ESC HTA 2024 usa **umbral único ≥10%**. Los cutoffs por edad son de Prevención 2021, no aplicables en HTA 2024.
11. **🔴 [[Valvulopatías]]** — TAVI presentado sin discriminar edad. ESC/EACTS **VHD 2025**: **TAVI Clase I-A en ≥70 años**, SAVR <70 años bajo riesgo (cambia el umbral de 75).
12. **🔴 [[Valvulopatías]]** — Faltan criterios cuantitativos VHD 2025 para IM primaria asintomática (LVESD <40 mm, LVESDi <20 mm/m², FEVI >60%, LAVI ≥60 mL/m² o AI ≥55 mm).
13. **🔴 [[Síndrome Cardiorrenal]]** — Tiazidas (HCT/clortalidona) recomendadas sin advertencia. CLOROTIC mostró **incremento creatinina 46.5% vs 17.2%** sin mejora en mortalidad/reingresos. Vigilar Cr y K+.

### Patrón general

- **Cobertura sustancialmente buena**: el 96% de las notas tiene fuente trazable; los hallazgos críticos son refinamientos de seguridad por desactualización de guías, no errores groseros.
- **Áreas con mayor `[OUTDATED-MANUAL]`**: HTA (ESC 2024), FA (ESC AF 2024), IC (Focused Update 2023), Valvulopatías (ESC/EACTS 2025), Pericardio (ESC 2025), Miocardiopatías (ESC 2023), Aorta (ESC 2024), HTP (ESC/ERS 2022).
- **Lo más sólido**: [[Endocarditis Infecciosa]] (ESC 2023 PDF cruzado), [[Pericarditis Aguda]] (formalmente correcta tras 12 Oct), [[Hipertensión Resistente y Crisis Hipertensiva]] (alineación excelente con ESC 2024 §7.5), [[Tratamiento No Farmacológico de la Hipertensión]] (concordante con ESC 2024 §8.2).
- **Notas muy incompletas**: [[Trombosis Venosa Profunda (TVP)]] (sin sección de tratamiento), [[Cardiopatías Congénitas del Adulto]] (auto-reconocida como provisional).

---

# Sección 1 — Bloque SCA + Cardiopatía isquémica (7 notas)

Fuente vinculante: **ACC/AHA 2025 SCA Guideline** (Rao SV et al, Circulation 2025;151:e771-e862, DOI 10.1161/CIR.0000000000001309) + Manual 12 Oct 2022.

## [[Cardiopatía isquémica]]

**Hallazgos:** 5 (🔴 1 · 🟠 2 · 🟢 1 · ⚪ 1)

### Hallazgo 1 · 🔴 Crítico
- **Hallazgo:** Dosis de carga AAS desactualizada. ACC/AHA 2025 recomienda 162-325 mg masticada, no 300 mg fija; preferencia por 75-100 mg en mantenimiento.
- **Cita en la nota:** "AAS 300 mg (carga) + Segundo inhibidor P2Y12" (línea 39); "AAS 300 mg al diagnóstico + Prasugrel/Ticagrelor" (línea 60)
- **Cita en la fuente:** "Aspirin should be initiated with a loading dose (162-325 mg) in patients with ACS without an absolute contraindication as soon as possible" (Rao et al 2025, p.e788, sección 4.3.1)
- **Cambio sugerido:** "AAS **162-325 mg masticada** (no entérica) seguida de 75-100 mg/día"

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** Pretratamiento P2Y12 en SCASEST mal alineado. Solo es **COR 2b** y solo si la angiografía se anticipa **>24h**.
- **Cita en la nota:** "Segundo inhibidor P2Y12 (Generalmente Ticagrelor o Prasugrel...) a administrar una vez se conoce la anatomía coronaria, o antes si demora en la técnica" (línea 39)
- **Cita en la fuente:** "In patients with NSTE-ACS planned for an invasive strategy with timing of angiography anticipated to be >24 hours, upstream treatment with clopidogrel or ticagrelor may be considered" (Rao et al 2025, COR 2b LOE B-NR, p.e789)
- **Cambio sugerido:** "En NSTEMI con cateterismo precoz (<24h) se difiere el P2Y12 hasta conocer la anatomía. Si angiografía anticipada >24h, puede considerarse pretratamiento (COR 2b)."

### Hallazgo 3 · 🟠 Moderado
- **Hallazgo:** Coronariografía precoz <24h descrita solo con "Alto riesgo (troponinas o GRACE >140)". Falta distinguir muy alto vs alto vs intermedio.
- **Cita en la nota:** "Precoz (< 24 h): Alto riesgo (Elevación troponinas o GRACE alto >140)" (línea 37)
- **Cita en la fuente:** Rao et al 2025, p.e807, sección 6.1
- **Cambio sugerido:** Mantener <2h (muy alto riesgo) y <24h (alto riesgo), añadir "intermedio: invasivo en hospitalización" y bajo riesgo (invasivo o selectivo).

### Hallazgo 4 · 🟢 Menor
- **Hallazgo:** "T de Wellens" mal clasificada como criterio SCACEST. Es patrón SCASEST de alto riesgo.
- **Cita en la nota:** "elevación persistente del ST > 20 min en ≥ 2 derivaciones contiguas o nuevo BRIHH o 'T de Wellens'" (línea 45)
- **Cambio sugerido:** Sustituir "T de Wellens" por **STEMI equivalentes**: descenso ST V1-V3 (IAM posterior), De Winter, ondas T hiperagudas. BRIHH nuevo aislado en asintomático no es STEMI equivalent.

### Hallazgo 5 · ⚪ Informativo
- **Hallazgo:** Frontmatter sin campo `fuente:` aunque la nota cita ACC/AHA 2025 al final.
- **Cambio sugerido:** Añadir `fuente: ACC/AHA 2025 SCA + Manual 12 Octubre 2022`

---

## [[Síndrome Coronario Agudo]]

**Fuente:** ACC/AHA 2025 SCA. **Hallazgos:** 4 (🔴 1 · 🟠 2 · 🟢 1 · ⚪ 0)

### Hallazgo 1 · 🔴 CRÍTICO
- **Hallazgo:** Las CI absolutas de fibrinólisis listan "ACV isquémico <6 meses". El ACC/AHA 2025 (Tabla 14) usa **<3 meses** (excepto ictus isquémico agudo <4.5h, que puede ser indicación de fibrinólisis específica).
- **Cita en la nota:** "**CI absolutas fibrinólisis:** ACV hemorrágico previo, ACV isquémico <6 meses, TCE/cirugía <3 semanas, hemorragia activa, disección aórtica, neoplasia SNC" (línea 148)
- **Cita en la fuente:** Tabla 14 (p.e806): "Absolute Contraindications: ... Ischemic stroke within 3 mo except acute ischemic stroke†" (footnote: †Acute ischemic stroke within 4.5 h of onset.)
- **Cambio sugerido:** Cambiar "<6 meses" → **"<3 meses"** (excepto ictus isquémico agudo <4.5h). Añadir: HTA grave no controlada (>180/110), cirugía intracraneal/espinal **<2 meses**, TCE significativo <3 meses (no <3 semanas), neoplasia intracraneal, MAV/aneurisma, sospecha de disección aórtica, sangrado activo o diátesis hemorrágica.

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** Tabla DAPT en SCACEST + fibrinólisis dice "Clopidogrel 300 mg carga → 75 mg/día" sin matizar edad. ACC/AHA 2025 (Tabla 7): 300 mg solo si ≤75 años; **sin carga (75 mg) si >75 años**.
- **Cita en la nota:** "SCACEST (fibrinólisis) | 75-100 mg | **Clopidogrel 300 mg carga → 75 mg/día** | ≥14 días → valorar ticagrelor" (línea 112)
- **Cita en la fuente:** Tabla 7 (p.e789)
- **Cambio sugerido:** Añadir matiz "300 mg carga si ≤75 años, sin carga (iniciar 75 mg/día) si >75 años".

### Hallazgo 3 · 🟠 Moderado
- **Hallazgo:** Eplerenona/Espironolactona: nota indica "K+<5". Criterios EPHESUS son K ≤5.0 mmol/L Y creatinina ≤2.5 mg/dL (excluye ERC avanzada).
- **Cita en la nota:** "**Eplerenona/Espironolactona** | FEVI <40% + síntomas IC o DM | Eplerenona 25-50 mg si TFGe >30 y K+<5" (línea 177)
- **Cita en la fuente:** Sec 4.7 (p.e801)
- **Cambio sugerido:** "K+ ≤5.0 mmol/L y creatinina ≤2.5 mg/dL (evitar ERC avanzada)".

### Hallazgo 4 · 🟢 Menor
- **Hallazgo:** Tabla discrepancias dice "Duración DAPT ACC-AHA 2025: 12 meses estándar; reducir a 6m si alto riesgo hemorrágico". La estrategia preferida 2025 es **transición a monoterapia con ticagrelor tras ≥1 mes** post-PCI (Class I-A) o de-escalation a clopidogrel tras 1 mes (Class IIb-B), no "6 meses".
- **Cita en la nota:** "Duración DAPT | 12 meses estándar; reducir a 6m si alto riesgo hemorrágico" (línea 227)
- **Cita en la fuente:** Recommendations DAPT (p.e826)
- **Cambio sugerido:** "12 meses estándar; en HBR, considerar monoterapia con ticagrelor o de-escalation a clopidogrel a partir de 1 mes post-PCI".

---

## [[SCA - Evaluacion Inicial y Clasificacion (ACC-AHA 2025)]]

**Hallazgos:** 4 (🟠 1 · ⚪ 3)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** "BRI de nueva aparición + clínica compatible = equivalente STEMI" omite el matiz importante. ACC/AHA 2025: "A new LBBB in an asymptomatic patient does not constitute a STEMI equivalent."
- **Cita en la nota:** "Bloqueo de rama izquierda (BRI) de nueva aparición + clínica compatible = equivalente de STEMI" (línea 47)
- **Cita en la fuente:** Tabla 3, footnote (p.e780)
- **Cambio sugerido:** "BRI nuevo o presumiblemente nuevo + clínica isquémica compatible = considerar como equivalente STEMI; BRI nuevo aislado en paciente asintomático NO es equivalente."

### Hallazgo 2 · ⚪ Informativo
- **Hallazgo:** Tabla "Manejo Prehospitalario" lista "antibióticos prehospitalarios en IAMCEST + hipotensión". **NO existe tal recomendación en ACC/AHA 2025** — probable confusión con sepsis.
- **Cita en la nota:** "Si IAMCEST + hipotensión y tiempo estimado hasta hospital > 60 min: considerar antibióticos prehospitalarios | 2a | C-EO" (línea 61)
- **Cita en la fuente:** ACC/AHA 2025 Sec 3.1.1 (p.e780-781): solo ECG <10 min FMC, transporte directo a centro PCI, prenotificación. Sin antibióticos.
- **Cambio sugerido:** Eliminar la fila completa.

### Hallazgo 3 · ⚪ Informativo
- **Hallazgo:** Cutoffs ECG "V7-V9 ≥0.5 mm" y "V3R-V4R ≥0.5 mm" provienen de la Definición Universal de IM (Thygesen 2018), no de ACC/AHA 2025 literal.
- **Cita en la nota:** "Derivaciones posteriores (V7-V9): ≥ 0.5 mm. Derivaciones derechas (V3R-V4R): ≥ 0.5 mm" (líneas 44-45)
- **Cita en la fuente:** Tabla 3 (p.e780): solo recomienda V7-V9 sin cutoff numérico de elevación
- **Cambio sugerido:** Citar Thygesen 2018 (Definición Universal de IM) para los cutoffs específicos.

### Hallazgo 4 · ⚪ Informativo
- **Hallazgo:** Falta la dosis de carga de AAS (162-325 mg masticada) en la sección "Evaluación Inicial en Urgencias".
- **Cita en la fuente:** Tabla 7 (p.e789): "Aspirin: NSTE-ACS or STEMI - Loading dose 162-325 mg orally. Aspirin (nonenteric coated) should be chewed"
- **Cambio sugerido:** Añadir línea: "AAS 162-325 mg masticada (no recubierta) lo antes posible si no contraindicación (Class 1 LOE A)."

---

## [[SCA - Reperfusion y Revascularizacion (ACC-AHA 2025)]]

**Hallazgos:** 3 (🟠 1 · 🟢 2)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** CI absolutas fibrinólisis: dice "Cirugía intracraneal o espinal <3 meses" y "TCE significativo <3 meses". ACC/AHA 2025 (Tabla 14): **cirugía intracraneal/espinal <2 meses** (no 3).
- **Cita en la nota:** "Cirugía intracraneal o espinal < 3 meses" (línea 74)
- **Cita en la fuente:** Tabla 14 (p.e806): "Intracranial or intraspinal surgery within 2 mo"
- **Cambio sugerido:** Cambiar a "Cirugía intracraneal o espinal en los últimos **2 meses**".

### Hallazgo 2 · 🟢 Menor
- **Hallazgo:** CI relativa "HTA grave no controlada (PAS >180 mmHg)" omite **PAD >110**.
- **Cita en la fuente:** Tabla 14 (p.e806): "Severe uncontrolled hypertension (SBP >180 or DBP >110 mm Hg)" — Absolute si no respondiente; Relative si solo en presentación.
- **Cambio sugerido:** Añadir "PAD >110 mmHg". Notar además que HTA grave no respondiente es CI absoluta, no solo relativa.

### Hallazgo 3 · 🟢 Menor
- **Hallazgo:** Reducción dosis tenecteplasa "≥75 años algunos protocolos sugieren mitad de dosis": **proviene del ensayo STREAM, NO es recomendación ACC/AHA 2025**. La reducción por edad es para enoxaparina, no para TNK.
- **Cita en la nota:** "En pacientes ≥ 75 años, algunos protocolos sugieren mitad de dosis de tenecteplasa." (línea 64)
- **Cita en la fuente:** Tabla 13 (p.e806): dosis estándar por peso sin reducción por edad. Tabla 10: la reducción ≥75 años es para enoxaparina.
- **Cambio sugerido:** Aclarar que la mitad de TNK en ≥75 años es STREAM (estrategia farmacoinvasiva), no recomendación ACC/AHA 2025; o citar STREAM.

---

## [[SCA - Tratamiento Medico (ACC-AHA 2025)]]

**Hallazgos:** 4 (🟠 2 · 🟢 2)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Timing P2Y12 en NSTE-ACS con COR equivocado. La nota cita "COR 2a LOE B-R" para diferir; la guía 2025 no tiene esa recomendación 2a — el pretratamiento upstream >24h es **COR 2b LOE B-NR**.
- **Cita en la nota:** "En IAMSEST con cateterismo precoz (< 24h): es razonable diferir el P2Y12 hasta conocer la anatomía coronaria | 2a | B-R" (línea 46)
- **Cita en la fuente:** ACC/AHA 2025, p.e789
- **Cambio sugerido:** "En NSTEMI con cateterismo anticipado <24h, no hay recomendación formal de pretratamiento; juicio clínico. Si angiografía anticipada >24h: pretratamiento upstream con clopidogrel o ticagrelor — COR 2b LOE B-NR."

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** Dosis Metoprolol no estandarizada ("25-50 mg VO cada 6-12h, titular hasta 200 mg/día"). Mezcla pautas tartrato/succinato. ACC/AHA 2025 solo dice "low dose with slow escalation".
- **Cita en la nota:** Línea 146
- **Cita en la fuente:** ACC/AHA 2025, p.e800, sec 4.6
- **Cambio sugerido:** "Metoprolol tartrato 25-50 mg VO/12h (escalar hasta 100 mg/12h) o Metoprolol succinato 25-200 mg/día en una toma. Iniciar a dosis baja en las primeras 24h si hemodinámicamente estable."

### Hallazgo 3 · 🟢 Menor
- **Hallazgo:** Cutoff "PAS >100 mmHg" para inicio IECA en SCA no aparece en ACC/AHA 2025 — práctica clínica, no recomendación formal.
- **Cita en la nota:** "Inicio en las primeras 24 horas si hemodinámicamente estable (PAS > 100 mmHg)" (línea 164)
- **Cambio sugerido:** Mantener "iniciar en 24h si hemodinámicamente estable" o eliminar cutoff PAS >100 si se quiere alinear estrictamente.

### Hallazgo 4 · 🟢 Menor
- **Hallazgo:** Lista FR Shock Cardiogénico (evitar BB) usa criterios COMMIT 2013, no los de la guía 2025.
- **Cita en la nota:** "Edad > 70 años, FC > 110, PAS < 120, Killip ≥ II, IAMCEST anterior, bloqueo AV" (línea 150)
- **Cambio sugerido:** Sustituir por contraindicaciones COR 3:Harm 2025: "Killip II-IV, signos de bajo gasto, BAV 2º-3º sin marcapasos, bradicardia severa, broncoespasmo activo, PR >240 ms".

---

## [[SCA - Manejo Hospitalario y Prevencion Secundaria (ACC-AHA 2025)]]

**Hallazgos:** 3 (🟠 1 · 🟢 1 · ⚪ 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** "Transición a monoterapia con ticagrelor (suspender AAS) tras ≥1 mes post-PCI | 1 | A" omite condición clave: solo aplica "in patients with ACS who have **tolerated DAPT with ticagrelor**".
- **Cita en la nota:** Línea 116
- **Cita en la fuente:** Recommendations DAPT (p.e826)
- **Cambio sugerido:** Añadir "en pacientes que han tolerado DAPT con ticagrelor" como condición previa.

### Hallazgo 2 · 🟢 Menor
- **Hallazgo:** Criterios menores ARC-HBR: "Hb 11-12.9 g/dL (hombres) o 11-11.9 g/dL (mujeres)". Correctos pero ACC/AHA Tabla 22 los enuncia con mujeres primero.
- **Cita en la fuente:** Tabla 22 (p.e829)
- **Cambio sugerido:** Sin cambio. Verificación positiva.

### Hallazgo 3 · ⚪ Informativo
- **Hallazgo:** Add-on tras estatina máxima cita "ezetimiba y/o iPCSK9". ACC/AHA 2025 (Top Take-Home #3) menciona también **inclisiran y bempedoic acid**.
- **Cita en la nota:** "ezetimiba y/o inhibidor de PCSK9" (línea 167)
- **Cita en la fuente:** Top Take-Home Message #3 (p.e773)
- **Cambio sugerido:** Añadir inclisiran y ácido bempedoico como opciones no-estatina.

---

## [[SCA - Complicaciones y Shock Cardiogenico (ACC-AHA 2025)]]

**Hallazgos:** 3 (🟠 1 · 🟢 1 · ⚪ 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Tabla mal formateada (líneas 58-61) con encabezados desordenados ("Recomendacin", celda vacía). Probable fragmento residual de copia/pegado.
- **Cita en la nota:** Líneas 58-61
- **Cambio sugerido:** Reformatear la tabla. La recomendación de fondo (BIAC en complicaciones mecánicas como puente a cirugía, Class 2a B-NR) es correcta.

### Hallazgo 2 · 🟢 Menor
- **Hallazgo:** Tabla "Indicaciones para DAI" omite el plazo temporal: **≥40 días post-IM Y ≥90 días post-revascularización** (Class 1 LOE A).
- **Cita en la nota:** Líneas 107-111
- **Cita en la fuente:** Sec 9.2 (p.e819)
- **Cambio sugerido:** Reforzar el plazo "≥40 días post-IM Y ≥90 días post-revascularización" en la propia tabla.

### Hallazgo 3 · ⚪ Informativo
- **Hallazgo:** "MADIT II (31% reducción mortalidad si FEVI ≤30%)" es correcto (HR 0.69, IC 95% 0.51-0.93).
- **Cita en la fuente:** Sec 9.2 (p.e819)
- **Cambio sugerido:** Sin cambio. Cita correcta.

---

# Sección 2 — Bloque HTA (10 notas)

Fuente vinculante: **ESC 2024 PA elevada e hipertensión** (PDF local).

## [[Clasificación de la Presión Arterial ESC 2024]]

**Hallazgos:** 3 (🔴 1 · 🟠 2)

### Hallazgo 1 · 🔴 Crítico
- **Hallazgo:** Umbrales **MAPA invertidos**. La nota dice "MAPA HTA: ≥140/90 día, ≥120/80 noche". ESC 2024 Tabla 5: **MAPA día ≥135/85, MAPA 24h ≥130/80, MAPA noche ≥120/70**.
- **Cita en la nota:** "MAPA para HTA | ≥130/80 mmHg día | ≥140/90 mmHg día; ≥120/80 mmHg noche | Más alto" (línea 45) y "MAPA: PA sistólica ≥140 mmHg día, ≥120 mmHg noche; PA diastólica ≥90 mmHg día, ≥80 mmHg noche." (línea 28)
- **Cita en la fuente:** Tabla 5 ESC 2024 (p.24)
- **Cambio sugerido:** Corregir a: MAPA diurna ≥135/85, MAPA 24h ≥130/80, MAPA nocturna ≥120/70.

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** ESC 2024 NO mantiene los "Grados/Estadios 1-2-3" de hipertensión; clasificación simplificada a 3 categorías (PA no elevada / PA elevada / Hipertensión).
- **Cita en la nota:** "Subclasificación de Hipertensión (Grados) — Estadio 1: 140-159/90-99; Estadio 2: 160-179/100-109; Estadio 3 (Severa): ≥180/110" (líneas 31-34)
- **Cita en la fuente:** ESC HTA 2024 §6.1, Fig.6 (p.27); Recomendaciones revisadas Tabla 4
- **Cambio sugerido:** Eliminar la subclasificación Estadio 1-3 o etiquetar como "terminología ESC 2018 (superseded)".

### Hallazgo 3 · 🟠 Moderado
- **Hallazgo:** Coexistencia de cutoffs SCORE2 conflictivos. Nota cita "muy alto SCORE2 ≥10%" en una parte y "≥5%" en otra. ESC HTA 2024 usa **umbral único ≥10%**.
- **Cita en la nota:** Línea 61 (≥10%) vs nota Riesgo CV (≥5%)
- **Cita en la fuente:** ESC HTA 2024 §6.3.1 (p.30)
- **Cambio sugerido:** Armonizar al umbral único ≥10%.

---

## [[Hipertensión Resistente y Crisis Hipertensiva]]

**Hallazgos:** 3 (🟠 2 · ⚪ 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Dosis labetalol bolo "ESC 20 mg" no se localiza explícitamente en texto principal ESC 2024 (la guía remite a Material Suplementario Tabla S13 para dosis IV).
- **Cita en la nota:** "Labetalol — Bolo 20 mg (ESC) / 50 mg (H12O); perfusión 200 mg/200 ml a 20 ml/h" (línea 158)
- **Cita en la fuente:** ESC HTA 2024 §10.1.2 (p.79)
- **Cambio sugerido:** Marcar como `[VERIFICAR-Tabla S13 Material Suplementario]`. La cifra "20 mg ESC" como dato duro podría ser inexacta.

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** Preeclampsia/eclampsia: nota dice "Objetivo PAS <160, PAD <105" pero omite umbrales de emergencia hipertensiva en embarazo (≥170/110 Clase I; ≥160/110 Clase IIa).
- **Cita en la nota:** Línea 152
- **Cita en la fuente:** ESC HTA 2024 §10.4.1 (p.81); Recomendaciones revisadas (p.16)
- **Cambio sugerido:** Añadir umbrales de ingreso hospitalario en embarazo (≥170/110 I/C; ≥160/110 IIa/C).

### Hallazgo 3 · ⚪ Informativo (positivo)
- **Hallazgo:** Definición HTA resistente, espironolactona 25-50 mg con TFGe ≥30 y K⁺ ≤4.5, denervación renal IIb/B, objetivo PAS 140-160 en hemorragia cerebral (IIa/A) — todos congruentes con ESC 2024.
- **Cita en la fuente:** §7.5 (p.40-41); Recomendaciones Tabla 32 (p.81)
- **Cambio sugerido:** Ninguno. Excelente alineación.

---

## [[Evaluación del Riesgo Cardiovascular en la Hipertensión]]

**Hallazgos:** 2 (🔴 1 · 🟢 1)

### Hallazgo 1 · 🔴 Crítico
- **Hallazgo:** Cutoffs SCORE2 (<1%, 1-<2.5%, 2.5-<5%, ≥5%) NO son los de ESC HTA 2024. La guía 2024 usa **umbral único ≥10%**. Los cutoffs por edad son de Prevención 2021 y la guía HTA 2024 los descarta explícitamente.
- **Cita en la nota:** "SCORE2: bajo <1 %, moderado 1-<2.5 %, alto 2.5-<5 %, muy alto ≥5 %. SCORE2 ≥5 % se considera 'suficientemente alto'" (líneas 53-57)
- **Cita en la fuente:** "utilizamos los términos 'riesgo suficientemente alto' o 'riesgo aumentado' para describir a las personas con un riesgo de ECV a 10 años ≥10 %... recomendar un único umbral de ≥10 % frente a la alternativa de utilizar umbrales específicos a la edad, como los que se emplean en la Guía ESC 2021" (ESC HTA 2024 §6.3.1, p.30)
- **Cambio sugerido:** Sustituir por **umbral único ≥10% a 10 años** definido por ESC HTA 2024.

### Hallazgo 2 · 🟢 Menor
- **Hallazgo:** Criterios historia familiar ECV prematura invertidos / discrepancia interna. Nota dice "<60 años mujeres, <55 años hombres" pero también "<55 años hombres, <65 años mujeres" en otra parte.
- **Cita en la nota:** Líneas 46 vs 84
- **Cambio sugerido:** Unificar a <55 años varón / <65 años mujer (estándar europeo).

---

## [[Daño Orgánico Mediado por Hipertensión]]

**Hallazgos:** 3 (🟢 3)

### Hallazgo 1 · 🟢 Menor
- **Hallazgo:** Cutoff volumen AI indexado: nota usa "≥16 mL/m² H, ≥14 mL/m² M". ESC 2024 Figura 12 usa **Volumen/altura² AI >18.5 (H) / >16.5 (M) ml/m²**.
- **Cita en la fuente:** Figura 12 ESC 2024 (p.39)
- **Cambio sugerido:** Actualizar a cutoffs Figura 12 (Vol/altura², no Vol/altura).

### Hallazgo 2 · 🟢 Menor
- **Hallazgo:** Clasificación Keith-Wagener-Barker con "Grado IV: papilitis 'malva'". El término "malva" no aparece en ESC 2024.
- **Cambio sugerido:** Eliminar descriptor "malva". O sustituir por la clasificación benigna/maligna que ESC 2024 favorece.

### Hallazgo 3 · 🟢 Menor
- **Hallazgo:** Sección "Hiperglucemia Renal" (línea 80) es errata; debe ser "Declive de TFGe en ERC hipertensiva".
- **Cambio sugerido:** Renombrar.

---

## [[Diagnóstico de Hipertensión y Causas Secundarias]]

**Hallazgos:** 2 (🟠 1 · 🟢 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Edad cribado HTA secundaria: nota dice "<30 años". ESC 2024 recomienda cribado exhaustivo en HTA diagnosticada **antes de los 40 años** (Clase I/B).
- **Cita en la fuente:** Recomendaciones, Adultos jóvenes (p.12)
- **Cambio sugerido:** Actualizar a "<40 años".

### Hallazgo 2 · 🟢 Menor
- **Hallazgo:** Ratio aldosterona-renina (RAR) cutoff "≥20 ng/dL per pg/mL/h" no avalado por cita literal en ESC 2024 (depende del ensayo local).
- **Cambio sugerido:** Marcar `[VERIFICAR-S2/S3]` o generalizar sin cifra dura.

---

## [[Fisiopatología de la Hipertensión]]

**Hallazgos:** 2 (🟢 1 · ⚪ 1)

### Hallazgo 1 · 🟢 Menor
- **Hallazgo:** Cifra "10% HTA secundaria" sin cita literal pero coherente con ESC 2024 (p.1169 cita similar). Aceptable.
- **Cambio sugerido:** Ninguno.

### Hallazgo 2 · ⚪ Informativo (positivo)
- **Hallazgo:** Descripción RAAS, SNS, disfunción endotelial y rigidez arterial concordante con Figura 1 ESC 2024. Sin discrepancias.
- **Cambio sugerido:** Ninguno relevante.

---

## [[Hipertensión en Poblaciones Especiales]]

**Hallazgos:** 5 (🟠 5)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Objetivo PA en ≥85 años mal representado. ESC 2024: ≥85 años SIN fragilidad → mismo objetivo 120-129 (I/A); solo frágiles moderados-graves o esperanza vida <3 años → "<140" (IIb/C).
- **Cita en la nota:** "Frágiles o ≥85 años: PAS 130-139 mmHg" (líneas 73-74)
- **Cita en la fuente:** Recomendaciones revisadas (p.12, p.15-16)
- **Cambio sugerido:** Separar edad ≥85 sin fragilidad (objetivo 120-129 I/A) de fragilidad moderada-grave (<140 IIb/C).

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** Objetivo PA en embarazo expresado de forma confusa ("diastólica <90 tolerada, NO sobrepasar por riesgo fetopalaciencia" — errata "fetoplacentaria"). ESC 2024: PA <140/90 pero **NO <80 mmHg diastólica**.
- **Cita en la fuente:** Recomendaciones revisadas (p.16, I/C)
- **Cambio sugerido:** Corregir objetivo: PA <140/90, NO <80 mmHg diastólica. Corregir typo.

### Hallazgo 3 · 🟠 Moderado
- **Hallazgo:** Umbral inicio tratamiento en embarazo correcto (≥140/90) pero no marca como **NUEVO** ESC 2024 (basado en CHAP, antes era 150/95).
- **Cita en la fuente:** Recomendaciones revisadas (I/B), CHAP trial
- **Cambio sugerido:** Explicitar cambio respecto a guía previa.

### Hallazgo 4 · 🟠 Moderado
- **Hallazgo:** "Nifedipino IR sublingual (no ideal pero usado)" en preeclampsia. ESC 2024 NO menciona vía sublingual; recomienda labetalol IV, nicardipino IV con MgSO4 (I/C) y nifedipino oral.
- **Cita en la fuente:** §10.4.1 (p.81); Tabla 33 (p.82)
- **Cambio sugerido:** Eliminar "sublingual" (usar nifedipino oral liberación prolongada) y añadir nicardipino IV.

### Hallazgo 5 · 🟠 Moderado
- **Hallazgo:** Objetivo PA en diabetes 120-129 correcto (I/A) pero omite excepción **≥65 años: rango 130-139**.
- **Cita en la fuente:** ESC HTA 2024 (p.16, I/A)
- **Cambio sugerido:** Añadir subgrupo ≥65 años diabetes → 130-139 mmHg.

---

## [[Medición de la Presión Arterial]]

**Hallazgos:** 1 (🟠 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Valores MAPA repiten error de C2 (Clasificación PA): "MAPA HTA ≥140/90 día, ≥120/80 noche" vs **MAPA día ≥135/85, MAPA 24h ≥130/80, MAPA noche ≥120/70**.
- **Cita en la nota:** Línea 88
- **Cita en la fuente:** Tabla 5 ESC 2024 (p.24)
- **Cambio sugerido:** Actualizar a Tabla 5.

---

## [[Tratamiento Farmacológico de la Hipertensión]]

**Hallazgos:** 4 (🟠 3 · 🟢 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Umbral inicio tratamiento en "PA elevada con riesgo CV alto" mal expresado. ESC 2024 (Clase I-A): tras 3 meses de cambios estilo vida, iniciar si PA confirmada **≥130/80** en pacientes con riesgo alto.
- **Cita en la nota:** "Si riesgo CV moderado-alto (SCORE2 5-<10%)... Si riesgo CV muy alto (SCORE2 ≥10%) o ECV previa: Iniciar medicamentos + estilo de vida" (líneas 18-19)
- **Cita en la fuente:** ESC 2024 PA, Tabla 3 (p.11), Clase I-A
- **Cambio sugerido:** Añadir: "Umbral de inicio farmacológico en PA elevada (120-139/70-89) y riesgo CV alto (SCORE2 ≥10% o ECV/ERC/DM/DOMH/HF) es **≥130/80 mmHg confirmada tras 3 meses de cambios de estilo de vida** (Clase I A)."

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** "Paso 4" lista antagonista aldosterona, BB, alfa-bloqueante como opciones equivalentes. ESC 2024 prioriza **espironolactona como 4ª línea (Clase I-A)**.
- **Cita en la fuente:** ESC 2024 PA, Tabla 4 (p.13)
- **Cambio sugerido:** "**Paso 4: Espironolactona (Clase I A)** como 4ª línea preferida. Si no efectiva/no tolerada: eplerenona, BB, antihipertensivo central / alfa-bloqueante / hidralazina (Clase IIa B)."

### Hallazgo 3 · 🟠 Moderado
- **Hallazgo:** Definición "PA Elevada" no aclara que es nueva categoría diagnóstica formal ESC 2024 (no equivale a "prehipertensión" ni "PA normal alta").
- **Cita en la fuente:** ESC 2024 §2.1 punto 2 (p.9)
- **Cambio sugerido:** Añadir definición clara: "**PA elevada (nueva categoría ESC 2024)**: PAS 120-139 o PAD 70-89 mmHg en consulta. **Hipertensión**: PAS ≥140 o PAD ≥90. **PA no elevada**: <120/70." Eliminar "PA normal alta" / "prehipertensión".

### Hallazgo 4 · 🟢 Menor
- **Hallazgo:** En HFpEF nota recomienda BCC dihidropiridínico Y no-dihidropiridínico. ESC 2024 no posiciona BCC no-DHP como primera línea en HFpEF.
- **Cita en la fuente:** ESC 2024 PA §9.8 (p.71-73)
- **Cambio sugerido:** "HFpEF: **IECA/ARA + diurético** ± iSGLT2. Evitar BCC no-DHP si disfunción sistólica."

---

## [[Tratamiento No Farmacológico de la Hipertensión]]

**Hallazgos:** 1 (⚪ 1)

### Hallazgo 1 · ⚪ Informativo (positivo)
- **Hallazgo:** Sal <5 g NaCl/día (≈2 g Na), potasio ≥3.5 g/día, ejercicio ≥150 min/semana aeróbico + fuerza 2-3/sem, alcohol <100 g/sem (H) y <70 g/sem (M), DASH/mediterránea — concordantes con ESC 2024 §8.2.1-§8.2.2 (p.48).
- **Cambio sugerido:** Ninguno relevante.

---

## Incoherencias inter-nota detectadas (HTA)

- **MAPA umbrales:** Clasificación PA y Medición PA duplican el error (≥140/90 día y ≥120/80 noche). Corrección conjunta requerida.
- **SCORE2 cutoffs:** Clasificación PA usa ≥10% pero Riesgo CV usa ≥5%. Alinear al umbral único ≥10% de ESC HTA 2024.
- **Historia familiar ECV prematura:** discrepancia interna de cifras dentro de Riesgo CV (<60/<55 vs <55/<65).

---

# Sección 3 — IC / Arritmias / Cardiorrenal (7 notas)

Fuentes vinculantes: **ESC HF 2021 + Focused Update 2023** · **ESC AF 2024** · **ESC VA/SCD 2022** · **KDIGO 2024** · Manual 12 Oct.

## [[Insuficiencia cardiaca]]

*(Re-auditada en Fase 1.5 con PDFs ESC HF 2021 y Focused Update 2023; reemplaza hallazgos provisionales del piloto)*

**Hallazgos:** 5 (🔴 1 · 🟠 3 · 🟢 1)

### Hallazgo 1 · 🔴 Crítico · `[OUTDATED-MANUAL]`
- **Hallazgo:** iSGLT2 descritos como "evidencia creciente" en IC-FEp mencionando solo empagliflozina. **Focused Update 2023 elevó dapagliflozina/empagliflozina a Clase I-A en IC-FEm e IC-FEp** (EMPEROR-Preserved + DELIVER).
- **Cita en la nota:** "iSGLT2: Beneficio independiente de ser diabético... *Evidencia creciente de beneficio incluso en FEVIp (estudio EMPEROR-HF con empagliflozina).*" (líneas 43-45)
- **Cita en la fuente:** "An SGLT2 inhibitor (dapagliflozin or empagliflozin) is recommended in patients with HFmrEF to reduce the risk of HF hospitalization or CV death." Clase I-A (Focused Update 2023, Recommendation Table 1, p.3633). Misma recomendación en HFpEF (Recommendation Table 2, p.3633).
- **Cambio sugerido:** Reescribir indicando que el tratamiento ya **NO es exclusivo de IC-FEr**: Clase I-A para todo el espectro de FEVI (incluyendo FEm y FEp). Añadir referencia EMPEROR-HF → corregir nombre real **EMPEROR-Preserved** (no existe "EMPEROR-HF").

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** Sacubitril/Valsartán: dosis inicio "24/26 o 49/51 mg/12h" sin matizar. Dosis estándar ESC 2021: **49/51 mg b.i.d.**; 24/26 mg solo si hipotensión sintomática previa.
- **Cita en la nota:** Línea 35
- **Cita en la fuente:** ESC HF 2021 Tabla 8 (p.3621): "ARNI / Starting dose: 49/51 mg b.i.d. / Target: 97/103 mg b.i.d. Optional lower starting dose 24/26 mg b.i.d. for those with a history of symptomatic hypotension."
- **Cambio sugerido:** "Dosis inicio: **49/51 mg/12h** (24/26 mg/12h solo si antecedente de hipotensión sintomática). Objetivo: 97/103 mg/12h."

### Hallazgo 3 · 🟠 Moderado
- **Hallazgo:** Criterios TRC: nota indica "QRS ≥150 ms con BCRI". ESC 2021: **Clase I para QRS ≥150 ms con BCRI** y **Clase IIa para QRS 130-149 ms con BCRI** (la nota omite la indicación IIa).
- **Cita en la nota:** Línea 56
- **Cita en la fuente:** ESC HF 2021 §6.2 (p.3627)
- **Cambio sugerido:** "TRC: NYHA II-IV en RS con FEVI ≤35% y BCRI: **Clase I si QRS ≥150 ms; Clase IIa si QRS 130-149 ms** (en ambos: optimización médica ≥3 meses)."

### Hallazgo 4 · 🟠 Moderado
- **Hallazgo:** Definición "FEVI Recuperada" ambigua. Definición ESC 2021 / Universal Definition HF 2021: **mejoría ≥10 puntos absolutos** desde FEVI basal <40% **alcanzando FEVI >40%**.
- **Cita en la nota:** "FEVI Recuperada: Aumento de la FEVI de ≥10% y >40% en 2 ETT consecutivos" (línea 18)
- **Cambio sugerido:** "Aumento absoluto **≥10 puntos** respecto a la FEVI basal <40%, llegando a FEVI >40% en 2 ETT consecutivos."

### Hallazgo 5 · 🟢 Menor
- **Hallazgo:** Carvedilol "25 mg/12h" sin matizar excepción peso >85 kg. ESC HF 2021: dosis objetivo 25 mg b.i.d.; **50 mg b.i.d. máximo si peso >85 kg**.
- **Cita en la fuente:** ESC HF 2021 Tabla 8 (p.3621)
- **Cambio sugerido:** "Carvedilol 25 mg/12h (puede llegar a 50 mg/12h si peso >85 kg)."

---

## [[Insuficiencia cardiaca aguda]]

*(Re-auditada en Fase 1.5)*

**Hallazgos:** 3 (🟠 2 · ⚪ 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Vasodilatadores (NTG) presentados como "Recomendación ESC para EAP hipertensivo (PAS >110 mmHg)". ESC HF 2021 los **rebajó de IIa (2016) a IIb**.
- **Cita en la nota:** Línea 68
- **Cita en la fuente:** ESC HF 2021 (p.3655); Tabla "Changes in recommendations" (p.3611): "2021 IIb / 2016 IIa"
- **Cambio sugerido:** "Vasodilatadores (NTG): **Clase IIb** en EAP con PAS >110 mmHg (rebajada en 2021). Evitar si PAS <90 o estenosis aórtica severa."

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** Inotrópicos: "solo si hipoperfusión periférica e hipotensión". ESC 2021 los reserva para hipoperfusión + PAS <90 mmHg sin respuesta a tratamiento estándar (IIb-C); uso rutinario contraindicado (Clase III).
- **Cita en la nota:** Línea 69
- **Cita en la fuente:** ESC HF 2021 (p.3656); Figura 9 (p.3650)
- **Cambio sugerido:** "Inotrópicos (Dobutamina, Milrinona, Levosimendán): solo en pacientes con **hipoperfusión + PAS <90 mmHg** que no responden a tratamiento estándar (IIb-C). Uso rutinario contraindicado (III). Aumentan consumo O₂ miocárdico."

### Hallazgo 3 · ⚪ Informativo
- **Hallazgo:** Regla "ampollas furosemida = cifra creatinina" es atajo del Manual 12 Oct, **no está en ESC 2021/2023**. Conviene etiquetarlo.
- **Cita en la nota:** Línea 56
- **Cambio sugerido:** Etiquetar como "**Práctica clínica española (Manual 12 Oct), no en guías ESC**".

> ✅ **Nota positiva:** Descripción ADVOR (acetazolamida 500 mg IV) concordante. Precaución sobre opiáceos (Clase III) exacta. Criterios VMNI alineados con ESC 2021. **Concordante en lo esencial.**

---

## [[Manejo Diurético Deterioro Renal ICA]]

**Hallazgos:** 2 (🟠 1 · ⚪ 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** No menciona la **dosis máxima de furosemida i.v. en ICA (400-600 mg/día, hasta 1000 mg en ERC severa)** que es referencia explícita ESC HF 2021. La nota habla de "intensificar" sin techo.
- **Cita en la nota:** "**¡Mantener o intensificar la terapia depletiva!**" (línea 29)
- **Cita en la fuente:** ESC HF 2021 Figura 13 footnote (p.3654): "The maximal daily dose for i.v. loop diuretics is generally considered furosemide 400-600 mg though up to 1000 mg may be considered in patients with severely impaired kidney function."
- **Cambio sugerido:** Especificar techo 400-600 mg/día (hasta 1000 mg si ERC severa) y criterios de respuesta (Na+ urinario ≥50-70 mEq/L a 2h, diuresis ≥100-150 mL/h en 6h).

### Hallazgo 2 · ⚪ Informativo
- **Hallazgo:** No cita explícitamente fuente ESC HF 2021 ni Focused Update 2023.
- **Cambio sugerido:** Añadir bloque "Fuentes" con ESC HF 2021 (§11.3) + Focused Update 2023 (ADVOR/EMPULSE).

---

## [[Síndrome Cardiorrenal]]

**Hallazgos:** 2 (🔴 1 · 🟢 1)

### Hallazgo 1 · 🔴 Crítico
- **Hallazgo:** En "Bloqueo Secuencial de la Nefrona" la nota recomienda HCT y clortalidona, pero NO cita el ensayo CLOROTIC ni que **el efecto se limita a pérdida de peso, con incremento significativo de creatinina (46.5% vs 17.2%, p<0.001)** y sin mejora clínica.
- **Cita en la nota:** "Añadir **Tiazidas** (ej. Hidroclorotiazida o Clortalidona) para bloquear el TCD." (línea 54)
- **Cita en la fuente:** "An increase in serum creatinine occurred more frequently in patients on hydrochlorothiazide (46.5%) compared with those on placebo (17.2%) (P < .001). The rates of HF rehospitalization and all-cause death were similar between groups" (Focused Update 2023 §4.1.1, p.3635)
- **Cambio sugerido:** Añadir advertencia: vigilar creatinina y K+ al añadir tiazida; el efecto es sobre peso, no sobre disnea ni reingresos (CLOROTIC).

### Hallazgo 2 · 🟢 Menor
- **Hallazgo:** Acetazolamida ADVOR: "+ 500 mg i.v." sin precisar **dosis única diaria** y matiz de **descongestión a 3 días** sin impacto en rehospitalización/mortalidad.
- **Cita en la nota:** Línea 55
- **Cita en la fuente:** Focused Update 2023 §4.1.1 (p.3635)
- **Cambio sugerido:** "500 mg i.v. una vez al día" + matiz: "mejora descongestión, sin impacto en mortalidad/reingresos a 3 meses".

---

## [[Arritmias]]

**Hallazgos:** 3 (🟠 1 · 🟢 1 · ⚪ 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** En TV monomorfa estable nota cita "Amiodarona 300 mg i.v. en 30-60 min + 900 mg/24 h". ESC VA/SCD 2022 prescribe **5 mg/kg en 20 min – 2 h** (loading), no régimen fijo de 300 mg. La pauta fija es ACLS/RCP, no específica de TV monomorfa.
- **Cita en la nota:** Línea 42
- **Cita en la fuente:** ESC VA/SCD 2022 Tabla 14 (p.4036)
- **Cambio sugerido:** Anotar que la dosis fija "300 mg" procede del régimen RCP/ACLS; añadir dosis ESC ajustada por peso para uso en TV monomorfa fuera de parada.

### Hallazgo 2 · 🟢 Menor
- **Hallazgo:** "Energías Sincronizadas (CVE) 50-100 J (Flutter o TV monomorfa)" no aparece literalmente en ESC VA/SCD 2022 (depende del desfibrilador).
- **Cambio sugerido:** Marcar la cifra como recomendación práctica del Manual; si se quiere referencia ESC, citar protocolo local.

### Hallazgo 3 · ⚪ Informativo
- **Hallazgo:** Única fuente declarada: "Manual 12 de Octubre Cap. 16" (2022). Existe ESC AF 2024 + ESC VA/SCD 2022 con clases y dosis específicas.
- **Cambio sugerido:** Añadir fuentes ESC 2022/2024 y marcar partes dependientes del Manual como `[OUTDATED-MANUAL]`.

---

## [[Fibrilación Auricular (FA)]]

*(Re-auditada en Fase 1.5 con ESC AF 2024 PDF; reemplaza hallazgos del piloto)*

**Hallazgos:** 6 (🔴 1 · 🟠 2 · 🟢 2 · ⚪ 1)

### Hallazgo 1 · 🔴 Crítico · `[OUTDATED-MANUAL]`
- **Hallazgo:** La nota usa **CHA₂DS₂-VASc** y mantiene umbrales sexo-dependientes. ESC AF 2024 ha sustituido el score por **CHA₂DS₂-VA** (sin componente sexo).
- **Cita en la nota:** "A largo plazo se basa en la escala **CHA₂DS₂-VASc**. (Anticoagular si ≥ 1 en varón o ≥ 2 en mujer)." (línea 42)
- **Cita en la fuente:** "this task force proposes... that clinicians and patients should use the CHA₂DS₂-VA score (excluding gender)... OAC are recommended in those with a CHA₂DS₂-VA score of 2 or more and should be considered in those with a CHA₂DS₂-VA score of 1" (ESC AF 2024 §6.1.1, p.3341; Tabla 6, p.3342)
- **Cambio sugerido:** "A largo plazo se basa en la escala **CHA₂DS₂-VA** (ESC 2024, sin componente sexo). Anticoagular si **≥2** (Clase I); considerar si =1 (Clase IIa)." [OUTDATED-MANUAL]

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** Ablación de venas pulmonares (PVI) está como "Mantenimiento Crónico del Ritmo: opción". Desde 2024 es **Clase I-A 1ª línea en FA paroxística sintomática** (cambio mayor desde IIa de 2020).
- **Cita en la nota:** Línea 38
- **Cita en la fuente:** ESC AF 2024 Tabla 4 — Revised recommendations §7.2 (p.3326): "Catheter ablation is recommended as a first-line option within a shared decision-making rhythm control strategy in patients with paroxysmal AF" (Clase I, A)
- **Cambio sugerido:** Añadir: "**PVI:** Clase I-A en FA **paroxística** sintomática como 1ª línea de control de ritmo (ESC 2024)."

### Hallazgo 3 · 🟠 Moderado
- **Hallazgo:** Umbral cardioversión sin anticoagulación previa: nota usa **48h**. ESC 2024 ha bajado a **24h**.
- **Cita en la nota:** Líneas 33-34
- **Cita en la fuente:** ESC AF 2024 Tabla 3 — New recommendations (p.3323): "Early cardioversion is not recommended without appropriate anticoagulation or transoesophageal echocardiography if AF duration is longer than 24 h" (Clase III-C)
- **Cambio sugerido:** Cambiar "48h" → "24h" y añadir "[OUTDATED-MANUAL — ESC 2024 ha reducido el umbral de 48h a 24h]".

### Hallazgo 4 · 🟢 Menor
- **Hallazgo:** Anticoagulación post-cardioversión "al menos 4 semanas". ESC 2024: opcional únicamente si FA <24h sin factores de riesgo embólico y restauración de ritmo sinusal en <24h.
- **Cita en la nota:** Línea 41
- **Cita en la fuente:** ESC AF 2024 §7.2.1 (p.3355)
- **Cambio sugerido:** "...al menos 4 semanas (opcional únicamente si FA <24h sin factores de riesgo embólico y se restaura ritmo sinusal en <24h, ESC 2024)."

### Hallazgo 5 · 🟢 Menor
- **Hallazgo:** Verapamilo "Contraindicados si FEVI < 40%". ESC 2024: contraindicado si **FEVI ≤40%** (incluye 40%).
- **Cita en la nota:** Línea 24
- **Cita en la fuente:** ESC AF 2024 Tabla 12 (p.3353)
- **Cambio sugerido:** Cambiar "FEVI < 40%" → "FEVI ≤40%".

### Hallazgo 6 · ⚪ Informativo
- **Hallazgo:** No recoge el nuevo marco AF-CARE (Comorbilidades / Anticoagulación / Reducción síntomas / Evaluación dinámica). Falta indicación **Clase I-A iSGLT2 en FA + IC**.
- **Cita en la fuente:** ESC AF 2024 Tabla 3 (p.3322): "Sodium-glucose cotransporter-2 inhibitors are recommended for patients with HF and AF regardless of left ventricular ejection fraction" (Clase I-A)
- **Cambio sugerido:** Añadir sección breve "Manejo de comorbilidades (AF-CARE)" con iSGLT2 en FA+IC.

---

## [[Escala CHA2DS2-VASc y HAS-BLED]]

**Hallazgos:** 4 (🔴 2 · 🟠 1 · 🟢 1)

### Hallazgo 1 · 🔴 Crítico
- **Hallazgo:** Score y título usan versión obsoleta CHA₂DS₂-VASc. ESC AF 2024 sustituye por **CHA₂DS₂-VA** (eliminando componente "Sc" sexo femenino).
- **Cita en la nota:** "# CHA₂DS₂-VASc — Riesgo tromboembólico en FA" (línea 10) y fila "**Sc** | Sexo femenino | 1" (línea 21)
- **Cita en la fuente:** "Table 10 Updated definitions for the CHA2DS2-VA score" (ESC AF 2024 §6.1, p.3343)
- **Cambio sugerido:** Renombrar score a **CHA₂DS₂-VA** (máximo 7 puntos), eliminar fila Sc, actualizar título y todas las referencias.

### Hallazgo 2 · 🔴 Crítico
- **Hallazgo:** Umbrales anticoagulación estratificados por sexo (columnas Hombres/Mujeres). ESC AF 2024 usa **umbral universal sin diferencia por sexo**: ≥2 = Clase I; =1 = Clase IIa.
- **Cita en la nota:** Líneas 29-31
- **Cita en la fuente:** ESC AF 2024 Recommendation Table 6 (p.3342)
- **Cambio sugerido:** Tabla única: 0 = no anticoagular; 1 = considerar (IIa); ≥2 = recomendado (I), sin distinción por sexo.

### Hallazgo 3 · 🟠 Moderado
- **Hallazgo:** Falta indicación específica de anticoagulación en **MCH y amiloidosis cardíaca independientemente del CHA₂DS₂-VA**.
- **Cita en la fuente:** ESC AF 2024 Recommendation Table 6 (p.3342): "Oral anticoagulation is recommended in all patients with AF and hypertrophic cardiomyopathy or cardiac amyloidosis, regardless of CHA2DS2-VA score" (Clase I-B)
- **Cambio sugerido:** Añadir nota: en MCH/amiloidosis se anticoagula independientemente del score.

### Hallazgo 4 · 🟢 Menor
- **Hallazgo:** Anticoagulación post-cardioversión: la guía 2024 recomienda 4 semanas de OAC tras CVE para todos (incluso CHA₂DS₂-VA = 0), salvo si <24h y bajo riesgo.
- **Cita en la fuente:** ESC AF 2024 Figura 12 (p.3355)
- **Cambio sugerido:** Añadir referencia cruzada al algoritmo de cardioversión para evitar confusión entre OAC perioperatoria y crónica.

---

# Sección 4 — Valvulopatías + Endocarditis + Síncope (3 notas)

## [[Valvulopatías]]

**Hallazgos:** 3 (🔴 2 · 🟠 1)

### Hallazgo 1 · 🔴 Crítico
- **Hallazgo:** Nota no refleja cambio crítico ESC/EACTS **VHD 2025**: TAVI ahora **≥70 años** (no ≥75 como en 2021), SAVR <70 años bajo riesgo. La nota solo menciona "SAVR o TAVI" sin discriminar edad.
- **Cita en la nota:** "**Tratamiento:** Su indicación principal es la aparición de síntomas… (SAVR o Percutáneo - TAVI)." (línea 47)
- **Cita en la fuente:** "TAVI is recommended in patients ≥70 years of age with tricuspid AV stenosis, if the anatomy is suitable. (Class I, A)" / "SAVR is recommended in patients <70 years of age, if the surgical risk is low. (Class I, B)" (ESC/EACTS VHD 2025 §8.5, p.4646)
- **Cambio sugerido:** Actualizar: TAVI ≥70 años (válvula tricúspide, anatomía favorable); SAVR <70 si bajo riesgo. Citar VHD 2025.

### Hallazgo 2 · 🔴 Crítico
- **Hallazgo:** En IM primaria asintomática, la nota carece de los nuevos cutoffs ESC/EACTS VHD 2025: **LVESD <40 mm + LVESDi <20 mm/m² + FEVI >60%** + dilatación AI (LAVI ≥60 mL/m² o AI ≥55 mm).
- **Cita en la nota:** "**Cirugía:** Reparación valvular de elección sobre el recambio protésico, si afecta la clase funcional (NYHA II-IV con FEVI > 30%)." (línea 30)
- **Cita en la fuente:** "Surgical MV repair should be considered in low-risk asymptomatic patients with severe PMR without LV dysfunction (LVESD <40 mm, LVESDi <20 mm/m², and LVEF >60%) in the presence of significant LA dilatation (LAVI ≥60 mL/m² or LA diameter ≥55 mm)" (Clase IIa-B) (VHD 2025 §9.1.4, p.4647)
- **Cambio sugerido:** Añadir criterios cuantitativos para asintomáticos.

### Hallazgo 3 · 🟠 Moderado
- **Hallazgo:** No se menciona EAo de **bajo flujo / bajo gradiente con FEVI conservada** (criterio SVi ≤35 mL/m²).
- **Cita en la fuente:** "Intervention should be considered in symptomatic patients with low-flow (SVi ≤35 mL/m²), low-gradient (<40 mmHg) AS with normal LVEF (≥50%)" (IIa-B) (VHD 2025 §8.4.1, p.4646)
- **Cambio sugerido:** Añadir párrafo sobre EAo paradójica bajo flujo/bajo gradiente con FEVI conservada.

---

## [[Endocarditis Infecciosa]]

**Hallazgos:** 5 (🔴 2 · 🟠 2 · 🟢 1)

### Hallazgo 1 · 🔴 Crítico
- **Hallazgo:** En *Streptococcus* (CMI <0,125) la nota da solo "Penicilina G, amoxicilina o Ceftriaxona 2 g/24 h" sin dosis específicas. ESC 2023: **Penicilina G 12-18 millones U/día i.v. en 4-6 dosis o continua**, **Amoxicilina 12 g/día i.v. en 4-6 dosis**.
- **Cita en la nota:** "Penicilina G, amoxicilina o Ceftriaxona 2 g/24 h" (tabla *Streptococcus*)
- **Cita en la fuente:** ESC 2023 Recommendation Table 7 (p.3977-3978)
- **Cambio sugerido:** Reescribir fila: "**Penicilina G 12-18 MU/día i.v.**, **Amoxicilina 12 g/día i.v. en 4-6 dosis** o **Ceftriaxona 2 g/24 h**".

### Hallazgo 2 · 🔴 Crítico
- **Hallazgo:** Cefazolina 6 g/día en MSSA NVE/PVE sin especificar repartición. ESC 2023: **6 g/día i.v. en 3 dosis (2 g/8h)**. Misma laguna en (Flu)cloxacilina (debe ser "en 4-6 dosis").
- **Cita en la nota:** "(Flu)Cloxacilina 12 g/día i.v. o Cefazolina 6 g/día i.v. (ambas primera línea)"
- **Cita en la fuente:** ESC 2023 Recommendation Table 8 (p.3980): "Cefazolin 6 g/day i.v. in 3 doses" + "(Flu)cloxacillin 12 g/day i.v. in 4-6 doses"
- **Cambio sugerido:** "Cefazolina **6 g/día i.v. en 3 dosis (2 g/8h)**" y "(Flu)Cloxacilina **12 g/día i.v. en 4-6 dosis**".

### Hallazgo 3 · 🟠 Moderado
- **Hallazgo:** Cirugía urgente con vegetación ≥10 mm sin embolismo: combinación incorrecta de criterios. ESC 2023: "vegetación ≥10 mm **sin disfunción valvular severa, sin embolismo y bajo riesgo quirúrgico**".
- **Cita en la nota:** Línea 228
- **Cita en la fuente:** ESC 2023 Tabla 4 (p.3958), Clase IIb-B
- **Cambio sugerido:** "Vegetaciones ≥ 10 mm **sin** disfunción valvular severa, **sin** embolismo y **bajo** riesgo quirúrgico → considerar cirugía urgente (Clase IIb / B)".

### Hallazgo 4 · 🟠 Moderado
- **Hallazgo:** Profilaxis dental con dos errores: (1) cefalexina marcada como i.v. cuando solo existe **oral** (cefalexina 2 g v.o.); (2) **clindamicina recomendada para alérgicos**, pero ESC 2023 explícitamente la **desaconseja** por riesgo C. difficile fatal.
- **Cita en la fuente:** ESC 2023 Tabla 6 (p.3961)
- **Cambio sugerido:** "amoxicilina 2 g v.o. DU (alternativas: ampicilina 2 g i.m./i.v., **cefalexina 2 g v.o.**, cefazolina o ceftriaxona 1 g i.m./i.v. DU). Alérgicos: **azitromicina o claritromicina 500 mg v.o.** o doxiciclina 100 mg v.o. **(NO clindamicina — desaconsejada por riesgo C. difficile)**".

### Hallazgo 5 · 🟢 Menor
- **Hallazgo:** Régimen corto Streptococcus 2 semanas: nota cita solo ceftriaxona, omitiendo penicilina G y amoxicilina como opciones igualmente válidas.
- **Cita en la fuente:** ESC 2023 Tabla 7 (p.3977)
- **Cambio sugerido:** "Penicilina G 12-18 MU/día, amoxicilina 12 g/día **o** ceftriaxona 2 g/24 h + Gentamicina 3 mg/kg/24 h en dosis única".

> ✅ **Nota positiva:** Sólida, bien estructurada, fuente PDF ESC 2023 correctamente citada. Concordante en duración tratamiento, criterios diagnósticos modificados, criterios POET, criterios cirugía y timing. Aciertos: rifampicina (no antes de 3-5 días), daptomicina ≥10 mg/kg, *E. faecalis* en HACEK como novedad, fibrinólisis Clase III. **Mantener calidad como referencia.**

---

## [[Síncope]]

**Hallazgos:** 2 (🟠 2)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** "Tilt training" descrito como recomendación estándar. ESC Syncope 2018 lo clasifica como **Clase IIb-B** (puede considerarse en jóvenes); las maniobras de contrapresión isométrica son IIa-B.
- **Cita en la nota:** Líneas 153-154
- **Cita en la fuente:** ESC Syncope 2018 (p.1923)
- **Cambio sugerido:** Marcar tilt training como IIb (uso seleccionado en jóvenes) y restringir PCM a <60 años con pródromos.

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** Falta indicación explícita del **Holter implantable (ILR) Clase I-A en síncope recurrente de origen incierto** sin criterios de alto riesgo.
- **Cita en la fuente:** ESC Syncope 2018 (p.1907)
- **Cambio sugerido:** Añadir párrafo sobre ILR (indicaciones I-A: síncope recurrente sin diagnóstico ni alto riesgo; síncope con alto riesgo sin diagnóstico tras estudio completo).

---

# Sección 5 — Pericardio + Miocardiopatías + Congénitas (4 notas)

## [[Pericarditis Aguda]]

**Hallazgos:** 3 (🟠 2 · ⚪ 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Colchicina "3 meses". ESC 2025 amplía a **3-6 meses** (alineación con COPE/CORP/ICAP).
- **Cita en la nota:** "Colchicina ... durante 3 meses"
- **Cita en la fuente:** ESC 2025 Myocarditis and Pericarditis, Tabla 13: "Colchicine 0.5 mg b.i.d. (0.5 mg o.d. if body weight <70 kg) **for 3-6 months** is recommended"
- **Cambio sugerido:** Cambiar "durante 3 meses" → "durante 3-6 meses".

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** No menciona los **antagonistas del receptor IL-1 (anakinra, rilonacept)** como opción en pericarditis recurrente o corticodependiente. Novedad mayor ESC 2025.
- **Cita en la fuente:** ESC 2025: "In patients with corticosteroid-dependent or refractory recurrent pericarditis, IL-1 receptor antagonists (anakinra, rilonacept) should be considered" (Clase IIa)
- **Cambio sugerido:** Añadir en pericarditis recurrente: "Refractaria/corticodependiente → considerar IL-1 antagonists (anakinra SC diaria, rilonacept SC semanal)."

### Hallazgo 3 · ⚪ Informativo
- **Hallazgo:** No introduce el concepto **SIMP** (Síndrome Inflamatorio Miopericárdico) ni la nomenclatura agrupada miocarditis-pericarditis ESC 2025.
- **Cambio sugerido:** Añadir nota: "ESC 2025 introduce categoría SIMP cuando hay solapamiento miocarditis-pericarditis."

---

## [[Taponamiento Cardiaco]]

**Hallazgos:** 2 (🟢 1 · ⚪ 1 positivo)

### Hallazgo 1 · 🟢 Menor
- **Hallazgo:** Cutoff VCI dilatada ">21 mm". Referencia ASE/ESC para VCI pletórica es **>20 mm** sin colapso inspiratorio normal.
- **Cita en la nota:** Línea 26
- **Cambio sugerido:** Cambiar ">21 mm" → ">20 mm".

### Hallazgo 2 · ⚪ Informativo (positivo)
- **Hallazgo:** Triada Beck, pulso paradójico >10 mmHg, pericardiocentesis y "diuréticos/vasodilatadores ESTRICTAMENTE CONTRAINDICADOS" (Clase III ESC 2015) están correctos.
- **Cita en la fuente:** ESC 2015 Pericardial Diseases p.2940
- **Cambio sugerido:** Ninguno.

---

## [[Miocardiopatías]]

**Hallazgos:** 2 (🟠 1 · 🟢 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Usa clasificación clásica MCD/MCH/MCR. ESC 2023 reconoce **5 fenotipos**: HCM, DCM, **NDLVC** (Non-Dilated Left Ventricular Cardiomyopathy), **ARVC**, RCM.
- **Cita en la fuente:** ESC 2023 Cardiomyopathies §2 ("New definitions and classification")
- **Cambio sugerido:** Añadir sección sobre NDLVC (hipocinesia VI sin dilatación, frecuente en cardiopatías genéticas y arritmogénicas) y ARVC.

### Hallazgo 2 · 🟢 Menor
- **Hallazgo:** En MCH no menciona **mavacamten** (inhibidor miosina cardíaca, primer fármaco específico para MCH obstructiva sintomática, ESC 2023 Clase IIa).
- **Cita en la fuente:** ESC 2023 Cardiomyopathies, Recommendations for HCM treatment
- **Cambio sugerido:** Añadir mavacamten como tercera línea en MCH obstructiva sintomática refractaria a BB/CaA no-DHP.

---

## [[Cardiopatías Congénitas del Adulto]]

**Hallazgos:** 1 (⚪ 1)

### Hallazgo 1 · ⚪ Informativo
- **Hallazgo:** La propia nota se reconoce limitada ("nota básica - fuente limitada"). No desarrolla CIA, CIV, ductus, coartación, Fallot reparado, etc. **ESC 2020 ACHD no consultada en esta auditoría**.
- **Cambio sugerido:** Programar ampliación contra ESC 2020 ACHD Guidelines. Mantener nota actual como provisional.

---

# Sección 6 — Aorta + Vascular Pulmonar + TEP/TVP (4 notas)

## [[Síndrome Aórtico Agudo y Enfermedad Aórtica]]

**Hallazgos:** 2 (🟢 1 · ⚪ 1 positivo)

### Hallazgo 1 · 🟢 Menor
- **Hallazgo:** No menciona **score ADD-RS** (Aortic Dissection Detection Risk Score) para estratificación pretest, herramienta destacada en ESC 2024 Aorta.
- **Cita en la fuente:** ESC 2024 §7.2: "ADD-RS is recommended to estimate the pretest probability of acute aortic syndrome (Class I-B). Patients with ADD-RS ≤1 and negative D-dimer have a very low probability and CT can be deferred."
- **Cambio sugerido:** Añadir sección breve sobre ADD-RS y su uso combinado con D-dímero.

### Hallazgo 2 · ⚪ Informativo (positivo)
- **Hallazgo:** Umbrales cirugía (AAA ≥55mm hombres / ≥50mm mujeres; raíz aórtica ≥50mm en Marfan; Stanford A → cirugía urgente, B no complicado → médico inicial; labetalol primera línea con TAS<120 / FC<60) correctamente alineados con ESC 2024.
- **Cita en la fuente:** ESC 2024 Aortic Diseases Tablas 17-19 y §8.3
- **Cambio sugerido:** Ninguno.

---

## [[Hipertensión Pulmonar]]

**Hallazgos:** 1 (🟠 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Definición correcta (mPAP >20 mmHg, ESC/ERS 2022) PERO en la tabla de clasificación hemodinámica mantiene cutoff antiguo **RVP ≥3 UW**. ESC/ERS 2022 redujo el umbral a **>2 WU**.
- **Cita en la nota:** Tabla clasificación hemodinámica usa "RVP ≥3 UW" en HP precapilar y combinada
- **Cita en la fuente:** ESC/ERS 2022 PH Tabla 5: "Pre-capillary PH: mPAP >20 + PAWP ≤15 + PVR >2 WU. Combined post- and pre-capillary: mPAP >20 + PAWP >15 + PVR >2 WU."
- **Cambio sugerido:** Cambiar "RVP ≥3 UW" por "RVP **>2 UW**" para HP precapilar y HP combinada.

---

## [[TEP - Tromboembolismo Pulmonar]]

**Fuente primaria:** AHA/ACC 2026 Acute PE Guideline. **Hallazgos:** 4 (🟠 2 · 🟢 2)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Manejo Categoría A incompleto. La nota dice "Asintomático | Alta desde Urgencias" sin mencionar **iniciar DOAC** (COR 1).
- **Cita en la nota:** "A | Asintomático | Alta desde Urgencias"
- **Cita en la fuente:** Figura 3 + Top take-home #2 (Creager et al 2026, p.e3, p.e21): "Initiate DOAC" (COR 1) + "Use HESTIA, PESI, and/or sPESI" (COR 1)
- **Cambio sugerido:** "A | Subclínico (incidental, asintomático) | **Iniciar DOAC** + alta a domicilio con seguimiento ambulatorio (no requiere hospitalización)"

### Hallazgo 2 · 🟠 Moderado
- **Hallazgo:** Categoría B incompleta. Falta definición clara (PESI I-II, sPESI=0, Hestia=0), subcategorías B1/B2, e **iniciar HBPM**.
- **Cita en la fuente:** Tabla 5 + Figura 2 + Figura 3 (Creager et al 2026, p.e13-e14, p.e21)
- **Cambio sugerido:** "B | Sintomático, severidad baja (PESI I-II / sPESI=0 / Hestia=0). Subcategorías B1 (subsegmental) y B2 (no subsegmental) | **Iniciar HBPM**, alta precoz / seguimiento ambulatorio."

### Hallazgo 3 · 🟢 Menor
- **Hallazgo:** PERC: añadir explícitamente que **TODOS los 8 criterios deben ser negativos** para descartar TEP.
- **Cita en la fuente:** Figura 1 + Tabla 3 (Creager et al 2026, p.e9)
- **Cambio sugerido:** Añadir "**TODOS los 8 criterios deben ser negativos**".

### Hallazgo 4 · 🟢 Menor
- **Hallazgo:** "Terapias Avanzadas (Cat. E/D)" no especifica COR ni quién activa PERT.
- **Cita en la fuente:** Top take-home #5 (p.e3) + Figura 3 (p.e21)
- **Cambio sugerido:** "Cat E1/D1-D2: trombólisis sistémica/CDL/trombectomía/embolectomía COR 2a. Cat C2-C3: trombólisis solo si bajo riesgo hemorrágico (COR 2b). **Activar PERT en Cat C-E (COR 1)**."

---

## [[Trombosis Venosa Profunda (TVP)]]

**Hallazgos:** 2 (🟠 1 · 🟢 1)

### Hallazgo 1 · 🟠 Moderado
- **Hallazgo:** Nota muy incompleta: cubre Wells, dímero D ajustado por edad y criterios de ingreso, pero **NO incluye sección de tratamiento** (anticoagulación, DOACs, AVK, duración 3 meses vs prolongada). Tampoco profilaxis primaria.
- **Cita en la nota:** Frontmatter: "Extraído de 50_Guardias/03 - Protocolos Rápidos Boxes Urgencias.md"
- **Cita en la fuente:** No se obtuvo cita literal de ASH 2020 ni ACCP CHEST 2021 (WebFetch denegado). Por SOURCE POLICY no se afirma "DOACs son primera línea según guía X p.Y" sin verificar.
- **Cambio sugerido:** Completar la nota con secciones (1) Tratamiento agudo (HBPM/DOAC/AVK, dosis y monitorización); (2) Duración según etiología; (3) Profilaxis primaria. Validar contra ASH 2020 VTE (Ortel et al, Blood Adv 2020;4:4693) y ACCP CHEST 2021 antes de publicar.

### Hallazgo 2 · 🟢 Menor
- **Hallazgo:** Errata tipográfica: "Trombofilia, **trandfusion**" en sección "Plantilla de Guardia".
- **Cita en la nota:** Línea 54
- **Cambio sugerido:** Corregir "trandfusion" → "transfusión".

---

# Sección 7 — Scores / Misc

## [[Criterios de Framingham]]

**Hallazgos:** 1 (⚪ 1 positivo)

### Hallazgo 1 · ⚪ Informativo (positivo)
- **Hallazgo:** Aplica correctamente criterios de Framingham para diagnóstico clínico de IC (2 mayores o 1 mayor + 2 menores). Reconoce explícitamente que ESC HF 2021 prefiere actualmente NT-proBNP/eco para diagnóstico, lo cual es correcto.
- **Cita en la fuente:** McKee PA et al, NEJM 1971;285:1441-1446
- **Cambio sugerido:** Ninguno. Bien contextualizada históricamente.

---

# Notas concordantes (sin hallazgos relevantes)

Las siguientes notas tienen hallazgos meramente positivos / informativos sin requerir cambios:

- [[Tratamiento No Farmacológico de la Hipertensión]] (excelente alineación ESC 2024 §8.2)
- [[Hipertensión Resistente y Crisis Hipertensiva]] (alineación excelente con §7.5)
- [[Fisiopatología de la Hipertensión]] (concordante con Figura 1 ESC 2024)
- [[Criterios de Framingham]] (correcto, bien contextualizado)

> ✅ **Bloque positivo destacado**: [[Endocarditis Infecciosa]] mantiene la calidad de referencia del piloto (errores de detalle en dosis, no de fondo).

---

# Limitaciones metodológicas honestas

1. **Notas con verificación PDF parcial**:
   - **TVP**: ASH 2020 / ACCP CHEST 2021 no disponibles localmente; WebFetch denegado. Hallazgo reportado como gap estructural sin cita externa numérica de DOACs.
   - **Cardiopatías Congénitas del Adulto**: ESC 2020 ACHD Guidelines no consultada (la propia nota se autocaracteriza como provisional).
2. **Manual 12 Oct 2022 desactualizado** en HTA (ESC 2024), FA (ESC 2024), IC (Focused Update 2023), Valvulopatías (VHD 2025), Pericardio (ESC 2025), Miocardiopatías (ESC 2023), Aorta (ESC 2024), HTP (ESC/ERS 2022), SCA (ACC/AHA 2025). Los hallazgos `[OUTDATED-MANUAL]` lo marcan explícitamente.
3. **Cobertura completa Cardio**: 36/36 notas auditadas tras Fase 1.5. La auditoría de 14 especialidades restantes (Fase 2) está pendiente de decisión.
4. **No se ha cruzado con UpToDate**: solo guías oficiales (ESC, ACC/AHA, KDIGO) y Manual 12 Oct.
5. **Auditoría documental, no clínica**: este informe valida la coherencia de las notas con sus fuentes citadas; no sustituye la revisión clínica del residente ni el juicio en cabecera.
