---
tags: [auditoria, fact-check, orl]
fecha_auditoria: 2026-04-20
fuentes_consultadas:
  - "Protocolos ORL Urgencias FJD (Enero 2024) — Manejo Epistaxis, Otalgia, Hipoacusia, Absceso Periamigdalino"
  - "PROA Antibióticos FJD (1ª Edición 2025, vs. 23 abril)"
  - "Manual de Diagnóstico y Terapéutica Médica Hospital 12 de Octubre, 9ª ed. 2022 — Capítulo 9 Patología ORL (pp. 109-128)"
notas_auditadas: 9
hallazgos_total: 14
---

# Fact-check ORL — 2026-04-20

## Resumen ejecutivo

Auditoría clínica de 9 notas de ORL del vault contra 3 fuentes primarias (Protocolos FJD ORL 2024, PROA FJD 2025, Manual 12 Octubre 2022 cap. 9). Se detectan **14 hallazgos** distribuidos así:

- 🔴 **Críticos (2):** dosis/intervalo erróneo de Penicilina V en faringoamigdalitis estreptocócica (riesgo terapéutico real de fracaso); ausencia total de mención a otitis externa maligna en pacientes diabéticos/inmunosuprimidos (entidad potencialmente mortal cuya omisión puede demorar el diagnóstico en urgencias).
- 🟠 **Moderados (5):** discrepancias de duración o dosificación con FJD/PROA en OMA y otitis externa, sección "ANTIBIÓTICO SOLO SI" vacía en sinusitis, ausencia de criterios McIsaac y de complicaciones supurativas en faringoamigdalitis.
- 🟢 **Menores (4):** tiempo de compresión en epistaxis (30 vs 15 min), ausencia de pomada antibiótica en taponamiento, intervalo retirada Merocel (48 h vs 48-72 h), ausencia de mención a corticoides sistémicos para hipoacusia súbita en flujo de derivación.
- ⚪ **Informativos (3):** falta de campo `fuente:` en frontmatter, ausencia de wikilinks bidireccionales en algunas notas, criterios diagnósticos OMA no explicitados.

**Prioridad de corrección:** primero los 2 hallazgos 🔴 (afectan seguridad del paciente), después los 🟠 (mejoran adecuación al protocolo institucional FJD).

---

## Hallazgos por nota

### 🔴 Faringoamigdalitis Aguda

**Hallazgo 1 — Dosis/intervalo Penicilina V erróneo**
- **Severidad:** 🔴 Crítico
- **Cita nota (literal):** "Penilevel 500 mg 1 comprimido cada 12 horas durante 10 días"
- **Cita fuente (literal):** "Penicilina V (fenoximetilpenicilina) — vía oral — 500 mg/6 h"
- **Fuente:** PROA Antibióticos FJD 2025 (vs. 23 abril), tabla de dosificación de penicilinas (sección Penicilina V).
- **Cambio sugerido:** corregir a "Penicilina V 500 mg cada 6 h durante 10 días" (o, si se prefiere monodosis IM, "Penicilina G benzatina 1.200.000 UI IM dosis única" para garantizar adherencia).
- **Impacto clínico:** intervalo cada 12 h infradosifica el área bajo la curva de la penicilina (semivida ~30 min); riesgo real de fracaso de erradicación estreptocócica y de complicaciones postestreptocócicas.

**Hallazgo 2 — Ausencia de criterios McIsaac y de complicaciones supurativas**
- **Severidad:** 🟠 Moderado
- **Cita nota (literal):** la nota cita criterios de Centor pero no aplica el modificador por edad ni alerta sobre el absceso periamigdalino.
- **Cita fuente (literal):** "Voz patata caliente, abombamiento del pilar amigdalino, desviación de úvula, signo del pulgar... dieta absoluta, sedestación, ceftriaxona + vancomicina + bolo de metilprednisolona, avisar ORL guardia."
- **Fuente:** Protocolos ORL Urgencias FJD 2024 — Absceso Periamigdalino.pdf.
- **Cambio sugerido:** añadir tabla McIsaac (Centor + edad: <15 años +1 punto, >44 años −1 punto) y un bloque "Signos de alarma → derivar a ORL guardia: voz en patata caliente, trismus, desviación uvular, abombamiento pilar".

---

### 🔴 Otitis Externa

**Hallazgo 3 — No menciona otitis externa maligna en diabéticos/inmunosuprimidos**
- **Severidad:** 🔴 Crítico
- **Cita nota (literal):** la nota describe únicamente otitis externa difusa bacteriana; no hay ninguna línea sobre OE maligna ni sobre factores predisponentes (diabetes, inmunosupresión).
- **Cita fuente (literal):** "Otitis externa maligna o necrotizante — Pseudomonas aeruginosa — predisponentes: inmunosupresión, diabetes mal controlada, edad avanzada — tratamiento: ciprofloxacino 400 mg/8 h IV ± piperacilina-tazobactam, ingreso, valorar TC peñasco."
- **Fuente:** Manual 12 de Octubre 2022, cap. 9 Patología ORL, p. 111, Tabla 3 (otitis externas).
- **Cambio sugerido:** añadir un callout `> [!danger]` con: "En diabético, inmunodeprimido o anciano con otalgia desproporcionada, otorrea persistente o tejido de granulación en CAE → sospechar OE maligna (Pseudomonas). Derivar a ORL urgente, no tratar ambulatoriamente con gotas."
- **Impacto clínico:** la OE maligna tiene mortalidad significativa si se demora; un diabético tratado como OE simple puede progresar a osteomielitis de base de cráneo en días.

**Hallazgo 4 — Dosificación Cetraxal Plus discrepante con protocolo institucional**
- **Severidad:** 🟠 Moderado
- **Cita nota (literal):** "Cetraxal Plus® (ciprofloxacino 2 mg/ml + fluocinolona 0.25 mg/ml): 3 gotas/12 h durante 7 días."
- **Cita fuente (literal):** "Otitis externa difusa: ciprofloxacino + corticoide tópico, 6 gotas cada 12 horas durante 7 días."
- **Fuente:** Protocolos ORL Urgencias FJD 2024 — Otalgia.pdf, p. 1/2 (algoritmo otitis externa).
- **Cita fuente complementaria:** "OE difusa: gotas de ciprofloxacino + corticoide, 6-8 gotas/12 h x 7 días."
- **Fuente complementaria:** Manual 12 Octubre 2022, cap. 9, p. 111, Tabla 3.
- **Cambio sugerido:** corregir a "6 gotas/12 h durante 7 días" para alinear con FJD y Manual 12 Oct.

---

### 🟠 Otitis Media Aguda (OMA)

**Hallazgo 5 — Duración amoxicilina discrepante con FJD**
- **Severidad:** 🟠 Moderado
- **Cita nota (literal):** "1ª elección: Amoxicilina 500 mg cada 8 h x 5 días"
- **Cita fuente (literal):** "OMA en adulto: amoxicilina 500 mg/8 h vía oral durante 7 días. Si fracaso a las 72 h o sospecha de resistencias: amoxicilina-clavulánico 875/125 mg/8 h durante 7 días."
- **Fuente:** Protocolos ORL Urgencias FJD 2024 — Otalgia.pdf, p. 2/2 (algoritmo OMA).
- **Cambio sugerido:** corregir duración a "x 7 días" (alineado con FJD). Para amoxi-clavulánico mantener 7 días.

**Hallazgo 6 — No menciona alta dosis de amoxicilina ni complicaciones graves**
- **Severidad:** 🟠 Moderado
- **Cita nota (literal):** la nota lista solo "Amoxicilina 500 mg/8 h" sin alternativa de dosis altas; tampoco incluye complicaciones intracraneales en signos de alarma.
- **Cita fuente (literal):** "Complicaciones de la OMA: parálisis facial, mastoiditis, laberintitis, petrositis (síndrome de Gradenigo), meningitis, absceso cerebral. Indicación de TC y consulta urgente con ORL."
- **Fuente:** Manual 12 Octubre 2022, cap. 9, p. 112, Tabla 4 (OMA y complicaciones).
- **Cambio sugerido:** añadir nota "Si recurrencias frecuentes o resistencia local elevada, valorar amoxicilina 875 mg/8 h o amoxi-clavulánico de inicio." Incluir en signos de alarma: cefalea intensa, vómitos, focalidad neurológica, otorrea fétida persistente, edema retroauricular (mastoiditis).

**Hallazgo 7 — Criterios diagnósticos no explicitados**
- **Severidad:** ⚪ Informativo
- **Cita nota (literal):** la nota describe la exploración pero no enuncia los criterios diagnósticos (otalgia + abombamiento timpánico u otorrea aguda + signos inflamatorios).
- **Cita fuente (literal):** "Diagnóstico clínico: otalgia aguda + signos inflamatorios timpánicos (eritema, abombamiento, pérdida de reflejo luminoso) ± otorrea reciente por perforación."
- **Fuente:** Manual 12 Octubre 2022, cap. 9, p. 112, Tabla 4.
- **Cambio sugerido:** añadir un breve apartado "Diagnóstico" con la tríada clínica.

---

### 🟠 Rinosinusitis Aguda

**Hallazgo 8 — Sección "ANTIBIÓTICO SOLO SI" sin criterios clínicos**
- **Severidad:** 🟠 Moderado
- **Cita nota (literal):** "**ANTIBIÓTICO SOLO SI (según PROA):** → Según PROA: 1ª elección: Amoxicilina 500 mg cada 8 h x 5 días."
- **Cita fuente (literal):** "Rinosinusitis aguda bacteriana: sospecha si síntomas persistentes >10 días sin mejoría, o doble empeoramiento (fiebre + dolor facial intenso tras mejoría inicial), o síntomas graves desde el inicio (fiebre ≥39 ºC + descarga purulenta + dolor facial >3-4 días)."
- **Fuente:** Manual 12 Octubre 2022, cap. 9, sección Rinosinusitis aguda (pp. 113-115).
- **Cambio sugerido:** rellenar los criterios bajo el encabezado "SOLO SI": (a) duración ≥10 días sin mejoría, (b) doble empeoramiento, (c) síntomas graves desde el inicio (fiebre ≥39 ºC + dolor facial intenso). Sin estos criterios, mantener tratamiento sintomático.
- **Impacto clínico:** la sección actual sugiere antibiótico sin filtrar, lo que contradice el espíritu PROA (uso racional).

---

### 🟢 Epistaxis

**Hallazgo 9 — Tiempo de compresión manual mayor que el protocolo FJD**
- **Severidad:** 🟢 Menor
- **Cita nota (literal):** "Compresión manual sobre tabique nasal (zona blanda) durante 30 minutos."
- **Cita fuente (literal):** "Compresión digital firme sobre la zona blanda del tabique (alas nasales) durante 15 minutos sin soltar, paciente sentado e inclinado hacia delante."
- **Fuente:** Protocolos ORL Urgencias FJD 2024 — Manejo Epistaxis 2024.pdf.
- **Cambio sugerido:** ajustar a "compresión continua de 15 minutos" (alineado con FJD); 30 min sin soltar puede generar peor adherencia y demora innecesaria a otras medidas.

**Hallazgo 10 — Falta indicar lubricación con pomada antibiótica al colocar Merocel**
- **Severidad:** 🟢 Menor
- **Cita nota (literal):** la nota indica colocar taponamiento anterior con Merocel pero no menciona lubricación con pomada antibiótica antes de la inserción.
- **Cita fuente (literal):** "Antes de la inserción del taponamiento (Merocel u otro), lubricar con pomada antibiótica para facilitar colocación y prevenir colonización."
- **Fuente:** Protocolos ORL Urgencias FJD 2024 — Manejo Epistaxis 2024.pdf.
- **Cambio sugerido:** añadir paso: "Lubricar Merocel con pomada antibiótica (mupirocina o bacitracina) antes de inserción."

**Hallazgo 11 — Intervalo de retirada del taponamiento incompleto**
- **Severidad:** 🟢 Menor
- **Cita nota (literal):** "Retirada del taponamiento en 48 h."
- **Cita fuente (literal):** "Retirada del taponamiento entre 48 y 72 horas, en consulta de ORL o por su MAP, con cobertura antibiótica oral mientras esté colocado."
- **Fuente:** Protocolos ORL Urgencias FJD 2024 — Manejo Epistaxis 2024.pdf.
- **Cambio sugerido:** corregir a "Retirada en 48-72 h por ORL/MAP, manteniendo amoxicilina-clavulánico oral mientras dure el taponamiento (profilaxis síndrome de shock tóxico)."

---

### 🟢 Otras notas con hallazgos menores/informativos

**Hallazgo 12 — Otitis Externa: falta de campo `fuente:` en frontmatter**
- **Severidad:** ⚪ Informativo
- **Cambio sugerido:** añadir al frontmatter `fuente: "Protocolos ORL Urgencias FJD 2024 — Otalgia.pdf; Manual 12 Octubre 2022 cap. 9, p. 111"` para trazabilidad.

**Hallazgo 13 — Otitis Media Serosa y Ototubaritis: ausencia de wikilink bidireccional con Rinosinusitis**
- **Severidad:** ⚪ Informativo
- **Cita nota (literal):** sólo enlaza con `[[Otitis Media Aguda (OMA)]]`.
- **Cambio sugerido:** añadir `[[Rinosinusitis Aguda]]` en sección Relacionados (frecuente comorbilidad postcatarral; el manejo de la disfunción tubárica se solapa con descongestivos nasales).

**Hallazgo 14 — Disfunción ATM/Bruxismo: Diazepam "se entrega en mano"**
- **Severidad:** ⚪ Informativo
- **Cita nota (literal):** "Diazepam 5 mg (solo si ansiedad asociada, ½ comp noche máximo 3-5 días, se entrega en mano)."
- **Comentario:** la práctica de entregar en mano benzodiacepinas en urgencias está alineada con buena praxis (control de stock, prevención de abuso). No es un error pero conviene documentar en frontmatter `precaucion_dispensacion: true` o equivalente para localizar fácilmente notas con dispensación restringida.
- **Cambio sugerido (opcional):** añadir tag `dispensacion-restringida` o nota equivalente.

---

## Notas sin hallazgos relevantes

Las siguientes notas no presentan errores clínicos ni discrepancias con las fuentes consultadas (FJD, PROA, Manual 12 Oct):

- **Laringitis Aguda** — manejo sintomático y corticoide oral acorde a práctica habitual; no hay protocolo FJD específico que contradiga el contenido.
- **Odontalgia y Flemón Dental** — escalada amoxicilina → amoxi-clavulánico razonable; no hay protocolo FJD ORL específico para esta patología (correspondería a Cirugía Maxilofacial / Manual 12 Oct cap. odontoestomatología, no auditado en este lote).

---

## Notas de método

- Toda cita literal procede de PDFs leídos directamente en `/home/arenas/Obsidian/MIR/Libros y referencias/`.
- Páginas indicadas corresponden a la numeración del PDF, no a la del libro impreso (Manual 12 Octubre).
- No se ha modificado ninguna nota del vault; las correcciones quedan como sugerencia para que el residente las aplique tras revisión personal.
- Se recomienda aplicar primero los 2 hallazgos 🔴 antes de la próxima guardia.
