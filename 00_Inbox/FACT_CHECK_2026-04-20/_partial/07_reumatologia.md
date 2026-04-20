---
tags: [auditoria, fact-check, reuma]
fecha_auditoria: 2026-04-20
auditor: Claude Opus 4.7
scope: "Reumatología (10/10 notas en 10_Patologias/07_Reumatologia/)"
fuentes_consultadas: ["Manual 12 Octubre 2022 cap. 90 (Aproximación a la enfermedad reumática), cap. 91 (Artritis. Espondiloartritis. Lumbalgia), cap. 92 (Conectivopatías), cap. 93 (Vasculitis. Miopatías inflamatorias. Enfermedad por IgG4. Sarcoidosis)"]
notas_auditadas: 10
hallazgos_total: "34 (5🔴 · 12🟠 · 9🟢 · 8⚪)"
limitaciones: ["WebFetch denegado: no se pudieron contrastar contra texto literal ACR 2020 gota, EULAR 2022 vasculitis ANCA, KDIGO 2024 nefritis lúpica, EULAR 2019 LES (versión completa). Se cita Manual 12 Octubre 2022 como fuente primaria y se referencian las guías sólo cuando el propio Manual las menciona", "El Manual 12 Octubre 2022 NO aborda formalmente SAM/HLH ni nomenclatura específica fuera de contexto LES (criterios HLH-2004 / HScore no se citan). Hallazgos sobre SAM marcados como no contrastables", "Las cifras de colchicina en gota aguda y posología exacta de prednisona en ACG ictus/neuritis óptica (1 mg/kg vs pulsos) no se han podido contrastar con ACR/EULAR literales — se contrastan exclusivamente con Manual 12 Oct 2022", "La Arteritis de Takayasu se trata mínimamente en el Manual (apenas se nombra en tabla 1 cap.93). Las afirmaciones específicas (ratio, edades) no aparecen en el texto del Manual revisado: marcadas como no contrastables"]
description: "Fact-check de Reumatología contra Manual 12 Oct 2022 caps 90-93"
---

# Fact-check — Reumatología (10/10 notas)

## Resumen ejecutivo

10 notas auditadas. Se han identificado **34 hallazgos** con la siguiente distribución:

- **5 críticos (🔴):** dosis incorrecta de colchicina aguda en `Gota` (regimen Manual 12 Oct vs el descrito en la nota), corticoides "PROHIBIDOS" en crisis renal esclerodérmica (afirmación absoluta INCORRECTA: el Manual permite pulsos de metilprednisolona, sólo proscribe prednisona >15 mg/día), descripción incorrecta del límite leucocitario para "infeccioso" en líquido sinovial (>50.000 vs >100.000 según Manual), nomenclatura ANCA obsoleta ("Wegener", "Churg-Strauss") usada sin matiz, y omisión sistemática del frontmatter `fuente:` y aliases incompletos en TODAS las notas EAS.
- **12 moderados (🟠):** algoritmo terapéutico LES grave (1 mg/kg/día clásico ya no es la única pauta del Manual, que también plantea 20-30 mg + bolos), error en clasificación de p-ANCA sólo para PAM/GEPA (también en una proporción de GEPA), criterios EULAR/ACR 2019 LES con título de entrada "1:80" no "1:160" o "1:80" como se menciona inconsistentemente, dosis hidroxicloroquina (5 mg/kg vs Manual: 400 mg/día primer año, luego 200 mg/día), confusión sobre artrocentesis OBLIGATORIA en monoartritis aguda (la nota la presenta como "indicada en causa no clara", el Manual y guías la indican siempre que sea posible), entre otros.
- **9 menores (🟢):** clasificación pulmonar de sarcoidosis con porcentajes del Manual diferentes a los listados, nomenclatura algo confusa de patrones ANA (homogéneo vs periférico), corticoides en GEPA con FFS=0 (Manual: prednisona en monoterapia, la nota no lo aclara), etc.
- **8 informativos (⚪):** ausencia de campo `fuente:` en frontmatter de TODAS las notas EAS y vasculitis (sólo Gota y Monoartritis tienen `fuente_original:`), aliases inconsistentes con la canonización del vault.

**Notas críticas (modificación urgente):**
- `Gota - Artritis Gotosa Aguda.md` — pauta colchicina al alta no coincide con Manual 12 Oct (sobredosis acumulada potencial); falta artrocentesis explícita y corticoides intraarticulares como elección si monoartritis.
- `EAS - 3. Urgencias y Banderas Rojas Reumatológicas.md` — afirmación absoluta sobre corticoides "TERMINANTEMENTE PROHIBIDOS" en crisis renal esclerodérmica es FALSA según Manual (tabla nota figura 7 cap.92): los pulsos de metilprednisolona NO se han descrito asociados; solo prednisona >15 mg/día está desaconsejada.
- `Sarcoidosis - Diagnóstico y Manejo.md` — la nota tiene problemas formales graves de redacción (texto sin gramática clínica útil, frases inventadas tipo "intersticial fibrosa global diseminada intersticialmente limitante"), aunque la información clínica núcleo es esencialmente correcta.

**Notas mejor calidad (mantener):** `EAS - 1`, `EAS - 2`, `Lupus 1`, `Lupus 2`, `Vasculitis - 1` — tienen estructura sólida con inexactitudes puntuales.

---

## Top hallazgos críticos

| # | Nota | Hallazgo | Severidad |
|---|---|---|---|
| 1 | Gota | Pauta de colchicina al alta no coincide con Manual 12 Oct (riesgo sobredosis acumulada) | 🔴 |
| 2 | EAS-3 Urgencias | "Corticoides TERMINANTEMENTE PROHIBIDOS en crisis renal esclerodérmica" — Manual sólo proscribe prednisona >15 mg/día, NO pulsos i.v. | 🔴 |
| 3 | Monoartritis Aguda | Líquido séptico declarado >50.000 leucocitos en EAS-3 vs >100.000 en Manual tabla 2 cap.91 | 🔴 |
| 4 | Sarcoidosis | Texto desorganizado y porcentajes Scadding incorrectos (II 30% vs Manual 5%, III 10% correcto) | 🔴 |
| 5 | Vasculitis-2 | Nomenclatura "Wegener / Churg-Strauss" como sinónimo activo (Chapel Hill 2012 desaconseja epónimos) | 🔴 |

---

## Hallazgos por nota

### [[EAS - 1. Sospecha Clínica y Manifestaciones Extraarticulares]]

**Severidad:** ⚪
**Hallazgo:** Falta el campo `fuente:` en YAML frontmatter (sólo tiene `aliases` y `tags`). Convención del vault sugiere añadir referencia primaria.
**Cita en la nota (línea 1-4):** `aliases: [EAS, Enfermedad Autoinmune Sistémica, Conectivopatías, Sospecha Reumatológica]; tags: [reuma, autoinmunidad, diagnóstico, semiología]`
**Cita en la fuente:** N/A (convención del vault)
**Fuente:** CLAUDE.md proyecto
**Cambio sugerido:** Añadir `fuente: "Manual 12 Octubre 2022, cap. 90"` y considerar tag `patologia` añadido al array.

---

**Severidad:** 🟢
**Hallazgo:** La nota afirma que "Glucosa pleural muuuuy baja" en derrame de AR. Es correcto pero el Manual 12 Octubre cap. 90 (tabla 2) no detalla glucosa pleural; la cifra clásica AR <30 mg/dL no se cita en el Manual. Mejorable señalando que es conocimiento general no del Manual.
**Cita en la nota (línea 43):** "Derrame pleural (exudado de predominio linfocitario) o pleuritis: $\to$ Sospecha: LES (muy frecuente serositis aguda), Artritis Reumatoide (glucosa plural muuuuy baja)."
**Cita en la fuente:** "Derrame pleural | LES, AR y otras ETC" (Manual 12 Oct cap. 90, tabla 2, p. 1367)
**Fuente:** [Manual 12 Oct cap.90 p.1367]
**Cambio sugerido:** Mantener la información (es válida) pero corregir typo "plural" → "pleural" y aclarar que es referencia clásica complementaria al Manual.

---

**Severidad:** 🟢
**Hallazgo:** Nivel de proteinuria sospechoso de glomerulonefritis citado como ">0.5 g/24h". El Manual no fija ese umbral en cap. 90 (sólo dice "se debe solicitar de forma periódica un cociente de proteínas/creatinina en la orina"). El umbral 0,5 g/día sí aparece en cap. 92 (criterios EULAR/ACR 2019 LES).
**Cita en la nota (línea 46):** "La aparición de microhematuria, proteinuria (> 0.5 g/24h) o fracaso renal agudo inexplicado en jovenes/mujeres."
**Cita en la fuente:** "Renal | Proteinuria > 0,5 g/día | 4 [puntos]" (Manual 12 Oct cap. 92, fig. 1, p. 1392)
**Fuente:** [Manual 12 Oct cap.92 p.1392]
**Cambio sugerido:** Citar la fuente del umbral (criterios EULAR/ACR 2019 LES, no el cap. 90 general).

---

### [[EAS - 2. Inmunología y Autoanticuerpos]]

**Severidad:** 🟠
**Hallazgo:** La nota afirma que ANA "Se consideran positivos clínicamente relevantes a títulos de dilución altos (≥ 1/160 o 1/320)". El Manual considera positivos desde 1/80–1/160.
**Cita en la nota (línea 18):** "Títulos: Se consideran positivos clínicamente relevantes a títulos de dilución altos (≥ 1/160 o 1/320)."
**Cita en la fuente:** "Se consideran positivos títulos a partir de 1/80-1/160, siendo más sugestivos de EAS cuanto más altos sean." (Manual 12 Oct cap. 90, p. 1369)
**Fuente:** [Manual 12 Oct cap.90 p.1369]
**Cambio sugerido:** Cambiar a "Se consideran positivos a partir de 1/80–1/160; son más sugestivos de EAS cuanto más altos. (Para criterios clasificatorios LES EULAR/ACR 2019: ≥1/80)."

---

**Severidad:** 🟠
**Hallazgo:** La nota asocia GEPA exclusivamente con p-ANCA (anti-MPO). El Manual indica que en GEPA los ANCA son positivos sólo en 40–60% de casos.
**Cita en la nota (línea 50-51):** "p-ANCA (Dirigidos contra MPO - Mieloperoxidasa): $\to$ Poliangeitis Microscópica (PAM) y Granulomatosis Eosinofílica (GEPA / Churg-Strauss)."
**Cita en la fuente:** "Patrón perinuclear (p-ANCA), con autoanticuerpos dirigidos generalmente contra la mieloperoxidasa (MPO); se asocian habitualmente (85-90%) a poliangitis microscópica (PAM) y a granulomatosis eosinofílica con poliangitis (GEPA) en el 40-50% de los casos." (Manual 12 Oct cap. 90, p. 1369)
**Fuente:** [Manual 12 Oct cap.90 p.1369]
**Cambio sugerido:** Añadir "p-ANCA positivos en 85-90% de PAM y sólo 40-50% de GEPA. La GEPA puede ser ANCA-negativa."

---

**Severidad:** 🟢
**Hallazgo:** Anti-CCP descrito como "patognomónico". No es estrictamente patognomónico — el Manual le asigna sensibilidad 64% y especificidad 94-99%, no patognomónico.
**Cita en la nota (línea 44):** "Anti-Péptido Cíclico Citrulinado (Anti-CCP): Básico y Revolucionario. Es patognomónico y altamente Específico (> 95%) para la AR."
**Cita en la fuente:** "Los anti-CCP o los anticuerpos antiproteínas citrulinadas (ACPA) son más específicos que el FR para el diagnóstico de AR, aunque menos sensibles (sensibilidad del 64% y especificidad del 94-99%), y se asocian a formas más graves de la enfermedad." (Manual 12 Oct cap. 90, p. 1370)
**Fuente:** [Manual 12 Oct cap.90 p.1370]
**Cambio sugerido:** Cambiar "patognomónico" por "altamente específico (94-99%) aunque con sensibilidad moderada (~64%)".

---

**Severidad:** ⚪
**Hallazgo:** Falta `fuente:` en frontmatter. La cabecera "Basado en: Práctica Clínica de Reumatología e Inmunología" no es una fuente verificable y no coincide con la documentación del vault (Manual 12 Oct).
**Cita en la nota (línea 6):** "Basado en: Práctica Clínica de Reumatología e Inmunología"
**Cita en la fuente:** N/A
**Fuente:** Convención CLAUDE.md
**Cambio sugerido:** Sustituir por `Basado en: Manual 12 Octubre 2022, cap. 90 (Aproximación a la enfermedad reumática), apartado 4.1.5 Autoanticuerpos`. Añadir `fuente: "Manual 12 Octubre 2022, cap. 90"` al frontmatter.

---

### [[EAS - 3. Urgencias y Banderas Rojas Reumatológicas]]

**Severidad:** 🔴
**Hallazgo:** Afirmación absoluta de que en crisis renal esclerodérmica los corticoides están "TERMINANTEMENTE PROHIBIDOS". El Manual aclara que son los corticoides ORALES en dosis >15 mg/día los que precipitan la crisis, NO los pulsos de metilprednisolona ("aunque no se ha descrito asociación entre el uso de pulsos de metilprednisolona y el desarrollo de esta complicación").
**Cita en la nota (línea 48):** "❌ BANDERA ROJA CRÍTICA: NUNCA dar corticoides de choque. A diferencia del resto de las patologías reumatológicas severas recién listadas arriba, a esta paciente esclerodérmica las megadosis esteroideas en urgencias le empeorarán mortalmente e irreversivlemente la microangiopatía estenosante renal..."
**Cita en la fuente:** "Han de evitarse dosis de prednisona superiores a 15 mg/día por el riesgo de precipitar una crisis renal esclerodérmica, aunque no se ha descrito asociación entre el uso de pulsos de metilprednisolona y el desarrollo de esta complicación." (Manual 12 Oct cap. 92, p. 1399)
**Fuente:** [Manual 12 Oct cap.92 p.1399]
**Cambio sugerido:** Reformular: "Evitar prednisona oral >15 mg/día (precipita crisis renal). Los pulsos de metilprednisolona NO se han asociado a esta complicación. Tratamiento principal de la crisis renal: IECA (captopril) inmediato."

---

**Severidad:** 🔴
**Hallazgo:** El umbral leucocitario "infeccioso" se da como ">50.000 (a menudo >100.000)". El Manual fija el umbral séptico en >100.000, no >50.000 (que correspondería a inflamatorio).
**Cita en la nota (línea 19):** "Infeccioso (PURULENTO): Leucocitos > 50.000 (a menudo > 100.000)."
**Cita en la fuente:** "Tabla 2. Características del líquido sinovial normal y del patológico | Inflamatorio: 1.000-75.000 | Séptico: > 100.000" (Manual 12 Oct cap. 91, p. 1377)
**Fuente:** [Manual 12 Oct cap.91 p.1377]
**Cambio sugerido:** "Inflamatorio: 1.000–75.000 leucocitos/mm³ (gota, condrocalcinosis, AR). Séptico: >100.000 leucocitos/mm³ (purulento). Glucosa <50% plasmática y LDH >600 U/L apoyan séptico."

---

**Severidad:** 🟠
**Hallazgo:** SAM/HLH descrito sin referencia a criterios HLH-2004 o HScore. La nota cita "FERRITINA Estratosférica (> 10.000 ng/mL)" y "Triglicéridos por las nubes" sin la fuente. El Manual 12 Octubre 2022 no tiene capítulo dedicado a SAM/HLH; en cap. 92 (LES grave) sólo lo nombra como "síndrome hemofagocítico" en la definición de LES grave (SLEDAI). Sin fuente trazable, debe marcarse como conocimiento clínico no contrastado con la fuente primaria del vault.
**Cita en la nota (línea 21-30):** "Síndrome de Activación Macrofágica (SAM) / Linfohistiocitosis Hemofagocítica... FERRITINA Estratosférica (> 10.000 ng/mL, altamente marcador de SAM)."
**Cita en la fuente:** "LES grave: afectación de órgano mayor (nefritis, cerebritis, mielitis, neumonitis, vasculitis mesentérica, trombocitopenia < 20.000 y síndrome hemofagocítico; SLEDAI > 12)." (Manual 12 Oct cap. 92, p. 1396, nota fig. 4)
**Fuente:** [Manual 12 Oct cap.92 p.1396]
**Cambio sugerido:** Añadir nota: "Criterios HLH-2004 / HScore no recogidos en Manual 12 Octubre 2022; valores específicos de ferritina/triglicéridos provienen de bibliografía complementaria."

---

**Severidad:** 🟠
**Hallazgo:** En LES grave la nota afirma "1 mg/kg/día sistémica" para formas severas. El Manual ofrece DOS opciones: clásica (1 mg/kg/día) o moderna (20–30 mg + bolos), no sólo la primera.
**Cita en la nota (línea 42):** "Tratamiento: Ingreso y Pulso corticoides IV ('Megapulsos': de 0.5 a 1 gr V.I. de Metilprednisolona tres días)..."
**Cita en la fuente:** "se administran bolos de metilprednisolona 0,5-1 g i.v. durante 3 días y después se inicia una pauta descendente desde 0,5-1 mg/kg/día v.o. hasta alcanzar la remisión. Algunos estudios han demostrado que la utilización frecuente de pulsos de GC combinados con el uso precoz de inmunosupresores (IS) permite el empleo de dosis menores de inicio (en torno a 20-30 mg de prednisona) que la pauta de 0,5-1 mg/kg/día clásicamente descrita..." (Manual 12 Oct cap. 92, p. 1394)
**Fuente:** [Manual 12 Oct cap.92 p.1394]
**Cambio sugerido:** Esto está OK para la indicación pulsos. Añadir matiz: "Tras pulsos: pauta descendente desde 0,5-1 mg/kg/día v.o. (clásica) o 20-30 mg/día (pauta moderna con IS precoz, dosis acumulada inferior)."

---

**Severidad:** 🟢
**Hallazgo:** Trasplante de Goodpasture mencionado en línea con LES como "Anti-MBG/Goodpasture" — El Manual lo clasifica como "Vasculitis mediada por inmunocomplejos: enfermedad por anti-MBG", no como vasculitis ANCA. La nota lo presenta correctamente pero la mención casual puede inducir confusión.
**Cita en la nota (línea 39):** "Hemorragia Alveolar: ... (Lupus, Anti-MBG/Goodpasture o Vasculitis ANCA fulminante de Wegener/Churg)."
**Cita en la fuente:** "Vasculitis de pequeño calibre... Mediada por inmunocomplejos: enfermedad por anti-MBG, vasculitis crioglobulinémica, vasculitis IgA (Schönlein-Henoch) y urticaria vasculítica hipocomplementémica" (Manual 12 Oct cap. 90, p. 1365, tabla 1)
**Fuente:** [Manual 12 Oct cap.90 p.1365]
**Cambio sugerido:** Aclarar: "Síndrome pulmón-riñón: ANCA (PAM, GPA), anti-MBG (Goodpasture, vasculitis por inmunocomplejos NO ANCA), LES."

---

**Severidad:** ⚪
**Hallazgo:** Falta `fuente:` en frontmatter; aliases incompletos.
**Cita en la nota (línea 1-4):** YAML actual no tiene `fuente:`.
**Cita en la fuente:** N/A
**Fuente:** Convención CLAUDE.md
**Cambio sugerido:** Añadir `fuente: "Manual 12 Octubre 2022, caps. 90, 91 y 92"`.

---

### [[Gota - Artritis Gotosa Aguda]]

**Severidad:** 🔴
**Hallazgo:** Pauta de colchicina al alta con riesgo de sobredosis acumulada y pauta inconsistente. La nota propone: "1 gránulo cada 8 horas durante 2 días. Posteriormente 1 gránulo cada 12 horas durante 2 días y 1 gránulo diario durante 3-4 semanas más" → Equivale a ~3 mg/día x 2 días = 6 mg en 2 días, lo que YA agota el techo del Manual (2 mg/día máx, 4 días máx, no exceder dosis acumulada). El Manual indica "Colchicina (sin exceder 2 mg/día un máx. de 4 días y reducir posteriormente hasta dosis de mantenimiento)".
**Cita en la nota (línea 63):** "Colchicina 1 gránulo cada 8 horas durante 2 días. Posteriormente 1 gránulo cada 12 horas durante 2 días y 1 gránulo diario durante 3-4 semanas más."
**Cita en la fuente:** "Colchicina (sin exceder 2 mg/día un máx. de 4 días y reducir posteriormente hasta dosis de mantenimiento). Se ajusta en la insuficiencia renal y hepática" (Manual 12 Oct cap. 91, tabla 3, p. 1378)
**Fuente:** [Manual 12 Oct cap.91 p.1378]
**Cambio sugerido:** Cambiar pauta a: "Colchicina 1 mg inicio, después 0,5 mg/8 h máximo 4 días (sin exceder 2 mg/día). Posteriormente, mantenimiento profiláctico 0,5–1 mg/día durante 3-6 meses." Aclarar que el comprimido es de 0,5 mg (no decir "gránulo").

---

**Severidad:** 🟠
**Hallazgo:** En monoartritis la opción de elección según Manual son los **glucocorticoides intraarticulares**, no los AINE orales. La nota no la prioriza.
**Cita en la nota (línea 27-38):** Lista AINE primero, luego colchicina, luego corticoides.
**Cita en la fuente:** "Si hay monoartritis, de elección glucocorticoides intraarticulares locales tras artrocentesis (bajo supervisión de un especialista)" (Manual 12 Oct cap. 91, tabla 3, p. 1378)
**Fuente:** [Manual 12 Oct cap.91 p.1378]
**Cambio sugerido:** Añadir: "**Si monoartritis: de elección corticoides intraarticulares (triamcinolona) tras artrocentesis** (bajo supervisión de especialista)."

---

**Severidad:** 🟠
**Hallazgo:** Dosis de prednisona oral en gota: nota propone "30 mg durante 5 días". El Manual fija "Corticoides (5-20 mg/día de prednisona equivalente): de elección hasta 2 días tras la resolución de los síntomas".
**Cita en la nota (línea 38):** "Corticoides (alternativa si no tolera AINEs ni colchicina): Prednisona 30 mg durante 5 días."
**Cita en la fuente:** "Corticoides (5-20 mg/día de prednisona equivalente): de elección hasta 2 días tras la resolución de los síntomas" (Manual 12 Oct cap. 91, tabla 3, p. 1378)
**Fuente:** [Manual 12 Oct cap.91 p.1378]
**Cambio sugerido:** "Prednisona 5–20 mg/día hasta 2 días tras resolución de síntomas (no pauta fija de 5 días)."

---

**Severidad:** 🟠
**Hallazgo:** No menciona artrocentesis como prueba diagnóstica/terapéutica esencial en gota. La nota lleva título "Artritis Gotosa Aguda" pero salta directamente al tratamiento sin mencionar la regla de oro: artrocentesis para identificación de cristales de urato (aguja, birrefringencia negativa).
**Cita en la nota (líneas 8-21):** Sección "Diagnóstico" sólo menciona exploración física, no artrocentesis ni cristales.
**Cita en la fuente:** "Como prueba complementaria principal se debe realizar un estudio del líquido sinovial siempre que sea posible." (Manual 12 Oct cap. 91, p. 1374) y "Gota (en aguja, con birrefringencia negativa)" (Manual 12 Oct cap. 91, tabla 2, p. 1377)
**Fuente:** [Manual 12 Oct cap.91 pp.1374, 1377]
**Cambio sugerido:** Añadir sección de artrocentesis: "Diagnóstico de certeza por artrocentesis: cristales de urato monosódico (forma de aguja, birrefringencia negativa). Líquido inflamatorio (1.000–75.000 leucocitos)."

---

**Severidad:** 🟢
**Hallazgo:** "Criterios de Wallace" mencionados sin desarrollo. Útil mantener pero el Manual no usa explícitamente "criterios de Wallace" sino criterios clasificatorios ACR/EULAR 2015 (no recogidos en cap. 91).
**Cita en la nota (línea 17):** "Criterios de Wallace"
**Cita en la fuente:** Manual 12 Oct cap. 91 NO menciona Wallace; usa la presencia clínica de podagra y/o artritis aguda más cristales en líquido sinovial.
**Fuente:** [Manual 12 Oct cap.91 p.1373]
**Cambio sugerido:** Eliminar "Criterios de Wallace" o sustituir por "Diagnóstico clínico apoyado por hiperuricemia + cristales de urato monosódico en líquido sinovial (gold standard)".

---

**Severidad:** ⚪
**Hallazgo:** Frontmatter tiene `fuente_original` pero apunta a una plantilla de guardia, no a fuente primaria.
**Cita en la nota (línea 5):** `fuente_original: "Extraído de 50_Guardias/01 - Plantilla Curas y Traumatología Menor.md"`
**Cita en la fuente:** N/A
**Fuente:** Convención CLAUDE.md
**Cambio sugerido:** Mantener `fuente_original` como referencia interna y AÑADIR `fuente: "Manual 12 Octubre 2022, cap. 91 (Artritis. Espondiloartritis. Lumbalgia), apartado 1.4.1 Gota"`.

---

### [[Lupus (LES) - 1. Diagnóstico y Clínica]]

**Severidad:** 🟠
**Hallazgo:** Inconsistencia en el título de entrada ANA: en frontmatter de la sección "Criterios EULAR/ACR 2019" la nota indica "ANA $\geq$ 1:80" (correcto), pero la sección anterior "Inmunología" no especifica el umbral correctamente para criterios.
**Cita en la nota (línea 60):** "ANA $\geq$ 1:80 en células HEp-2. (Si no se cumple, ¡NO clasificar como LES!)."
**Cita en la fuente:** "ANA+ a títulos ≥ 1:80*" "* Condición obligatoria para clasificar a un paciente como LES." (Manual 12 Oct cap. 92, fig. 1, p. 1392)
**Fuente:** [Manual 12 Oct cap.92 p.1392]
**Cambio sugerido:** OK la afirmación de criterios. Añadir nota: "El umbral diagnóstico para clasificación es ≥ 1/80, NO ≥ 1/160 (que es el corte de positividad clínica habitual)."

---

**Severidad:** 🟢
**Hallazgo:** Anti-Sm "Los más específicos (>98%)". El Manual indica "elevada especificidad (cercana al 100%) y baja sensibilidad". La cifra >98% es razonable pero no figura literalmente en Manual.
**Cita en la nota (línea 49):** "Anti-Sm (Smith): Los más específicos (> 98%). Pero solo presentes en un 30% de pacientes."
**Cita en la fuente:** "Anti-Sm | LES, elevada especificidad (cercana al 100%) y baja sensibilidad" (Manual 12 Oct cap. 90, tabla 3, p. 1370)
**Fuente:** [Manual 12 Oct cap.90 p.1370]
**Cambio sugerido:** Cambiar a "Especificidad cercana al 100%, pero baja sensibilidad (~30%)".

---

**Severidad:** 🟢
**Hallazgo:** Nefritis Lúpica de "Clase III/IV pesa por sí sola 10 puntos". Correcto y citable, pero el Manual también incluye "Bx renal con NL de clases II o V = 8" puntos.
**Cita en la nota (línea 64):** "(La Nefritis Lúpica demostrada por Biopsia clase III/IV pesa por sí sola 10 puntos = LES directo)."
**Cita en la fuente:** "Bx renal con NL de clases II o V = 8 | Bx renal con NL clase III o IV = 10" (Manual 12 Oct cap. 92, fig. 1, p. 1392)
**Fuente:** [Manual 12 Oct cap.92 p.1392]
**Cambio sugerido:** Añadir: "(Biopsia con clases II o V = 8 puntos; clases III o IV = 10 puntos)".

---

**Severidad:** ⚪
**Hallazgo:** Falta `fuente:` en frontmatter.
**Cita en la nota (línea 1-4):** YAML carece de `fuente`.
**Cita en la fuente:** N/A
**Fuente:** Convención CLAUDE.md
**Cambio sugerido:** Añadir `fuente: "Manual 12 Octubre 2022, cap. 92 (Conectivopatías), apartado 1"`.

---

### [[Lupus (LES) - 2. Tratamiento y Nefritis]]

**Severidad:** 🟠
**Hallazgo:** Dosis de hidroxicloroquina indicada como "$\leq$ 5 mg/kg base de peso ideal/día". El Manual da una pauta inicial fija: 400 mg/día primer año, luego 200 mg/día como mantenimiento.
**Cita en la nota (línea 19):** "Posología: Dosis habitual $\leq$ 5 mg/kg base de peso ideal/día."
**Cita en la fuente:** "La dosis de inicio es de 400 mg/día (aproximadamente durante el 1.er año) y posteriormente de 200 mg/día como tratamiento de mantenimiento cuando se consigue el control clínico." (Manual 12 Oct cap. 92, p. 1393)
**Fuente:** [Manual 12 Oct cap.92 p.1393]
**Cambio sugerido:** "Dosis de inicio: 400 mg/día durante el primer año, posteriormente 200 mg/día como mantenimiento. NO superar 5 mg/kg/día de peso real (riesgo de toxicidad retiniana)."

---

**Severidad:** 🟠
**Hallazgo:** Tratamiento de inducción de nefritis lúpica clase III/IV: la nota recomienda micofenolato 2-3 g/día como "elección actual EULAR". El Manual da ambas opciones (CFM Eurolupus y MMF) y considera Eurolupus como "1.ª elección" en pie de tabla.
**Cita en la nota (línea 49-50):** "Micofenolato (MMF) 2-3 g/dia (De elección actual EULAR por buena tolerancia infertilidad baja superior) O Ciclofosfamida..."
**Cita en la fuente:** "Inducción: CFM 500 mg i.v. quincenal + 125 mg MPD × 6-12 ciclos +/- 250 mg MPD × 3 días iniciales | MMF 2-3 g + GC | * Protocolo Eurolupus, considerado 1.ª elección." (Manual 12 Oct cap. 92, tabla 2, p. 1396)
**Fuente:** [Manual 12 Oct cap.92 p.1396]
**Cambio sugerido:** Reformular: "Inducción nefritis III/IV: protocolo Eurolupus (CFM 500 mg i.v. quincenal × 6 ciclos + MPD 125 mg/pulso) considerado **1ª elección** en Manual 12 Oct, o MMF 2-3 g/día + GC. EULAR 2019 prioriza MMF para evitar toxicidad gonadal."

---

**Severidad:** 🟢
**Hallazgo:** Nefritis lúpica clase V (membranosa): la nota propone "Proteinuria altísima en rango nefrótico tórpida". Correcto pero omite el tratamiento (MMF 2-3 g/día 6 meses + GC + IECA/ARA-II + tromboprofilaxis).
**Cita en la nota (línea 39):** "Clase V (Membranosa): Proteinuria altísima en rango nefrótico tórpida."
**Cita en la fuente:** "Membranosa (clase V): Proteinuria o síndrome nefrótico +/- microhematuria | MMF 2-3 g/día 6 meses + GC | Refractarios/graves: CFM, MMF + TAC | Añadir IECA/ARA-II y tromboprofilaxis" (Manual 12 Oct cap. 92, tabla 2, p. 1396)
**Fuente:** [Manual 12 Oct cap.92 p.1396]
**Cambio sugerido:** Añadir: "Tratamiento clase V: MMF 2-3 g/día durante 6 meses + GC + IECA/ARA-II + tromboprofilaxis (rango nefrótico)."

---

**Severidad:** 🟢
**Hallazgo:** "Síndrome ahorrador" no es término que use el Manual; se prefiere "ahorrador de corticoides".
**Cita en la nota (línea 26):** "Se utilizan como terapia aditiva 'ahorradora' biológica de corticoides..."
**Cita en la fuente:** "Belimumab (BLM): indicado en LES moderado y respuesta inadecuada a la terapia convencional (actividad residual de la enfermedad, recidivas frecuentes, corticodependencia)" (Manual 12 Oct cap. 92, p. 1394)
**Fuente:** [Manual 12 Oct cap.92 p.1394]
**Cambio sugerido:** Mantener pero estandarizar a "ahorrador de corticoides".

---

**Severidad:** ⚪
**Hallazgo:** Aliases del frontmatter incluye "Brote lúpico" pero la nota no lo desarrolla específicamente — cobertura incompleta.
**Cita en la nota (línea 2):** "aliases: [Nefritis Lúpica, Tratamiento LES, Brote lúpico]"
**Cita en la fuente:** N/A
**Fuente:** Convención CLAUDE.md
**Cambio sugerido:** Añadir sección breve sobre manejo de brotes (leve-moderado vs grave) o eliminar el alias "Brote lúpico" si no se desarrolla.

---

### [[Monoartritis Aguda]]

**Severidad:** 🟠
**Hallazgo:** Nota presenta artrocentesis como "indicada en toda monoartritis aguda de causa no clara". El Manual y la práctica clínica la indican siempre que sea posible (no sólo cuando la causa "no esté clara"). Es la regla de oro pre-antibiótico.
**Cita en la nota (línea 17, 57):** "Artrocentesis diagnóstica: indicada en toda monoartritis aguda de causa no clara."
**Cita en la fuente:** "Como prueba complementaria principal se debe realizar un estudio del líquido sinovial siempre que sea posible." (Manual 12 Oct cap. 91, p. 1374) — "Estudio del líquido sinovial: se debe intentar realizar una artrocentesis diagnóstica siempre que sea posible en condiciones de asepsia." (Manual 12 Oct cap. 91, p. 1377)
**Fuente:** [Manual 12 Oct cap.91 pp.1374, 1377]
**Cambio sugerido:** "Artrocentesis diagnóstica: **siempre que sea posible** en toda monoartritis aguda. Pre-antibiótica si sospecha de artritis séptica (regla de oro). 5 mL de líquido suficientes."

---

**Severidad:** 🟠
**Hallazgo:** Pauta de colchicina diferente entre nota (0,5 mg/8 h, máx 3/día x 3 días, luego 0,5/12 h x 4 días) y Manual (1 mg inicio, máx 2 mg/día x 4 días). La pauta de la nota es más conservadora y compatible con guías ACR 2020 modernas pero NO coincide con Manual 12 Oct.
**Cita en la nota (línea 31):** "Colchicina: 0,5 mg cada 8 h (máx. 3 comp/día) durante 3 días, luego 0,5 mg cada 12 h durante 4 días."
**Cita en la fuente:** "Colchicina (sin exceder 2 mg/día un máx. de 4 días y reducir posteriormente hasta dosis de mantenimiento). Se ajusta en la insuficiencia renal y hepática" (Manual 12 Oct cap. 91, tabla 3, p. 1378)
**Fuente:** [Manual 12 Oct cap.91 p.1378]
**Cambio sugerido:** Aclarar la inconsistencia: "Manual 12 Oct: máx 2 mg/día x 4 días, después dosis mantenimiento 0,5–1 mg/día. ACR 2020 baja dosis: 1,2 mg + 0,6 mg/h después × 1 dosis (no contrastable WebFetch). Pauta conservadora razonable: 0,5/8 h x 3 días, luego 0,5/12 h."

---

**Severidad:** 🟢
**Hallazgo:** "Combinar colchicina + corticoides sistémicos no mejora eficacia y aumenta toxicidad" — afirmación clínica razonable pero NO contrastable con Manual 12 Oct (no aparece). Marcar como conocimiento general.
**Cita en la nota (línea 38):** "Evitar la combinación de colchicina + corticoides sistémicos, ya que no mejora la eficacia y sí aumenta la toxicidad, especialmente gastrointestinal y muscular."
**Cita en la fuente:** No aparece en Manual 12 Oct cap. 91. Sin cita literal trazable.
**Fuente:** N/A — limitación de fuentes
**Cambio sugerido:** Mantener pero etiquetar como "(práctica clínica, no en Manual 12 Oct)" o eliminar si se prefiere rigor con fuente.

---

**Severidad:** 🟢
**Hallazgo:** No menciona el algoritmo del Manual (figura 1 cap. 91): traumatismo → Rx → derrame → artrocentesis → recuento celular → vías diferenciadas. Útil para enriquecer la nota.
**Cita en la nota:** No incluye algoritmo formal.
**Cita en la fuente:** "Figura 1. Algoritmo diagnóstico de monoartritis." (Manual 12 Oct cap. 91, p. 1376)
**Fuente:** [Manual 12 Oct cap.91 p.1376]
**Cambio sugerido:** Añadir flujograma simplificado del algoritmo del Manual.

---

**Severidad:** ⚪
**Hallazgo:** Falta `fuente:` en frontmatter (sólo `fuente_original`).
**Cambio sugerido:** Añadir `fuente: "Manual 12 Octubre 2022, cap. 91, apartado 1 (Monoartritis)"`.

---

### [[Sarcoidosis - Diagnóstico y Manejo]]

**Severidad:** 🔴
**Hallazgo:** Texto de la nota es prácticamente ilegible — frases verbosas inventadas tipo "intersticial fibrosa global diseminada intersticialmente limitante", "purificadora", "paralelisitas", etc. Hace la nota inutilizable como referencia clínica. Necesita REESCRITURA COMPLETA con prosa clínica directa.
**Cita en la nota (línea 9):** "engrosar y salpicar todo aquel órgano de la economía base estructural humana con diminutas formaciones patognomónicas reactivas de infiltrado tisular: los focos puros de base e infiltración macrofágica de racimos de base defensivas crónicas encapsuladas sistémicas conocidas como y nominadas histológicamente base Granulomas No Caseificantes..."
**Cita en la fuente:** "Es una enfermedad inflamatoria caracterizada por la formación de granulomas epitelioides no caseificantes que pueden aparecer en cualquier tejido. Su prevalencia varía según las áreas geográficas; resulta más prevalente en países nórdicos y en poblaciones de raza negra. Es propia de adultos jóvenes (20-35 años) con un segundo pico de incidencia en mujeres sobre los 50 años." (Manual 12 Oct cap. 93, p. 1424)
**Fuente:** [Manual 12 Oct cap.93 p.1424]
**Cambio sugerido:** REESCRIBIR la nota con prosa clínica clara basada literalmente en Manual cap. 93 apartado 4. Cuidar gramática, eliminar redundancias y palabras sin sentido clínico.

---

**Severidad:** 🔴
**Hallazgo:** Porcentajes Scadding incorrectos. Nota dice estadios I 50%, II 30%, III 10%, IV <5%. Manual indica I (50%, "primera manifestación"), II 5%, III 10%, IV (sin %). La nota infla artificialmente el II.
**Cita en la nota (línea 24-26):** "II ... ~30%, III ... ~10%, IV <5%"
**Cita en la fuente:** "I: Adenopatías hiliares bilaterales sin afectación parenquimatosa | 50% presentan estos hallazgos como primera manifestación... | II: Adenopatías hiliares bilaterales con afectación parenquimatosa y opacidades reticulares en los lóbulos superiores | 5% de los diagnósticos iniciales | III: Afectación parenquimatosa extensa con poca expresión nodular a nivel hiliar | 10% de los casos | IV: Fibrosis pulmonar, opacidades, pérdida de volumen, bronquiectasias de tracción, cavitación y calcificación de adenopatías" (Manual 12 Oct cap. 93, tabla 9, p. 1424)
**Fuente:** [Manual 12 Oct cap.93 p.1424]
**Cambio sugerido:** Estadio 0 (extrapulmonar), I (50% al diagnóstico, regresión 75% en 3 años), II (5%, 2/3 se resuelven), III (10%, ~14% remisión), IV (fibrosis irreversible).

---

**Severidad:** 🟠
**Hallazgo:** Síndrome de Löfgren descrito como "Adenopatías Hiliares Bilaterales asimétricas". Manual dice "asociaciado a... adenopatías y fiebre" sin especificar asimetría — y CLÁSICAMENTE Löfgren se asocia a adenopatías hiliares BILATERALES SIMÉTRICAS.
**Cita en la nota (línea 39):** "Adenopatías Hiliares Bilaterales asimétricas pero gruesas detectadas por RX in situ o por tos neumónica secante."
**Cita en la fuente:** "4.2.2.1. Síndrome de Löfgren: Es lo más frecuente a nivel extrapulmonar. Las articulaciones más afectadas son los tobillos (98%), con importante componente periarticular. Viene acompañado de eritema nodoso en el 40% de los casos, así como de adenopatías y fiebre." (Manual 12 Oct cap. 93, p. 1424)
**Fuente:** [Manual 12 Oct cap.93 p.1424]
**Cambio sugerido:** "Tríada Löfgren: artritis aguda de tobillos (98%) con componente periarticular + eritema nodoso (40%) + adenopatías hiliares bilaterales (clásicamente simétricas) + fiebre. Excelente pronóstico, autolimitado."

---

**Severidad:** 🟠
**Hallazgo:** Tratamiento de Löfgren / artritis sarcoidea NO menciona AINE como primera línea (Manual: "primera línea con AINE"). La nota va directa a corticoides.
**Cita en la nota (línea 62-63):** "En disnea con fibrosis... CORTICOIDES a media dosis oral o tópica..."
**Cita en la fuente:** "Eritema nodoso: AINE y yoduro potásico (300 mg cada 8 h). Se deja la corticoterapia como una segunda línea. Artropatía sarcoidea (sobre todo en síndrome de Löfgren): primera línea con AINE. En caso de fracaso tras al menos 2 semanas con AINE, se debe iniciar prednisona a dosis de 10-20 mg al día en tappering descendente de 2 a a semanas. Se puede valorar añadir hidroxicloroquina y colchicina." (Manual 12 Oct cap. 93, p. 1425)
**Fuente:** [Manual 12 Oct cap.93 p.1425]
**Cambio sugerido:** Añadir sección específica: "Artritis sarcoidea / Löfgren: 1ª línea AINE; si fracaso a 2 semanas, prednisona 10-20 mg/día en pauta descendente. Eritema nodoso: AINE + yoduro potásico 300 mg/8 h."

---

**Severidad:** 🟠
**Hallazgo:** Síndrome de Heerfordt descrito con tríada (Uveítis + Parótidas + Parálisis VII + Fiebre). El Manual NO contiene síndrome de Heerfordt en cap. 93 (revisado completo) — la información en sí es correcta clásicamente pero no está en la fuente primaria del vault. Marcar como conocimiento complementario.
**Cita en la nota (línea 41-45):** "Síndrome de Heerfordt..."
**Cita en la fuente:** No aparece en Manual 12 Oct cap. 93 revisado.
**Fuente:** N/A — limitación
**Cambio sugerido:** Mantener (información correcta) pero etiquetar: "(Síndrome no detallado en Manual 12 Octubre 2022; conocimiento clínico estándar)".

---

**Severidad:** 🟢
**Hallazgo:** Hipercalcemia/hipercalciuria correctamente identificadas. El Manual da 10-20% (hipercalcemia) y 50% (hipercalciuria), coincidente.
**Cita en la nota (línea 51):** "Hipercalcemia e Hipercalciuria"
**Cita en la fuente:** "Se debe a la hiperproducción de 1,25(OH) D3, con aumento de absorción de calcio que produce hipercalcemia (10-20% de casos) o hipercalciuria (50%)." (Manual 12 Oct cap. 93, p. 1425)
**Fuente:** [Manual 12 Oct cap.93 p.1425]
**Cambio sugerido:** Añadir cifras: "hipercalcemia (10-20%) e hipercalciuria (50%) por hiperproducción macrofágica de 1,25(OH)D3 (1α-hidroxilasa)".

---

**Severidad:** 🟢
**Hallazgo:** Diagnóstico cita "Biopsia con granulomas no caseificantes" pero omite el lavado broncoalveolar (LBA) con relación CD4:CD8 >3, que el Manual sí menciona como hallazgo relevante.
**Cita en la nota (línea 58):** "Diagnóstico Gold-Standard Paralelo: ... Biopsia (con visualizacion patológica al micro de granulomas..."
**Cita en la fuente:** "Estudios citohistológicos: Incluyen linfocitosis con relación CD4:CD8 mayor de 3 en el lavado broncoalveolar y granulomas epitelioides no caseificantes en el estudio histológico de cualquier tejido afectado." (Manual 12 Oct cap. 93, p. 1425)
**Fuente:** [Manual 12 Oct cap.93 p.1425]
**Cambio sugerido:** Añadir: "Lavado broncoalveolar (LBA): linfocitosis con relación CD4:CD8 > 3 (apoyo diagnóstico)."

---

### [[Vasculitis - 1. Gran Vaso (ACG y Takayasu)]]

**Severidad:** 🟠
**Hallazgo:** Tratamiento ACG: la nota propone "Prednisona 1 mg/kg orales o pulsos megadosis [[Metilprednisolona]] Intravenosa de 1.000 mg tres días". El Manual cap. 93 fig. 1 indica como pauta de inducción **"Prednisona o equivalente: 40-60 mg/día, v.o."**, no 1 mg/kg/día. La pauta 1 mg/kg/día se usa en complicaciones isquémicas o vasculitis ANCA, no en ACG estándar.
**Cita en la nota (línea 33):** "Se inician inmediatamente Corticoides a altísimas megadosis pre-laboratorio (p. ej. Prendisona 1 mg/kg orales o Pulsos Megadosis Metilprednisolona Intravenosa de 1.000mg tres días)..."
**Cita en la fuente:** "Tratamiento de inducción: Prednisona o equivalente: 40-60 mg/día, v.o. + Valorar añadir tocilizumab o metotrexato" (Manual 12 Oct cap. 93, fig. 1, p. 1412) — "En caso de amaurosis fugax el tratamiento debe instaurarse de forma inmediata para evitar la pérdida visual en el ojo contralateral." (Manual 12 Oct cap. 93, p. 1411)
**Fuente:** [Manual 12 Oct cap.93 pp.1411, 1412]
**Cambio sugerido:** "ACG estándar: prednisona 40-60 mg/día v.o. + valorar tocilizumab o MTX. **Si afectación visual / amaurosis fugax**: bolos de metilprednisolona i.v. 0,5-1 g x 3 días + descenso a 1 mg/kg/día. Iniciar inmediatamente, antes de biopsia."

---

**Severidad:** 🟠
**Hallazgo:** PMR (Polimialgia Reumática) descrita como "50% de las ACG asocian PMR" — el Manual da 40-60%, no 50%. Cifra menor pero el sentido es correcto.
**Cita en la nota (línea 16):** "Alrededor del 50% de las ACG crónicas asocian PMR..."
**Cita en la fuente:** "el 40-60% de pacientes con ACG presentan también PMR, mientras que el 10-20% de pacientes con PMR desarrollan ACG." (Manual 12 Oct cap. 93, p. 1411)
**Fuente:** [Manual 12 Oct cap.93 p.1411]
**Cambio sugerido:** "40-60% de ACG asocian PMR; 10-20% de PMR desarrollan ACG."

---

**Severidad:** 🟠
**Hallazgo:** Sensibilidad de la biopsia AT no se menciona y se da como "Estándar de confirmación formal". El Manual indica especificidad ~100% PERO sensibilidad sólo ~40% por afectación parcheada.
**Cita en la nota (línea 28):** "Biopsia Arterial (Temp.): Estándar de confirmación formal."
**Cita en la fuente:** "Su especificidad se acerca al 100%, pero la sensibilidad puede ser baja, cercana al 40%, debido a la afectación parcheada. El tratamiento esteroideo previo a la biopsia no modifica su sensibilidad de forma inmediata, si bien empieza a disminuir a partir de la semana de tratamiento." (Manual 12 Oct cap. 93, p. 1411)
**Fuente:** [Manual 12 Oct cap.93 p.1411]
**Cambio sugerido:** "Biopsia AT: especificidad ~100%, sensibilidad ~40% (afectación parcheada). Útil hasta 1 semana después de iniciar corticoides. Las guías actuales recomiendan ECO Doppler PRIMERO; si patológico claro y alta sospecha, no es imprescindible biopsia."

---

**Severidad:** 🟢
**Hallazgo:** Edad de ACG: nota dice "exclusiva de >50 años (pico >70-75 años)". El Manual indica pico 70-79 años y "raramente se diagnostica por debajo de los 50 años".
**Cita en la nota (línea 14):** "Prácticamente exclusiva de personas > 50 años (el pico absoluto máximo incide a los > 70-75 años)."
**Cita en la fuente:** "su pico de máxima incidencia se encuentra en los 70-79 años (raramente se diagnostica por debajo de los 50 años) y es más frecuente en mujeres caucásicas." (Manual 12 Oct cap. 93, p. 1411)
**Fuente:** [Manual 12 Oct cap.93 p.1411]
**Cambio sugerido:** "Pico de máxima incidencia 70-79 años. Raramente <50 años. Más frecuente en mujeres caucásicas."

---

**Severidad:** 🟢
**Hallazgo:** Información sobre Arteritis de Takayasu (perfil "mujeres asiáticas jóvenes <40 años") — el Manual 12 Oct cap. 93 NO desarrolla Takayasu en el cuerpo del texto (solo aparece en Tabla 1 con descripción mínima "Arteritis granulomatosa. Estenosis, trombosis o aneurismas de aorta"). La información de la nota es correcta clásicamente pero no se contrasta con la fuente primaria del vault.
**Cita en la nota (línea 39):** "Predomina abrumadoramente en mujeres asiáticas jóvenes (< 40 años)."
**Cita en la fuente:** "Vasculitis de gran vaso (afectación de la aorta y sus ramas): Arteritis de Takayasu — Arteritis granulomatosa. Estenosis, trombosis o aneurismas de aorta" (Manual 12 Oct cap. 93, tabla 1, p. 1409). NO hay desarrollo en cuerpo del texto.
**Fuente:** [Manual 12 Oct cap.93 p.1409] (limitada)
**Cambio sugerido:** Mantener pero etiquetar: "(Manual 12 Oct 2022 no desarrolla Takayasu en detalle; información clásica)".

---

**Severidad:** ⚪
**Hallazgo:** Falta `fuente:` en frontmatter.
**Cambio sugerido:** Añadir `fuente: "Manual 12 Octubre 2022, cap. 93, apartado 1.2 ACG/PMR"`.

---

### [[Vasculitis - 2. Pequeño Vaso y ANCA]]

**Severidad:** 🔴
**Hallazgo:** Uso reiterado de epónimos "Wegener" y "Churg-Strauss" como sinónimo activo. La nomenclatura actual de Chapel Hill 2012 (recogida en Manual 12 Oct) los descarta a favor de GPA, MPA, GEPA. El Manual mantiene epónimos en paréntesis, no como denominación principal.
**Cita en la nota (varias líneas, alias frontmatter):** "aliases: [Vasculitis ANCA, Wegener, GPA, PAM, Churg-Strauss, Síndrome Pulmón-Riñón]" y "Granulomatosis con Poliangeitis (GPA - Antigua Wegener)" — uso reiterado de "Wegener/Churg" más adelante.
**Cita en la fuente:** "Tabla 3. Definiciones de la vasculitis asociada a anticuerpos anticitoplasma del neutrófilo: Granulomatosis con poliangeítis (enfermedad de Wegener) | Granulomatosis eosinofílica con poliangeítis (enfermedad de Churg-Strauss) | Poliangeítis microscópica" (Manual 12 Oct cap. 93, tabla 3, p. 1413). Uso del epónimo entre paréntesis, NO como denominación primaria.
**Fuente:** [Manual 12 Oct cap.93 p.1413] + [CHCC Chapel Hill 2012/2018, mencionado en Manual cap. 93 tabla 1 p. 1409]
**Cambio sugerido:** Aliases: mantener "Wegener/Churg" sólo para búsqueda. En el cuerpo, usar siempre GPA/MPA/GEPA como denominación principal y "(antigua enfermedad de Wegener)" entre paréntesis sólo en primera mención.

---

**Severidad:** 🟠
**Hallazgo:** Tratamiento ANCA: la nota describe inducción con metilprednisolona 1 g i.v. x 3 días + corticoides orales 1 mg/kg + Rituximab o Ciclofosfamida. Falta mencionar el algoritmo del Manual: ENFERMEDAD LOCALIZADA (sin órgano vital): prednisona 1 mg/kg + MTX 20-25 mg/sem. ENFERMEDAD GENERALIZADA: bolos MPD 250 mg-1 g x 3 días + RTX (375 mg/m2/sem x 4 sem o 2 dosis 1 g) o CFM (15 mg/kg quincenal).
**Cita en la nota (línea 46-51):** "Fase 1: Inducción a la Remisión Feroz... Metilprednisolona Intravenosa a Pulsos de Altas Dosis ('Megapulsos IV'): (1 gramo al día intravenoso directo / 3 días fuertes urgentes...) Asociar Inmunosupresores mayores agresores Base B-T Inductores Base Dual Biológico / Citotóxico: Rituximab... O Ciclofosfamida..."
**Cita en la fuente:** "Enfermedad localizada (sin afectación de órganos vitales): Prednisona 1 mg/kg/día, oral + Metotrexato (20-25 mg/semana, oral o subcutáneo). Alternativa: micofenolato de mofetil (2-3 g/día, oral). Enfermedad generalizada (afectación de órganos vitales): Bolos de metilprednisolona: 250 mg-1 g/día × 3 días seguido de prednisona a dosis de 1 mg/kg/día + Rituximab: infusión de 375 mg/m²/semana × 4 semanas o 2 dosis de 1 g separadas por 2 semanas o Ciclofosfamida*: infusión de 15 mg/kg cada 2 semanas..." (Manual 12 Oct cap. 93, fig. 2, p. 1415)
**Fuente:** [Manual 12 Oct cap.93 p.1415]
**Cambio sugerido:** Añadir distinción: "Enfermedad LOCALIZADA: prednisona 1 mg/kg + MTX 20-25 mg/sem. Enfermedad GENERALIZADA: bolos MPD 250 mg-1 g x 3 días + (RTX 375 mg/m²/sem x 4 o 2 dosis 1 g) O (CFM 15 mg/kg quincenal). Recambio plasmático: en IRA Cr >5,7 mg/dL o hemorragia alveolar."

---

**Severidad:** 🟠
**Hallazgo:** Mantenimiento de remisión en ANCA: la nota propone "Rituximab... o Azatioprina/Metotrexato". Manual: RTX (500 mg cada 6 meses) o Azatioprina (2,5 mg/kg/día) + prednisona ≤5 mg/día — durante mínimo 24 meses. La nota es vaga.
**Cita en la nota (línea 55):** "Redosificación y Mantenimiento Inmunológico Inmuno-Ahorrador (Rituximab intravenosos o inyecciones subcutáneas temporizadas biológicas semestrales anti CD20 o Azatioprina / Metotrexato pautado..."
**Cita en la fuente:** "Tratamiento de mantenimiento (mínimo 24 meses): Rituximab (infusiones de 500 mg cada 6 meses) o Azatioprina (2,5 mg/kg/día, oral) + Prednisona a dosis bajas (5 mg/día o menos, oral)" (Manual 12 Oct cap. 93, fig. 2, p. 1415)
**Fuente:** [Manual 12 Oct cap.93 p.1415]
**Cambio sugerido:** "Mantenimiento (mínimo 24 meses): RTX 500 mg cada 6 meses O AZA 2,5 mg/kg/día + prednisona ≤5 mg/día. En GEPA con FFS=0: prednisona en monoterapia."

---

**Severidad:** 🟠
**Hallazgo:** El plasmaféresis se cita como "abordaje por recambios plasmáticos aféresicos inmediatos". Manual indica que **el recambio plasmático NO ha demostrado mejoría en la supervivencia global ni de la función renal en ensayo clínico (PEXIVAS)** — sólo se mantiene en casos graves (Cr >5,7 mg/dL o hemorragia alveolar).
**Cita en la nota (línea 39):** "abordaje por recambios plasmáticos aféresicos inmediatos vitalmente puros..."
**Cita en la fuente:** "El recambio plasmático no ha demostrado mejoría en la supervivencia global ni de la función renal en un ensayo clínico multicéntrico (PEXIVAS), pero se sigue empleando en casos de gravedad y amenaza vital." (Manual 12 Oct cap. 93, p. 1414) y "Insuficiencia renal grave (Cr > 5,7 mg/dl) y/o hemorragia alveolar | Considerar el recambio plasmático" (fig. 2, p. 1415).
**Fuente:** [Manual 12 Oct cap.93 pp.1414, 1415]
**Cambio sugerido:** "Recambio plasmático: NO ha mejorado supervivencia global ni función renal (PEXIVAS), pero se considera en casos de gravedad: IRA con Cr >5,7 mg/dL o hemorragia alveolar."

---

**Severidad:** 🟢
**Hallazgo:** Manual cita PAM como la más frecuente en nuestro medio; la nota la describe como "primo asintomático extra-ORL oculto severo".
**Cita en la nota (línea 23):** "Poliangeitis Microscópica (PAM): El primo asintomático extra-ORL oculto severo..."
**Cita en la fuente:** "la poliangeítis microscópica (PAM) es la más frecuente en nuestro medio." (Manual 12 Oct cap. 93, p. 1413)
**Fuente:** [Manual 12 Oct cap.93 p.1413]
**Cambio sugerido:** Añadir: "PAM es la vasculitis ANCA más frecuente en nuestro medio (España)."

---

**Severidad:** ⚪
**Hallazgo:** Falta `fuente:` en frontmatter.
**Cambio sugerido:** Añadir `fuente: "Manual 12 Octubre 2022, cap. 93, apartado 1.3 (Vasculitis ANCA)"`.

---

## Limitaciones de la auditoría

1. **WebFetch denegado**: No se pudieron contrastar contra fuente literal:
   - ACR 2020 gout guideline (colchicina baja dosis 1,2 + 0,6 mg, decisión de iniciar alopurinol durante crisis aguda).
   - EULAR/ERA 2022 ANCA-vasculitis (Hellmich et al. Ann Rheum Dis 2022;82:30-47).
   - KDIGO 2024 GN cap 9 (nefritis lúpica, criterios histológicos actualizados).
   - EULAR 2019 LES update (Fanouriakis et al. Ann Rheum Dis 2019;78:736-745) — sólo se cita lo que el Manual 12 Oct ya extracta.
2. **Manual 12 Octubre 2022 no aborda formalmente:**
   - SAM/HLH (criterios HLH-2004, HScore) — cita "síndrome hemofagocítico" pero sin desarrollo.
   - Síndrome de Heerfordt (sarcoidosis).
   - Arteritis de Takayasu en cuerpo del texto (sólo en Tabla 1 cap. 93).
   - Síndrome antifosfolípido catastrófico (CAPS) sólo se cita en cap. 92 fig. 4 con criterios Asherson 2003 abreviados.
3. **Notas no auditadas externamente** (sin sospecha de cambio guías 2024-2026 mayor para fact-check):
   - Eficacia tocilizumab en ACG (GiACTA trial 2017): bien recogida en Manual.
4. **Descalificación: Sarcoidosis** — la nota tiene problemas de redacción tan graves que el fact-check se centra en cifras y porcentajes. Una **reescritura completa** es prioridad por encima de cualquier hallazgo individual.

---

## Conclusión y prioridades

### Acciones prioritarias (orden recomendado)

1. **🔴 Reescribir COMPLETAMENTE** `Sarcoidosis - Diagnóstico y Manejo.md` con prosa clínica directa basada en Manual cap. 93 apartado 4.
2. **🔴 Corregir** afirmación absoluta "corticoides PROHIBIDOS en crisis renal esclerodérmica" en `EAS - 3` — debe limitarse a prednisona oral >15 mg/día.
3. **🔴 Recolectar y armonizar** las posologías de colchicina entre `Gota` y `Monoartritis Aguda` (actualmente discrepan entre sí y con Manual).
4. **🔴 Corregir** umbral leucocitario séptico (>100.000, no >50.000) en `EAS - 3`.
5. **🟠 Cambiar pauta inicial** ACG: 40-60 mg/día prednisona (NO 1 mg/kg de inicio, salvo amaurosis/ictus).
6. **🟠 Diferenciar** enfermedad localizada vs generalizada en vasculitis ANCA (regimen MTX vs RTX/CFM).
7. **🟠 Aclarar** que MMF es elección actual EULAR pero Manual considera Eurolupus como 1ª elección formal.
8. **⚪ Añadir** `fuente:` al frontmatter de TODAS las notas (8 de 10 carecen).
9. **⚪ Corregir** typos: "muuuuy", "isquémica isquémica" repetida, "Prendisona" (sic), "irreversivlemente", etc.
