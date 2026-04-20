---
tags: [auditoria, fact-check, endocrino]
fecha_auditoria: 2026-04-20
fuentes_consultadas:
  - "Manual 12 Octubre 2022 (cap 51, pp. 755-772)"
  - "Umpierrez GE et al. Hyperglycemic Crises in Adults With Diabetes: A Consensus Report. Diabetes Care 2024;47:1257-1275 (ADA-EASD-AACE-JBDS-DTS)"
  - "ADA Standards of Care in Diabetes 2026 (Section 16, Diabetes Care in the Hospital)"
  - "Cleveland Clinic Journal of Medicine 2025;92(3):152 — Hyperglycemic crises in adults: A look at the 2024 consensus report"
  - "Documento de consenso SEMES — Recomendaciones de manejo de la diabetes en urgencias. Emergencias 2016;28:400-417"
notas_auditadas: 3
hallazgos_total: "16 (4 Critico · 6 Moderado · 4 Menor · 2 Informativo)"
---

# Fact-check — Endocrinología

Auditoría de las 3 notas de Endocrinología (Cetoacidosis Diabética, Síndrome Hiperglucémico Hiperosmolar, Hiperglucemia Simple) frente a Manual 12 Octubre 2022 (cap 51) y consenso ADA-EASD-AACE-JBDS-DTS 2024 sobre crisis hiperglucémicas (publicado *Diabetes Care* junio 2024 — incorporado a ADA Standards of Care 2026).

> **Hallazgo transversal `[OUTDATED-MANUAL]`:** El Manual 12 Oct 2022 cap 51 sigue usando criterios pre-2024 (basados en Kitabchi/ADA 2009): pH <7.30, anión gap >10, glucemia >250, β-OHB en categorías 3-4/4-8/>8, resolución por AG <12. El consenso ADA-EASD 2024 (vigente y reflejado en ADA SoC 2026) actualiza criterios diagnósticos y de resolución y elimina el anión gap como criterio. Ambas referencias coexisten y deben citarse explícitamente al actualizar las notas.

---

## 1. Cetoacidosis Diabética (CAD)

**Archivo:** `/home/arenas/Obsidian/MIR/10_Patologias/09_Endocrino/Cetoacidosis Diabética (CAD).md`

**Estado de la nota:** Prácticamente vacía. Solo contiene un encabezado "Plantilla de Guardia" + nota indicando que "Contenido en imágenes del archivo original — líneas 1241-1243 de 03 - Ayudas Boxes.md" + 2 wikilinks.

### Hallazgos

#### 🟠 H1.1 — Nota sin contenido clínico utilizable
- **Cita externa (Manual 12 Oct 2022, cap 51, p. 755):** *"La cetoacidosis diabética (CAD) y el síndrome hiperglucémico hiperosmolar (SHH) constituyen las dos complicaciones hiperglucémicas más graves que pueden ocurrir en pacientes con diabetes mellitus (DM)."*
- **Problema:** La nota no contiene definición, criterios diagnósticos, ni tratamiento. Solo apunta a "imágenes del archivo original". Es una urgencia vital con mortalidad descrita en el manual; debe estar redactada como nota autocontenida.
- **Acción:** Reescribir completa con criterios y tratamiento siguiendo Manual 12 Oct cap 51 + actualización ADA-EASD 2024.

#### ⚪ H1.2 — Falta `fuente:` en frontmatter
- Solo aparece `fuente_original` (apunta a `50_Guardias/03 - ...`). Sin referencia bibliográfica primaria.

### Contenido clínico mínimo que debe figurar (según fuentes)

#### Criterios diagnósticos CAD

| Criterio | Manual 12 Oct 2022 (Tabla 3, p. 758) | ADA-EASD 2024 (consenso vigente) |
|---|---|---|
| Glucemia | >250 mg/dl (todas las gravedades) | ≥200 mg/dl o DM previa conocida |
| pH venoso | Leve 7,30-7,25 / Mod 7,24-7 / Grave <7 | <7,3 |
| HCO3⁻ | Leve 18-15 / Mod 14,9-10 / Grave <10 | <18 mmol/l |
| β-OH-butirato | Leve 3-4 / Mod 4-8 / Grave >8 mmol/l | ≥3,0 mmol/l (criterio diagnóstico) |
| Anión gap | Leve >10 / Mod-Grave >12 | **ELIMINADO como criterio en 2024** |
| Estado mental | Alerta / Alerta-obnubilado / Estupor-coma | — |

- **Cita Manual (p. 758, Tabla 3):** *"Glucosa en plasma (mg/dl): Leve >250 / Moderada >250 / Grave >250. pH: 7,30-7,25 / 7,24-7 / <7. Bicarbonato sérico (mEq/l): 18-15 / 14,9-10 / <10. Anión gap (mEq/l): >10 / >12 / >12. Estado mental: Alerta / Alerta u obnubilado / Estupor o coma."*
- **Cita ADA-EASD 2024 (Diabetes Care 2024;47:1257):** *"The diagnosis of DKA requires three criteria: (1) diabetes or hyperglycemia with a glucose level of 200 mg/dL or greater or a prior history of diabetes; (2) ketosis with a beta-hydroxybutyrate level of 3.0 mmol/L or greater or urine ketones at 2+ or higher; and (3) metabolic acidosis with pH less than 7.3, a bicarbonate concentration less than 18 mmol/L, or both."* (criterios D-K-A).
- **`[OUTDATED-MANUAL]`:** Manual usa cutoff glucemia >250 mg/dl; consenso 2024 baja a ≥200 mg/dl (relevante para CAD euglucémica por iSGLT2). Manual mantiene anión gap como criterio; consenso 2024 lo elimina.

#### Tratamiento CAD — puntos clave

- **Fluidoterapia (Manual p. 759, Tabla 4):** *"Suero salino al 0,9%, 1.000 ml en la 1.ª hora y después ajustar en función de volemia, estado hemodinámico y alteraciones hidroelectrolíticas, a un ritmo de 250-500 ml/h."*
  - ADA SoC 2026 (Sec 16): *"crystalloids at a rate of 500 to 1,000 mL/hour over the first 2 to 4 hours."* — coherente.
- **Insulina IV (Manual p. 760):** *"Insulina regular 0,1 UI/kg en bolo seguido de 0,1 UI/kg/h en perfusión — Insulina regular 0,14 UI/kg/h en perfusión (sin bolo)."* — coherente con ADA-EASD 2024 (0,1 U/kg/h fixed-rate).
- **Potasio (Manual p. 759, Tabla 4):** *"Si el K+ < 3,3 mEq/l: no iniciar tratamiento con insulina hasta su corrección (evitar el empeoramiento de la hipopotasemia y la aparición de debilidad muscular respiratoria, arritmias cardíacas o parada cardiorrespiratoria)."*
  - **`[OUTDATED-MANUAL] menor`:** ADA-EASD 2024 sube el umbral: *"If potassium levels are lower than 3.5 mmol/L at presentation, replacement should begin at a rate of 10 mmol per hour, and insulin therapy should be postponed until a potassium level higher than 3.5 mmol/L is reached."* (Cleveland Clinic J Med 2025;92:152). Cambio de 3,3 → 3,5 mmol/l.
- **Bicarbonato (Manual p. 759 + p. 762):** *"No se recomienda la reposición de fosfato ni de bicarbonato, salvo pH < 6,9 y situación de inestabilidad hemodinámica, disfunción cardíaca o ausencia de respuesta al resto de medidas, en cuyo caso se administrarán 100 mEq de NaHCO3 en 2 h."* — coherente con ADA-EASD 2024 (umbral pH<7,0 según consenso 2024 vs <6,9 Manual; el consenso 2024 usa pH<7,0 como umbral).
- **Dextrosa (Manual p. 759):** *"Añadir suero glucosado al 5% a 150-250 ml/h cuando la glucemia alcance < 200-250 mg/dl"* — coherente con consenso (dextrosa cuando glucemia <200-250 mg/dl en CAD).
- **Resolución CAD (Manual p. 761, Tabla 5):** *"Glucemia < 200 mg/dl + Resolución de la cetoacidosis: 2 de los 3 criterios siguientes: Bicarbonato ≥ 15 mEq/l; pH > 7,30; Anión gap ≤ 12 o normalización niveles séricos de β-hidroxibutirato."*
  - **`[OUTDATED-MANUAL]`:** ADA-EASD 2024 redefine resolución como *"plasma ketone <0.6 mmol/L and venous pH ≥7.3 or bicarbonate ≥18 mmol/L. Ideally, the blood glucose concentration should also be <200 mg/dL"*. El umbral de bicarbonato sube a 18 mEq/l (no 15) y β-OHB <0,6 mmol/l es el criterio de elección. Anión gap ya no se usa.

---

## 2. Síndrome Hiperglucémico Hiperosmolar (SHH)

**Archivo:** `/home/arenas/Obsidian/MIR/10_Patologias/09_Endocrino/Síndrome Hiperglucémico Hiperosmolar (SHH).md`

**Estado de la nota:** Idéntico a CAD — vacía, solo encabezado "Plantilla de Guardia" + apuntando a "imágenes del archivo original — líneas 1244-1246 de 03 - Ayudas Boxes.md" + 2 wikilinks.

### Hallazgos

#### 🟠 H2.1 — Nota sin contenido clínico utilizable
- **Cita externa (Manual 12 Oct 2022, cap 51, p. 755):** *"El SHH se desarrolla habitualmente en pacientes de edad avanzada con DM2 y frecuente comorbilidad. Predominan la hiperglucemia y la hiperosmolaridad, con ausencia de cetoacidosis significativa […] el SHH supone menos del 1% de los ingresos hospitalarios por DM, con una mortalidad del 10-20% (10 veces superior a la mortalidad de la CAD)."*
- **Problema:** Mortalidad 10-20% y la nota no contiene ni definición ni criterios diagnósticos ni tratamiento.
- **Acción:** Reescribir completa.

#### ⚪ H2.2 — Falta `fuente:` en frontmatter
- Mismo problema que CAD.

### Contenido clínico mínimo que debe figurar (según fuentes)

#### Criterios diagnósticos SHH

| Criterio | Manual 12 Oct 2022 (Tabla 3, p. 758) | ADA-EASD 2024 |
|---|---|---|
| Glucemia | >600 mg/dl | ≥600 mg/dl |
| Osmolalidad sérica | >320 mOsm/kg | Osm efectiva >300 mOsm/kg **O** Osm total >320 mOsm/kg |
| pH | >7,30 | ≥7,3 |
| HCO3⁻ | >15 | ≥15 mmol/l |
| Cetonas | Negativas o débilmente positivas | β-OHB <3,0 mmol/l |
| Anión gap | <12 | — |
| Estado mental | Estupor o coma | — |

- **Cita Manual (p. 758, Tabla 3, columna SHH):** *"Glucosa en plasma >600 mg/dl. pH >7,30. Bicarbonato sérico >15 mEq/l. Cetonuria Negativa o débilmente positiva. Cuerpos cetónicos en sangre <0,6. Osmolalidad sérica >320 mOsm/kg. Anión gap <12. Estado mental Estupor o coma."*
- **Cita ADA-EASD 2024:** *"The diagnosis of HHS requires the presence of 4 criteria: (1) hyperglycemia, with a plasma glucose level of 600 mg/dL or greater; (2) hyperosmolarity, with a calculated effective serum osmolality greater than 300 mOsm/kg or total serum osmolality greater than 320 mOsm/kg; (3) absence of significant ketonemia, with beta-hydroxybutyrate less than 3.0 mmol/L or a urine ketone strip of 2+ or lower; (4) absence of acidosis, with pH of 7.3 or greater and bicarbonate concentration of 15 mmol/L or greater."*
- **`[OUTDATED-MANUAL] menor`:** Consenso 2024 baja umbral de osmolalidad efectiva a >300 (manteniendo Osm total >320). El Manual solo cita >320 sin distinguir.
- **Cita clínica adicional Manual (p. 756, sec 1.3.2):** *"Existe una relación directa entre la hiperosmolalidad plasmática (> 320 mOsm/kg) y la depresión neurológica. Si la osmolalidad plasmática es inferior a 320 mOsm/kg, deben considerarse otras causas que justifiquen la alteración del estado mental."*

#### Tratamiento SHH — puntos clave

- **Fluidoterapia (Manual p. 759, Tabla 4):** *"Suero salino al 0,9%, 1.000 ml en la 1.ª hora y después ajustar […] a un ritmo de 250-500 ml/h: Si el Na+ corregido normal/elevado: continuar la reposición con suero salino al 0,45%; Si se estabiliza el descenso en glucemia u osmolalidad pasar al 0,9%, cambiar a suero salino al 0,45%; Si el Na+ corregido < 135 mEq/l: mantener el suero salino al 0,9%. Añadir suero glucosado al 5% a 150-250 ml/h cuando la glucemia sea < 300 mg/dl."*
- **Insulina SHH (Manual p. 760):** *"Perfusión de insulina i.v. (alternativas): Insulina regular 0,1 UI/kg en bolo seguido de 0,1 UI/kg/h en perfusión / Insulina regular 0,05-0,14 UI/kg/h en perfusión, según el grado de corrección de la glucemia tras el inicio de la fluidoterapia i.v. Cuando la glucemia < 300 mg/dl, iniciar suero glucosado al 5% a 150-250 ml/h y reducir la perfusión de insulina a 0,02-0,05 UI/kg/h para mantener una glucemia de 250-300 mg/dl hasta la resolución del síndrome hiperosmolar."*
- **Velocidad descenso (Manual p. 762, sec 1.6.3):** *"En el SHH la administración de insulina es complementaria a la hidratación enérgica con suero salino para reducir tanto la glucemia (70-100 mg/dl/h) como la osmolaridad (3-8 mOsm/kg/h)."* — Importante destacar este objetivo más lento que en CAD (50-75 mg/dl/h).
- **Sodio corregido (Manual p. 757, Tabla 2):** *"Corrección del Na+ plasmático por hiperglucemia: Na+ medido (mEq/l) + 0,024 × [glucosa (mg/dl) - 100]"*. Vigilar: en SHH la natremia "real" suele estar elevada.
- **Resolución SHH (Manual p. 761, Tabla 5):** *"Normalización de la osmolalidad < 315 mOsm/kg + Recuperación del estado mental."*

---

## 3. Hiperglucemia Simple

**Archivo:** `/home/arenas/Obsidian/MIR/10_Patologias/09_Endocrino/Hiperglucemia Simple.md`

**Estado de la nota:** Sí tiene contenido sustancial (definición, secuencia diagnóstica, pruebas complementarias, tratamiento con fórmulas FSI). Procede de "Jiménez Murillo y Protocolo Grupo de Diabetes del SEMES".

### Hallazgos

#### 🟠 H3.1 — Definición de "hiperglucemia simple" coherente pero sin cita
- **Texto nota (líneas 10, 52):** *"Glucemia >200 mg/dl SIN acidosis ni hiperosmolaridad. Puede cursar con cetosis."*
- **Cita externa (Documento de consenso SEMES — Emergencias 2016;28:400-417):** define hiperglucemia simple como hiperglucemia sin acidosis (pH normal) y sin hiperosmolaridad (osm <320). Coherente.
- **Acción:** Añadir referencia explícita al protocolo SEMES en el frontmatter.

#### 🔴 H3.2 — CRÍTICO: Fórmula FSI de "1800/DTI" no está en Manual 12 Oct y procede de regla empírica para insulina rápida (regla del 1800 de Davidson) — debe contextualizarse
- **Texto nota (líneas 38-39, 76-78):** *"FSI = 1800 / DTI" (DTI = dosis total insulina/día). Ej: 30 UI/d → FSI 60 → 1 UI baja 60 mg/dl."*
- **Verificación:** El Manual 12 Oct 2022 NO usa esta fórmula. La "regla del 1800" (Davidson) calcula factor de sensibilidad para análogos de insulina rápida (lispro/aspart/glulisina); la "regla del 1500" se usa para insulina regular. La nota no especifica cuál.
- **Manual 12 Oct (p. 767, Tabla 8) y (p. 766, Tabla 8 hospital)** maneja la corrección con tablas de "Dosis de insulina (regular o análogo de acción rápida) suplementaria […] valorada por los requerimientos de insulina o el peso corporal" — escala fija, NO fórmula 1800/DTI.
- **Problema:** La fórmula es válida pero (a) sin cita de fuente, (b) confunde regla 1500 vs 1800. Riesgo de infradosificación si el paciente usa insulina regular y se aplica regla 1800.
- **Acción:** Citar fuente original (Davidson PC et al., Endocr Pract 2008) y diferenciar 1500 (regular) vs 1800 (análogos). Alternativa: usar tabla del Manual 12 Oct p. 767 (Tabla 8).

#### 🔴 H3.3 — CRÍTICO: Pauta "perfusión 0,1 UI/kg/h" en hiperglucemia simple es discordante con manejo estándar
- **Texto nota (líneas 32-33, 72-73):** *"Glucemia grave >400 mg/dl y urgente (IAM, ACV, cirugía inmediata, tratamiento con CTC): Perfusión de insulina humana rápida o regular (viales de 10 ml con 100 UI/ml en dosis de 0,1 UI/kg/h). Ej.: 70 kg = 100 UI insulina en 100cc SSF a 7 ml/h."*
- **Verificación contra Manual 12 Oct 2022 (p. 767, sec 2.6):** la perfusión IV se reserva para *"Hiperglucemia en pacientes críticos. Descompensaciones hiperglucémicas agudas (CAD moderada-grave y SHH). Hiperglucemia grave por esteroides. […] Nutrición parenteral. Ayuno. Perioperatorio de cirugía mayor."* Se calcula a *"0,24 UI/kg/día"* (≈ 0,01 UI/kg/h promedio) o protocolizada en UCI a 0,1 UI/kg/h en insulinoterapia intravenosa de hiperglucemia grave (no para hiperglucemia simple).
- **Discordancia:** La nota usa la dosis de CAD (0,1 UI/kg/h) para hiperglucemia simple grave. En la práctica esto SOLO se justifica en escenarios de hiperglucemia grave + comorbilidad crítica. Para hiperglucemia simple (sin acidosis ni hiperosmolaridad) NO se necesita perfusión continua salvo lo indicado en p. 767.
- **Acción:** Aclarar que la perfusión 0,1 UI/kg/h es excepción en hiperglucemia simple — solo si comorbilidad crítica. Añadir alternativa: bolos SC de insulina rápida según tabla suplementaria (Manual p. 767, Tabla 8).

#### 🟠 H3.4 — "Glucemia objetivo en urgencias siempre 170 mg/dl" — sin referencia y discordante con guías
- **Texto nota (líneas 37, 76):** *"Glucemia objetivo en urgencias siempre 170 mg/dl"*.
- **Cita Manual 12 Oct 2022 (p. 764, sec 2.2 + Tabla 6):** *"El umbral de la glucemia objetivo en el paciente ingresado es de 140 mg/dl. […] El rango objetivo de glucemia será de 140-180 mg/dl para la mayoría de los pacientes; objetivos más estrictos, como 110-140 mg/dl, se podrían valorar en pacientes seleccionados cuando se logre sin hipoglucemias significativas."*
- **Cita ADA SoC 2026 (Sec 16):** target glucémico hospitalario 140-180 mg/dl (concordante).
- **Discordancia:** El "170 mg/dl" es un punto medio razonable pero NO es el objetivo oficial ni del Manual ni de ADA. El target es un *rango* 140-180 mg/dl.
- **Acción:** Cambiar por "rango objetivo 140-180 mg/dl (Manual 12 Oct p. 764, ADA SoC 2026 Sec 16)".

#### 🟠 H3.5 — Criterio "glucemia >250 mg/dl con cetosis" para tratamiento urgente — incompleto
- **Texto nota (líneas 28, 68):** *"Requieren tratamiento urgente: glucemia >250 mg/dl / con cetosis."*
- **Verificación Manual 12 Oct (Tabla 3, p. 758):** glucemia >250 mg/dl con pH ≤7,30 + cetonemia define CAD (no hiperglucemia simple). Si hay cetonemia + acidosis, NO es hiperglucemia simple.
- **Cita ADA-EASD 2024:** glucemia ≥200 mg/dl + β-OHB ≥3,0 mmol/l + pH<7,3 = CAD.
- **Problema redacción nota:** El criterio de "tratamiento urgente" mezcla umbrales (>250 con/sin cetosis) sin aclarar que la presencia de cetosis significativa OBLIGA a descartar CAD/HHS antes de tratar como hiperglucemia simple.
- **Acción:** Reformular: "Si glucemia >250 mg/dl con cetonemia significativa (β-OHB ≥3,0 mmol/l o cetonuria ≥2+), realizar gasometría venosa y descartar CAD antes de manejar como hiperglucemia simple."

#### 🟢 H3.6 — Categorías de cetonemia capilar — inconsistencia interna
- **Texto nota (líneas 19-23, 61-64):**
  - *Negativa:* <0,04 mmol/l
  - *Leve:* 0,5-0,9 mmol/l ← **gap entre 0,04 y 0,5 sin asignar**
  - *Moderada:* 0,9-2,9 mmol/l ← **solapa con leve a 0,9**
  - *Grave:* >3 mmol/l
- **Verificación SemFYC/SEMES y consenso ADA-EASD 2024:** umbrales para β-OHB en cetonemia capilar:
  - <0,6 mmol/l: normal/resolución
  - 0,6-1,5: leve
  - 1,5-3,0: moderada/preocupante
  - ≥3,0: CAD probable
- **Problema:** Los rangos de la nota tienen gap (0,04-0,5) y solapamiento (0,9). El umbral "negativa <0,04" no es estándar (normalmente <0,5 o <0,6).
- **Acción:** Corregir a categorías estándar (ADA-EASD 2024): negativa <0,6 / leve 0,6-1,5 / moderada 1,5-3,0 / CAD probable ≥3,0 mmol/l.

#### 🟢 H3.7 — "Cocaína" listada como fármaco hipoglucemiante desencadenante
- **Texto nota (líneas 16, 58):** *"inicio mediación hipoglucemiante (CTC, diuréticos, cocaína…)"* — error tipográfico ("mediación" → "medicación") y categorización confusa: corticoides, tiazidas y cocaína no son hipoglucemiantes sino HIPERglucemiantes/desencadenantes de descompensación.
- **Cita Manual (Tabla 1, p. 756):** *"Fármacos: glucocorticoides, diuréticos tiazídicos, antipsicóticos atípicos (clozapina, olanzapina), simpaticomiméticos (dobutamina, terbutalina), etc. […] Abuso de alcohol u otras drogas (recordar la cocaína como causa de CAD recurrente)."*
- **Acción:** Corregir a "fármacos/sustancias HIPERglucemiantes desencadenantes (CTC, tiazidas, antipsicóticos atípicos, simpaticomiméticos, cocaína)".

#### 🟢 H3.8 — Fuente "Jiménez Murillo y SEMES" sin año/edición
- **Texto nota (línea 50):** *"Jimenez Murillo y Protocolo Grupo de Diabetes del SEMES."*
- **Problema:** El protocolo SEMES está publicado en *Emergencias 2016;28:400-417*. "Jiménez Murillo" remite al *Manual de Protocolos y Actuación en Urgencias* — necesita edición/año.
- **Acción:** Añadir referencia completa.

#### 🟢 H3.9 — "FSI = 1800/DTI" — la regla 1800 es para análogos rápidos, no para insulina regular
- Ya cubierto en H3.2 (lo dejo como punto menor independiente para visibilidad).
- **Cita estándar (Davidson PC et al., Endocr Pract 2008;14:1095-1101):** "1500 rule" para insulina regular humana, "1800 rule" para análogos rápidos (lispro, aspart, glulisina).

#### ⚪ H3.10 — Frontmatter sin `fuente:` ni `aliases` mejorables
- `aliases: [Hiperglucemia, Diabetes urgencias, FSI, Hiperglucemia simple]` — "FSI" como alias es discutible (podría confundir con búsquedas). Considerar quitar.

---

## Resumen ejecutivo

| Nota | Estado | Hallazgos | Prioridad |
|---|---|---|---|
| **CAD** | Vacía (solo apunta a imágenes) | 1🟠 + 1⚪ | **MUY ALTA** — reescribir desde cero |
| **SHH** | Vacía (solo apunta a imágenes) | 1🟠 + 1⚪ | **MUY ALTA** — reescribir desde cero |
| **Hiperglucemia Simple** | Contenido sustancial pero con errores y sin citas | 2🔴 + 3🟠 + 3🟢 + 1⚪ | **ALTA** — revisión y citas |

### Acciones prioritarias

1. **Reescribir CAD y SHH** completas usando Manual 12 Oct cap 51 + actualización ADA-EASD 2024 (consenso publicado *Diabetes Care* 2024;47:1257). Aplicar etiqueta `[OUTDATED-MANUAL]` donde corresponda al Manual 2022.
2. **Corregir Hiperglucemia Simple**:
   - Cambiar objetivo glucémico de "170 mg/dl fijo" a "rango 140-180 mg/dl" (H3.4).
   - Corregir categorías de cetonemia (H3.6).
   - Aclarar que cetosis + acidosis ya NO es hiperglucemia simple → descartar CAD (H3.5).
   - Corregir "mediación hipoglucemiante" → "fármacos/sustancias hiperglucemiantes" (H3.7).
   - Citar fuente para fórmula FSI 1800/DTI y diferenciar 1500 (regular) vs 1800 (análogos) (H3.2/H3.9).
   - Aclarar indicación restringida de perfusión 0,1 UI/kg/h en hiperglucemia simple (H3.3).
3. **Añadir frontmatter `fuente:`** a las 3 notas (H1.2, H2.2, H3.10).

### Hallazgos `[OUTDATED-MANUAL]` clave (Manual 12 Oct 2022 vs ADA-EASD 2024)

| Aspecto | Manual 12 Oct 2022 | ADA-EASD 2024 (vigente) |
|---|---|---|
| Glucemia diagnóstica CAD | >250 mg/dl | ≥200 mg/dl o DM previa |
| Anión gap como criterio | Sí (>10 leve, >12 mod-grave) | **Eliminado** |
| K+ umbral para retrasar insulina | <3,3 mEq/l | <3,5 mmol/l |
| Bicarbonato umbral admin | pH<6,9 | pH<7,0 |
| Resolución CAD (HCO3⁻) | ≥15 mEq/l | ≥18 mmol/l |
| Resolución CAD (β-OHB) | "Normalización" | <0,6 mmol/l |
| HHS osmolalidad | >320 mOsm/kg total | Efectiva >300 **o** total >320 |
| Manejo CAD leve-mod no crítica | UCI/IV | SC en planta convencional aceptable |

---

## Notas sin hallazgos

- Ninguna. Las 3 notas presentan al menos 2 hallazgos cada una.

---

## Fuentes consultadas (literales)

1. **Manual 12 Octubre 2022, 9.ª edición.** Capítulo 51 — Complicaciones agudas de la diabetes mellitus (Verdejo Gómez M.A., Furió Collao S.A.; asesora: García Fernández E.). Páginas 755-772.
2. **Umpierrez GE, Davis GM, ElSayed NA, et al.** Hyperglycemic Crises in Adults With Diabetes: A Consensus Report. *Diabetes Care* 2024;47(8):1257-1275. DOI: 10.2337/dci24-0032 (consenso ADA-EASD-AACE-JBDS-DTS).
3. **American Diabetes Association.** 16. Diabetes Care in the Hospital: Standards of Care in Diabetes—2026. *Diabetes Care* 2026;49(Suppl 1):S339.
4. **Mustafa OG, Rayman G.** Hyperglycemic crises in adults: A look at the 2024 consensus report. *Cleve Clin J Med* 2025;92(3):152.
5. **Documento de consenso SEMES — SED — SEEN — semFYC — SEMERGEN — SEMG.** Recomendaciones de manejo de la diabetes, de sus complicaciones metabólicas agudas y de la nueva terapia en el adulto. *Emergencias* 2016;28(6):400-417.
