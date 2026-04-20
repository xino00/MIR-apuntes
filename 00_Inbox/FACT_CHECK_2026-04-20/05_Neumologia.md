---
tags: [auditoria, fact-check, neumo]
fecha_auditoria: 2026-04-20
fuentes_consultadas:
  - "GEMA 5.5 (2025) - Guía Española para el Manejo del Asma"
  - "GOLD 2026 - Global Strategy for COPD"
notas_auditadas: 17
hallazgos_total: "16 (0🔴 · 7🟠 · 5🟢 · 4⚪)"
auditor: claude-opus-4-7
---

# Auditoría 05 - Neumología (17 notas)

## Resumen ejecutivo

Auditoría clínica de las 17 notas de Neumología contrastando contra GEMA 5.5 (2025) y GOLD 2026. **Sin hallazgos críticos** (ninguno con riesgo inmediato para el paciente), pero existen **7 hallazgos moderados** que afectan la fidelidad de las notas a las guías locales actuales:

1. **Tabla de control del asma**: la nota `Asma - Clasificación y Control` usa la cadencia "días/semana" en vez de "días/mes" para clasificar bien controlada (GEMA Tabla 2.6).
2. **Cutoffs ACQ**: la nota usa la versión internacional (<0,75/0,75-1,5/>1,5) en vez de la versión española validada por GEMA (<0,5/0,5-0,99/≥1).
3. **Salbutamol en crisis adulto**: la nota Crisis Asmática dice "4-10 puls c/20 min"; GEMA Tabla 4.3 dice "2-8 puls c/10-15 min".
4. **Umbrales de eosinófilos en biológicos AGNC**: las notas `Asma Grave No Controlada` y `Asma - Tratamiento Escalonado` confunden umbrales de **indicación IPT** con umbrales de **mayor eficacia** para Mepolizumab, Benralizumab y Dupilumab.
5. **Criterios IPA**: las notas `Asma - Definición y Patogenia` y `Asma - Pediátrica` listan **3** criterios mayores (incluyendo sensibilización a aeroalérgenos), cuando GEMA 5.5 Tabla 1.11 lista solo **2** (asma en padres + dermatitis atópica).
6. **HFNT como "1ª línea" en EPOC hipoxémica**: las notas `EPOC - Exacerbación` y `EPOC reagudizado` afirman que GOLD 2026 lo recomienda como primera modalidad con Evidencia A. GOLD 2026 NO afirma esto: oxígeno convencional sigue siendo "first line" y HFNT es opción cuando fallan o no se toleran las alternativas.
7. **Mepolizumab en EPOC con eos ≥150**: la nota `EPOC - Manejo Crónico` cita "Eos ≥ 150 (cribado) o ≥ 300 (año previo)". GOLD 2026 (Cap 3, p.66) recomienda mepolizumab en pacientes con **eos ≥ 300/µL**; el umbral ≥150 no aparece en GOLD 2026 como umbral de recomendación.

**Hallazgos menores** (5🟢): mezcla de "≥ 1 exacerbación" en columna mal vs parcialmente controlada, FENO de "buena respuesta a GCI" como ≥ 50 vs ≥ 25 ppb (matiz), umbral de "Salbutamol max 5 días" en broncoespasmo IRVA, ensifentrine sin nota de disponibilidad solo en EE.UU., y rangos de GCI dosis altas abiertas hacia arriba sin tope GEMA.

**Hallazgos informativos** (4⚪): notas extraídas de plantilla de guardia (`Bronquitis Aguda`, `Broncoespasmo en IRVA`, `NAC`, segmentos de `EPOC reagudizado`) sin fuente formal declarada para los esquemas terapéuticos; incluyen recomendaciones plausibles pero no respaldadas por las fuentes maestras GEMA/GOLD que sí auditamos.

---

## Hallazgos por nota

### 🟠 Asma - Clasificación y Control

**Ruta**: `/home/arenas/Obsidian/MIR/10_Patologias/05_Neumologia/Asma - Clasificación y Control.md`

#### 🟠 Hallazgo 1: Cadencia incorrecta en tabla "Bien controlada"

- **Cita en la nota** (líneas 27-34): tabla "Nivel de Control del Asma" muestra:
  - Síntomas diurnos bien controlada: "≤ 2 días/**semana**"
  - SABA rescate bien controlada: "≤ 2 días/**semana**"
  - Síntomas diurnos parcialmente controlada: "> 2 días/**semana**"
- **Fuente literal** GEMA 5.5 Tabla 2.6 (Cap 2, p.49):
  - Síntomas diurnos bien controlada: "Ninguno o ≤ 2 días al **mes**"
  - Necesidad medicación de rescate bien controlada: "Ninguna o ≤ 2 días al **mes**"
  - Síntomas diurnos parcialmente controlada: "> 2 días al **mes**"
- **Por qué importa**: criterio mucho más estricto del que figura en la nota. Un paciente con síntomas 2 días/semana sería "parcialmente controlada" según GEMA, no "bien controlada". Riesgo de infraescalar tratamiento.
- **Acción sugerida**: corregir "/semana" → "/mes" en filas 1, 4 y 5 de la tabla; añadir matiz de que la versión actual de GEMA usa una cadencia mensual más estricta que la GINA internacional.

#### 🟠 Hallazgo 2: Cutoffs ACQ no son los validados en español

- **Cita en la nota** (líneas 46-52):
  - "< 0,75 = bien controlada"
  - "0,75-1,5 = parcialmente"
  - "> 1,5 = mal controlada"
- **Fuente literal** GEMA 5.5 §2.6 (Cap 2, p.51): "También se han validado en la versión española del ACQ unos puntos de corte, basados en práctica clínica real, siendo la puntuación para el asma bien controlada **< 0,5**, entre **0,5 a 0,99** para el asma parcialmente controlada y **≥ 1**, para el asma mal controlada."
- Adicionalmente, GEMA Tabla 2.7 lista ACQ > 1,5 sólo como "factor de riesgo" para exacerbaciones (no como umbral de control).
- **Acción sugerida**: actualizar la tabla ACQ a los cortes españoles validados; mantener mención de > 1,5 como factor de riesgo añadido.

#### 🟢 Hallazgo 3: "≥ 1 exacerbación" mezclado entre Parcialmente y Mal controlada

- **Cita en la nota** (línea 34): la columna "Mal controlada" pone "Exacerbaciones: ≥ 1 en el año previo".
- **Fuente literal** GEMA Tabla 2.6 (Cap 2, p.49): solo "Parcialmente controlada" tiene "≥ 1/año"; en "Mal controlada" no aparece esta fila.
- **Acción sugerida**: borrar la celda "≥ 1 en el año previo" de la columna "Mal controlada" o aclarar que ≥ 3 características de parcialmente controlada = mal controlada (la propia GEMA lo señala).

#### 🟢 Hallazgo 4: Función pulmonar "Normal" en bien controlada

- **Cita en la nota** (línea 33): "Función pulmonar bien controlada = Normal".
- **Fuente literal** GEMA Tabla 2.6: "Bien controlada: FEV1 **≥ 80% del valor teórico** o Z-score ≥ -1,64; PEF ≥ 80 % del mejor valor personal".
- **Acción sugerida**: sustituir "Normal" por el criterio cuantitativo concreto.

---

### 🟠 Asma - Crisis Asmática

**Ruta**: `/home/arenas/Obsidian/MIR/10_Patologias/05_Neumologia/Asma - Crisis Asmática.md`

#### 🟠 Hallazgo 5: Dosis e intervalo de Salbutamol en crisis leve-moderada

- **Cita en la nota** (línea 35): "Salbutamol vía inhalatoria o cámara espaciadora. **4-10 pulsaciones cada 20 min** durante la primera hora."
- **Fuente literal** GEMA 5.5 Tabla 4.3 (Cap 4, p.105): "Salbutamol: pMDI + cámara: 200-800 μg (**2-8 inhalaciones de 100 μg/puls**) **c/10-15 min** durante la 1ª hora."
- **Por qué importa**: la nota infraestima la frecuencia (cada 20 min cuando GEMA pide cada 10-15 min) y el rango superior es ligeramente alto (10 vs 8). En una crisis moderada, una cadencia c/20 min puede ser insuficiente.
- **Acción sugerida**: cambiar a "2-8 pulsaciones cada 10-15 min durante la primera hora".

#### 🟢 Hallazgo 6: PEF de "buena respuesta" >70% — verificación

- **Cita en la nota** (línea 54): "Buena respuesta: SatO2 > 94 %, PEF > 70 %".
- **Fuente literal** GEMA 5.5 Fig 4.2 (Cap 4, p.109): el algoritmo de destino indica que "PEF o FEV1 > 70 %" + estabilidad → criterio de alta. Texto del cap 4 (p.109): "Valores de FEV1 o PEF > 70 % y con mínima sintomatología pueden ser criterios de alta".
- **Resultado**: la nota es CORRECTA. Solo se mantiene como hallazgo informativo para confirmar que el cutoff > 70 % está bien.
- **Acción sugerida**: ninguna; nota correcta.

---

### 🟠 Asma Grave No Controlada (AGNC)

**Ruta**: `/home/arenas/Obsidian/MIR/10_Patologias/05_Neumologia/Asma Grave No Controlada.md`

#### 🟠 Hallazgo 7: Umbrales de eosinófilos en biológicos confunden indicación IPT con eficacia

- **Cita en la nota** (líneas 95-102, Tabla "Biológicos para AGNC"):
  - Mepolizumab: "eos ≥ **500/µL** o ≥ **300/µL** + exacerbaciones"
  - Benralizumab: "eos ≥ **300/µL**"
  - Dupilumab: "Eos ≥ **150/µL** o FENO ≥ **50 ppb**; corticodependiente"
- **Fuente literal** GEMA 5.5 Tabla 7.5 (Cap 7, p.159-160):
  - Mepolizumab — Aprobación IPT: "Eos ≥ **500** o **< 500** con 2 exacerbaciones graves o 1 hospitalización en el año previo"
  - Benralizumab — Aprobación IPT: "Eo ≥ **500** o **< 500** con 2 exacerbaciones graves o 1 hospitalización en el año previo"
  - Dupilumab — Aprobación IPT: "marcadores T2 (Eos ≥ **300** o FENO ≥ **50 ppb**) o corticodependiente"
- **Texto adicional cap 7.4** (líneas 590-611): "Mepolizumab — su indicación es a partir de **150 Eo/µl**, pero **mayor eficacia ≥ 500 eos./µl**: indicado en pacientes con ≥ 150 Eo/µl si existen valores históricos de ≥ 300 Eo/µl"; "Benralizumab — **mayor eficacia ≥ 300 eos./µl**"; "Dupilumab — **mayor eficacia ≥ 300 Eo/µl y/o FENO ≥ 50 ppb**".
- **Por qué importa**: la nota mezcla los umbrales "de la ficha técnica/IPT" con los "de mayor eficacia". Concretamente:
  - Para **Mepolizumab**, el umbral inferior con exacerbaciones es < 500 (no ≥ 300/µL); el ≥ 150/µL aparece en el texto narrativo (con historial de ≥ 300) pero NO como criterio principal de la Tabla 7.5.
  - Para **Benralizumab**, el IPT español exige ≥ 500 o < 500 con exacerbaciones (no ≥ 300/µL).
  - Para **Dupilumab**, el umbral de indicación IPT es ≥ 300 (no ≥ 150 como dice la nota); ≥ 150/µL es el umbral inferior con FENO elevado en algunos resúmenes pero la Tabla 7.5 oficial dice ≥ 300.
- **Acción sugerida**: rehacer la columna "Indicación (IPT España)" reproduciendo literalmente la Tabla 7.5 GEMA y separar en columna aparte los "Biomarcadores de mayor eficacia" (donde sí aparecen los umbrales más bajos).

#### 🟢 Hallazgo 8: Dupilumab biomarcador respuesta "FENO ≥ 25 ppb" — matiz

- **Cita en la nota** (línea 101, columna "Biomarcadores respuesta"): "Eos ≥ 150/µL o FENO ≥ **25 ppb**".
- **Fuente literal** GEMA 5.5 Tabla 7.5 (p.160) — Aprobación: "FENO ≥ 50 ppb"; texto Cap 7.4 (p.756): "el efecto del dupilumab es mayor en pacientes con FENO ≥ **50 ppb**".
- El cutoff ≥ 25 ppb aparece sólo como umbral mínimo de inflamación T2 (cap 7.4, línea 608 GEMA) — útil pero no es el biomarcador específico de respuesta a dupilumab.
- **Acción sugerida**: aclarar que ≥ 50 ppb es el umbral de mayor eficacia; ≥ 25 ppb es el umbral mínimo de inflamación T2.

---

### 🟠 Asma - Tratamiento Escalonado

**Ruta**: `/home/arenas/Obsidian/MIR/10_Patologias/05_Neumologia/Asma - Tratamiento Escalonado.md`

#### 🟠 Hallazgo 9: Mismos umbrales de biológicos discordantes que en AGNC

- **Cita en la nota** (líneas 67-72, tabla biológicos del Escalón 6):
  - Mepolizumab: "eos ≥ 300/µL"
  - Benralizumab: "eos ≥ 300/µL"
  - Dupilumab: "T2 con eos ≥ 150/µL o FENO ≥ 25 ppb"
- **Fuente literal**: idéntico al hallazgo 7 — GEMA Tabla 7.5 dice ≥ 500 (o < 500 con exacerbaciones) para Mepolizumab y Benralizumab; ≥ 300 (o FENO ≥ 50 ppb) para Dupilumab.
- **Acción sugerida**: armonizar con la tabla principal de AGNC tras corregir aquélla.

#### 🟢 Hallazgo 10: Dosis altas de GCI sin tope superior

- **Cita en la nota** (líneas 78-83): GCI dosis alta "Budesónida > 800 µg/día"; "Beclometasona > 1.000 µg/día"; etc.
- **Fuente literal** GEMA 5.5 Tabla 3.3 (Cap 3, p.86): Budesónida alta = **801-1.600 µg/día**; Beclometasona alta = **1.001-2.000 µg/día**; Fluticasona propionato alta = **501-1.000 µg/día**; Ciclesonida alta = **321-1.280 µg/día**.
- **Por qué importa**: los rangos GEMA tienen tope superior; "abrir hacia arriba" puede sugerir que se pueden usar dosis aún mayores cuando GEMA fija un máximo razonable.
- **Acción sugerida**: añadir el tope superior según Tabla 3.3 GEMA.

---

### 🟠 Asma - Definición y Patogenia / Asma - Pediátrica (afecta a ambas)

**Rutas**: 
- `/home/arenas/Obsidian/MIR/10_Patologias/05_Neumologia/Asma - Definición y Patogenia.md`
- `/home/arenas/Obsidian/MIR/10_Patologias/05_Neumologia/Asma - Pediátrica.md`

#### 🟠 Hallazgo 11: IPA con un criterio mayor adicional no listado en GEMA Tabla 1.11

- **Cita en la nota** Asma - Definición y Patogenia (líneas 98-102):
  - "Criterios mayores: Diagnóstico médico de asma en padre/madre / Dermatitis atópica / **Sensibilización alérgica a aeroalérgenos**"
- **Cita en la nota** Asma - Pediátrica (líneas 21-25): mismas tres categorías como criterios mayores.
- **Fuente literal** GEMA 5.5 Tabla 1.11 (Cap 1, p.36):
  - "Criterios mayores: – Diagnóstico médico de asma en alguno de los padres. – Diagnóstico médico de eccema atópico (a los 2-3 años de edad)." (Solo **2** mayores.)
  - Criterios menores GEMA: rinitis alérgica, sibilancias no asociadas a resfriados, eosinofilia ≥ 4 %.
- **Por qué importa**: el "tercer criterio mayor" (sensibilización a aeroalérgenos) es del mAPI/IPA modificado de Guilbert 2004 (Castro-Rodríguez), no del IPA clásico de Tucson recogido por GEMA. Diferenciarlos es relevante para decisiones de inicio precoz de GCI.
- **Acción sugerida**: corregir ambas notas para listar solo los 2 criterios mayores GEMA (asma parental + dermatitis atópica), o bien etiquetar explícitamente que se está usando "IPA modificado (mAPI)" si se mantienen los 3.

---

### 🟠 EPOC - Manejo Crónico

**Ruta**: `/home/arenas/Obsidian/MIR/10_Patologias/05_Neumologia/EPOC - Manejo Crónico.md`

#### 🟠 Hallazgo 12: Mepolizumab en EPOC con "Eos ≥ 150 (cribado)"

- **Cita en la nota** (línea 83): "Mepolizumab (Anti-IL-5, 100 mg/4 sem): **Eos ≥ 150 (cribado) o ≥ 300 (año previo)**. Ensayos METREO/METREX/MATINEE: RR exacerbaciones 0.79-0.82."
- **Fuente literal** GOLD 2026 Cap 3 "Group E follow-up" (p.66, líneas 2969-2975 del extracto): "Among patients with blood eosinophils **≥ 300 cells/µL**, consider adding **dupilumab** (if chronic bronchitis) or **mepolizumab** (with and without chronic bronchitis) (Figure 3.11)."
- Búsqueda en todo GOLD 2026 (texto extraído): el umbral "150 cells/μL" no aparece como umbral de recomendación para mepolizumab en EPOC. El ensayo MATINEE incluyó pacientes con eos ≥ 150 como criterio de inclusión, pero GOLD no lo eleva a umbral de recomendación.
- **Acción sugerida**: simplificar la indicación a "Eos ≥ 300 cells/µL (GOLD 2026 Fig 3.11)" o aclarar que el umbral inferior pertenece al diseño del ensayo MATINEE, no a la recomendación GOLD.

#### 🟢 Hallazgo 13: Ensifentrine sin caveat de disponibilidad

- **Cita en la nota** (línea 80): "Ensifentrine: Inhibidor dual PDE3/PDE4 inhalado. Posicionado en el algoritmo de seguimiento (Fig. 3.9) como opción add-on cuando LABA+LAMA no controla la disnea persistente."
- **Fuente literal** GOLD 2026 Cap 3 §Pharmacological therapy (línea 17163 extracto completo): "Ensifentrine is **currently only available in the US**."
- **Por qué importa**: aunque GOLD lo posicione en el algoritmo, no está comercializado en España (consultar AEMPS antes de incluirlo en la práctica). Útil para evitar prescripción frustrada.
- **Acción sugerida**: añadir nota de disponibilidad: "(GOLD 2026: actualmente solo disponible en EE.UU.)".

---

### 🟠 EPOC - Exacerbación y Manejo Agudo

**Ruta**: `/home/arenas/Obsidian/MIR/10_Patologias/05_Neumologia/EPOC - Exacerbación y Manejo Agudo.md`

#### 🟠 Hallazgo 14: HFNT como "primera modalidad" con Evidencia A

- **Cita en la nota** (línea 32): "Alto Flujo (HFNT/GNAF): *(GOLD 2026, Evidencia A)* — **primera modalidad de soporte ventilatorio** en pacientes con EPOC e insuficiencia respiratoria **hipoxémica** aguda."
- **Fuente literal** GOLD 2026 Cap 4 §Oxygen therapy / High-flow nasal therapy (p.105, línea 2510 extracto):
  - "Oxygen therapy has been considered **first line respiratory support** in patients suffering an exacerbation. **However, in patients with COPD who remain hypoxemic despite the use of conventional oxygen therapy, hypercapnic, or unable to tolerate NIV, HFNT has been used**..."
  - GOLD 2026 NO atribuye Evidencia A a HFNT como primera línea hipoxémica. Tampoco existe esta etiqueta en el texto extraído.
- **Por qué importa**: distorsiona el algoritmo. La primera línea sigue siendo oxígeno convencional titulado SaO₂ 88-92 %; HFNT es alternativa cuando falla esto, hay hipercapnia o no se tolera NIV. NIV sigue siendo el estándar para fallo hipercápnico (líneas 2634-2636 GOLD: "ERS Clinical Practice Guidelines currently recommend the use of NIV over HFNT for patients hospitalized with exacerbations and hypercapnic respiratory failure").
- **Acción sugerida**: reformular: "HFNT es alternativa cuando hay hipoxemia persistente a oxígeno convencional, hipercapnia leve o intolerancia a NIV (GOLD 2026 Cap 4, p.105). Para fallo hipercápnico la NIV sigue siendo el estándar."

---

### 🟠 EPOC reagudizado (índice)

**Ruta**: `/home/arenas/Obsidian/MIR/10_Patologias/05_Neumologia/EPOC reagudizado.md`

#### 🟠 Hallazgo 15: Misma afirmación HFNT "1ª línea"

- **Cita en la nota** (línea 21): "Oxígeno: objetivo SpO₂ 88-92%; **HFNT como 1.ª línea de soporte ventilatorio en hipoxemia**; VMNI si pH ≤ 7.35 + pCO₂ ≥ 45"
- **Fuente literal**: idéntica al hallazgo 14.
- **Acción sugerida**: corregir la frase resumen.

---

### 🟢 Bronquitis Aguda

**Ruta**: `/home/arenas/Obsidian/MIR/10_Patologias/05_Neumologia/Bronquitis Aguda.md`

#### ⚪ Hallazgo 16: Sin fuente documentada para esquema antibiótico

- **Cita en la nota** (líneas 23-27, "ANTIBIÓTICO SOLO SI"): "1ª ELECCIÓN: Amoxicilina 500 mg/8h × 5 d / SÍNTOMAS GRAVES: Amoxi-Clav 875/125/8h × 5 d / ALÉRGICOS: Azitromicina 500 mg/24h × 3 d / FRACASO+ALÉRGICOS: Levofloxacino 500 mg/24h × 5 d".
- **Frontmatter declarado**: "fuente_original: Extraído de 50_Guardias/02 - Plantilla Policlínicas Urgencias.md".
- GEMA 5.5 y GOLD 2026 no cubren esta entidad. La afirmación previa de la nota — "**No está indicado el antibiótico salvo criterios de sobreinfección o sospecha de neumonía**" — está alineada con la doctrina general (NICE NG120, ACP/CDC), aunque no se puede citar fuente local.
- **Acción sugerida** (no obligatoria): añadir referencia al protocolo PROA local o a NICE NG120 para respaldar el esquema; o etiquetar como "esquema empírico de la guardia, sin fuente externa formal".

---

### ⚪ Broncoespasmo en IRVA

**Ruta**: `/home/arenas/Obsidian/MIR/10_Patologias/05_Neumologia/Broncoespasmo en IRVA.md`

- **Frontmatter declarado**: extracto de plantilla de guardia.
- Recomendaciones de salbutamol y MART (Symbicort/Foster) coherentes con GEMA 5.5 §3 (escalón 1-2). No se observan discrepancias accionables. Se mantiene como ⚪ (no contradice fuente, fuente no es maestra).

---

### ⚪ Neumonía Adquirida en la Comunidad (NAC)

**Ruta**: `/home/arenas/Obsidian/MIR/10_Patologias/05_Neumologia/Neumonía Adquirida en la Comunidad (NAC).md`

#### ⚪ Hallazgo (informativo): epidemiología y "tos postinfecciosa con CTC oral" sin fuente local

- **Cita en la nota** (líneas 27-32): porcentajes "M. pneumoniae (16%) / S. pneumoniae (14%) / Virus (15%) / C. pneumoniae (12%)".
- **Cita en la nota** (línea 51): "La tos postinfecciosa puede persistir hasta 3 meses. Se puede ajustar tratamiento inhalado con **GCI + LABA + CTC oral (Prednisona 30mg 5 días)**."
- GEMA y GOLD no cubren NAC. Las guías estándar SEPAR/IDSA-ATS no respaldan rutinariamente CTC oral para tos postinfecciosa post-NAC. Los porcentajes etiológicos son aproximados y no coinciden exactamente con datos SEPAR/SemFYC clásicos (S. pneumoniae sigue siendo el más frecuente cuando se identifica patógeno, ~30-50 %).
- **Acción sugerida** (no obligatoria, pendiente de confirmar con SEPAR 2022 / Manual 12 Octubre 2022): revisar la etiología y la recomendación de CTC oral para tos postinfecciosa.

---

## Notas sin hallazgos relevantes (auditadas)

Las siguientes notas se contrastaron contra GEMA 5.5 / GOLD 2026 y no presentan discrepancias accionables (los puntos verificados están alineados con la fuente):

- **Asma - Definición y Patogenia** — además del hallazgo IPA (compartido con Asma Pediátrica), el resto de la patogenia T2 (alarminas TSLP/IL-25/IL-33; ILC2; IL-4/5/13; IgE FcεRI; periostina) está alineada con GEMA Cap 1.4 y Tabla 7.4. *(Nota: solo el hallazgo IPA queda como 🟠).*

- **Asma - Diagnóstico** — FEV1/FVC < LIN, PBD positiva (≥ 12 % y ≥ 200 mL), umbrales FENO ≥ 40 ppb (adultos) y ≥ 50 ppb (predice respuesta GCI), variabilidad PEF > 20 % y test metacolina (caída FEV1 ≥ 20 %) coinciden con GEMA Cap 2.4 (p.43-46).

- **Asma - Manejo Crónico** — resumen general alineado con GEMA Cap 3 (escalonado 1-6) y GEMA 5.5 / REMAS 2024 (criterios de remisión clínica/completa).

- **Asma - Pediátrica** — algoritmo crisis pediátrica (Salbutamol 0,15 mg/kg, prednisona 1-2 mg/kg, sulfato Mg 40 mg/kg IV) y dosis GCI Tabla 5.5 coinciden con GEMA Cap 5 (p.124-126). *(Solo se mantiene el hallazgo IPA compartido).*

- **Asma - Dispositivos de Inhalación** — no auditada en profundidad, pero el contenido está vinculado a GEMA Cap 3.2.2; no se identificaron afirmaciones discordantes en revisión rápida.

- **Asma - Circunstancias Especiales** — ACO (criterios fumador/exfumador ≥ 35 años, FEV1/FVC < 70 %, eos ≥ 300 o PBD ≥ 15 % y 400 mL), asma y embarazo (budesónida 1ª línea, riesgo de mal control > riesgo de fármacos), asma ocupacional (PPBE como gold standard) coinciden con GEMA Cap 8.

- **Rinitis Alérgica y Rinosinusitis** — clasificación ARIA (intermitente/persistente, leve/moderada/grave) y criterios POLINA para biológicos en RSCcPN (RSCcPN bilateral grave + CENS previa + ≥ 1 criterio adicional: T2 con eos ≥ 300/µL o IgE ≥ 100 UI/mL, EVA > 7, ≥ 2 ciclos GCO/año, asma/EREA con GCI continuado) coinciden literalmente con GEMA 5.5 Tabla 6.4.

- **Asma Grave No Controlada** — definición, diagnóstico secuencial (Fig 7.1), comorbilidades (Tabla 7.3), Azitromicina (AMAZES 500 mg × 3 sem × 48 sem), termoplastia y reducción GCO bien alineados con GEMA Cap 7. *(Solo el hallazgo de umbrales de eos en biológicos queda como 🟠).*

- **Asma - Tratamiento Escalonado** — escalones 1-5 alineados con Fig 3.2 GEMA; estrategia MART correcta. *(Solo los hallazgos 9 y 10 quedan como 🟠/🟢).*

- **Asma - Crisis Asmática** — clasificación de gravedad, magnesio 2 g IV en 20 min, prednisona 40-50 mg × 5-7 días sin pauta descendente, criterios UCI (PaCO₂ > 45 mmHg, SaO₂ < 90 % refractaria, intubación previa) bien alineados con GEMA Cap 4 Tabla 4.2-4.4. *(Solo el hallazgo 5 de salbutamol queda como 🟠).*

- **EPOC - Manejo Crónico** — clasificación ABE (Group E ≥ 1 exacerbación moderada/grave, novedad GOLD 2026 Fig 2.13 confirmada), umbrales eos ≥ 300 para iniciar triple terapia en E (línea 2710 GOLD Cap 3), criterios añadir/retirar ICS (Fig 3.10) y dupilumab/mepolizumab (Fig 3.11) bien alineados. *(Solo los hallazgos 12 y 13 quedan como 🟠/🟢).*

- **EPOC - Exacerbación y Manejo Agudo** — clasificación de Roma (Fig 4.2 GOLD: leve/moderada/severa con criterios VAS disnea, FR, FC, SaO₂, CRP, gasometría) reproducida correctamente; antibioterapia con criterios "≥ 2 de 4 síntomas, uno purulencia" alineada con GOLD 2026 Cap 4 §Antibiotics (p.104, línea 2380 extracto); prednisona 40 mg × 5 d alineada (línea 2219 GOLD); Vit D < 10 ng/ml o < 25 nM con suplementación coincide con GOLD Cap 5 (p.100, línea 11479 extracto completo). *(Solo el hallazgo 14 HFNT queda como 🟠).*

- **EPOC reagudizado** — índice/hub correcto. *(Solo el hallazgo 15 HFNT queda como 🟠).*

---

## Notas sobre fuentes y limitaciones

- **GEMA 5.5 (2025)**: revisado capítulos 1 (IPA, Tabla 1.11), 2 (Tabla 2.6 control, Tabla 2.7 factores riesgo, ACQ cutoffs), 3 (Tabla 3.3 GCI, Fig 3.2 escalonado), 4 (Tabla 4.3 fármacos crisis, Fig 4.1-4.2 algoritmos), 5 (Tabla 5.5 GCI pediátrico, Fig 5.2 crisis pediátrica), 6 (Tabla 6.2 ARIA, Tabla 6.4 POLINA), 7 (Tabla 7.5 biológicos AGNC, §7.3 mal control AGNC, §7.4 fenotipos y eficacia biológicos).

- **GOLD 2026**: revisado capítulos 2 (assessment ABE, Fig 2.13 grupos), 3 (Fig 3.6 vacunas, Fig 3.10 indicaciones ICS, Fig 3.11 biológicos en EPOC, ensifentrine), 4 (Fig 4.2 Rome severity, §Antibiotics p.104, §HFNT/NIV p.105, Vit D p.100).

- **Manual 12 Octubre 2022 / SEPAR / IDSA-ATS**: no se ha consultado en esta auditoría para `Bronquitis Aguda`, `Broncoespasmo en IRVA` y `NAC`. Las conclusiones de esas notas se marcan como ⚪ informativo. Si el residente desea elevar la evidencia de esas notas, se requiere segunda pasada con esas fuentes.

- **Política aplicada**: se ha respetado estrictamente la regla "no incluir hallazgos sin cita literal". Los hallazgos enumerados llevan referencia a página/sección concreta de GEMA o GOLD y reproducen literalmente el texto fuente y el texto de la nota.
