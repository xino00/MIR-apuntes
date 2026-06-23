# Prompts para auditar las guías MUST con OpenEvidence

Copia uno de los bloques de abajo y pégalo **entero** en OpenEvidence (mejor de uno en uno). Cada bloque ya incluye el texto ACTUAL y ampliado de la guía, así que no tienes que pegar nada más. Si quieres que conteste solo lo esencial, añade al final: «Resume en los 5 cambios más importantes».

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
1) Prioriza guías EUROPEAS (ESC) y ESPAÑOLAS (SEC, SEMES, GEMA, GALAXIA, SEPAR, SEN, SSC) cuando existan; usa AHA/ACC/GINA/GOLD como complemento y AVISA cuando la recomendación europea/española difiera de la americana (dosis, umbrales o fármacos).
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
3) El estilo es texto plano conciso de bolsillo, sin frontmatter ni referencias dentro de la guía: no lo marques como defecto. Esta guía SÍ detalla el tratamiento concreto (fármaco, dosis, vía e intervalo) por diagnóstico; revisa esas dosis y pautas a fondo, que es lo que más importa.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

DISNEA

Primero asegura vía aérea, oxigenación y ventilación; el diagnóstico exacto viene después. Tu trabajo con el paciente que respira pero está sintomático es orientar hacia el origen (cardíaco, pulmonar, pleural-mecánico, vascular, metabólico o psicógeno), iniciar el tratamiento dirigido cuanto antes y reconocer cuándo el caso se te escapa de las manos. La disnea no es un diagnóstico, es un síntoma con seis grandes culpables que matan rápido: edema agudo de pulmón, crisis de broncoespasmo que claudica, TEP, neumonía grave/sepsis, anafilaxia y neumotórax a tensión. La disnea por ansiedad o hiperventilación es SIEMPRE un diagnóstico de exclusión.


1- CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR
Mirada rápida de 10 segundos — avisa si detectas cualquiera de estos:
- SpO2 <90% pese a oxígeno, o desaturación progresiva.
- FR >30 rpm (taquipnea extrema si >40) o FR <10 rpm (agotamiento → la bradipnea en un paciente que estaba taquipneico anuncia la parada).
- PAS <90 mmHg (shock) o crisis hipertensiva extrema con EAP.
- Trabajo respiratorio intenso: musculatura accesoria, tiraje, respiración abdominal paradójica, habla entrecortada (palabras sueltas), no tolera el decúbito.
- Cianosis central, mala perfusión, o alteración del nivel de consciencia (agitación hipóxica o somnolencia hipercápnica).
- Estridor o sospecha de obstrucción de la vía aérea alta (angioedema, anafilaxia, cuerpo extraño): emergencia de vía aérea, pide ayuda YA.
- "Tórax silente" en un asmático/EPOC que antes pitaba: la desaparición de las sibilancias con trabajo respiratorio es signo ominoso (no entra aire), no de mejoría.
- Dolor torácico o síncope acompañando a la disnea (SCA, TEP de alto riesgo, taponamiento, disección).
- Hipercapnia con pH <7,25 que no remonta, o Glasgow en descenso: candidato a VMNI urgente o intubación.

Regla de oro: el trabajo respiratorio intenso que claudica (FR que baja, somnolencia, paradoja abdominal, tórax que deja de pitar) precede a la parada respiratoria. No esperes a la desaturación: avisa.


2- QUÉ PREGUNTAR (anamnesis dirigida, <3 minutos)

1. TIEMPO DE INSTAURACIÓN
- Súbita (segundos-minutos): TEP, neumotórax, edema agudo de pulmón, arritmia, cuerpo extraño, anafilaxia.
- Horas-días: infección respiratoria, EPOC o asma agudizados, derrame, insuficiencia cardíaca descompensada.
- ¿Es la primera vez o ya le ha pasado? ¿Cómo terminó la última vez (ingreso, UCI, intubación)?

2. POSTURA Y ESFUERZO (muy rentables)
- ¿Empeora al tumbarse (ortopnea) o se despierta de noche ahogado y tiene que sentarse o asomarse a la ventana (disnea paroxística nocturna)? → insuficiencia cardíaca.
- ¿Cuánto esfuerzo aguanta? ¿Hasta dónde camina? ¿Oye pitos en el pecho? → broncoespasmo.
- ¿Cuántas almohadas usa para dormir y cuántas usaba antes? (ortopnea cuantificada).

3. SÍNTOMAS ACOMPAÑANTES
- Dolor pleurítico (aumenta con la inspiración) → TEP, neumotórax, neumonía.
- Tos con fiebre y esputo purulento → infección; esputo rosado y espumoso → edema agudo de pulmón.
- Hemoptisis → TEP, neoplasia, infección.
- Dolor e hinchazón de UNA pierna → TVP (apoya TEP).
- Ortopnea + edemas + nicturia + aumento de peso reciente → insuficiencia cardíaca.
- Urticaria, prurito, angioedema, sensación de cierre de garganta tras un alérgeno (fármaco, alimento, picadura) → anafilaxia.
- Ansiedad con parestesias peribucales/manos y suspiros → hiperventilación (siempre por exclusión, nunca como primera etiqueta).

4. ANTECEDENTES Y MEDICACIÓN
- Cardiopatía, IC, fibrilación auricular, valvulopatía, EPOC, asma, tabaquismo (paquetes-año), oxigenoterapia domiciliaria, enfermedad tromboembólica previa, cáncer, diabetes (cetoacidosis), anemia, insuficiencia renal.
- ¿Toma o ha dejado diuréticos, inhaladores o anticoagulación? La mala adherencia/transgresión dietética es el desencadenante #1 del EAP.
- Factores de riesgo de TEP: cirugía/inmovilización reciente (<4 semanas), neoplasia activa, estrógenos, embarazo/puerperio, TEP-TVP previa.
- Posible exposición a monóxido de carbono (braseros, calderas, varios convivientes con cefalea/náuseas simultáneas — la SpO2 puede ser falsamente normal).
- Revisa la receta electrónica y los informes de alta previos.


3- QUÉ EXPLORAR (exploración dirigida, <2 minutos)
Recuerda: una exploración normal NO descarta enfermedad (ni TEP, ni asma grave, ni acidosis).

CONSTANTES Y TRABAJO RESPIRATORIO
- Cuenta la FR durante 30 segundos (es la constante que más se falsea y la que más predice gravedad).
- Mira el trabajo respiratorio: musculatura accesoria (esternocleidomastoideo), tiraje intercostal/supraclavicular, paradoja abdominal, aleteo nasal.
- Habla: ¿frases completas, frases cortas o palabras sueltas? Es un marcador rápido de gravedad del broncoespasmo.
- Ingurgitación yugular (IC derecha, taponamiento, cor pulmonale, TEP con fallo de VD).

AUSCULTACIÓN PULMONAR
- Sibilancias espiratorias difusas → asma o EPOC. Ojo: el "tórax silente" es PEOR que las sibilancias.
- Crepitantes bibasales húmedos → edema agudo de pulmón o IC; crepitantes focales con fiebre → neumonía.
- Hipofonesis unilateral con matidez a la percusión → derrame pleural; con timpanismo y desviación traqueal contralateral → neumotórax (a tensión si además hay hipotensión/IY).
- Roncus que cambian con la tos → secreciones (bronquitis, EPOC).

AUSCULTACIÓN CARDÍACA
- Ritmo (¿arritmia, FA rápida como desencadenante de IC?), soplos (valvulopatía), tercer ruido o galope (IC), roce pericárdico.

PIERNAS
- Edemas simétricos con fóvea (IC) vs. empastamiento unilateral doloroso de una pantorrilla (TVP → apoya TEP).

VÍA AÉREA ALTA Y PIEL
- Si sospechas obstrucción alta: mira orofaringe, úvula, lengua y cuello (angioedema). Escucha si hay estridor.
- Piel: urticaria/habones, eritema, cianosis central (labios, lengua), livedo, frialdad/sudoración (mala perfusión).


4- QUÉ PRUEBAS PEDIR

INMEDIATAS A PIE DE CAMA
- Pulsioximetría continua. Una SpO2 normal con trabajo respiratorio o taquipnea NO tranquiliza (puede estar compensando): confirma con gasometría.
- Glucemia capilar: una acidosis metabólica con el pulmón limpio orienta a cetoacidosis diabética (respiración de Kussmaul).
- ECG de 12 derivaciones: arritmia, isquemia (SCA como equivalente anginoso de la disnea), signos de sobrecarga derecha en el TEP (S1Q3T3, BRD, T negativas en V1-V4; lo más frecuente sigue siendo la taquicardia sinusal).

GASOMETRÍA
- Gasometría arterial (o venosa para un primer cribado de pH/CO2/HCO3): valora hipoxemia, hipercapnia y estado ácido-base. Define la insuficiencia respiratoria (PaO2 <60 y/o PaCO2 >45 mmHg) y, sobre todo, decide la VMNI.
- Distingue aguda (pH <7,35 con HCO3 normal) de crónica reagudizada (pH casi normal con HCO3 elevado). El pH es el que manda para la VMNI, no la cifra absoluta de CO2 del retenedor crónico.
- Gradiente A-a [normal = 2,5 + (0,21 × edad)]: si está elevado con hipoxemia, la falla es pulmonar/vascular (neumonía, EAP, TEP, SDRA); si es normal con hipercapnia, es hipoventilación pura (depresión SNC, neuromuscular).

ANALÍTICA E IMAGEN
- Hemograma y bioquímica (anemia, función renal, iones, glucosa; TSH si procede).
- Péptidos natriuréticos si sospechas IC: rule-out agudo si NT-proBNP <300 o BNP <100 (descarta IC con alto valor predictivo negativo).
- Troponinas seriadas si sospecha de SCA o para estratificar el TEP (un TEP con troponina/BNP elevados o VD dilatado es de mayor riesgo).
- Dímero-D solo si probabilidad clínica de TEP baja/intermedia (ver escalas); con corte ajustado a edad.
- Radiografía de tórax: condensación (neumonía), líneas B de Kerley/redistribución/cardiomegalia/derrame (IC-EAP), neumotórax, masa. Una Rx normal NO excluye TEP, asma grave ni acidosis.
- Ecografía a pie de cama (POCUS) si está disponible: líneas B difusas y VCI dilatada no colapsable en EAP/IC, derrame, deslizamiento pleural ausente en neumotórax, dilatación de VD en TEP. >3 líneas B en ≥2 zonas por hemitórax = edema pulmonar (S/E >95%).

ESCALAS DE PROBABILIDAD CLÍNICA
- Wells / Geneva (TEP): Wells <2 bajo, 2-6 moderado, >6 alto (binario: ≤4 TEP improbable). Geneva simplificada: 0-2 improbable, 3-7 probable. Si probabilidad baja/intermedia → dímero-D con corte ajustado a edad (edad × 10 ng/ml en >50 años) descarta TEP sin imagen. Si alta → angio-TC (CTPA) directa sin esperar al dímero. Regla PERC (solo si probabilidad <15%): si los 8 criterios son negativos, descarta TEP sin más pruebas.
- NT-proBNP (IC, rule-in por edad, ESC 2021): >450 (<50 años), >900 (50-75 años), >1.800 (>75 años). En obesidad los cortes bajan ~50%. Rule-out global: <300.
- CURB-65 (neumonía): Confusión, Urea >7 mmol/L (BUN >19 mg/dL), FR ≥30, PAS <90 o PAD ≤60, edad ≥65. 0-1 = ambulatorio; 2 = valorar ingreso/observación; ≥3 = ingreso, valorar UCI. (Complementar con FINE-PSI si procede.)
- Anthonisen (agudización de EPOC, criterios ampliados GOLD): aumento de disnea, aumento del volumen del esputo, aumento de la purulencia del esputo (± fiebre). Antibiótico si ≥2 criterios, SIEMPRE que uno sea la purulencia, o si el paciente precisa ventilación mecánica (invasiva o no).
- Gravedad de la crisis asmática (GEMA): LEVE (habla en párrafos, FR normal, SpO2 >95%, FEV1/PEF >70%); MODERADA (habla en frases, FR 20-30, SpO2 90-95%, FEV1/PEF 50-70%); GRAVE (habla en palabras, FR >30, FC >120, SpO2 <90%, FEV1/PEF <50%, pulso paradójico); RIESGO VITAL / near-fatal (somnolencia/confusión, BRADICARDIA, tórax silente, gasping, SpO2 <90%, y el dato gasométrico clave: PaCO2 >45 mmHg = agotamiento). Una PaCO2 "normal o alta" en plena crisis grave es ominosa (debería estar baja por la taquipnea).
- Gravedad del EPOC reagudizado (propuesta de Roma, GOLD 2026): MODERADA si ≥3 de (disnea VAS ≥5, FR ≥24, FC ≥95, SpO2 <92% en aire ambiente, PCR ≥10 mg/L); GRAVE si PaO2 ≤60 y/o acidosis (pH <7,35 con PaCO2 >45). La acidosis hipercápnica es la que define la indicación de VMNI.
- Gravedad de la IRA (gasométrica): Tipo I/hipoxémica (PaO2 <60 con PaCO2 normal-baja: neumonía, EAP, TEP, SDRA); Tipo II/hipercápnica (PaCO2 >45: EPOC agudizado grave, asma casi fatal, hipoventilación). El efecto shunt (SDRA, EAP masivo, neumonía masiva) NO corrige con O2 a alto flujo y exige presión positiva (CPAP/VMNI/PEEP).

⚠ TRAMPAS COMUNES
- Una radiografía normal NO excluye TEP, asma grave ni acidosis. Si la clínica orienta, sigue el algoritmo (escala → dímero/angio-TC).
- En el TEP lo más frecuente es la taquicardia sinusal; la ausencia de S1Q3T3 no descarta nada.
- SpO2 normal con trabajo respiratorio o taquipnea no tranquiliza: puede estar compensando. Mira la gasometría.
- Acidosis metabólica con pulmón limpio = busca causa metabólica (cetoacidosis, sepsis, tóxicos, salicilatos), no respiratoria. El paciente "hiperventila" para compensar, no por patología pulmonar.
- Oxígeno a alto flujo en el retenedor de CO2 puede empeorar la hipercapnia y bajar el nivel de consciencia: objetivo SpO2 88-92%, no más.
- Hasta el 20% de las anafilaxias NO tienen síntomas cutáneos (sobre todo las alimentarias): la ausencia de urticaria no la descarta.
- "Tórax silente" = no entra aire = gravedad máxima. No lo confundas con mejoría porque "ya no pita".
- SpO2 normal NO descarta intoxicación por CO (la carboxihemoglobina engaña al pulsioxímetro): si hay sospecha epidemiológica, pide cooximetría/carboxiHb.
- PaCO2 normal en una crisis asmática grave taquipneica es un signo de alarma, no de normalidad: significa que el paciente ya no puede mantener la hiperventilación.


5- MEDIDAS Y TRATAMIENTO SEGÚN SOSPECHA

MEDIDAS GENERALES DE SOPORTE
- Incorpora al paciente (sedestación/Fowler), monitoriza (TA, FC, FR, SpO2, ECG), coge vía venosa periférica y extrae analítica/gasometría; glucemia capilar inmediata.
- Oxígeno con objetivo de SpO2 94-98% en la mayoría; 88-92% si es EPOC o retenedor de CO2 conocido. Escalado: gafas nasales → mascarilla Venturi → mascarilla con reservorio → gafas nasales de alto flujo (GNAF) en la insuficiencia hipoxémica pura → presión positiva (VMNI) según indicación.
- Si bajo nivel de consciencia (Glasgow <8) o incapacidad de proteger la vía aérea → preparar intubación; avisa.
- Trata el desencadenante específico en paralelo al soporte: no esperes al diagnóstico de imagen para empezar broncodilatadores, diurético, adrenalina o antibiótico si la sospecha es clara.

CRITERIOS Y AJUSTES DE VMNI (BiPAP/CPAP) — no lo dejes en "valora con el adjunto"
- INDICACIONES principales (avisa al adjunto en paralelo, pero conoce el umbral):
  → EPOC reagudizado con acidosis hipercápnica: pH ≤7,35 con PaCO2 ≥45 mmHg pese a tratamiento médico inicial. Es indicación IA (BiPAP). Cuanto más precoz, mejor; no esperes a que el pH baje de 7,25.
  → Edema agudo de pulmón / IC con disnea grave, FR >25, SpO2 <90% (FiO2 0,5), uso de musculatura accesoria o pH <7,35: CPAP (o BiPAP). Reduce la necesidad de intubación.
  → Insuficiencia respiratoria hipoxémica que no mejora con GNAF (con cautela).
- MODALIDAD: BiPAP (dos niveles de presión) en el fallo hipercápnico (EPOC, asma — esta última con extrema cautela y siempre con el adjunto); CPAP (presión continua) en el EAP cardiogénico, donde el problema es el reclutamiento alveolar y la precarga.
- PARÁMETROS INICIALES ORIENTATIVOS:
  → BiPAP: IPAP (presión inspiratoria) 10-12 cmH2O subiendo de 2 en 2 hasta 15-20 según volumen corriente y confort; EPAP/PEEP 4-5 cmH2O. FiO2 mínima para SpO2 88-92% (EPOC).
  → CPAP en EAP: 7,5-10 cmH2O (empezar en ~7,5 y subir a 10 si tolera). FiO2 para SpO2 ≥94%.
- REEVALUACIÓN: gasometría de control a los 30-60 min. Si el pH y la PaCO2 no mejoran, o empeora el nivel de consciencia → fracaso de VMNI → considerar intubación/UCI.
- CONTRAINDICACIONES: bajo nivel de consciencia que impide proteger la vía aérea, parada inminente, shock/inestabilidad hemodinámica grave, vómitos/riesgo de aspiración, agitación incontrolable, traumatismo/cirugía facial, secreciones abundantes no manejables.
- CRITERIOS DE INTUBACIÓN (no demorar): parada respiratoria, agotamiento con bradipnea, Glasgow en descenso, pH <7,25 que persiste tras 1 h de VMNI bien ajustada, hipoxemia refractaria, inestabilidad hemodinámica. En el asma casi fatal, preparar IOT con ketamina (broncodilatadora y sedante).

A. BRONCOESPASMO (ASMA O EPOC AGUDIZADO)
Soporte: oxígeno con objetivo SpO2 93-95% en el asma; 88-92% en el EPOC retenedor. GNAF si insuficiencia hipoxémica.
- BRONCODILATADORES DE ACCIÓN CORTA (la base del tratamiento, ya):
  → Salbutamol (SABA) nebulizado 2,5-5 mg + bromuro de ipratropio (SAMA) 0,5 mg, repetible cada 20 min durante la primera hora (doble broncodilatación en crisis moderada-grave).
  → Alternativa con cámara espaciadora (igual de eficaz, facilita en paciente colaborador): salbutamol 4-8 pulsaciones (100 mcg/puff) + ipratropio 4-8 puff cada 10-15 min la primera hora.
  → En crisis muy grave / box: nebulización continua de salbutamol 10-15 mg/h. En EPOC, frecuencia inicial cada hora (p. ej. 400/80 mcg de SABA/SAMA o nebulización si mucho trabajo respiratorio).
- CORTICOIDE SISTÉMICO PRECOZ (en los primeros 60 min; no acelera la crisis aguda pero frena la inflamación y reduce recaídas):
  → ASMA: prednisona/prednisolona 50 mg VO en dosis única precoz, y continuar 50 mg/24 h × 5-7 días al alta SIN pauta descendente. Si intolerancia oral, shock o gravedad extrema: hidrocortisona 100-200 mg IV o metilprednisolona 40-60 mg IV.
  → EPOC: prednisona 40 mg VO/24 h × 5 días (vía oral = vía IV en eficacia; reservar IV para vómitos o bajo nivel de consciencia).
- SULFATO DE MAGNESIO en crisis GRAVE que no responde al tratamiento inicial: 2 g IV en 20 minutos, dosis única (potente relajante del músculo liso bronquial). Indicado sobre todo en el asma grave; razonable en EPOC grave refractario.
- ANTIBIÓTICO EN EPOC (criterios de Anthonisen ≥2, sobre todo si hay purulencia, o si precisa ventilación mecánica): durante 5 días.
  → Leve/moderada sin comorbilidad: amoxicilina/clavulánico 500/125 mg/8 h × 5 días.
  → Moderada con comorbilidad o grave: amoxicilina/clavulánico 875/125 mg/8 h o levofloxacino 500 mg/24 h × 5-7 días.
  → Riesgo de Pseudomonas (FEV1 <30%, bronquiectasias, ingresos repetidos, antibióticos frecuentes, intubación previa): ciprofloxacino 750 mg/12 h × 7-10 días.
  → Alergia a betalactámicos: azitromicina 500 mg/24 h × 3 días o levofloxacino.
- VMNI (BiPAP) precoz si insuficiencia respiratoria hipercápnica con acidosis (pH ≤7,35 y PaCO2 ≥45) pese a tratamiento médico — avisa al adjunto y aplica los parámetros de arriba. No retrasarla.
- Reevaluar a la hora: buena respuesta (SpO2 >94% en aire, PEF >70%, cede tiraje/sibilancias) → plantear alta con SABA a demanda + corticoide oral 5-7 días + revisión en ≤5 días. Mala respuesta o factores de riesgo vital (UCI/IOT previa por asma) → ingreso/UCI.

B. EDEMA AGUDO DE PULMÓN / INSUFICIENCIA CARDÍACA
Soporte: sienta al paciente con las piernas colgando. Oxígeno solo si SpO2 <90% (88-92% si EPOC). CPAP precoz si disnea grave/FR >25/SpO2 <92% con FiO2 0,5 o pH <7,35 (reduce la intubación) — parámetros arriba.
- DIURÉTICO DE ASA (pilar de la congestión):
  → Furosemida IV en bolo: 20-40 mg si es de novo / sin diurético previo; si ya tomaba furosemida oral, administrar 1-2 veces (ESC) la dosis oral diaria total por vía IV. El Manual 12 de Octubre es más agresivo (hasta 2,5 veces la dosis oral previa); en la práctica se inicia según ESC y se ajusta rápido si no hay respuesta.
  → Si insuficiencia renal (regla práctica del Manual 12 Oct): tantas ampollas de furosemida en bolo como la cifra de creatinina (p. ej. Cr 3 mg/dL → 3 ampollas).
  → Objetivos: diuresis >100-150 ml/h en las primeras 6 h y sodio urinario a las 2 h >50-70 mEq/L. Reevaluar respuesta a los 60-120 min. Si resistencia: doblar la dosis IV (máx. 400-600 mg/día), y si persiste, bloqueo secuencial de nefrona (añadir tiazida o acetazolamida 500 mg IV).
- VASODILATADOR (si PAS >110 mmHg, especialmente en EAP hipertensivo): nitroglicerina sublingual 0,4 mg (puede repetirse) o, mejor, en perfusión IV 10-200 µg/min titulando a la TA. EVÍTALA si PAS <90 mmHg o si hay estenosis aórtica severa.
- NO uses morfina de rutina (aumenta intubación, VMNI e hipotensión; ESC clase III). Resérvala solo para dolor isquémico o ansiedad irreductible.
- Identifica y trata el desencadenante (CHAMP: SCA, crisis hipertensiva, arritmia/FA rápida, causa mecánica valvular, TEP). NO suspendas IECA/ARA-II/sacubitrilo-valsartán ni betabloqueante crónicos salvo hipotensión sintomática o hipoperfusión (no inicies betabloqueante en fase aguda).
- Shock cardiogénico (frío y húmedo, PAS <90 + hipoperfusión): avisa a UCI; inotrópicos (dobutamina) y/o noradrenalina si no responde. No es manejo de R1 en solitario.

C. TEP DE ALTA SOSPECHA
Soporte: oxígeno con objetivo SpO2 >90%. Fluidoterapia CAUTELOSA (evita sobrecargar el VD; pequeños bolos de 250 ml si hipotensión, vigilando).
- ANTICOAGULACIÓN (iniciar ante alta sospecha sin esperar a la imagen si no hay contraindicación; coméntalo con el adjunto):
  → HBPM de elección: enoxaparina 1 mg/kg/12 h SC (o 1,5 mg/kg/24 h SC). Si FG <30 ml/min: 1 mg/kg/24 h SC.
  → Heparina no fraccionada IV (bolo 80 UI/kg + perfusión 18 UI/kg/h, ajustada por aPTT) SOLO si inestabilidad hemodinámica, alto riesgo de sangrado/reversión rápida previsible, o si se prevé fibrinólisis/procedimiento inminente.
  → Mantenimiento posterior con ACOD (apixabán, rivaroxabán, edoxabán, dabigatrán) salvo FG <30, embarazo (HBPM) o cáncer digestivo/GU.
- TEP DE ALTO RIESGO (inestabilidad hemodinámica: PAS <90 o caída >40 mmHg >15 min, shock, fallo de VD): es una emergencia.
  → FIBRINÓLISIS SISTÉMICA si no hay contraindicación: alteplasa 100 mg IV en 2 h (o régimen acelerado 0,6 mg/kg, máx. 50 mg, en 15 min en parada/periparada). Avisa a UCI y activa el PERT (Pulmonary Embolism Response Team) si existe.
  → Si contraindicación a fibrinólisis o fracaso: trombólisis dirigida por catéter, trombectomía percutánea o embolectomía quirúrgica.
- Estratifica el riesgo intermedio (VD dilatado en angio-TC/eco + troponina/BNP elevados): vigilancia estrecha (telemetría/UCI), fibrinólisis de rescate si se deteriora.

D. ANAFILAXIA (disnea con urticaria/angioedema, estridor o hipotensión tras un alérgeno; recuerda que hasta el 20% no tiene clínica cutánea)
- ADRENALINA IM YA, es el ÚNICO tratamiento de primera línea y no debe retrasarse:
  → 0,5 mg IM (0,01 mg/kg) en la cara anterolateral del muslo, concentración 1:1.000 (1 mg/ml). Repetible cada 5-15 min si no hay respuesta.
  → NO la retrases dando antes corticoide o antihistamínico (son solo coadyuvantes, sin efecto sobre la hipotensión ni el broncoespasmo agudo).
- POSICIÓN: decúbito supino con piernas elevadas (lateral izquierdo si embarazada; semisentado si predomina la disnea). NO sentar ni poner de pie bruscamente (riesgo de colapso).
- OXÍGENO a alto flujo (FiO2 50-100%, 10-15 L/min, objetivo SpO2 >95%) y FLUIDOS: SSF 0,9% 1-2 L en infusión rápida si hipotensión (125 ml/h si normotenso).
- COADYUVANTES (después de la adrenalina, nunca en su lugar):
  → Antihistamínico H1: dexclorfeniramina (Polaramine) 5 mg IV.
  → Corticoide: metilprednisolona 1-2 mg/kg IV o hidrocortisona 200 mg IV (inicio más rápido; inyectar lento).
  → Salbutamol nebulizado 2,5-5 mg si broncoespasmo asociado.
- BETABLOQUEADOS resistentes a adrenalina: glucagón 1-2 mg IV (máx. 5 mg), repetir a los 5 min o perfusión 5-15 µg/min.
- REFRACTARIA (≥2 dosis IM sin respuesta): perfusión IV de adrenalina (1 mg en 100 ml SSF; inicio 0,5-1 ml/kg/h) en medio monitorizado + vasopresores (noradrenalina) si hipotensión persistente. Avisa a UCI. Es box vital.
- Observación mínima 4-6 h asintomático (8-24 h si grave o factores de riesgo de reacción bifásica). Al alta: autoinyector de adrenalina + evitación del alérgeno + derivación a Alergología.

E. NEUMONÍA (NAC)
Soporte: oxígeno según objetivo. Antibiótico empírico PRECOZ (no lo demores si hay datos de sepsis; idealmente en la primera hora si shock séptico). Estratifica con CURB-65 para decidir destino y vía.
- AMBULATORIO (CURB-65 0-1):
  → Típica, <65 años, sin comorbilidad, no EPOC: amoxicilina/clavulánico 875/125 mg/8 h + azitromicina 500 mg/24 h × 3-5 días (cobertura de atípicos obligatoria). Alternativa en monoterapia o si alergia: levofloxacino 500 mg/24 h × 5 días.
  → Paciente frágil / >65 años / comorbilidad / EPOC / institucionalizado / >3 ciclos de antibiótico en el último año: amoxicilina/clavulánico 875/125 mg/8 h × 7 días; alérgicos: levofloxacino 500 mg/24 h × 7 días.
- HOSPITALARIO (CURB-65 ≥2 o criterios de ingreso): ceftriaxona 1-2 g/24 h IV (o cefotaxima 2 g/8 h IV) + macrólido (azitromicina 500 mg/24 h o claritromicina 500 mg/12 h); alternativa en monoterapia: levofloxacino 500 mg/12 h IV o moxifloxacino 400 mg/24 h. Valora UCI si CURB-65 ≥3 con criterios de gravedad.
- Si hay sepsis/shock séptico: hemocultivos antes del antibiótico (sin retrasarlo), fluidoterapia y manejo de sepsis en paralelo.

F. NEUMOTÓRAX A TENSIÓN
Emergencia de procedimiento: NO se resuelve con un fármaco y NO espera a la radiografía. Sospéchalo ante disnea súbita + hipofonesis/timpanismo unilateral + hipotensión + ingurgitación yugular ± desviación traqueal.
- DESCOMPRESIÓN INMEDIATA con aguja/angiocatéter grueso (14-16 G): 2º espacio intercostal en la línea medioclavicular, o 4º-5º espacio intercostal en la línea axilar media/anterior (preferido en adultos por la pared más fina). Avisa de inmediato.
- A continuación, colocación de DRENAJE PLEURAL (tubo de tórax) definitivo.
- Oxígeno a alto flujo mientras tanto. Es una de las pocas situaciones en que actúas con las manos antes que con cualquier prueba.


6- PERLAS PARA NO OLVIDAR

🔑 Primero ABC, después diagnóstico. El trabajo respiratorio que claudica (FR que cae, somnolencia, paradoja abdominal, tórax que deja de pitar) anuncia la parada: avisa antes de la desaturación.

🔑 La disnea por ansiedad o hiperventilación es SIEMPRE un diagnóstico de exclusión. Nunca la etiquetes sin haber descartado lo orgánico (incluida la acidosis metabólica y el TEP).

🔑 Ortopnea + disnea paroxística nocturna + edemas + nicturia = insuficiencia cardíaca. Furosemida IV + nitroglicerina si PAS >110, sienta al paciente y pon CPAP si lo precisa. El NT-proBNP rule-out (<300) ayuda a descartarla.

🔑 No des morfina de rutina en el edema agudo de pulmón. Aumenta la intubación, la VMNI y la hipotensión. El tratamiento es furosemida, nitroglicerina (si PAS >110) y presión positiva.

🔑 Rx normal no descarta TEP. Estima la probabilidad (Wells/Geneva), ajusta el dímero-D a la edad y, en alta probabilidad, pide angio-TC directa sin esperar. Anticoagula ante alta sospecha; fibrinólisis si hay shock.

🔑 En el EPOC retenedor, objetivo SpO2 88-92%. El oxígeno a alto flujo le sube el CO2 y le baja el nivel de consciencia. Y la VMNI se indica por el pH (≤7,35 con hipercapnia), no por la cifra absoluta de CO2.

🔑 "Tórax silente" en un asmático/EPOC = no entra aire = riesgo vital. Es lo contrario de mejoría. Sulfato de magnesio 2 g IV en la crisis grave que no responde, y prepárate para intubar (ketamina).

🔑 Anafilaxia = adrenalina IM en el muslo (0,5 mg), YA. Corticoide y antihistamínico son coadyuvantes, no la primera medida, y no deben retrasarla. Hasta el 20% no tiene urticaria: no la descartes por la piel.

🔑 Estridor o angioedema con disnea = emergencia de vía aérea. Pide ayuda y prepárate para una vía aérea difícil; no lo dejes para más tarde.

🔑 Antibiótico precoz en la neumonía con sepsis (primera hora si shock). En el EPOC, antibiótico si Anthonisen ≥2 con purulencia o si necesita ventilación mecánica.

🔑 Neumotórax a tensión: descompresión con aguja (4º-5º EIC línea axilar media o 2º EIC línea medioclavicular) antes de la radiografía. Se trata con las manos, no con la imagen.

🔑 SpO2 normal con taquipnea o trabajo respiratorio no tranquiliza: mira la gasometría. Y recuerda que en la intoxicación por CO la SpO2 también engaña (pide carboxiHb).
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
1) Prioriza guías EUROPEAS (ESC) y ESPAÑOLAS (SEC, SEMES, GEMA, GALAXIA, SEPAR, SEN, SSC) cuando existan; usa AHA/ACC/GINA/GOLD como complemento y AVISA cuando la recomendación europea/española difiera de la americana (dosis, umbrales o fármacos).
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
3) El estilo es texto plano conciso de bolsillo, sin frontmatter ni referencias dentro de la guía: no lo marques como defecto. Esta guía SÍ detalla el tratamiento concreto (fármaco, dosis, vía e intervalo) por diagnóstico; revisa esas dosis y pautas a fondo, que es lo que más importa.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

DOLOR TORÁCICO

Lo primero es descartar lo mortal. Tu trabajo en la puerta no es cerrar el diagnóstico, es separar al paciente que esconde una de las 6 causas letales (SCA, TEP, síndrome aórtico, taponamiento, neumotórax a tensión, rotura esofágica) del que puede esperar. Idea fija: hasta un 5% de los "dolores no isquémicos" dados de alta eran en realidad un infarto; no cierres el caso como ansiedad u osteomuscular sin descartar antes lo grave. El ECG en los primeros 10 minutos y la troponina seriada son tus dos herramientas; ninguna prueba aislada y normal descarta el SCA.


1- CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR
Toma constantes y haz un ECG en los primeros 10 minutos. Mirada rápida de 10 segundos — avisa si detectas cualquiera de estos:
- PAS <90 mmHg o FC >100-110 lpm (inestabilidad hemodinámica), o signos de mala perfusión (palidez, sudoración fría, obnubilación): sospecha de shock.
- PAS >180 mmHg o PAD >110 mmHg (hipertensión arterial extrema), sobre todo si sospechas síndrome aórtico.
- FR >30 o <10 rpm, o SpO2 <90%.
- Bajo nivel de consciencia o focalidad neurológica (la disección que ocluye carótidas da ictus; el TEP masivo, síncope).
- ECG con elevación del ST (SCACEST): avisa a la Unidad Coronaria / Hemodinámica de inmediato (Código Infarto). Un bloqueo de rama izquierda u otra alteración que no estuviera en electros previos también es bandera roja: compara SIEMPRE con los ECG antiguos para confirmar que el cambio es nuevo. Ante un BRI con clínica isquémica, los criterios de Sgarbossa aumentan la especificidad de oclusión coronaria aguda.
- Dolor desgarrador y migratorio a la espalda + asimetría de pulsos o diferencia de TA entre brazos → síndrome aórtico: avisa a cirugía cardiovascular / UCI.
- Tríada de Beck (ingurgitación yugular + hipotensión + tonos apagados) → taponamiento cardíaco: es procedimiento, avisa ya.
- Hipofonesis unilateral + timpanismo + disnea extrema + desviación traqueal → neumotórax a tensión: descomprime sin esperar a la radiografía.
- Vómito violento o instrumentación esofágica reciente + dolor + enfisema subcutáneo (signo de Hamman) → rotura esofágica.
- Arritmia ventricular maligna o parada cardiorrespiratoria recuperada.

Regla de oro: ante sospecha de causa potencialmente mortal, sospecha y avisa; no te pongas a estratificar tú solo con escalas. La decisión de destino la cierra el adjunto, pero el paquete de tratamiento inicial (AAS, antiagregante, anticoagulación, betabloqueo, anticoagulación del TEP…) puedes y debes iniciarlo según la sospecha.


2- QUÉ PREGUNTAR (anamnesis dirigida, <3 minutos)

1. INICIO Y DURACIÓN
- Brusco y máximo desde el primer segundo → aórtico o TEP/neumotórax.
- Progresivo (crescendo) → isquémico.
- <5 min, cede con reposo o nitroglicerina → angina estable.
- >20 min en reposo y que no cede → sospecha de SCA.

2. CUALIDAD E IRRADIACIÓN
- Opresivo, "como un peso", irradiado a mandíbula, cuello, hombros o brazo → isquémico.
- Desgarrador "como si se rompiera algo" y migratorio a la espalda/escápulas/abdomen → aórtico.
- Punzante a punta de dedo que aumenta al respirar o toser → pleurítico (TEP, neumotórax, neumonía).
- Urente retroesternal → esofágico.
- Irradiado a los trapecios y que mejora inclinándose hacia delante → pericárdico.

3. MODIFICADORES
- Mejora al inclinarse hacia delante (plegaria mahometana) → pericárdico.
- Se reproduce a la palpación → osteomuscular (solo tras descartar lo grave).
- Cede con nitroglicerina → isquémico (ojo: el espasmo esofágico también cede a nitratos).
- Desencadenado por ingesta o decúbito → esofágico.

4. SÍNTOMAS ACOMPAÑANTES
- Cortejo vegetativo (sudor frío, náuseas, vómitos) y sensación de muerte inminente → SCA o aórtico.
- Disnea súbita → TEP, neumotórax.
- Síncope → TEP, estenosis aórtica, síndrome aórtico, taponamiento.
- Fiebre con tos → neumonía o pericarditis.
- Hemoptisis → TEP.

5. ANTECEDENTES Y FACTORES DE RIESGO
- FRCV (HTA, DM, dislipemia, tabaco, antecedentes familiares). Ojo al perfil atípico (mujer, anciano, diabético: equivalentes anginosos sin dolor típico; hasta el 80% de presentaciones de SCA pueden ser atípicas).
- Riesgo de TEP: cáncer activo, inmovilización o cirugía reciente (<4 semanas), trombosis previa, anticonceptivos/estrógenos, embarazo/puerperio.
- Riesgo aórtico: HTA mal controlada (principal FR), Marfan u otra conectivopatía, válvula aórtica bicúspide, aneurisma conocido, cocaína/anfetaminas, manipulación aórtica reciente.
- Toma de anticoagulantes/antiagregantes (condiciona fibrinólisis y reversión), e inhibidores de PDE5 (sildenafilo/tadalafilo) en las últimas 24-48 h (contraindican nitratos).
- Revisa la receta electrónica.


3- QUÉ EXPLORAR (exploración dirigida, <2 minutos)
Recuerda: una exploración normal NO descarta enfermedad.

CONSTANTES
- TA, FC, FR, SpO2, Tª y glucemia capilar. Toma la TA en AMBOS brazos si sospechas síndrome aórtico.

AUSCULTACIÓN CARDÍACA
- Soplo diastólico de insuficiencia aórtica nuevo → disección tipo A (en el 75% de las tipo A).
- Roce pericárdico (pericarditis; se oye mejor con el tronco inclinado hacia delante y al final de la espiración).
- Tonos apagados → taponamiento.

AUSCULTACIÓN PULMONAR
- Hipofonesis unilateral con timpanismo → neumotórax.
- Crepitantes o condensación → neumonía. Crepitantes bibasales + 3.er ruido → insuficiencia cardiaca por el SCA (Killip II).

INSPECCIÓN Y PALPACIÓN
- Ingurgitación yugular + hipotensión + tonos apagados (tríada de Beck) → taponamiento cardíaco.
- Pulso paradójico (caída de PAS >10 mmHg en inspiración) → taponamiento (prácticamente patognomónico en contexto).
- Palpa la pared torácica: si reproduce exactamente el dolor, orienta a osteomuscular (Tietze).
- Piernas: signos de TVP (edema unilateral, dolor) apoyan el TEP.
- Piel: vesículas de herpes zóster siguiendo un dermatoma; enfisema subcutáneo o crepitación con el latido (signo de Hamman) en la rotura esofágica.

DIRIGIDA (si sospechas síndrome aórtico agudo)
- Toma la TA en ambos brazos y compara los pulsos; la asimetría de pulsos o una diferencia de TA >20 mmHg entre miembros apoya la disección.


4- QUÉ PRUEBAS PEDIR

- ECG de 12 derivaciones en <10 min (ya en el filtro). Amplía a derivaciones derechas (V3R-V4R) y posteriores (V7-V9) si sospechas infarto inferior o posterior. Compara SIEMPRE con ECG previos. Un ECG normal NO excluye el SCA (hasta un 30% de los IAMSEST tienen ECG normal).
- Troponina: con troponina ultrasensible, algoritmo seriado 0/1 h (alternativa 0/2 h) valorando el valor basal y su variación (delta); con troponina convencional, segundo control a las 3-6 h. Un único valor normal muy precoz no descarta. Recuerda que se eleva en otras causas (TEP, disección, miocarditis, IC, sepsis, ERC): la elevación aislada sin clínica ni cambios dinámicos es "daño miocárdico", no SCA.
- Radiografía de tórax: mediastino ensanchado / botón aórtico prominente (aórtico), neumotórax, condensación, derrame, cardiomegalia "en cantimplora/tetera" (derrame pericárdico), neumomediastino o derrame pleural izquierdo (rotura esofágica). Una Rx normal NO excluye TEP ni disección.
- Analítica básica con hemograma, coagulación (INR, aPTT), bioquímica (creatinina, iones, glucosa) y, según sospecha, dímero-D, lactato y NT-proBNP. Cruza y reserva si sospechas sangrado (aórtico).
- Ecografía a pie de cama (POCUS) si está disponible: derrame/taponamiento, sobrecarga de VD (TEP), disfunción ventricular, líquido libre. En el TEP/disección inestables, el ETT es la prueba inicial.
- Síndrome aórtico: la prueba es la angio-TC de aorta; si ADD-RS ≥2, pídela urgente independientemente del dímero-D, y avisa al adjunto.
- TEP: la prueba confirmatoria es la angio-TC (CTPA), reportando ratio VD/VI. Gammagrafía V/Q si contraindicación de contraste o embarazo.

Escalas de probabilidad clínica
- HEART (dolor torácico en urgencias): History, ECG, Age, Risk factors, Troponina (0-2 cada uno). 0-3 = bajo riesgo (MACE ~1,7%, valorar alta precoz); 4-6 = riesgo intermedio (observación + troponina seriada); ≥7 = alto riesgo (ingreso, estrategia invasiva).
- GRACE / TIMI (SCA ya diagnosticado): estratifican el riesgo y marcan el momento del cateterismo en el SCASEST. GRACE >140 (o TIMI alto) = alto riesgo → coronariografía <24 h; muy alto riesgo (inestabilidad, IC/shock, arritmia maligna, dolor refractario) → <2 h. La estrategia la decide cardiología, pero el GRACE orienta la urgencia.
- Wells / Geneva (TEP): si probabilidad baja o intermedia, dímero-D con corte ajustado a edad (edad × 10 ng/ml en >50 años) descarta TEP sin angio-TC. Si alta, angio-TC directa. Regla PERC: solo si probabilidad muy baja (<15%), los 8 criterios negativos descartan TEP sin más pruebas.
- Sgarbossa (BRI o marcapasos con clínica isquémica): ST concordante ≥1 mm, descenso ST ≥1 mm en V1-V3, o ST discordante desproporcionado ≥5 mm (Smith-modificado) → sugiere oclusión coronaria.
- ADD-RS (síndrome aórtico): suma 1 punto por cada categoría con ≥1 criterio (condición predisponente / dolor de características aórticas / hallazgos exploratorios; máx. 3). ADD-RS ≤1 + dímero-D negativo (<500 ng/ml) → puede diferirse la angio-TC. ADD-RS ≥2 → angio-TC urgente independientemente del dímero-D.

⚠ TRAMPAS COMUNES
- ECG normal NO excluye SCA. Repite el ECG y seria troponina si la clínica es sugestiva.
- Una troponina precoz única normal NO descarta SCA. Necesitas el delta seriado.
- Rx de tórax normal NO excluye TEP ni disección. La normalidad no tranquiliza.
- En el TEP lo más frecuente es la taquicardia sinusal; los signos de sobrecarga derecha (S1Q3T3, T negativas V1-V4) aparecen solo en casos graves, así que su ausencia no descarta TEP.
- El dolor que cede con nitroglicerina NO confirma origen coronario (el espasmo esofágico también cede).
- En la disección, el ECG puede ser indistinguible de un IAM tipo 1 (10% comprimen una coronaria): si lo etiquetas de SCA y antiagregas/anticoagulas/fibrinolizas, puedes matar al paciente. Ante dolor desgarrador + asimetría de pulsos, piensa en aorta ANTES de dar AAS.
- No etiquetes de osteomuscular, esofágico o ansiedad hasta haber descartado lo grave.


5- MEDIDAS Y TRATAMIENTO SEGÚN SOSPECHA

MEDIDAS GENERALES DE SOPORTE
- Monitorización continua: TA, FC, SatO₂, ECG. Coge vía (dos vías de grueso calibre si sospechas shock o sangrado) y extrae analítica.
- Oxígeno solo si SpO2 <90% (en el SCA el oxígeno innecesario es perjudicial: vasoconstricción coronaria y mayor daño miocárdico).
- Trata el dolor desde el principio; no enmascara el diagnóstico.
- ABC. Si el paciente está inestable, soporte vital y avisa antes de filiar.

A. SOSPECHA DE SCA
Fuente principal de las dosis: nota del vault "SCA - Tratamiento Médico" (ACC/AHA 2025) y "SCA - Reperfusión y Revascularización". El paquete farmacológico se aplica EN PARALELO a la decisión de reperfusión, no después.

Paquete inmediato (los cuatro pilares + analgesia):
- AAS: carga 162-325 mg VO, masticada y sin cubierta entérica (la práctica habitual es 300 mg; salvo alergia o sangrado activo). Mantenimiento posterior 75-100 mg/día.
- SEGUNDO ANTIAGREGANTE (inhibidor P2Y12) — elígelo con cardiología según la estrategia, pero estas son las cargas:
  * Ticagrelor 180 mg VO (bucodispersable). Mantenimiento 90 mg/12 h. Es el de elección si NO hay estrategia invasiva planificada, y opción preferente (junto a prasugrel) si va a ICP.
  * Prasugrel 60 mg VO de carga. Mantenimiento 10 mg/día (5 mg/día si <60 kg o ≥75 años). Solo si se va a ICP y se conoce la anatomía. CONTRAINDICADO si ictus/AIT previo.
  * Clopidogrel: carga 300-600 mg VO (mantenimiento 75 mg/día). Es el P2Y12 de elección cuando se da FIBRINÓLISIS (STEMI fibrinolizado): 300 mg si ≤75 años; 75 mg sin carga si >75 años. También si prasugrel/ticagrelor no están disponibles, no se toleran o están contraindicados.
- ANTICOAGULACIÓN PARENTERAL (en todos los SCA, hasta la revascularización). Dosis del vault:
  * HNF (la más usada upstream y para soporte de ICP): carga 60 UI/kg IV (máx. 4000 UI) + perfusión 12 UI/kg/h (máx. 1000 UI/h), ajustada a aPTT 60-80 s. Para soporte de ICP sin anticoagulación previa, bolo 70-100 UI/kg para ACT 250-300 s.
  * Enoxaparina: 1 mg/kg SC c/12 h (1 mg/kg SC c/24 h si FG <30 ml/min). Es alternativa en el SCASEST sin estrategia invasiva precoz; preferida sobre HNF si el STEMI se fibriniliza (con bolo IV de 30 mg si <75 años; sin bolo y 0,75 mg/kg/12h si ≥75 años).
  * Fondaparinux: 2,5 mg SC c/24 h (contraindicado si FG <30). Alternativa en SCASEST. NO usar como anticoagulante único para soporte de ICP (trombosis de catéter): si el paciente va a cateterismo, se añade HNF.
- NITRATOS: si el dolor es isquémico y la PAS ≥90 mmHg, nitroglicerina sublingual 0,4 mg, repetible cada 5 min hasta 3 dosis. Si persiste el dolor / HTA / edema pulmonar: NTG IV en perfusión, inicio 10 µg/min, titulando. NO dar nitratos si PAS <90 mmHg, sospecha de infarto de ventrículo derecho, o toma de inhibidor PDE5 (sildenafilo/vardenafilo 24 h, tadalafilo 48 h, avanafilo 12 h).
- MORFINA: si el dolor no cede, 2-4 mg IV, repetible cada 5-15 min (hasta ~10 mg). Alternativa fentanilo 25-50 µg IV. Aviso: la morfina puede retrasar la absorción de los P2Y12 orales.
- ESTATINA de alta intensidad cuanto antes (atorvastatina 80 mg o rosuvastatina 20-40 mg).
- NO: AINE distintos del AAS (aumentan MACE); prasugrel si ictus/AIT previo; oxígeno si SpO2 ≥90%; betabloqueante IV de rutina antes de la reperfusión.

Reperfusión — la diferencia clave SCACEST vs SCASEST:
- SCACEST (elevación persistente del ST o equivalente, incluido BRI nuevo con clínica): es Código Infarto. El objetivo es ABRIR EL VASO ya.
  * ICP primaria si el tiempo previsto desde el primer contacto médico hasta abrir el vaso es ≤120 min (objetivo device ≤90 min si acude directo, ≤120 si hay traslado). Avisa a Hemodinámica.
  * Si NO se puede hacer ICP en ≤120 min → FIBRINÓLISIS sistémica (door-to-needle ≤30 min) salvo contraindicación, y traslado para coronariografía 2-24 h (estrategia farmacoinvasiva) o ICP de rescate si no reperfunde. Fibrinolítico de elección: tenecteplasa (TNK) en bolo IV único ajustado a peso (<60 kg 30 mg; 60-69 kg 35 mg; 70-79 kg 40 mg; 80-89 kg 45 mg; ≥90 kg 50 mg; mitad de dosis si ≥75 años). Contraindicación absoluta clave: sospecha de disección aórtica, hemorragia intracraneal previa, ictus isquémico <3 meses, sangrado activo, HTA no controlable >180/110.
- SCASEST (sin elevación persistente del ST): NO se fibriniliza nunca (la fibrinólisis es dañina). Se estabiliza con el paquete farmacológico y se hace coronariografía según riesgo: muy alto riesgo (inestabilidad, IC/shock, arritmia maligna, dolor refractario) <2 h; alto riesgo (GRACE >140, troponina dinámica, cambios ST/T) <24 h; intermedio <72 h; bajo riesgo, estrategia selectiva.
- En ambos: avisa a la Unidad Coronaria. La elección fina del P2Y12 y del anticoagulante la consensúas con cardiología, pero AAS + anticoagulación + estatina + analgesia los inicias tú.

B. SOSPECHA DE SÍNDROME AÓRTICO AGUDO (DISECCIÓN)
Fuente: nota del vault "Síndrome Aórtico Agudo y Enfermedad Aórtica" (ESC 2024 + Manual 12).
- NO des antiagregantes ni anticoagulantes ni fibrinólisis (aunque el ECG parezca un SCA).
- El BETABLOQUEANTE IV va SIEMPRE PRIMERO (control de frecuencia antes que de tensión, para no propagar el flap con la taquicardia refleja). Objetivos: FC <60 lpm, PAS 100-120 mmHg (TAM <80 mmHg), vigilando perfusión distal y diuresis.
  * Labetalol (1.ª elección): bolo 50 mg IV en 1 min, repetible a los 5 min, hasta máx. 200 mg. Perfusión: 250 mg en 250 ml SSF, inicio 1 mg/min (60 ml/h), máx. 600 ml/h.
  * Esmolol (2.ª elección; contraindicado en IC y bradicardia): bolo 80 mg IV en 1 min; perfusión 2,5 g/250 ml, inicio 50 µg/kg/min, máx. 300 µg/kg/min. Útil por su vida media ultracorta.
- Si tras el betabloqueo la TA sigue alta, AÑADE un vasodilatador (nunca en solitario): nitroprusiato 0,5-10 µg/kg/min, o urapidilo. Si el betabloqueante está contraindicado, diltiazem (bolo 0,25 mg/kg en 2 min; perfusión 10 ml/h, máx. 15 mg/h).
- Si HIPOTENSIÓN/shock (sospecha de rotura, taponamiento o IAo aguda): noradrenalina en perfusión (16 mg en 250 ml SG5% a 10 ml/h; 0,1-1 µg/kg/min) + ETT urgente. Cruza y reserva hemoderivados.
- ANALGESIA: cloruro mórfico 3-5 mg IV cada 30 min hasta control del dolor (el dolor dispara la TA y la FC). Lorazepam 1 mg VO si ansiedad.
- DESTINO: todos a UCI. Tipo A (afecta aorta ascendente) → cirugía cardiovascular urgente/emergente. Tipo B no complicada → tratamiento médico. Avisa a cirugía cardiovascular / UCI ya.

C. SOSPECHA DE TEP DE ALTO RIESGO / ALTA SOSPECHA
Fuente: nota del vault "TEP - Tromboembolismo Pulmonar" (AHA/ACC 2026 + Manual 12).
- Oxígeno (objetivo SaO2 >90%), analgesia, y fluidoterapia CAUTELOSA (evita la sobrecarga del VD: bolos pequeños, 250 ml, y reevalúa; el VD dilatado tolera mal el volumen).
- ANTICOAGULACIÓN sin esperar a la imagen si la sospecha es alta y no hay contraindicación:
  * Enoxaparina 1 mg/kg/12 h SC (o 1,5 mg/kg/24 h SC); reduce a 1 mg/kg/24 h si FG <30 ml/min. Es la de elección en el TEP estable.
  * HNF IV (bolo 80 UI/kg + perfusión 18 UI/kg/h, ajustada a aPTT) si hay inestabilidad extrema, fallo renal grave, o se prevé fibrinólisis/procedimiento inminente (es reversible y de vida media corta).
- TEP DE ALTO RIESGO (hipotensión persistente PAS <90 o shock — categoría E): activa el PERT (Pulmonary Embolism Response Team) si existe y valora terapia de reperfusión con UCI:
  * FIBRINÓLISIS SISTÉMICA: alteplasa 100 mg IV en 2 h (o régimen acelerado 0,6 mg/kg en 15 min, máx. 50 mg, en parada inminente). Es el tratamiento de elección del TEP de alto riesgo si no hay contraindicación hemorrágica mayor.
  * Si la fibrinólisis está contraindicada o fracasa: trombólisis dirigida por catéter, trombectomía mecánica percutánea o embolectomía quirúrgica.
- Avisa al adjunto/UCI. En el TEP inestable la prueba inicial es el ETT (sobrecarga de VD; además excluye taponamiento).

D. SOSPECHA DE PERICARDITIS
Fuente: nota del vault "Pericarditis Aguda" (ESC 2025 + Manual 12).
- AINE a dosis de ataque + colchicina desde el primer día (la colchicina reduce drásticamente las recurrencias):
  * Ibuprofeno 600 mg/8 h VO (1-2 semanas, luego descenso lento según PCR y clínica). En pacientes isquémicos, AAS 750-1000 mg/6-8 h en lugar del ibuprofeno.
  * Colchicina 0,5 mg/24 h (<70 kg) o 0,5 mg/12 h (>70 kg), durante 3-6 meses.
- Reposo relativo hasta resolución clínica y normalización de PCR.
- Corticoides (prednisona 0,25-0,5 mg/kg/día) solo de 2.ª línea (contraindicación a AINE, fracaso o embarazo): aumentan el riesgo de recurrencia.
- Protege el estómago con IBP si das AINE a dosis altas. Ingreso si criterios de mal pronóstico (fiebre >38, derrame grande >20 mm, taponamiento, miopericarditis, inmunodepresión, anticoagulación, falta de respuesta a 1 semana).

E. SOSPECHA DE TAPONAMIENTO CARDÍACO
Fuente: nota del vault "Taponamiento Cardíaco" (ESC 2025 + Manual 12).
- Es una emergencia de procedimiento: el tratamiento curativo es EVACUAR el líquido. PERICARDIOCENTESIS urgente guiada por ETT/fluoroscopia (o ventana pericárdica quirúrgica si es por disección tipo A, trauma grave o rotura miocárdica). Avisa ya a cardiología/UCI/cirugía.
- Mientras llega el drenaje, MANTÉN EL RETORNO VENOSO: expansión agresiva de volumen con cristaloides y drogas vasoactivas (inotrópicos) si hacen falta.
- NUNCA des diuréticos ni vasodilatadores (estrictamente contraindicados): el llenado depende de presiones venosas altas; los bajarías y provocarías parada.

F. SOSPECHA DE NEUMOTÓRAX A TENSIÓN
[HUECO EN VAULT: no hay nota específica; dosis/técnica por conocimiento clínico estándar.]
- Es un diagnóstico CLÍNICO (disnea extrema, hipotensión, hipofonesis unilateral con timpanismo, desviación traqueal contralateral, ingurgitación yugular). NO esperes a la radiografía.
- DESCOMPRESIÓN INMEDIATA con aguja: angiocatéter grueso (14G), en el 2.º espacio intercostal línea medioclavicular (borde superior de la 3.ª costilla) o, alternativa con mejor llegada en adultos, 4.º-5.º espacio intercostal línea axilar anterior/media. Saldrá aire a presión: has convertido el neumotórax a tensión en uno abierto, ganando tiempo.
- A continuación, DRENAJE TORÁCICO definitivo (tubo de tórax) en el triángulo de seguridad. Avisa a cirugía/neumología.

G. SOSPECHA DE ROTURA ESOFÁGICA (SÍNDROME DE BOERHAAVE)
[HUECO EN VAULT: solo se menciona de pasada (signo de Hamman) en "Dolor Torácico - Perfiles Clínicos"; manejo por conocimiento clínico estándar.]
- Sospéchala ante dolor torácico/epigástrico intenso tras vómitos violentos o instrumentación esofágica, con enfisema subcutáneo cervical, signo de Hamman (crepitación con el latido) y derrame pleural izquierdo / neumomediastino en la imagen. La tríada de Mackler (vómitos + dolor torácico + enfisema subcutáneo) está presente en una minoría.
- Es una emergencia quirúrgica con alta mortalidad. Mientras avisas a Cirugía (torácica/general):
  * DIETA ABSOLUTA. Nada por boca.
  * FLUIDOTERAPIA agresiva (suelen estar sépticos/hipovolémicos) y analgesia IV.
  * ANTIBIÓTICOS de amplio espectro precoces (cubrir flora orofaríngea y digestiva, incluidos anaerobios y Candida): piperacilina-tazobactam 4/0,5 g IV/6-8 h, o meropenem 1 g IV/8 h, con antifúngico (fluconazol/equinocandina) por la mediastinitis.
  * IBP IV (omeprazol/pantoprazol) para reducir la agresión ácida.
  * Confirmación con TC torácica con contraste hidrosoluble (esofagograma con gastrografín) — NUNCA bario si sospechas perforación.
  * El tratamiento definitivo (reparación quirúrgica, drenaje, prótesis endoscópica) lo decide cirugía; cuanto antes (<24 h), mejor pronóstico.


6- PERLAS PARA NO OLVIDAR

🔑 ECG en <10 min en todo dolor torácico, y compáralo SIEMPRE con electros previos. Un cambio nuevo (incluido un BRI) en clínica isquémica es para avisar a la Unidad Coronaria y activar Código Infarto.

🔑 Un ECG normal y una troponina precoz normal NO descartan el SCA. Seria la troponina (delta 0/1 h) y repite el ECG. El 5% de los infartos se va de alta etiquetado de "no isquémico".

🔑 En el SCA, el paquete inmediato es AAS 300 mg masticada + segundo antiagregante (ticagrelor 180 mg / prasugrel 60 mg si ICP / clopidogrel si fibrinólisis o no disponibles) + anticoagulación (HNF 60 UI/kg máx 4000 + 12 UI/kg/h, o enoxaparina 1 mg/kg/12h) + estatina alta intensidad. La diferencia clave: SCACEST se REPERFUNDE ya (ICP <120 min o fibrinólisis); SCASEST NUNCA se fibriniliza.

🔑 Cuidado con el perfil atípico: mujer, anciano y diabético pueden infartar sin dolor típico (equivalentes anginosos). Umbral bajo.

🔑 Dolor desgarrador, migratorio a la espalda, o asimetría de pulsos/TA entre brazos = síndrome aórtico. NO anticoagules ni antiagregues ni fibrinolices. BETABLOQUEANTE IV PRIMERO (labetalol 50 mg IV en 1 min, repetible, máx 200; objetivo FC <60 y PAS 100-120) y angio-TC de aorta. En la disección, el control es de FRECUENCIA antes que de tensión, para no propagar el flap con la taquicardia refleja.

🔑 Disnea súbita + dolor pleurítico + signos de TVP = TEP. Estima la probabilidad (Wells/Geneva) antes del dímero-D; en alta probabilidad, angio-TC directa. Anticoagula ya (enoxaparina 1 mg/kg/12h) si la sospecha es alta y no hay contraindicación. Si hay shock (alto riesgo), fibrinólisis sistémica (alteplasa 100 mg en 2 h) con UCI/PERT.

🔑 Tríada de Beck (yugulares ingurgitadas + hipotensión + tonos apagados) + pulso paradójico = taponamiento. Es procedimiento (pericardiocentesis), no fármaco: volumen y avisa ya. NUNCA diuréticos ni vasodilatadores.

🔑 Neumotórax a tensión = diagnóstico clínico, descompresión inmediata con aguja (14G, 2.º EIC medioclavicular o 5.º EIC axilar anterior) ANTES de la radiografía. Luego tubo de tórax.

🔑 Vómitos violentos + dolor torácico + enfisema subcutáneo (Hamman) = sospecha rotura esofágica (Boerhaave). Dieta absoluta, antibióticos de amplio espectro + antifúngico, IBP y cirugía urgente. Esofagograma con gastrografín, nunca bario.

🔑 No uses oxígeno de rutina si la SpO2 es normal: en el SCA el oxígeno innecesario puede ser perjudicial.

🔑 La analgesia NO enmascara el diagnóstico. Trata el dolor desde el principio (y en la disección, además, baja la TA y la FC que el propio dolor dispara).
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
1) Prioriza guías EUROPEAS (ESC) y ESPAÑOLAS (SEC, SEMES, GEMA, GALAXIA, SEPAR, SEN, SSC) cuando existan; usa AHA/ACC/GINA/GOLD como complemento y AVISA cuando la recomendación europea/española difiera de la americana (dosis, umbrales o fármacos).
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
3) El estilo es texto plano conciso de bolsillo, sin frontmatter ni referencias dentro de la guía: no lo marques como defecto. Esta guía SÍ detalla el tratamiento concreto (fármaco, dosis, vía e intervalo) por diagnóstico; revisa esas dosis y pautas a fondo, que es lo que más importa.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

SÍNCOPE

El síncope es una pérdida transitoria del conocimiento por hipoperfusión cerebral, de inicio brusco, duración corta y recuperación espontánea, completa y precoz. En guardia el síncope no es un cuadro que "se trate con un fármaco": es ante todo un TRIAJE de riesgo. Tu trabajo en los primeros minutos no es etiquetar el mecanismo exacto, sino separar al paciente que se va de alta tranquilo del que esconde una causa cardíaca (arritmia, isquemia, estenosis aórtica, TEP) que puede matarlo en los próximos días. La herramienta que más rinde no es ningún fármaco: son el ECG de 12 derivaciones y una historia clínica dirigida. Dicho esto, hay escenarios concretos —bradicardia o taquiarritmia sintomática, hipovolemia— en los que SÍ tienes que actuar con un fármaco y una dosis, y para eso es esta guía.


1- CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR
Toma constantes completas y haz un ECG de 12 derivaciones cuanto antes. Mirada rápida de 10 segundos — avisa, y no des de alta por tu cuenta, si detectas cualquiera de estos:
- Síncope durante el ESFUERZO, o estando en DECÚBITO o sentado (orienta a causa cardíaca, no a vasovagal).
- Palpitaciones de aparición rápida justo ANTES de perder el conocimiento.
- Síncope brusco, SIN pródromos, que ha provocado un traumatismo importante (cara, occipucio, fractura).
- Cardiopatía estructural conocida, FEVI baja, insuficiencia cardíaca o infarto previo.
- Dolor torácico, disnea, cefalea brusca o dolor abdominal acompañando al episodio.
- PAS <90 mmHg sin causa clara, o sospecha de sangrado digestivo (hazle un tacto rectal).
- Soplo sistólico no estudiado (sospecha de estenosis aórtica o miocardiopatía hipertrófica).
- Bradicardia mantenida <40 lpm en vigilia, o el paciente sigue bradicárdico/hipotenso al llegar (síncope que NO ha recuperado del todo el ritmo o la TA → puede ser una arritmia en curso).
- ECG patológico: isquemia aguda, BAV de 2.º grado Mobitz II o de 3.er grado, FA lenta <40 lpm, pausas sinusales >3 s en vigilia, TV sostenida o no sostenida, patrón de Brugada tipo 1 (elevación ST en V1-V3), QTc >460 ms, QRS preexcitado (preexcitación) o disfunción de marcapasos/DAI.
- 🔑 Compara SIEMPRE con electros previos: si la alteración del ECG es NUEVA, avisa.

Regla de oro: ante sospecha de causa potencialmente mortal NO te pongas a puntuar escalas para decidir tú el destino; sospecha, monitoriza y avisa. La estratificación fina y la decisión de ingreso las cierra el adjunto. Si el paciente llegó bien y "ahora no está bien" (bradicárdico, hipotenso, con dolor torácico), no esperes a la prueba que lo confirme.


2- QUÉ PREGUNTAR (anamnesis dirigida, <3 minutos)

1. POSICIÓN Y DESENCADENANTE
- Bipedestación prolongada, calor, lugar abarrotado, dolor, miedo, visión de sangre, o durante la micción, la defecación, la tos o la deglución → REFLEJO (vasovagal o situacional).
- Al incorporarse desde tumbado o sentado (cambio postural reciente, <5 min) → ORTOSTÁTICO.
- Al rotar la cabeza, afeitarse o con el cuello apretado → síndrome del seno carotídeo.
- Durante el ESFUERZO o estando TUMBADO → CARDÍACO (bandera roja).

2. PRÓDROMOS
- Sudoración, náuseas, calor, visión borrosa o acúfenos antes de caer → reflejo.
- AUSENCIA de pródromos, o palpitaciones rápidas previas → cardíaco.

3. RECUPERACIÓN
- Rápida y completa (típica del síncope, sea reflejo o cardíaco) vs. confusión que dura más de 5 min (orienta a crisis epiléptica, NO a síncope).

4. DATOS QUE SUGIEREN CRISIS Y NO SÍNCOPE
- Mordedura LATERAL de la lengua, movimientos tónico-clónicos prolongados, desviación de la cabeza o los ojos, automatismos, aura previa.
- (Las mioclonías breves tras la caída SÍ son frecuentes en el síncope; no las confundas con una crisis.)

5. MEDICACIÓN Y ANTECEDENTES
- Antihipertensivos, diuréticos, vasodilatadores (nitratos), fármacos que alargan el QT, antidepresivos, neurolépticos, dopaminérgicos, frenadores del nodo AV (betabloqueantes, verapamilo, diltiazem, digoxina). Revisa la receta electrónica: la polifarmacia cardiovascular es la causa más frecuente de síncope en el anciano.
- Anticoagulantes/antiagregantes (si traumatismo craneal → riesgo de hemorragia).
- Antecedente familiar de MUERTE SÚBITA precoz (canalopatía, miocardiopatía).
- Sospecha de pérdidas (vómitos, diarrea, melenas, sangrado) → hipovolemia.


3- QUÉ EXPLORAR (exploración dirigida, <2 minutos)
Recuerda: una exploración normal NO descarta una causa cardíaca grave.

CONSTANTES Y ORTOSTATISMO
- Constantes completas (TA, FC, SatO₂, Tª) y glucemia capilar.
- TA y FC en decúbito supino y de nuevo a los 3 min de bipedestación activa. Hipotensión ortostática: caída de la PAS ≥20 mmHg, de la PAD ≥10 mmHg, o PAS <90 mmHg, que reproduzca los síntomas.
- Si la FC en bipedestación sube >30 lpm (o >120 lpm) sin caída de TA → orienta a STPO (síndrome de taquicardia postural), no a síncope cardíaco.

AUSCULTACIÓN CARDÍACA
- Soplo sistólico eyectivo en foco aórtico irradiado a carótidas (estenosis aórtica) o soplo que aumenta con Valsalva (miocardiopatía hipertrófica obstructiva).
- Ritmo: arritmia, bradicardia o taquicardia mantenidas.

NEUROLÓGICO
- Exploración básica buscando focalidad. Si HAY focalidad persistente al recuperar la consciencia → NO es un síncope simple: piensa en ictus/AIT vertebrobasilar o HSA y reorienta (ver MUST - Déficit Neurológico).

DIRIGIDA
- Tacto rectal si sospechas sangrado digestivo como causa de hipotensión (anciano con síncope + PAS baja sin causa clara).
- TA en ambos brazos si sospecha de robo de la subclavia o disección (diferencia ≥20 mmHg).
- Signos de hipovolemia: sequedad de mucosas, pliegue cutáneo, relleno capilar lento.


4- QUÉ PRUEBAS PEDIR

INMEDIATAS
- ECG de 12 derivaciones SIEMPRE, en TODO síncope (Clase I, es obligatorio y es lo que más rinde). Tira de ritmo larga. Busca: isquemia, BAV, QTc, Brugada, hipertrofia/ondas Q, preexcitación, pausas, FC.
- Glucemia capilar (descartar hipoglucemia como causa de la pérdida de conocimiento).
- Monitorización ECG continua / telemetría desde la llegada en todo paciente de alto riesgo (Clase I).

ANALÍTICA (orientada, no "de rutina")
- Hemograma: anemia o anemización por sangrado (un hematocrito <30% es criterio de alto riesgo).
- Iones y función renal: alteraciones hidroelectrolíticas (causa de arritmia y de hipotensión).
- Test de embarazo (β-hCG) en mujer en edad fértil (ectópico sangrante como causa de hipovolemia/síncope).
- Troponina, dímero-D o radiografía de tórax SOLO si la clínica lo orienta (dolor torácico, disnea, sospecha de SCA o de TEP). Pedidos de rutina rinden poco y NO ayudan a estratificar (ESC 2018).
- NO pidas en la primera valoración de puerta: masaje del seno carotídeo, mesa basculante (tilt-test) ni Holter. Son del estudio diferido, no de la guardia.

Escalas de probabilidad clínica
- Características de ALTO riesgo (ESC 2018, Tabla 6):
  MAYORES (alto riesgo aunque no haya cardiopatía estructural): nueva aparición de dolor torácico, disnea, dolor abdominal o cefalea con el episodio; síncope de esfuerzo o en decúbito; palpitaciones rápidas seguidas de síncope; PAS <90 sin causa; sospecha de sangrado digestivo; bradicardia <40 lpm en vigilia; soplo sistólico no estudiado; y los criterios ECG diagnósticos (isquemia aguda, BAV Mobitz II / 3.er grado, FA o bradicardia <40 lpm, pausa >3 s, TV, disfunción de marcapasos/DAI, Brugada tipo 1, QTc >460 ms).
  MENORES (alto riesgo SOLO si se asocian a cardiopatía o ECG anormal): síncope sin pródromos o pródromos <10 s, historia familiar de muerte súbita precoz, síncope en sedestación, BAV 1.er grado / Mobitz I, bradicardia sinusal leve (40-50 lpm), TSV/FA paroxística, QRS preexcitado, QTc corto, patrones de Brugada atípicos, ondas T negativas en precordiales derechas / ondas épsilon.
- Características de BAJO riesgo (ESC 2018): pródromos típicos vegetativos (calor, sudoración, náuseas), desencadenante claro (calor, dolor, bipedestación, micción/tos/defecación), síncope al levantarse, historia larga de síncopes recurrentes similares, ausencia de cardiopatía y ECG NORMAL.
- Canadian Syncope Risk Score (CSRS): combina datos clínicos, ECG y troponina para estimar el riesgo de evento adverso grave a 30 días (de muy bajo a muy alto). Orienta el destino, pero la decisión la cierra el adjunto. (ESC 2018 desaconseja usar escalas de forma AISLADA —San Francisco, OESIL, EGSYS— porque rinden peor que el juicio clínico; úsalas como apoyo, no como única herramienta.)

⚠ TRAMPAS COMUNES
- Una exploración y un ECG normales NO descartan una causa cardíaca grave si la historia es de alto riesgo (esfuerzo, decúbito, palpitaciones, sin pródromos).
- "Mejora del todo" no significa banal: el síncope cardíaco también recupera rápido y completo. La recuperación rápida NO es tranquilizadora por sí sola.
- No etiquetes de "vasovagal" un síncope de esfuerzo, en decúbito o precedido de palpitaciones. Eso es CARDÍACO hasta que se demuestre lo contrario.
- La troponina y el dímero-D de rutina NO estratifican el síncope: pídelos solo si la clínica los orienta. Una troponina mínimamente elevada en un anciano no convierte un vasovagal claro en un SCA.
- Confusión postcrítica >5 min, mordedura LATERAL de la lengua o clonías prolongadas orientan a crisis, NO a síncope.
- Un ECG de 12 derivaciones puntual normal NO descarta una arritmia paroxística: si la sospecha es alta, lo que detecta la arritmia es la telemetría/monitorización, no un electro aislado.
- En el anciano con síncope e hipotensión sin causa clara, la "lipotimia banal" puede ser un sangrado digestivo o un TEP. Umbral bajo para avisar.


5- MEDIDAS Y TRATAMIENTO SEGÚN SOSPECHA

MEDIDAS GENERALES DE SOPORTE
- La MAYORÍA de los síncopes (reflejo, situacional, ortostático banal) NO necesitan ningún fármaco: el tratamiento de la guardia es postural y de soporte, y el resto es triaje de destino.
- ABC. Tumba al paciente en decúbito con las piernas elevadas (posición de Trendelenburg/anti-shock). Esto por sí solo aborta la mayoría de los reflejos.
- Monitorización continua (TA, FC, SatO₂) y ECG/telemetría si hay cualquier dato de riesgo.
- Coge VÍA venosa periférica y extrae la analítica orientada. Repite la TA.
- Glucemia capilar; si hipoglucemia, corrígela (glucosa IV) y reevalúa.
- O₂ solo si SatO₂ baja o sospecha de causa cardiopulmonar.
- NO des betabloqueantes ni vasodilatadores de entrada (empeoran la hipotensión/bradicardia).
- NO uses midodrina ni fludrocortisona en la guardia: son tratamiento CRÓNICO del síncope reflejo y de la hipotensión ortostática, se pautan en consulta. (Dosis crónicas, solo de referencia: midodrina 2,5-10 mg/8 h; fludrocortisona 0,1-0,3 mg/día. NO las inicies tú en urgencias, y NO uses fludrocortisona si HTA o insuficiencia cardíaca.)

A. SÍNCOPE REFLEJO (VASOVAGAL) / SITUACIONAL
- Lo de la guardia es POSTURAL y educativo. Decúbito con piernas elevadas y tranquilizar; reasegurar sobre su naturaleza benigna.
- MANIOBRAS DE CONTRAPRESIÓN FÍSICA para abortar el pródromo en episodios recurrentes: entrecruzar las piernas o entrelazar las manos y tensar los brazos (más eficaces en <60 años con pródromos reconocibles).
- EDUCACIÓN al alta: reconocer pródromos para sentarse/tumbarse a tiempo, evitar desencadenantes (deshidratación, calor, lugares abarrotados, bipedestación prolongada), aumentar ingesta de líquidos y sal, micción sentado si síncope miccional.
- NO betabloqueantes (Clase III en síncope reflejo: sin eficacia demostrada y agravan la bradicardia en el seno carotídeo).
- El tratamiento farmacológico/marcapasos del reflejo es del ámbito CRÓNICO especializado, no de la guardia.

B. SÍNCOPE ORTOSTÁTICO / HIPOVOLEMIA
- Si está deshidratado, sangrante o hipotenso: SUEROTERAPIA con cristaloides. Suero salino fisiológico 0,9% IV o Ringer Lactato; bolo de 250-500 mL y reevaluar respuesta (TA, FC, diuresis). Repetir según respuesta.
- Si hay sangrado activo o anemización significativa → segunda vía de grueso calibre, cruzar y reservar, y manejar como hemorragia (ver MUST correspondiente / avisar). El tacto rectal puede objetivar la melena.
- REVISA Y AJUSTA los fármacos hipotensores responsables (antihipertensivos, diuréticos, nitratos, antidepresivos, neurolépticos, dopaminérgicos): la retirada/reducción es la medida más eficaz en el anciano. Esto se consensúa, pero puedes suspender en urgencias el fármaco claramente implicado.
- Medidas posturales: levantarse despacio (decúbito → sedestación 2-3 min → bipedestación), cabecero elevado, medias de compresión (todo ello CRÓNICO, para el informe de alta).
- NO inicies midodrina ni fludrocortisona en la guardia (tratamiento crónico de la HO; además, fludrocortisona contraindicada si HTA o IC).

C. BRADICARDIA SINTOMÁTICA CON COMPROMISO HEMODINÁMICO
Aplica si el síncope se debe a una bradiarritmia y el paciente sigue bradicárdico e inestable (PAS <90, mala perfusión, bajo nivel de consciencia, dolor torácico isquémico, IC aguda). Monitoriza, vía, O₂. Avisa a cardiología/intensivos en paralelo.
- 1.ª LÍNEA — ATROPINA: 0,5-1 mg IV en bolo rápido, repetible cada 3-5 min hasta un MÁXIMO de 3 mg. NUNCA por debajo de 0,5 mg (dosis menores pueden producir bradicardia paradójica). Funciona mejor en bloqueos suprahisianos (BAV nodal, bradicardia sinusal); responde mal en BAV infrahisiano (Mobitz II / 3.er grado con QRS ancho). [Discrepancia de dosis del vault: el vault Arritmias da 1 mg IV repetible hasta 3 mg como recomendación actual AHA/ERC, frente a 0,5 mg de la pauta clásica del Manual 12 Octubre. En la práctica de guardia se empieza con 0,5-1 mg y se titula hasta 3 mg.]
- 2.ª LÍNEA, si NO responde a atropina o el bloqueo es infrahisiano:
  * MARCAPASOS TRANSCUTÁNEO (parches): inícialo de inmediato. Pon la frecuencia objetivo (p. ej. 60-80 lpm) y sube la salida (mA) hasta CONSEGUIR CAPTURA (espiga seguida de QRS ancho) y pulso palpable que se corresponda. Sedoanalgesia para tolerarlo (la captura es dolorosa): p. ej. midazolam ± fentanilo/cloruro mórfico a dosis bajas tituladas, vigilando que no agraven la hipotensión.
  * Y/O PERFUSIÓN CRONOTRÓPICA mientras llega el marcapasos o si este no captura:
    - Isoproterenol (isoprenalina): 1 mg en 250 mL de SSF; iniciar la perfusión y titular al alza por efecto (frecuencia y TA). [El vault da la dilución 1 mg/250 mL pero NO fija el ritmo de inicio en µg/min; pauta estándar de referencia: comenzar a 2-10 µg/min y ajustar. HUECO del vault en el ritmo concreto.]
    - Dopamina: 2-10 µg/kg/min IV en perfusión, titulando por respuesta. DE ELECCIÓN si se sospecha isquemia miocárdica como causa de la bradicardia.
    - (Adrenalina 2-10 µg/min es alternativa de rescate si bradicardia con shock refractaria, según ACLS; el vault no la recoge para bradicardia — CONOCIMIENTO CLÍNICO.)
- PASO FINAL: marcapasos transvenoso transitorio, colocado por cardiología/intensivos. Busca y corrige causas reversibles: isquemia (sobre todo IAM inferior → puede precisar revascularización), intoxicación por frenadores del nodo (betabloqueantes, calcioantagonistas, digoxina) y alteraciones iónicas (hiperpotasemia).

D. TAQUIARRITMIA SINTOMÁTICA
Aplica si el síncope se debe a una taquiarritmia. La primera decisión es la ESTABILIDAD hemodinámica. Monitoriza, vía, O₂; avisa.
- PACIENTE INESTABLE (síncope + hipotensión/shock, IC aguda, dolor torácico isquémico, deterioro de consciencia con la taquicardia) → CARDIOVERSIÓN ELÉCTRICA SINCRONIZADA urgente, con sedación previa (propofol 0,5-1 mg/kg IV, o midazolam + etomidato):
  * Energías sincronizadas: 50-100 J en arritmias organizadas (flutter, TV monomorfa); 150-200 J en FA. (Recomendación práctica Manual 12 Octubre; ajusta a tu desfibrilador y protocolo local.)
  * Si TV SIN PULSO o FV → desfibrilación ASINCRÓNICA a máxima energía (360 J monofásico / la máxima de tu equipo bifásico) + RCP (algoritmo de parada).
  * Si TV POLIMORFA → desfibrilación asincrónica a máxima energía.
- PACIENTE ESTABLE → orientación según el QRS (la pauta fina la decide cardiología; ver detalle en el vault Arritmias):
  * QRS ESTRECHO (TSV): maniobras vagales (Valsalva) → adenosina 6 mg IV en bolo rápido, luego 12 mg (repetible una vez; algunos protocolos AHA dan un 3.er bolo de 18 mg, que el Manual 12 Octubre evita). Contraindicada la adenosina si preexcitación o broncoespasmo grave. Flutter/FA: control de frecuencia con frenadores del nodo.
  * QRS ANCHO = TV hasta que se demuestre lo contrario. En TV monomorfa estable, cardioversión farmacológica: procainamida (p. ej. 10 mg/kg a 20-50 mg/min, máx 1 g) o amiodarona (carga 5 mg/kg IV en 20 min-2 h, seguida de perfusión 900-1200 mg/24 h; la dosis fija de 300 mg es del algoritmo de PARADA, no de la TV estable) o lidocaína 1-1,5 mg/kg. NO uses frenadores del nodo si dudas entre TV y TSV con aberrancia.
  * TORSADES DE POINTES (QT largo): sulfato de magnesio 1-2 g IV en 10 min + corregir desencadenantes (hipopotasemia, fármacos que alargan el QT). Retira el fármaco causal.
- Tras estabilizar, telemetría e ingreso a cargo de cardiología; el tratamiento definitivo (ablación, DAI, ajuste antiarrítmico) lo decide cardiología.

E. SOSPECHA DE CAUSA CARDÍACA ESTRUCTURAL / ELÉCTRICA DE ALTO RIESGO (sin arritmia activa que tratar)
Paciente con síncope de esfuerzo, soplo de estenosis aórtica o miocardiopatía hipertrófica, FEVI baja, cardiopatía isquémica conocida, Brugada o QT largo, etc., pero que llega estable y en ritmo.
- En la PUERTA no hay un fármaco que dar: lo que toca es MONITORIZAR con telemetría, SOPORTE y AVISAR a cardiología, porque el riesgo es de muerte súbita por arritmia.
- En estenosis aórtica grave sintomática evita vasodilatadores y depleción de volumen (precipitan colapso); maneja la hipotensión con cautela. El tratamiento es la sustitución valvular (SAVR/TAVI), que decide cardiología.
- En sospecha de isquemia como sustrato (dolor torácico, ECG isquémico, troponina) → trata el SCA según protocolo y avisa (ver Dolor Torácico).
- El tratamiento específico —marcapasos, ablación, DAI, revascularización, cirugía valvular— lo decide cardiología. Tu papel es no dar de alta, monitorizar y coordinar.

DESTINO (lo afina el adjunto)
- ALTA desde urgencias: solo características de BAJO riesgo (pródromos típicos de reflejo/situacional + ECG normal + sin cardiopatía + recuperación completa). Instrucciones de medidas posturales y derivación a consulta si los episodios son recurrentes.
- OBSERVACIÓN / TELEMETRÍA en el SU (6-24 h): zona intermedia (ni claramente bajo ni claramente alto riesgo). Monitorización ECG continua. NO dar de alta directa.
- INGRESO: cualquier dato de ALTO riesgo (Tabla 6), causa grave identificada (arritmia documentada, isquemia, estenosis aórtica grave, TEP, hemorragia, disección), lesión por el síncope que requiera tratamiento, o necesidad de pruebas urgentes no ambulatorias (EEF, coronariografía, ecocardiograma urgente). El nivel (planta/telemetría/UCI) depende de la causa y la inestabilidad.


6- PERLAS PARA NO OLVIDAR

🔑 ECG en TODO síncope: es obligatorio (Clase I) y es lo que más rinde. Compáralo con electros previos; un cambio NUEVO es para avisar.

🔑 El síncope no se trata "con un fármaco": es un triaje de riesgo. La historia y el ECG separan al que se va de alta del que ingresa. Pero cuando hay bradicardia o taquiarritmia sintomática, SÍ hay fármaco y dosis: no te quedes solo en "que lo vea cardiología".

🔑 Síncope de esfuerzo, en decúbito o precedido de palpitaciones = cardíaco hasta que se demuestre lo contrario. Nunca lo etiquetes de vasovagal.

🔑 La recuperación rápida y completa NO descarta causa cardíaca. No te fíes de "ya está bien"; el síncope cardíaco también recupera rápido.

🔑 Bradicardia sintomática: atropina 0,5-1 mg IV, repetible cada 3-5 min hasta 3 mg, NUNCA por debajo de 0,5 mg (paradójicamente empeora la bradicardia). Si no responde o es infrahisiana (Mobitz II / 3.er grado): marcapasos transcutáneo con captura + perfusión de isoprenalina (1 mg/250 mL SSF) o dopamina (2-10 µg/kg/min, de elección si isquemia).

🔑 Taquiarritmia con síncope e inestabilidad = cardioversión eléctrica sincronizada YA (50-100 J organizada, 150-200 J en FA), con sedación previa (propofol 0,5-1 mg/kg). TV sin pulso o FV → desfibrilar a máxima energía + RCP.

🔑 No uses midodrina ni fludrocortisona en urgencias: son tratamiento crónico, se pautan en consulta. Y nada de betabloqueantes en el síncope reflejo (Clase III).

🔑 Diferencia síncope de crisis: confusión >5 min, mordedura LATERAL de la lengua o clonías prolongadas apuntan a crisis epiléptica. Si queda focalidad neurológica al recuperar la consciencia, piensa en ictus/HSA, no en síncope.

🔑 En el anciano con síncope e hipotensión sin causa clara, piensa en sangrado digestivo (hazle un tacto rectal) y en TEP. Y revisa SIEMPRE la medicación: la polifarmacia cardiovascular es la causa más frecuente de síncope ortostático en el anciano.
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
1) Prioriza guías EUROPEAS (ESC) y ESPAÑOLAS (SEC, SEMES, GEMA, GALAXIA, SEPAR, SEN, SSC) cuando existan; usa AHA/ACC/GINA/GOLD como complemento y AVISA cuando la recomendación europea/española difiera de la americana (dosis, umbrales o fármacos).
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
3) El estilo es texto plano conciso de bolsillo, sin frontmatter ni referencias dentro de la guía: no lo marques como defecto. Esta guía SÍ detalla el tratamiento concreto (fármaco, dosis, vía e intervalo) por diagnóstico; revisa esas dosis y pautas a fondo, que es lo que más importa.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

FIEBRE SIN FOCO

El febril agudo del adulto en la puerta. Tu objetivo en los primeros minutos no es etiquetar la causa exacta, sino detectar a tiempo la sepsis y la meningitis, buscar el foco con una anamnesis y exploración dirigidas, y decidir cuándo el antibiótico empírico no puede esperar. Una vez tengas la sospecha de foco, el antibiótico empírico es ESPECÍFICO: fármaco, dosis, vía y tiempo concretos. Esto no es el estudio de la fiebre de origen desconocido prolongada, ni el del niño. Regla mental: en la sepsis, cada hora de retraso del antibiótico adecuado aumenta la mortalidad; el antibiótico precoz y bien dirigido es la intervención que más vidas salva.


1- CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR
Toma constantes completas con SatO2, glucemia capilar y nivel de consciencia nada más entrar. Mirada rápida de 10 segundos — avisa si detectas cualquiera de estos:
- Criterios de sepsis o shock: qSOFA con 2 o más (FR ≥22, PAS ≤100, alteración mental), o hipotensión (PAS <90 o TAM <65), mala perfusión (piel moteada, relleno capilar >3 s, oliguria) o lactato elevado. Aquí no puntúas y decides tú: sospecha de sepsis = aviso.
- Signos meníngeos (rigidez de nuca, Kernig, Brudzinski) o cualquier alteración del nivel de consciencia.
- Petequias o púrpura: sospecha de meningococo (púrpura fulminante). El antibiótico va INMEDIATO, no esperes a la punción lumbar; avisa mientras lo preparas.
- Inmunodeprimido (VIH, quimioterapia, corticoides, esplenectomía, trasplante) o NEUTROPÉNICO FEBRIL: este paciente se descompensa rápido y la fiebre puede ser el único signo.
- Temperatura >40 °C, o hipotermia <36 °C (mal pronóstico, frecuente en ancianos, alcohólicos, urémicos e infección por bacilos gramnegativos).
- Embarazada con fiebre (Listeria, pielonefritis, corioamnionitis).
- Portador de prótesis, catéter venoso central o sonda con fiebre, y el ADVP (endocarditis, bacteriemia asociada a catéter).
- Lactato ≥4 mmol/l, PaO2/FiO2 <300, GCS <12, plaquetas <100.000, creatinina >2 mg/dl o bilirrubina >2 mg/dl no atribuibles a causa crónica: ya hay disfunción orgánica → criterio de aviso a UCI (Manual 12 de Octubre).

Regla de oro: la sospecha de sepsis o de meningitis ya es motivo de aviso; no te quedes solo con el paciente. Ninguna prueba de imagen (TC, eco, radiografía) ni la punción lumbar justifican retrasar el antibiótico empírico ni la dexametasona.


2- QUÉ PREGUNTAR (anamnesis dirigida, <3 minutos)
La meta es encontrar el foco y pesar la gravedad.

1. TIEMPO Y PATRÓN
- ¿Desde cuándo? ¿Brusca (neumonía lobar, pielonefritis) o gradual? ¿Es la primera vez? ¿Escalofríos con tiritona franca (orienta a bacteriemia)? ¿Fiebre que persiste >48 h pese a antibiótico de amplio espectro (sospecha de foco no controlado o candidemia)?

2. SÍNTOMAS LOCALIZADORES (repásalos uno a uno; cada uno cambia el antibiótico)
- Disuria, polaquiuria, dolor lumbar o en fosa renal (urinario).
- Tos, expectoración purulenta, disnea, dolor pleurítico (respiratorio).
- Dolor abdominal, vómitos, diarrea, dolor en hipocondrio derecho (digestivo/biliar).
- Cefalea intensa con rigidez, fotofobia o vómitos (meníngeo); confusión o focalidad (encefalitis).
- Exantema, celulitis, herida, úlcera por presión, dolor desproporcionado en una extremidad con crepitación (partes blandas / fascitis necrotizante).
- Dolor articular con impotencia funcional (artritis séptica).

3. EPIDEMIOLOGÍA
- Viajes recientes, contacto con enfermos, animales y mascotas (mordeduras), ambiente laboral, exposición a agua dulce/salada en heridas.

4. ESTADO INMUNE Y FACTORES DE RIESGO DE MULTIRRESISTENCIA
- VIH, quimioterapia, corticoides, esplenectomía, trasplante, neutropenia.
- Factores de riesgo de microorganismo MDR/BLEE: hospitalización reciente o prolongada, antibiótico de amplio espectro reciente, colonización o infección previa por MDR, portador de dispositivos, residencia sociosanitaria, exposición a quinolonas o cefalosporinas de 2ª-3ª generación.

5. FÁRMACOS Y DISPOSITIVOS
- Prótesis, sondas, catéteres, CVC, ADVP; y el último ciclo de antibiótico.
- ALERGIAS reales a betalactámicos (diferencia exantema leve de anafilaxia; condiciona toda la pauta).
- Función renal conocida y peso (condicionan dosis de vancomicina, aminoglucósidos y betalactámicos).


3- QUÉ EXPLORAR (exploración dirigida, <2 minutos)
Recuerda: una exploración normal NO descarta enfermedad grave.

CONSTANTES
- Completas con SatO2, glucemia y nivel de consciencia. Calcula qSOFA y NEWS2 mentalmente.

PIEL Y MUCOSAS
- Petequias o púrpura (busca activamente en tronco, conjuntivas y mucosas), celulitis, herida o úlcera por presión, puntos de venopunción, ectima gangrenosa (sospecha Pseudomonas), eritrodermia (shock tóxico estafilocócico/estreptocócico).

ORL
- Orofaringe, oídos, senos paranasales (foco de neumococo y de meningitis por contigüidad).

CARDIOPULMONAR
- Crepitantes o condensación (foco respiratorio); soplos nuevos (endocarditis si hay foco vascular, ADVP o prótesis).

ABDOMEN
- Dolor, defensa, Murphy (colecistitis) y puñopercusión renal bilateral (pielonefritis).

SIGNOS MENÍNGEOS
- Rigidez de nuca, Kernig y Brudzinski. Su ausencia NO descarta meningitis en el anciano o el inmunodeprimido.

DIRIGIDA
- Articulaciones (artritis séptica), exploración de partes blandas buscando dolor desproporcionado o crepitación, y según el caso tacto rectal y exploración genital/prostática.
- Revisa los puntos de inserción de cualquier catéter, sonda o prótesis.


4- QUÉ PRUEBAS PEDIR

- Analítica: hemograma, PCR y procalcitonina, función renal y hepática, iones y coagulación. La procalcitonina >2 ng/ml orienta a origen bacteriano, pero NO esperes a ella para tratar.
- Lactato: marcador de hipoperfusión y de pronóstico; >2 mmol/l es mal dato y ≥4 obliga a fluidos. Vuelve a medirlo si estaba elevado.
- Hemocultivos x2 ANTES del antibiótico, pero sin retrasarlo si hay shock.
- Sistemático de orina y urocultivo (en sondado: recambiar sonda antes de recoger la muestra si es posible).
- Radiografía de tórax.
- Gasometría con lactato.
- Según el foco: punción lumbar si sospechas meningitis. Pide TC craneal previo SOLO si hay focalidad neurológica, inmunodepresión, crisis o bajo nivel de consciencia (GCS <12); en los demás, punción directa. El TC y la propia punción NUNCA deben retrasar ni el antibiótico ni la dexametasona.
- Otros según sospecha: ecografía abdominal (colecistitis, vía biliar, hidronefrosis), TC abdominopélvico (foco intraabdominal), urocultivo + hemocultivos en prostatitis, aspirado/biopsia si partes blandas complicadas.

Escalas de probabilidad clínica
- qSOFA: FR ≥22, PAS ≤100, alteración mental (GCS <15). ≥2 orienta a mayor riesgo y mal pronóstico, pero su ausencia NO descarta sepsis (SSC 2026 ya no lo recomienda como cribado aislado).
- NEWS2 / SIRS: para cribar gravedad se prefiere NEWS2, NEWS o SIRS al qSOFA aislado por mayor sensibilidad (SSC 2026). NEWS2 ≥5 (o 3 puntos en un solo parámetro) = aviso. SIRS positivo con ≥2 de: Tª >38 o <36 °C, FC >90, FR >20 (o PaCO2 <32), leucocitos >12.000 o <4.000 o >10% cayados.
- Procalcitonina: >2 ng/ml orienta a origen bacteriano y guía la SUSPENSIÓN del antibiótico (descenso >70% a las 48-72 h), no su inicio.
- CURB-65 (si foco respiratorio / NAC): Confusión, Urea >44 mg/dl (BUN >19), FR ≥30, PAS <90 o PAD ≤60, edad ≥65. 0-1 ambulatorio; 2 valorar ingreso/observación; ≥3 ingreso (≥4-5 valorar UCI). Es la escala que decide dónde se trata la neumonía y, por tanto, qué pauta antibiótica.

⚠ TRAMPAS COMUNES
- Un lactato normal NO descarta sepsis; la hipotermia (<36 °C) es de mal pronóstico, no tranquiliza.
- La procalcitonina NO sirve para decidir iniciar el antibiótico: no esperes a ella.
- Ante petequias/púrpura, el antibiótico va INMEDIATO; no esperes a la PL ni al TC.
- El TC craneal y la punción lumbar NUNCA retrasan el antibiótico ni la dexametasona en la meningitis.
- El anciano y el inmunodeprimido pueden tener sepsis con febrícula o sin fiebre; fíate de las constantes y la perfusión, no del termómetro.
- En el sondado, un urocultivo positivo sin clínica NO es indicación de antibiótico (bacteriuria asintomática); pero si hay fiebre sin otro foco y sonda, sí trátalo como ITU y recambia la sonda.
- Ceftriaxona a dosis estándar (2 g/24 h) NO sirve para meningitis: la dosis meníngea es 2 g/12 h.
- "Cubrir de todo" no es gratis: la cobertura de MDR, anaerobios o antifúngicos solo si hay factores de riesgo (SSC 2026). El exceso selecciona resistencias.


5- MEDIDAS Y TRATAMIENTO SEGÚN SOSPECHA

MEDIDAS GENERALES DE SOPORTE
- Monitoriza, coge vía (dos vías de grueso calibre si shock) y extrae analítica con hemocultivos x2 y glucemia capilar. Oxígeno con objetivo de SatO2 94-98%.
- Antitérmico: paracetamol 1 g IV en 15 min o VO cada 6-8 h (máximo 4 g/día; 2-3 g/día en ancianos o hepatópatas). Alternativa: metamizol 2 g IV diluido en 100 ml de suero en perfusión lenta de 10-15 min (NUNCA en bolo, da hipotensión).
- PAQUETE DE SEPSIS DE LA PRIMERA HORA (si hay sepsis o shock, bundle ≤1 h):
  1. Medir LACTATO (repetir si >2 mmol/l).
  2. HEMOCULTIVOS x2 ANTES del antibiótico (sin retrasarlo si hay shock).
  3. ANTIBIÓTICO EMPÍRICO precoz (<1 h) dirigido al foco sospechado (ver subsecciones).
  4. CRISTALOIDES 30 ml/kg IV si hipotensión o lactato ≥4 mmol/l (en obesidad/IMC >30, calcular sobre peso ajustado o ideal — SSC 2026 Rec. 10).
  5. Si persiste la hipotensión tras los fluidos: NORADRENALINA 1ª línea (puede iniciarse por vía periférica de forma precoz; con el adjunto). Vasopresina 2ª línea.
- En posible sepsis sin shock y sin foco claro: evaluación rápida; si a las 3 h persiste la sospecha de infección, administrar antimicrobiano (SSC 2026).

A. SOSPECHA DE MENINGITIS (incluida meningitis con púrpura → meningococo)
Orden y tiempos: dexametasona JUSTO ANTES o junto a la primera dosis de antibiótico; antibiótico empírico en <1 h; ni el TC ni la PL lo retrasan.
- Dexametasona 0,15 mg/kg IV (~10 mg) cada 6 h durante 4 días, ANTES o concomitante al antibiótico, NUNCA después. Mantener solo si se confirma neumococo. [VAULT: Meningitis y Encefalitis]
- Ceftriaxona 2 g IV cada 12 h (DOSIS MENÍNGEA: 2 g/12 h o 4 g/24 h, NO 1-2 g/24 h). Alternativa: cefotaxima 2 g IV cada 4-6 h.
- Añade VANCOMICINA 15-20 mg/kg IV cada 8-12 h (carga 25-30 mg/kg si shock) si sospechas NEUMOCOCO RESISTENTE a cefalosporinas. Verifica con el adjunto.
- Añade AMPICILINA 2 g IV cada 4 h si >50 años, embarazada o inmunodeprimido (cobertura de Listeria). Es la cobertura que más se olvida en el mayor.
- Traumatismo penetrante o neurocirugía previa: vancomicina + ceftazidima 2 g/8 h o cefepime 2 g/8 h o meropenem 2 g/8 h (en lugar de ceftriaxona). [VAULT: Meningitis y Encefalitis]
- ALERGIA a betalactámicos (anafilaxia): moxifloxacino 400 mg/24 h IV en lugar de la cefalosporina (mantener vancomicina ± añadir cobertura de Listeria con cotrimoxazol si procede). [VAULT: Meningitis y Encefalitis]
- Si no puedes descartar ENCEFALITIS (confusión, focalidad, crisis): añade aciclovir 10 mg/kg IV cada 8 h empíricamente, sin esperar a la PCR. [VAULT: Meningitis y Encefalitis]
- Quimioprofilaxis de contactos estrechos (meningococo): ciprofloxacino 500 mg VO dosis única o ceftriaxona 250 mg IM dosis única.

B. SOSPECHA DE FOCO URINARIO / UROSEPSIS
Pielonefritis y urosepsis se tratan parenteral. La cobertura empírica de la FJD evita quinolonas, cotrimoxazol y amoxicilina/clavulánico de inicio (resistencias locales elevadas). [VAULT: PROA ITU]
- Pielonefritis aguda / urosepsis: CEFTRIAXONA 2 g IV (1ª dosis en urgencias). Si manejo hospitalario, mantener ceftriaxona 2 g IV/24 h; si se decide alta (sin criterios de ingreso, ≥12 h de observación), pasar a cefixima 400 mg/24 h VO hasta 7 días, revisando antibiograma en 48 h. [VAULT: PROA ITU]
- Urosepsis con shock o sin foco urinario seguro: ceftriaxona 2 g/24 h o, si se prefiere bactericida rápido, gentamicina 5-7 mg/kg IV/24 h (peso ideal ajustado). [VAULT: Sepsis y Shock Séptico]
- ALERGIA a betalactámicos (confirmada): amikacina 15-20 mg/kg IV en urgencias (+ ciprofloxacino 500 mg/12 h VO al alta), revisando urocultivo en 48 h. [VAULT: PROA ITU]
- Riesgo de BLEE (ITU recurrente, dispositivos, exposición previa a quinolonas/cefalosporinas, hospitalización): valorar carbapenem según gravedad (p. ej. meropenem 1 g/8 h IV; ertapenem 1 g/24 h IV si estable y ambulatorizable). NO usar carbapenem sistemáticamente si hay alternativa sensible en antibiograma. [VAULT: PROA ITU]
- Sondado con fiebre sin otro foco: tratar como ITU + RECAMBIAR la sonda; cefixima 400 mg/24 h 7 días si ambulatorio, o ceftriaxona 2 g/24 h IV si ingresa. Revisar urocultivos previos por riesgo de MDR. [VAULT: PROA ITU]
- Ajuste renal de ceftriaxona: máximo 2 g/24 h si FG <10. [VAULT: PROA Betalactámicos]

C. SOSPECHA DE FOCO RESPIRATORIO / NAC
Decide el nivel asistencial con CURB-65; la pauta cambia según ambulatorio vs. ingreso vs. UCI. [VAULT: PROA Infecciones Respiratorias]
- NAC que ingresa (sala): CEFTRIAXONA 2 g IV/24 h + AZITROMICINA 500 mg IV/24 h (cobertura de neumococo + atípicos). Es la pauta empírica de sepsis de foco respiratorio. [VAULT: Sepsis y Shock Séptico]
- NAC grave / UCI (shock o insuficiencia respiratoria): ceftriaxona 2 g/24 h (o cefotaxima 2 g/6-8 h) + azitromicina 500 mg/24 h; valorar levofloxacino 500 mg/12 h como alternativa al macrólido. Si riesgo de Pseudomonas (bronquiectasias, EPOC grave, ATB de amplio espectro reciente): sustituir por pauta antipseudomónica (piperacilina-tazobactam 4/0,5 g IV/6 h en perfusión extendida, o cefepime 2 g/8 h, o meropenem) + azitromicina o levofloxacino. [GUÍA: estándar NAC grave; el vault da la pauta antipseudomónica en Sepsis Antiinfecciosos]
- ALERGIA a betalactámicos: levofloxacino 500 mg/24 h IV (cubre típicos y atípicos en monoterapia). [VAULT: PROA Infecciones Respiratorias]
- NAC de manejo ambulatorio (CURB-65 0-1), como referencia de paso a VO: <65 años sin comorbilidad → amoxicilina 1 g/8 h VO 5 días; >65 años o comorbilidad → amoxicilina/clavulánico 875/125 mg/8 h 7 días; sospecha de atípico → azitromicina 500 mg/24 h 3 días. [VAULT: PROA Infecciones Respiratorias]
- EPOC reagudizado con criterios de Anthonisen, como referencia: amoxicilina/clavulánico 875/125 mg/8 h; si FEV1 <30% o sospecha de Pseudomonas, ciprofloxacino 750 mg/12 h. [VAULT: PROA Infecciones Respiratorias]

D. SOSPECHA DE FOCO INTRAABDOMINAL / BILIAR
Recuerda: foco intraabdominal = factor de riesgo de anaerobios → añade cobertura anaerobia (SSC 2026 Rec. 28-29). Excepción biliar: en colecistitis comunitaria NO se añade metronidazol salvo fístula bilioentérica. [VAULT: Colecistitis Aguda; Sepsis Antiinfecciosos]
- Sepsis intraabdominal comunitaria (peritonitis, diverticulitis, absceso): CEFTRIAXONA 2 g IV/24 h + METRONIDAZOL 500 mg IV/8 h. [VAULT: Sepsis y Shock Séptico]
- Colecistitis/colangitis leve-moderada comunitaria: CEFTRIAXONA 2 g IV/24 h en monoterapia. Añadir metronidazol 500 mg/8 h SOLO si fístula bilioentérica (anastomosis biliodigestiva, stent biliar, CPRE previa). [VAULT: Colecistitis Aguda]
- Foco intraabdominal/biliar GRAVE, nosocomial o shock séptico: PIPERACILINA-TAZOBACTAM 4/0,5 g IV/6-8 h (perfusión extendida 3-4 h tras bolo inicial) o MEROPENEM 1 g/8 h IV (2 g/8 h si shock/MDR). Pip-tazo y carbapenems ya cubren anaerobios (no añadir metronidazol). [VAULT: Colecistitis Aguda; Sepsis Antiinfecciosos]
- Riesgo de BLEE o shock grave: priorizar MEROPENEM sobre pip-tazo. [VAULT: Sepsis Antiinfecciosos]
- Control del foco: la antibioterapia no sustituye al drenaje. Colangitis → drenaje biliar urgente (CPRE); absceso → drenaje; idealmente control del foco en las primeras 6 h (SSC 2026). [VAULT: Sepsis y Shock Séptico]
- Ajuste renal pip-tazo: FG 20-40 máx. 4/0,5 g/8 h; FG <20 máx. 4/0,5 g/12 h. Meropenem grave: FG 26-50 → 1 g/12 h; FG <10 → 1 g/24 h. [VAULT: PROA Betalactámicos]

E. SOSPECHA DE FOCO EN PIEL Y PARTES BLANDAS
La mayoría de las IPPB que producen sepsis son por S. pyogenes y S. aureus. Lo prioritario: distinguir celulitis simple de FASCITIS NECROTIZANTE (dolor desproporcionado, crepitación, bullas, rápida progresión, toxicidad sistémica) → urgencia quirúrgica + avisar YA. [VAULT: PROA IPPB]
- Celulitis/erisipela que ingresa con datos de gravedad o sepsis: cobertura de S. pyogenes y SASM. En guardia, parenteral: cefazolina 2 g IV/8 h (SASM y estreptococos) o amoxicilina/clavulánico 2 g/200 mg IV/8 h si celulitis complicada. [VAULT: PROA IPPB para amox-clav complicada; PROA Betalactámicos para dosis IV de cefazolina]
- Sospecha de SARM (hospitalización, ATB en 3 meses, ADVP, deportes de contacto): añadir o sustituir por cobertura anti-SARM → vancomicina 15-20 mg/kg IV/8-12 h, daptomicina 8-10 mg/kg IV/24 h o linezolid 600 mg/12 h. Ambulatorio leve: clindamicina 300 mg/8 h o cotrimoxazol 800/160 mg/12 h VO. [VAULT: PROA IPPB; Sepsis Antiinfecciosos]
- FASCITIS NECROTIZANTE / shock tóxico estreptocócico (manejo en guardia mientras se activa quirófano): cobertura de amplio espectro + clindamicina o linezolid por su efecto antitoxina. Pauta típica: piperacilina-tazobactam 4/0,5 g IV/6-8 h (o meropenem) + CLINDAMICINA 600-900 mg IV/8 h (o linezolid 600 mg/12 h), añadiendo vancomicina/daptomicina si riesgo de SARM. [GUÍA: estándar fascitis necrotizante; el vault aporta clindamicina/linezolid como antitoxina en S. pyogenes — Sepsis Antiinfecciosos Tabla 7]
- Mordedura con datos de infección: amoxicilina/clavulánico 875/125 mg/8 h (cobre Pasteurella/Eikenella/anaerobios); alergia → cotrimoxazol 800/160 mg/12 h + clindamicina 450 mg/8 h. Revisar tétanos/rabia. [VAULT: PROA IPPB]
- Herida con exposición a agua de mar/pescado (Vibrio vulnificus): doxiciclina + ceftriaxona/ciprofloxacino; punzante en planta del pie (Pseudomonas): ciprofloxacino 750 mg/12 h. [VAULT: PROA IPPB]

F. SEPSIS SIN FOCO CLARO
Si tras anamnesis, exploración y pruebas no hay foco, cubre de forma empírica según el ámbito de adquisición y la gravedad (Manual 12 de Octubre, Tabla 5). [VAULT: Sepsis Antiinfecciosos]
- Comunitaria, sin shock, sin riesgo de MDR: CEFTRIAXONA 2 g IV/24 h, ajustando cobertura según sospecha posterior. Si sospecha de anaerobios (no presente por defecto), añadir metronidazol 500 mg IV/8 h. [VAULT: Sepsis y Shock Séptico]
- Comunitaria con SHOCK SÉPTICO: priorizar piperacilina-tazobactam 4/0,5 g IV/6 h (perfusión extendida) o MEROPENEM 2 g IV/8 h (perfusión 3 h) sobre cefalosporina. ± amikacina 15-25 mg/kg/24 h por efecto bactericida rápido. ± daptomicina 8-10 mg/kg/24 h o linezolid 600 mg/12 h si sospecha de grampositivo resistente (linezolid preferible si foco pulmonar o shock tóxico). [VAULT: Sepsis Antiinfecciosos]
- Nosocomial o antibiótico previo: MEROPENEM 2 g/8 h (perfusión extendida) o ceftazidima-avibactam 2/0,5 g/8 h ± aztreonam + (daptomicina o linezolid) + amikacina ± anidulafungina 200 mg (carga) → 100 mg/24 h si riesgo de candidemia (Candida Score >2,5). [VAULT: Sepsis Antiinfecciosos]
- Riesgo de BLEE: priorizar MEROPENEM sobre pip-tazo. Cobertura anaerobia, antifúngica o de SARM SOLO con factores de riesgo (SSC 2026). [VAULT: Sepsis Antiinfecciosos]
- Tras carga inicial, perfusión extendida/continua de los betalactámicos de vida media corta (pip-tazo, carbapenems) — recomendación fuerte SSC 2026 (BLING III). [VAULT: Sepsis Antiinfecciosos]

G. NEUTROPÉNICO FEBRIL
Neutropenia (<500/mm³, o <1.000 en descenso) + fiebre = urgencia. Betalactámico ANTIPSEUDOMÓNICO en la primera hora, sin esperar a más pruebas. [VAULT: Sepsis y Shock Séptico]
- 1ª línea (monoterapia): CEFEPIME 2 g IV/8 h o PIPERACILINA-TAZOBACTAM 4/0,5 g IV/6 h (perfusión extendida) o MEROPENEM 1-2 g IV/8 h. [VAULT: Sepsis y Shock Séptico; dosis en PROA Betalactámicos]
- Añadir VANCOMICINA 15-20 mg/kg IV/8-12 h (o daptomicina/linezolid) SOLO si: inestabilidad/shock, sospecha de infección de catéter, mucositis grave, colonización por SARM o infección de piel y partes blandas. No de rutina. [GUÍA: estándar neutropenia febril; coherente con cobertura dirigida de grampositivos del vault]
- ALERGIA a betalactámicos (anafilaxia): aztreonam 2 g/8 h + vancomicina, ± amikacina (cubre gramnegativos y Pseudomonas sin betalactámico). [VAULT: PROA Betalactámicos — aztreonam en alergia a betalactámicos]
- Si fiebre persiste >4-7 días pese a antibiótico de amplio espectro y neutropenia prolongada: valorar antifúngico empírico (equinocandina, p. ej. anidulafungina/caspofungina; o anfotericina B liposomal). [VAULT: Candidemia en Sepsis Antiinfecciosos]
- Ajuste renal cefepime: FG 30-60 → 1 g/12-24 h; FG <11 → 250-500 mg/24 h (ojo neurotoxicidad: encefalopatía y mioclonías en FG alterado). [VAULT: PROA Betalactámicos]


6- PERLAS PARA NO OLVIDAR

🔑 La sospecha de sepsis no se puntúa, se avisa. NEWS2/SIRS para cribar mejor que el qSOFA aislado; sospecha de sepsis = aviso. El antibiótico empírico adecuado en la primera hora es la intervención que más vidas salva.

🔑 Hemocultivos x2 ANTES del antibiótico, pero sin retrasarlo si hay shock. Un urocultivo en el sondado y el recambio de la sonda; cultivos del foco siempre que puedas, pero nunca a costa de demorar el tratamiento.

🔑 Petequias o púrpura + fiebre = meningococo. Antibiótico INMEDIATO (ceftriaxona dosis meníngea), no esperes a la PL ni al TC; avisa mientras lo preparas.

🔑 Dexametasona ANTES o junto a la primera dosis de antibiótico en la meningitis, nunca después. Ceftriaxona a DOSIS MENÍNGEA (2 g/12 h, no 2 g/24 h). Ampicilina por Listeria si >50 años, embarazada o inmunodeprimido (la cobertura que más se olvida). Si dudas de encefalitis, aciclovir 10 mg/kg/8 h empírico.

🔑 El antibiótico es ESPECÍFICO por foco: urinario → ceftriaxona 2 g; respiratorio → ceftriaxona + azitromicina (CURB-65 decide el nivel); biliar comunitario → ceftriaxona en monoterapia (metronidazol solo si fístula); intraabdominal → ceftriaxona + metronidazol; partes blandas graves → añade clindamicina/linezolid por su efecto antitoxina.

🔑 Shock séptico o riesgo de BLEE/nosocomial: sube el escalón a piperacilina-tazobactam o meropenem (meropenem si BLEE), en perfusión extendida tras la carga. La cobertura de SARM, anaerobios o Candida solo si hay factores de riesgo (SSC 2026): cubrir de más selecciona resistencias.

🔑 Neutropénico febril: betalactámico antipseudomónico (cefepime 2 g/8 h o pip-tazo o meropenem) en la primera hora, sin esperar. Vancomicina solo si shock, catéter, mucositis o partes blandas.

🔑 Un lactato normal no descarta sepsis, y la hipotermia es mal pronóstico. La procalcitonina NO sirve para decidir iniciar el antibiótico (sí para suspenderlo). El anciano y el inmunodeprimido se descompensan rápido y con poca fiebre: fíate de las constantes y de la perfusión, no del termómetro.

🔑 Ajusta por alergia y por riñón, pero no a costa del tiempo. Alergia anafiláctica a betalactámicos → aztreonam (gramnegativos) + vancomicina (grampositivos) ± aminoglucósido, o moxifloxacino en la meningitis. La dosis de CARGA (vancomicina, aminoglucósidos) no se reduce por insuficiencia renal; solo se ajustan las dosis de mantenimiento.
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
1) Prioriza guías EUROPEAS (ESC) y ESPAÑOLAS (SEC, SEMES, GEMA, GALAXIA, SEPAR, SEN, SSC) cuando existan; usa AHA/ACC/GINA/GOLD como complemento y AVISA cuando la recomendación europea/española difiera de la americana (dosis, umbrales o fármacos).
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
3) El estilo es texto plano conciso de bolsillo, sin frontmatter ni referencias dentro de la guía: no lo marques como defecto. Esta guía SÍ detalla el tratamiento concreto (fármaco, dosis, vía e intervalo) por diagnóstico; revisa esas dosis y pautas a fondo, que es lo que más importa.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

DOLOR ABDOMINAL

Todo dolor abdominal agudo puede esconder una catástrofe quirúrgica. Tu trabajo en los primeros minutos no es llegar al diagnóstico exacto: es identificar al paciente que se muere (peritonitis, isquemia, rotura vascular, perforación) y separarlo del que puede esperar. La analgesia NO enmascara el diagnóstico — adminístrala desde el principio.


1- CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR
Mirada rápida de 10 segundos — avisa si detectas cualquiera de estos:
- TAS <90 mmHg o signos de shock (palidez, sudoración fría, taquicardia, obnubilación).
- FC >120 lpm con dolor abdominal (pensar en hemorragia intraabdominal, sepsis, perforación).
- Tª >38,5 °C + defensa abdominal (peritonitis séptica).
- Abdomen en tabla (rigidez involuntaria generalizada) = peritonitis → cirugía.
- Distensión abdominal masiva con vómitos fecaloideos (obstrucción intestinal avanzada).
- Masa abdominal pulsátil + hipotensión (rotura de aneurisma aórtico abdominal).
- Paciente inmóvil, quieto, que no tolera ningún movimiento (irritación peritoneal).
- Dolor desproporcionado a la exploración ("me duele muchísimo" pero el abdomen está blando) → isquemia mesentérica hasta que se demuestre lo contrario.
- Rectorragia masiva o hematemesis con inestabilidad hemodinámica.
- Mujer en edad fértil + dolor abdominal + hipotensión → embarazo ectópico roto hasta que se descarte.

Regla de oro: el paciente anciano, inmunodeprimido u obeso puede tener una catástrofe abdominal con exploración casi normal. Si algo no cuadra, avisa.


2- QUÉ PREGUNTAR (anamnesis dirigida, <3 minutos)

1. LOCALIZACIÓN DEL DOLOR
*Epigástrico: úlcera péptica, pancreatitis, SCA (infarto inferior), disección aórtica.
*Hipocondrio derecho (HCD): colecistitis, cólico biliar, hepatitis, neumonía basal derecha.
*Hipocondrio izquierdo (HCI): infarto esplénico, pancreatitis (cola), neumonía basal izquierda.
*Fosa ilíaca derecha (FID): apendicitis, ectópico, torsión ovárica, adenitis mesentérica.
*Fosa ilíaca izquierda (FII): diverticulitis, ectópico, torsión ovárica, cólico renal.

2. CARÁCTER DEL DOLOR
*Difuso: peritonitis, obstrucción intestinal, isquemia mesentérica, rotura de AAA, cetoacidosis diabética.
*Cólico (va y viene): biliar, renal, obstrucción intestinal.
*Inflamatorio (continuo y creciente): apendicitis, colecistitis, pancreatitis, peritonitis.

3. INSTAURACIÓN
- Súbita (segundos): perforación de víscera hueca, rotura de AAA, disección aórtica, torsión ovárica/testicular, infarto esplénico/renal.
- Progresiva (horas): apendicitis, colecistitis, pancreatitis, diverticulitis, obstrucción.
- Recurrente: cólico biliar, cólico renal, enfermedad inflamatoria intestinal, úlcera péptica.

4. SÍNTOMAS ACOMPAÑANTES
- Vómitos precoces + dolor difuso → obstrucción intestinal alta, pancreatitis.
- Ausencia de gases y heces en las últimas 24 h → obstrucción intestinal.
- Diarrea sanguinolenta + dolor → isquemia mesentérica, colitis isquémica, EII.
- Ictericia + fiebre + dolor en HCD (tríada de Charcot) → colangitis aguda. Si se añade confusión + hipotensión (péntada de Reynolds) → colangitis grave.
- Disuria + hematuria → cólico renal, ITU.
- Amenorrea + sangrado vaginal + dolor en FI → embarazo ectópico.

5. ANTECEDENTES Y FÁRMACOS
- Cirugías abdominales previas (adherencias → obstrucción).
- AINEs, anticoagulantes, corticoides (úlcera, hemorragia).
- FA, vasculopatía, ICC (isquemia mesentérica).
- Neoplasia activa (obstrucción, perforación, metástasis).
- Última menstruación en toda mujer en edad fértil (embarazo ectópico).
- Aneurisma aórtico conocido.


3- QUÉ EXPLORAR (exploración dirigida, <2 minutos)

INSPECCIÓN
- Posición del paciente: inmóvil (peritonitis) vs. agitado/retorciéndose (cólico).
- Distensión abdominal, cicatrices quirúrgicas (adherencias), hernias visibles.
- Equimosis periumbilical (signo de Cullen) o en flancos (signo de Grey-Turner) → hemorragia retroperitoneal (pancreatitis necrotizante, rotura de AAA). Son signos tardíos pero muy específicos.

AUSCULTACIÓN
- Ruidos metálicos/de lucha → obstrucción mecánica.
- Silencio abdominal → íleo paralítico, peritonitis, isquemia mesentérica avanzada.
- Soplo abdominal → aneurisma, estenosis arterial.

PERCUSIÓN / PALPACIÓN
- Percusión dolorosa focal = test más sensible y menos doloroso que el Blumberg para detectar irritación peritoneal.
- Defensa involuntaria (rigidez) = peritonitis → cirugía.
- Murphy positivo (detención de la inspiración al palpar HCD) → colecistitis. Específico pero no descarta si es negativo.
- McBurney, Rovsing, psoas, obturador → apendicitis (baja sensibilidad individual, pero aumentan la probabilidad si son positivos).
- Carnett positivo (dolor que aumenta al contraer la pared abdominal) → dolor de pared abdominal (no intraabdominal).
- Masa pulsátil → AAA. No palpar repetidamente si se sospecha rotura.

EXPLORACIÓN DIRIGIDA
- Tacto rectal: si sospecha de hemorragia digestiva alta/baja, obstrucción, absceso pélvico.
- Exploración ginecológica: en toda mujer con dolor en hipogastrio/fosas ilíacas (masas anexiales, cervicitis, sangrado).
- Orificios herniarios: SIEMPRE. Una hernia incarcerada es una causa frecuente y evitable de obstrucción.
- Exploración testicular en varones con dolor abdominal bajo (torsión testicular referida).
- POCUS (ecografía a pie de cama): líquido libre (FAST), colelitiasis, hidronefrosis III-IV, AAA (diámetro >3 cm = aneurisma; >5 cm con dolor = urgencia), embarazo intrauterino (descarta ectópico).


4- QUÉ PRUEBAS PEDIR

INMEDIATAS
- Test de embarazo (β-hCG): OBLIGATORIO en toda mujer en edad fértil con dolor abdominal. Un ectópico roto mata.
- Glucemia capilar: descartar cetoacidosis diabética como causa de dolor abdominal.
- ECG: en todo dolor epigástrico, especialmente en >50 años. El IAM inferior puede presentarse como "dolor de estómago".

ANALÍTICA BÁSICA
*Hemograma (leucocitosis con neutrofilia: OR 2,4 para patología quirúrgica), bioquímica (creatinina, iones, glucosa), coagulación.
*PCR: >0,6 mg/dL se asocia a patología quirúrgica (OR 2,8). Útil como marcador de inflamación, pero inespecífica.
*Lipasa sérica: >3× el límite superior de la normalidad = pancreatitis aguda (OR 26,4 para ingreso/cirugía). Más sensible y específica que la amilasa.
*Perfil hepático: GOT, GPT, GGT, FA, bilirrubina. Imprescindible si dolor en HCD o ictericia.
*Lactato: >2 mmol/L = hipoperfusión. En dolor abdominal con lactato elevado, pensar en isquemia mesentérica o sepsis abdominal. Pero un lactato normal NO descarta isquemia mesentérica precoz.
*Sedimento de orina: hematuria (cólico renal), piuria (ITU), leucocituria sin bacteriuria (apendicitis retrocecal, diverticulitis).

PRUEBAS DE IMAGEN
*Ecografía abdominal: primera elección en dolor en HCD (colecistitis: sensibilidad 81%, especificidad 83%). También útil para líquido libre, hidronefrosis, AAA, patología ginecológica.
*TC abdominopélvico con contraste IV: gold standard para dolor abdominal agudo en adultos no embarazados. La TC con contraste es ~30% más precisa que sin contraste. No retrasar por creatinina si no hay antecedente de insuficiencia renal. Solicitar si:
  → Dolor difuso o localización atípica.
  → Sospecha de apendicitis (en pacientes mayores), diverticulitis, obstrucción, perforación, isquemia mesentérica.
  → Discordancia entre clínica y exploración.
*Angio-TC (trifásica): si sospecha de isquemia mesentérica o rotura/disección aórtica.
*Rx de abdomen: papel limitado. Útil solo si sospecha de neumoperitoneo (aire libre subdiafragmático), obstrucción (niveles hidroaéreos) o cuerpo extraño. La TC la ha sustituido en la mayoría de indicaciones.

Escalas de probabilidad clínica
- Alvarado (apendicitis): <4 = improbable; 4-6 = posible (solicitar imagen); ≥7 = probable (consulta quirúrgica). Sensibilidad 72%, especificidad 77%.
- RIPASA (apendicitis): ≥7,5 = positivo. Mayor sensibilidad que Alvarado (93-95% vs. 72%), especialmente útil para descartar apendicitis cuando es negativo.
- BISAP (pancreatitis): BUN >25 mg/dL, alteración del nivel de consciencia, SIRS, edad >60 años, derrame pleural. ≥3 = pancreatitis grave (OR 7,4 para fallo orgánico; mortalidad >20%).
- Tokyo Guidelines (colecistitis): Grado I (leve), Grado II (moderada: leucocitos >18.000, masa palpable, síntomas >72 h), Grado III (grave: disfunción orgánica).

⚠ TRAMPAS COMUNES
- Dolor abdominal + ECG normal ≠ "no es cardíaco". El IAM inferior puede tener ECG inicial normal. Si hay factores de riesgo, pedir troponina seriada.
- Leucocitos normales NO descartan apendicitis ni isquemia mesentérica. La clínica manda.
- Lipasa normal NO descarta pancreatitis si han pasado >5 días desde el inicio (puede haberse normalizado).
- Lactato normal NO descarta isquemia mesentérica precoz. Se eleva cuando ya hay necrosis transmural.
- El anciano con dolor abdominal es un campo de minas. Puede tener una perforación con mínima defensa, una isquemia mesentérica con exploración anodina, o un AAA roto con "lumbalgia". Umbral bajo para TC.
- Dolor "desproporcionado" a la exploración = isquemia mesentérica hasta que se demuestre lo contrario. Es el diagnóstico más letal que más se retrasa.


5- MEDIDAS Y TRATAMIENTO SEGÚN SOSPECHA

MEDIDAS GENERALES DE SOPORTE
- ABC. Monitorización: TA, FC, SatO₂, Tª.
- Vía venosa periférica (dos vías de grueso calibre si sospecha de hemorragia o shock).
- Fluidoterapia: Ringer Lactato. Bolo de 500 mL si signos de hipovolemia; ajustar según respuesta.
- ANALGESIA PRECOZ: no retrasar. No altera la precisión diagnóstica ni la toma de decisiones quirúrgicas.
*1ª línea: paracetamol 1 g IV + dexketoprofeno 50 mg IV (o ketorolaco 30 mg IV). Los AINEs son tan eficaces como los opioides en cólico biliar y renal (NNT = 3).
*2ª línea (dolor intenso): cloruro mórfico 0,05-0,1 mg/kg IV titulado (bolos de 2-3 mg cada 5-10 min hasta control del dolor). Alternativa: fentanilo 1 µg/kg IV.
*Evitar AINEs si sospecha de hemorragia digestiva, insuficiencia renal, o perforación.
- DIETA ABSOLUTA si sospecha de patología quirúrgica.
- SNG si vómitos incoercibles u obstrucción intestinal.

A. SOSPECHA DE APENDICITIS AGUDA
- ANALGESIA + DIETA ABSOLUTA + FLUIDOTERAPIA.
- SOLICITAR TC abdominopélvico con contraste (o ecografía como primera opción en jóvenes, embarazadas y niños). Interconsulta a Cirugía General precoz si Alvarado ≥7 o RIPASA ≥7,5.
- ANTIBIOTERAPIA PREOPERATORIA: cefazolina 2 g IV + metronidazol 500 mg IV (o amoxicilina-clavulánico 2 g/200 mg IV). Administrar en la hora previa a la incisión.
- Si apendicitis no complicada confirmada: apendicectomía laparoscópica (estándar). El manejo conservador con antibióticos solos es una alternativa en casos seleccionados (apendicitis no complicada, sin apendicolito), aunque con tasa de recurrencia del 25-40% a 5 años.

B. SOSPECHA DE COLECISTITIS AGUDA
- ANALGESIA: AINEs como primera línea (dexketoprofeno 50 mg IV o ketorolaco 30 mg IV). Reducen el dolor y la progresión de cólico biliar a colecistitis (NNT = 3). Opioides como rescate (nota: las guías americanas no comercializan metamizol; en España el metamizol tiene efecto antiespasmódico, por lo que muchos lo ponen antes que el ketorolaco).
- DIETA ABSOLUTA + FLUIDOTERAPIA.
- ANTIBIÓTICOS: ceftriaxona 2 g ± metronidazol 500 mg IV o amoxicilina-clavulánico 2 g/200 mg IV/8 h. Alternativa: piperacilina-tazobactam 4/0,5 g IV/6-8 h si sospecha de colecistitis grave o colangitis.
- ECOGRAFÍA ABDOMINAL URGENTE.
- Interconsulta a Cirugía General con el dx: colecistectomía laparoscópica precoz (dentro de las primeras 72 h) es el tratamiento de elección. La cirugía precoz reduce complicaciones (11,8% vs. 34,4%), estancia hospitalaria y costes frente a la cirugía diferida. Tokyo Grado III (grave con disfunción orgánica): valorar colecistostomía percutánea como puente si el paciente no es candidato quirúrgico.
- Si sospecha de colangitis aguda (tríada de Charcot): antibióticos de amplio espectro + drenaje biliar urgente (CPRE). Si péntada de Reynolds (confusión + hipotensión): soporte en UCI + drenaje biliar emergente.

C. SOSPECHA DE PANCREATITIS AGUDA
Diagnóstico: ≥2 de 3 criterios (dolor abdominal típico + lipasa >3× LSN + hallazgos en imagen). BISAP ≥3: alto riesgo de fallo orgánico y necrosis. Considerar ingreso en UCI/semicríticos.
- DIETA ABSOLUTA INICIALMENTE. Reiniciar dieta oral baja en grasa precozmente (en 24-48 h) si tolera y dolor controlado.
- FLUIDOTERAPIA AGRESIVA PRECOZ (primeras 12-24 h): Ringer Lactato (preferido sobre SSF) a 5-10 mL/kg/h, ajustando a objetivos: FC <120, PAM 65-85 mmHg, diuresis >0,5 mL/kg/h, descenso de BUN. Evitar sobrehidratación tras las primeras 24-48 h (riesgo de complicaciones respiratorias y síndrome compartimental abdominal).
- ANALGESIA: paracetamol IV (ahorrador de opioides) + opioides titulados (morfina 2-3 mg cada 15 min hasta rebajar dolor). No hay evidencia de que la morfina empeore la pancreatitis.
- NO DAR ANTIBIÓTICOS PROFILÁCTICOS en pancreatitis aguda (no previenen necrosis infectada).
- Si etiología biliar con colangitis asociada: CPRE urgente (<24 h).
- Si etiología biliar sin colangitis: colecistectomía durante el mismo ingreso (una vez resuelta la pancreatitis).

D. SOSPECHA DE OBSTRUCCIÓN INTESTINAL
- DIETA ABSOLUTA + SNG a aspiración (descompresión).
- FLUIDOTERAPIA AGRESIVA (las pérdidas al tercer espacio son enormes → Ringer 1.000 mL de primeras e ir viendo hasta corregir hipovolemia).
- CORREGIR IONES (hipopotasemia frecuente).
- ANALGESIA (evitar AINEs si sospecha de isquemia asociada).
- SONDAJE VESICAL para control de diuresis.
- PRUEBA DE IMAGEN → TC abdominopélvico con contraste IV: identifica causa, nivel de obstrucción y signos de complicación (isquemia, estrangulación, vólvulo).
- INTERCONSULTA a Cirugía General desde el inicio (la obstrucción ingresada en servicio quirúrgico tiene menor estancia y mortalidad que en servicio médico).
- CIRUGÍA URGENTE SI: peritonitis, signos de estrangulación/isquemia en TC (neumatosis, gas portal, ausencia de realce de pared), acidosis metabólica, fiebre, leucocitosis progresiva, dolor continuo.
- MANEJO CONSERVADOR (si no hay signos de complicación): SNG + fluidoterapia + observación. Si no resuelve en 48-72 h: estudio con contraste hidrosoluble (gastrografín) — es diagnóstico y terapéutico. Si no resuelve en 3-5 días: cirugía. Cada día de retraso quirúrgico en obstrucción que no responde al manejo conservador aumenta un 20% la probabilidad de resección intestinal.

E. SOSPECHA DE ISQUEMIA MESENTÉRICA
Pensar en ella si paciente >60 años, FA, vasculopatía, ICC, dolor desproporcionado a la exploración, diarrea sanguinolenta.
- PRUEBA DE IMAGEN → Angio-TC trifásica urgente (sin contraste + arterial + venosa): modalidad de elección. No esperar a la analítica.
- TRATAMIENTO INMEDIATO:
  *FLUIDOTERAPIA agresiva con cristaloides (se hipotensan como nada y se mueren).
  *HEPARINA NF IV: bolo 80 UI/kg + perfusión 18 UI/kg/h (anticoagulación plena desde la sospecha).
  *ANTIBIOTERAPIA DE AMPLIO ESPECTRO: piperacilina-tazobactam 4/0,5 g IV/6-8 h o meropenem 1 g IV/8 h (alto riesgo de translocación bacteriana).
  *DIETA ABSOLUTA + SNG.
  *ANALGESIA agresiva (opioides IV titulados).
- INTERCONSULTA URGENTE multidisciplinar: Cirugía General + Radiología Intervencionista + Cirugía Vascular.
  *Si peritonitis: laparotomía urgente con resección del intestino necrótico + second-look a las 24-48 h.
  *Si trombosis venosa mesentérica sin peritonitis: anticoagulación con heparina IV (puede ser suficiente).
- MORTALIDAD GLOBAL: 50-80%. El diagnóstico precoz es el único factor modificable que mejora la supervivencia.

F. SOSPECHA DE PERFORACIÓN DE VÍSCERA HUECA
- PRUEBA DE IMAGEN: Rx de tórax en bipedestación (neumoperitoneo: aire libre subdiafragmático). Si no es concluyente: TC con contraste.
- DIETA ABSOLUTA + SNG a aspiración.
- FLUIDOTERAPIA AGRESIVA + corrección de alteraciones hidroelectrolíticas.
- ANTIBIOTERAPIA DE AMPLIO ESPECTRO: piperacilina-tazobactam 4/0,5 g IV/6-8 h o meropenem 1 g IV/8 h.
- IBP IV: omeprazol 80 mg IV en bolo + perfusión 8 mg/h (si sospecha de úlcera péptica perforada).
- INTERCONSULTA CON CGD urgente. La cirugía dentro de las primeras 12 h mejora significativamente los resultados. Retrasar >12 h sin mejoría clínica empeora el pronóstico.
- Manejo conservador (sin cirugía) solo en casos muy seleccionados: <70 años, hemodinámicamente estable, sin peritonitis difusa, sin sepsis, perforación sellada confirmada por imagen. Reevaluar cada 6-12 h.

G. SOSPECHA DE ROTURA DE ANEURISMA AÓRTICO ABDOMINAL (AAA)
- Tríada clásica: dolor abdominal/lumbar + hipotensión + masa abdominal pulsátil. Solo presente en ~50% de los casos.
- Si inestable: activar código quirúrgico/vascular inmediatamente. No perder tiempo en pruebas.
- Si estable: TC con contraste urgente para confirmar diagnóstico y planificar reparación (endovascular vs. abierta).
- Hipotensión permisiva: objetivo TAS 70-90 mmHg. No reanimar agresivamente con líquidos (aumenta el sangrado). Cristaloides en bolos pequeños (250 mL) solo para mantener consciencia y pulso.
- Cruzar y reservar hemoderivados (mínimo 6 concentrados de hematíes). Activar protocolo de transfusión masiva si es necesario.
- Reparación endovascular (EVAR) preferida sobre cirugía abierta si la anatomía lo permite (menor morbimortalidad).
- Mortalidad global del AAA roto: 80-90% (incluyendo los que no llegan al hospital). En los que llegan y se operan: ~50% con cirugía abierta, ~18% con EVAR en centros con protocolo de rotura.

H. CÓLICO RENAL
- Analgesia: AINEs como primera línea. Dexketoprofeno 50 mg IV o ketorolaco 30 mg IV (NNT ~3). Tan eficaces como opioides con menos efectos adversos.
- Paracetamol 1 g IV como adyuvante.
- Opioides solo si refractario: cloruro mórfico 0,05-0,1 mg/kg IV titulado.
- Antieméticos: metoclopramida 10 mg IV u ondansetrón 4 mg IV.
- TC sin contraste: gold standard para confirmar litiasis y descartar complicaciones (hidronefrosis, pionefrosis). Alternativa: ecografía (primera opción en embarazadas y niños).
- Criterios de ingreso/interconsulta a Urología: litiasis >10 mm, obstrucción completa, riñón único, pionefrosis (fiebre + obstrucción = urgencia urológica → drenaje con catéter doble J o nefrostomía), insuficiencia renal, dolor refractario.
- Alfa-bloqueante (tamsulosina 0,4 mg/día) como terapia médica expulsiva para litiasis de 5-10 mm (evidencia moderada, beneficio modesto).


6- PERLAS PARA NO OLVIDAR

🔑 Test de embarazo en TODA mujer en edad fértil con dolor abdominal. Un ectópico roto es la causa más letal que más fácilmente se pasa por alto. Se puede ampliar en el sistemático de orina.

🔑 ECG en todo dolor epigástrico. El IAM inferior se disfraza de "gastritis" con una frecuencia alarmante. Un ECG tarda 2 minutos y puede salvar una vida.

🔑 "Dolor desproporcionado a la exploración" = isquemia mesentérica. El paciente grita de dolor pero el abdomen está blando. Si es anciano con FA o vasculopatía, pide angio-TC trifásica ya.

🔑 Revisa los orificios herniarios. Siempre. La hernia incarcerada es una causa frecuente de obstrucción intestinal que se diagnostica con las manos, no con el TC.

🔑 La analgesia NO enmascara el diagnóstico. Múltiples ensayos aleatorizados lo confirman. No dejar sufrir al paciente "para no perder signos" es una práctica obsoleta y éticamente inaceptable.

🔑 AINEs/metamizol antes que opioides en cólico biliar y renal. Son igual de eficaces, con menos efectos adversos, y en el cólico biliar reducen la progresión a colecistitis.

🔑 El anciano con dolor abdominal es el paciente más peligroso de urgencias. Exploración anodina, leucocitos normales, y por dentro puede tener una isquemia mesentérica, un AAA roto o una perforación sellada. Umbral bajísimo para TC con contraste.

🔑 Lipasa >3× LSN = pancreatitis. No pidas amilasa si puedes pedir lipasa (más sensible y específica). Y recuerda: la fluidoterapia agresiva con Ringer Lactato en las primeras 12-24 h es el pilar del tratamiento, no los antibióticos.

🔑 TC con contraste IV es ~30% más precisa que sin contraste para el dolor abdominal agudo. No la pidas sin contraste "por si acaso la creatinina" salvo que haya antecedente real de insuficiencia renal. El riesgo de no diagnosticar supera al riesgo del contraste.
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
1) Prioriza guías EUROPEAS (ESC) y ESPAÑOLAS (SEC, SEMES, GEMA, GALAXIA, SEPAR, SEN, SSC) cuando existan; usa AHA/ACC/GINA/GOLD como complemento y AVISA cuando la recomendación europea/española difiera de la americana (dosis, umbrales o fármacos).
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
3) El estilo es texto plano conciso de bolsillo, sin frontmatter ni referencias dentro de la guía: no lo marques como defecto. Esta guía SÍ detalla el tratamiento concreto (fármaco, dosis, vía e intervalo) por diagnóstico; revisa esas dosis y pautas a fondo, que es lo que más importa.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

CEFALEA

La mayoría de las cefaleas son primarias y benignas, pero tu trabajo en la puerta es el contrario: detectar la cefalea secundaria que mata. Las primarias (tensional, migraña, racimos) se tratan y se van de alta; las secundarias graves (hemorragia subaracnoidea, meningitis, arteritis de células gigantes, trombosis venosa, glaucoma agudo) tienen ventana terapéutica corta y el retraso cuesta vida o visión. Esta guía te orienta mientras valoras, te dice cuándo dejar de tratar el dolor y avisar, y —para cada sospecha grave— te da el fármaco concreto con dosis, vía y tiempos para que NO te quedes parado esperando al adjunto. Las banderas rojas se memorizan como SNOOP / SNNOOP10. La analgesia precoz NO enmascara el diagnóstico: trátala, pero no dejes de estudiar.


1- CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR
Toma constantes con temperatura, tensión arterial y glucemia capilar. Mirada rápida de 10 segundos — avisa si detectas cualquiera de estos:
- Cefalea en trueno: máxima intensidad en menos de 1 minuto, o "la peor cefalea de mi vida". Es hemorragia subaracnoidea mientras no se demuestre lo contrario.
- Cefalea con fiebre y rigidez de nuca o alteración del nivel de consciencia: sospecha de meningitis o encefalitis. No esperes a la PL ni al TC para iniciar el tratamiento.
- Focalidad neurológica nueva (motora, sensitiva, del lenguaje o cerebelosa), papiledema en el fondo de ojo o crisis comicial.
- Disminución del nivel de consciencia (Glasgow ≤12) o deterioro progresivo.
- Cefalea de inicio reciente o progresiva en >50 años: piensa en arteritis de células gigantes (claudicación mandibular, arteria temporal indurada o dolorosa, alteración visual) y en lesión ocupante de espacio. La amaurosis fugax es una urgencia: corticoide YA.
- Inmunodeprimido o paciente oncológico (absceso, toxoplasmosis, metástasis, linfoma del SNC, meningitis criptocócica).
- Embarazo o puerperio: trombosis venosa cerebral, preeclampsia/eclampsia, SVCR postparto.
- Desencadenada por Valsalva (tos, esfuerzo), que cambia con la postura, o que interrumpe el sueño nocturno (HTIC / LOE de fosa posterior).
- Tras un traumatismo craneal, sobre todo en ancianos, anticoagulados o bebedores (hematoma subdural).
- Ojo rojo doloroso con midriasis media arreactiva y visión de halos: glaucoma agudo de ángulo cerrado. Es una urgencia oftalmológica que también puede perder la visión.
- TA sistólica >220 o <90 mmHg; Tª >38,5 °C con rigidez de nuca; SatO₂ <92 %.

Regla de oro: ante la sospecha de una causa grave, AVISA y empieza el tratamiento que esta guía detalla; no es tu trabajo estratificarla ni descartarla solo, pero tampoco dejes al paciente sin la primera dosis. La analgesia no debe enmascarar ni retrasar el diagnóstico.


2- QUÉ PREGUNTAR (anamnesis dirigida, <3 minutos)

1. TIEMPO HASTA EL PICO DE DOLOR
- Instantáneo (segundos, "como un mazazo") → cefalea en trueno y hemorragia subaracnoidea (también TVC, disección arterial, SVCR, apoplejía hipofisaria).
- Horas-días → infección (meningitis/encefalitis) o causa progresiva (LOE, HTIC, hematoma subdural).

2. ¿PRIMER EPISODIO O CEFALEA RECURRENTE CONOCIDA?
- Y si la conoce: ¿es exactamente igual a las de siempre o ha cambiado de patrón, frecuencia o intensidad? "Igual que siempre" tranquiliza; "distinta a las de siempre" obliga a estudiar.

3. LOCALIZACIÓN Y CARÁCTER
- Pulsátil hemicraneal con foto/fonofobia y náusea, que empeora con la actividad → migraña.
- Opresivo bilateral "en banda", leve-moderada, sin náuseas, no empeora con la actividad → tensional.
- Unilateral periocular con lagrimeo, rinorrea, miosis/ptosis o congestión nasal, en crisis cortas y muy intensas ("dolor suicida") → cefalea en racimos.
- Sorda, quemante, en sien/cuero cabelludo en >50 años ("el peine me quema al rozar la sien") → arteritis de células gigantes.

4. SÍNTOMAS ACOMPAÑANTES
- Aura visual; fiebre; vómitos sin otra causa; despertar nocturno por el dolor; claudicación mandibular; alteración visual; crisis.

5. POSTURA, ESFUERZO Y VALSALVA
- ¿Empeora de pie (hipotensión licuoral) o tumbado/por la mañana (HTIC/LOE)? ¿Con el esfuerzo, la tos o el Valsalva?

6. FÁRMACOS Y TÓXICOS
- Sobreuso de analgésicos o triptanes (cefalea por abuso de medicación: >15 días/mes con simples, >10 con triptanes/opioides/combinados), y fármacos nuevos (nitratos, anticonceptivos, inhibidores de PDE5).
- Anticoagulantes (condicionan hematoma subdural y manejo de hemorragias).
- Exposición a monóxido de carbono: braseros, calentadores, varios convivientes con cefalea a la vez en invierno.


3- QUÉ EXPLORAR (exploración dirigida, <2 minutos)
Recuerda: una exploración normal NO descarta una causa secundaria.

CONSTANTES
- Temperatura, glucemia capilar y tensión arterial (cifras >160/120 pueden justificar la cefalea; descarta también crisis hipertensiva y preeclampsia en gestante).

NEUROLÓGICO
- Nivel de consciencia (Glasgow, separado en O-V-M si lo vas a transmitir a Neurocirugía) y focalidad motora, sensitiva o cerebelosa; pares craneales; lenguaje.

SIGNOS MENÍNGEOS
- Rigidez de nuca (Kernig, Brudzinski). Su ausencia no descarta meningitis precoz.

OJO Y FONDO DE OJO
- Papiledema (HTIC); agudeza visual y pupilas: midriasis media fija + ojo rojo + córnea turbia (glaucoma), Horner doloroso (disección carotídea), defecto pupilar aferente (neuropatía óptica isquémica de la ACG).

PALPACIÓN
- Arterias temporales (induración, engrosamiento, ausencia de pulso o dolor en la arteritis de células gigantes) y senos frontales y maxilares (sinusitis).

PIEL
- Petequias/púrpura (meningococo), exantema, herpes zóster en territorio V1.


4- QUÉ PRUEBAS PEDIR

- La mayoría de las cefaleas primarias NO requieren ninguna prueba: el diagnóstico es clínico.
- TC craneal urgente sin contraste si hay cualquier bandera roja: trueno, focalidad, crisis, papiledema, >50 de novo, inmunodepresión o traumatismo. Hazla en general antes de la punción lumbar. Sensibilidad para HSA 93-100 % en las primeras 6 h, cae al 85-90 % a las 72 h y al 50 % a la semana.
- Punción lumbar: obligatoria si sospechas meningitis (citobioquímica, glucorraquia, proteínas, lactato, Gram, cultivos y PCR múltiple). Y si el TC es normal pero persiste la sospecha de hemorragia subaracnoidea, la PL buscando xantocromía (realizada ≥6-12 h tras el inicio) sigue siendo necesaria: un TC normal NO descarta la HSA. NO retrases el antibiótico ni la dexametasona por esperar a la PL o al TC.
- Analítica: hemograma, bioquímica con iones y función renal, coagulación. Hemocultivos (×2) antes del antibiótico si fiebre. Glucemia capilar siempre.
- VSG y PCR si sospechas arteritis de células gigantes; pídelas, pero NO esperes al resultado para empezar el corticoide. En la ACG la VSG suele ser de triple cifra (>80-100 mm/h) con trombocitosis y anemia de trastorno crónico.
- Dímero-D si sospechas trombosis venosa cerebral (VPN alto; si normal con baja sospecha, reduce la probabilidad). Confirmación con angio-TC venoso o venografía-RM.
- RM, angio-TC o venografía cuando se sospecha causa vascular o trombosis venosa: coordínalo con el adjunto, pero no demores la anticoagulación si la sospecha de TVC es alta y se confirma.
- Tonometría (presión intraocular) y avisar a Oftalmología si sospechas glaucoma agudo (PIO típicamente >40-50 mmHg).

Escalas de probabilidad clínica
- SNNOOP10 (banderas rojas): Síntomas sistémicos/fiebre, Neoplasia, déficit Neurológico, Onset súbito (trueno), Older (>50), cambio de Patrón, Papiledema, Posicional, precipitada por Valsalva, Progresiva, Embarazo, dolor Ocular, Postraumática, Patología inmune, abuso de analgésicos (Painkiller). Cualquier positivo obliga a descartar causa secundaria.
- Ottawa SAH Rule (cefalea no traumática, máxima en <1 h, alerta, ≥15 años): investigar HSA si edad ≥40, dolor o rigidez cervical, pérdida de consciencia presenciada, inicio durante el esfuerzo, cefalea en trueno (pico instantáneo) o flexión cervical limitada. Sensibilidad ~100 %, especificidad baja (sirve para descartar, no para confirmar).
- Hunt & Hess y WFNS (gravedad de la HSA ya confirmada); Fisher (riesgo de vasoespasmo en TC).

⚠ TRAMPAS COMUNES
- Un TC craneal normal NO descarta la HSA: si la sospecha persiste, hace falta la PL con xantocromía.
- En la arteritis de células gigantes, NO esperes a la VSG ni a la biopsia para iniciar el corticoide: retrasarlo puede costar la visión, y la biopsia sigue siendo rentable hasta ~1 semana tras empezar el corticoide.
- Si sospechas meningitis bacteriana, no demores la antibioterapia ni la dexametasona por esperar a la PL o al TC. El retraso del antibiótico es el factor pronóstico más modificable.
- Los opioides NO son de primera línea en la cefalea: empeoran la náusea, no abortan la migraña y favorecen la cefalea por abuso de medicación.
- "Igual que siempre" tranquiliza; "distinta a las de siempre" o "la peor de mi vida" obliga a estudiar.
- En el embarazo/puerperio una cefalea nueva no es "migraña del embarazo" hasta descartar TVC y preeclampsia.
- En el anciano, el dolor "del peine" o la claudicación al masticar no es banal: es ACG hasta que se demuestre lo contrario.


5- MEDIDAS Y TRATAMIENTO SEGÚN SOSPECHA

MEDIDAS GENERALES DE SOPORTE
- Si hay bandera roja, lo primero es avisar y, en paralelo, iniciar el tratamiento específico que sigue; la analgesia no debe enmascarar ni retrasar el diagnóstico.
- ABC y monitorización (TA, FC, SatO₂, Tª). Vía venosa periférica. Glucemia capilar.
- Para la cefalea primaria: ambiente tranquilo y oscuro, reposo.
- Antiemético si náuseas/vómitos: metoclopramida 10 mg IV en bolo lento (≥3 min) u ondansetrón 4 mg IV. Rehidrata con suero salino si vómitos.
- Evita los opioides como primera línea: no abortan la cefalea primaria, empeoran la náusea y cronifican.
- Si la TA es muy alta y hay sospecha de causa que lo exige (HSA, hemorragia, encefalopatía hipertensiva), controla la TA con labetalol o urapidilo IV (ver subsecciones); en la cefalea primaria no persigas la TA de forma agresiva.

A. CEFALEA TENSIONAL O INESPECÍFICA LEVE
- Paracetamol 1 g IV en 15 min cada 4-6 h, o 1 g VO cada 6-8 h (máximo 4 g/día; 2-3 g/día en ancianos o hepatópatas).
- O un AINE: dexketoprofeno 25 mg VO cada 8 h (máximo 75 mg/día) o 50 mg IV/IM cada 8-12 h (máximo 150 mg/día). Alternativas VO: ibuprofeno 400-600 mg, naproxeno 500 mg, AAS 500-1000 mg.
- Si es muy frecuente (>15 días/mes) o muy limitante, recomendar al alta valorar preventivo con amitriptilina (iniciar 10 mg/noche, subir hasta 50-75 mg/noche); no se inicia en la guardia.

B. CRISIS DE MIGRAÑA
- AINE o paracetamol a las dosis anteriores (naproxeno 500-1000 mg VO, ibuprofeno 400-600 mg VO, dexketoprofeno 25 mg VO / 50 mg IV, o paracetamol 1 g) + metoclopramida 10 mg IV en bolo lento de ≥3 min (controla el dolor y la náusea); rehidrata con suero si hay vómitos.
- Si no responde al AINE: sumatriptán 6 mg SC (o 50-100 mg VO; repetir a las 2 h, máximo 12 mg/24 h SC o 200 mg/24 h VO). Alternativas VO: rizatriptán 10 mg liofilizado, eletriptán 20-40 mg, almotriptán 12,5 mg.
- ANTES del triptán comprueba que no haya cardiopatía isquémica, enfermedad cerebrovascular o vascular periférica, HTA no controlada ni embarazo, y que no haya tomado un ergótico u otro triptán en las últimas 24 h: en esos casos está CONTRAINDICADO y tratas solo con AINE + antiemético. En paciente con riesgo cardiovascular puede valorarse lasmiditán 50-200 mg VO (sin efecto vasoconstrictor; máximo 1 dosis/24 h, produce mareo) como alternativa donde esté disponible.
- ESTATUS MIGRAÑOSO (crisis >72 h pese a tratamiento): suero salino + metoclopramida 10 mg IV, y añade dexametasona 10 mg IV (rango 4-24 mg; reduce la recurrencia precoz) + ketorolaco 30 mg IV + sumatriptán 6 mg SC si no se ha usado en 24 h. Alternativa: valproato sódico 400-1000 mg IV. Opción no farmacológica útil (también en embarazo): bloqueo del nervio occipital mayor con lidocaína/bupivacaína.

C. CEFALEA EN RACIMOS / TRIGÉMINO-AUTONÓMICAS
- Oxígeno al 100 % a 12-15 l/min con mascarilla con reservorio durante 15-20 min (efectividad >70 %) + sumatriptán 6 mg SC (vía de elección por rapidez; máximo 2 dosis/día, con las mismas contraindicaciones cardiovasculares del apartado B). Alternativa si se quiere evitar la inyección: zolmitriptán nasal 5 mg.
- Tratamiento de transición/puente que puede pautarse para abortar el racimo: prednisona 60 mg/día VO durante 3-5 días con pauta descendente (reducir 10 mg cada 3 días; no prolongar >3 semanas), y/o bloqueo del nervio occipital mayor (GON) con anestésico local + corticoide.
- El preventivo de fondo (verapamilo, con ECG previo por riesgo de bloqueo AV) lo pauta Neurología; no se inicia en la guardia.

D. ARTERITIS DE CÉLULAS GIGANTES (ARTERITIS DE LA TEMPORAL)
NO esperes a la VSG ni a la biopsia: el corticoide se inicia ante la sospecha clínica. Pide VSG/PCR pero trata ya.
- ACG SIN afectación visual (cefalea, claudicación mandibular, arteria temporal patológica, VSG alta, SIN pérdida de visión): prednisona 40-60 mg/día VO (1 mg/kg/día), dosis única matutina. Descenso muy lento durante meses, pautado por Reumatología/Neurología.
- ACG CON afectación visual (amaurosis fugax, pérdida visual, diplopía) o ictus: bolos de metilprednisolona IV 0,5-1 g/día durante 3 días, seguidos de prednisona 1 mg/kg/día VO en descenso. Iniciar de inmediato, antes de la biopsia: la ceguera por isquemia óptica instaurada es IRREVERSIBLE.
- Asocia protección gástrica (IBP) y profilaxis ósea; el tocilizumab o el metotrexato (ahorradores de corticoide) los decide la consulta, no la guardia.
- Avisa a Oftalmología (valoración del fondo de ojo / neuropatía óptica) y deja constancia para que Reumatología programe la biopsia de arteria temporal (rentable hasta ~1 semana de corticoide).

E. HEMORRAGIA SUBARACNOIDEA
Confírmala con TC (y PL con xantocromía si TC normal y sospecha alta). En cuanto la sospeches firmemente:
- REPOSO ABSOLUTO en cama, cabecero a 30°, habitación tranquila y semioscura. Laxantes para evitar Valsalva (p. ej. lactulosa); antieméticos (ondansetrón o metoclopramida).
- ANALGESIA: paracetamol 1 g IV cada 6-8 h. EVITA los AINEs (alteran la función plaquetaria). Si dolor intenso: cloruro mórfico 2-4 mg IV titulado.
- CONTROL DE TA: objetivo TAS <160 mmHg hasta la oclusión del aneurisma (el vault recoge TAS 140-160 mmHg; trata si >180). Fármacos: labetalol 10-20 mg IV en 1-2 min (repetible cada 10-20 min, máx. 300 mg) o urapidilo 25 mg IV en bolo lento seguido de perfusión 5-40 mg/h. Evita descensos bruscos.
- NIMODIPINO 60 mg VO cada 4 h durante 21 días (prevención del daño isquémico tardío por vasoespasmo). Iniciar lo antes posible tras el diagnóstico. Si la vía oral no es posible, nimodipino IV (preferible por vía central).
- Profilaxis de crisis con levetiracetam: controvertida; razonable en el periodo perioperatorio.
- IMAGEN para localizar el aneurisma: angio-TC (o arteriografía si negativa con alta sospecha).
- AVISA URGENTE a Neurocirugía y pon en aviso a la UCI: objetivo ocluir el aneurisma (coiling endovascular de elección, o clipaje) en las primeras 24-72 h para prevenir el resangrado (máximo riesgo en las primeras 72 h).

F. MENINGITIS (BACTERIANA AGUDA) Y ENCEFALITIS
URGENCIA MÉDICA: inicia el tratamiento empírico en <1 hora. NO lo demores por esperar al TC o a la PL (si la PL se va a retrasar por contraindicación, extrae hemocultivos y trata). Orden práctico: dexametasona inmediatamente antes o junto con la primera dosis de antibiótico.
- DEXAMETASONA 0,15 mg/kg IV cada 6 h durante 4 días, administrada previa o concomitante al antibiótico (reduce secuelas, sobre todo sordera, en neumococo). Mantenla solo si se confirma neumococo.
- ANTIBIOTERAPIA EMPÍRICA IV según el perfil:
  → Adulto <50 años, sin factores de riesgo: ceftriaxona 2 g IV cada 12 h + vancomicina 15-20 mg/kg IV cada 8-12 h.
  → >50 años, embarazo, alcoholismo o inmunodepresión (cobertura de Listeria): añade ampicilina 2 g IV cada 4 h al esquema anterior (ceftriaxona + vancomicina + ampicilina).
  → Inmunodepresión grave / postneurocirugía / TCE penetrante (cobertura de bacilos gramnegativos y Pseudomonas): vancomicina + cefepime 2 g IV cada 8 h o meropenem 2 g IV cada 8 h (en lugar de ceftriaxona), + ampicilina si procede cubrir Listeria.
  → Alergia grave a betalactámicos: moxifloxacino 400 mg IV cada 24 h en lugar de la cefalosporina (+ vancomicina ± cotrimoxazol para Listeria).
- ENCEFALITIS (alteración de consciencia/conducta, crisis, foco temporal): añade aciclovir 10 mg/kg IV cada 8 h empíricamente ante cualquier sospecha, ANTES del resultado de la PCR (cubre VHS-1). Si no puedes descartar meningitis bacteriana concomitante, mantén también la antibioterapia empírica.
- MEDIDAS: estabilización hemodinámica y fluidoterapia de mantenimiento; aislamiento respiratorio las primeras 24 h si meningococo; vigilar SIADH; si HTIC, cabecero 30° y osmoterapia (ver apartado H).
- Quimioprofilaxis de contactos estrechos del caso meningocócico: ciprofloxacino 500 mg VO dosis única (o ceftriaxona 250 mg IM dosis única).

G. TROMBOSIS VENOSA CEREBRAL
Sospéchala en mujer joven, anticonceptivos, embarazo/puerperio, trombofilia, o cefalea con crisis/HTIC/foco. Confirma con angio-TC venoso o venografía-RM (dímero-D de apoyo).
- ANTICOAGULACIÓN: es el tratamiento fundamental y se inicia incluso si hay infarto venoso hemorrágico (a diferencia del ictus arterial). En fase aguda: heparina no fraccionada IV en bolo + perfusión ajustada a TTPA 60-80 s, o HBPM a dosis terapéutica (enoxaparina 1 mg/kg SC cada 12 h). La pauta concreta y la elección HNF vs HBPM, confírmalas con el adjunto/Neurología, pero la indicación es clara.
- HTIC asociada: cabecero a 30°; si papiledema amenazante con pérdida visual, PL evacuadora; acetazolamida 250-500 mg cada 12 h si patrón de HTIC. Si hidrocefalia obstructiva, DVE.
- Edema/herniación: manitol 20 % 0,25-0,5 g/kg IV; hiperventilación transitoria solo como puente; craniectomía descompresiva si infarto venoso extenso con herniación.
- CRISIS: levetiracetam (preferible por interacciones).
- TVC SÉPTICA (origen otógeno/sinusal): antibioterapia IV — ceftriaxona + metronidazol ± vancomicina — además de la anticoagulación.
- Retira el factor protrombótico (suspender anticonceptivos, retirar catéter yugular si es la causa).

H. HIPERTENSIÓN INTRACRANEAL (Y HTIC IDIOPÁTICA / PSEUDOTUMOR CEREBRI)
- MEDIDAS GENERALES de HTIC (aplican a cualquier causa): cabecero a 30° con cabeza en línea media; evitar hipotensión (mantener PPC ≥60 mmHg); normocapnia; tratar fiebre y dolor; usar suero salino (NO glucosado/hipoosmolar).
- HTIC IDIOPÁTICA (papiledema + cefalea + diplopía VI en mujer joven obesa, neuroimagen sin masa, PL con presión >250 mmH₂O): acetazolamida 250-500 mg VO cada 12 h (máximo 1000 mg/día; inhibe la producción de LCR), pérdida de peso, y PL evacuadora terapéutica si hay amenaza visual. Derivación lumboperitoneal o fenestración de la vaina del nervio óptico solo en casos graves/refractarios (no en la guardia).
- HTIC POR EFECTO MASA / EDEMA VASOGÉNICO PERITUMORAL: dexametasona, carga 4-16 mg IV → mantenimiento 4-16 mg/día (sin efecto mineralocorticoide, vida media larga). En herniación inminente, bolo 40-100 mg IV; puede potenciarse con furosemida 20 mg IV.
- HERNIACIÓN INMINENTE / HTIC REFRACTARIA (signos: tríada de Cushing —bradicardia + HTA + alteración respiratoria—, anisocoria, deterioro de consciencia): agentes hiperosmolares — manitol 20 % 0,5-2 g/kg IV en 15-30 min (osmolaridad objetivo <320 mOsm/L) o suero salino hipertónico 3 % 100-250 mL IV en 10-20 min (preferible si hipotensión). Hiperventilación a pCO₂ 30-35 mmHg solo como puente máximo 30 min. AVISA a Neurocirugía y UCI (evacuación/craniectomía/DVE según causa).

GLAUCOMA AGUDO DE ÁNGULO CERRADO
Ojo rojo doloroso, midriasis media arreactiva, córnea turbia, halos y visión borrosa, a menudo con náuseas/vómitos; PIO muy elevada. AVISA a Oftalmología URGENTE (es quien hará la iridotomía láser definitiva), pero inicia el tratamiento médico para bajar la presión sin demora:
- Acetazolamida 500 mg IV (o VO si no hay vía / no vómitos), seguida de 250 mg cada 6-12 h (máximo 1000 mg/día). Contraindicada en alergia a sulfamidas y en insuficiencia renal grave.
- Tópicos para bajar la PIO: timolol 0,5 % 1 gota (betabloqueante) + brimonidina 1 gota (alfa-agonista); espaciados unos minutos. Añadir corticoide tópico (dexametasona/prednisolona) 1 gota cada 15-30 min para la inflamación.
- Pilocarpina 2 % tópica 1 gota (mióticos que abren el ángulo); clásicamente se difiere hasta que la PIO baja algo, porque con PIO muy alta el esfínter está isquémico y responde mal — coordínalo con Oftalmología.
- Si la PIO no cede: manitol 20 % 1-2 g/kg IV en 30-60 min (osmótico).
- Posición: paciente en decúbito supino. Analgesia y antiemético según necesidad.
- Tratamiento DEFINITIVO: iridotomía periférica con láser por Oftalmología (y profiláctica en el ojo contralateral).


6- PERLAS PARA NO OLVIDAR

🔑 Cefalea en trueno = HSA hasta que se demuestre lo contrario. TC urgente y, si es normal con sospecha persistente, PL con xantocromía (≥6 h). Un TC normal no la descarta. Una vez confirmada: reposo, TAS <160, nimodipino 60 mg/4 h × 21 días, analgesia SIN AINEs y Neurocirugía urgente para ocluir el aneurisma en 24-72 h.

🔑 Meningitis: dexametasona 0,15 mg/kg/6 h justo antes o con el antibiótico, y ceftriaxona 2 g/12 h + vancomicina ya. Añade ampicilina 2 g/4 h si >50 años, embarazo, alcoholismo o inmunodepresión (Listeria). El antibiótico NO espera al TC ni a la PL: el retraso es lo que mata.

🔑 Cefalea de novo o progresiva en >50 años + arteria temporal dolorosa o claudicación mandibular = arteritis de células gigantes. Corticoide YA (prednisona 40-60 mg/día; bolos de metilprednisolona 0,5-1 g/día × 3 si hay pérdida visual), sin esperar a la VSG ni a la biopsia, para salvar la visión.

🔑 Trombosis venosa cerebral: mujer joven, anticonceptivos o puerperio, con cefalea progresiva + crisis o papiledema. Se anticoagula (HNF IV o enoxaparina 1 mg/kg/12 h) AUNQUE haya infarto venoso hemorrágico. No es "migraña del embarazo".

🔑 Glaucoma agudo: ojo rojo doloroso + midriasis media fija + halos. Acetazolamida 500 mg IV + timolol/brimonidina/corticoide tópicos (± pilocarpina coordinada con Oftalmo) + manitol si no cede, y Oftalmología urgente para la iridotomía láser. También pierde visión si se demora.

🔑 HTIC idiopática (mujer joven obesa, papiledema, diplopía VI): acetazolamida 250-500 mg/12 h + perder peso + PL evacuadora si amenaza visual. Ante signos de herniación (tríada de Cushing, anisocoria): manitol 20 % o suero salino 3 % y Neurocirugía/UCI.

🔑 "Distinta a las de siempre" o "la peor de mi vida" cambia el patrón: deja de tratar el dolor y estudia.

🔑 Evita los opioides en la cefalea. Empeoran la náusea, no abortan la migraña ni el racimo y cronifican (cefalea por abuso de medicación). En la migraña usa AINE + metoclopramida ± triptán; en el racimo, oxígeno 100 % a 12-15 l/min + sumatriptán 6 mg SC.

🔑 Comprueba las contraindicaciones cardiovasculares ANTES de dar un triptán. En cardiopatía isquémica, enfermedad cerebrovascular, HTA no controlada o embarazo, trata solo con AINE + antiemético (o valora lasmiditán donde esté disponible).

🔑 Piensa en el monóxido de carbono cuando varios convivientes tienen cefalea a la vez en invierno (brasero, calentador). Es un diagnóstico que se pasa por alto y se trata con oxígeno al 100 %.
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
1) Prioriza guías EUROPEAS (ESC) y ESPAÑOLAS (SEC, SEMES, GEMA, GALAXIA, SEPAR, SEN, SSC) cuando existan; usa AHA/ACC/GINA/GOLD como complemento y AVISA cuando la recomendación europea/española difiera de la americana (dosis, umbrales o fármacos).
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
3) El estilo es texto plano conciso de bolsillo, sin frontmatter ni referencias dentro de la guía: no lo marques como defecto. Esta guía SÍ detalla el tratamiento concreto (fármaco, dosis, vía e intervalo) por diagnóstico; revisa esas dosis y pautas a fondo, que es lo que más importa.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

MAREO Y VÉRTIGO

Lo primero NO es etiquetar el oído, es descartar el cerebro: un ictus de fosa posterior se disfraza de vértigo banal y mata si se va de alta. La clave no es CÓMO lo describe el paciente ("se mueve todo", "me voy a caer") —los pacientes describen fatal y solapan categorías— sino CUÁNDO le pasa (continuo de días vs. episódico) y QUÉ lo desencadena (postura, nada, bipedestación). Esa cronología te coloca en una de cuatro casillas, cada una con su exploración y su diferencial. La mayoría de los vértigos son periféricos y benignos, pero tu trabajo en los primeros minutos es identificar al ~10 % de los vértigos agudos continuos que son un ictus, y separar al que necesita una maniobra de reposición (curativa, sin fármacos) del que necesita la vía ictus. Esta guía te orienta mientras valoras y, si algo pinta a central, mientras avisas.


1- CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR
Toma constantes, glucemia capilar y MIRA LA MARCHA antes de sentarte a pensar. Mirada rápida de 10 segundos — avisa, y NO cierres el caso como periférico, si detectas cualquiera de estos:
- Cualquier focalidad neurológica: diplopía, disartria, disfagia, disfonía, hemiparesia, dismetría, alteración sensitiva cruzada (cara de un lado / cuerpo del otro), síndrome de Horner.
- Vértigo agudo CONTINUO (de >24 h, de días) con datos de centralidad en la batería HINTS: head-impulse NORMAL (paradójicamente, que el reflejo se conserve es lo SOSPECHOSO), nistagmo que cambia de dirección con la mirada o es vertical/torsional puro, o test of skew (cover test) positivo.
- Ataxia troncal grave: incapacidad para mantenerse SENTADO sin apoyo o para caminar, desproporcionada al vértigo. HINTS central + ataxia troncal grave ≈ 100 % sensibilidad para ictus (mejor que HINTS solo). Recuerda: ~50 % de los ictus cerebelosos NO tienen nistagmo → en ellos el HINTS no aplica y la MARCHA es tu única bandera.
- Cefalea o cervicalgia occipital súbita o intensa, NUEVA (sospecha de disección de arteria vertebral o hemorragia cerebelosa). Cefalea en trueno → descartar HSA.
- Hipoacusia SÚBITA unilateral acompañando al vértigo agudo: puede ser un infarto de AICA, no un problema de oído banal. AVISA.
- Factores de riesgo vascular (FA, HTA, diabetes, tabaquismo) con vértigo agudo persistente, o PRIMER episodio en >60 años con FRCV (sospecha de ictus vertebrobasilar).
- Alteración del nivel de consciencia o inestabilidad hemodinámica.
- Desviación forzada de la mirada conjugada, anisocoria o cualquier dato de oclusión de gran vaso / herniación.

Regla de oro: ante sospecha de causa central, AVISA; la estratificación y la decisión de código ictus las toma el adjunto, no tú. Si dudas, NO lo etiquetes de neuritis ni de VPPB. El head-impulse normal en un vértigo agudo continuo es para avisar, no para tranquilizarse.


2- QUÉ PREGUNTAR (anamnesis dirigida, <3 minutos)
Manda la CRONOLOGÍA y el DESENCADENANTE, no la descripción del síntoma. Olvida el viejo esquema "vértigo / presíncope / desequilibrio": genera más errores que aciertos. Pregunta "¿cuándo y por qué?", no "¿qué siente?".

1. TIEMPO (PATRÓN TEMPORAL) — la primera pregunta
- ¿Episódico recurrente (asintomático ENTRE crisis) o agudo y CONTINUO desde hace días? El cuadro continuo de días (síndrome vestibular agudo) es el que OBLIGA a descartar ictus.
- Si despertó con ello, indaga si ya estaba al acostarse.

2. DURACIÓN DEL EPISODIO — diferencial casi directo
- Segundos (<1 min) con cada movimiento de la cabeza, en salvas → VPPB.
- Minutos a horas (20 min – 12 h), recurrente con asintomático intercrisis → Ménière (con síntomas auditivos) o migraña vestibular.
- Minutos, brusco, con FRCV → AIT vertebrobasilar.
- Días continuo, monofásico → neuritis vestibular o ictus.
- Meses, fluctuante, sin spinning → MPPP (mareo postural perceptivo persistente). No es de guardia.

3. DESENCADENANTE (trigger) — debe ser OBVIO y REPRODUCIBLE
- Girar la cabeza, tumbarse, mirar arriba o agacharse, reproducible → VPPB.
- Al ponerse de pie → hipotensión ortostática / presíncope.
- Estímulo sonoro intenso (Tullio) o Valsalva → dehiscencia del canal superior.
- Espontáneo, sin disparador → neuritis, ictus, Ménière o migraña vestibular.
- OJO: un trigger no es lo mismo que un factor agravante. Casi todo vértigo empeora al mover la cabeza; eso NO lo convierte en posicional.

4. SÍNTOMAS ASOCIADOS (banderas diagnósticas)
- Hipoacusia, acúfenos o plenitud ótica FLUCTUANTE unilateral → Ménière.
- Hipoacusia SÚBITA con vértigo agudo continuo → infarto de AICA (central, avisa).
- Cefalea con foto/fonofobia o historia migrañosa conocida → migraña vestibular.
- Cualquier síntoma neurológico (diplopía, disartria, disfagia, debilidad, hormigueo cruzado) → central.
- Palidez, sudoración fría, "voy a desmayarme", oscurecimiento visual → presíncope cardiovascular u ortostático.
- Confusión + oftalmoplejía + ataxia → encefalopatía de Wernicke (alcohol, desnutrición, hiperémesis) → tiamina empírica.

5. ANTECEDENTES Y MEDICACIÓN
- Factores de riesgo cardiovascular, ictus/AIT previos, FA, migraña conocida.
- Episodios previos idénticos (un VPPB o un Ménière suelen repetir el mismo patrón).
- Fármacos ototóxicos (aminoglucósidos, sobre todo GENTAMICINA → vestibulopatía bilateral), antiepilépticos, sedantes. Revisa la receta electrónica.
- Traumatismo craneal reciente, viaje en barco prolongado (mal de débarquement).


3- QUÉ EXPLORAR (exploración dirigida, <2 minutos)
Recuerda: una exploración NORMAL no descarta enfermedad, y un head-impulse normal en el contexto equivocado es alarmante, no tranquilizador.

CONSTANTES Y ORTOSTATISMO
- Constantes completas, glucemia capilar y constantes ortostáticas: TA y FC en decúbito, y al 1.er y 3.er minuto de bipedestación. Caída de la sistólica ≥20 mmHg o de la diastólica ≥10 mmHg apoya hipotensión ortostática.

NEUROLÓGICO Y MARCHA (lo más rentable)
- Pares craneales, pruebas cerebelosas (dedo-nariz, talón-rodilla, disdiadococinesia), y MARCHA + Romberg SIEMPRE que sea posible. La incapacidad para caminar o para mantenerse sentado sin apoyo es BANDERA ROJA de ictus, aunque no haya nistagmo.

NISTAGMO (obsérvalo en posición primaria y en las miradas laterales)
- Periférico: unidireccional, horizontal (con leve componente torsional), bate siempre al mismo lado, sigue la ley de Alexander (aumenta al mirar hacia la fase rápida) y SE SUPRIME con la fijación visual.
- Central: vertical (downbeating/upbeating) o torsional PURO, o que CAMBIA de dirección con la mirada (gaze-evoked), y NO se suprime con la fijación.

DIX-HALLPIKE — para el vértigo POSICIONAL (segundos al mover la cabeza). Confirma VPPB de canal posterior. Paso a paso:
1. Paciente SENTADO en la camilla, con espacio para que la cabeza quede colgando del borde superior. Avísale de que va a provocar el vértigo unos segundos.
2. Gira la cabeza del paciente 45° hacia el lado que se explora (p. ej. derecho).
3. Túmbalo rápidamente a decúbito supino MANTENIENDO los 45° de rotación, dejando que la cabeza quede colgando ~20-30° por debajo del plano de la camilla (cuello en extensión).
4. Mantén la posición ≥30 s observando los ojos.
5. POSITIVO (canal posterior del oído declive): nistagmo torsional-vertical que bate hacia el suelo / hacia la frente (upbeating-torsional), con LATENCIA (aparece a los pocos segundos), de DURACIÓN BREVE (<1 min), FATIGABLE (disminuye al repetir) y acompañado de vértigo. Esa reproducibilidad ES el diagnóstico.
6. Sienta al paciente y repite hacia el lado contrario.
- Si el nistagmo NO tiene latencia, no se agota, es puramente vertical, cambia de dirección o no se acompaña de sensación vertiginosa → sospecha VPPB central / lesión de fosa posterior.
- Si Dix-Hallpike negativo pero clínica posicional clara, sospecha canal horizontal → test de giro supino (McClure): paciente en decúbito, gira la cabeza 90° a cada lado buscando nistagmo horizontal geotrópico (conductolitiasis) o apogeotrópico (cupulolitiasis).

HINTS — para el vértigo agudo CONTINUO con nistagmo espontáneo (NO sirve en el episódico ni si no hay nistagmo). Los tres componentes, e interpreta AL REVÉS de lo intuitivo:
- H — Head-Impulse Test (impulso cefálico): sujeta la cabeza, pide fijar la mirada en tu nariz y gírala rápido y poco (~10-20°) a un lado, observando si el ojo se queda fijo o hace una sacada de refijación. PERIFÉRICO (benigno) = ANORMAL (hay sacada de refijación, el VOR está dañado en ese laberinto). CENTRAL (peligro) = NORMAL (el ojo sigue clavado en la diana, VOR intacto → el problema no está en el oído).
- I — Nystagmus (nistagmo): PERIFÉRICO = unidireccional, horizontal, se suprime con la fijación. CENTRAL = cambia de dirección con la mirada, o es vertical/torsional puro.
- TS — Test of Skew (cover test alternante): tapa y destapa alternativamente cada ojo buscando una corrección VERTICAL al destapar. PERIFÉRICO = ausente. CENTRAL = skew presente (desviación vertical, desconjugación).
- Regla nemotécnica de centralidad: INFARCT (Impulse Normal, Fast-phase Alternating, Refixation on cover test). Si se cumple → CENTRAL.
- HINTS-plus: añade la audición. Hipoacusia súbita unilateral en este contexto NO tranquiliza → sugiere infarto de AICA (central).

OTOSCOPIA Y AUDICIÓN
- Otoscopia (descarta tapón, perforación, vesículas herpéticas en zona Ramsay-Hunt) y valoración grosera de la audición (frota dedos junto a cada oído).


4- QUÉ PRUEBAS PEDIR

- Glucemia capilar: en el minuto cero, descarta hipoglucemia como simulador.
- ECG de 12 derivaciones: si hay presíncope, palpitaciones o sospecha de causa cardiogénica (arritmia, bloqueo).
- Analítica básica (hemograma, bioquímica con iones): SOLO si la orientas (sospecha ortostática/deshidratación por vómitos, causa sistémica). En el vértigo periférico típico su rentabilidad es muy baja (en un estudio, 0 de 200 TC craneales hallaron causa en mareo aislado). Considera tiamina empírica si sospechas Wernicke.
- NEUROIMAGEN: la mayoría de los vértigos periféricos NO necesitan imagen. Si sospechas causa central (HINTS central, focalidad, ataxia troncal grave, hipoacusia súbita, cefalea/cervicalgia nueva, FRCV con vértigo persistente), la prueba es la RM con DIFUSIÓN (DWI), NO el TC. Indica e interpreta la RM con el adjunto.

Escalas de probabilidad clínica
- TiTrATE / ATTEST (enfoque, no puntuación): clasifica el síndrome vestibular por Timing (cronología) y Triggers (desencadenantes) ANTES de explorar, en cuatro casillas:
  • t-EVS (episódico desencadenado, seg-min, por postura) → VPPB, ortostatismo → Dix-Hallpike / ortostatismo.
  • s-EVS (episódico espontáneo, min-horas, sin trigger) → migraña vestibular, Ménière, AIT → diagnóstico por HISTORIA.
  • AVS (agudo continuo, >24 h, espontáneo) → neuritis (~90 %) vs. ictus fosa posterior (~10 %) → HINTS + marcha.
  • Crónico (semanas-meses) → PPPD, vestibulopatía bilateral → derivar, no urgencia.
- HINTS / INFARCT (solo en AVS con nistagmo espontáneo): INFARCT (Impulse Normal, Fast-phase Alternating, Refixation on Cover Test) = CENTRAL. Por explorador entrenado, sensibilidad ~95-100 % y especificidad ~90 % para ictus de fosa posterior, SUPERIOR a la RM-difusión en las primeras 24-48 h (la RM-DWI tiene hasta ~50 % de falsos negativos en infartos pequeños <48 h). HINTS-plus (con audición): sensibilidad ~99 %, especificidad ~84 %.
- ABCD2 (si se sospecha AIT vertebrobasilar): orienta el riesgo de ictus a corto plazo, pero un ABCD2 bajo NO descarta etiología vascular; completa siempre el estudio.

⚠ TRAMPAS COMUNES
- El TC craneal es casi inútil para la fosa posterior precoz (sensibilidad ~10-16 %): un TC normal NO descarta un ictus cerebeloso ni troncoencefálico. La prueba es la RM con difusión (repítela a las 48-72 h si la primera es negativa y la sospecha es alta).
- En el vértigo agudo continuo, un head-impulse NORMAL es SOSPECHOSO de central (justo lo contrario de lo intuitivo). No te tranquilices con él.
- ~50 % de los ictus cerebelosos NO tienen nistagmo → entonces el HINTS no aplica. Usa la MARCHA y la ataxia troncal: si no puede sentarse sin apoyo, es central hasta que se demuestre lo contrario.
- HINTS solo es válido en AVS CON nistagmo espontáneo y por explorador entrenado. Aplicarlo en un episódico (VPPB, Ménière) o sin entrenamiento da resultados engañosos.
- No etiquetes un vértigo de "periférico" o "neuritis" sin haber hecho el HINTS y mirado la marcha. El ictus cerebeloso mata si se va de alta.
- La hipoacusia súbita con vértigo agudo NO es un oído banal: puede ser un infarto de AICA.
- Los sedantes vestibulares son INÚTILES en el VPPB (se trata con maniobras) y, prolongados, FRENAN la compensación central y empeoran cualquier vértigo. Regla: ≤72 h y fuera.


5- MEDIDAS Y TRATAMIENTO SEGÚN SOSPECHA

MEDIDAS GENERALES DE SOPORTE
- Tranquiliza al paciente (la ansiedad amplifica el cuadro) y colócalo en posición cómoda, con la cabeza quieta si el vértigo es intenso.
- Monitoriza (TA, FC, SatO₂) si está muy vegetativo o hay sospecha central.
- Vía venosa periférica con sueroterapia (suero fisiológico) SOLO si vómitos importantes con riesgo de deshidratación; no es necesaria en el VPPB típico.
- Antieméticos si náuseas/vómitos: ondansetrón 4-8 mg IV/8 h es el PREFERIBLE en urgencias (poco sedante, no enmascara la exploración ni frena la compensación). Alternativa metoclopramida 10 mg IV/8 h (más sedante; bolo IV lento ≥3 min).
- Principio rector: los supresores vestibulares (sulpirida, dimenhidrinato, benzodiacepinas) son un parche de la fase aguda, NUNCA un tratamiento de fondo. Máximo 48-72 h. Lo que cura el vértigo periférico agudo es la REHABILITACIÓN VESTIBULAR precoz, no el fármaco.

A. VPPB (vértigo posicional paroxístico benigno)
El tratamiento es una MANIOBRA DE REPOSICIÓN, NO fármacos (la AAO-HNS recomienda explícitamente EN CONTRA de los supresores vestibulares en el VPPB). Cura en una o dos sesiones.

- CANAL POSTERIOR (~85 % de los VPPB) → MANIOBRA DE EPLEY, paso a paso (lado afecto = el que dio Dix-Hallpike positivo; ejemplo, oído derecho):
  1. Partiendo de la posición de Dix-Hallpike positiva: paciente en supino, cabeza colgando ~20-30° y rotada 45° HACIA el lado afecto (derecha). Mantén ~30-60 s o hasta que ceda el nistagmo.
  2. Sin incorporarlo, gira la cabeza 90° hacia el lado SANO (ahora 45° a la izquierda), manteniendo la extensión. Espera 30-60 s.
  3. Gira cabeza Y cuerpo otros 90° en el mismo sentido, de modo que el paciente quede en decúbito LATERAL izquierdo mirando hacia el suelo (~135° respecto al inicio). Espera 30-60 s; puede reaparecer nistagmo en la misma dirección (buena señal, "liberatorio").
  4. Incorpóralo a sedestación con la cabeza aún rotada, y al final lleva la barbilla ligeramente al pecho.
  - Cada posición se mantiene ≥30 s o hasta que cesen vértigo y nistagmo. Éxito 80-90 % en 1 sesión; si persiste, se puede repetir. Recurrencia ~36 % a 4 años. NO son necesarias restricciones posturales posteriores (sin beneficio demostrado).
  - Alternativa si el paciente no tolera la extensión cervical o tiene patología cervical: MANIOBRA DE SEMONT (preferible en estenosis cervical).

- CANAL HORIZONTAL (lateral) → si el Dix-Hallpike es negativo pero el giro supino (McClure) reproduce nistagmo horizontal:
  - MANIOBRA DE LEMPERT (barbacoa / BBQ roll): con el paciente en decúbito, se realizan giros sucesivos de 90° de toda la cabeza-cuerpo HACIA EL LADO SANO, completando 270-360°, hasta "rodar" el otolito fuera del canal. [Fuente: vault — Vértigo en Urgencias / Síntesis de Guías.]
  - Alternativa: maniobra de GUFONI (sobre todo en cupulolitiasis).

- NO dar sedantes vestibulares: son inútiles en el VPPB y, al frenar la compensación, lo empeoran. Como mucho, un antiemético puntual si hay vómito intenso.
- VPPB refractario a 3 maniobras correctamente realizadas → derivar a ORL / otoneurología.

B. NEURITIS VESTIBULAR (vértigo periférico agudo intenso, SVA periférico, SIN hipoacusia)
- SEDANTE VESTIBULAR solo en la FASE AGUDA y la mínima duración posible (24-72 h, NUNCA lo cronifiques): sulpirida (Dogmatil) 50-100 mg/8-12 h VO/IM/IV. Alternativa dimenhidrinato 50 mg/4-6 h VO/IM/IV (menos extrapiramidalismo; útil en mayores donde la sulpirida puede dar parkinsonismo).
- ANTIEMÉTICO si predominan náuseas/vómitos: ondansetrón 4-8 mg IV/8 h (preferible) o metoclopramida 10 mg IV/8 h.
- CORTICOIDE PRECOZ (controvertido, decisión con el adjunto): prednisona 1 mg/kg/día VO (máx. 80 mg) 5 días, seguida de pauta de descenso 5 días. Si intolerancia oral, metilprednisolona IV equivalente (1 mg prednisona ≈ 0,8 mg metilprednisolona). Evidencia: mejora la recuperación calórica precoz, pero la Cochrane NO demuestra beneficio sintomático a 12 meses → no es rutinario en todos los protocolos; sigue el de tu centro.
- Si lesiones herpéticas (vesículas, parálisis facial → Ramsay-Hunt): añadir aciclovir o valaciclovir VO.
- REHABILITACIÓN VESTIBULAR precoz: es lo que de verdad acelera la recuperación (ejercicios de fijación de mirada con giro cefálico). Empieza en cuanto remita lo peor de la fase aguda; suspender el sedante en cuanto sea posible para no frenar la compensación.

C. ENFERMEDAD DE MÉNIÈRE
- CRISIS AGUDA (debut o paciente conocido): controlar el vértigo y el vómito como cualquier crisis vestibular → sedante vestibular corto (sulpirida 50-100 mg o dimenhidrinato 50 mg) + antiemético (ondansetrón 4-8 mg IV). En el debut, confirmar el diagnóstico ambulatoriamente con audiometría.
- TRATAMIENTO DE FONDO (iniciar/ajustar, casi siempre ambulatorio):
  • Restricción de sal (<2 g/día de sodio) como medida base.
  • BETAHISTINA (Serc) 16 mg/8 h VO (hasta 24 mg/8 h en algunos esquemas) — efecto LENTO y profiláctico, NO sirve para cortar la crisis.
  • Diurético: en crisis/debut algunos protocolos asocian furosemida 40 mg/24 h o torasemida 5 mg/24 h (o una tiazida) como ahorro de líquido endolinfático.
  • Refractario → corticoide o gentamicina INTRATIMPÁNICA (ORL/otoneurología). Los esquemas intratimpánicos varían entre centros; confírmalos con tu protocolo.

D. MIGRAÑA VESTIBULAR (causa episódica espontánea más infradiagnosticada)
- CRISIS AGUDA: sedante vestibular corto si vértigo intenso (sulpirida o dimenhidrinato a las dosis de arriba) + antiemético. Puede usarse el tratamiento abortivo migrañoso habitual del paciente.
- PREVENCIÓN (ambulatoria, no de guardia): flunarizina 5-10 mg/24 h, topiramato 50-100 mg/día, propranolol o venlafaxina, según el caso; + rehabilitación vestibular. El diagnóstico es por HISTORIA (criterios Bárány: ≥5 episodios de vértigo de 5 min-72 h + historia migrañosa + ≥50 % con rasgos migrañosos) y la exploración suele ser normal.

E. AIT VERTEBROBASILAR (episódico espontáneo con FRCV)
- Vértigo breve (minutos) en paciente con FRCV, sin antecedente migrañoso, inicio brusco. Aunque ya esté asintomático, NO es un alivio: es una urgencia diagnóstica.
- Manejo como vía vascular: RM-difusión + angio (TSA/intracraneal), antiagregación o anticoagulación según etiología, y prevención secundaria. Comparte con el adjunto / Neurología.

F. CRISIS MUY INTENSA E INCAPACITANTE, REFRACTARIA
- De forma PUNTUAL y excepcional: diazepam 5 mg (rango 1-5 mg/12 h) VO o IV, o lorazepam 1-2 mg. Máximo 48 h. Vigila sedación y caídas, sobre todo en ancianos (las benzodiacepinas frenan la compensación y aumentan el riesgo de caída).

G. VÉRTIGO CENTRAL / SOSPECHA DE ICTUS (lo que de verdad importa)
- NO es un problema de fármaco antivertiginoso. El tratamiento es la VÍA ICTUS.
- Soporte (ABC, glucemia, monitorización), activar la vía ictus si está en ventana (trombólisis <4,5 h) y AVISAR a Neurología / adjunto SIN demora.
- NO des sedantes vestibulares: enmascaran la exploración y no aportan nada.
- Ingreso: el ictus cerebeloso puede edematizarse y producir hidrocefalia obstructiva / compresión de tronco en las primeras 48-72 h → vigilancia estrecha y Neurocirugía en aviso. Prevención secundaria una vez estable. Ver vía de Ictus Isquémico del hospital.


6- PERLAS PARA NO OLVIDAR

🔑 Manda el CUÁNDO y el QUÉ lo desencadena, no el "se mueve todo". El patrón temporal (continuo de días vs. episódico) y el disparador orientan mucho más que cómo describe el síntoma el paciente. TiTrATE: cuatro casillas, cada una con su exploración.

🔑 No etiquetes de "vértigo periférico" sin hacer el HINTS y MIRAR LA MARCHA. El ictus cerebeloso mata si se va de alta. Y recuerda los dos puntos ciegos: el head-impulse NORMAL en un vértigo agudo continuo es para AVISAR (no para tranquilizarse), y ~50 % de los ictus cerebelosos no tienen nistagmo (entonces manda la ataxia troncal: si no puede sentarse sin apoyo, es central).

🔑 El TC normal NO descarta ictus de fosa posterior (sensibilidad ~10-16 %). Si sospechas central, la prueba es la RM con DIFUSIÓN, y se repite a las 48-72 h si la primera sale negativa con alta sospecha.

🔑 VPPB = MANIOBRA, no pastillas. Dix-Hallpike para diagnosticar el canal posterior; Epley (4 posiciones, ≥30 s cada una) para tratarlo, con 80-90 % de éxito en una sesión. Para el canal horizontal, Lempert (barbacoa). Los sedantes vestibulares no sirven en el VPPB y frenan la compensación.

🔑 Sedante vestibular SOLO en la fase aguda de la neuritis y ≤72 h. Cronificarlo retrasa la recuperación; lo que cura es la rehabilitación vestibular precoz. En urgencias, prefiere el ondansetrón (no sedante, no enmascara la exploración) para las náuseas.

🔑 Hipoacusia SÚBITA + vértigo agudo continuo: piensa en infarto de AICA, no en oído banal. Avisa.

🔑 Vértigo + cefalea o cervicalgia occipital súbita y nueva: sospecha disección de arteria vertebral o hemorragia cerebelosa. Avisa.

🔑 Glucemia en el minuto cero y constantes ORTOSTÁTICAS (1 y 3 min). La hipoglucemia y la hipotensión ortostática son simuladores baratos de descartar antes de complicarse con maniobras.

🔑 Un "AIT vertebrobasilar" que ya cedió NO es un alivio: es una urgencia diagnóstica (RM-difusión + angio + prevención secundaria). "Mejora" no significa "resuelta".
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
1) Prioriza guías EUROPEAS (ESC) y ESPAÑOLAS (SEC, SEMES, GEMA, GALAXIA, SEPAR, SEN, SSC) cuando existan; usa AHA/ACC/GINA/GOLD como complemento y AVISA cuando la recomendación europea/española difiera de la americana (dosis, umbrales o fármacos).
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
3) El estilo es texto plano conciso de bolsillo, sin frontmatter ni referencias dentro de la guía: no lo marques como defecto. Esta guía SÍ detalla el tratamiento concreto (fármaco, dosis, vía e intervalo) por diagnóstico; revisa esas dosis y pautas a fondo, que es lo que más importa.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

AGITACIÓN PSICOMOTRIZ

Estado de hiperactividad física y mental descontrolada e improductiva de gran intensidad. Lo primero es tu seguridad y la del paciente; el diagnóstico viene después. Idea fija: toda agitación de inicio agudo, en un anciano o en alguien sin antecedentes psiquiátricos, es ORGÁNICA hasta que se demuestre lo contrario, y la organicidad puede matar (hipoglucemia, hipoxia, abstinencia alcohólica, sepsis, hemorragia intracraneal). Tu trabajo en los primeros minutos no es etiquetar el cuadro de "psiquiátrico", sino garantizar la seguridad, descartar lo orgánico tratable (empezando por la glucemia capilar) y calmar al paciente — el objetivo es CALMAR, no SEDAR. Nunca te quedes solo con el paciente, ten siempre una vía de salida a tu espalda, retira objetos que sirvan de arma y avisa a seguridad antes de entrar.


1- CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR
Mirada rápida de 10 segundos — avisa, sin quedarte solo, si detectas cualquiera de estos:
- Riesgo inminente de auto o heteroagresión, o necesidad de contención mecánica.
- Alteración del nivel de consciencia (somnolencia, estupor, obnubilación o fluctuación) o focalidad neurológica.
- Cualquier dato de agitación ORGÁNICA con riesgo vital: hipoglucemia, hipoxia (SpO2 <92%), traumatismo craneal, fiebre o sepsis, abstinencia alcohólica o de sedantes, intoxicación.
- Constantes alteradas: TAS <90 mmHg o shock, taquicardia >120 lpm, taquipnea, SpO2 baja, fiebre >38 °C o hipertensión extrema.
- Signos de hiperactividad autonómica grave en posible abstinencia alcohólica: TAS >150 mmHg + FC >100 lpm + sudoración profusa + temblor (riesgo de delirium tremens).
- Convulsión activa o reciente (la convulsión de abstinencia alcohólica precede al delirium tremens).
- Hipertermia + rigidez muscular + agitación tras antipsicótico → sospecha de síndrome neuroléptico maligno (urgencia vital).
- ECG con QTc largo (>500 ms) o cualquier alteración nueva que NO estuviera en electros previos: compara SIEMPRE y, si el cambio es nuevo, avisa antes de dar un antipsicótico.
- Intento autolítico de alta letalidad o ideación suicida estructurada subyacente a la agitación.
- Fracaso de la contención verbal y farmacológica.

Regla de oro: el primer episodio de agitación en un adulto mayor o sin antecedentes psiquiátricos es orgánico mientras no se demuestre lo contrario. Glucemia capilar a todos, siempre, y tiamina ANTES que glucosa en el alcohólico.


2- QUÉ PREGUNTAR (anamnesis dirigida, <3 minutos)
Pregunta al paciente y, sobre todo, a los acompañantes (a menudo el paciente no colabora). La meta es separar lo ORGÁNICO de lo PSIQUIÁTRICO.

1. INICIO Y CURSO
- Agudo o subagudo y fluctuante, con empeoramiento nocturno y alucinaciones visuales → ORGÁNICO (síndrome confusional agudo / delirium).
- Instauración más insidiosa, con psicopatología propia (delirios estructurados, alucinaciones auditivas) y sin alteración de la consciencia → PSIQUIÁTRICO.

2. ANTECEDENTES PSIQUIÁTRICOS VS. PRIMER EPISODIO
- La agitación psiquiátrica aparece en quien YA tiene patología psiquiátrica conocida (esquizofrenia, trastorno bipolar, trastorno de personalidad) y sin datos de organicidad.
- Un PRIMER episodio en un adulto mayor obliga a descartar causa orgánica. Ojo a la agitación MIXTA: paciente psiquiátrico conocido (o con deterioro cognitivo / retraso mental) descompensado por un evento somático.

3. TÓXICOS
- Consumo o abstinencia de alcohol (¿cuándo fue la última ingesta? La abstinencia arranca a las 6-12 h, las convulsiones a las 24-48 h y el delirium tremens a las 48-72 h).
- Consumo de estimulantes (cocaína, anfetaminas, alucinógenos) → agitación + midriasis + taquicardia + HTA + hipertermia.
- Abstinencia de benzodiacepinas u otros depresores del SNC.

4. FÁRMACOS
- Revisa la receta electrónica: benzodiacepinas, opioides, anticolinérgicos, corticoides, levodopa, digoxina como precipitantes de delirium o psicosis.
- ¿Antipsicótico reciente o cambio de dosis? (distonía aguda, acatisia, síndrome neuroléptico maligno).

5. ENFERMEDAD SOMÁTICA Y TCE
- Enfermedad conocida, diabetes (piensa en hipoglucemia), hepatopatía (encefalopatía hepática), nefropatía (uremia), infección activa (ITU y neumonía son las causas más frecuentes de delirium en el anciano).
- Traumatismo craneal reciente, incluso banal en anticoagulado (hematoma subdural).

6. RIESGO AUTOLÍTICO SUBYACENTE
- Si la agitación acompaña a un gesto o intento autolítico, registra intentos previos (factor de riesgo principal), planificación, letalidad y accesibilidad de los medios.


3- QUÉ EXPLORAR (exploración dirigida, <2 minutos)
Haz lo que la situación de seguridad permita, sin perder de vista la puerta.

GLUCEMIA Y CONSTANTES
- GLUCEMIA CAPILAR SIEMPRE: la hipoglucemia es la primera causa tratable y se corrige en segundos.
- Constantes completas: TA, FC, FR, SpO2 y temperatura. TODA alteración de constantes apunta a organicidad.

NIVEL DE CONSCIENCIA Y ORIENTACIÓN
- Busca fluctuación del nivel de consciencia, desorientación e inatención (pídele que diga los meses del año al revés). Su presencia define el delirium.

NEUROLÓGICO
- Focalidad neurológica (asimetría motora, pupilas, pares craneales), signos meníngeos si fiebre.
- Pupilas: midriasis (estimulantes, abstinencia), miosis (opioides), anisocoria (lesión estructural).

SIGNOS DE TÓXICOS O ABSTINENCIA
- Temblor, sudoración profusa, taquicardia, HTA (abstinencia alcohólica).
- Estigmas de hepatopatía (ictericia, arañas vasculares, ascitis), signos de venopunción, fetor enólico.

SIGNOS DE COMPLICACIÓN FARMACOLÓGICA
- Rigidez muscular "en tubo de plomo" + hipertermia + disautonomía → síndrome neuroléptico maligno.
- Contractura cervical/ocular sostenida tras antipsicótico → distonía aguda (tratar con biperideno).
- Inquietud motora subjetiva que no puede parar → acatisia.

DATOS DE ORGANICIDAD (resumen — su presencia obliga a descartar causa somática)
- Alteración del nivel de consciencia, desorientación, curso fluctuante, empeoramiento nocturno, alucinaciones VISUALES y constantes o exploración alteradas. Su AUSENCIA, en un paciente con antecedentes psiquiátricos, orienta a agitación psiquiátrica.


4- QUÉ PRUEBAS PEDIR
Si hay cualquier sospecha de organicidad (y casi siempre la hay en el primer episodio o en el anciano):
- Glucemia capilar (ya hecha) y, según el caso, glucemia venosa.
- Hemograma, función renal y hepática, iones (incluidos Na, K, Ca y Mg — la hipopotasemia y la hipomagnesemia favorecen el delirium tremens y prolongan el QTc).
- Nivel de etanol en sangre ante sospecha de intoxicación etílica.
- Hormonas tiroideas (TSH) si la exploración es anormal o no hay antecedentes psiquiátricos; CK si la agitación es franca (rabdomiólisis, sospecha de síndrome neuroléptico maligno).
- Tóxicos en orina, con test de embarazo cuando proceda (mujer en edad fértil: condiciona la elección del fármaco).
- ECG: mide el QTc ANTES de dar un antipsicótico y vuelve a controlarlo después. Compara con electros previos.
- Gasometría y amonio si lo orienta la clínica (hipoxia, hipercapnia, encefalopatía hepática).
- Sedimento de orina y radiografía de tórax en el anciano (ITU y neumonía son los precipitantes más frecuentes de delirium).
- TC craneal sin contraste si hay focalidad, traumatismo craneal, anticoagulación o cuadro no filiado.

Escalas de probabilidad clínica
- RASS (Richmond Agitation-Sedation Scale): cuantifica el nivel de agitación/sedación de +4 (combativo, violento) a -5 (no despertable); 0 = alerta y tranquilo. Úsala para titular la contención y monitorizar tras medicar (objetivo: paciente tranquilo y despertable, no estuporoso). RASS −3 a −5 tras medicar = sobresedación, busca causa.
- 4AT / CAM (cribado de delirium): el CAM exige inicio agudo + curso fluctuante Y inatención, MÁS pensamiento desorganizado O alteración del nivel de consciencia → delirium probable. El 4AT (alerta, orientación con AMT-4, atención con meses al revés, cambio agudo/fluctuante) ≥4 sugiere delirium.
- Criterios de organicidad: alteración de consciencia, desorientación, curso fluctuante, empeoramiento nocturno, alucinaciones visuales, edad avanzada, ausencia de antecedentes psiquiátricos, constantes o exploración anormales.
- CIWA-Ar (Clinical Institute Withdrawal Assessment for Alcohol, revisada — para la abstinencia alcohólica): 10 ítems (náuseas/vómitos, temblor, sudoración, ansiedad, agitación, alteraciones táctiles, auditivas y visuales, cefalea, orientación), 0-7 cada uno salvo orientación 0-4. Total 0-67. Interpretación: <8 = leve (suele no precisar fármaco); 8-15 = moderada (responde a dosis modestas de BDZ); >15 = grave (riesgo de convulsiones y delirium tremens, especialmente si TAS >150 o FC >100). Es la escala que guía la pauta de benzodiacepina "según síntomas".

⚠ TRAMPAS COMUNES
- Agitación aguda en anciano o sin antecedentes psiquiátricos = ORGÁNICA hasta que se demuestre lo contrario. No la etiquetes de "psiquiátrica" por comodidad ni la sedes sin descartar lo somático.
- Las benzodiacepinas EMPEORAN el delirium orgánico (lo prolongan y agravan)... SALVO en la abstinencia alcohólica o de sedantes y en la intoxicación por estimulantes, donde SON el fármaco de elección. Sé estricto con esta distinción: es el error de manejo más frecuente.
- No des un antipsicótico sin mirar el QTc, y no combines fármacos que lo prolonguen sin un ECG. Corrige antes la hipopotasemia y la hipomagnesemia.
- Haloperidol está CONTRAINDICADO en enfermedad de Parkinson y en demencia por cuerpos de Lewy (empeora el parkinsonismo y puede desencadenar un cuadro grave): usa un atípico (quetiapina).
- En el alcohólico, la TIAMINA va ANTES que la glucosa (la glucosa sin tiamina precipita la encefalopatía de Wernicke).
- El haloperidol como monoterapia en la abstinencia alcohólica es un error: baja el umbral convulsivo y no trata la hiperactividad gabaérgica. Es solo ADYUVANTE a la benzodiacepina.
- Hipoactivo no es "tranquilo y estable": el delirium hipoactivo (~50%, el más frecuente) se infradiagnostica como depresión y tiene PEOR pronóstico. No todo lo orgánico se agita.
- La agitación que aparece o empeora TRAS un antipsicótico puede ser acatisia (no más psicosis): subir la dosis lo empeora. Y la rigidez + fiebre tras antipsicótico es un síndrome neuroléptico maligno hasta que se descarte.


5- MEDIDAS Y TRATAMIENTO SEGÚN SOSPECHA

MEDIDAS GENERALES DE SOPORTE
- SEGURIDAD PRIMERO: área privada y libre de objetos-arma, distancia de seguridad, vía de salida a tu espalda, personal de apoyo/seguridad presente. Nunca a solas.
- El primer paso terapéutico SIEMPRE es la CONTENCIÓN VERBAL (desescalada): contacto ocular sin sostenerlo fijamente, tono bajo pero firme, una sola persona lidera la comunicación, interésate por el problema y ofrece ayuda. Especialmente útil en la agitación orgánica (en la que se altera la comprensión). El objetivo es CALMAR, no SEDAR.
- CORRIGE LO TRATABLE de inmediato: glucemia capilar a todos. Si sospechas alcoholismo o encefalopatía de Wernicke, TIAMINA 100 mg IV o IM ANTES de dar glucosa; después corrige la hipoglucemia. Oxígeno si SpO2 baja.
- OFRECE SIEMPRE LA MEDICACIÓN POR VÍA ORAL PRIMERO (construye alianza y evita la contención física); reserva la parenteral para cuando la rechace o sea inviable.
- Espera al menos 1 hora antes de repetir la dosis de un antipsicótico. Vigila el QTc antes y después de medicar. Ten a mano biperideno (distonía aguda) y flumazenilo (no de rutina; solo si sobresedación grave por BDZ y sin riesgo convulsivo).

A. AGITACIÓN PSIQUIÁTRICA
Paciente con antecedentes psiquiátricos y SIN datos de organicidad (esquizofrenia, manía, brote psicótico). En el primer episodio psicótico, deriva SIEMPRE a Psiquiatría tras descartar organicidad.
- DE ELECCIÓN, antipsicótico de SEGUNDA GENERACIÓN (eficacia similar al haloperidol con menos extrapiramidalismo):
  * Olanzapina 5-10 mg VO o IM (Manual Tabla 9; máx. 20 mg/24 h). Riesgo de hiperglucemia e hipotensión. En ancianos o insuficiencia renal, iniciar a 2,5-5 mg.
  * Aripiprazol 5-10 mg VO o IM (máx. 30 mg/24 h). No alarga el QTc y seda menos; principal efecto adverso la acatisia. No precisa ajuste en insuficiencia renal/hepática.
  * Risperidona 1-2 mg VO (máx. 6 mg/24 h); solución oral útil. En ancianos iniciar a 0,25-0,5 mg (Manual Tabla 9).
- ALTERNATIVA CLÁSICA, haloperidol 5 mg VO, SC o IV (Manual Tabla 9; máx. 100 mg/24 h). Baja el umbral convulsivo; riesgo de extrapiramidalismo y de prolongación del QTc (sobre todo IV y a dosis altas). Sigue siendo opción válida, en especial por vía parenteral.
- COMBINACIÓN CON BENZODIACEPINA para potenciar el efecto en agitación intensa (clásico "haloperidol + BDZ"): añade midazolam 7,5-15 mg/24 h (vida media ultracorta <6 h, útil en agitación intensa) o lorazepam. El diazepam y el clorazepato dipotásico son de elección por su disponibilidad parenteral.
- NO administres olanzapina IM y benzodiacepina IM a la vez: deja al menos 1 hora entre ambas (riesgo de hipotensión y depresión respiratoria/cardiorrespiratoria).

B. AGITACIÓN ORGÁNICA / DELIRIUM (síndrome confusional agudo)
Lo prioritario es IDENTIFICAR Y TRATAR LA CAUSA (la mnemotecnia FIND ME: Fármacos, Infección, Neurológico, Dolor/Deprivación, Metabólico, Entorno) — el fármaco sedante es solo un complemento cuando la agitación pone en riesgo la seguridad. Primera línea NO farmacológica siempre: reorientación, iluminación adecuada (luz de día / oscuridad de noche), familiar presente, devolver gafas/audífonos/dentadura, hidratar, evitar sondas y sujeción física innecesarias.
- ANTIPSICÓTICO a DOSIS BAJAS (el de elección; EVITA las benzodiacepinas porque empeoran el delirium):
  * Haloperidol 0,5-1 mg VO (o 0,5 mg IM si la VO es imposible); puede repetirse a los 20-30 min. Dosis máxima en el anciano 2-5 mg/día (la mínima eficaz). Vigila extrapiramidalismo y QTc.
  * En ancianos, alternativamente un atípico a dosis baja: aripiprazol 5-10 mg (no alarga el QTc), olanzapina 2,5-5 mg o risperidona 0,25-0,5 mg.
- HALOPERIDOL CONTRAINDICADO EN PARKINSON Y EN DEMENCIA POR CUERPOS DE LEWY → usa quetiapina 12,5-25 mg VO (menor efecto extrapiramidal) o clotiapina 10-20 mg VO.
- MELATONINA 2,5-5 mg por la noche en el anciano: regula el ciclo sueño-vigilia, sin riesgo relevante (medida coadyuvante, no de rescate agudo).
- REVISA Y RETIRA fármacos precipitantes: opioides (reduce o rota), anticolinérgicos, antihistamínicos, benzodiacepinas de vida media larga, corticoides e hipnóticos no imprescindibles.
- EXCEPCIÓN: si el delirium es por abstinencia alcohólica/de sedantes → ve al apartado C (la BDZ pasa a ser de elección).

C. ABSTINENCIA ALCOHÓLICA / DELIRIUM TREMENS
Aquí la BENZODIACEPINA SÍ es de elección (es la piedra angular: repone el tono gabaérgico). Objetivo: sedación ligera con el paciente DESPERTABLE, monitorizando constantes cada 15-30 min hasta que el cuadro ceda (~3 días). Guíate por la CIWA-Ar (pauta "según síntomas", que reduce dosis y duración frente a la pauta fija, siempre que puedas monitorizar con frecuencia).

TIAMINA antes que glucosa (prevención de Wernicke):
- Hospitalizado, profilaxis: 500 mg IV 1-2 veces/día durante 3 días.
- Sospecha de encefalopatía de Wernicke: 500 mg IV 3 veces/día durante 5 días + multivitamínicos.
- (Profilaxis ambulatoria leve: 100 mg/día VO 3-5 días.)

BENZODIACEPINA (elegir según función hepática):
- Diazepam (vida media larga, metabolitos activos; eficaz pero riesgo de acumulación/encefalopatía en hepatopatía avanzada):
  * Pauta según síntomas: 10-20 mg IV o VO cada 1-4 h según necesidad.
  * Pauta de carga/escalada: 5 mg IV (a 2,5 mg/min) → si precisa, 10 mg a los 10 min → si precisa, 10 mg a los 10 min → si precisa, 20 mg a los 10 min → continuar a 5-20 mg/h según necesidad.
- Lorazepam (vida media corta, SIN metabolitos activos → PREFERIBLE en hepatopatía, ancianos y EPOC):
  * 1-4 mg IV cada 5-15 min según necesidad; alternativamente 1-40 mg IM cada 30-60 min.
  * Pauta de carga: 8 mg IV/IM/VO cada 15 min según necesidad; tras 16 mg, si persiste el delirium, bolo de 8 mg y luego 10-30 mg/h.

MANEJO DE LA HIPERACTIVIDAD AUTONÓMICA Y CASOS REFRACTARIOS:
- Sueroterapia: el alcohólico se hipohidrata y pierde electrolitos. Reposición con cristaloides y corrección de hipopotasemia, hipomagnesemia e hipofosfatemia (la hipomagnesemia favorece convulsiones y arritmias).
- Haloperidol SOLO como ADYUVANTE (nunca monoterapia) para agitación o alucinosis refractaria a BDZ: 0,5-5 mg IV o IM cada 30-60 min (máx. 20 mg), o 0,5-5 mg VO cada 4 h (máx. 30 mg). Recuerda que baja el umbral convulsivo y prolonga el QTc.
- Refractario en UCI: fenobarbital (hasta 1500-2000 mg VO o IV el día 1), dexmedetomidina (agonista α2, hasta 0,7 µg/kg/h IV, controla la disautonomía sin deprimir la respiración; contraindicada en bloqueo cardíaco) o propofol (0,3-1,25 mg/kg IV, hasta 4 mg/kg/h ≤48 h) en el paciente intubado.
- La muerte en el delirium tremens viene de hipertermia, arritmias, complicaciones de las convulsiones o comorbilidad. La intervención precoz reduce la mortalidad (1-4%). Hospitaliza si: convulsiones de abstinencia previas, comorbilidad médica/psiquiátrica, dependencia de BDZ o entorno inseguro.

D. INTOXICACIÓN POR ESTIMULANTES (cocaína, anfetaminas)
Cuadro de agitación + hiperactividad simpática (taquicardia, HTA, midriasis, hipertermia, diaforesis).
- BENZODIACEPINA de elección (controla agitación, taquicardia, HTA e hipertermia y baja el riesgo convulsivo): diazepam 2,5-10 mg VO o IV (repetir según respuesta) o lorazepam 1-4 mg IV/IM/VO; midazolam IM/IV si se necesita una vía rápida.
- EVITA los antipsicóticos como primera línea (bajan el umbral convulsivo, alteran la termorregulación y prolongan el QTc); resérvalos como adyuvante si hay psicosis franca pese a BDZ adecuada.
- EVITA los betabloqueantes en cocaína (riesgo clásico de estimulación alfa sin oposición e HTA paradójica).
- Medidas físicas de enfriamiento si hipertermia; sueroterapia; vigila CK (rabdomiólisis) y el ECG.

E. CONTENCIÓN MECÁNICA (inmovilización terapéutica)
Es el ÚLTIMO RECURSO, solo cuando la contención verbal y la farmacológica han fracasado y persiste el riesgo de auto/heteroagresión. Tiene implicaciones médico-legales: requiere indicación y registro médicos.
- Personal suficiente y entrenado (idealmente ≥4-5 personas, una por extremidad y otra que dirige); sujeción homologada en los puntos de anclaje.
- Acompáñala SIEMPRE de contención farmacológica y de un plan para retirarla en cuanto sea posible.
- MONITORIZACIÓN continua mientras dure: constantes, nivel de consciencia (RASS), estado de la piel y la circulación distal de los miembros sujetos, revisión periódica; vigila la vía aérea y evita el decúbito prono prolongado.
- Profilaxis de complicaciones del encamamiento (TVP) y reevaluación frecuente de la indicación.

Vigila SIEMPRE el QTc antes y después de cualquier antipsicótico (haloperidol, olanzapina y risperidona lo prolongan; el aripiprazol es el más seguro a este respecto) y no combines dos fármacos que lo alarguen sin un ECG y sin haber corregido el potasio y el magnesio.


6- PERLAS PARA NO OLVIDAR

🔑 Tu seguridad primero: vía de salida a tu espalda, retira objetos-arma, avisa a seguridad y nunca te quedes solo con el paciente.

🔑 Agitación aguda en anciano o sin antecedentes psiquiátricos = ORGÁNICA hasta que se demuestre lo contrario. Y la organicidad puede matar.

🔑 Glucemia capilar a TODOS. La hipoglucemia es la primera causa tratable y se corrige en segundos.

🔑 Contención verbal SIEMPRE primero. El objetivo es CALMAR, no SEDAR; la desescalada funciona incluso en el delirium, y ofrece la medicación VO antes que la parenteral.

🔑 En el delirium orgánico, EVITA las benzodiacepinas (lo empeoran) y usa antipsicótico a dosis baja. La EXCEPCIÓN es la abstinencia alcohólica/de sedantes y la intoxicación por estimulantes, donde la benzodiacepina ES de elección.

🔑 Abstinencia alcohólica: BENZODIACEPINA guiada por CIWA-Ar (lorazepam si hepatopatía, diazepam si no) + tiamina + sueroterapia + corregir K y Mg. El haloperidol solo como adyuvante, nunca solo (baja el umbral convulsivo).

🔑 Tiamina ANTES que la glucosa en el alcohólico, para no precipitar una encefalopatía de Wernicke.

🔑 Mide el QTc antes y después de dar un antipsicótico, corrige antes K y Mg. Y recuerda: haloperidol FUERA en Parkinson y en demencia por cuerpos de Lewy (usa quetiapina).

🔑 Rigidez + fiebre + disautonomía tras un antipsicótico = síndrome neuroléptico maligno hasta que se descarte. Y la inquietud que empeora al subir la dosis puede ser acatisia, no más psicosis.
```

---

## Prompt 9 — MUST Déficit Neurológico

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
1) Prioriza guías EUROPEAS (ESC) y ESPAÑOLAS (SEC, SEMES, GEMA, GALAXIA, SEPAR, SEN, SSC) cuando existan; usa AHA/ACC/GINA/GOLD como complemento y AVISA cuando la recomendación europea/española difiera de la americana (dosis, umbrales o fármacos).
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
3) El estilo es texto plano conciso de bolsillo, sin frontmatter ni referencias dentro de la guía: no lo marques como defecto. Esta guía SÍ detalla el tratamiento concreto (fármaco, dosis, vía e intervalo) por diagnóstico; revisa esas dosis y pautas a fondo, que es lo que más importa.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

DÉFICIT NEUROLÓGICO

Todo déficit neurológico agudo es un ictus hasta que se demuestre lo contrario. El tiempo es cerebro: cada minuto sin reperfusión se pierden ~1,9 millones de neuronas. Tu trabajo no es diagnosticar el tipo de ictus, es activar el código ictus y descartar hipoglucemia antes de que pasen 10 minutos desde la llegada.


1- CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR
Mirada rápida de 10 segundos — avisa si detectas cualquiera de estos:
- Glasgow ≤12 o deterioro del nivel de consciencia progresivo.
- Desviación forzada de la mirada conjugada (sugiere oclusión de gran vaso).
- Anisocoria con déficit motor contralateral (herniación).
- Déficit motor denso bilateral o tetraplejia aguda (ictus de tronco / compresión medular).
- Dificultad respiratoria con debilidad progresiva (crisis miasténica, Guillain-Barré).
- Convulsión activa o estado postictal prolongado (>20 min).
- TA sistólica >220 mmHg o <90 mmHg.
- FC <40 o >130 lpm.
- SatO₂ <92% sin respuesta a O₂.
- Fiebre >38,5 °C + rigidez de nuca + déficit focal (meningoencefalitis).

Regla de oro: si el paciente llegó bien y ahora "no está bien", avisa. No esperes a tener la prueba que lo confirme.


2- QUÉ PREGUNTAR (anamnesis dirigida, <3 minutos)

1. HORA DE INICIO / ÚLTIMA VEZ VISTO BIEN (LKW)
Es LA pregunta. Determina si el paciente es candidato a fibrinólisis (<4,5 h) o trombectomía (<24 h). Si despertó con el déficit, la LKW es la hora de acostarse (ICTUS DEL DESPERTAR → llamar a Neuro).

2. SITUACIÓN BASAL
¿Es independiente para las ABVD? Escala de Rankin modificada; generalmente no se activa código en pacientes dependientes (Rankin ≥3).

3. INSTAURACIÓN
- Súbita (segundos-minutos): CAUSA VASCULAR (ictus isquémico, hemorrágico, disección arterial).
- Progresiva (horas-días): CAUSA INFLAMATORIA, INFECCIOSA o TUMORAL (compresión medular, meningoencefalitis, Guillain-Barré, absceso, tumor).
- Fluctuante: AIT recurrente, crisis epiléptica, hipoglucemia.

4. ANTECEDENTES Y FÁRMACOS
- Fibrilación auricular (cardioembolia).
- Anticoagulantes (tipo, última dosis, hora) → condiciona la fibrinólisis.
- Antecedente de ictus previo, cirugía intracraneal <3 meses.
- Neoplasia activa (metástasis, compresión medular).
- Inmunosupresión (absceso, infección oportunista).
- Embarazo (trombosis venosa cerebral).

5. DESPISTAJE DE STROKE MIMICS (simuladores de ictus)
- Glucemia capilar: OBLIGATORIA en el minuto cero. La hipoglucemia es el principal simulador de focalidad. Si <60 mg/dL, corregir inmediatamente y reevaluar antes de activar el código.
- Crisis epiléptica / parálisis de Todd: antecedentes de epilepsia, testigos de crisis, focalidad postcrítica.
- Encefalopatía metabólica / infecciosa: desorientación, fluctuación o delirio (sobre todo en ancianos) → descartar foco infeccioso (respiratorio, urinario) o sepsis.
- Migraña con aura: paciente joven con antecedentes migrañosos y progresión típica (visual o sensitiva).

6. SÍNTOMAS ACOMPAÑANTES CLAVE
- Cefalea explosiva ("la peor de mi vida") → hemorragia subaracnoidea.
- Cefalea + dolor cervical + Horner → disección carotídea/vertebral.
- Vértigo + diplopía + disartria + ataxia → ictus de circulación posterior (no lo etiquetes de "vértigo periférico").
- Debilidad ascendente simétrica + arreflexia → Guillain-Barré.
- Dolor dorsal + nivel sensitivo + retención urinaria → compresión medular.
- Fiebre + confusión + déficit focal → meningoencefalitis / absceso.


3- QUÉ EXPLORAR (exploración dirigida, <2 minutos)

NEUROLÓGICO
- NIVEL DE CONSCIENCIA (Neuro pedirá que lo describas; Neurocirugía pedirá el Glasgow → siempre separar en O-V-M, ej. GCS 15 = O4V5M6).
- PUPILAS: tamaño, simetría, reactividad. Anisocoria = alerta máxima (pregunta antes si ya tenía el ojo así).
- LENGUAJE: afasia (no habla o no comprende) vs. disartria (habla mal pero comprende).
- PARES CRANEALES: paresia facial central (respeta frente) vs. periférica (afecta frente); desviación de la mirada; reflejo corneal si bajo nivel de consciencia.
- MOTOR: fuerza en 4 extremidades (Barré/Mingazzini). Asimetría = focalidad.
- SENSIBILIDAD: buscar nivel sensitivo (medular) o hemihipoestesia (hemisférica).
- COORDINACIÓN (cerebelo): dismetría dedo-nariz o talón-rodilla.
- MARCHA: siempre que sea posible.

COMPLETAR NIHSS: pasa la escala completa en cuanto sea posible. Orienta gravedad y elegibilidad terapéutica.

HINTS (solo si el motivo principal es vértigo agudo con nistagmo)
- Head-Impulse normal + nistagmo que cambia de dirección + skew deviation = CENTRAL (regla INFARCT). Sensibilidad ~94% para ictus de fosa posterior, superior a la RM precoz en las primeras 48 h.

CARDIOVASCULAR
- Auscultación: arritmia (FA), soplos carotídeos.
- TA en ambos brazos (diferencia >20 mmHg → disección aórtica/subclavia).

OTROS
- Signos meníngeos (Kernig, Brudzinski) si fiebre o cefalea.
- Fondo de ojo si sospecha de hipertensión intracraneal (papiledema).
- Piel: petequias, livedo reticularis (vasculitis, endocarditis).


4- QUÉ PRUEBAS PEDIR

- GLUCEMIA CAPILAR: OBLIGATORIA antes de activar código ictus. La hipoglucemia es el gran simulador. Corregir si <60 mg/dL.
- DESCARTAR OTROS STROKE MIMICS (sin retrasar la activación si el déficit es claro y el tiempo de evolución <4,5-6 h: el riesgo de demorar la reperfusión supera al de tratar un simulador).
- ANALÍTICA BÁSICA:
  *Hemograma, coagulación (INR, aPTT), bioquímica (glucosa, iones, creatinina), troponina.
  *Si toma anticoagulantes directos: niveles específicos o tiempo de trombina diluido / anti-Xa según el fármaco.
- ECG: buscar FA, IAM concomitante, QT largo.
- PRUEBAS DE IMAGEN:
  *TC craneal sin contraste: objetivo en <25 min desde la llegada. Descarta hemorragia. Un TC normal NO descarta ictus isquémico (sensibilidad 47-53% en las primeras 3 h). Signos precoces: hiperdensidad de ACM, borramiento de surcos, pérdida de diferenciación gris-blanca.
  *Angio-TC de troncos supraaórticos e intracraneal: si NIHSS ≥6 o sospecha de oclusión de gran vaso. No esperar a la creatinina si no hay antecedente de insuficiencia renal.
- OTRAS PRUEBAS SEGÚN SOSPECHA:
  *Perfusión TC o RM-DWI/perfusión: ventana 6-24 h para seleccionar candidatos a trombectomía (DAWN/DEFUSE-3).
  *RM cerebral con difusión: si TC normal y alta sospecha (sobre todo fosa posterior). La RM-DWI puede ser falsamente negativa en las primeras 24-48 h en ictus de tronco.
  *Punción lumbar: HSA con TC normal (>6 h desde la cefalea) o meningoencefalitis.
  *RM medular urgente: sospecha de compresión medular (nivel sensitivo + debilidad + retención urinaria).
  *EEG urgente: sospecha de estatus no convulsivo (déficit fluctuante, confusión sin causa clara).

Escalas de probabilidad clínica
- NIHSS: 0-5 leve, 6-14 moderado, 15-24 grave, ≥25 muy grave. NIHSS ≥6 con oclusión de gran vaso = candidato a trombectomía.
- ASPECTS: ≥6 en TC = candidato a trombectomía en ventana <6 h.
- ABCD2 (si AIT): 0-3 bajo, 4-5 moderado, 6-7 alto riesgo de ictus a 90 días. Un ABCD2 bajo NO descarta etiología de alto riesgo (estenosis carotídea, FA): completa siempre el estudio vascular.

⚠ TRAMPAS COMUNES
- TC normal ≠ "no tiene ictus". Solo descarta hemorragia de forma fiable.
- Ictus de fosa posterior: el TC tiene muy baja sensibilidad. Si la clínica es sugestiva, pide RM.
- Paciente joven con cefalea + déficit focal: piensa en disección arterial, trombosis venosa cerebral, vasculitis.
- Déficit que "mejora" en urgencias: no des el alta sin estudio completo. Un AIT es una emergencia, no un alivio.


5- MEDIDAS Y TRATAMIENTO SEGÚN SOSPECHA

A. SOSPECHA DE ICTUS ISQUÉMICO
CONTROL DE TA:
- Candidato a fibrinólisis: TA <185/110 mmHg antes de iniciar alteplasa y <180/105 mmHg durante las 24 h siguientes.
- NO candidato a fibrinólisis: no tratar la TA salvo ≥220/120 mmHg; en ese caso, reducir un 15% en las primeras 24 h.
- Fármacos: labetalol 10-20 mg IV en 1-2 min (repetir cada 10-20 min, máx. 300 mg) o urapidilo 25 mg IV en bolo lento, seguido de perfusión 5-40 mg/h. Evita descensos bruscos.

Fibrinólisis IV (alteplasa):
- Dosis: 0,9 mg/kg (máx. 90 mg). El 10% en bolo IV en 1 min; el 90% restante en perfusión IV en 60 min.
- Ventana: ≤4,5 h desde LKW. Posible extensión a 9 h con selección por imagen (mismatch RM-DWI/FLAIR).
- Contraindicaciones absolutas principales: hemorragia intracraneal activa, HSA, cirugía intracraneal/espinal <3 meses, TCE grave <3 meses, sangrado activo interno, diátesis hemorrágica (plaquetas <100.000, INR >1,7, aPTT elevado), TA no controlable <185/110, HBPM a dosis terapéutica en las últimas 24 h.
- Ventana 3-4,5 h, exclusiones adicionales clásicas: >80 años, NIHSS >25, ictus previo + diabetes, anticoagulante oral (las guías AHA 2018 flexibilizan varios de estos criterios).
- Alternativa: tenecteplasa 0,25 mg/kg (máx. 25 mg) en bolo IV único, preferible en candidatos a trombectomía.

Trombectomía mecánica:
- Indicada si oclusión de gran vaso (ACI, ACM-M1) + NIHSS ≥6 + ASPECTS ≥6 + mRS previo 0-1 + punción <6 h.
- Ventana extendida 6-24 h: selección por perfusión TC/RM (DAWN o DEFUSE-3).
- No retrasar la alteplasa si el paciente es candidato a ambas: administra alteplasa y traslada a intervencionismo.

AIT o ictus menor (NIHSS ≤3-5) sin indicación de fibrinólisis:
- Doble antiagregación: AAS 300 mg + clopidogrel 300 mg (carga) VO, seguido de AAS 100 mg/d + clopidogrel 75 mg/d durante 21 días, luego monoterapia.
- Estatina de alta potencia (atorvastatina 80 mg) desde el inicio.
- Iniciar en las primeras 24 h. Si se administró alteplasa, esperar 24 h para antiagregar.

B. SOSPECHA DE HEMORRAGIA INTRACEREBRAL
- CONTROL DE TA: si TAS 150-220 mmHg → objetivo TAS 130-140 mmHg de forma rápida pero controlada (<1 h). Evita TAS <130 mmHg. Fármacos: labetalol o urapidilo IV en perfusión.
- REVERTIR ANTICOAGULACIÓN:
  *Acenocumarol/warfarina: vitamina K 10 mg IV lento + CCP (complejo protrombínico) 25-50 UI/kg IV.
  *Dabigatrán: idarucizumab 5 g IV (2 bolos de 2,5 g).
  *Rivaroxabán/apixabán/edoxabán: andexanet alfa (si disponible) o CCP 50 UI/kg.
  *Heparina: protamina 1 mg por cada 100 UI de heparina de las últimas 2-3 h (máx. 50 mg).
- Transfundir plaquetas si <100.000 (o <50.000 en candidato quirúrgico).
- VALORACIÓN NEUROCIRUGÍA URGENTE si: hematoma cerebeloso >3 cm, hidrocefalia, deterioro neurológico progresivo, hematoma lobar >30 mL accesible.
- Cabecero a 30°; osmoterapia (manitol 20% 0,25-1 g/kg IV o SSH 3%) si signos de HIC.

C. SOSPECHA DE HEMORRAGIA SUBARACNOIDEA
- MEDIDAS GENERALES: reposo absoluto, cabecero 30°, habitación tranquila, laxantes (evitar Valsalva).
- ANALGESIA: paracetamol 1 g IV/6 h. Evita AINEs. Si dolor intenso: cloruro mórfico 2-4 mg IV titulado.
- CONTROL DE TA: TAS <160 mmHg hasta oclusión del aneurisma (labetalol o urapidilo IV).
- NIMODIPINO 60 mg VO/4 h durante 21 días (prevención del vasoespasmo). Iniciar lo antes posible.
- IMAGEN: angio-TC o arteriografía urgente para localizar el aneurisma.
- Objetivo: ocluir el aneurisma (coiling o clipaje) en las primeras 24-72 h. PON EN AVISO a la UCI e interconsulta URGENTE a Neurocirugía.

D. SOSPECHA DE COMPRESIÓN MEDULAR
- CORTICOIDES → dexametasona IV: carga 10 mg IV en bolo, seguido de 4 mg IV/6 h (clásico en compresión medular maligna). En déficit motor rápidamente progresivo algunos protocolos usan dosis altas (hasta 100 mg IV inicial), sin superioridad clara demostrada.
- RM de columna completa urgente (con y sin contraste).
- INTERCONSULTA URGENTE a Neurocirugía y/o Oncología Radioterápica (radioterapia si metástasis con compresión).
- Sondaje vesical si retención urinaria.
- Profilaxis de TVP con HBPM (si no hay contraindicación hemorrágica).

E. CRISIS EPILÉPTICA / SOSPECHA DE ESTATUS EPILÉPTICO
1ª línea (minuto 0-5): benzodiacepinas.
  *Diazepam 0,15 mg/kg IV (máx. 10 mg/dosis), repetir una vez.
  *Midazolam 10 mg IM (si >40 kg) o 0,2 mg/kg IV/intranasal (máx. 10 mg).
  *O lorazepam 0,1 mg/kg IV (máx. 4 mg/dosis), repetir a los 10-15 min (máx. 8 mg total).
  *NO INFRADOSIFICAR por miedo a la depresión respiratoria: el riesgo de un estatus no tratado es mayor.
2ª línea (minuto 10-30): si persisten las crisis tras 2 dosis de benzodiacepina.
  *Levetiracetam 60 mg/kg IV (máx. 4.500 mg) en 10-15 min.
  *O ácido valproico 40 mg/kg IV (máx. 3.000 mg) en 10 min (evita en hepatopatía, embarazo, mitocondriopatía).
  *O lacosamida 200-400 mg IV en 15 min.
  *O fenitoína/fosfenitoína 20 mg/kg IV (máx. 1.500 mg) a ritmo ≤50 mg/min (fenitoína) o ≤150 mg EF/min (fosfenitoína). Monitoriza ECG (riesgo de arritmia e hipotensión).
3ª línea (estatus refractario, >30 min): IOT + sedación con propofol, midazolam en perfusión o tiopental. Ingreso en UCI. Monitorización EEG continua.

F. SOSPECHA DE GUILLAIN-BARRÉ
- Monitorización respiratoria estrecha (regla de los 20: FVC <15-20 mL/kg, PIM <30, PEM <40 → valorar IOT electiva). Telemetría continua (disautonomía).
- Inmunoglobulinas IV 0,4 g/kg/día durante 5 días (total 2 g/kg) o plasmaféresis (5 recambios en 10-14 días). Equivalentes; no se combinan.
- NO uses corticoides en monoterapia (ineficaces e incluso perjudiciales en GBS idiopático).
- Profilaxis de TVP (enoxaparina 40 mg/24 h SC). Analgesia neuropática (gabapentina, pregabalina). Bradicardia sintomática → atropina.
- Ingreso en UCI o semicríticos.


6- PERLAS PARA NO OLVIDAR

🔑 Glucemia antes que nada. La hipoglucemia imita cualquier déficit focal. Un Glucosmón puede "curar" un ictus que no lo era.

🔑 No etiquetes un vértigo como "periférico" sin hacer el HINTS. El ictus cerebeloso mata si se va de alta. El HINTS por explorador entrenado tiene sensibilidad ~94% para causa central, superior a la RM precoz (<48 h).

🔑 El TC normal no descarta ictus isquémico. Solo descarta hemorragia. Si la clínica es compatible, activa el código ictus igualmente.

🔑 "Mejora" no significa "resuelta". Un AIT es una urgencia diagnóstica (riesgo de ictus a 90 días hasta 17,8% con ABCD2 alto). Nunca des el alta sin estudio vascular completo.

🔑 No infradosifiques las benzodiacepinas en el estatus. Más de la mitad de los pacientes reciben dosis insuficientes; el estatus no tratado tiene mayor morbimortalidad que la depresión respiratoria por benzodiacepina bien dosificada.

🔑 Debilidad bilateral ascendente + arreflexia = Guillain-Barré hasta que se demuestre lo contrario. Vigila la función respiratoria.

🔑 Dolor de espalda + debilidad en piernas + retención urinaria en paciente oncológico = compresión medular. Dexametasona IV y RM urgente. Cada hora cuenta para preservar la deambulación.
```

---

## Prompt 10 — MUST Sepsis

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
1) Prioriza guías EUROPEAS (ESC) y ESPAÑOLAS (SEC, SEMES, GEMA, GALAXIA, SEPAR, SEN, SSC) cuando existan; usa AHA/ACC/GINA/GOLD como complemento y AVISA cuando la recomendación europea/española difiera de la americana (dosis, umbrales o fármacos).
2) Cíñete a la evidencia con cita; no inventes. Si algo es controvertido o sin consenso, dilo.
3) El estilo es texto plano conciso de bolsillo, sin frontmatter ni referencias dentro de la guía: no lo marques como defecto. Esta guía SÍ detalla el tratamiento concreto (fármaco, dosis, vía e intervalo) por diagnóstico; revisa esas dosis y pautas a fondo, que es lo que más importa.
4) Distingue «error real / cambio necesario» de «mejora opcional».
5) Señala también las OMISIONES peligrosas o de alto rendimiento que falten para un R1.
6) Termina con una lista priorizada de los 3-5 cambios más importantes.

Responde en español. Guía a revisar:

SEPSIS

El paciente con sospecha de infección que se deteriora. Tu objetivo en la puerta no es filiar el germen, sino reconocer la sepsis y el shock séptico, activar el Código Sepsis y completar el paquete de la primera hora (lactato, hemocultivos, antibiótico y fluidos) sin perder tiempo. Definiciones (Sepsis-3): sepsis es infección con disfunción orgánica (SOFA que sube ≥2 puntos sobre el basal); shock séptico es la sepsis que, pese a fluidos adecuados, necesita vasopresores para una TAM ≥65 y mantiene lactato >2. El diagnóstico es clínico: ningún biomarcador aislado lo confirma ni lo descarta.


1- CUÁNDO AVISAR YA AL ADJUNTO O RESIDENTE MAYOR
Constantes completas con SatO2, glucemia capilar, lactato y nivel de consciencia nada más entrar. Mirada rápida de 10 segundos — la sospecha de sepsis ya es motivo de aviso; no te quedes solo con el paciente si hay:
- Shock séptico: hipotensión (PAS <100 o TAM <65) o necesidad de vasopresores, o lactato >2 mmol/l pese a fluidos.
- Cribado positivo: qSOFA con 2 o más (FR ≥22, PAS ≤100, alteración mental con GCS <15) o NEWS2 ≥5 (o 3 puntos en un solo parámetro).
- Disfunción orgánica (criterios de aviso a UCI): PaO2/FiO2 <300; GCS <12; plaquetas <100.000; bilirrubina >2; creatinina >2 o diuresis <0,5 ml/kg/h en 2 h; lactato >2.
- Hipotermia <36 °C (mal pronóstico, frecuente en ancianos, alcohólicos y bacilos gramnegativos) o fiebre >40 °C.
- Púrpura o petequias (sospecha de meningococo): el antibiótico va INMEDIATO, no esperes a la punción lumbar.
- Inmunodeprimido o neutropénico febril, embarazada, portador de prótesis/catéter venoso central/sonda, o ADVP.
- Foco que exige control urgente (absceso, colangitis, pielonefritis obstructiva, fascitis necrotizante): avisa en paralelo a cirugía o intervencionismo.

Regla de oro: la sospecha de sepsis no se puntúa para decidir tú, se avisa. Para cribar usa NEWS2/SIRS mejor que el qSOFA aislado, pero ningún resultado de laboratorio justifica retrasar el antibiótico ni los fluidos.


2- QUÉ PREGUNTAR (anamnesis dirigida, <3 minutos)
La meta es encontrar el foco, pesar la gravedad y anticipar resistencias.

1. FOCO (repásalo uno a uno)
- Disuria o polaquiuria (urinario); tos, expectoración o disnea (respiratorio); dolor abdominal o diarrea (digestivo, biliar); cefalea con fotofobia o rigidez (meníngeo); dolor y enrojecimiento cutáneo (partes blandas); dolor lumbar o en fosa renal.

2. TIEMPO Y ESCALOFRÍOS
- Tiempo de evolución y escalofríos con tiritona franca (orienta a bacteriemia).

3. ESTADO INMUNE
- VIH, quimioterapia, corticoides, esplenectomía, trasplante, neutropenia.

4. DISPOSITIVOS Y FÁRMACOS
- Prótesis, sondas, catéter venoso central, ADVP; y el último antibiótico (ojo a la fiebre que persiste pese a amplio espectro).

5. RIESGO DE MULTIRRESISTENCIA O PSEUDOMONAS
- Colonización o infección previa por germen MDR, antibiótico de amplio espectro reciente, hospitalización prolongada o ingreso en unidad con alta resistencia, bronquiectasias o fibrosis quística.

6. SITUACIÓN BASAL Y VOLUNTADES ANTICIPADAS
- La fragilidad extrema, la demencia avanzada o la enfermedad terminal cambian el techo terapéutico (ver criterios de UCI antes de escalar).


3- QUÉ EXPLORAR (exploración dirigida, <2 minutos)
Recuerda: una exploración normal NO descarta sepsis.

CONSTANTES
- Completas con SatO2, lactato, glucemia y nivel de consciencia (ACVPU o Glasgow).

PIEL Y MUCOSAS
- Púrpura o petequias (búscalas activamente), ectima gangrenosa (Pseudomonas), celulitis o crepitación con dolor desproporcionado (partes blandas necrotizantes), puntos de venopunción, úlceras por presión.

FOCO
- Orofaringe, oídos y senos; auscultación cardiopulmonar (condensación, soplos nuevos); abdomen con Murphy y puñopercusión renal bilateral; signos meníngeos (rigidez de nuca, Kernig, Brudzinski); articulaciones (artritis séptica).

DISPOSITIVOS Y ZONAS OCULTAS
- Revisa los puntos de inserción de cualquier catéter o sonda y, según el caso, valora tacto rectal y exploración genital o perineal (gangrena de Fournier).


4- QUÉ PRUEBAS PEDIR

- Analítica: hemograma, función renal y hepática, iones, coagulación con dímero D y fibrinógeno (despistaje de CID), PCR y procalcitonina.
- Lactato y gasometría: >2 mmol/l es mal dato y ≥4 obliga a fluidos; vuelve a medirlo a las 2-4 h si estaba alto (busca su aclaramiento).
- Hemocultivos x2 ANTES del antibiótico, pero sin retrasarlo si hay shock.
- Cultivos dirigidos al foco: sistemático de orina y urocultivo, esputo, exudados, líquidos; antigenuria de neumococo y Legionella si foco respiratorio; punción lumbar si sospechas meningitis (ni el TC ni la punción retrasan el antibiótico ni la dexametasona).
- Imagen según foco: radiografía de tórax, ecografía o TC abdominal, ecografía urológica. Busca activamente un foco drenable.

Escalas de probabilidad clínica
- qSOFA: FR ≥22, PAS ≤100, alteración mental (GCS <15). ≥2 = mayor riesgo, pero su ausencia NO descarta sepsis.
- NEWS2 / SIRS: preferidos al qSOFA para cribar. NEWS2 ≥5 (o 3 puntos en un solo parámetro) = aviso.
- SOFA: la sepsis (Sepsis-3) es un aumento ≥2 puntos del SOFA sobre el basal por la infección.
- Criterios de disfunción orgánica / aviso a UCI: PaO2/FiO2 <300, GCS <12, plaquetas <100.000, bilirrubina >2, creatinina >2 o diuresis <0,5 ml/kg/h, lactato >2.
- Procalcitonina: >2 orienta a origen bacteriano y guía la SUSPENSIÓN del antibiótico, no su inicio.

⚠ TRAMPAS COMUNES
- Un lactato normal NO descarta sepsis; la hipotermia (<36 °C) es de mal pronóstico, no tranquiliza.
- La procalcitonina NO sirve para decidir iniciar el antibiótico.
- Ningún resultado de laboratorio ni prueba de imagen justifica retrasar el antibiótico ni los fluidos.
- Una exploración normal no descarta sepsis; el foco puede estar oculto (perineo, catéter, articulación).
- En el paciente frágil o terminal, pesa el techo terapéutico antes de escalar.


5- MEDIDAS Y TRATAMIENTO SEGÚN SOSPECHA

MEDIDAS GENERALES DE SOPORTE
- Marco de tiempo (SSC 2026): si hay shock séptico o sepsis probable, todo en la primera hora; si solo es posible sepsis sin shock, reevalúa y, si persiste la duda, antibiótico antes de las 3 h; difiere el antibiótico solo si la probabilidad de infección es baja.
- Monitoriza, coge dos vías de buen calibre, extrae analítica con hemocultivos y lactato, glucemia capilar, y oxígeno con objetivo de SatO2 94-98%.

Paquete de la primera hora:
1. Lactato (y repetir si >2).
2. Hemocultivos x2 antes del antibiótico.
3. Antibiótico empírico dirigido al foco, lo antes posible.
4. Cristaloides balanceados (Ringer lactato o Plasmalyte, mejor que salino fisiológico) 30 ml/kg si hipotensión o lactato ≥4; en obesidad (IMC >30) calcula sobre peso ajustado o ideal. Reevalúa con medidas dinámicas (elevación pasiva de piernas, ecografía de vena cava) y no cargues a ciegas.
5. Vasopresores si persiste la hipotensión: noradrenalina como primera línea (inicia 0,05-0,1 mcg/kg/min), pronto y por vía periférica de buen calibre. Objetivo TAM ≥65 (basta 60-65 si ≥65 años). Si no llegas, añade vasopresina 0,01-0,03 U/min y, después, adrenalina. Hidrocortisona 200 mg/día (50 mg/6 h) si el shock sigue dependiente de vasopresores. Dobutamina 2,5-20 mcg/kg/min si hay disfunción miocárdica (todo esto, con el adjunto).

Antibiótico empírico por foco (dosis IV de inicio; ajusta a función renal y a alergias):

A. RESPIRATORIO (NEUMONÍA)
- Ceftriaxona 2 g/24 h + azitromicina 500 mg/24 h.

B. URINARIO (UROSEPSIS)
- Ceftriaxona 2 g/24 h (o gentamicina 5-7 mg/kg/24 h).

C. INTRAABDOMINAL O BILIAR
- Ceftriaxona 2 g/24 h + metronidazol 500 mg/8 h (o piperacilina-tazobactam en monoterapia).

D. PIEL Y PARTES BLANDAS
- Si necrosante: cirugía urgente + amplio espectro + clindamicina (efecto antitoxina).

E. MENINGITIS
- Dexametasona 0,15 mg/kg JUSTO antes o con la primera dosis + ceftriaxona 2 g/12 h (dosis meníngea); añade ampicilina 2 g/4 h si >50 años o inmunodeprimido (Listeria).

F. FOCO DESCONOCIDO GRAVE O SHOCK
- Piperacilina-tazobactam 4,5 g/6 h o meropenem 2 g/8 h en perfusión extendida. Añade vancomicina o daptomicina/linezolid si sospechas SARM.

G. NEUTROPÉNICO FEBRIL
- Betalactámico antipseudomónico YA (piperacilina-tazobactam o cefepime 2 g/8 h), sin esperar.

COBERTURA DE PSEUDOMONAS O BGN MULTIRRESISTENTE
- Solo si hay factores de riesgo (colonización previa, amplio espectro reciente, ingreso prolongado, inmunodepresión). Betalactámico antipseudomónico (piperacilina-tazobactam, cefepime, ceftazidima o meropenem) ± amikacina 25 mg/kg/24 h; en sospecha de BLEE prioriza meropenem; para carbapenemasas (KPC u OXA-48) ceftazidima-avibactam (consulta con Infecciosas o Farmacia). Desescala en cuanto tengas el antibiograma.

CONTROL DEL FOCO
- Drena el absceso, retira el catéter o la sonda infectados y desbrida la necrosis, idealmente en las primeras 6 horas. El antibiótico no sustituye al control del foco.

REEVALUACIÓN
- A la 1.ª, 3.ª y 6.ª hora: objetivo TAM ≥65, diuresis >0,5 ml/kg/h, aclaramiento del lactato y mejora del relleno capilar. Si no responde, sospecha un foco no controlado, sube el soporte (vasopresina, hidrocortisona) y plantea la UCI.


6- PERLAS PARA NO OLVIDAR

🔑 La sepsis se reconoce y se activa, no se filia en la puerta. Tu trabajo es el paquete de la primera hora, no el germen.

🔑 Ningún resultado de laboratorio ni prueba de imagen justifica retrasar el antibiótico ni los fluidos. Un lactato normal no descarta sepsis.

🔑 Hemocultivos x2 ANTES del antibiótico, pero sin retrasarlo si hay shock. El tiempo es supervivencia.

🔑 Cristaloides balanceados (Ringer/Plasmalyte) 30 ml/kg si hipotensión o lactato ≥4, y reevalúa con medidas dinámicas; no cargues a ciegas.

🔑 Noradrenalina de primera línea, pronto y por vía periférica de buen calibre. No esperes a la central. Objetivo TAM ≥65.

🔑 El antibiótico no sustituye al control del foco: drena, retira el catéter, desbrida en las primeras 6 h.

🔑 La hipotermia es mal pronóstico, y en el paciente frágil o terminal pesa el techo terapéutico antes de escalar.

🔑 Petequias o púrpura = meningococo. Antibiótico inmediato, sin esperar a la PL.
```
