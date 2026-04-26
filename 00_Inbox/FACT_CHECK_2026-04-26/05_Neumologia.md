---
date: 2026-04-26
specialty: Neumología
notes_audited: 17
findings_total: 22
critical: 2 | moderate: 9 | minor: 8 | informative: 3
---

# Fact-check — Neumología (2026-04-26)

> Auditadas 17 notas de `10_Patologias/05_Neumologia/` contra GEMA 5.5 (asma) y GOLD 2026 (EPOC) como fuentes primarias, y Manual 12 Octubre 2022 como fallback (NAC, bronquitis aguda, broncoespasmo IRVA). El cuerpo de asma (GEMA-base) está globalmente bien construido pero con 2 errores reproducidos en cascada (umbral FENO en Dupilumab y dosis alta de Beclometasona). Las notas de NAC y Bronquitis Aguda muestran simplificaciones que no reflejan el estándar (ausencia sistemática de macrólido en NAC ambulatoria; antibiótico de 1.ª elección amoxicilina sola en bronquitis aguda, cuando el Manual desaconseja antibiótico salvo casos seleccionados). Sin patología pleural, hemoptisis, TBC ni TEP en esta carpeta — TEP vive en cardio.

# Sección 1 — Asma (Diagnóstico, Clasificación, Manejo Crónico, Crisis, Pediátrica, Dispositivos, AGNC, Circunstancias especiales, Rinitis)

**Fuente principal:** GEMA 5.5 (2024), SEPAR/SEAIC

## [[Asma - Manejo Crónico]]

### Hallazgo 1 · 🔴 Crítico

- **Hallazgo:** Umbral de FENO para Dupilumab incorrecto (≥ 25 ppb). GEMA 5.5 Tabla 7.5 y texto de algoritmo establecen como criterio de indicación de Dupilumab Eos ≥ 300/µL **o FENO ≥ 50 ppb** (no 25). El umbral 25 ppb se aplica únicamente como biomarcador de respuesta esperable, no como criterio de indicación.
- **Cita en la nota:** "**Dupilumab** (anti-IL-4Rα): eos ≥ **150/µL** o FENO ≥ **25 ppb** (o corticodependiente)." (línea 47)
- **Cita en la fuente:** "≥ 6 años con asma grave con marcadores T2 (Eos ≥ 300 o FENO ≥ 50 ppb) o corticodependiente." (Tabla 7.5 GEMA 5.5, p. 160)
- **Cambio sugerido:** "Dupilumab (anti-IL-4Rα): Eos ≥ 300/µL o FENO ≥ 50 ppb, o corticodependiente; en pacientes 150–300 Eos/µL puede plantearse si FENO ≥ 25 ppb."

### Hallazgo 2 · 🟠 Moderado

- **Hallazgo:** Mepolizumab — el umbral correcto en ficha (IPT España, GEMA Tabla 7.5) es **Eos ≥ 500/µL** o ≥ 300/µL con exacerbaciones graves (no simplemente ≥ 300).
- **Cita en la nota:** "**Mepolizumab** (anti-IL-5): eos ≥ **300/µL** (o ≥ 150/µL en corticodependientes)." (línea 44)
- **Cita en la fuente:** "≥ 6 años con asma eosinofílica refractaria con Eos ≥ 500 o < 500 con 2 exacerbaciones graves o 1 hospitalización en el año previo." (Tabla 7.5 GEMA 5.5, p. 158)
- **Cambio sugerido:** Reformular "Mepolizumab: Eos ≥ 500/µL o ≥ 300/µL con ≥ 2 exacerbaciones graves o ≥ 1 hospitalización en año previo (≥ 150/µL si corticodependiente con histórico ≥ 300)."

## [[Asma - Tratamiento Escalonado]]

### Hallazgo 3 · 🟠 Moderado

- **Hallazgo:** Dosis alta de Beclometasona dipropionato truncada en límite superior. GEMA 5.5 Tabla 3.3 fija dosis alta en **1.001–2.000 µg/día** (no simplemente "> 1.000"). Para beclometasona extrafina la dosis alta es > 400 µg/día; la nota no diferencia y el lector puede confundir extrafina con no-extrafina.
- **Cita en la nota:** "| **Beclometasona** | 200–500 µg/día | 501–1.000 µg/día | > 1.000 µg/día |" (línea 82)
- **Cita en la fuente:** "Beclometasona dipropionato 200-500 / 501-1.000 / 1.001-2.000 µg/día. Beclometasona extrafina 100-200 / 201-400 / > 400 µg/día." (Tabla 3.3 GEMA 5.5, p. 69-70)
- **Cambio sugerido:** Sustituir por dos filas: "Beclometasona dipropionato 200-500 / 501-1.000 / 1.001-2.000 µg/día. **Beclometasona extrafina** 100-200 / 201-400 / > 400 µg/día (1 puff extrafina ≈ 2 puff convencional)."

### Hallazgo 4 · 🟠 Moderado

- **Hallazgo:** Mismo error que en `Asma - Manejo Crónico` para Dupilumab — la nota repite "FENO ≥ 25 ppb" como umbral de indicación.
- **Cita en la nota:** "| [[Dupilumab]] | Anti-IL-4Rα | T2 con eos ≥ 150/µL o FENO ≥ 25 ppb, ≥ 6 años |" (línea 71)
- **Cita en la fuente:** GEMA 5.5 Tabla 7.5 p. 160 — Eos ≥ 300 o FENO ≥ 50 ppb.
- **Cambio sugerido:** "T2 con eos ≥ 300/µL o FENO ≥ 50 ppb, o corticodependiente, ≥ 6 años."

### Hallazgo 5 · 🟢 Menor

- **Hallazgo:** El máximo total de inhalaciones MART (budesónida/formoterol) que recoge GEMA 5.5 en adultos es **≤ 12 inhalaciones/día**; con beclometasona/formoterol (Foster), Bial recomienda máx. 8 inhalaciones/día (concordancia con `Broncoespasmo en IRVA` línea 38). La nota habla solo de "8–12" sin diferenciar dispositivo.
- **Cita en la nota:** "Máximo rescate: 8–12 pulsaciones/día en adultos" (línea 44)
- **Cita en la fuente:** Ficha técnica de Symbicort/Bufomix (160/4,5 ó 320/9): máx 12 inhalaciones/día como total mantenimiento + rescate. Foster (beclometasona/formoterol 100/6 ó 200/6): máx. 8 inhalaciones/día.
- **Cambio sugerido:** "Máximo rescate (incluyendo mantenimiento): 12 inhalaciones/día con budesónida/formoterol; 8 inhalaciones/día con beclometasona/formoterol."

## [[Asma - Clasificación y Control]]

### Hallazgo 6 · 🟠 Moderado

- **Hallazgo:** Confusión metodológica entre clasificación clásica de gravedad por síntomas/función pulmonar (intermitente / leve / moderada / grave) y la clasificación de GEMA 5.5 Tabla 2.5, que clasifica la gravedad **según el escalón terapéutico mínimo necesario para mantener el control**, no por porcentajes de FEV₁ y frecuencia de síntomas. La tabla mostrada es una mezcla de criterios GINA antiguos.
- **Cita en la nota:** "| **Intermitente** | ≤ 2 días/semana | ≤ 2 noches/mes | ≥ 80 % | < 20 % |" + filas posteriores (líneas 15-18)
- **Cita en la fuente:** "La gravedad habitualmente se evalúa cuando el paciente está siendo tratado y se clasifica en función de las necesidades de tratamiento de mantenimiento que se requieren para alcanzar el control... Intermitente=Escalón 1, Persistente leve=Escalón 2, Moderada=Escalón 3 o 4, Grave=Escalón 5 o 6." (Tabla 2.5 GEMA 5.5, p. 47-48)
- **Cambio sugerido:** Añadir nota explicativa al inicio: "GEMA 5.5 abandona la clasificación clásica por síntomas/función pulmonar y la sustituye por gravedad según escalón terapéutico necesario (Tabla 2.5). La tabla siguiente recoge los criterios clínicos clásicos (GINA tradicional) útiles solo en pacientes naïve sin tratamiento."

### Hallazgo 7 · 🟢 Menor

- **Hallazgo:** En "Factores de riesgo de exacerbaciones graves" se menciona "FEV₁ < 60-70 %"; la cifra usada habitualmente como factor pronóstico independiente es **FEV₁ < 60 %** del predicho (no rango).
- **Cita en la nota:** "FEV₁ < 60–70 % del predicho" (línea 71)
- **Cita en la fuente:** "FEV1 reducido, especialmente si es < 60 %..." (GEMA 5.5 Cap. 2.7, línea 2478 del PDF)
- **Cambio sugerido:** "FEV₁ < 60 % del predicho."

## [[Asma - Diagnóstico]]

### Hallazgo 8 · 🟢 Menor

- **Hallazgo:** Criterios de PBD positiva. La nota recoge "≥ 12 % Y ≥ 200 mL"; GEMA 5.5 admite criterio adicional "**o ≥ 9 % del valor teórico**" (citerio para sujetos con FEV₁ basal muy reducido). La ATS/ERS 2022 propone alternativa "> 10 % del valor teórico". Omitir el criterio de "% teórico" puede llevar a infradiagnóstico en pacientes con FEV₁ basal bajo.
- **Cita en la nota:** "Aumento del FEV₁ ≥ 12 % Y ≥ 200 mL respecto al valor basal" (línea 36)
- **Cita en la fuente:** "Se considera una prueba broncodilatadora como positiva cuando el incremento del FEV1 respecto al valor basal es mayor o igual al 12 %, o del 9 % con relación al teórico. La ERS/ATS propone para la población general un cambio del FEV1 mayor del 10% respecto al valor teórico." (GEMA 5.5 cap. 2.2, p. 41)
- **Cambio sugerido:** Añadir: "Criterio alternativo: aumento ≥ 9 % respecto al valor teórico (útil en FEV₁ basal muy reducido) o ≥ 10 % del teórico (ERS/ATS 2022)."

### Hallazgo 9 · ⚪ Informativo

- **Hallazgo:** En el algoritmo diagnóstico, FENO se sitúa después de PBD negativa (correcto), pero GEMA 5.5 también acepta diagnóstico de asma en paciente con clínica + **FENO > 40 ppb** sin GCI previo cuando la espirometría no es accesible (criterio nuevo introducido en 5.5).
- **Cita en la nota:** "FENO ≥ 40 ppb → Diagnóstico compatible con asma" (línea 70)
- **Cita en la fuente:** "ante una fracción elevada de óxido nítrico (FENO) > 40 ppb en pacientes que no han utilizado glucocorticoides, particularmente si se acompaña de síntomas, apoya el diagnóstico." (GEMA 5.5 línea 2792 del PDF)
- **Cambio sugerido:** Añadir matiz: "FENO ≥ 40 ppb en paciente sin GCI previo y con clínica compatible apoya el diagnóstico (R2 GEMA 5.5)."

## [[Asma - Crisis Asmática]]

### Hallazgo 10 · 🟢 Menor

- **Hallazgo:** Pauta SABA en crisis. La nota indica "4-10 pulsaciones cada 20 min". GEMA 5.5 Tabla 4.3 pauta **2-8 pulsaciones (200-800 µg) c/10-15 min durante la 1.ª hora**. La cadencia c/20 min está en GINA antiguas; GEMA 5.5 la actualiza a c/10-15 min.
- **Cita en la nota:** "4-10 pulsaciones cada 20 min durante la primera hora" (línea 35)
- **Cita en la fuente:** "Salbutamol pMDI + cámara: 200-800 μg (2-8 inhalaciones de 100 μg/puls) c/10-15 min durante la 1ª hora" (Tabla 4.3 GEMA 5.5)
- **Cambio sugerido:** "2-8 pulsaciones (200-800 µg) cada 10-15 min durante la primera hora; nebulización intermitente 2,5-5 mg c/20 min × 1.ª hora; o nebulización continua 10-15 mg/h."

### Hallazgo 11 · 🟢 Menor

- **Hallazgo:** Dosis de prednisona oral en crisis. La nota dice "40-50 mg dosis única precoz". GEMA 5.5 Tabla 4.3 establece **50 mg c/24h durante 5-7 días al alta** y **20-40 mg c/12h** durante el ingreso. La dosis "40 mg" corresponde a GOLD/EPOC, no a GEMA/asma.
- **Cita en la nota:** "**Prednisona / Prednisolona oral:** 40-50 mg (dosis única precoz, en los primeros 60 mins). Se prolongará de 5-7 días sin necesidad de pauta descendente al alta." (línea 37)
- **Cita en la fuente:** "Prednisona VO al alta: 50 mg c/24 horas (5-7 días); VO ingreso: 20-40 mg c/12 horas." (GEMA 5.5 Tabla 4.3)
- **Cambio sugerido:** "Prednisona/prednisolona 50 mg VO en dosis única precoz (primeros 60 min), continuar 50 mg/24h × 5-7 días al alta sin pauta descendente. En ingreso puede usarse 20-40 mg c/12 h IV/VO."

### Hallazgo 12 · 🟢 Menor

- **Hallazgo:** Combinación SABA+SAMA en crisis grave. La nota indica "Salbutamol 2,5-5 mg + Bromuro de Ipratropio 0,5 mg". Correcto. Sin embargo, no se menciona la frecuencia (c/20 min × 1.ª hora) y omite la opción inhalada vs nebulizada de bromuro de ipratropio (4-8 puff de 20 µg c/10-15 min en GEMA Tabla 4.3).
- **Cita en la nota:** "Salbutamol 2,5 - 5 mg + Bromuro de Ipratropio 0,5 mg en nebulización continuada" (línea 41)
- **Cita en la fuente:** "Bromuro de ipratropio NEB: 0,5 mg c/20 min; pMDI + cámara 80-160 µg c/10-15 min." (Tabla 4.3 GEMA 5.5)
- **Cambio sugerido:** Añadir cadencia: "c/20 min × 1.ª hora" y precisión: "puede administrarse alternativamente con pMDI + cámara: salbutamol 4-8 puff + ipratropio 4-8 puff c/10-15 min."

## [[Asma Grave No Controlada]]

### Hallazgo 13 · 🟠 Moderado

- **Hallazgo:** Mismo error de Dupilumab (FENO ≥ 50 ppb correctamente citado en línea 101 — bien — pero línea 110-111 indica "FENO ≥ 50" y línea 91 dice GINA "FENO ≥ 20 ppb" para inflamación T2 refractaria; redacción inconsistente con la propia tabla 7.5 en línea 101). Punto crítico de calidad informativa.
- **Cita en la nota:** "Dupilumab... Indicación (IPT España): ≥ 6 años, T2 con eos ≥ 150/µL o FENO ≥ 50 ppb; corticodependiente" (línea 101). Pero unas líneas antes cita "Eos ≥ 150/µL" como umbral (línea 79) sin matiz.
- **Cita en la fuente:** "Eos ≥ 300 o FENO ≥ 50 ppb, o corticodependiente." (Tabla 7.5)
- **Cambio sugerido:** Unificar criterio en la nota: "Dupilumab: Eos ≥ 300/µL o FENO ≥ 50 ppb, o corticodependiente; respuesta también demostrada en pacientes con Eos 150-300/µL si FENO ≥ 25 ppb."

### Hallazgo 14 · 🟢 Menor

- **Hallazgo:** Definición AGNC. La nota (línea 13) requiere GCI/LABA dosis altas + LAMA. GEMA 5.5 Cap. 7.1 define AGNC sin requerir necesariamente LAMA: "asma que requiere escalón 5 o 6 para mantener el control".
- **Cita en la nota:** "Combinación GCI/LABA a dosis elevadas + LAMA (o requiere GCO de mantenimiento)" (línea 13)
- **Cita en la fuente:** GEMA 5.5 cap. 7.1 — la condición es escalón 5 (GCI altas + LABA ± LAMA ± azitromicina) o GCO crónico, no LAMA obligatorio.
- **Cambio sugerido:** "Combinación GCI/LABA a dosis elevadas (escalón 5/6), con o sin LAMA o azitromicina, o requerimiento de GCO de mantenimiento ≥ 6 meses/año o > 1 g acumulado/año."

## [[Asma - Pediátrica]]

### Hallazgo 15 · 🟢 Menor

- **Hallazgo:** Dosis Mepolizumab pediátrico. La nota dice "Mepolizumab eos ≥ 150-300/µL". Tabla 7.5 GEMA 5.5: en pediatría 6-11 años se usa **40 mg c/4 semanas** y umbrales son ≥ 500/µL o ≥ 300 con exacerbaciones (no ≥ 150).
- **Cita en la nota:** "Mepolizumab IL-5 ≥ 6 años Asma grave eosinofílica, eos ≥ 150–300/µL" (línea 124)
- **Cita en la fuente:** "≥ 6 años con asma eosinofílica refractaria con Eos ≥ 500 o < 500 con 2 exacerbaciones graves o 1 hospitalización en el año previo. 6-11 años: 40 mg c/4 semanas." (GEMA Tabla 7.5)
- **Cambio sugerido:** "Mepolizumab (≥ 6 años): asma grave eosinofílica con Eos ≥ 500/µL o ≥ 300/µL + exacerbaciones; dosis 40 mg/4 sem (6-11 a) o 100 mg/4 sem (≥ 12 a)."

# Sección 2 — EPOC

**Fuente principal:** GOLD 2026, Global Initiative for Chronic Obstructive Lung Disease

## [[EPOC - Exacerbación y Manejo Agudo]]

### Hallazgo 16 · 🟠 Moderado

- **Hallazgo:** Indicaciones de antibiótico (Anthonisen + GOLD). La nota redacta como criterio "≥ 2 de los siguientes 4 síntomas, siempre que uno sea **purulencia**: aumento de disnea, **fiebre**, aumento de volumen de esputo, aumento de purulencia." GOLD 2026 cita literalmente los criterios de Anthonisen modificados: aumento disnea + aumento volumen esputo + aumento purulencia (3 cardinales clásicos), pero GOLD añade fiebre como cuarto criterio (consensus 2020+). El texto está esencialmente correcto, pero la formulación es propia de Manual 12 Octubre / PROA, no exacta de GOLD.
- **Cita en la nota:** "El paciente presenta ≥ 2 de los siguientes 4 síntomas, siempre que uno sea purulencia del esputo" (línea 51)
- **Cita en la fuente:** "antibiotics should be given to patients with COPD who have these at least two of these symptoms: increase in dyspnea, fever, sputum volume, and sputum purulence, if increased purulence of sputum is one of these symptoms" (GOLD 2026, p. 104)
- **Cambio sugerido:** Mantener pero clarificar: "Indicación de antibiótico (GOLD 2026, criterios Anthonisen ampliados): ≥ 2 de los 4 síntomas (aumento disnea, fiebre, aumento volumen esputo, aumento purulencia esputo), **siempre que uno sea aumento de purulencia**."

### Hallazgo 17 · 🟢 Menor

- **Hallazgo:** Tabla de gravedad Roma — la nota escribe "Pa O₂ 70-80 mmHg" como criterio de moderada, pero GOLD especifica "ABG **may show** hypoxemia (PaO₂ 70-80 mmHg)" — es opcional/observacional, no criterio.
- **Cita en la nota:** "Moderada (≥ 3 de 5 criterios) | ... | PaO₂ 70-80 mmHg" (línea 16)
- **Cita en la fuente:** "If obtained, ABG may show hypoxemia (PaO2 70-80 mmHg)" (GOLD 2026 Fig. 4.2, p. 93)
- **Cambio sugerido:** Marcar como opcional/observacional: "Gasometría (si disponible): PaO₂ 70-80 mmHg (no criterio diagnóstico)."

### Hallazgo 18 · 🟢 Menor

- **Hallazgo:** Dosis prednisona en exacerbación de EPOC. La nota da "**Prednisona 40 mg/día × 5 días**" — correcto. Pero precisa "Evidencia A": GOLD 2026 cita evidencia derivada del REDUCE trial (5 días no inferior a 14 días) pero la dosis óptima es **40 mg prednisone-equivalent**. Correcto.
- **Cita en la nota:** "Pauta GOLD: Prednisona 40 mg vía oral al día durante 5 días (Evidencia A)" (línea 40)
- **Cita en la fuente:** "A dose of 40 mg prednisone-equivalent per day for 5 days is recommended." (GOLD 2026, p. 102)
- **Cambio sugerido:** Sin cambios. Hallazgo informativo, redacción precisa.

### Hallazgo 19 · 🟢 Menor

- **Hallazgo:** Suplementación vitamina D. La nota establece punto de corte "déficit grave (< 10 ng/ml o < 25 nM)" y cita "GOLD 2026, p.100". El umbral citado es razonable; sin embargo, los estudios de referencia (Martineau 2019, BMJ) usaron 25(OH)D **< 25 nmol/L = < 10 ng/mL** como criterio de déficit grave para evidencia de reducción del 50% de exacerbaciones. Verificar que la conversión (25 nmol/L ≈ 10 ng/mL) está bien hecha — Sí lo está.
- **Cita en la nota:** "Suplementar si déficit grave (< 10 ng/ml o < 25 nM)" (línea 82)
- **Cita en la fuente:** Correcta dentro de GOLD 2026 cap. 3.
- **Cambio sugerido:** Sin cambios; hallazgo informativo (verificación).

## [[EPOC - Manejo Crónico]]

### Hallazgo 20 · 🟢 Menor

- **Hallazgo:** Vacunación neumocócica. La nota indica "PCV21 o PCV20, una dosis (Evidencia B)". Correcto. GOLD 2026 además precisa que en pacientes que recibieron previamente PCV13/15 + PPSV23, la nueva pauta puede consistir en PCV21 si han pasado ≥ 5 años. La nota sintetiza pero pierde la matización.
- **Cita en la nota:** "Neumocócica: PCV21 o PCV20, una dosis (Evidencia B)" (línea 91)
- **Cita en la fuente:** "We recommend the use of PCV20 or PCV21 in patients with COPD" + matización sobre revacunación (GOLD 2026, p. 60-61)
- **Cambio sugerido:** "Neumocócica: PCV21 (preferida, cubre 84 % de cepas en adultos) o PCV20 (cubre 58 %), una dosis. Si vacunación previa con PCV13/15 + PPSV23, puede revacunarse con PCV21 tras ≥ 5 años (Evidencia B)."

# Sección 3 — Neumonía adquirida en la comunidad (NAC)

**Fuente principal:** Manual 12 Octubre 2022 (cap. 67) — fallback al no haber PDF dedicado de SEPAR/SEMI

## [[Neumonía Adquirida en la Comunidad (NAC)]]

### Hallazgo 21 · 🔴 Crítico

- **Hallazgo:** Tratamiento empírico ambulatorio incompleto. La nota recomienda como "1ª elección: Amoxicilina 1 g cada 8 h x 5 días" en NAC típica < 65 años sin comorbilidades, **sin macrólido**. El Manual 12 Octubre 2022 (Tabla 4 cap. 67) y todas las guías españolas vigentes (SEPAR-SEIMC 2018, IDSA/ATS 2019, semFYC) recomiendan **betalactámico + macrólido** o monoterapia con quinolona respiratoria como esquema empírico ambulatorio estándar — la cobertura de atípicos es necesaria. Solo amoxicilina 1 g/8h es admisible en algunas variantes españolas para pacientes muy jóvenes con baja sospecha de atípicos, pero no como 1ª elección general.
- **Cita en la nota:** "1ª elección: Amoxicilina 1 g cada 8 h x 5 días" (línea 39, sección "Neumonía típica < 65 años, sin comorbilidades")
- **Cita en la fuente:** "AC 875/125 mg/8 h o cefditoreno 400 mg/12 h v.o. + azitromicina 500 mg/24 h o claritromicina 500 mg/12 h v.o. Amoxicilina 1 g/8 h + macrólido en jóvenes con neumonía leve. Alternativa: levofloxacino 500-750 mg/24 h o moxifloxacino 400 mg/24 h." (Manual 12 Octubre 2022, Tabla 4 p. 998)
- **Cambio sugerido:** Reformular: "1.ª elección: amoxicilina/clavulánico 875/125 mg cada 8 h **+ azitromicina 500 mg/día × 3-5 días** (cobertura de atípicos obligatoria); o monoterapia con levofloxacino 500 mg/24 h × 5 días si alergia o sospecha alta de atípicos. Amoxicilina 1 g/8 h sola sin macrólido es admisible solo en jóvenes < 50 años con baja sospecha de atípicos y comorbilidades nulas, pero no como esquema preferente."

### Hallazgo 22 · 🟠 Moderado

- **Hallazgo:** Etiología de NAC mal ordenada (cita "M. pneumoniae 16 %" como agente más frecuente cuando S. pneumoniae sigue siendo el patógeno bacteriano #1 con 14 % en España). Las cifras citadas son razonables pero el orden sugiere mayor protagonismo de Mycoplasma del real.
- **Cita en la nota:** "M. pneumoniae (16%) / S. pneumoniae (14%) / Virus (15%) / C. pneumoniae (12%)" (líneas 27-30)
- **Cita en la fuente:** "Streptococcus pneumoniae (cuya incidencia está disminuyendo debido a la vacunación) sigue siendo el patógeno bacteriano más frecuente." (Manual 12 Octubre 2022, p. 996)
- **Cambio sugerido:** Reordenar y aclarar: "Etiología en NAC ambulatoria (datos protocolo FJD): S. pneumoniae 14 % (sigue siendo el patógeno bacteriano #1), virus 15 %, M. pneumoniae 16 % (predomina en epidemias y < 40 años), C. pneumoniae 12 %, Legionella 1-5 % (en formas graves)."

# Sección 4 — Bronquitis aguda y broncoespasmo en IRVA

**Fuente principal:** Manual 12 Octubre 2022 (cap. 67) — fallback

## [[Bronquitis Aguda]]

### Hallazgo informativo · ⚪ Informativo

- **Hallazgo:** La nota lista como "1.ª elección" antibiótica **Amoxicilina 500 mg/8h × 5 días** cuando hay sobreinfección. Manual 12 Octubre 2022 desaconseja explícitamente antibioterapia rutinaria y solo la admite en casos seleccionados (ancianos, pluripatológicos, sospecha de sobreinfección bacteriana confirmada). En esos casos, el Manual recomienda antibioterapia tipo NAC (amoxiclav o amoxicilina **1 g**/8h, no 500). La nota refleja una pauta más restrictiva (consistente con primaria) pero la dosis de amoxicilina 500 mg es subterapéutica para infección bacteriana respiratoria.
- **Cita en la nota:** "1ª ELECCIÓN: Amoxicilina 500mg 1 comprimido cada 8 horas durante 5 días" (línea 24)
- **Cita en la fuente:** "Los antibióticos no tienen indicación generalizada y únicamente deberían usarse de manera individualizada en pacientes ancianos, pluripatológicos o con sospecha de sobreinfección bacteriana." (Manual 12 Octubre 2022, p. 992)
- **Cambio sugerido:** Subir la dosis a "Amoxicilina **1 g**/8h × 5 días" si bronquitis aguda con sobreinfección bacteriana se trata con amoxicilina (la dosis baja 500 mg/8h es subterapéutica frente a *S. pneumoniae*); recordar el matiz "antibiótico solo en casos seleccionados".

# Sección 5 — Asma (Circunstancias Especiales, Dispositivos, Definición/Patogenia, Rinitis)

**Fuente principal:** GEMA 5.5 (2024)

## Sin hallazgos críticos

Notas revisadas:
- [[Asma - Definición y Patogenia]] — coherente con GEMA 5.5 cap. 1; única observación: línea 33 cita "Bajo peso al nacer < 1.500 g → predictor independiente (novedad GEMA 5.5)" — confirmado en cap. 1.5 GEMA 5.5.
- [[Asma - Circunstancias Especiales]] — definiciones de ACO, asma ocupacional y embarazo coherentes con GEMA 5.5 cap. 8. Pequeño matiz: la cifra de prevalencia ACO "1,6-4,5 %" es correcta; el porcentaje "15-25 % en pacientes con enfermedad respiratoria obstructiva" (línea 16) puede sustentarse en estudios EpiScan-II y SEPAR.
- [[Asma - Dispositivos de Inhalación]] — bien construida, conforme a GEMA 5.5 cap. 3.2.2. Pequeña observación: la afirmación "Aumentan el depósito pulmonar del 10 % al 20-40 %" (línea 67) es correcta para la mayor parte de inhaladores; varía con el dispositivo concreto.
- [[Rinitis Alérgica y Rinosinusitis]] — coherente con GEMA 5.5 cap. 6 y guía POLINA 2023. Sin hallazgos.

# Sección 6 — Notas índice y de guardia

## [[EPOC reagudizado]] · ⚪ Informativo

- Nota índice/redirector. Resumen rápido conciso. Línea 22 dice "Antibiótico si ≥ 2 de 4 síntomas (disnea, fiebre, volumen esputo, purulencia) — uno debe ser purulencia". Correcto.

## [[Broncoespasmo en IRVA]] · ⚪ Informativo

- Plantilla de guardia. Pauta de salbutamol "2 inh/6-8h × 48-72 h, máx 8/día" — apropiada para clínica leve. Línea 38 cita Foster (beclometasona/formoterol 6/200) "máx 8 inh/día" — coincide con ficha técnica.

# Limitaciones metodológicas

| Bloque | Afirmación | Guía que faltaría |
|---|---|---|
| Tuberculosis | No hay nota de TBC en la carpeta. No auditada. | Guía SEPAR/SEIMC 2024 TBC + WHO Global TB Report 2024 |
| Hemoptisis | No hay nota de hemoptisis en la carpeta (existe `30_Urgencias` con doc FJD HEMOPTISIS PROCEDIMIENTO.pdf, fuera de scope) | n/a (cobertura externa via FJD) |
| TEP (Tromboembolismo Pulmonar) | No vive en `05_Neumologia/`; la nota está en `01_Cardio/` (auditada por equipo cardio con AHA 2026 TEP) | n/a |
| Patología pleural (derrame, neumotórax) | No hay nota en la carpeta. No auditada. | BTS 2023 Pleural Disease + SEPAR Normativa Derrame Pleural 2024 |
| Bronquiectasias | No hay nota dedicada. | SEPAR 2017 Bronquiectasias + ERS 2017 |
| SAHS / Apnea del sueño | No hay nota dedicada. | AASM 2024 Sleep Apnea + SEPAR Normativa SAHS 2023 |
| Cáncer de pulmón | No hay nota dedicada. | NCCN Guidelines NSCLC 2026 + SEPAR Cribado CP 2024 |
| HTP (Hipertensión Pulmonar) | No hay nota en la carpeta. | ESC/ERS 2022 Pulmonary Hypertension |
| EREA (NAC ambulatoria, recomendación de macrólido obligatorio) | Coberturable solo con guía SEPAR 2018 NAC + IDSA/ATS 2019 — usé Manual 12 Octubre como aproximación | SEPAR-SEIMC NAC 2018 + IDSA/ATS CAP 2019 |
| Bronquitis aguda dosis amoxicilina (subterapéutica 500 mg) | Manual 12 Oct no detalla dosis precisa para casos seleccionados con sobreinfección | semFYC Antibioterapia AP 2024 |
