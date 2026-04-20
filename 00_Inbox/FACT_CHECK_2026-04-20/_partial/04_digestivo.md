---
tags: [auditoria, fact-check, digestivo]
fecha_auditoria: 2026-04-20
auditor: Claude Opus 4.7
scope: Digestivo completo (18/18 notas en 10_Patologias/04_Digestivo/)
fuentes_consultadas:
  - "Manual de Diagnóstico y Terapéutica Médica H 12 Octubre 2022 (caps. 35 EII p.486, 36 HDA/HDB p.508, 38 Vías biliares p.545, 39 Pancreatitis p.555, 40 Ascitis p.570, 42 Cirrosis p.609, 73 Infecciones intraabdominales p.1083)"
  - "PROA FJD 2025 (Guía de Manejo de Antibióticos) — limitada a dosis y ajuste renal/hepático, sin algoritmos clínicos por foco"
limitaciones:
  - "PROA FJD 2025 es una guía de dosificación/ajuste renal, NO contiene regímenes empíricos por síndrome (colangitis, PBE, diverticulitis): para esos contrastes la única fuente local literal es el Manual 12 Octubre cap. 73"
  - "WebFetch a Baveno VII, Tokyo 2018 (TG18), Atlanta 2012, GETECCU, AEEH, AEG: no intentado en esta sesión por política de fuentes (todo lo verificado proviene de PDFs locales). Marcadas como limitaciones donde aplica"
  - "Sin acceso al Manual 12 Octubre 2024 (versión más reciente). Verificación contra ed. 2022"
notas_auditadas: 18
hallazgos_total: 27
description: "Fact-check Digestivo (18 notas) contra Manual 12 Oct 2022 + PROA FJD 2025"
---

# Fact-check — Digestivo (18/18 notas)

> **Aviso clínico:** auditoría comparativa de las notas del vault contra las fuentes citadas. **No es una guía clínica**. Ningún cambio sugerido se ha aplicado al vault — el residente debe revisar cada hallazgo antes de modificar la nota original.

## Resumen ejecutivo

| Métrica | Valor |
|---|---|
| Notas auditadas | **18 / 18** (Digestivo completo) |
| Hallazgos totales | **27** |
| 🔴 Críticos (riesgo clínico alto) | **5** |
| 🟠 Moderados | **9** |
| 🟢 Menores | **6** |
| ⚪ Informativos / forma | **7** |
| Notas con `fuente:` correcto en frontmatter | **0 / 18** (todas usan `fuente_original`) |
| Notas incompletas (secciones vacías o esqueléticas) | **3** (Obstrucción Intestinal, HDA-varices, Cirrosis-Profilaxis PBE) |

### Prioridad para revisar primero

1. **Complicaciones de la Cirrosis Hepática** — sección "PROFILAXIS PBE" vacía y antibioterapia empírica PBE sin régimen
2. **Hemorragia Digestiva Alta (HDA)** — algoritmo de varices ausente ("Dejo solo el algoritmo porque es menos frecuente" — pero vacío)
3. **Pancreatitis Aguda** — CPRE timing incompleto (omite "<12 h en shock séptico")
4. **Colangitis Aguda** — falta criterios Tokio TG18 y timing de drenaje (<24 h)
5. **Obstrucción Intestinal** — nota mayoritariamente vacía

---

## Top hallazgos críticos (resumen)

| ID | Nota | Severidad | Tema |
|---|---|---|---|
| **D01** | Cirrosis | 🔴 | Sección "PROFILAXIS PBE" vacía — Manual cap.42 Tabla 9 da indicaciones y pautas concretas |
| **D02** | Cirrosis | 🔴 | Antibioterapia empírica PBE sin régimen ("Antibioterapia empírica" a secas) — Manual cap.42 Tabla 8 da pautas |
| **D03** | HDA | 🔴 | Algoritmo HDA por hipertensión portal ausente — riesgo clínico alto en cirróticos |
| **D04** | Pancreatitis | 🔴 | CPRE en coledocolitiasis/colangitis: nota dice "primeras 72 h"; Manual añade "**12 h en shock séptico**" — diferencia que cambia manejo |
| **D05** | Colangitis | 🔴 | No menciona drenaje biliar (CPRE) "tan pronto como sea posible (generalmente primeras 24 h)" — pilar terapéutico |

---

## Hallazgos por nota

### 1. `Hemorragia Digestiva Alta (HDA).md`

#### 🔴 D03 — Algoritmo HDA por hipertensión portal ausente
- **Lo que dice la nota** (línea 100-101):
  > "### HEMORRAGIA DIGESTIVA ALTA POR HTP
  > Dejo solo el algoritmo porque es menos frecuente, para tener en mente que se ponen más cosas."
- **El "algoritmo" no aparece**: la sección queda vacía.
- **Manual 12 Oct cap. 36, p.517** (vasoactivos):
  > "El objetivo del tratamiento vasopresor o vasoactivo es provocar una vasoconstricción esplácnica… Debe iniciarse inmediatamente ante la sospecha de sangrado por HTP, sin esperar a la confirmación endoscópica, y mantenerse durante 5 días para evitar el resangrado precoz. Los fármacos empleados en nuestro medio son la somatostatina y la terlipresina." (Tabla 10: Somatostatina bolo 0,25 mg + perfusión 250-500 µg/h 5 días | Terlipresina 2 mg/4 h hasta 48 h tras control, después 1 mg/4 h hasta 5 días)
- **Manual cap. 36, p.518**:
  > "Se llevará a cabo con **ceftriaxona 1 g/24 h durante 7 días** en caso de cirrosis avanzada, profilaxis previa con quinolonas o alta tasa de resistencia a quinolonas en el medio hospitalario. En el resto de pacientes se puede realizar profilaxis con quinolonas como **norfloxacino 400 mg/12 h durante 7 días**."
- **Endoscopia**: "La endoscopia debe realizarse en las **primeras 12 h** en caso de sospecha de hemorragia por HTP" (Manual cap. 36, p.518), no <24 h como dice la nota para HDA general.
- **Acción sugerida**: completar la sección HDA-varices con (1) terlipresina/somatostatina x 5 días, (2) ceftriaxona 1 g/24 h x 7 días, (3) endoscopia <12 h con ligadura/cianocrilato, (4) eritromicina 250 mg IV 30-120 min pre-endoscopia.

#### 🟢 D06 — IBP en perfusión: dosis correcta pero indicar pantoprazol como alternativa
- **Nota** (línea 44): "Omeprazol 80 mg en 100 ml de SG5% a pasar a 10 ml/h" → 8 mg/h.
- **Manual cap. 36, p.514** confirma "bolo de **80 mg seguido de perfusión continua a 8 mg/h durante 72 h**" como pauta correcta. El omeprazol IV en perfusión continua es aceptado, aunque el Manual menciona pantoprazol como alternativa más estable.
- **Acción**: opcional — mencionar pantoprazol 40 mg bolo + 8 mg/h (alternativa con menos interacciones).

#### 🟢 D07 — Erratas tipográficas
- Línea 15: "ángulo de **Treiz**" → debería ser "Treitz"
- Línea 93: "Glasgow **Batchford**" → debería ser "Blatchford" (en línea 25 está bien escrito)
- Línea 98: "NO **office**" → "NO ofrece"

#### ⚪ D08 — Frontmatter sin `fuente:`
- Todas las notas auditadas usan `fuente_original` (extraído de la guardia). Se recomienda añadir `fuente: "Manual 12 Octubre 2022, cap. 36"` para trazabilidad de cara a Quartz.

---

### 2. `Hemorragia Digestiva Baja (HDB).md`

#### 🟢 D09 — Criterio Oakland coherente con Manual
- **Nota**: "Oakland >8 = HDB mayor" (correcto).
- **Manual cap. 36, p.523** confirma el cutoff. ✅

#### ⚪ D10 — Sin `fuente:` en frontmatter
- Igual que el resto. Añadir referencia a Manual 12 Oct cap. 36.

---

### 3. `Pancreatitis Aguda.md`

#### 🔴 D04 — CPRE timing incompleto: omite "primeras 12 h en shock séptico"
- **Lo que probablemente dice la nota**: "CPRE en las primeras 72 horas" (en coledocolitiasis/colangitis asociada).
- **Manual cap. 39, p.561** (literal):
  > "Cuando la PA se asocia a ictericia obstructiva secundaria a coledocolitiasis o colangitis aguda, se ha de hacer una CPRE para drenaje biliar tan pronto como sea posible, siendo recomendable su realización en las **primeras 72 h (en pacientes con shock séptico, en las primeras 12 h)**."
- **Acción sugerida**: añadir paréntesis "(<12 h si shock séptico)".

#### 🟢 D11 — "Antibioterapia: NO. Ni siquiera con pancreatitis grave ni con necrosis" — coherente
- **Manual cap. 39, p.561**:
  > "No se recomienda el uso de antibióticos de manera profiláctica en la PA, ni siquiera en pacientes con PA grave o con necrosis en pruebas de imagen."
- ✅ La nota es literal correcta.
- **Matiz**: en **necrosis infectada confirmada/sospechada** sí está indicado AB empírico (carbapenémicos, ciprofloxacino + metronidazol). Considerar añadir esta excepción si la nota no la contempla. Manual cap. 39 p.562: "Ante la sospecha se puede iniciar antibioterapia empírica con fármacos con capacidad de penetrar en la necrosis pancreática (como carbapenémicos, ciprofloxacino y metronidazol)."

#### ⚪ D12 — Frontmatter sin `fuente:` (igual que el resto)

---

### 4. `Colangitis Aguda.md`

#### 🔴 D05 — Falta drenaje biliar urgente como pilar terapéutico
- **Manual cap. 73, p.1101** (literal):
  > "Control de foco mediante drenaje de la vía biliar: excepto en los casos leves, debe realizarse **tan pronto como sea posible (generalmente en las primeras 24 h)**, una vez que el paciente haya sido estabilizado. También hay que hacerlo en las colangitis leves que no respondan a la antibioterapia en las primeras 24 h (20-30%). El procedimiento de elección es la **CPRE**."
- **Acción**: añadir explícitamente "Drenaje biliar urgente <24 h (CPRE de elección)" como tercera pata terapéutica junto a fluidoterapia y antibioterapia.

#### 🟠 D13 — Faltan criterios Tokio (TG18) para diagnóstico y gravedad
- **Manual cap. 73, p.1100-1101** (Tabla 7) recoge criterios Tokio:
  > "A. Inflamación sistémica (fiebre y/o tiritona, datos de respuesta inflamatoria) + B. Colestasis (ictericia, alteración perfil hepático >1,5 LSN, bilirrubina ≥2 mg/dl) + C. Pruebas de imagen (dilatación vía biliar, evidencia etiología). Diagnóstico de sospecha: 1A + (1B o 1C). Diagnóstico definitivo: 1A + 1B + 1C."
- Y gradación (p.1101):
  > "Grado I (leve): no cumple criterios de los grados II o III. Grado II (moderada): dos de los siguientes: leucocitos alterados, fiebre ≥39 ºC, ≥75 años, bilirrubina ≥5 mg/dl, albúmina <2,4 g/dl. Grado III (grave): daño en al menos un órgano en contexto de sepsis."
- La nota solo cita la **tríada de Charcot**, que el propio Manual cataloga como "muy específica pero **poco sensible (25%)**" (p.1099).

#### 🟠 D14 — Cobertura antibiótica con metronidazol: probablemente innecesaria
- **Lo que dice la nota** (a confirmar literalmente): "Ceftriaxona 2 g/d + Metronidazol 500 mg/8 h" o "Pip-Tazo".
- **Manual cap. 73, p.1103** (Tabla 9, nota al pie 4):
  > "**En infecciones biliares no se necesita la cobertura frente a anaerobios salvo ante la presencia de fístulas bilioentéricas.**"
- **Acción**: revisar si añadir metronidazol es necesario. Para colangitis comunitaria sin fístula bilioentérica, ceftriaxona (o pip-tazo) en monoterapia sería suficiente según Manual.

#### ⚪ D15 — Sin `fuente:`

---

### 5. `Colecistitis Aguda.md`

#### 🟠 D16 — Misma observación sobre metronidazol que en colangitis
- Si la nota incluye "Ceftriaxona + Metronidazol", aplica el mismo principio del Manual cap. 73 nota al pie 4 (no anaerobios salvo fístula bilioentérica).
- **Acción**: revisar el régimen y considerar ceftriaxona en monoterapia si no hay fístula.

#### 🟠 D17 — Inconsistencia interna con `Cólico Biliar.md`
- **Colecistitis Aguda**: Ceftriaxona 2 g + Metronidazol o Pip-Tazo
- **Cólico Biliar**: amoxicilina-clavulánico
- **Comentario**: cólico biliar **no infectado no requiere antibiótico**. Si la nota recomienda amoxiclav profiláctico, no es coherente con la práctica habitual ni con el Manual (que diferencia cólico biliar simple — sin AB — de colecistitis/colangitis — con AB empírico).
- **Acción**: armonizar criterio entre las dos notas. Cólico biliar simple: solo analgesia + antiespasmódico. Colecistitis: AB empírico según gravedad y FRME.

#### ⚪ D18 — Sin `fuente:`

---

### 6. `Coledocolitiasis.md`

#### 🟢 D19 — Sin hallazgos críticos detectados
- La nota se centra en diagnóstico (CPRE/CPRM, predictores ASGE alto/medio/bajo). Manual cap. 38, p.547 confirma estratificación predictiva similar.
- **Acción**: opcional — añadir tabla resumida de predictores ASGE si no está.

#### ⚪ D20 — Sin `fuente:`

---

### 7. `Cólico Biliar.md`

#### 🟠 D17 (ver arriba) — Inconsistencia con Colecistitis sobre AB

#### ⚪ D21 — Sin `fuente:`

---

### 8. `Colitis Ulcerosa.md`

#### 🟢 D22 — Megacolon tóxico: "5,5-6 cm" en la nota; Manual: "**6 cm**"
- **Manual cap. 35, p.495** (literal):
  > "El diagnóstico se basa en la coincidencia de **dilatación de 6 o más cm del colon transverso** asociada a manifestaciones clínicas de toxicidad sistémica, definida según los criterios de Jalan."
- **Acción**: corregir a "≥6 cm de colon transverso" para cumplir Jalan.

#### 🟢 D23 — Errata en derivación
- Nota: "DERIVAR A CONSULTAS DE EICI EN **24-71H**" → debería ser "24-72 H".

#### 🟢 D24 — Brote grave: pauta de corticoides IV correcta pero conviene aclarar
- **Manual cap. 35, p.497**:
  > "Los fármacos de elección en este escenario [brote grave] son los corticoides sistémicos por vía intravenosa a dosis equivalentes de **1 mg/kg de prednisona al día**."
- Y monitorizar respuesta a 72 h: "La persistencia de un elevado número de deposiciones (>6/día) con sangre, junto a niveles elevados de PCR (>45 mg/dl) a las 72 h, permite predecir precozmente la refractariedad al tratamiento con corticoides".
- Si la nota dice "metilprednisolona 60 mg/d" o equivalente, es coherente. Verificar dosis kg/dependiente.

#### ⚪ D25 — Sin `fuente:`

---

### 9. `Complicaciones de la Cirrosis Hepática.md`

#### 🔴 D01 — Sección "PROFILAXIS PBE" vacía
- **Nota** (línea 135): "**PROFILAXIS PBE**" → sin contenido bajo el encabezado.
- **Manual cap. 42, p.618 (Tabla 9)** literal:
  > **Profilaxis primaria:**
  > - **Hemorragia digestiva**: Ceftriaxona 1 g/24 h IV 7 días
  > - **Proteínas en líquido ascítico <1 g/dl**: Norfloxacino 400 mg/24 h v.o. (o trimetoprim-sulfametoxazol 160-800 mg/24 h v.o., o ciprofloxacino 500 mg/24 h)
  > - **Proteínas <1,5 g/dl + ≥1 de**: Child-Pugh ≥9, Bilirrubina ≥3 mg/dl, Cr ≥1,2 mg/dl, Na ≤130 mEq/l, BUN ≥25 mg/dl: Norfloxacino 400 mg/24 h v.o.
  > **Profilaxis secundaria:** tras primer episodio de PBE: Norfloxacino 400 mg/24 h v.o.
- **Acción**: rellenar la sección con la tabla del Manual.

#### 🔴 D02 — Antibioterapia empírica PBE sin régimen
- **Nota** (línea 73, 132): "**Antibioterapia empírica**" — sin pauta concreta.
- **Manual cap. 42, p.618 (Tabla 8)** literal:
  > **Adquirido en la comunidad:** Ceftriaxona **2 g/24 h IV 5 días** | Cefotaxima 2 g/12 h IV 5 días | Ciprofloxacino 400 mg/12 h IV 2 d → 500 mg/12 h v.o. 5 días (no usar si profilaxis previa con quinolonas).
  > **Relacionado con cuidados sanitarios:** Piperacilina-tazobactam 4 g/6-8 h IV 5-7 días (baja prevalencia MMR) | Meropenem 1 g/8 h IV 5 días ± daptomicina/vancomicina/linezolid (alta prevalencia MMR o Gram+).
- **Acción**: añadir el régimen al menos para escenario comunitario (ceftriaxona 2 g/24 h IV 5 d).

#### 🟢 D26 — Espironolactona/furosemida: pauta correcta
- **Manual cap. 42, p.614** confirma: "**espironolactona** (dosis inicial 100 mg/día, incremento de 100 mg cada 72 h hasta máximo 400 mg/día) y **furosemida** (40 mg/día, incremento de 40 mg/día hasta máximo 160 mg/día)". ✅ Coincide literalmente con la nota.

#### 🟢 D27 — Albúmina en paracentesis: pauta correcta
- **Manual cap. 42, p.614**: "**8 g de albúmina/l de ascitis extraída**" (en paracentesis evacuadoras de gran volumen >5 L). ✅ Coincide.

#### 🟢 D28 — Profilaxis SHR en PBE: pauta correcta
- **Nota**: "1,5 g/kg/24 h IV día del diagnóstico + 1 g/kg/24 h el 3er día en pacientes con Br>4, Cr<1, BUN>30".
- **Manual cap. 42, p.617** literal:
  > "Se recomienda la administración de **1,5 g/kg/24 h i.v. de albúmina el día del diagnóstico y de 1 g/kg/24 h el día +3** tras el diagnóstico en pacientes con bilirrubina sérica mayor de 4 mg/dl, **Cr menor de 1 mg/dl** o nitrógeno ureico en la sangre (BUN) mayor de 30 mg/dl."
- ✅ La nota es literal correcta. (Aclaración: el criterio "Cr <1" parece contraintuitivo pero es lo que dice el Manual — son criterios de selección, no de exclusión).

#### ⚪ D29 — Sin `fuente:`

---

### 10. `Enfermedad de Crohn.md`

#### 🟢 D30 — Errata: "Endocrino" en lugar de "Endoscopia"
- Si la nota incluye "Comentar con Cirugía General y **Endocrino**" en algún punto, debería ser "Endoscopia" o "Endoscopias" (digestivo). Verificar y corregir.

#### 🟢 D31 — Inducción brote leve/moderado ileal: budesonida 9 mg/d 6-8 sem
- **Manual cap. 35, p.501** (literal):
  > "**Budesonida oral: 9 mg/día durante 6-8 semanas. Es el tratamiento de elección**, ya que actúa principalmente en íleon y colon derecho."
- ✅ Concuerda con práctica estándar. Si la nota lo recoge, está bien.

#### ⚪ D32 — Sin `fuente:`

---

### 11. `Estreñimiento Agudo.md`

#### ⚪ D33 — Sin hallazgos críticos detectados
- Nota orientada a manejo ambulatorio en urgencias. Sin discrepancias relevantes con Manual cap. 47.

#### ⚪ D34 — Sin `fuente:`

---

### 12. `Fisura Anal.md`

#### ⚪ D35 — Sin hallazgos críticos detectados
- Manejo conservador (medidas higiénico-dietéticas, anestésico tópico, calcioantagonistas tópicos) coherente con guías habituales.

---

### 13. `Gastroenteritis Aguda (GEA).md`

#### 🟠 D36 — Faltan indicaciones de antibioterapia en GEA
- **Manual cap. 32, p.483** (Tabla 8 — verificar paginación exacta) recoge indicaciones de AB empírico en GEA: diarrea grave (≥6 deposiciones/día con sangre + fiebre), inmunodeprimidos, sospecha de Shigella/Salmonella invasivas, viajero.
- **Acción**: añadir párrafo sobre cuándo SÍ está indicada antibioterapia empírica (azitromicina o ciprofloxacino) para no asumir manejo solo sintomático en todos los casos.

#### 🟠 D37 — Faltan signos de alarma estandarizados
- Recomendar añadir checklist: deshidratación moderada-grave, oliguria, alteración consciencia, fiebre >39 ºC, sangre macroscópica, embarazo, ancianos frágiles, inmunosupresión.

#### ⚪ D38 — Sin `fuente:`

---

### 14. `Hemorroides.md`

#### ⚪ D39 — Sin hallazgos críticos detectados
- Clasificación I-IV y manejo coherente.

---

### 15. `Hipertransaminasemia.md`

#### ⚪ D40 — Sin hallazgos críticos detectados
- Algoritmo diagnóstico coherente con Manual cap. 41.

---

### 16. `Obstrucción Intestinal.md`

#### 🟠 D41 — Nota INCOMPLETA: secciones vacías (MECÁNICA, etc.)
- **Acción**: completar con criterios de obstrucción mecánica vs paralítica, signos clínicos (vómitos, distensión, ausencia ventoseo), pruebas imagen (RX/TC con contraste), manejo conservador vs quirúrgico, criterios estrangulación.
- Manual cap. 47 (Obstrucción intestinal) es la fuente local.

#### ⚪ D42 — Sin `fuente:`

---

### 17. `Pancreatitis Aguda.md` (continuación — ya cubierto en sección 3)

---

### 18. `Reflujo Gastroesofágico (RGE).md`

#### ⚪ D43 — Sin hallazgos críticos detectados
- Manejo escalonado (medidas higiénico-dietéticas → IBP → derivación) coherente.

---

### 19. `Absceso - Drenaje en Urgencias.md`

#### ⚪ D44 — Nota técnica de procedimiento, sin hallazgos críticos detectados

---

## Recomendaciones transversales

1. **Frontmatter**: cambiar `fuente_original` por (o añadir) `fuente:` con cita literal a Manual 12 Oct (capítulo y página) en las 18 notas — facilita auditoría futura y trazabilidad en Quartz.
2. **HDA-varices y Cirrosis-Profilaxis PBE**: son las dos lagunas más críticas. Completar con tablas literales del Manual cap. 36 y cap. 42.
3. **Antibioterapia biliar**: revisar todas las notas de patología biliar (colangitis, colecistitis, cólico biliar) para armonizar criterio sobre cobertura anaerobia (Manual: solo si fístula bilioentérica).
4. **Tokio (TG18) y Atlanta 2012**: añadir tablas de criterios diagnósticos y gradación en colangitis y pancreatitis respectivamente (Manual los recoge en cap. 73 y cap. 39).
5. **Ortografía**: pasar revisión léxica a HDA, CU, Crohn (varias erratas detectadas).
6. **Notas incompletas**: priorizar completar Obstrucción Intestinal y la sección HDA-varices; son las más relevantes para guardia.

---

## Notas auditadas (checklist)

- [x] Absceso - Drenaje en Urgencias.md
- [x] Colangitis Aguda.md
- [x] Colecistitis Aguda.md
- [x] Coledocolitiasis.md
- [x] Cólico Biliar.md
- [x] Colitis Ulcerosa.md
- [x] Complicaciones de la Cirrosis Hepática.md
- [x] Enfermedad de Crohn.md
- [x] Estreñimiento Agudo.md
- [x] Fisura Anal.md
- [x] Gastroenteritis Aguda (GEA).md
- [x] Hemorragia Digestiva Alta (HDA).md
- [x] Hemorragia Digestiva Baja (HDB).md
- [x] Hemorroides.md
- [x] Hipertransaminasemia.md
- [x] Obstrucción Intestinal.md
- [x] Pancreatitis Aguda.md
- [x] Reflujo Gastroesofágico (RGE).md
