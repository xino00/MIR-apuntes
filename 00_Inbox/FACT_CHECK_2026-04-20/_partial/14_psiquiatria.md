---
tags: [auditoria, fact-check, psiquiatria]
fecha_auditoria: 2026-04-20
fuentes_consultadas:
  - "Schuckit MA. Recognition and Management of Withdrawal Delirium (Delirium Tremens). N Engl J Med 2014;371:2109-13"
  - "Haber PS. Identification and Treatment of Alcohol Use Disorder. N Engl J Med 2025;392:258-66"
  - "Manual de Diagnóstico y Terapéutica Médica, Hospital 12 de Octubre, 9.ª ed. (2022), Cap. 11 (Patología psiquiátrica más frecuente), pp. 147-159"
  - "Protocolo Sujeción Física 4H-11-P1 v0 (HUFJD-HUGV-HUIE-HURJC), marzo 2022"
  - "Procedimiento Detección Sumisión Química HUFJD 9.1/P22 v0, enero 2020"
notas_auditadas: 7
hallazgos_total: 14 (0🔴 · 3🟠 · 4🟢 · 7⚪)
---

# Fact-check — Psiquiatría

Auditoría de las 7 notas de psiquiatría del vault frente a las fuentes primarias disponibles. La conclusión global es que **la mayoría del contenido de las notas es transcripción literal o muy fiel del Manual del 12 de Octubre 2022 cap. 11**, junto con extracción correcta de los dos NEJM sobre AUD y Withdrawal Delirium para la nota de Delirium Tremens. No se han encontrado errores críticos de dosis ni omisiones de seguridad inaceptables. Los hallazgos moderados se concentran en interpretación numérica imprecisa y omisiones puntuales relevantes para urgencias.

---

## Tabla de hallazgos

| # | Nota | Sev. | Resumen |
|---|---|---|---|
| 1 | Delirium Tremens | 🟠 | "Convulsiones tónico-clónicas en 3-5%" — la fuente atribuye ese 3-5% a "convulsiones, delirium o ambos", no a convulsiones aisladas |
| 2 | Delirium Tremens | 🟠 | Tabla CIWA-Ar: la nota dice "10 ítems puntuados de 0 a 7 (excepto orientación: 0-4)"; la fuente dice "Nine items scored on a scale ranging from 0 to 7 + One item scored on a scale ranging from 0 to 4" (9+1, no 10 ítems homogéneos) |
| 3 | Delirium Tremens | 🟠 | Falta mención explícita de magnesio; la fuente original (Schuckit 2014) dice expresamente que "there is little support for routine administration of magnesium" |
| 4 | Trastorno Depresivo Mayor / Intento Autolítico | 🟢 | "Citalopram/Escitalopram contraindicado en ancianos" — afirmación tomada literal del Manual H12O, pero la realidad regulatoria es **dosis máxima reducida**, no contraindicación absoluta (ver nota) |
| 5 | Agitación Psicomotriz | 🟢 | Tabla de antipsicóticos: falta la advertencia explícita de **screening de QTc previo** a haloperidol IV (recomendación general, no presente en Manual H12O cap. 11) |
| 6 | Delirium Tremens | 🟢 | Fenobarbital "Hasta 1500-2000 mg vo o IV el día 1" coincide con la fuente, pero falta la indicación de que es **alternativa o monoterapia** (la fuente lo cita en pacientes "with delirium" como dosis del día 1, no como rescate) |
| 7 | Crisis de Ansiedad | 🟢 | Diazepam: la nota redondea "vida media larga > 24 h" pero el Manual H12O nota al pie "vida media larga (> 24 h)" — coincide; sin error real, marcado para verificación |
| 8 | Intento Autolítico | ⚪ | Falta la **Columbia Suicide Severity Rating Scale (C-SSRS)** mencionada en el briefing como herramienta estándar |
| 9 | Trastorno Depresivo Mayor | ⚪ | Falta mención del **PHQ-9** como escala de cribado (mencionada en AUD review NEJM 2025 como instrumento validado de 9 ítems) |
| 10 | Agitación / Trastorno Depresivo / Psicosis | ⚪ | No se mencionan ni el **síndrome neuroléptico maligno (NMS)** ni el **síndrome serotoninérgico** entre las complicaciones graves a vigilar |
| 11 | Agitación Psicomotriz | ⚪ | El bloque "Contención mecánica" es muy escueto; existe protocolo FJD detallado (4H-11-P1) que podría enlazarse |
| 12 | Psicosis Aguda | ⚪ | No se citan dosis específicas de antipsicóticos en primer episodio (la nota redirige a Agitación, lo cual es correcto pero podría duplicar lo esencial) |
| 13 | Trastornos de Ansiedad | ⚪ | La nota es deliberadamente breve y se autodeclara "basada en fuente limitada"; no se aborda el manejo crónico (ISRS primera línea, etc.) |
| 14 | Todas | ⚪ | El campo `fuente:` del frontmatter es uniforme y correcto en las 7 notas |

---

## Hallazgos detallados

### 🟠 1. Delirium Tremens — Convulsiones "3-5%" mal atribuidas

**Nota** (`Delirium Tremens y Abstinencia Alcoholica.md`, tabla "Cronología", fila 24-48 h):

> "Convulsiones tónico-clónicas generalizadas (en 3-5% de pacientes)"

**Fuente** — Schuckit MA. *N Engl J Med* 2014;371:2109-13, p. 2109, párrafo 2 ("States of Alcohol Withdrawal — Mild and Moderate Withdrawal"):

> "About 50% of persons with alcohol-use disorders will have symptoms of alcohol withdrawal when they reduce or discontinue their alcohol consumption; **in 3 to 5% of these persons, grand mal convulsions, severe confusion (a delirium), or both develop**."

**Hallazgo:** la cifra del 3-5% en la fuente se refiere a *cualquiera* de los tres desenlaces graves (convulsiones, delirium o ambos). La nota la atribuye exclusivamente a convulsiones tónico-clónicas, lo cual subestima la prevalencia conjunta y desinforma sobre el riesgo. Sugerir reformular: *"Convulsiones tónico-clónicas, delirium o ambos: 3-5% del total de pacientes con síntomas de abstinencia"*.

---

### 🟠 2. Delirium Tremens — CIWA-Ar: estructura de ítems imprecisa

**Nota**, sección "Escala CIWA-Ar":

> "Escala de **10 ítems puntuados de 0 a 7** (excepto orientación: 0-4). Puntuación total: 0-67."

**Fuente** — Schuckit MA. *N Engl J Med* 2014;371:2109-13, Tabla 1 (p. 2110):

> "**Nine items scored on a scale ranging from 0 (no symptoms) to 7 (most severe symptoms)** [...] **One item scored on a scale ranging from 0 (no symptoms) to 4 (disoriented with respect to place or person)**"

**Hallazgo:** el resultado total (0-67) es correcto, pero la formulación "10 ítems puntuados de 0 a 7 excepto orientación" oculta la estructura real (9+1). Es un matiz pedagógico relevante porque al leer la nota se entiende que el ítem orientación es la excepción dentro de un grupo homogéneo, cuando la fuente lo presenta como categoría aparte. Es un fallo menor de transcripción; reformular como **"9 ítems de 0-7 + 1 ítem de orientación de 0-4"**.

---

### 🟠 3. Delirium Tremens — Falta postura sobre magnesio

**Nota:** no menciona magnesio en el bloque de tratamiento.

**Fuente** — Schuckit MA. *N Engl J Med* 2014;371:2109-13, p. 2111, párrafo final de "Treatment of Withdrawal Delirium":

> "Although thiamine (e.g., 500 mg infused intravenously over the course of 30 minutes once or twice daily for 3 days) and multivitamins are recommended, **there is little support for routine administration of magnesium**."

**Hallazgo:** el briefing explícitamente pide cubrir "magnesio" en el foco crítico de delirium tremens. La nota lo omite. Aunque la fuente recomienda **no** administrarlo de rutina, esa misma posición es la que hay que documentar — es información clínicamente útil porque es práctica frecuente en urgencias añadir magnesio empírico. Sugerir añadir línea: *"Magnesio: la guía Schuckit/NEJM 2014 indica que no hay soporte para administración rutinaria; reservar para hipomagnesemia documentada"*.

---

### 🟢 4. Citalopram/Escitalopram en ancianos — afirmación literal del Manual pero matizable

**Notas afectadas:** `Trastorno Depresivo Mayor.md` e `Intento Autolitico - Valoracion y Manejo.md`, ambas con la frase:

> "Contraindicado en ancianos por riesgo de aumento de QTc"

**Fuente directa de la nota** — Manual de Diagnóstico y Terapéutica Médica H12O, 9.ª ed. (2022), Cap. 11, Tabla 6 (p. 153):

> "Citalopram [...] Contraindicado en ancianos por riesgo de aumento de QTc"
> "Escitalopram [...] Contraindicado en ancianos por riesgo de aumento de QTc"

**Hallazgo:** la nota es **literalmente fiel al Manual H12O** (que es la fuente declarada en el frontmatter), por lo que técnicamente no hay error de transcripción. Sin embargo, la afirmación del Manual es una simplificación: la postura regulatoria FDA/EMA es de **dosis máxima reducida** en >60 años (citalopram 20 mg/día, escitalopram 10 mg/día), no contraindicación absoluta. Como esta auditoría no tiene acceso WebFetch a la guía FDA en este momento, **el hallazgo se mantiene como 🟢 menor**: la nota refleja correctamente su fuente y solo un comentario al margen sería útil. No requiere acción inmediata.

---

### 🟢 5. Agitación Psicomotriz — Falta recomendación de ECG/QTc previo a haloperidol IV

**Nota** (tabla de antipsicóticos, fila Haloperidol):

> "Riesgo de sintomatología extrapiramidal, **prolongación de QTc (iv y a altas dosis)**, hipotensión y ortostatismo"

**Fuente** — Manual H12O Cap. 11, Tabla 9 (p. 156):

> "Mayor riesgo de sintomatología extrapiramidal, prolongación de QTc (i.v. y a altas dosis), hipotensión y ortostatismo (sobre todo en la IC)"

**Hallazgo:** la nota es fiel a la fuente. El Manual H12O *tampoco* menciona ECG/QTc previo. En la nota solo se enumera ECG entre las pruebas iniciales ("ECG si es posible") en la tabla de pruebas complementarias. Es una limitación heredada de la fuente, no un error. Marcado como 🟢 para mejora futura: añadir nota explícita *"Realizar ECG basal antes de haloperidol IV cuando sea posible"*.

---

### 🟢 6. Delirium Tremens — Fenobarbital, contexto de uso

**Nota** (tabla "Fármacos adyuvantes"):

> "Fenobarbital — Alternativa en UCI; casos refractarios a BDZ — Hasta 1500-2000 mg vo o IV el día 1"

**Fuente** — Schuckit MA. *N Engl J Med* 2014;371:2109-13, p. 2111:

> "These agents include phenobarbital (**up to 1500 to 2000 mg administered orally or intravenously on day 1 in patients with delirium**)"

**Hallazgo:** la dosis es correcta. Sin embargo, la fuente la describe como dosis del **día 1 en pacientes con delirium ya establecido**, no específicamente como rescate ni reservada a UCI; la frase de la nota "Alternativa en UCI; casos refractarios a BDZ" añade matices no presentes en esta cita concreta (sí presentes en otras guías). Marcado 🟢 por ser ampliación razonable, pero conviene aclarar la cita.

---

### 🟢 7. Crisis de Ansiedad — Vida media de diazepam (verificación, sin error)

**Nota**, tabla de BDZ: "Diazepam — Larga (> 24 h)".

**Fuente** — Manual H12O Cap. 11, Tabla 2 (p. 151), nota al pie 3: "Vida media larga (> 24 h)".

**Hallazgo:** coincide. Sin error. Se incluye solo para confirmar verificación.

---

### ⚪ 8. Intento Autolítico — Ausencia de Columbia Suicide Severity Rating Scale

**Nota:** describe el algoritmo de exploración suicida del Manual H12O (factores de riesgo + valoración de ideas suicidas + estratificación bajo/moderado-alto), pero **no menciona la C-SSRS**.

**Comentario:** el briefing pide explícitamente cubrir Columbia. La fuente declarada (Manual H12O cap. 11) no la incluye, por lo que la omisión es coherente con la fuente. **Acción sugerida:** ampliar nota con sección "Escalas validadas: C-SSRS (Columbia)" cuando se obtenga fuente externa accesible (NICE NG225, APA Suicide Risk Assessment).

---

### ⚪ 9. Trastorno Depresivo Mayor — Falta PHQ-9

**Nota:** describe clínica DSM-style (afectiva, física, cognitiva) pero **no menciona el PHQ-9** como escala de cribado.

**Fuente externa parcial** — Haber PS. *N Engl J Med* 2025;392:258-66, p. 261:

> "It is advisable to screen patients with this disorder for suicide risk and symptoms of other mental health disorders (ideally with the use of **a validated instrument such as the nine-item Patient Health Questionnaire**), include mental health care in the management plan..."

**Comentario:** el AUD review NEJM 2025 cita el PHQ-9 como instrumento validado. La nota podría enriquecerse mencionándolo (cribado en AP, puntuación, severidad por tramos). Marcado ⚪ porque la fuente declarada no lo incluye.

---

### ⚪ 10. Agitación / Depresión / Psicosis — Falta NMS y síndrome serotoninérgico

**Notas afectadas:** `Agitacion Psicomotriz en Urgencias.md`, `Trastorno Depresivo Mayor.md`, `Psicosis Aguda y Esquizofrenia.md`.

**Comentario:** ninguna de las tres notas advierte de:
- **Síndrome neuroléptico maligno (NMS):** complicación grave de antipsicóticos (haloperidol, olanzapina, risperidona) — fiebre, rigidez, alteración consciencia, aumento CK
- **Síndrome serotoninérgico:** complicación grave de combinación de fármacos serotoninérgicos (ISRS+IMAO, ISRS+linezolid/triptanes/tramadol)

La nota Agitación enlaza a `[[Síndrome Neuroléptico Maligno]]` en sus referencias pero no lo desarrolla. Marcado ⚪ porque ambas son notas independientes que probablemente existen en el vault (verificar con `clinical-linker`).

---

### ⚪ 11. Agitación Psicomotriz — Bloque de contención mecánica muy escueto

**Nota:** el bloque "Contención mecánica" tiene solo 2 frases.

**Fuente disponible local** — Protocolo Sujeción Física HUFJD/HUGV/HUIE/HURJC 4H-11-P1 v0, marzo 2022, pp. 6-19. Cubre indicaciones (4.3, p. 7-9), contraindicaciones (4.4, p. 10), abordaje secuencial verbal→ambiental→química→mecánica (4.8, p. 13-17), reducción con 5 personas (1 por miembro + 1 cabeza, p. 15), grado mínimo de sujeción (tronco + 1 extremidad), prohibición de inmovilizar 4 extremidades en geriátrico/anciano frágil salvo excepción (p. 17).

**Comentario:** existe protocolo FJD detallado y aplicable. Sugerir crear nota propia `[[Sujeción Mecánica - Protocolo FJD]]` enlazada desde Agitación.

---

### ⚪ 12. Psicosis Aguda — No duplica dosis (correcto), pero la nota es muy breve

**Comentario:** la nota correctamente redirige a `[[Agitacion Psicomotriz en Urgencias]]` para el manejo farmacológico. No es un error. Marcado ⚪ por concisión, no por incorrección.

---

### ⚪ 13. Trastornos de Ansiedad — Autodeclarada "fuente limitada"

**Comentario:** la nota incluye un callout `[!warning] Nota basada en fuente limitada`. El manejo crónico (ISRS de primera línea, derivación a Salud Mental, terapia cognitivo-conductual) no está cubierto. Sugerir ampliar con guía NICE/APA cuando se disponga de PDF.

---

### ⚪ 14. Frontmatter — Campo `fuente:` correcto en las 7 notas

**Verificado:** las 7 notas tienen el campo `fuente:` correctamente referenciado a su PDF primario (Manual H12O cap. 11 en 6 notas; Schuckit + AUD review en Delirium Tremens). No hay wikilinks en el frontmatter (cumple regla Quartz/Obsidian del proyecto).

---

## Notas sin hallazgos significativos

Estas notas se han auditado y se confirma que **el contenido coincide fielmente con la fuente declarada (Manual H12O cap. 11, pp. 147-159)** y no presentan errores clínicos:

- ✅ `Crisis de Ansiedad.md` — tabla de BDZ idéntica a Manual H12O Tabla 2 (p. 151); tabla "Otros fármacos" idéntica a Tabla 3 (p. 151); contraindicaciones absolutas/relativas correctamente citadas
- ✅ `Trastornos de Ansiedad.md` — algoritmo coincide con Figura 1 del Manual (p. 150)
- ✅ `Psicosis Aguda y Esquizofrenia.md` — Tabla 10 (patologías orgánicas) y Tabla 11 (signos de organicidad) literales del Manual (p. 157)
- ✅ `Trastorno Depresivo Mayor.md` — Tabla 6 (antidepresivos) literal del Manual (p. 153)
- ✅ `Intento Autolitico - Valoracion y Manejo.md` — Figura 2 (algoritmo riesgo autolítico) literal del Manual (p. 152-153)
- ✅ `Agitacion Psicomotriz en Urgencias.md` — Tabla 9 (antipsicóticos) literal del Manual (p. 156); tablas 7 y 8 idem
- ✅ `Delirium Tremens y Abstinencia Alcoholica.md` — regímenes de diazepam y lorazepam literales de Schuckit Tabla 3 (p. 2112); tiamina ANTES de glucosa (advertencia presente y correcta); criterios DSM-5 de delirium tremens copiados literalmente de Tabla 2 (p. 2111)

---

## Conclusión

- **0 hallazgos críticos.** Ninguna dosis de BZD/antipsicótico es errónea, ninguna omisión grave de seguridad (la advertencia tiamina-antes-de-glucosa, el aviso olanzapina IM + BZD parenteral 1 h después, y la limitación de antipsicóticos como adyuvantes en delirium están correctamente recogidos).
- **3 hallazgos moderados** concentrados en la nota de Delirium Tremens: cifra de convulsiones mal atribuida, descripción imprecisa de la estructura CIWA-Ar, y omisión de la postura sobre magnesio.
- **4 menores** sobre matices farmacológicos (citalopram en ancianos, ECG previo a haloperidol IV, contexto de fenobarbital) y verificaciones.
- **7 informativos** sobre escalas y temas no cubiertos por la fuente primaria declarada (C-SSRS, PHQ-9, NMS, sd. serotoninérgico) que requerirían fuentes externas (APA, NICE) no auditadas en esta revisión por restricción de WebFetch.

**Recomendación priorizada:**
1. Corregir hallazgos 🟠 1, 2 y 3 en `Delirium Tremens y Abstinencia Alcoholica.md` (ediciones puntuales).
2. Crear nota `[[Sujeción Mecánica - Protocolo FJD]]` derivada del PDF 4H-11-P1.
3. Completar `Trastornos de Ansiedad.md` con manejo crónico cuando se disponga de fuente externa.

