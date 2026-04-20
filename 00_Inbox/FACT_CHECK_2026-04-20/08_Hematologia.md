---
tags: [auditoria, fact-check, hemato]
fecha_auditoria: 2026-04-20
fuentes_consultadas:
  - "UpToDate – Diagnostic approach to anemia in adults (Means & Brodsky, Nov 2025)"
  - "UpToDate – Anemia of chronic disease/anemia of inflammation (Camaschella & Weiss, Feb 2026)"
  - "Manual de Diagnóstico y Terapéutica Médica – Hospital 12 de Octubre (8.ª ed., 2022). Caps. 81 (Trastornos de la serie roja, pp. 1237-1243, 1249-1251), 84 (Pancitopenia. Hemoterapia, pp. 1277-1289), HLH 1283-1285, Hemorragia digestiva pp. 509, 516"
notas_auditadas: 9
hallazgos_total: "16 (3🔴 · 7🟠 · 4🟢 · 2⚪)"
---

# Fact-check — Hematología

**Alcance:** 9 notas (`Anemia - Abordaje General`, `ACD/AI`, `Ferropénica`, `Hemolítica – Abordaje`, `Macrocítica`, `Microcítica`, `Normocítica`, `Pancitopenia`, `Sdme Hemofagocitico`).

**Fuentes primarias verificadas:**
- UpToDate "Diagnostic approach to anemia in adults" (Means RJ, Brodsky RA. Lit. review Feb 2026; this topic last updated Nov 20, 2025) — leído íntegramente.
- UpToDate "Anemia of chronic disease/anemia of inflammation" (Camaschella C, Weiss G. Lit. review Feb 2026; topic last updated Feb 06, 2026) — leído íntegramente.
- Manual 12 Octubre 2022 caps. 81 y 84 — leídos.

---

## Resumen ejecutivo

| Nota | 🔴 | 🟠 | 🟢 | ⚪ |
|---|---|---|---|---|
| Anemia - Abordaje General | 0 | 0 | 1 | 0 |
| ACD/AI | 0 | 1 | 0 | 0 |
| Anemia Ferropénica | 1 | 3 | 1 | 0 |
| Anemia Hemolítica | 0 | 0 | 0 | 0 |
| Anemia Macrocítica | 0 | 0 | 1 | 0 |
| Anemia Microcítica | 0 | 1 | 0 | 0 |
| Anemia Normocítica | 0 | 0 | 0 | 0 |
| Pancitopenia | 0 | 0 | 1 | 0 |
| Sdme Hemofagocitico | **2** | 2 | 0 | 2 |
| **Total** | **3** | **7** | **4** | **2** |

El bloque de Hematología está globalmente **bien anclado a UpToDate** (las dos notas más extensas — abordaje general y ACD — son fieles a la fuente citada). Los hallazgos críticos se concentran en (1) la **nota de HLH**, que está literalmente vacía a pesar de ser una urgencia hematológica con criterios cuantitativos exactos; y (2) algunos cutoffs y dosis del manejo de **anemia ferropénica** que no se corresponden con la fuente citada.

---

## 1. `Sdme Hemofagocitico.md`

### 🔴 [CRÍTICO] La nota está vacía: solo dice "Calcular SCORE HEMOFAGOCITICO"

**Hallazgo:** El cuerpo de la nota es una sola línea ("Calcular SCORE HEMOFAGOCITICO"). No hay criterios diagnósticos, ni umbrales analíticos, ni esquema terapéutico. Los enlaces desde `Pancitopenia.md` y `Anemia Hemolítica - Abordaje.md` apuntan a esta nota como "ver para criterios HLH-2004 / dexametasona + etopósido" — pero la nota no contiene esa información.

**Por qué es crítico:** HLH es una urgencia hematológica con mortalidad ≈40% (Manual 12 Oct, p. 1285: *"La mortalidad global alcanza el 41%"*) en la que el inicio empírico no debe demorarse por el estudio genético.

**Cita de fuente — Manual 12 Oct 2022, cap. 84, p. 1284, Tabla 5 ("Criterios diagnósticos de linfohistiocitosis hemofagocítica de la Sociedad del Histiocito (2004)"):**
> "A. Diagnóstico molecular de mutaciones patogénicas (PRF1, UNC13D, Munc18-2, RAB27A, STX11, SH2D1A o BIRC4) **o**
> B. **5 de los siguientes criterios**:
> – Fiebre **≥ 38,5 °C**
> – Esplenomegalia
> – Citopenias: **hemoglobina < 9 g/dl, plaquetas < 100.000/µl y neutrófilos < 1.000/µl**
> – Hipertrigliceridemia (en ayuno, **> 265 mg/dl**) o hipofibrinogenemia (**< 150 mg/dl**)
> – Hemofagocitosis en médula ósea, bazo, ganglios linfáticos o hígado
> – Disminución o ausencia de actividad de linfocitos NK
> – Ferritina **> 500 ng/ml**
> – CD25 soluble elevado **≥ 2.400 U/ml**"

> Nota: el PDF transcribe "plaquetas < 10.000/µl" pero en el contexto y según la versión publicada en Pediatr Blood Cancer 2007 (Henter et al., HLH-2004) el umbral es **< 100 × 10⁹/L (100.000/µl)**. Recomiendo verificar con la publicación original.

**Acción:** reescribir la nota con: criterios HLH-2004 (5/8), H-Score (Manual 12 Oct, p. 1284, Tabla 6: ferritinemia 2000-6000 +35 / >6000 +50; H-Score >169 → S 93%, E 86%), pista clínica de la sospecha (fiebre alta persistente + hepatoesplenomegalia + ferritina >10.000 + hipertrigliceridemia + hipofibrinogenemia, p. 1284), tratamiento.

---

### 🔴 [CRÍTICO] Falta esquema terapéutico HLH-94/2004

**Cita — Manual 12 Oct 2022, cap. 84, p. 1285:**
> *"En pacientes con daño orgánico progresivo o en los que se predice mala evolución hay que iniciar **etopósido (150 mg/m² bisemanal durante las primeras 2 semanas y semanal en las semanas 3-8) y dexametasona diaria (iniciar a 10 mg/m²) durante 8 semanas en dosis decrecientes**, además de medidas de soporte vital y tratamiento del factor desencadenante si se conoce. En caso de síntomas neurológicos se debe asociar metotrexato intratecal e hidrocortisona."*

> *"En caso de >10.000 copias/µg de ADN de VEB, se puede utilizar **rituximab 375 mg/m²/semana durante 1-4 semanas**."*

**Acción:** añadir esquema y umbrales al texto.

---

### 🟠 [MODERADO] Falta el factor desencadenante más frecuente y el umbral de ferritina muy alterada

**Cita — Manual 12 Oct 2022, p. 1283-1284:**
> Tabla 4: VEB = factor precipitante "Más frecuente (>100 casos)" / Linfoma T/NK = neoplasia más frecuente / LES = autoinmune más frecuente.
> *"Es muy sugestiva de HLH la evidencia de hemofagocitosis junto con valores muy alterados de hipofibrinogenemia, hipertrigliceridemia e **hiperferritinemia (> 10.000 mg/ml)**"* (sic, debe leerse > 10.000 ng/ml).

**Cita — UpToDate ACD, sección "Iron studies":**
> *"Ferritin can reach extremely high values (up to 10,000 mcg/L [10,000 ng/mL] and higher) in hemophagocytic lymphohistiocytosis (HLH) or macrophage activation syndrome (MAS) from the combination of severe inflammation and macrophage iron accumulation secondary to hemophagocytosis."*

**Acción:** documentar el umbral diagnóstico de ferritina (≥500 ng/ml para criterio HLH-2004, pero >10.000 = altamente sugestivo) y los desencadenantes principales.

---

### 🟠 [MODERADO] Falta mención al H-Score (calculadora alternativa más práctica en adultos)

**Cita — Manual 12 Oct 2022, p. 1284, Tabla 6 ("H-Score"):**
> "Si score > 169: **sensibilidad 93%, especificidad 86%** para el diagnóstico de linfohistiocitosis hemofagocítica."
> Componentes con peso: inmunosupresión (+18), hepatoesplenomegalia (+38), pancitopenia (+34), ferritina >6000 ng/ml (+50), triglicéridos >350 mg/dl (+64), fibrinógeno <250 (+30), AST >30 U/l (+19), hemofagocitosis MO (+35), Tª >39,4°C (+49).

**Acción:** añadir el H-Score como complemento (la nota dice "Calcular SCORE HEMOFAGOCITICO" — probablemente refiriéndose a esto, pero sin desarrollar nada).

---

### ⚪ [INFORMATIVO] Falta `fuente:` en frontmatter y desarrollo de fisiopatología (NK + T citotóxicos), clínica multiorgánica (UCI 40%, mortalidad 41%) — ver Manual p. 1283-1285.

### ⚪ [INFORMATIVO] El alias está bien (HLH, Síndrome Hemofagocítico) pero la nota debería enlazar a `Pancitopenia` y `Anemia Hemolítica - Abordaje` (de donde ya se enlaza hacia ella).

---

## 2. `Anemia Ferropénica.md`

### 🔴 [CRÍTICO] La pauta "Sulfato ferroso 325 mg/8h" no aparece en las fuentes españolas; los preparados comerciales en España son 525 mg (Fero Gradumet® = 105 mg Fe elemental) o 256 mg (Tardyferon® = 80 mg). Además, existe evidencia de mejor absorción con **dosis alterna**

**Hallazgo en la nota (líneas 76-80, sección Tratamiento oral):**
> "Sulfato ferroso: 325 mg/8 h (contiene 65 mg de hierro elemental por comprimido)."

**Cita — Manual 12 Oct 2022, p. 1242, Tabla 5 ("Preparados comerciales de hierro oral"):**
> Sulfato ferroso → "**Fero Gradumet® comp. 525 mg, 105 mg de hierro elemental, 1 comp/12-24 h**"
> "**Tardyferon® gragea 256 mg, 80 mg de hierro elemental, 1 grágea/12 h**"

**Cita — Manual 12 Oct 2022, p. 1243, "Pauta y tiempo de tratamiento":**
> *"Se recomienda iniciar a dosis de **150-200 mg/día de hierro elemental repartido en varias tomas**. Si solo hay ferropenia sin anemia, se administrarán **30-50 mg/día de hierro elemental**. Se requieren **6-8 semanas para mejorar la cifra de Hb y hasta 6 meses para reponer los depósitos de hierro**."*

**Cita — Manual 12 Oct 2022, p. 1242, "Efectos adversos":**
> *"Estos efectos secundarios son dosis-dependientes y generalmente más frecuentes al inicio del tratamiento. En algunos casos se puede plantear **dar dosis elevadas en días alternos**, administrarlo con comidas (aunque disminuiría su efectividad) o valorar otros preparados, como los férricos liposomados."*

**Acción:**
1. Sustituir "325 mg/8h (65 mg Fe elemental)" por la pauta del Manual: 150-200 mg/día de **hierro elemental**, con preparados comerciales reales en España (Fero Gradumet® 525 mg = 105 mg Fe / Tardyferon® 256 mg = 80 mg Fe).
2. Mencionar la opción de **dosis a días alternos** (avalada por el Manual y por la literatura reciente sobre hepcidina circadiana — UpToDate "Treatment of iron deficiency").
3. Dato adicional crítico ya correcto en la nota: respuesta esperada (reticulocitosis 7-10 días, Hb +2 g/dl en 3 semanas — coincide con Manual p. 1243).

---

### 🟠 [MODERADO] Umbral de ferritina para definir refractariedad mal documentado

**Hallazgo en la nota:** "continuar 3-6 meses tras normalización de Hb para rellenar depósitos (ferritina >50)."

**Cita — Manual 12 Oct 2022, p. 1243, sección 2.6 "Anemia ferropénica refractaria":**
> *"Hay que considerar una anemia ferropénica como refractaria ante la falta de respuesta a sales ferrosas a dosis de **al menos 100 mg/día de hierro elemental durante 4-8 semanas**, manteniéndose la ferritina sérica **por debajo de 15 µg/l**."*

**Acción:** clarificar que el objetivo de ferritina al final del tratamiento debe ser >50-100 µg/l (rellenar depósitos), pero la **definición operativa de refractariedad** es ferritina <15 µg/l tras 4-8 semanas a dosis adecuadas.

---

### 🟠 [MODERADO] Listado de preparados IV no incluye dosis usables

**Hallazgo en la nota (líneas 91-94):** menciona Venofer®, Ferinject®, hierro dextrano sin dosis.

**Cita — Manual 12 Oct 2022, p. 1243, Tabla 6 ("Preparados de hierro intravenoso"):**
> "**Hierro sacarosa (Venofer®, Normon®, Feriv®)** — 20 mg/ml — Múltiples dosis: **100-200 mg, 1-3 veces/semana**."
> "**Carboximaltosa férrica (Ferinject®)** — 50 mg/ml — **No más de 1.000 mg/semana en una única dosis** (diluir en 250 ml de SSF, a pasar en 30 min) o en múltiples de 200 mg."
> "**Complejo de hierro dextrano (Cosmofer®)** — 50 mg/ml — Múltiples dosis: 100-200 mg 2-3 veces/semana. Dosis única: **1.000 mg, diluido en 500 ml SSF/SG, a pasar en 6 h**."
> *"No hay evidencia de que una dosis única superior a 1.000 mg tenga beneficio"* (p. 1243).
> *Premedicación: "Se recomienda administrar **125 mg de metilprednisolona antes de la infusión**"* en pacientes con asma, alergia múltiple o artritis inflamatoria.

**Acción:** añadir dosis y nota de premedicación en pacientes de alto riesgo de hipersensibilidad.

---

### 🟠 [MODERADO] Umbrales de transfusión incompletos (no contempla HDA ni cifra objetivo)

**Hallazgo en la nota:** *"Reservar para anemia sintomática grave (Hb <7-8 g/dL, o <10 g/dL con cardiopatía isquémica)"* (línea 101).

**Cita — Manual 12 Oct 2022, cap. 84 (Hemoterapia), p. 1287, sección 2.3.2.1 "Indicaciones":**
> *"Se recomienda transfundir hematíes a pacientes **no cardiópatas si su Hb es menor de 7 g/dl y a pacientes con enfermedad cardiovascular si es inferior a 9 g/dl**."*
> Anemia preoperatoria: *"Hay que transfundir CH si la Hb es menor de **7 g/dl en pacientes sanos o menor de 8,5-9,5 g/dl en caso de enfermedad cardiovascular o respiratoria crónica**."*
> Anemia crónica refractaria: *"no se recomienda permitir cifras de Hb por debajo de **7-8 g/dl** de manera prolongada. En pacientes con factores de riesgo cardiovascular, sobre todo con enfermedad coronaria, el dintel mínimo de Hb debe ser **más alto, alrededor de 9 g/dl**."*

**Cita — Manual 12 Oct 2022, cap. 36 (Hemorragia digestiva), p. 509:**
> HDA no asociada a HTP: *"Se debe trasfundir a pacientes con cifras de hemoglobina (Hb) de menos de **7 g/dl**, con una **Hb objetivo de 7-9 g/dl**. Si existen comorbilidades significativas (especialmente patología cardiovascular), hay que considerar trasfundir con **Hb menor de 8 g/dl, con una cifra objetivo de Hb de más de 9 g/dl**."*

**Acción:** alinear la cifra para cardiópatas: el umbral correcto en el Manual 12 Oct para cardiópatas es **<8 g/dl** (HDA) o **<9 g/dl** (anemia crónica/preoperatorio), no <10 g/dl como dice la nota. Añadir contraindicación relativa: *"Anemia carencial (déficit de hierro, vit B12 o ácido fólico): salvo que sean sintomáticas, priorizar reposición de hematínicos"* (Manual p. 1288).

---

### 🟢 [MENOR] Plummer-Vinson: nombre alternativo correcto pero el umbral de Hb a partir del cual aparece y la asociación con cáncer postcricoideo no se mencionan.

**Acción:** añadir nota de derivación a ORL en disfagia + ferropenia; no es un hallazgo crítico para una nota de Medicina de Familia.

---

## 3. `Anemia de Enfermedad Crónica (ACD-AI).md`

### 🟠 [MODERADO] Umbral de transferrina/TIBC discrepante con UpToDate

**Hallazgo en la nota (línea 70-71):** "Transferrina/TIBC **baja** (< 300 mcg/dL)".

**Cita — UpToDate ACD/AI, sección "Iron studies":**
> *"Transferrin (also measured as total iron binding capacity [TIBC]) is low (**normal range, 300 to 360 mcg/dL** [3 to 3.6 mg/L]; 54 to 64 microM/L)."*

> Sección "Making the diagnosis": *"**Normal to low serum transferrin (generally <300 mcg/dL)**"*.

**Lectura correcta:** TIBC <300 µg/dl = bajo (porque el rango normal arranca en 300). La nota es técnicamente correcta pero introduce confusión: dice "<300" como "bajo" sin aclarar que el rango normal **comienza** en 300. Mejorable.

**Acción:** especificar rango normal (300-360 µg/dl) para que el "<300" se interprete bien.

---

## 4. `Anemia Microcítica.md`

### 🟠 [MODERADO] Umbral de Mentzer y comentario sobre "RBC alto en talasemia" — bien, pero falta mencionar punteado basófilo en β-talasemia y necesidad de electroforesis con HbA2

**Cita — UpToDate "Diagnostic approach to anemia in adults", sección "Microcytosis":**
> *"The ratio of the MCV to the red blood cell (RBC) count (Mentzer index) is useful in predicting the likelihood of thalassemia trait versus iron deficiency. **If the ratio of MCV (in fL) to RBC count (in millions of cells/microL) is less than 13, thalassemia is more likely than iron deficiency**. However, specific testing is needed for diagnosis."*

> *"Basophilic stippling may also be seen with beta thalassemia."*

**Cita — Manual 12 Oct 2022, p. 1238:**
> "**β-talasemia minor (rasgo talasémico): eritrocitosis, microcitosis, dianocitos, ocasional punteado basófilo y eritroblastos aislados**."

La nota lo menciona en una línea pero sin explicitar que el dx confirmatorio en β-talasemia es **electroforesis con HbA2 elevada** y que en α-talasemia se necesita **estudio genético** (la electroforesis suele ser normal en adultos).

**Acción:** añadir aclaración de que la electroforesis NO detecta α-talasemia adulta.

---

## 5. `Anemia Macrocítica.md`

### 🟢 [MENOR] El criterio de derivación a Hematología por MCV >110 está bien (UpToDate lo apoya), pero la dosis de cianocobalamina IM en la nota es subóptima

**Hallazgo en la nota (línea 73):** *"Cianocobalamina 1000 µg/día IM durante 1 semana → semanal 1 mes → mensual indefinidamente"*.

**Cita — Manual 12 Oct 2022, p. 1251:**
> *"Cianocobalamina parenteral: **1.000 µg/semana hasta corregir el déficit y posteriormente 1.000 µg/mes**. En afectación neurológica, embarazo o anemia sintomática hay que administrar **1.000 µg a días alternos durante 2 semanas y posteriormente 1.000 µg/mes**."*

> *"Cianocobalamina oral: **1.000 µg/día**. Si la absorción oral no está impedida, es igual de eficaz que su administración parenteral. Si la absorción oral está disminuida, se deben administrar **1.000-2.000 µg/día**."*

**Lectura:** la pauta "1000 µg/día IM × 1 semana" de la nota es más intensiva que la del Manual ("1000 µg/semana hasta corregir"). La pauta intensiva (días alternos × 2 sem) está reservada a **afectación neurológica/anemia sintomática/embarazo**.

**Acción:** ajustar a la pauta del Manual, distinguiendo casos no graves vs. afectación neurológica. La advertencia "Nunca tratar con folato sin descartar antes déficit de B12" está perfectamente alineada con Manual p. 1250 ("ya que el uso de ácido fólico en exclusiva puede mejorar la anemia producida por ambos déficits pero empeorar las manifestaciones neurológicas ocasionadas por el déficit de vitamina B12").

---

## 6. `Anemia - Abordaje General.md`

### 🟢 [MENOR] Cifra OMS para mujeres embarazadas — refinar

**Hallazgo en la nota:** "Mujeres embarazadas (1.er trimestre) — < 11 g/dL".

**Cita — UpToDate "Diagnostic approach to anemia in adults", Tabla 1 (WHO 2024):**
> Embarazo:
> - **1.er trimestre**: <11,0 g/dl (no anémica ≥11,0)
> - **2.º trimestre**: <10,5 g/dl (no anémica ≥10,5)
> - **3.er trimestre**: <11,0 g/dl

**Cita — Manual 12 Oct 2022, p. 1238:**
> "Hb < 11 g/dl en mujeres embarazadas (**< 10,5 g/dl en el segundo trimestre y < 10 g/dl en el tercero**)" — discrepa con UpToDate (que pone 11,0 en el tercer trimestre).

**Acción:** la nota solo menciona el 1.er trimestre. Conviene añadir 2.º y 3.er trimestre (puede usarse el criterio del Manual o el de UpToDate, pero hay que indicarlo).

> **Nota técnica:** los rangos de "MCV 82,5-98 fL" y demás índices CBC en la nota (líneas 22-25) **coinciden exactamente** con UpToDate (Tabla 2: "MCV 82.5 to 98", "MCH 27.6 to 33.3", "MCHC 32.5 to 35.2", "RDW 11.4 to 13.5"). Excelente.

---

## 7. `Pancitopenia.md`

### 🟢 [MENOR] La definición debería alinearse al Manual y los umbrales de gravedad citopénica deberían ser explícitos

**Cita — Manual 12 Oct 2022, p. 1278:**
> *"En pacientes con pancitopenia de origen central, la urgencia con la que debe programarse el estudio morfológico de la MO depende de la gravedad del cuadro clínico, que está determinada fundamentalmente por el grado de citopenias (**anemia con reticulocitos <20 × 10⁹/l, plaquetopenia <10 × 10⁹/l de nuevo diagnóstico o <50 × 10⁹/l con evidencia de sangrado y neutropenia <0,5 × 10⁹/l**)."*

**Acción:** añadir umbrales cuantitativos de gravedad citopénica a la sección "Red Flags" (la nota ya menciona "pancitopenia grave + hipoplasia medular → aplasia medular" pero sin cifras).

---

## 8. `Anemia Hemolítica - Abordaje.md`

**Sin hallazgos.** La nota es exhaustiva, los criterios de hemólisis (LDH↑ + haptoglobina↓ = 90% específica; LDH normal + haptoglobina normal = 92% sensibilidad para descartar) coinciden literalmente con UpToDate "Diagnostic approach to anemia in adults", sección "Hemolysis":

> *"The combination of an increased LDH and reduced haptoglobin is **90 percent specific for acute hemolysis**, while the combination of a normal LDH and a serum haptoglobin greater than 25 mg/dL is **92 percent sensitive for ruling out hemolysis**."*

Las urgencias (esquistocitos → TMA → plasmaféresis en TTP, **NO transfundir plaquetas en TTP**) están correctamente identificadas. La clasificación etiológica (hereditarias / adquiridas inmunes / no inmunes) y el algoritmo (Coombs directo + frotis) son fieles a UpToDate.

---

## 9. `Anemia Normocítica.md`

**Sin hallazgos.** Las causas, el papel pivotal de los reticulocitos y el algoritmo (>60 años → SPEP, testosterona, MDS panel) reflejan UpToDate "Diagnostic approach to anemia in adults", secciones "Older adults" y "Normocytic":

> *"Major causes of anemia in older adults include: **Nutritional deficiencies in approximately one third. Kidney disease or anemia of chronic disease/inflammation (ACD/AI) in approximately one third. Unexplained in the remaining third**."*

> *"Anemia in an individual with diabetes should not be attributed to diabetes without a thorough evaluation for other causes."*

---

## Resumen de prioridades para el residente

1. **Reescribir `Sdme Hemofagocitico.md`** desde cero (es la única nota del bloque que no aporta nada actualmente y es una urgencia hematológica).
2. **Corregir `Anemia Ferropénica.md`**: pauta de hierro oral en mg de Fe elemental (150-200 mg/día), preparados españoles reales (Fero Gradumet, Tardyferon), opción de dosis alterna, premedicación de hierro IV en alérgicos, umbral correcto de transfusión en cardiópatas (<8-9 g/dl, no <10).
3. **Aclarar rango de transferrina/TIBC** en `ACD-AI.md` (300-360 µg/dl es normal; "<300" es bajo).
4. **Añadir umbrales cuantitativos de citopenia grave** en `Pancitopenia.md` (Hb con retic <20 ×10⁹/l, plaq <10 ×10⁹/l, NEU <0,5 ×10⁹/l).
5. **Ajustar pauta de cianocobalamina** en `Anemia Macrocítica.md` a la del Manual.
6. **Completar criterios OMS de anemia en embarazo** (2.º y 3.er trimestre) en `Anemia - Abordaje General.md`.

---

## Notas sin hallazgos (3/9)

- `Anemia Hemolítica - Abordaje.md`
- `Anemia Normocítica.md`
- (parcialmente) `Anemia - Abordaje General.md` — solo 1 hallazgo menor

---

## Anexo: archivos temporales generados durante la auditoría

- `/home/arenas/Obsidian/MIR/.tmp_uptodate_acd.txt` (texto plano del PDF de UpToDate ACD)
- `/home/arenas/Obsidian/MIR/.tmp_uptodate_anemia.txt` (texto plano del PDF de UpToDate Anemia)
- `/home/arenas/Obsidian/MIR/.tmp_manual12oct.txt` (texto plano del Manual 12 Oct 2022)

Pueden eliminarse con `rm /home/arenas/Obsidian/MIR/.tmp_*.txt`.
