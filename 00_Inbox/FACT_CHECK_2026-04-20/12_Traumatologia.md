---
tags: [auditoria, fact-check, trauma]
fecha_auditoria: 2026-04-20
fuentes_consultadas: [POLITRAUMA FJD v0 (HUFJD_09.01P005, nov 2023), Manual 12 Octubre 2022 cap 2 (Politrauma p.19-33), Manual 12 Octubre 2022 cap 91 (Lumbalgia p.1386-1389), Manual 12 Octubre 2022 cap 70 (Heridas/IPPB p.1040-1050), Manual 12 Octubre 2022 cap 4 (Dolor y sedoanalgesia)]
notas_auditadas: 15
hallazgos_total: "21 (3 🔴 · 9 🟠 · 4 🟢 · 5 ⚪)"
---

# Fact-check — Traumatología

## Resumen

Auditoría de las 15 notas de `10_Patologias/12_Traumatologia/`. La mayoría son plantillas de guardia (anamnesis + exploración + tratamiento al alta) y por su naturaleza tienen pocos errores de hechos clínicos (los planes terapéuticos para patología menor coinciden con la práctica habitual y no se contradicen con las fuentes consultadas). Los hallazgos críticos se concentran en:

1. **`Esguince de Tobillo.md`**: la nota cita "criterios Ottawa" pero NO los enumera. Esto es un omitido crítico (la regla es la base diagnóstica para decidir Rx en tobillo). Además la clasificación I/II/III por presencia/ausencia de hematoma e inestabilidad está simplificada en exceso.
2. **`Lumbalgia.md` y `Lumbociática.md`**: red flags incompletas (faltan dolor nocturno, edad > 50, traumatismo, fiebre como signo de alarma sistémico — algunos están parcialmente recogidos pero la nota no lista la tabla completa que sí está en Manual 12 Oct).
3. **`Heridas y Suturas.md`**: NO incluye profilaxis tetánica (esquema según vacunación + herida limpia/tetanígena) NI profilaxis antibiótica de mordeduras. Es una omisión crítica para una nota que pretende ser referencia de guardia.

Los planes analgésicos (paracetamol/AINE/metamizol/tramadol) son razonables y conformes a práctica habitual; no se documentan errores de dosis. El esquema de derivación a Traumatología en fractura costal (≥3 fracturas o volet) es coherente con el Manual 12 Oct (que considera "tórax inestable / volet costal" criterio de activación de equipo de trauma — p.28, Tabla "Criterios anatómicos").

---

## Hallazgos por nota

---

### 1. `Cervicalgia Mecánica.md`

#### 🟠 Moderado — Falta criterio NEXUS / Canadian C-Spine para indicar Rx cervical

La nota contempla cervicalgia mecánica y termina con "Tras radiografía cervical sin aparente patología ósea aguda…", pero no incorpora ningún criterio reglado para decidir cuándo está indicada la Rx (o TC) cervical, que es justamente la decisión clave en una guardia.

**Fuente — Manual 12 Octubre 2022, cap 2, Tabla 7 (p.30):**

> "Tabla 7. Criterios clínicos de retirada del collarín cervical
> Cumple los criterios NEXUS:
> - El paciente se encuentra consciente (GCS 15) y plenamente atento y colaborador
> - No existe evidencia clínica/analítica de intoxicación
> - No presenta déficits neurológicos
> - No refiere dolor a la palpación de la columna cervical
> - No tiene lesiones distrayentes o dolor por otra causa
> Aplica las Canadian Cervical Spine Rule:
> - No presenta los siguientes factores de riesgo: Edad > 65 años; Mecanismo de alto riesgo (caída desde > 1 m o 5 escaleras, colisión de vehículo > 100 km/h, vuelco o expulsión del vehículo, bicicleta y/o atropello)
> - Presencia de factores de bajo riesgo que permiten una movilización segura: Alcance posterior simple; Sentado en Urgencias; Ambulatorio; Inicio tardío del dolor; Ausencia de contractura en la musculatura paracervical
> - Capacidad para girar la cabeza a ambos lados 45°"

**Acción sugerida**: añadir bloque "> [!warning] Red flags / Criterios para Rx cervical" enumerando NEXUS y Canadian C-Spine.

#### 🟢 Menor — "Tizadinina" debería ser "Tizanidina"

Errata ortográfica en el principio activo (línea 28 de la nota). Correcto: **tizanidina** (relajante muscular agonista α2-adrenérgico).

#### ⚪ Informativo

Mejoraría añadir referencia explícita a fuente (`fuente: Manual 12 Oct 2022 cap 2`).

---

### 2. `Contusión y Fractura Costal.md`

#### 🟢 Menor — "Tizadinina" → "Tizanidina"

Misma errata ortográfica que en cervicalgia (línea 47).

#### ⚪ Informativo — Volet costal

La nota define volet costal como "≥ 3 fracturas". Más estrictamente, el volet costal es la fractura de **3 o más costillas consecutivas en al menos 2 puntos cada una**, lo que crea un segmento de pared torácica con respiración paradójica. La definición de "≥ 3 fracturas" es una simplificación útil para guardia pero conviene matizarlo.

**Fuente — Manual 12 Octubre 2022, cap 2, p.28 (Figura 9, criterios anatómicos de activación de equipo de trauma):**

> "Tórax inestable (volet costal)" — listado como criterio anatómico de activación.

**Fuente — POLITRAUMA FJD v0, p.6 (sección B: ventilación):**

> "Tórax inestable
> Contusión pulmonar
> Fracturas costales"
> y "valorar la frecuencia respiratoria y áreas de inestabilidad que provoquen áreas de respiración paradójica (volet costal)."

La indicación de la nota de derivar a traumatología si ≥3 fracturas o volet es coherente con la práctica. La sección de recomendaciones (ejercicios respiratorios, no usar fajas, dormir incorporado) es razonable y no contradice fuentes.

---

### 3. `Contusión y Fractura de 5º Dedo del Pie.md`

#### ⚪ Informativo — Sin hallazgos

No se identifican errores de hecho clínico. Sindactilia como inmovilización funcional + control radiográfico no presencial por traumatología es práctica habitual; no contradice fuentes consultadas. La nota es muy concreta y autocontenida.

---

### 4. `Coxalgia - Dolor de Cadera.md`

#### 🟠 Moderado — Dato de exploración inconsistente

En la sección "Exploración" (línea 17) se lee:

> "No alteración cutánea, no hematoma, **deformidad y acortamiento de miembro afecto en rotación externa**."

La frase está mal redactada/ambigua: "deformidad y acortamiento en rotación externa" es la presentación clásica de **fractura de cadera (cuello femoral)** — no es algo que deba aparecer en una exploración "normal" de coxalgia que termina con "Radiografías: No lesiones óseas agudas". Si la plantilla pretende reflejar exploración normal, debe decir "**no** deformidad y **no** acortamiento". Si pretende reflejar fractura, el resto del texto (sin Rx aguda, alta a domicilio) es incoherente.

Esta confusión es relevante porque la fractura de cadera con acortamiento + rotación externa nunca debería ir de alta a domicilio.

**Fuente — Manual 12 Octubre 2022, cap 2, p.28 (Figura 9, criterios anatómicos):**

> "Lesión penetrante proximal a codo/rodilla; (…) Amputación traumática proximal a tobillo/muñeca; Ausencia de pulso o parálisis de alguna extremidad" — ejemplos de criterios anatómicos de activación de trauma.

**Acción sugerida**: corregir la línea para que indique exploración normal con "no deformidad, no acortamiento, no rotación externa" o, alternativamente, escribir un bloque explícito "[!warning] Red flag — Sospecha de fractura de cadera: acortamiento + rotación externa de extremidad → Rx urgente, NO alta a domicilio".

#### 🟢 Menor — Erratas ortográficas

- "sobresfuerzos" (varias veces) → "sobreesfuerzos"
- "frio" → "frío"
- "dia" → "día"

---

### 5. `Esguince de Tobillo.md`

#### 🔴 Crítico — Ottawa Ankle Rules citadas pero NO desarrolladas

La nota dice (línea 20):

> "Rx de tobillo para descartar fractura (criterios Ottawa)."

No enumera las Ottawa Ankle Rules. Para una nota cuya función es ser referencia rápida en guardia, la cita sin contenido convierte el criterio en inútil. Los Ottawa Ankle Rules son la regla de decisión clínica con mayor evidencia para indicar Rx en traumatismos de tobillo y pie (sensibilidad ≈100% para fracturas clínicamente significativas).

**No se ha podido obtener cita literal de fuente externa** (WebFetch denegado en esta sesión y el Manual 12 Octubre 2022 no incluye un capítulo específico de patología osteoarticular traumática menor con Ottawa). Por la regla inviolable de fuente, **se recomienda completar este hallazgo consultando la fuente original** (Stiell IG, et al. JAMA 1994 / Ann Emerg Med) o protocolo SECOT/RCEM antes de cerrar el fact-check de esta nota. La criticidad se mantiene como 🔴 porque la omisión es objetiva (la nota cita la regla y no la desarrolla).

**Acción sugerida**: añadir la regla literal con cita a la publicación original o, mientras se obtiene fuente verificada, marcar el bloque como "pendiente de citar fuente".

#### 🟠 Moderado — Clasificación I/II/III demasiado simplificada

La nota clasifica esguinces así:

> "Grado I: Lesión leve, sobreestiramiento con micro-roturas. NO hematoma.
> Grado II: Lesión moderada, rotura parcial del ligamento. HEMATOMA.
> Grado III: Lesión grave, rotura completa del ligamento. HEMATOMA e INESTABILIDAD."

La clasificación clínica habitual (Kannus, AAOS) se basa en **estabilidad articular y capacidad de carga**, no en presencia/ausencia de hematoma (que es muy variable y depende del tiempo desde el trauma). Un esguince grado I puede tener hematoma si han pasado 24-48 h, y un grado III reciente puede no haber desarrollado hematoma todavía.

**No se ha podido obtener cita literal externa** en esta sesión (limitaciones de WebFetch y de Manual 12 Oct para este tema). Marcar como pendiente de fuente para ampliación.

#### 🟠 Moderado — Falta criterio de carga precoz / bota walker

La nota indica vendaje compresivo + tobillera + reposo deportivo 2 semanas, pero no aborda explícitamente la **carga precoz** (recomendación actual para grados I-II) ni el uso de **bota walker** en grados II-III. Es información práctica relevante para alta de urgencias.

**Pendiente de fuente externa para citar literal.**

#### ⚪ Informativo

URL de YouTube en línea 57. Aceptable como recurso complementario.

---

### 6. `Gonalgia y Lesión Ligamentosa de Rodilla.md`

#### 🟠 Moderado — Falta criterio de Rx (Ottawa Knee Rules) y derivación urgente

La nota describe maniobras exploratorias correctamente y diferencia gonalgia simple vs sospecha ligamentosa, pero:

- No incluye **Ottawa Knee Rules** ni **Pittsburgh Knee Rules** para indicar Rx (criterios análogos a tobillo).
- En la sospecha ligamentosa, el plan al alta es idéntico al de gonalgia simple ("derivación a traumatología si persiste el dolor tras una semana"). Una rotura completa de LCA o luxación rotuliana suele requerir derivación urgente ortopédica antes de una semana, no esperar a control en 4-5 días por MAP.

**Fuente — Manual 12 Octubre 2022 no aborda específicamente Ottawa Knee Rules**; pendiente de cita externa para incluir el criterio.

#### ⚪ Informativo — Hemartros

La definición clínica diferencia "tumefacción" de "hemartros" pero la plantilla de exploración NO contiene el dato de "hemartros precoz" como red flag (rotura LCA, fractura osteocondral, luxación rotuliana). Mejoraría añadirlo.

---

### 7. `Heridas y Suturas.md`

#### 🔴 Crítico — Falta profilaxis tetánica

La nota es la referencia de guardia para suturas/curas y NO menciona en absoluto la profilaxis antitetánica (esquema vacunal Td + IGT según historia vacunal y tipo de herida limpia/tetanígena). Esto es la decisión obligada en toda herida atendida en urgencias.

**Fuente — Manual 12 Octubre 2022, cap 70, Tabla 5, "Celulitis por mordedura" (p.1045):**

> "Profiláctico (sin celulitis) en pacientes de riesgo. Valorar profilaxis antitetánica y antirrábica. Humana: extraer serologías VIH, VHB y VHC y valorar profilaxis postexposición al VIH según el riesgo."

El Manual 12 Octubre menciona "valorar profilaxis antitetánica" pero no incluye el esquema completo. **El esquema oficial debe consultarse en el Ministerio de Sanidad** ("Vacunación en adultos. Recomendaciones. Vacuna de difteria y tétanos. Actualización 2017") **antes de cerrar este hallazgo con cita literal**. Marcado como crítico porque la omisión en una nota de heridas es de seguridad clínica.

**Acción sugerida**: añadir tabla con esquema simplificado:
- Vacunación correcta (≥3 dosis): herida limpia → nada (refuerzo si > 10 a desde última dosis); herida tetanígena → Td si > 5 a desde última dosis; IGT solo si herida de alto riesgo + inmunodeprimido.
- Vacunación incompleta o desconocida: Td + completar pauta. IGT en heridas tetanígenas.

#### 🔴 Crítico — Falta profilaxis antibiótica en mordeduras

La nota titula "Heridas y Suturas" y trata herida incisa "limpia/sucia" pero no aborda el manejo específico de mordeduras (humana, perro, gato), que es escenario frecuente en guardia y exige cobertura antibiótica empírica + valoración de cierre diferido.

**Fuente — Manual 12 Octubre 2022, cap 70, Tabla 1 (p.1041) y Tabla 5 (p.1045):**

> "Mordeduras:
> - Humanas: estreptococos del grupo viridans, anaerobios (Fusobacterium spp. y Bacteroides spp.) y característicamente Eikenella corrodens
> - Perro: Pasteurella spp. (Pasteurella canis, Pasteurella multocida y Pasteurella stomatis) y Capnocytophaga canimorsus (microorganismo encapsulado; riesgo de sepsis fulminante en asplenia)
> - Gato: Pasteurella multocida y Bartonella henselae"

> "Celulitis por mordedura: Amoxicilina/ácido clavulánico 875/125 mg/8-12 h v.o. o 1 g/200 mg/8 h i.v. o moxifloxacino 500 mg/24 h. Profiláctico (sin celulitis) en pacientes de riesgo. Valorar profilaxis antitetánica y antirrábica."

> Nota a pie de Tabla 5: "Mordeduras por gato (alto riesgo de osteomielitis), inmunodeprimidos, asplenia, cirrosis, en la región facial o sobre un edema previo, daño axonal previo o intensa destrucción tisular." (p.1045)

**Acción sugerida**: añadir sección "Mordeduras" con dosis y criterios de profilaxis antibiótica (de elección amoxicilina/clavulánico) y mención a profilaxis antirrábica.

#### 🟠 Moderado — Limpieza con clorhexidina vs povidona

La nota indica "limpieza de herida con SSF y solución yodada (betadine)" (línea 23). El Manual 12 Octubre matiza que en piel intacta se recomienda clorhexidina jabonosa al 2-4 % o acuosa al 0,5-1 % en piel no intacta, y específicamente desaconseja povidona en úlceras por presión.

**Fuente — Manual 12 Octubre 2022, cap 70, p.1043 (1.4.1.1. Medidas generales):**

> "Se debe limpiar la superficie, haciendo especial hincapié en la eliminación de cuerpos extraños y de las heridas contaminadas, con suero salino y clorhexidina (sobre piel intacta jabonosa al 2-4%; sobre piel no intacta, con clorhexidina acuosa al 0,5-1%)."

**Fuente — Manual 12 Octubre 2022, cap 70, Tabla 7 "Manejo de las úlceras por presión", apartado "Medidas generales" (p.1049):**

> "Evitar povidona yodada, agua oxigenada y clorhexidina (citotóxicos en el tejido sano)"

(El comentario sobre evitar es para úlceras crónicas, no para heridas agudas, pero la primera elección de antiséptico para limpieza de herida aguda en el Manual es clorhexidina, no povidona.)

**Acción sugerida**: matizar que la primera elección es clorhexidina y la povidona/betadine es alternativa.

#### 🟢 Menor — Tiempos de retirada de sutura

La nota indica:
> "Retirada de los puntos en 7 días. *3-7 días (cara-cuello) / 7-10 días (cuero cab.) / 8-10 días (tórax y M.sup) / 10-12 días (espalda, M.Inf)."

Estos rangos son razonables y coherentes con la práctica habitual. No se ha podido contrastar con fuente literal en esta sesión.

---

### 8. `Lumbalgia.md`

#### 🟠 Moderado — Red flags incompletas

La nota presenta callout con red flags:
> "Síndrome de cola de caballo: anestesia en silla de montar, disfunción vesical, incontinencia vesical o rectal, pérdida de fuerza o sensibilidad progresivas en MMII. Fiebre o síntomas sistémicos. Antecedentes de cáncer."

El Manual 12 Oct enumera explícitamente más signos de alarma:

**Fuente — Manual 12 Octubre 2022, cap 91, Tabla 10 (p.1387):**

> "Tabla 10. Signos y síntomas de alarma en la lumbalgia
> Antecedentes: Manipulación instrumental; Usuarios de drogas por vía parenteral; Infección previa; Inmunosupresión; Neoplasia; Traumatismo reciente
> Síntomas: Dolor inflamatorio o de intensidad progresiva; Pérdida de fuerza o sensibilidad en los miembros inferiores; Incontinencia de esfínteres; Fiebre; Síndrome constitucional
> Signos: Afectación motora de los miembros inferiores; Síndrome de «cola de caballo»; Masa o soplo abdominal; Fiebre; Adenopatías"

Faltan en la nota: manipulación instrumental, UDVP, inmunosupresión, dolor inflamatorio/progresivo, masa/soplo abdominal, adenopatías.

#### 🟠 Moderado — Indicaciones de Rx no listadas

La nota indica "una vez descartada patología ósea aguda" en el resumen evolutivo pero no especifica cuándo está indicada la Rx en lumbalgia. El Manual es categórico:

**Fuente — Manual 12 Octubre 2022, cap 91, p.1387 (4.3.3. Pruebas complementarias):**

> "Pruebas de imagen: no se aconsejan si no existen datos de alarma (tabla 11)."

**Fuente — Manual 12 Octubre 2022, cap 91, Tabla 11 (p.1388):**

> "Tabla 11. Indicaciones de la radiografía simple en el estudio de la lumbalgia
> - Mayores de 50 años
> - Antecedentes de neoplasia previa o activa
> - Tratamiento crónico con corticoides
> - Uso de tóxicos (alcohol o usuarios de drogas por vía parenteral)
> - Historia de traumatismo previo
> - Dolor en reposo, nocturno o acompañado de rigidez matutina
> - Déficit neurológico: paresia de alguna extremidad, hiperreflexia, compromiso vesical, anestesia «en silla de montar», etc.
> - Síndrome constitucional
> - Fiebre
> - Ausencia de mejoría tras 2-4 semanas de tratamiento conservador adecuado"

**Acción sugerida**: añadir sección "Cuándo solicitar Rx lumbar" con esta lista.

#### ⚪ Informativo — Tratamiento conservador y reposo

La nota recomienda "no superar los 3-4 días en cama". El Manual matiza:

**Fuente — Manual 12 Octubre 2022, cap 91, p.1388 (4.4.1):**

> "Se desaconseja el reposo absoluto durante más de 2 días ya que puede debilitar al paciente."

Diferencia 2 vs 3-4 días. Coherencia en concepto general (evitar reposo absoluto prolongado), pero el límite del Manual es más conservador (2 días).

#### 🟢 Menor — Yurelax / Tizanidina / Diazepam

La nota usa "Yurelax 10 mg cada 8 h" como relajante muscular. Yurelax® = ciclobenzaprina. La dosis máxima recomendada en ficha técnica es 10 mg/8 h pero por periodos cortos (≤ 2-3 semanas). Aceptable como pauta corta.

---

### 9. `Lumbociática.md`

#### 🟠 Moderado — Tabla de niveles radiculares: pequeña imprecisión sensitiva en L3-L4

La nota indica:
> "L3-L4 | 5% | Femoral → cuádriceps (dificultad subir escaleras) | Hipoestesia medial pantorrilla"

La afectación sensitiva clásica de L4 es la **cara medial de la pierna y maléolo medial**, no específicamente "medial de la pantorrilla". Es una descripción imprecisa. El reflejo afectado típico (rotuliano) tampoco está mencionado.

**No se ha podido obtener cita literal de fuente externa específica para este nivel** en esta sesión (Manual 12 Oct cap 91 trata lumbalgia pero no detalla los dermatomas radiculares). Pendiente.

#### 🟠 Moderado — Test de Lasègue: sensibilidad y umbral

La nota indica:
> "Lasègue es dudoso si el dolor irradiado aparece a partir de 70º"

El Manual define el test con criterios distintos:

**Fuente — Manual 12 Octubre 2022, cap 91, p.1387 (4.3.2):**

> "Es de especial utilidad el test de Lasègue, que orienta a patología radicular con sensibilidad mayor del 90% (positivo en caso de dolor agudo irradiado hacia la pierna en la flexión de cadera/pelvis entre 30° y 60° con la rodilla en extensión)"

Es decir, el rango de positividad es **30°-60°**. La nota sitúa el "dudoso" a partir de 70°, lo que sugiere que un dolor a 60-70° aún sería positivo, cuando para el Manual ya estaría fuera del rango clásico de positividad. La descripción es funcional en práctica pero no coincide exactamente con el Manual.

#### 🟢 Menor — Mismo problema que `Lumbalgia.md`

Red flags incompletas (faltan los mismos elementos de la Tabla 10).

#### ⚪ Informativo — Pauta corticoide

La nota recomienda "Prednisona 30 mg durante tres días, 1 día 15 mg, otro 10 mg y cortar" y cita Jiménez Murillo 2023 con dexametasona. La evidencia para corticoides en ciática aguda es controvertida. El Manual 12 Oct no incluye corticoides como pauta de primera línea en lumbociática (sí en compresión medular). Aceptable como pauta corta supervisada.

---

### 10. `Omalgia - Dolor de Hombro.md`

#### 🟢 Menor — Errata

"Impigment" → "Impingement" (línea 40).

#### ⚪ Informativo — Sin hallazgos críticos

Las maniobras exploratorias (Apley, Jobe, impingement, brazo cruzado) y la diferenciación tendinitis/articular son razonables. La derivación de patología que requiera valoración traumatológica no está explicitada como criterio reglado.

---

### 11. `Patología de Codo.md`

#### 🟢 Menor — Errata anatómica

Línea 14:
> "Tinel en canal epitrocleano (depresión entre olécranon y epicóndilo lateral)"

El canal epitrocleano (canal cubital) está entre el olécranon y la **epitróclea (epicóndilo medial)**, no el epicóndilo lateral. La epitróclea ES el epicóndilo medial. Errata anatómica.

Línea 33-34 repite el mismo error:
> "(entre el olécranon y epicóndilo lateral hay una depresión que es este canal donde por ahí pasa el nervio cubital)"

El nervio cubital pasa por el canal epitrocleano, **medial** (entre olécranon y epitróclea/epicóndilo medial).

**Acción sugerida**: corregir "lateral" → "medial" en ambas menciones.

#### ⚪ Informativo — Sin hallazgos adicionales

---

### 12. `Patología de Muñeca.md`

#### ⚪ Informativo — Sin hallazgos

Maniobras (tabaquera anatómica, telescopaje, Tinel, Phalen) coherentes. Plan razonable. La indicación de inmovilización en sospecha de fractura de escafoides con Rx negativa (yeso antebraquial-pulgar y nueva Rx en 10-14 días) NO aparece y sería una mejora, pero no es un error.

---

### 13. `Tendinitis - Plantilla General.md`

#### ⚪ Informativo — Sin hallazgos

Es plantilla genérica. No hay datos clínicos verificables que auditar más allá del esquema básico (movilidad pasiva dolorosa = articular; activa = tendinosa). El esquema es correcto.

---

### 14. `Traumatismo de Dedo de Mano.md`

#### ⚪ Informativo — Sin hallazgos

Maniobras (Finkelstein, varo/valgo IF, exploración de tendones flexores) coherentes. La pauta analgésica y el uso de sindactilia/muñequera en espina son razonables.

---

### 15. `Traumatismo General - Plantilla.md`

#### 🟠 Moderado — La plantilla NO refleja el algoritmo ABCDE para politrauma

La nota se llama "Traumatismo General - Plantilla" pero su contenido es una plantilla de informe para traumatismo **menor** (anamnesis, exploración local, alta con analgesia). NO contiene el algoritmo ABCDE, ni criterios de activación de equipo de trauma, ni FAST/E-FAST, ni manejo de la triada de la muerte (hipotermia/acidosis/coagulopatía). El nombre de la nota induce a confusión: el verdadero "traumatismo general" en urgencias es el politrauma.

**Fuente — POLITRAUMA FJD v0, p.5-10 (Evaluación Primaria ABCDE):**

> "4.1 A: vía aérea y estabilización de la columna cervical: A todo paciente politraumatizado que acuda a Urgencias se le colocará sobre una camilla de cuchara (…) la primera actuación será la colocar un collarín cervical rígido estilo Philadelphia con control mandibular (…)"
>
> "4.2 B: ventilación (breathing): Este apartado está especialmente diseñado para detectar con premura algunas patologías que amenazan la función pulmonar: Neumotórax a tensión, Hemotórax, Tórax inestable, Contusión pulmonar, Fracturas costales."
>
> "4.3 C: circulación y atención a la hemorragia: en cualquier politraumatizado la hipotensión debe considerarse secundaria a hipovolemia mientras no se demuestre lo contrario."
>
> "4.4 D: evaluación neurológica (disability): Nivel de conciencia según la escala de coma de Glasgow (3 a 15)."
>
> "4.5 E: exposición y control ambiental (environment): (…) Recordar que muchos serán pacientes que han perdido sangre, el pH tiende a bajar, y la hipotermia tiende a agravar el círculo vicioso (TRIADA DE LA MUERTE) de hipotermia, acidosis, alteración de la coagulación."

**Fuente — POLITRAUMA FJD v0, p.8 (pruebas radiológicas):**

> "A todo paciente y sobre todo si muestra signos de inestabilidad se le realizará ecografía según el esquema extended fast (EFAST). Esta ecografía la realizará el equipo de ecografía de Urgencias (…)
> 1. Las 2 cúpulas diafragmáticas buscando el sliding pleural (…) descarta la presencia de neumotórax a tensión.
> 2. Presencia de derrame pericárdico de gran cuantía que pueda evolucionar a un taponamiento cardiaco (…)
> 3. Búsqueda de líquido libre peritoneal que nos pone en el camino de sospechar lesión visceral intrabdominal."

**Acción sugerida**: o bien renombrar la nota a "Traumatismo Menor - Plantilla", o bien ampliarla con un bloque explícito de algoritmo ABCDE + E-FAST + activación de trauma. Dado que el Manual 12 Oct y el PDF Politrauma FJD ya cubren el politrauma extensamente, otra opción es enlazar a `[[POLITRAUMA FJD]]` y `[[Manual 12 Oct - Cap 2]]` en la sección "Ver también".

#### ⚪ Informativo — Falta mención a ácido tranexámico y transfusión masiva

NO se mencionan en la nota (ni en ninguna del módulo Trauma) ácido tranexámico (1 g iv en 10 min en las primeras 3 h, recomendación CRASH-2) ni protocolo de transfusión masiva. **El PDF Politrauma FJD v0 tampoco los menciona explícitamente** (revisado todo el PDF, p.1-12), por lo que no procede exigirlo desde esa fuente. El Manual 12 Octubre 2022 cap 2 tampoco los detalla. Pendiente de cita externa (CRASH-2 / NICE) para incluirlo como mejora.

---

## Notas SIN hallazgos

- `Contusión y Fractura de 5º Dedo del Pie.md`
- `Patología de Muñeca.md`
- `Tendinitis - Plantilla General.md`
- `Traumatismo de Dedo de Mano.md`

(El resto tiene al menos un hallazgo, según se desglosa arriba.)

---

## Limitaciones de la auditoría

1. **WebFetch denegado** durante esta sesión: no he podido recuperar cita literal de:
   - Ottawa Ankle Rules (paper original Stiell 1994 o protocolo RCEM/AAOS).
   - Esquema oficial de profilaxis tetánica del Ministerio de Sanidad (PDF en mscbs.gob.es).
   - Clasificación AAOS/Kannus de esguinces grado I/II/III.
   - Ottawa Knee Rules.
   Los hallazgos relacionados (esguince tobillo Ottawa, heridas profilaxis tetánica, gonalgia Ottawa Knee) se han mantenido como críticos/moderados por la objetividad de la omisión, pero requieren completar la cita literal en una segunda pasada con acceso web.

2. **Manual 12 Octubre 2022 carece de capítulo dedicado a patología osteoarticular traumática menor** (esguinces, fracturas, ortopedia ambulatoria). Cubre politrauma (cap 2), aparato locomotor reumatológico (cap 91, lumbalgia incluida), infecciones de piel (cap 70) y osteomielitis (cap 71). Para Ottawa rules y profilaxis tetánica detallada se requiere fuente externa.

3. **PDF POLITRAUMA FJD v0 (nov 2023) leído íntegramente (12 páginas).** No menciona ácido tranexámico ni protocolo de transfusión masiva específico. Confirma ABCDE, E-FAST, triada de la muerte y criterios de activación. Es un protocolo de actuación organizativa más que un protocolo terapéutico exhaustivo.

---

## Conteo final

| Categoría | Nº |
|---|---|
| 🔴 Críticos | 3 (Esguince tobillo Ottawa; Heridas profilaxis tetánica; Heridas mordeduras) |
| 🟠 Moderados | 9 |
| 🟢 Menores | 4 |
| ⚪ Informativos | 5 |
| **TOTAL** | **21 hallazgos en 11 notas con observaciones** |
