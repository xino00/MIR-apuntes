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

## Prompt 3 — MUST Síncope

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
1) Prioriza guías EUROPEAS y ESPAÑOLAS (ESC 2018 sobre síncope, SEMES) y el Manual 12 de Octubre (cap. 13); usa AHA/ACC 2017 como complemento y AVISA cuando difieran (umbrales de alto riesgo, destino del paciente).
3) NO marques como error estas decisiones DELIBERADAS del autor: (a) el síncope se enfoca como TRIAJE DE RIESGO en puerta y se difieren a propósito las pruebas no urgentes (masaje del seno carotídeo, mesa basculante, Holter); (b) midodrina y fludrocortisona se EXCLUYEN deliberadamente como tratamiento de guardia por ser tratamiento crónico del síncope reflejo/hipotensión ortostática; (c) el R1 sospecha y deriva, no estratifica el alto riesgo de forma definitiva; (d) estilo conciso de texto plano, de bolsillo.
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

SÍNCOPE EN GUARDIA — GUÍA RÁPIDA PARA EL R1

En guardia el síncope no es un cuadro que "se trate con un fármaco": es un triaje de riesgo. Tu trabajo es separar al que se va de alta tranquilo del que esconde una causa cardíaca que puede matarlo en los próximos días. La herramienta clave no es un fármaco, son el ECG y la historia clínica.


CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR

Toma constantes y haz un ECG de 12 derivaciones cuanto antes. Avisa de inmediato, y no des de alta por tu cuenta, si hay:
- Síncope durante el esfuerzo, o estando en decúbito o sentado (orienta a causa cardíaca, no a vasovagal).
- Palpitaciones de aparición rápida justo antes de perder el conocimiento.
- Síncope brusco, sin pródromos, que ha provocado un traumatismo importante.
- Cardiopatía estructural conocida, FEVI baja, insuficiencia cardíaca o infarto previo.
- Dolor torácico, disnea, cefalea o dolor abdominal acompañando al episodio.
- PAS < 90 mmHg sin causa clara, o sospecha de sangrado digestivo (haz tacto rectal).
- Soplo sistólico no estudiado (sospecha de estenosis aórtica o miocardiopatía hipertrófica).
- ECG patológico: cambios de isquemia aguda, BAV de 2.º grado Mobitz II o de 3.er grado, bradicardia o FA lenta < 40 lpm, pausas sinusales > 3 s, taquicardia ventricular, patrón de Brugada tipo 1, QTc > 460 ms, preexcitación (QRS preexcitado) o disfunción de marcapasos/DAI. Compara SIEMPRE con electros previos: si la alteración es NUEVA respecto a un ECG antiguo, avisa.

Idea fija: ante sospecha de causa potencialmente mortal NO te pongas a puntuar escalas para decidir tú el destino; sospecha y avisa. La estratificación fina y la decisión de ingreso las cierra el adjunto.


QUÉ PREGUNTAR

La meta es encasillar el episodio en reflejo, ortostático o cardíaco.
- Posición y desencadenante: bipedestación prolongada, calor, lugar abarrotado, dolor, visión de sangre, o durante la micción, la tos o la deglución, orienta a reflejo; al incorporarse desde tumbado o sentado, a ortostático; durante el esfuerzo o estando tumbado, a cardíaco (bandera roja).
- Pródromos: sudoración, náuseas, calor o visión borrosa antes de caer apoyan el reflejo; ausencia de pródromos o palpitaciones previas orientan a cardíaco.
- Recuperación: rápida y completa (típica del síncope) frente a confusión que dura más de 5 minutos (orienta a crisis epiléptica).
- Datos que sugieren crisis y no síncope: mordedura lateral de la lengua, movimientos tónico-clónicos prolongados, desviación de la cabeza o los ojos.
- Medicación: antihipertensivos, diuréticos, fármacos que alargan el QT, antidepresivos, neurolépticos, frenadores del nodo AV. Revisa la receta electrónica.
- Antecedente familiar de muerte súbita precoz.


QUÉ EXPLORAR (menos de 2 minutos)

- Constantes completas y glucemia capilar.
- TA en decúbito supino y de nuevo a los 3 minutos de bipedestación. Hipotensión ortostática: caída de la PAS ≥ 20 mmHg, de la PAD ≥ 10 mmHg, o PAS < 90 mmHg, que reproduzca los síntomas.
- Auscultación cardíaca: soplo sistólico de estenosis aórtica o de miocardiopatía hipertrófica.
- Exploración neurológica básica buscando focalidad (orienta fuera del síncope: ictus, HSA).
- Tacto rectal si sospechas sangrado digestivo como causa de hipotensión.

Recuerda: una exploración normal NO descarta una causa cardíaca grave.


QUÉ PRUEBAS PEDIR

- ECG de 12 derivaciones SIEMPRE, en todo síncope (es obligatorio y es lo que más rinde).
- Glucemia capilar.
- Hemograma (anemia o anemización por sangrado) e iones.
- Test de embarazo en mujer en edad fértil.
- Troponina, dímero-D o radiografía de tórax SOLO si la clínica lo orienta (dolor torácico, disnea, sospecha de SCA o de TEP). Pedidos de rutina rinden poco y no ayudan a estratificar.
- No pidas en la primera valoración de puerta: masaje del seno carotídeo, mesa basculante (tilt-test) ni Holter. Son del estudio diferido, no de la guardia.


TRATAMIENTO INICIAL (mientras valoras o avisas)

La mayoría de los síncopes NO necesitan ningún fármaco. El tratamiento de la guardia es postural y de soporte; el resto es triaje de destino.

Medidas generales: tumba al paciente en decúbito con las piernas elevadas, monitoriza, coge vía y extrae la analítica, y repite la TA.
- Si es ortostático, está deshidratado o hipotenso: sueroterapia con cristaloides (suero salino fisiológico 0,9% IV).
- Bradicardia sintomática con compromiso hemodinámico: atropina 0,5-1 mg IV en bolo rápido, repetible cada 3-5 minutos hasta un máximo de 3 mg. No uses dosis menores de 0,5 mg (pueden empeorar la bradicardia de forma paradójica).
- NO des betabloqueantes ni vasodilatadores.
- NO uses midodrina ni fludrocortisona en la guardia: son tratamiento CRÓNICO del síncope reflejo y de la hipotensión ortostática, se pautan en consulta, no en urgencias.

Destino (lo afina el adjunto):
- Bajo riesgo (pródromos típicos de reflejo + ECG normal + sin cardiopatía): alta, con derivación a consulta si los episodios son recurrentes.
- Zona intermedia (ni claramente bajo ni alto riesgo): observación en el SU 6-24 h con telemetría.
- Cualquier dato de alto riesgo: ingreso.

Y recuerda: no etiquetes de "vasovagal" un síncope de esfuerzo, en decúbito o precedido de palpitaciones. Eso es cardíaco hasta que se demuestre lo contrario.


FUENTES (para el residente; puedes borrar este bloque antes de compartir)
- Guía ESC 2018 sobre diagnóstico y tratamiento del síncope (Rev Esp Cardiol 2018;71(10):837.e1-e92): red flags Tabla 6, criterios de hipotensión ortostática, triaje de urgencias y algoritmo de destino Tabla 7.
- Manual 12 de Octubre 2022, cap. 13 (Dolor torácico. Síncope).
- Notas del vault: Síncope (cardio), Síncope Neurológico (diferencial con crisis/ictus/HSA), Arritmias, Valvulopatías (estenosis aórtica de esfuerzo).
- Ficha de fármaco del vault: Atropina (dosis en bradicardia sintomática 0,5-1 mg IV, repetible cada 3-5 min, máx 3 mg).
```

---

## Prompt 4 — MUST Fiebre sin Foco

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
1) Prioriza guías EUROPEAS y ESPAÑOLAS (Surviving Sepsis Campaign 2021/2026, SEIMC, SEMES; meningitis: ESCMID/guía española) y el Manual 12 de Octubre; usa IDSA como complemento y AVISA cuando difieran (dosis o cobertura empírica).
3) NO marques como error estas decisiones DELIBERADAS del autor: (a) el alcance es el ADULTO febril agudo en puerta (descartar sepsis/meningitis y buscar foco), NO el estudio de la fiebre de origen desconocido prolongada ni la fiebre del lactante/niño; (b) los antibióticos empíricos se citan como ejemplo orientativo y deben ajustarse al protocolo local de PROA; (c) estilo conciso de texto plano, de bolsillo.
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

FIEBRE SIN FOCO EN GUARDIA — GUÍA RÁPIDA PARA EL R1

El febril agudo del adulto en la puerta. Tu objetivo no es etiquetar la causa, sino detectar a tiempo la sepsis y la meningitis, buscar el foco y decidir cuándo el antibiótico empírico no puede esperar. No es el estudio de la fiebre de origen desconocido prolongada ni el del niño.


CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR

Toma constantes completas con SatO2, glucemia capilar y nivel de consciencia nada más entrar. Avisa de inmediato, y no te quedes solo con el paciente, si hay:
- Criterios de sepsis o shock: qSOFA con 2 o más (FR mayor o igual a 22, PAS menor o igual a 100, alteración mental), o hipotensión, mala perfusión o lactato elevado. Aquí no puntúas y decides tú: sospecha de sepsis igual a aviso.
- Signos meníngeos (rigidez de nuca, Kernig, Brudzinski) o cualquier alteración del nivel de consciencia.
- Petequias o púrpura: sospecha de meningococo. El antibiótico va INMEDIATO, no esperes a la punción lumbar; avisa mientras lo preparas.
- Inmunodeprimido (VIH, quimioterapia, corticoides, esplenectomía, trasplante) o neutropénico febril: este paciente se descompensa rápido.
- Temperatura mayor de 40 grados, o hipotermia menor de 36 (mal pronóstico, frecuente en ancianos y alcohólicos).
- Embarazada con fiebre.
- Portador de prótesis, catéter venoso central o sonda con fiebre, y el ADVP.


QUÉ PREGUNTAR

La meta es encontrar el foco y pesar la gravedad.
- Tiempo y patrón: ¿desde cuándo? ¿brusca (neumonía lobar) o gradual? ¿es la primera vez? ¿escalofríos con tiritona franca (orienta a bacteriemia)?
- Síntomas localizadores, repasándolos uno a uno: disuria o polaquiuria (urinario); tos, expectoración o disnea (respiratorio); dolor abdominal o diarrea (digestivo); cefalea con rigidez o fotofobia (meníngeo); exantema; dolor articular; dolor lumbar o en fosa renal.
- Epidemiología: viajes recientes, contacto con enfermos, animales y mascotas, ambiente laboral.
- Estado inmune: VIH, quimioterapia, corticoides, esplenectomía, trasplante.
- Fármacos y dispositivos: prótesis, sondas, catéteres, ADVP; y el último ciclo de antibiótico (ojo a la fiebre que persiste pese a antibiótico de amplio espectro).


QUÉ EXPLORAR (menos de 2 minutos)

Recuerda: una exploración normal NO descarta enfermedad grave.
- Constantes completas con SatO2, glucemia y nivel de consciencia.
- Piel y mucosas: petequias o púrpura (busca activamente), celulitis, herida o úlcera por presión, puntos de venopunción.
- ORL: orofaringe, oídos, senos.
- Auscultación cardiopulmonar: crepitantes o condensación (foco respiratorio), soplos nuevos (endocarditis si hay foco vascular).
- Abdomen: dolor, Murphy y puñopercusión renal bilateral.
- Signos meníngeos: rigidez de nuca, Kernig y Brudzinski.
- Articulaciones (artritis séptica) y, según el caso, valora tacto rectal y exploración genital.
- Revisa los puntos de inserción de cualquier catéter o sonda.


QUÉ PRUEBAS PEDIR

- Analítica: hemograma, PCR y procalcitonina, función renal y hepática, iones y coagulación. La procalcitonina por encima de 2 orienta a origen bacteriano, pero no esperes a ella para tratar.
- Lactato: marcador de hipoperfusión y de pronóstico; por encima de 2 mmol/l es mal dato y por encima de 4 obliga a fluidos. Vuelve a medirlo si estaba elevado.
- Hemocultivos x2 ANTES del antibiótico, pero sin retrasarlo si hay shock.
- Sistemático de orina y urocultivo.
- Radiografía de tórax.
- Gasometría con lactato.
- Según el foco: punción lumbar si sospechas meningitis. Pide TC craneal previo SOLO si hay focalidad neurológica, inmunodepresión, crisis o bajo nivel de consciencia; en los demás, punción directa. El TC y la propia punción NUNCA deben retrasar ni el antibiótico ni la dexametasona.


TRATAMIENTO INICIAL (mientras valoras o avisas)

Medidas generales: monitoriza, coge vía y extrae analítica con hemocultivos, glucemia capilar, y oxígeno con objetivo de SatO2 94-98%.

Paquete de sepsis de la primera hora (si hay sepsis o shock): lactato, hemocultivos x2, antibiótico empírico precoz (en menos de 1 hora) y, si hay hipoperfusión o lactato mayor o igual a 4 mmol/l, cristaloides 30 ml/kg IV (en obesidad calcula sobre peso ajustado o ideal). Si persiste la hipotensión tras los fluidos, noradrenalina (con el adjunto).

Antitérmico: paracetamol 1 g IV en 15 minutos o VO cada 6-8 h (máximo 4 g/día; 2-3 g/día en ancianos o hepatópatas). Alternativa: metamizol 2 g IV diluido en 100 ml de suero en perfusión lenta de 10-15 minutos (nunca en bolo, da hipotensión).

Según la sospecha:
- Meningitis: dexametasona 0,15 mg/kg IV (en torno a 10 mg) JUSTO ANTES o junto a la primera dosis de antibiótico, nunca después, mas ceftriaxona 2 g IV cada 12 h (dosis meníngea: 2 g/12 h, NO 1 g/24 h). Añade ampicilina 2 g IV cada 4 h si tiene más de 50 años o está inmunodeprimido (cobertura de Listeria), y vancomicina 15-20 mg/kg IV cada 8-12 h si sospechas neumococo resistente. Verifica con el adjunto.
- Sepsis sin foco claro: ceftriaxona 2 g IV de inicio, ajustando la cobertura según la sospecha y el protocolo local. Si hay foco intraabdominal, añade metronidazol 500 mg IV cada 8 h (cobertura de anaerobios).
- Neutropénico febril: betalactámico antipseudomónico (piperacilina-tazobactam o cefepime); pauta la dosis con el adjunto.

Y recuerda: ante petequias o sospecha de meningitis, el antibiótico precoz manda; ninguna prueba de imagen justifica retrasarlo.


FUENTES (para el residente; puedes borrar este bloque antes de compartir)
- Manual 12 de Octubre 2022, cap. 6 (síndrome febril) y cap. 65 (sepsis); notas Sepsis - Abordaje Inicial (SSC 2026), Sepsis - Antiinfecciosos y Soporte Vital, y Meningitis y Encefalitis del vault; fichas de Paracetamol, Metamizol, Ceftriaxona y Metronidazol.
- Guías: Surviving Sepsis Campaign (SSC) 2021/2026 (bundle de la primera hora, lactato, hemocultivos, fluidos 30 ml/kg, noradrenalina); guía de meningitis bacteriana aguda (dexametasona antes/con el antibiótico, ceftriaxona 2 g/12 h, ampicilina por Listeria en mayores de 50 o inmunodeprimidos).
```

---

## Prompt 5 — MUST Dolor Abdominal

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
1) Prioriza guías EUROPEAS y ESPAÑOLAS (AEC cirugía, AEG, WSES para abdomen agudo) y el Manual 12 de Octubre (Tabla 8 de tratamiento sintomático); avisa de divergencias EU/EE. UU. en dosis.
3) NO marques como error estas decisiones DELIBERADAS del autor: (a) se recomienda DELIBERADAMENTE la analgesia precoz (el mito de «no analgesia hasta el diagnóstico» está desmentido); (b) no se detallan los algoritmos quirúrgicos ni de imagen avanzada (decisión del adjunto/cirugía); (c) estilo conciso de texto plano, de bolsillo.
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

DOLOR ABDOMINAL EN GUARDIA — GUÍA RÁPIDA PARA EL R1

Lo primero es separar el abdomen quirúrgico o catastrófico del banal. Esta guía te orienta mientras valoras y, si algo pinta mal, mientras avisas. Idea fija: la valoración seriada del paciente es tu mejor herramienta diagnóstica, y un dolor epigástrico puede ser un infarto inferior; no cierres ningún caso sin haber descartado antes lo grave.


CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR

Toma constantes con temperatura y haz una glucemia capilar. Avisa de inmediato, y no te quedes solo con el paciente, si hay:
- PAS < 90 mmHg, taquicardia o signos de mala perfusión (sospecha de shock): el dolor abdominal con inestabilidad es una emergencia hasta que se demuestre lo contrario.
- Abdomen en tabla, defensa generalizada o Blumberg (peritonismo): sospecha de perforación o peritonitis.
- Dolor brusco y desgarrador con masa abdominal pulsátil, o asimetría de pulsos o de TA entre miembros: sospecha de aneurisma de aorta abdominal roto.
- Dolor desproporcionado a una exploración pobre, sobre todo con fibrilación auricular o arteriopatía: sospecha de isquemia mesentérica.
- Hematemesis o melenas con inestabilidad hemodinámica: hemorragia digestiva con repercusión.
- Mujer en edad fértil con dolor abdominal bajo más hipotensión o síncope: sospecha de embarazo ectópico roto.
- Ausencia de tránsito (no ventosea ni defeca) con vómitos fecaloideos y distensión: obstrucción posiblemente complicada.
- Recuerda el IAM de cara inferior, que se presenta como epigastralgia con cortejo vegetativo: ante la duda, haz un ECG.


QUÉ PREGUNTAR

La meta es localizar el dolor y encasillar su perfil temporal.
- Localización e irradiación: epigastrio orienta a pancreatitis, úlcus o IAM; hipocondrio derecho (irradiado a escápula/hombro) a patología biliar; fosa iliaca derecha a apendicitis; fosa iliaca izquierda a diverticulitis; hipogastrio a causa urológica o ginecológica; "en cinturón" a la espalda a pancreatitis; difuso o migratorio a isquemia, obstrucción o peritonitis.
- Tipo e inicio: cólico (víscera hueca) frente a continuo (inflamatorio o peritonítico). Súbito y máximo desde el primer segundo orienta a perforación, vascular o cólico renoureteral; progresivo en horas, a un proceso inflamatorio o infeccioso.
- Relación con la ingesta y vómitos: empeora con grasas (biliar), mejora al vomitar (obstrucción); vómitos biliosos frente a fecaloideos (obstrucción distal).
- Tránsito: cierre intestinal (obstrucción, íleo), diarrea, melenas o rectorragia.
- Síntomas urinarios y fiebre; fecha de la última regla y posibilidad de embarazo en toda mujer fértil.
- Antecedentes y medicación: cirugías previas (bridas), litiasis o alcohol (biliar/pancreatitis), cardiopatía o FA (isquemia mesentérica), y fármacos clave (AINE, anticoagulantes). Revisa la receta electrónica.


QUÉ EXPLORAR (menos de 2 minutos)

Recuerda: una exploración normal NO descarta enfermedad, y el anciano y el diabético dan clínica atípica.
- Constantes con temperatura, aspecto general y postura (quieto en el peritonismo, inquieto en el cólico, reclinado en la pancreatitis).
- Inspección: distensión, cicatrices de cirugías previas, hernias; signos de Cullen o Grey-Turner.
- Auscultación: silencio abdominal (íleo o peritonitis) frente a ruidos metálicos de lucha (obstrucción mecánica).
- Palpación: defensa y Blumberg (peritonismo); Murphy (colecistitis); McBurney, Rovsing y psoas (apendicitis).
- Puñopercusión renal (patología renoureteral) y palpación de hernias.
- Tacto rectal si sospechas melenas, masa o fecaloma; exploración pélvica o genital si procede (dolor a la movilización cervical, torsión testicular).
- Palpa los pulsos femorales y busca una masa abdominal pulsátil si sospechas patología aórtica.


QUÉ PRUEBAS PEDIR

- Analítica: hemograma, bioquímica con amilasa y lipasa, función renal y hepática con bilirrubina, iones, PCR y coagulación.
- Gasometría venosa con lactato: orienta a isquemia intestinal o sepsis; la urea elevada sin fallo renal apoya un sangrado digestivo alto.
- Sistemático de orina (infección, litiasis; puede alterarse en la apendicitis).
- Test de embarazo en TODA mujer en edad fértil: es obligatorio y se olvida con facilidad.
- ECG: descarta el IAM inferior que simula epigastralgia, sobre todo en mayores de 50 años o con factores de riesgo.
- Radiografía de abdomen: niveles hidroaéreos (obstrucción) y neumoperitoneo (perforación, mejor en bipedestación o decúbito lateral izquierdo).
- Ecografía: elección para vía biliar y vesícula; a pie de cama valora aorta, líquido libre y causa ginecológica.
- TC abdominal con contraste: ante sospecha vascular o de perforación, o en el caso dudoso; indícala con el adjunto.


TRATAMIENTO INICIAL (mientras valoras o avisas)

Medidas generales: monitoriza, dieta absoluta, coge vía y extrae analítica con gasometría, inicia sueroterapia con cristaloides, y coloca SNG si hay vómitos u obstrucción.

La analgesia precoz NO enmascara el diagnóstico (es un mito): trata el dolor desde el principio.
- Dolor leve-moderado: paracetamol 1 g IV en perfusión de 15 minutos cada 6-8 h, o metamizol 2 g IV en perfusión lenta de 10-15 minutos (nunca en bolo, hipotensa).
- Dolor moderado-intenso: morfina 2-5 mg IV cada 15 minutos, titulando hasta controlar el dolor (carga habitual en torno a 10 mg); como alternativa, fentanilo 10-25 mcg IV cada 5 minutos.
- Náuseas o vómitos: ondansetrón 4-8 mg IV (primera elección), o metoclopramida 10 mg IV en bolo lento de al menos 3 minutos como alternativa (evítala si hay obstrucción mecánica o hemorragia GI activa).
- Cólico biliar o digestivo inespecífico: butilbromuro de escopolamina 20 mg IV o IM como espasmolítico.
- Cólico renoureteral: AINE IV de primera elección (por ejemplo, dexketoprofeno 50 mg IV o diclofenaco), ya que la escopolamina no ha demostrado eficacia en esta indicación.
- Sospecha de úlcus o de hemorragia digestiva alta: pantoprazol 40 mg IV.
- Sospecha de peritonitis, perforación o colangitis: antibiótico precoz tras los cultivos (por ejemplo, ceftriaxona 2 g/24 h IV con metronidazol, o piperacilina-tazobactam 4 g/6-8 h IV); pauta la cobertura con el adjunto.

Y recuerda: avisa a cirugía precozmente ante todo abdomen quirúrgico; no esperes a tener el diagnóstico cerrado.


FUENTES (para el residente; puedes borrar este bloque antes de compartir)
- Manual 12 de Octubre 2022, cap. 32 Dolor abdominal (Tabla 8 de tratamiento sintomático); caps. 36, 39, 47 y 73; notas y fichas de fármacos del vault.
- Notas del vault: Dolor Abdominal (generalidades, anamnesis, pruebas y manejo), Colecistitis Aguda, Pancreatitis Aguda, Obstrucción Intestinal, Hemorragia Digestiva Alta (HDA).
- Fichas de fármacos: Paracetamol, Metamizol, Morfina, Metoclopramida y Ceftriaxona.
```

---

## Prompt 6 — MUST Cefalea

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
1) Prioriza guías EUROPEAS y ESPAÑOLAS (Sociedad Española de Neurología — SEN, IHS/ICHD-3) y el Manual 12 de Octubre (cap. 63); usa AHS/AAN como complemento y AVISA cuando difieran (triptanes, criterios de neuroimagen).
3) NO marques como error estas decisiones DELIBERADAS del autor: (a) las banderas rojas se memorizan como SNOOP y el R1 sospecha y deriva (HSA, meningitis y arteritis se manejan con el adjunto); (b) no se usan scores; (c) estilo conciso de texto plano, de bolsillo.
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

CEFALEA EN GUARDIA — GUÍA RÁPIDA PARA EL R1

La mayoría de las cefaleas son primarias y benignas, pero tu trabajo en la puerta es el contrario: detectar la cefalea secundaria que mata. Esta guía te orienta mientras valoras y, sobre todo, te dice cuándo dejar de tratar el dolor y avisar.


CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR

Las banderas rojas se memorizan como SNOOP. La regla es sencilla: ante la sospecha de una causa grave, AVISA; no es tu trabajo estratificarla ni descartarla solo. Avisa, y no te quedes solo con el paciente, si hay:
- Cefalea en trueno: máxima intensidad en menos de 1 minuto, o "la peor cefalea de mi vida". Es hemorragia subaracnoidea mientras no se demuestre lo contrario.
- Cefalea con fiebre y rigidez de nuca o alteración del nivel de consciencia: sospecha de meningitis o encefalitis.
- Focalidad neurológica nueva, papiledema en el fondo de ojo o crisis comicial.
- Cefalea de inicio reciente o progresiva en mayor de 50 años: piensa en arteritis de células gigantes (claudicación mandibular, arteria temporal indurada o dolorosa, alteración visual) y en lesión ocupante de espacio.
- Inmunodeprimido o paciente oncológico (absceso, toxoplasmosis, metástasis, linfoma).
- Embarazo o puerperio: trombosis venosa cerebral, preeclampsia/eclampsia.
- Desencadenada por Valsalva (tos, esfuerzo) o que cambia con la postura, o que interrumpe el sueño nocturno.
- Tras un traumatismo craneal, sobre todo en ancianos, anticoagulados o bebedores (hematoma subdural).
- Ojo rojo doloroso con midriasis media arreactiva y visión de halos: glaucoma agudo de ángulo cerrado.


QUÉ PREGUNTAR

La meta es separar la cefalea primaria conocida de la secundaria peligrosa.
- Tiempo hasta el pico de dolor: instantáneo (segundos) orienta a trueno y hemorragia subaracnoidea; en horas-días, a infección o causa progresiva.
- ¿Es el primer episodio o una cefalea recurrente ya conocida? Y si la conoce: ¿es exactamente igual a las de siempre o ha cambiado de patrón, frecuencia o intensidad?
- Localización y carácter: pulsátil hemicraneal con foto/fonofobia y náusea orienta a migraña; opresivo bilateral "en banda", a tensional; unilateral periocular con lagrimeo, rinorrea o ptosis, a cefalea en racimos.
- Síntomas acompañantes: aura visual; fiebre; vómitos sin otra causa; despertar nocturno por el dolor.
- Relación con la postura (empeora de pie o tumbado) y con el esfuerzo o el Valsalva.
- Consumo y sobreuso de analgésicos o triptanes (cefalea por abuso de medicación), y fármacos nuevos (nitratos, anticonceptivos).
- Exposición a monóxido de carbono: braseros, calentadores, varios convivientes con cefalea a la vez.


QUÉ EXPLORAR (menos de 2 minutos)

Recuerda: una exploración normal NO descarta una causa secundaria.
- Constantes con temperatura y glucemia capilar; tensión arterial (cifras > 160/120 pueden justificar la cefalea).
- Nivel de consciencia y focalidad motora, sensitiva o cerebelosa; pares craneales.
- Signos meníngeos (rigidez de nuca).
- Fondo de ojo buscando papiledema; agudeza visual y pupilas (midriasis fija del glaucoma, Horner doloroso de la disección).
- Palpa las arterias temporales (induración o dolor en la arteritis de células gigantes) y los senos frontales y maxilares.


QUÉ PRUEBAS PEDIR

- La mayoría de las cefaleas primarias NO requieren ninguna prueba: el diagnóstico es clínico.
- TC craneal urgente sin contraste si hay cualquier bandera roja: trueno, focalidad, crisis, papiledema, mayor de 50 de novo, inmunodepresión o traumatismo. Hazla en general antes de la punción lumbar.
- Punción lumbar: obligatoria si sospechas meningitis. Y si el TC es normal pero persiste la sospecha de hemorragia subaracnoidea, la PL buscando xantocromía sigue siendo necesaria: un TC normal NO descarta la HSA.
- VSG y PCR si sospechas arteritis de células gigantes; pídelas, pero NO esperes al resultado para empezar el corticoide.
- Si sospechas meningitis bacteriana, no demores la antibioterapia por esperar a la PL.
- RM, angio-TC o venografía cuando se sospecha causa vascular o trombosis venosa: lo decide el adjunto.


TRATAMIENTO INICIAL (mientras valoras o avisas)

Si hay bandera roja, lo primero es avisar; la analgesia no debe enmascarar ni retrasar el diagnóstico. Para la cefalea primaria, ambiente tranquilo y oscuro, y según la sospecha:
- Cefalea tensional o inespecífica leve: paracetamol 1 g en perfusión IV de 15 min cada 4-6 h, o 1 g VO cada 6-8 h (máximo 4 g/día; 2-3 g/día en ancianos o hepatópatas), o un AINE como dexketoprofeno 25 mg VO cada 8 h (máximo 75 mg/día) o 50 mg IV/IM cada 8-12 h (máximo 150 mg/día por vía IV).
- Crisis de migraña: AINE o paracetamol a las dosis anteriores, junto con metoclopramida 10 mg IV en bolo lento de al menos 3 min (controla el dolor y la náusea); rehidrata con suero si hay vómitos. Si no responde, sumatriptán 6 mg SC (o 50 mg VO); máximo 12 mg/24 h. ANTES de dar el triptán comprueba que no haya cardiopatía isquémica, enfermedad cerebrovascular o vascular periférica, HTA no controlada ni embarazo, y que no haya tomado un ergótico u otro triptán en las últimas 24 h: en esos casos el triptán está contraindicado y tratas solo con AINE y antiemético.
- Cefalea en racimos: oxígeno al 100% a 12-15 l/min con mascarilla con reservorio durante 15-20 min, junto con sumatriptán 6 mg SC (con las mismas contraindicaciones).
- Sospecha de arteritis de células gigantes: inicia el corticoide precoz sin esperar a la biopsia ni a la VSG; prednisona aproximadamente 1 mg/kg/día VO, y si hay pérdida visual, megadosis de metilprednisolona IV (pautada con el adjunto). Retrasar el corticoide puede costar la visión.
- Evita los opioides en la cefalea: no son de primera línea, empeoran la náusea y favorecen la cefalea por abuso de medicación.
- Hemorragia subaracnoidea, meningitis o cualquier causa grave: medidas de soporte y AVISA; el tratamiento específico se decide con el adjunto.


FUENTES (para el residente; puedes borrar este bloque antes de compartir)
- Manual 12 de Octubre 2022, cap. 63 Cefaleas y algias craneofaciales (signos de alarma, indicaciones de TC/PL, migraña: AINE + antieméticos, evitar opioides) y cap. 61.
- Notas del vault: Cefaleas - Abordaje Inicial (SNOOP10); CEFALEA con signos de alarma; Cefaleas Trigemino-Autonómicas y Tensional (oxígeno 12-15 l/min y sumatriptán 6 mg SC en racimos).
- Fichas de fármacos del vault: Paracetamol, Dexketoprofeno, Metamizol, Sumatriptán (contraindicaciones cardiovasculares y dosis), Metoclopramida, Morfina.
- Guías SEN de cefaleas; criterios de neuroimagen urgente y de descarte de HSA (TC + PL con xantocromía); corticoide precoz en arteritis de células gigantes.
```

---

## Prompt 7 — MUST Mareo y Vértigo

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
1) Prioriza guías EUROPEAS y ESPAÑOLAS (criterios de la Bárány Society, GRACE-3, AAO-HNS para VPPB, SEORL) y el Manual 12 de Octubre (cap. 9); avisa de divergencias relevantes.
3) NO marques como error estas decisiones DELIBERADAS del autor: (a) el enfoque es por CRONOLOGÍA y DESENCADENANTES (TiTrATE/ATTEST), no por la descripción del síntoma; (b) la batería HINTS se aplica solo al síndrome vestibular agudo continuo, no al vértigo posicional; (c) el R1 sospecha centralidad y deriva; (d) estilo conciso de texto plano, de bolsillo.
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

MAREO Y VÉRTIGO EN GUARDIA — GUÍA RÁPIDA PARA EL R1

Lo primero es descartar lo central: un ictus de fosa posterior se disfraza de vértigo banal. La clave no es cómo lo describe el paciente ("se mueve todo") sino CUÁNDO le pasa y QUÉ lo desencadena. Esta guía te orienta mientras valoras y, si algo pinta a central, mientras avisas.


CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR

Toma constantes, glucemia y mira la marcha. Avisa de inmediato, y no cierres el caso como periférico, si hay:
- Cualquier focalidad neurológica: diplopía, disartria, disfagia, hemiparesia, dismetría, alteración sensitiva cruzada, síndrome de Horner.
- Vértigo agudo continuo (de días) con datos de centralidad en la batería HINTS: head-impulse NORMAL (paradójicamente, el reflejo conservado es lo sospechoso), nistagmo que cambia de dirección con la mirada o es vertical/torsional puro, o test of skew positivo. Si dudas, no lo etiquetes de neuritis.
- Ataxia troncal grave: incapacidad para mantenerse sentado o caminar desproporcionada al vértigo.
- Cefalea o cervicalgia occipital súbita o intensa (sospecha de disección de arteria vertebral o hemorragia).
- Hipoacusia súbita unilateral acompañando al vértigo agudo (puede ser un infarto de AICA, no un problema de oído banal).
- Factores de riesgo vascular con vértigo agudo persistente, o primer episodio en mayor de 60 años con FRCV (sospecha de ictus vertebrobasilar).
- Alteración del nivel de consciencia o inestabilidad hemodinámica.

Regla: ante sospecha de causa central, AVISA; la estratificación del ictus la decide el adjunto, no tú.


QUÉ PREGUNTAR

Manda la cronología y el desencadenante, no la descripción del síntoma.
- Tiempo (patrón temporal): ¿episódico recurrente (asintomático entre crisis) o agudo y continuo desde hace días? El cuadro continuo de días es el que obliga a descartar ictus.
- Duración del episodio: segundos con cada movimiento de la cabeza orienta a VPPB; minutos-horas a Ménière, migraña vestibular o AIT vertebrobasilar; días continuo a neuritis vestibular o ictus.
- Desencadenante: girar la cabeza o tumbarse y reproducible (VPPB); al ponerse de pie (hipotensión ortostática); espontáneo, sin disparador (neuritis o ictus).
- Síntomas asociados: hipoacusia, acúfenos o plenitud ótica fluctuante (Ménière); cefalea con foto/fonofobia o historia migrañosa (migraña vestibular); cualquier síntoma neurológico (central).
- Antecedentes y medicación: factores de riesgo cardiovascular, ictus o AIT previos, migraña; fármacos ototóxicos (aminoglucósidos, sobre todo gentamicina) o sedantes. Revisa la receta electrónica.


QUÉ EXPLORAR (menos de 2 minutos)

Recuerda: una exploración normal NO descarta enfermedad.
- Constantes, glucemia capilar y constantes ortostáticas (tumbado y al minuto y a los 3 min de bipedestación): caída de la sistólica de 20 mmHg o más, o de la diastólica de 10 mmHg o más, apoya hipotensión ortostática.
- Exploración neurológica dirigida: pares craneales, pruebas cerebelosas (dismetría, disdiadococinesia), marcha y Romberg. La incapacidad para caminar es bandera roja.
- Nistagmo: describe la dirección y si cambia con la mirada. Unidireccional, horizontal y que se suprime con la fijación orienta a periférico; vertical, torsional puro o que cambia de dirección orienta a central.
- En el vértigo agudo CONTINUO con nistagmo espontáneo: batería HINTS (head-impulse, nistagmo, test of skew). Interpreta al revés de lo intuitivo: head-impulse normal = sospechoso de central.
- Si el vértigo es POSICIONAL (segundos al mover la cabeza): Dix-Hallpike (cabeza rotada 45° y bajada en supino con la cabeza colgando 30 s); nistagmo torsional-vertical, con latencia, breve y fatigable confirma VPPB de canal posterior.
- Otoscopia y valoración de la audición.


QUÉ PRUEBAS PEDIR

- Glucemia capilar (descarta hipoglucemia como causa de mareo).
- ECG de 12 derivaciones si hay presíncope o sospecha de causa cardiogénica (arritmia).
- Analítica básica solo si la orientas (sospecha ortostática, sistémica o vómitos con riesgo de deshidratación); en el vértigo periférico típico su rentabilidad es muy baja.
- Neuroimagen: la mayoría de los vértigos periféricos NO necesitan imagen. Si sospechas causa central (HINTS central, focalidad, FRCV con vértigo persistente), la prueba es la RM con difusión, no el TC: el TC craneal es poco sensible para la fosa posterior y un TC normal NO descarta un ictus cerebeloso. Indica la RM con el adjunto.


TRATAMIENTO INICIAL (mientras valoras o avisas)

Medidas generales: tranquiliza al paciente, monitoriza si está vegetativo, y coge vía con sueroterapia si hay vómitos importantes.

Según la sospecha:
- VPPB: maniobra de reposición. Para el canal posterior, maniobra de Epley (es la primera medida y el tratamiento de elección). NO uses sedantes vestibulares: son inútiles en el VPPB y, al frenar la compensación, lo empeoran.
- Vértigo periférico agudo intenso (neuritis vestibular) con cortejo vegetativo: sedante vestibular SOLO en fase aguda y la mínima duración posible (3 días o menos, nunca lo cronifiques). Sulpirida 50-100 mg cada 8 h IV o VO. Si predominan náuseas y vómitos, metoclopramida 10 mg cada 6 h IV o VO (bolo IV lento en 3 minutos como mínimo). Valora corticoide precoz: prednisona 1 mg/kg/día VO 5 días, con descenso posterior. Rehabilitación vestibular precoz: es lo que de verdad acelera la recuperación.
- Crisis de Ménière conocido: antiemético o sedante vestibular corto (sulpirida o metoclopramida a las dosis de arriba); ajuste de fondo (betahistina, restricción de sal) en consulta.
- Crisis muy intensa e incapacitante refractaria: de forma puntual, diazepam 5 mg (rango 1-5 mg cada 12 h) VO o IV; vigila sedación y caídas, sobre todo en ancianos.
- Vértigo central (sospecha de ictus): no es un problema de fármaco. Soporte, vía ictus si procede y AVISA a neurología; no des sedantes vestibulares que enmascaren la exploración.

Y recuerda: no etiquetes el cuadro de neuritis ni de vértigo periférico hasta haber descartado lo central; el head-impulse normal en un vértigo agudo continuo es para avisar.


FUENTES (para el residente; puedes borrar este bloque antes de compartir)
- Manual 12 de Octubre 2022, cap. 9 (Patología ORL): protocolo HINTS, Dix-Hallpike, RM frente a TC en fosa posterior, dosis de sulpirida 50-100 mg/8 h, metoclopramida 10 mg/6 h, diazepam 1-5 mg/12 h y prednisona 1 mg/kg/día en neuritis; tablas 5-6.
- Notas del vault: Mareo y Vértigo - Síntesis de Guías y Evidencia; Vértigo en Urgencias; Mareo y Vértigo - Abordaje Diagnóstico. Fichas de fármacos: Metoclopramida, Diazepam.
- Guías: GRACE-3 (Acad Emerg Med 2023) y TiTrATE/ATTEST para el enfoque temporal y de desencadenantes; AAO-HNS 2017 (recomendación en contra de fármacos en el VPPB, maniobras de reposición); clasificación de Bárány (criterios de Ménière y migraña vestibular); Kattah/Newman-Toker (interpretación del HINTS y superioridad sobre la RM precoz).
```

---

## Prompt 8 — MUST Agitación Psicomotriz

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
1) Prioriza guías y consensos ESPAÑOLES (consenso español de agitación psicomotriz, SEMES, SEP) y el Manual 12 de Octubre (Tabla 9 de antipsicóticos); usa BAP/Project BETA como complemento y AVISA cuando difieran (fármacos o dosis).
3) NO marques como error estas decisiones DELIBERADAS del autor: (a) la contención VERBAL (de-escalada) es siempre el primer paso deliberado; (b) primero se descarta la organicidad (glucemia, constantes, tóxicos); (c) el R1 sospecha causa vital y avisa; (d) estilo conciso de texto plano, de bolsillo.
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

AGITACIÓN PSICOMOTRIZ EN GUARDIA — GUÍA RÁPIDA PARA EL R1

Lo primero es tu seguridad y la del paciente; el diagnóstico viene después. Idea fija: toda agitación de inicio agudo, en un anciano o en alguien sin antecedentes psiquiátricos, es orgánica hasta que se demuestre lo contrario, y la organicidad puede matar. Nunca te quedes solo con el paciente, ten siempre una vía de salida a tu espalda, retira objetos que sirvan de arma y avisa a seguridad antes de entrar.


CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR

Una mirada de 10 segundos, las constantes y una glucemia capilar. Avisa de inmediato, sin quedarte solo, si hay:
- Riesgo inminente de auto o heteroagresión, o necesidad de contención mecánica.
- Cualquier dato de agitación ORGÁNICA con riesgo vital o causa que descartar: hipoglucemia, hipoxia, traumatismo craneal, sepsis o fiebre, abstinencia alcohólica o de sedantes, intoxicación.
- Alteración del nivel de consciencia (somnolencia, estupor, fluctuación) o focalidad neurológica.
- Constantes alteradas: hipotensión, taquicardia, taquipnea, SpO2 baja, fiebre o hipertensión extrema.
- Sospecha de organicidad por los datos de la Tabla 7: alteración de la consciencia, desorientación, fluctuación, empeoramiento nocturno, alucinaciones visuales, exploración o constantes anormales.
- Fracaso de la contención verbal y farmacológica.
- ECG con QTc largo o cualquier alteración que NO estuviera en electros previos: compara SIEMPRE con los ECG antiguos y, si el cambio es nuevo, avisa antes de dar un antipsicótico.


QUÉ PREGUNTAR

Pregunta al paciente y, sobre todo, a los acompañantes. La meta es separar orgánico de psiquiátrico.
- Inicio y curso: agudo y fluctuante, con empeoramiento nocturno, orienta a orgánico (síndrome confusional); instauración más insidiosa con psicopatología propia, a psiquiátrico.
- Antecedentes psiquiátricos frente a primer episodio: la agitación psiquiátrica aparece en quien ya tiene patología psiquiátrica conocida y sin datos de organicidad; un primer episodio en un adulto mayor obliga a descartar causa orgánica.
- Tóxicos: consumo o abstinencia de alcohol y otras sustancias (la abstinencia alcohólica es causa orgánica tratable y peligrosa).
- Fármacos: revisa la receta electrónica (benzodiacepinas, opioides, anticolinérgicos, corticoides como precipitantes de delirium).
- Enfermedad somática conocida, diabetes (piensa en hipoglucemia) y traumatismo craneal reciente.


QUÉ EXPLORAR (menos de 2 minutos)

Haz lo que la situación permita, sin perder la seguridad.
- GLUCEMIA CAPILAR SIEMPRE: la hipoglucemia es la primera causa tratable.
- Constantes completas: TA, FC, FR, SpO2 y temperatura. Toda alteración apunta a organicidad.
- Nivel de consciencia y orientación; busca fluctuación y desorientación.
- Focalidad neurológica.
- Signos de intoxicación o de abstinencia (temblor, sudoración, taquicardia).
- Estigmas de hepatopatía y signos de venopunción.
- Recuerda la Tabla 7: alteración de la consciencia, desorientación, fluctuación, alucinaciones visuales y constantes o exploración alteradas son datos de organicidad; su ausencia, con antecedentes psiquiátricos, orienta a agitación psiquiátrica.


QUÉ PRUEBAS PEDIR

Si hay cualquier sospecha de organicidad (Tabla 8):
- Glucemia capilar (ya hecha) y, según el caso, glucemia en sangre.
- Hemograma, función renal y hepática, iones.
- Nivel de etanol en sangre ante sospecha de intoxicación etílica; considera hormonas tiroideas (si la exploración es anormal o no hay antecedentes psiquiátricos) y CK (si la agitación es franca).
- Tóxicos en orina, con test de embarazo cuando proceda.
- ECG: mide el QTc ANTES de dar un antipsicótico y vuelve a controlarlo después.
- Gasometría y amonio si lo orienta la clínica.
- TC craneal si hay focalidad, traumatismo craneal o cuadro no filiado.


TRATAMIENTO INICIAL (mientras valoras o avisas)

El primer paso SIEMPRE es la CONTENCIÓN VERBAL (desescalada): contacto ocular sin sostenerlo fijamente, tono bajo pero firme, interésate por el problema y ofrece ayuda. Es especialmente útil en la agitación orgánica, donde la comprensión está alterada. El objetivo es calmar, no sedar.

Corrige lo tratable: si sospechas alcoholismo o encefalopatía de Wernicke, administra tiamina 100 mg IV o IM ANTES de dar glucosa; después corrige la hipoglucemia. Ofrece siempre la medicación por vía oral primero para construir alianza; reserva la parenteral para cuando la rechace.

Contención farmacológica (dosis de la Tabla 9; espera al menos 1 hora antes de repetir):
- Agitación PSIQUIÁTRICA: de elección un antipsicótico de segunda generación. Olanzapina 5-10 mg VO o IM (máx. 20 mg/24 h) o haloperidol 5 mg VO, SC o IV (máx. 100 mg/24 h); puedes asociar una benzodiacepina para potenciar el efecto (midazolam o lorazepam). Alternativas: risperidona 1-2 mg VO (máx. 6 mg/24 h) o aripiprazol 5-10 mg VO o IM (máx. 30 mg/24 h). No administres olanzapina IM y benzodiacepina IM a la vez: deja al menos 1 hora entre ambas.
- Agitación ORGÁNICA (delirium): antipsicótico (haloperidol u olanzapina) y EVITA las benzodiacepinas, porque empeoran el delirium. En ancianos usa un atípico a dosis baja: aripiprazol 5-10 mg (no alarga el QTc), olanzapina 2,5-5 mg o risperidona 0,25-0,5 mg. Haloperidol está contraindicado en demencia por cuerpos de Lewy y en Parkinson.
- Excepción: en la abstinencia alcohólica o de sedantes, y en la intoxicación por estimulantes, la benzodiacepina SÍ es de elección: diazepam 2,5-10 mg VO o IV, lorazepam, o midazolam.

Vigila el QTc antes y después de medicar; no combines fármacos que prolonguen el QT sin un ECG. Si necesitas contención mecánica, avisa: es el último recurso, tras fracasar la verbal y la farmacológica, y exige protocolo y monitorización.


FUENTES (para el residente; puedes borrar este bloque antes de compartir)
- Manual 12 de Octubre 2022, cap. 11 (Tabla 7 organicidad, Tabla 8 pruebas, Tabla 9 antipsicóticos con dosis y máximos) y cap. 58 (síndrome confusional / delirium).
- Notas del vault: Agitación Psicomotriz en Urgencias; Síndrome Confusional Agudo.
- Fichas de fármacos del vault: Haloperidol, Olanzapina, Aripiprazol, Risperidona, Midazolam, Diazepam.
```

---

**Notas de uso**
- Pégalos de uno en uno (OpenEvidence trabaja mejor con una guía por consulta).
- OpenEvidence tira de literatura/guías anglosajonas por defecto; por eso el prompt le pide priorizar ESC/españolas y avisar de divergencias EU/EE. UU. (p. ej. dosis de AAS o ventanas de los inhibidores de la PDE5).
- Si quieres contrastar su salida con mi revisión previa, compáralas: lo que coincida en ambas es lo de mayor confianza.
