# Prompts para auditar las guías MUST con OpenEvidence

Copia uno de los dos bloques de abajo y pégalo **entero** en OpenEvidence (mejor de uno en uno). Cada bloque ya incluye el texto actual de la guía, así que no tienes que pegar nada más. Si quieres que conteste solo lo esencial, añade al final: «Resume en los 5 cambios más importantes».

---

## Prompt 1 — MUST Disnea

```
Eres médico adjunto de Medicina de Urgencias. Audita esta guía de bolsillo —escrita para un residente de primer año (R1) en la primera valoración de un paciente de guardia en un hospital español (Madrid)— frase por frase, contra las guías de práctica clínica VIGENTES.

Para CADA problema, responde así:
• Fragmento: «cita literal del texto»
• Tipo: error | desactualizado | impreciso | omisión | mejora
• Gravedad: alta | media | baja
• Problema: qué está mal o qué falta y por qué importa en urgencias.
• Corrección: el texto corregido o el añadido, CONCRETO y en el mismo registro breve de texto plano (no reescribas toda la guía; dosis en mg o mg/kg, con vía e intervalo).
• Fuente: guía concreta + año (+ clase/nivel de recomendación si aplica).

Reglas:
1) Prioriza guías EUROPEAS (ESC) y ESPAÑOLAS (SEC, SEMES, GEMA, GALAXIA, SEPAR) cuando existan; usa AHA/ACC/GINA/GOLD como complemento y AVISA cuando la recomendación europea/española difiera de la americana (dosis, umbrales o fármacos).
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
3) NO marques como error estas decisiones DELIBERADAS del autor: (a) el umbral de aviso se deja como rango «FC > 100-110 lpm»; (b) no se usa la escala HEART; (c) el síndrome aórtico se deriva al adjunto sin detallar el ADD-RS; (d) estilo conciso de texto plano, de bolsillo.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

DISNEA EN GUARDIA — GUÍA RÁPIDA PARA EL R1

Primero asegura vía aérea, oxigenación y ventilación; el diagnóstico exacto viene después. Esta guía te orienta con el paciente que respira pero está sintomático, y te dice cuándo el caso se te escapa de las manos.


CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR

Una mirada de 10 segundos y las constantes. Avisa de inmediato, y no te quedes solo con el paciente, si hay:
- SpO2 < 90% pese a oxígeno, o desaturación progresiva.
- FR > 30 rpm (taquipnea extrema si > 40) o FR < 10 rpm (agotamiento).
- PAS < 90 mmHg o crisis hipertensiva extrema.
- Trabajo respiratorio intenso: musculatura accesoria, respiración abdominal paradójica, habla entrecortada, no tolera el decúbito.
- Cianosis central, mala perfusión, o alteración del nivel de consciencia (agitación hipóxica o somnolencia hipercápnica).
- Estridor o sospecha de obstrucción de la vía aérea alta (angioedema, anafilaxia, cuerpo extraño): emergencia de vía aérea, pide ayuda ya.
- Dolor torácico o síncope acompañando a la disnea.


QUÉ PREGUNTAR

La meta es orientar hacia cardíaco, pulmonar, pleural-mecánico, metabólico o psicógeno.
- Tiempo: súbita en segundos-minutos orienta a TEP, neumotórax, edema agudo de pulmón, arritmia o cuerpo extraño; en horas-días, a infección respiratoria, EPOC o asma agudizados, derrame o insuficiencia cardíaca. ¿Es la primera vez o ya le ha pasado?
- Postura y esfuerzo (muy rentables): ¿empeora al tumbarse (ortopnea) o se despierta de noche ahogado y tiene que sentarse (disnea paroxística nocturna)? Orienta a insuficiencia cardíaca. ¿Cuánto esfuerzo aguanta? ¿Oye pitos? Orienta a broncoespasmo.
- Síntomas acompañantes: dolor pleurítico (TEP, neumotórax, neumonía); tos con fiebre y esputo purulento (infección) o esputo rosado y espumoso (edema agudo de pulmón); hemoptisis (TEP, neoplasia, infección); dolor e hinchazón de UNA pierna (TVP, que apoya TEP); ortopnea con edemas y nicturia (insuficiencia cardíaca); ansiedad con parestesias y suspiros (hiperventilación, siempre por exclusión).
- Antecedentes y medicación: cardiopatía, IC, fibrilación auricular, EPOC, asma, tabaquismo, oxigenoterapia domiciliaria, enfermedad tromboembólica o cáncer, diabetes (cetoacidosis), anemia, insuficiencia renal. ¿Toma o ha dejado diuréticos, inhaladores o anticoagulación? Posible exposición a monóxido de carbono (braseros, varios convivientes con cefalea). Revisa la receta electrónica.


QUÉ EXPLORAR (menos de 2 minutos)

Recuerda: una exploración normal NO descarta enfermedad.
- Cuenta la FR durante 30 segundos; mira el trabajo respiratorio, la cianosis y la ingurgitación yugular (IC, taponamiento, cor pulmonale).
- Auscultación pulmonar: sibilancias espiratorias difusas (asma o EPOC); crepitantes bibasales (edema agudo de pulmón o IC) o focales con fiebre (neumonía); hipofonesis unilateral con matidez (derrame) o con timpanismo (neumotórax).
- Auscultación cardíaca: ritmo (arritmia), soplos, tercer ruido o galope (IC).
- Piernas: edemas simétricos con fóvea (IC) frente a empastamiento unilateral doloroso (TVP).
- Si sospechas vía aérea alta: mira orofaringe, úvula y cuello (angioedema).


QUÉ PRUEBAS PEDIR

- Pulsioximetría y gasometría (arterial o venosa): hipoxemia, hipercapnia y estado ácido-base. Una acidosis metabólica con el pulmón limpio orienta a cetoacidosis, sepsis o tóxicos.
- ECG de 12 derivaciones: arritmia, isquemia (SCA como equivalente anginoso). En el TEP lo más frecuente es la taquicardia sinusal; los signos de sobrecarga derecha (S1Q3T3, T negativas de V1 a V4) aparecen solo en casos graves, así que su ausencia no descarta TEP.
- Radiografía de tórax: condensación (neumonía), líneas B, derrame o redistribución (IC), neumotórax, masa. Una radiografía normal NO excluye TEP, asma grave ni acidosis.
- Analítica con hemograma y bioquímica (anemia, función renal, iones, glucosa; TSH si procede).
- Péptidos natriuréticos si sospechas IC: rule-out agudo NT-proBNP < 300 o BNP < 100. Rule-in por edad (ESC 2021, solo NT-proBNP): > 450 (< 50 años), > 900 (50-75 años) o > 1.800 (> 75 años). En obesidad los cortes bajan en torno a un 50%.
- TEP: probabilidad con Wells o Geneva; si es baja o intermedia, dímero-D con el corte ajustado a edad (edad x 10 ng/ml en mayores de 50 años): por debajo descarta TEP sin imagen. Si es alta, angio-TC directa.
- Ecografía a pie de cama (POCUS) si está disponible (líneas B en IC, derrame, neumotórax, TEP con sobrecarga derecha). Espirometría con test broncodilatador, en circuito no urgente (asma reversible frente a EPOC).


TRATAMIENTO INICIAL (mientras valoras o avisas)

Medidas generales: incorpora al paciente, monitoriza, coge vía y extrae analítica/gasometría, haz una glucemia capilar inmediata, y pon oxígeno con objetivo de SpO2 94-98% (88-92% si es EPOC o retenedor de CO2).

Según la sospecha:
- Broncoespasmo (asma o EPOC): salbutamol nebulizado 2,5-5 mg + bromuro de ipratropio 0,5 mg, repetible cada 20 minutos la primera hora (o salbutamol en cámara, 4-8 pulsaciones). Corticoide sistémico precoz: prednisona 40-50 mg por vía oral (o, si no tolera, metilprednisolona 40-60 mg IV o hidrocortisona 100-200 mg IV). En la crisis asmática grave que no responde, sulfato de magnesio 2 g IV en 20 minutos. En la agudización de EPOC: antibiótico si cumple criterios de Anthonisen (≥ 2 de aumento de disnea, del volumen o de la purulencia del esputo; sobre todo si hay purulencia), y valora VMNI precoz —con el adjunto— si hay insuficiencia respiratoria hipercápnica (pH < 7,35 con hipercapnia).
- Edema agudo de pulmón / insuficiencia cardíaca: sienta al paciente, oxígeno o VMNI si lo precisa, y furosemida IV en bolo lento (20-40 mg si es de novo; 1-2 veces su dosis oral diaria si ya la tomaba). Si la PAS es mayor de 110 mmHg, nitroglicerina (sublingual 0,4 mg o en perfusión IV); evítala si la PAS es menor de 90 mmHg o hay estenosis aórtica severa. NO uses morfina de rutina.
- TEP de alta sospecha: oxígeno y, con el adjunto, anticoagulación con enoxaparina 1 mg/kg cada 12 h SC (1 mg/kg cada 24 h si FG < 30 ml/min), si no hay contraindicación, mientras confirmas con imagen.
- Anafilaxia (disnea con urticaria/angioedema o tras un alérgeno): adrenalina 0,5 mg IM en la cara anterolateral del muslo (concentración 1 mg/ml, 1:1000), repetible cada 5-15 minutos; la adrenalina IV en perfusión queda reservada a la anafilaxia refractaria y exige monitorización. No la retrases dando antes corticoide o antihistamínico (son solo coadyuvantes). Coloca al paciente en decúbito con las piernas elevadas, oxígeno y fluidos. Es box vital: avisa.
- Neumonía: oxígeno e inicia antibiótico empírico precoz según el protocolo del centro y la gravedad (CURB-65); no lo demores si hay datos de sepsis.
- Neumotórax a tensión: emergencia de procedimiento (descompresión). Avisa de inmediato.

Y recuerda: la disnea por ansiedad o hiperventilación es siempre un diagnóstico de exclusión.


FUENTES (para el residente; puedes borrar este bloque antes de compartir)
- Manual 12 de Octubre 2022, cap. 22 y 15; notas y fichas de fármacos del vault.
- Guías: ESC 2021/2023 insuficiencia cardíaca (NT-proBNP, furosemida, nitroglicerina); GEMA 5.5 asma y GOLD 2026 EPOC (salbutamol, ipratropio, corticoide, oxígeno); ESC 2019 / AHA 2026 TEP (dímero-D ajustado a edad); GALAXIA 2022 anafilaxia (adrenalina).
```

---

## Prompt 2 — MUST Dolor Torácico

```
Eres médico adjunto de Medicina de Urgencias. Audita esta guía de bolsillo —escrita para un residente de primer año (R1) en la primera valoración de un paciente de guardia en un hospital español (Madrid)— frase por frase, contra las guías de práctica clínica VIGENTES.

Para CADA problema, responde así:
• Fragmento: «cita literal del texto»
• Tipo: error | desactualizado | impreciso | omisión | mejora
• Gravedad: alta | media | baja
• Problema: qué está mal o qué falta y por qué importa en urgencias.
• Corrección: el texto corregido o el añadido, CONCRETO y en el mismo registro breve de texto plano (no reescribas toda la guía; dosis en mg o mg/kg, con vía e intervalo).
• Fuente: guía concreta + año (+ clase/nivel de recomendación si aplica).

Reglas:
1) Prioriza guías EUROPEAS (ESC) y ESPAÑOLAS (SEC, SEMES, GEMA, GALAXIA, SEPAR) cuando existan; usa AHA/ACC/GINA/GOLD como complemento y AVISA cuando la recomendación europea/española difiera de la americana (dosis, umbrales o fármacos).
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
3) NO marques como error estas decisiones DELIBERADAS del autor: (a) el umbral de aviso se deja como rango «FC > 100-110 lpm»; (b) no se usa la escala HEART; (c) el síndrome aórtico se deriva al adjunto sin detallar el ADD-RS; (d) estilo conciso de texto plano, de bolsillo.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

DOLOR TORÁCICO EN GUARDIA — GUÍA RÁPIDA PARA EL R1

Lo primero es descartar lo mortal. Esta guía te orienta mientras valoras y, si algo pinta mal, mientras avisas. Idea fija: hasta un 5% de los "dolores no isquémicos" dados de alta eran en realidad un infarto; no cierres el caso como ansiedad u osteomuscular sin descartar antes lo grave.


CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR

Toma constantes y haz un ECG en los primeros 10 minutos. Avisa de inmediato, y no te quedes solo con el paciente, si hay:
- PAS < 90 mmHg o FC > 100-110 lpm (inestabilidad hemodinámica), o signos de mala perfusión (sospecha de shock).
- PAS > 180 mmHg o PAD > 110 mmHg (hipertensión arterial extrema).
- FR > 30 o < 10 rpm, o SpO2 < 90%.
- Bajo nivel de consciencia o focalidad neurológica.
- ECG con elevación del ST (SCACEST): avisa a la Unidad Coronaria de inmediato. Un bloqueo de rama izquierda, u otra alteración del ECG que no estuviera en electros previos, también es bandera roja: compara SIEMPRE con los ECG antiguos para confirmar que el cambio es nuevo y, si lo es, avisa. Ante un BRI con clínica isquémica, los criterios de Sgarbossa aumentan la especificidad de oclusión coronaria aguda.
- Sospecha de cualquiera de las 6 causas mortales: SCA, TEP, síndrome aórtico (disección), taponamiento cardíaco, neumotórax a tensión o rotura esofágica.


QUÉ PREGUNTAR

La meta es encasillar el dolor en un perfil.
- Inicio y duración: brusco y máximo desde el primer segundo orienta a aórtico o a TEP/neumotórax; progresivo, a isquémico. Menos de 5 minutos y cede con reposo o nitroglicerina: angina estable. Más de 20 minutos en reposo y que no cede: sospecha de SCA.
- Cualidad e irradiación: opresivo, "como un peso", irradiado a mandíbula, cuello o brazo: isquémico. Desgarrador y migratorio a la espalda: aórtico. Punzante que aumenta al respirar o toser: pleurítico. Urente retroesternal: esofágico.
- Modificadores: mejora al inclinarse hacia delante (pericárdico); se reproduce a la palpación (osteomuscular, pero solo tras descartar lo grave); cede con nitroglicerina (isquémico; ojo: el espasmo esofágico también cede a nitratos).
- Síntomas acompañantes: cortejo vegetativo (sudor frío, náuseas) y sensación de muerte inminente (SCA o aórtico); disnea súbita (TEP, neumotórax); síncope (TEP, estenosis aórtica, síndrome aórtico); fiebre con tos (neumonía o pericarditis).
- Antecedentes y medicación: factores de riesgo cardiovascular. Ojo al perfil atípico (mujer, anciano, diabético: equivalentes anginosos sin dolor típico). Riesgo de TEP (cáncer, inmovilización o cirugía reciente, trombosis previa, anticonceptivos). Riesgo aórtico (HTA mal controlada, Marfan u otra conectivopatía, aneurisma conocido). Revisa la receta electrónica.


QUÉ EXPLORAR (menos de 2 minutos)

Recuerda: una exploración normal **NO descarta** enfermedad.
- Constantes: TA, FC, FR, SpO2, Tª y glucemia capilar.
- Auscultación cardíaca: soplo de insuficiencia aórtica nuevo (disección), roce pericárdico (pericarditis; se oye mejor con el tronco inclinado hacia delante), tonos apagados (taponamiento).
- Auscultación pulmonar: hipofonesis unilateral con timpanismo (neumotórax), crepitantes o condensación (neumonía).
- Ingurgitación yugular + hipotensión + tonos apagados (tríada de Beck): taponamiento cardíaco.
- Palpa la pared torácica (si reproduce exactamente el dolor, orienta a osteomuscular), mira las piernas (signos de TVP apoyan el TEP) y la piel (vesículas de herpes zóster; enfisema subcutáneo o crepitación con el latido en la rotura esofágica).
- **Si sospechas síndrome aórtico agudo (SAoA):** toma la TA en ambos brazos y compara los pulsos; la asimetría de pulsos o una diferencia de TA entre miembros apoya la disección.


QUÉ PRUEBAS PEDIR

- ECG de 12 derivaciones en menos de 10 minutos (ya en el filtro). Amplía a derivaciones derechas (V3R-V4R) y posteriores (V7-V9) si sospechas infarto inferior o posterior. Un ECG normal NO excluye el SCA.
- Troponina: con troponina ultrasensible, algoritmo seriado 0/1 h (alternativa 0/2 h) valorando el valor basal y su variación (delta); con troponina convencional, segundo control a las 3-6 h. Un único valor normal muy precoz no descarta.
- Radiografía de tórax: mediastino ensanchado (aórtico), neumotórax, condensación, derrame, cardiomegalia "en tetera" (derrame pericárdico).
- TEP: estima la probabilidad con Wells o Geneva. Si es baja o intermedia, dímero-D con el corte ajustado a edad (edad x 10 ng/ml en mayores de 50 años): por debajo de él descarta TEP sin angio-TC. Si la probabilidad es alta, angio-TC directa.
- Síndrome aórtico: si lo sospechas, avisa al adjunto — la prueba es la angio-TC de aorta. La estratificación (ADD-RS) y la decisión de angio-TC vs. dímero-D la marca él/ella.
- Analítica básica y, si está disponible, ecografía a pie de cama (POCUS): taponamiento, TEP con sobrecarga derecha, derrame.


TRATAMIENTO INICIAL (mientras valoras o avisas)

Medidas generales: monitoriza, coge vía y extrae analítica, oxígeno solo si SpO2 < 90%, y trata el dolor.

Según la sospecha:
- SCA: AAS 300 mg (rango 162-325 mg) por vía oral, masticada y sin cubierta entérica (salvo alergia o sangrado activo). Si el dolor es isquémico y la PAS es 90 mmHg o más, nitroglicerina sublingual 0,4 mg, repetible cada 5 minutos hasta 3 dosis (NO si PAS < 90 mmHg, sospecha de infarto de ventrículo derecho, o toma de sildenafilo/tadalafilo en las últimas 24-48 h). Si el dolor no cede, morfina 2-4 mg IV, repetible cada 5-15 minutos (máximo en torno a 10 mg). La doble antiagregación y la anticoagulación se pautan con cardiología según la estrategia. Avisa a la Unidad Coronaria.
- Síndrome aórtico (disección): NO des antiagregantes ni anticoagulantes. Analgesia y control de frecuencia y tensión: el betabloqueante intravenoso va SIEMPRE primero (labetalol o esmolol IV; objetivo FC < 60 lpm y PAS 100-120 mmHg); no des un vasodilatador en solitario, porque la taquicardia refleja puede propagar la disección. Pauta con el adjunto y avisa a cirugía cardiovascular / UCI ya.
- Pericarditis: ibuprofeno 600 mg cada 8 h por vía oral + colchicina 0,5 mg cada 12 h (más de 70 kg) o 0,5 mg cada 24 h (menos de 70 kg), con reposo relativo.
- TEP de alta sospecha: oxígeno y analgesia; valora anticoagulación con enoxaparina 1 mg/kg cada 12 h por vía subcutánea (1 mg/kg cada 24 h si FG < 30 ml/min), con el adjunto, si no hay contraindicación y mientras confirmas con imagen.
- Taponamiento o neumotórax a tensión: son emergencias de procedimiento (pericardiocentesis / drenaje torácico). Avisa de inmediato; no se resuelven con un fármaco.

Y recuerda: no etiquetes el dolor de osteomuscular, esofágico o ansiedad hasta haber descartado lo grave.


FUENTES (para el residente; puedes borrar este bloque antes de compartir)
- Manual 12 de Octubre 2022, cap. 13 y 17; notas y fichas de fármacos del vault.
- Guías: ESC 2023 / ACC-AHA 2025 SCA (troponina, AAS, nitratos, morfina, oxígeno); ESC 2019 / AHA 2026 TEP (dímero-D ajustado a edad); ESC 2024 aorta (ADD-RS); ESC 2025 pericarditis (ibuprofeno + colchicina).
```

---

**Notas de uso**
- Pégalos de uno en uno (OpenEvidence trabaja mejor con una guía por consulta).
- OpenEvidence tira de literatura/guías anglosajonas por defecto; por eso el prompt le pide priorizar ESC/españolas y avisar de divergencias EU/EE. UU. (p. ej. dosis de AAS o ventanas de los inhibidores de la PDE5).
- Si quieres contrastar su salida con mi revisión previa, compáralas: lo que coincida en ambas es lo de mayor confianza.
