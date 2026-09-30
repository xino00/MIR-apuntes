"""Esquemas nativos del HTML, derivados únicamente de la revisión CRM existente."""
from html import escape
from bs4 import BeautifulSoup

IC = 'https://academic.oup.com/eurheartj/advance-article/doi/10.1093/eurheartj/ehag100/8766302'
ERC = 'https://academic.oup.com/eurheartj/advance-article/doi/10.1093/eurheartj/ehag098/8766283'
KDIGO = 'https://kdigo.org/wp-content/uploads/2026/09/KDIGO-CKM-Commentary-The-Kidney-in-the-Middle.pdf'
CARDIORENAL = 'https://kdigo.org/wp-content/uploads/2026/05/KDIGO-2026-Kidney-Disease-Heart-Failure-Controversies-Conference-Report-KI-Final.pdf'


def box(label, title, body, note='', kind=''):
    """Un nodo mantiene juntos la decisión, su explicación y su excepción."""
    return (f'<div class="flow-box {kind}"><span class="node-label">{label}</span>'
            f'<h4>{title}</h4><p>{body}</p>'
            + (f'<p class="node-note">{note}</p>' if note else '') + '</div>')


def arrow(label=''):
    return f'<div class="flow-link"><span>{label}</span><i aria-hidden="true"></i></div>'


def split(*nodes):
    return '<div class="flow-split" style="--branches:' + str(len(nodes)) + '">' + ''.join(
        '<div class="flow-branch">' + node + '</div>' for node in nodes) + '</div>'


def note(text, urgent=False):
    return f'<div class="graphic-note {"urgent-note" if urgent else ""}">{text}</div>'


def figure(number, key, title, subtitle, body, refs, text_anchor):
    citations = ' · '.join(f'<a href="{url}">{label}</a>' for label, url in refs)
    return f'''<section class="clinical-graphic" id="grafico-{key}" aria-labelledby="titulo-{key}" data-graphic="{key}">
      <header class="graphic-heading"><span class="graphic-number">{number:02d}</span><div><p class="graphic-kicker">Esquema clínico</p><h3 id="titulo-{key}">{title}</h3><p class="graphic-subtitle">{subtitle}</p></div></header>
      <div class="graphic-canvas">{body}</div>
      <div class="graphic-caption"><span>Síntesis del texto: {citations}.</span><a href="#{text_anchor}" class="read-detail">Leer desarrollo y excepciones</a></div>
    </section>'''


def network():
    connector = '''<div class="organ-connector" aria-hidden="true"><svg viewBox="0 0 50 40"><path d="M5 20H45 M12 13L5 20L12 27 M38 13L45 20L38 27"/></svg></div>'''
    organs = [
        ('metabolismo', 'Metabolismo', 'Adiposidad · glucemia · presión', 'Peso, HbA1c, presión y lípidos'),
        ('rinon', 'Riñón', 'Filtración · albuminuria · volumen', 'FGe, CAC, potasio y tendencia'),
        ('corazon', 'Corazón', 'Congestión · perfusión · función', 'Síntomas, exploración, ECG y eco'),
    ]
    cards = []
    for key, title, subtitle, measures in organs:
        cards.append(f'<button class="organ-node" type="button" data-organ="{key}" aria-pressed="false" aria-controls="organ-detail"><span class="organ-dot" aria-hidden="true"></span><strong>{title}</strong><span>{subtitle}</span><small>{measures}</small></button>')
    body = '<div class="organ-network">' + connector.join(cards) + '</div>'
    body += '''<div class="shared-path"><span>Inflamación</span><span>Disfunción vascular</span><span>Activación neurohormonal</span></div>
      <div id="organ-detail" class="organ-detail" aria-live="polite"><strong>Una evaluación integrada.</strong> Selecciona un componente para ver qué aporta a las decisiones. El marco CRM no sustituye el diagnóstico de cada enfermedad.</div>'''
    return figure(1, 'mapa-crm', 'Tres sistemas, una valoración conjunta', 'Las relaciones son bidireccionales; el tratamiento parte de diagnósticos concretos.', body,
                  [('KDIGO-CRM, fisiopatología', KDIGO), ('KDIGO IC/ERC', CARDIORENAL)], 'definiciones')


def matrix():
    rows = [('G1', '≥90'), ('G2', '60–89'), ('G3a', '45–59'), ('G3b', '30–44'), ('G4', '15–29'), ('G5', '&lt;15')]
    cols = [('A1', '&lt;30'), ('A2', '30–300'), ('A3', '&gt;300')]
    content = '<div class="matrix-scroll"><table class="ga-matrix"><caption>FGe (mL/min/1,73 m²) × CAC (mg/g)</caption><thead><tr><th scope="col">FGe ↓ / CAC →</th>'
    for a, val in cols:
        content += f'<th scope="col"><strong>{a}</strong><span>{val} mg/g</span></th>'
    content += '</tr></thead><tbody>'
    for g, val in rows:
        content += f'<tr><th scope="row"><strong>{g}</strong><span>{val}</span></th>'
        for a, a_val in cols:
            other = g in ('G1', 'G2') and a == 'A1'
            renal = g not in ('G1', 'G2')
            reason = ('No establece ERC sin otro marcador de daño.' if other else
                      'Filtrado y albuminuria alterados: confirmar cronicidad y causa.' if renal and a != 'A1' else
                      'Filtrado disminuido: confirmar cronicidad y causa.' if renal else
                      'Albuminuria aumentada: confirmar persistencia y causa.')
            label = 'Otros marcadores' if other else 'FGe + CAC' if renal and a != 'A1' else 'FGe' if renal else 'CAC'
            descr = f'{g} {a}. FGe {val} mL/min/1,73 m²; CAC {a_val} mg/g. {reason}'
            content += f'<td class="{"ga-open" if other else "ga-damage"}"><button type="button" data-ga-description="{escape(descr)}" aria-label="Explorar {g} {a}" aria-pressed="false" aria-controls="ga-detail"><strong>{g} {a}</strong><small>{label}</small></button></td>'
        content += '</tr>'
    content += '</tbody></table></div><p class="matrix-output" id="ga-detail" aria-live="polite">Selecciona una casilla para interpretar la combinación. La selección es un ejemplo educativo, no una valoración de un paciente.</p>'
    content += note('<strong>Cronicidad y causa:</strong> persistencia ≥3 meses u otros datos que demuestren cronicidad. Si se sospecha LRA, actuar sin esperar. El color distingue marcadores; esta matriz no calcula riesgo renal.')
    return figure(2, 'clasificacion-renal', 'Leer el filtrado junto a la albuminuria', 'Dos dimensiones distintas. G1/G2 y A1 no bastan para diagnosticar ERC.', content,
                  [('ESC/ERA, §3.1–3.2', ERC)], 'evaluacion')


def dm2():
    body = box('Entrada', 'DM2: primero, comorbilidad y estabilidad', 'FGe, CAC, HbA1c, potasio, presión, peso, IC y tratamiento real.', kind='entry')
    body += note('<strong>Salida urgente:</strong> inestabilidad o sospecha de cetoacidosis requieren evaluación inmediata; con iSGLT2 puede faltar una hiperglucemia intensa.', True)
    body += arrow('Las comorbilidades pueden coexistir')
    body += split(
        box('Si hay IC', 'Protección cardiaca', 'Priorizar iSGLT2 cuando corresponda y completar tratamiento de IC.', 'En IC/ERC, inicio según guía con FGe ≥20; revisar volumen y seguridad.'),
        box('Si hay ERC', 'Protección renal', 'Decidir con FGe y CAC aunque la HbA1c esté en objetivo.', 'Revisar RAAS y elegibilidad para finerenona o semaglutida; ver esquema 05.'),
        box('Obesidad / aterosclerosis', 'Evidencia del agente', 'Valorar peso y beneficio cardiovascular del fármaco concreto.', 'No extrapolar una indicación estudiada a todo el grupo ni a cualquier población.')
    )
    body += arrow('Después, resolver la necesidad glucémica restante')
    body += box('Integrar', 'Objetivo individual de HbA1c', 'Ajustar tratamiento según función renal, peso e hipoglucemias.', 'Metformina: FGe ≥30; reducir por debajo de 45. Protección orgánica y descenso de glucosa no son equivalentes.')
    body += arrow()
    body += box('Conducta final', 'Tratamiento con finalidad y control definidos', 'Medicamentos, cambios concretos, señales de alarma y fecha de revisión.', kind='outcome')
    return figure(3, 'dm2', 'Algoritmo 1 · Elegir por comorbilidad', 'Cada rama señala qué beneficio se busca; varias pueden aplicarse a la misma persona.', body,
                  [('ESC/ERA, §5.5–5.6', ERC), ('ESC-IC', IC)], 'algoritmo-1')


def confirm_ckd():
    body = box('Entrada', 'Medir FGe + CAC', 'Preferir CAC cuantitativo en primera orina de la mañana y revisar resultados anteriores.', kind='entry')
    body += note('<strong>Antes de esperar:</strong> deterioro brusco, oliguria, hiperpotasemia o sospecha obstructiva requieren evaluación de un proceso agudo.', True)
    body += arrow('¿FGe <60, CAC ≥30 u otro marcador de daño?')
    body += split(
        box('Sí', 'Confirmar y estudiar', 'Repetir lo inesperado según gravedad; descartar alteraciones transitorias.', 'Confirmar persistencia ≥3 meses, salvo datos previos o estructurales de cronicidad.'),
        box('No', 'No etiquetar ERC por G1/G2 A1', 'Sin otros marcadores, continuar cribado según riesgo.', 'Una enfermedad aguda o un hallazgo nuevo puede exigir revisar esta conclusión.')
    )
    body += arrow('Si se confirma ERC')
    body += box('Clasificar', 'Causa · categoría G · categoría A', 'Valorar patrón atípico y progresión. KFRE puede apoyar decisiones en G3–G5.', 'No esperar a un porcentaje de riesgo para derivar una sospecha de enfermedad renal específica.')
    body += arrow()
    body += box('Conducta final', 'Intervenir y fijar seguimiento o derivación', 'Documentar diagnóstico, tratamiento inicial, pruebas pendientes y próxima revisión.', kind='outcome')
    return figure(4, 'confirmacion-erc', 'Algoritmo 2 · De hallazgo a diagnóstico', 'Confirmar cronicidad no significa posponer la atención de una posible LRA.', body,
                  [('ESC/ERA, §3–5', ERC), ('KDIGO-CRM', KDIGO)], 'algoritmo-2')


def dm2_ckd():
    body = box('Entrada', 'DM2 + ERC confirmada, en situación estable', 'Revisar FGe, CAC, K, presión, volumen y tratamientos previos.', kind='entry')
    body += note('Si hay hipovolemia, LRA, hipotensión sintomática o hiperpotasemia relevante: estabilizar y programar la reconsideración del tratamiento.')
    body += '<p class="branch-legend">Capas de tratamiento · la secuencia se individualiza</p><div class="treatment-layers">'
    body += box('RAAS', 'IECA o ARA-II cuando esté indicado', 'Especialmente claros con diabetes, hipertensión y albuminuria.', 'No combinarlos entre sí. ARNI ya contiene bloqueo del receptor de angiotensina.')
    body += box('iSGLT2', 'FGe ≥20', 'Protección renal y cardiovascular, independientemente de HbA1c.', 'Comprobar producto, volumen, intercurrencias y riesgo de cetoacidosis.')
    body += box('Finerenona', 'FGe ≥25 + CAC ≥30 mg/g', 'K adecuado; evidencia renal sobre RAAS a dosis tolerada.', 'Un único ARM. No trasladar la pauta de finerenona de IC a DM2/ERC.')
    body += box('Semaglutida: tabla renal ESC/ERA', 'Dos poblaciones concretas', 'FGe 25–49 con CAC ≥100; o FGe 50–74 con CAC ≥300 mg/g.', 'La tabla 12 y el texto narrativo difieren. Se conserva aquí la tabla, sin ampliar la recomendación.')
    body += '</div>' + arrow('En paralelo')
    body += box('Integración', 'Glucemia · presión · lípidos · hábitos', 'Individualizar HbA1c y revisar metformina según filtrado; no perder protección por una HbA1c satisfactoria.')
    body += arrow()
    body += box('Conducta final', 'Prescripción específica y vigilancia', 'Definir K/FGe, tolerancia, necesidad de derivación y fecha de control. Las dosis regulatorias no se deducen del esquema.', kind='outcome')
    return figure(5, 'dm2-erc', 'Algoritmo 3 · Proteger riñón y corazón', 'FGe en mL/min/1,73 m². La indicación, la seguridad y el objetivo glucémico se valoran por separado.', body,
                  [('ESC/ERA, tabla 12 y figura 8', ERC)], 'algoritmo-3')


def diagnose_hf():
    body = box('Entrada', 'Sospecha de IC en consulta estable', 'Síntomas, exploración, antecedentes, ECG y diagnósticos alternativos.', kind='entry')
    body += note('<strong>Si hay compromiso respiratorio o circulatorio:</strong> salir del circuito programado y derivar urgentemente.', True)
    body += arrow('NT-proBNP: puntos de decisión ambulatorios, no diagnóstico aislado')
    body += '''<div class="threshold-strip">
      <div><span>&lt;50 años</span><strong>≥125</strong><small>pg/mL</small></div>
      <div><span>50–74 años</span><strong>≥250</strong><small>pg/mL</small></div>
      <div><span>≥75 años</span><strong>≥500</strong><small>pg/mL</small></div></div>
      <p class="threshold-context">BNP: ≥35 pg/mL. NT-proBNP &gt;2000 pg/mL: mayor riesgo, priorizar valoración.</p>'''
    body += split(
        box('Péptido elevado o sospecha alta', 'Ecocardiografía', 'También con péptido por debajo del corte si la sospecha persiste.', 'Si no hay acceso a péptidos, decidir el ecocardiograma por la valoración clínica.'),
        box('Valor bajo y menor sospecha', 'Revisar otras causas', 'Continuar evaluación clínica y seguimiento; reconsiderar si persisten o progresan los síntomas.', 'Obesidad puede reducir péptidos; edad, ERC y FA pueden elevarlos. Sin corte renal único.')
    )
    body += arrow('Integrar clínica y ecocardiografía')
    body += split(
        box('FEVI <50%', 'Fenotipo reducido', 'Con síntomas o signos de IC. Registrar FEVI exacta y trayectoria.'),
        box('FEVI ≥50%', 'Fenotipo conservado', 'Requiere clínica compatible y evidencia objetiva de alteración estructural o funcional.', 'Una FEVI conservada, aislada, no confirma ni excluye IC.')
    )
    body += arrow()
    body += box('Conducta final', 'Confirmar causa y tratar, o continuar el estudio', 'Coordinar Cardiología si se confirma IC o persiste una duda relevante; derivación urgente si aparece deterioro.', kind='outcome')
    return figure(6, 'diagnostico-ic', 'Algoritmo 4 · De la sospecha al ecocardiograma', 'La probabilidad clínica gobierna la interpretación de los péptidos.', body,
                  [('ESC-IC, §3.3, §5 y figura 4', IC), ('KDIGO IC/ERC', CARDIORENAL)], 'algoritmo-4')


def treat_hf():
    body = box('Entrada', 'IC sintomática confirmada y estable', 'FEVI exacta, volumen, perfusión, presión, pulso, FGe y K.', kind='entry')
    body += arrow('Seleccionar el fenotipo y conservar sus matices de evidencia')
    body += split(
        box('FEVI <50%', 'Tratamiento fundamental', '<span class="drug-line">iSGLT2</span><span class="drug-line">ARM esteroideo</span><span class="drug-line">Betabloqueante en estabilidad</span><span class="drug-line">IECA o ARNI; ARA-II si corresponde</span>', 'La base experimental para algunos grupos es menos directa en FEVI 41–49%.'),
        box('FEVI ≥50%', 'Protección y comorbilidad', '<span class="drug-line">iSGLT2</span><span class="drug-line">ARM apropiado</span><span class="drug-line">IECA/ARA-II/ARNI: recomendación más débil</span><span class="drug-line">Betabloqueante por otra indicación</span>', 'No atribuir a todos los grupos el mismo beneficio sobre mortalidad.')
    )
    body += note('<strong>Seguridad renal:</strong> el umbral de FGe 25 del ARM no esteroideo no se traslada a espironolactona. No combinar dos ARM; decidir con K, filtrado e indicación.')
    body += arrow('Para ambos fenotipos')
    body += box('Si hay congestión', 'Diurético de asa según respuesta', 'Aliviar síntomas y alcanzar euvolemia con control clínico y analítico.', 'Hipoperfusión, disnea grave o deterioro rápido requieren valoración urgente.')
    body += arrow()
    body += box('Conducta final', 'Titular · vigilar · mantener lo tolerado', 'Ajustes en torno a 1–2 semanas según vigilancia; evitar retirada rutinaria al mejorar la FEVI.', 'Sin vigilancia estrecha, los anexos aconsejan no duplicar dosis antes de 2 semanas. Mala evolución o posible dispositivo: Cardiología.', kind='outcome')
    return figure(7, 'tratamiento-ic', 'Algoritmo 5 · Tratar según FEVI y tolerancia', 'El límite diagnóstico de 50% no sustituye los umbrales específicos de ensayos o dispositivos.', body,
                  [('ESC-IC, tratamiento y S4–S9', IC), ('ESC/ERA, §6', ERC)], 'algoritmo-5')


def integrated():
    body = '<div class="integration-grid">'
    for label, title, body_text in [
        ('Cardiovascular', '¿Qué enfermedad existe?', 'IC, aterosclerosis, arritmia o valvulopatía; distinguir prevención primaria y secundaria.'),
        ('Renal', '¿Qué indican FGe y CAC?', 'Confirmar cronicidad, causa y categorías; valorar evolución y riesgo.'),
        ('Metabólico', '¿Qué necesita la persona?', 'Glucemia, adiposidad, nutrición, capacidad funcional e hipoglucemias.'),
        ('Seguridad', '¿Qué limita el tratamiento?', 'Presión, potasio, volumen, fragilidad, interacciones y capacidad de seguimiento.'),
    ]:
        body += box(label, title, body_text)
    body += '</div>' + arrow('Priorizar intervenciones con una indicación real')
    body += box('Unificar objetivos', 'Evitar eventos · controlar glucosa · aliviar síntomas', 'Un fármaco puede cubrir varias indicaciones. Esto no demuestra que todos sus beneficios sean equivalentes ni aditivos.', kind='entry')
    body += note('Sin DM2 ni IC, no extrapolar automáticamente iSGLT2 a FGe 45–59 y albuminuria inferior a las poblaciones estudiadas. Revisar la elegibilidad en el desarrollo.')
    body += arrow()
    body += box('Conducta final', 'Un plan compartido y ejecutable', 'Responsable, cambios prioritarios, pruebas, fecha de revisión y criterios de contacto o derivación.', kind='outcome')
    return figure(8, 'integracion', 'Algoritmo 6 · Integrar antes de añadir', 'Evaluar en paralelo evita que un órgano o una cifra oculte los demás problemas.', body,
                  [('ESC/ERA, §4–6 y §14', ERC), ('KDIGO-CRM', KDIGO)], 'algoritmo-6')


def purposes():
    body = '<div class="purpose-grid">'
    for index, title, objective, examples, caveat in [
        ('01', 'Pronóstico', 'Reducir eventos', 'IC, progresión renal o enfermedad aterosclerótica, según la indicación del tratamiento.', 'Una HbA1c satisfactoria no elimina una indicación de protección orgánica.'),
        ('02', 'Glucemia', 'Controlar exposición a glucosa', 'Objetivo individual, con atención a hipoglucemia y función renal.', 'Un buen hipoglucemiante no reemplaza automáticamente el tratamiento de IC/ERC.'),
        ('03', 'Síntomas', 'Aliviar congestión y limitación', 'Diurético ajustado a volumen y respuesta, además de las otras medidas apropiadas.', 'Mejoría sintomática no demuestra por sí sola beneficio sobre supervivencia.'),
    ]:
        body += f'<div class="purpose"><span class="purpose-index">{index}</span><h4>{title}</h4><strong>{objective}</strong><p>{examples}</p><p class="node-note">{caveat}</p></div>'
    body += '</div>' + note('Las tres finalidades pueden coexistir. Registrar para qué se prescribe cada medicamento ayuda a ajustar sin perder beneficios necesarios.')
    return figure(9, 'objetivos', 'Tres finalidades del tratamiento', 'Antes de cambiar una dosis, identificar qué objetivo cubre.', body,
                  [('ESC-IC, clasificación de tratamientos', IC), ('ESC/ERA, §5.5–5.6', ERC)], 'prescripcion')


def creatinine():
    body = box('Hallazgo', 'Creatinina en ascenso', 'Comparar con basal y revisar tiempo, volumen, presión, K, diuresis y cambios de tratamiento.', kind='entry')
    body += arrow('La conducta depende del contexto')
    body += split(
        box('Congestión + perfusión conservada', 'Evaluar respuesta de descongestión', 'Si mejora y el cambio es tolerable, no retirar automáticamente toda protección.', 'La tolerancia a cambios durante descongestión hospitalaria no es un umbral ambulatorio universal.'),
        box('Hipovolemia, pérdidas o hipotensión', 'Corregir el problema hemodinámico', 'Revisar diurético y fármacos implicados; individualizar la reposición y los ajustes.', 'No indicar líquidos indiscriminadamente sin comprobar congestión.')
    )
    body += note('<strong>No son equivalentes:</strong> creatinina +30% y FGe −30%. Interpretar la variable, la trayectoria y el contexto que especifica la fuente.')
    body += arrow()
    body += box('Conducta final', 'Mantener, ajustar o derivar con control definido', 'Oliguria, deterioro rápido, alteración electrolítica importante, hipoperfusión o causa incierta: evaluación urgente según gravedad.', kind='outcome')
    return figure(10, 'creatinina', 'Un resultado, decisiones distintas', 'La analítica se interpreta junto al volumen y a la perfusión.', body,
                  [('ESC/ERA, figura 8 y §6.4', ERC), ('KDIGO IC/ERC', CARDIORENAL)], 'descompensaciones')


def potassium():
    body = '''<p class="scale-label">Potasio en mmol/L · tramos de actuación, no una escala de seguridad automática</p>
    <div class="potassium-bands">
      <div class="potassium-band"><span>Elevado, pero</span><strong>&lt;5,5</strong><h4>Revisar causas y tendencia</h4><p>Medicación, función renal, suplementos y sales con K. No retirar toda protección por defecto.</p></div>
      <div class="potassium-band"><span>Entre</span><strong>5,5 y &lt;6,0</strong><h4>Revisión pronta por fármaco</h4><p>Corregir causas; reducir o pausar según agente y contexto. No mantener dosis completas automáticamente.</p></div>
      <div class="potassium-band urgent-band"><span>A partir de</span><strong>≥6,0</strong><h4>Valoración urgente</h4><p>ESC/ERA figura 8: detener IECA/ARA-II/finerenona. Revisar los demás agentes implicados y la gravedad.</p></div>
    </div>'''
    body += note('<strong>Con síntomas, alteraciones del ECG o deterioro:</strong> actuar urgentemente sin esperar a una revisión programada. Comprobar hemólisis no debe retrasar atención si el cuadro es concordante.', True)
    body += '''<details class="graphic-discrepancy" open><summary>Diferencia entre guía renal y anexos de IC</summary><p>ESC-IC S4 aconseja interrupción/consulta de IECA o ARA-II con K &gt;5,5. S8 propone reducir ARM si &gt;5,5 y suspender si &gt;6,0. ESC/ERA usa suspensión ≥6,0. El esquema conserva el límite inclusivo de 6,0 y exige decisión individual en el tramo intermedio.</p></details>'''
    body += arrow('Después de corregir causas y controlar K')
    body += box('Reevaluar', 'Reconsiderar indicación, dosis y reinicio', 'Un episodio reversible no debe convertirse en una retirada indefinida sin revisión.', kind='outcome')
    return figure(11, 'potasio', 'Potasio: del resultado a la conducta', 'Conservar beneficio requiere tratar el riesgo y las causas corregibles.', body,
                  [('ESC/ERA, figura 8', ERC), ('ESC-IC, S4 y S8', IC)], 'descompensaciones')


def timeline():
    body = '''<div class="follow-timeline">
      <div class="time-stop"><span class="time-pin" aria-hidden="true"></span><span class="node-label">Antes de empezar</span><h4>Situación basal</h4><p>Presión, volumen, pulso, FGe, K y tratamiento real. Los controles dependen del fármaco.</p></div>
      <div class="time-stop"><span class="time-pin" aria-hidden="true"></span><span class="node-label">Inicio / titulación</span><h4>Primeras semanas</h4><div class="time-window"><strong>1–2 semanas</strong><span>IC: revisión y controles según fármaco y cambio.</span></div><div class="time-window"><strong>1–4 semanas</strong><span>RAAS en ERC: K y FGe.</span></div></div>
      <div class="time-stop"><span class="time-pin" aria-hidden="true"></span><span class="node-label">Tras estabilización</span><h4>Seguimiento periódico</h4><div class="time-window"><strong>4–6 meses</strong><span>Analítica habitual en anexos de IC; adaptar visitas y controles.</span></div><p>ERC: frecuencia según G/A, evolución y complicaciones.</p></div>
    </div>'''
    body += '<div class="post-discharge"><strong>Después de ingreso por IC</strong><span>Seguimiento frecuente durante las <b>primeras 6 semanas</b>, con descongestión y optimización del tratamiento.</span></div>'
    body += note('<strong>Adelantar si cambia la clínica.</strong> Los intervalos no autorizan esperar ante deterioro, hipotensión, hiperpotasemia o posible LRA. Tras una pausa terapéutica, fijar revisión y criterios de reinicio.')
    return figure(12, 'seguimiento', 'Cuándo volver a evaluar', 'Ventanas de control según situación; no son una pauta idéntica para todos los fármacos.', body,
                  [('ESC-IC, §7, §11.6 y S4–S9', IC), ('ESC/ERA, figura 8', ERC)], 'seguimiento')


CSS = r'''
/* Una sola paleta, diagramas de texto y conectores; sin recursos de red. */
:root{--soft:#f7f7f8;--warm:#17212c;--diagram:#002fa7;--diagram-light:#eef2fb}
.hero{padding-top:40px}.hero .intro{margin-bottom:22px}.source-note{background:#f7f7f8;border-color:#17212c}.clinical-graphic{margin:30px 0 38px;border:1px solid #c5cfdf;background:#fff;scroll-margin-top:22px;font-size:14px;line-height:1.6;isolation:isolate;overflow-wrap:break-word}.graphic-heading{display:flex;gap:18px;align-items:flex-start;padding:22px 24px;border-bottom:1px solid #c5cfdf;background:#f7f7f8}.graphic-number{font-size:34px;line-height:1.05;font-weight:700;letter-spacing:-.04em;color:var(--diagram);min-width:42px;font-variant-numeric:tabular-nums}.graphic-kicker{font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:#536171;font-weight:700;margin:0 0 5px!important}.graphic-heading h3{font-size:22px;line-height:1.25;letter-spacing:-.018em;margin:0 0 6px!important;border:0;padding:0}.graphic-subtitle{font-size:13px;color:#536171;margin:0!important;max-width:none}.graphic-canvas{padding:26px 24px}.clinical-graphic p{max-width:none}.graphic-caption{padding:14px 24px;border-top:1px solid #d8dee8;font-size:11px;line-height:1.65;display:flex;flex-wrap:wrap;gap:8px 20px;justify-content:space-between}.graphic-caption .read-detail{font-weight:700;white-space:normal}.node-label{font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:#536171;font-weight:700;display:block;margin-bottom:7px}.flow-box{border:1px solid #bdc9dc;padding:17px 18px;background:white;position:relative;height:100%}.flow-box h4,.purpose h4,.potassium-band h4,.time-stop h4{font-size:17px;line-height:1.3;letter-spacing:-.012em;margin:0 0 9px;font-weight:700}.flow-box p{font-size:13px;margin:0;line-height:1.65}.flow-box .node-note,.node-note{font-size:12px!important;line-height:1.6!important;border-top:1px solid #d8dee8;padding-top:10px;margin-top:12px!important;color:#455366}.flow-box.entry{border-left:4px solid var(--diagram);background:#eef2fb}.flow-box.outcome{background:#002fa7;color:#fff;border-color:#002fa7}.flow-box.outcome .node-label{color:#e0e8fd}.flow-box.outcome .node-note{color:#fff;border-color:#6d89d3}.flow-link{position:relative;min-height:43px;display:flex;align-items:center;justify-content:flex-start;gap:16px;padding-left:calc(50% + 15px);font-size:11px;color:#536171;line-height:1.4}.flow-link>span{padding:8px 0}.flow-link i{display:block;position:absolute;left:50%;top:0;bottom:7px;width:1px;background:#7c90b5}.flow-link i:after{content:'';position:absolute;bottom:-1px;left:-4px;width:8px;height:8px;border-right:1.5px solid var(--diagram);border-bottom:1.5px solid var(--diagram);transform:rotate(45deg)}.flow-split{display:grid;grid-template-columns:repeat(var(--branches),minmax(0,1fr));gap:17px;position:relative;padding-top:23px}.flow-split:before{content:'';position:absolute;top:0;left:calc(50% / var(--branches));right:calc(50% / var(--branches));height:1px;background:#7c90b5}.flow-branch{position:relative;min-width:0}.flow-branch:before{content:'';position:absolute;top:-23px;left:50%;height:23px;border-left:1px solid #7c90b5}.flow-branch:after{content:'';position:absolute;top:-6px;left:calc(50% - 3px);height:6px;width:6px;border-right:1px solid var(--diagram);border-bottom:1px solid var(--diagram);transform:rotate(45deg)}.graphic-note{margin-top:18px;padding:12px 15px;border-left:3px solid var(--diagram);background:#f3f5fa;font-size:12px;line-height:1.7}.urgent-note{background:#17212c;border-color:#17212c;color:#fff}.branch-legend{font-size:11px;font-weight:700;color:#536171;margin:21px 0 10px!important}.treatment-layers,.integration-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.drug-line{display:block;padding:6px 0;border-bottom:1px solid #e0e5ee}.drug-line:last-child{border-bottom:0}
.organ-network{display:grid;grid-template-columns:minmax(0,1fr) 42px minmax(0,1fr) 42px minmax(0,1fr);align-items:center}.organ-node{display:flex;flex-direction:column;align-items:flex-start;min-width:0;min-height:174px;height:100%;padding:17px 15px;border:1px solid #afbdd4;border-radius:0;background:#fff;text-align:left;position:relative;font-size:12px;line-height:1.6;transition:background .15s}.organ-node strong{font-size:25px;letter-spacing:-.04em;line-height:1.2;margin:5px 0 10px;overflow-wrap:normal}.organ-node>span:not(.organ-dot){font-size:12px;color:#455366}.organ-node small{display:block;font-size:10px;margin-top:12px;color:#536171;line-height:1.5}.organ-dot{width:9px;height:9px;border:2px solid var(--diagram);border-radius:50%;display:block}.organ-node[aria-pressed=true]{background:var(--diagram-light);outline:2px solid var(--diagram);outline-offset:-2px}.organ-node[aria-pressed=true] .organ-dot{background:var(--diagram)}.organ-connector svg{display:block;width:100%;height:38px;stroke:var(--diagram);stroke-width:1.4;fill:none}.shared-path{display:flex;gap:12px 22px;flex-wrap:wrap;font-size:11px;color:#536171;border-top:1px solid #a8b8d0;margin:18px 0 0;padding-top:12px}.shared-path span{padding-left:11px;position:relative}.shared-path span:before{content:'';height:5px;width:5px;background:#6f82a6;position:absolute;left:0;top:7px}.organ-detail{border-top:1px solid #d8dee8;margin-top:13px;padding-top:14px;font-size:13px;min-height:66px}.organ-detail strong{color:var(--diagram)}
.visual-index{margin-top:22px;border-top:1px solid #d8dee8;padding-top:17px;scroll-margin-top:24px}.visual-index>h2{font-size:16px;margin:0 0 12px;padding:0;border:0;letter-spacing:0}.visual-index-links{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0;border-left:1px solid #d8dee8;border-top:1px solid #d8dee8}.visual-index-links a{display:flex;gap:10px;align-items:baseline;padding:9px 12px;border-right:1px solid #d8dee8;border-bottom:1px solid #d8dee8;text-decoration:none;color:#17212c;font-size:12px;line-height:1.5}.visual-index-links b{font-variant-numeric:tabular-nums;color:var(--diagram)}.visual-index-links a:hover{background:#eef2fb}.hero>.clinical-graphic{margin-bottom:26px}.hero .quick{display:none}.graphic-toggle{margin:0 0 10px}
.matrix-scroll{overflow-x:auto;width:100%}.ga-matrix{width:100%;min-width:430px;table-layout:fixed;border-collapse:separate;border-spacing:5px;margin:0;font-size:13px}.ga-matrix caption{text-align:left;font-size:12px;font-weight:700;padding-bottom:12px}.ga-matrix th,.ga-matrix td{border:0;padding:0;background:none!important;vertical-align:middle}.ga-matrix thead th{background:#f7f7f8!important;padding:11px 8px;text-align:left}.ga-matrix th strong{display:block;font-size:17px;line-height:1.2}.ga-matrix th span{display:block;font-size:11px;font-weight:400;margin-top:4px}.ga-matrix tbody th{padding:7px 8px;width:25%}.ga-matrix td button{display:block;width:100%;min-height:58px;padding:8px;text-align:left;border-radius:0;background:#edf2fc;border:1px solid #c1cfe7}.ga-matrix .ga-open button{background:#fff;border-style:dashed}.ga-matrix button strong{display:block;font-size:13px;color:#17212c}.ga-matrix button small{font-size:10px;line-height:1.4;display:block;color:#536171}.ga-matrix button[aria-pressed=true]{background:#002fa7;color:#fff;border-color:#002fa7}.ga-matrix button[aria-pressed=true] strong,.ga-matrix button[aria-pressed=true] small{color:#fff}.matrix-output{font-size:12px;margin:17px 0 0!important;background:#f7f7f8;padding:13px 15px;min-height:70px}
.threshold-strip{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0;border:1px solid #c1cfe7;background:#eef2fb;margin:0}.threshold-strip>div{padding:14px 18px;border-right:1px solid #c1cfe7}.threshold-strip>div:last-child{border:0}.threshold-strip span{display:block;font-size:12px;font-weight:700}.threshold-strip strong{display:block;font-size:34px;line-height:1.2;letter-spacing:-.04em;color:var(--diagram);font-variant-numeric:tabular-nums;margin:4px 0}.threshold-strip small{font-size:11px;color:#536171}.threshold-context{font-size:11px;color:#455366;margin:10px 0 25px!important}.purpose-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}.purpose{border-top:3px solid var(--diagram);padding-top:15px}.purpose-index{font-size:36px;line-height:1;letter-spacing:-.04em;color:var(--diagram);display:block;margin-bottom:15px}.purpose>strong{display:block;font-size:13px;margin-bottom:10px}.purpose>p{font-size:12px;margin:0;line-height:1.7}
.scale-label{font-size:12px;color:#536171;margin:0 0 13px!important}.potassium-bands{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border:1px solid #b8c5db}.potassium-band{padding:16px 16px 19px;border-right:1px solid #b8c5db;border-top:5px solid #afbfda}.potassium-band:nth-child(2){background:#eef2fb;border-top-color:#002fa7}.potassium-band:last-child{border-right:0}.potassium-band>span{font-size:11px;display:block;color:#536171}.potassium-band>strong{display:block;font-size:29px;line-height:1.2;letter-spacing:-.04em;margin:5px 0 19px;color:var(--diagram);white-space:nowrap}.potassium-band h4{font-size:15px}.potassium-band p{font-size:12px;margin:0;line-height:1.7}.potassium-band.urgent-band{background:#17212c;border-top-color:#17212c;color:#fff}.potassium-band.urgent-band>span,.potassium-band.urgent-band>strong{color:#fff}.graphic-discrepancy{margin-top:16px;font-size:12px;border:1px solid #bdc9dc;padding:12px 15px}.graphic-discrepancy summary{cursor:pointer;font-weight:700;line-height:1.6}.graphic-discrepancy p{margin:12px 0 0;line-height:1.75}.follow-timeline{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;padding-top:18px;position:relative}.follow-timeline:before{content:'';height:1px;background:#8ba0c4;position:absolute;left:0;right:0;top:4px}.time-stop{position:relative;padding-top:12px}.time-pin{position:absolute;width:9px;height:9px;border:2px solid #002fa7;background:#fff;top:-18px;left:0;border-radius:50%}.time-stop>p{font-size:12px;line-height:1.7;margin:0}.time-window{border-top:1px solid #d8dee8;padding-top:9px;margin:12px 0}.time-window strong{display:block;font-size:18px;color:var(--diagram);line-height:1.3}.time-window span{display:block;font-size:12px;line-height:1.65;margin-top:4px}.post-discharge{margin-top:24px;border:1px solid var(--diagram);border-left:5px solid var(--diagram);padding:13px 16px;display:flex;flex-wrap:wrap;gap:5px 24px;font-size:12px}.post-discharge>strong{color:var(--diagram)}
@media(max-width:1050px) and (min-width:721px){.graphic-canvas{padding:22px 18px}.graphic-heading{padding:20px 18px}.organ-network{grid-template-columns:minmax(0,1fr) 25px minmax(0,1fr) 25px minmax(0,1fr)}.organ-node{padding:13px 10px}.organ-node strong{font-size:21px}.flow-box{padding:14px}.flow-box h4{font-size:15px}.flow-split{gap:12px}.potassium-band{padding:14px 11px}.potassium-band>strong{font-size:24px}.purpose-grid{gap:14px}.visual-index-links{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:720px){.hero{padding-top:30px}.graphic-heading{padding:17px 15px;gap:11px}.graphic-number{font-size:27px;min-width:31px}.graphic-heading h3{font-size:20px}.graphic-subtitle{font-size:12px}.graphic-canvas{padding:20px 15px}.graphic-caption{padding:13px 15px;font-size:11px}.clinical-graphic{margin-top:24px;margin-bottom:30px}.organ-network{grid-template-columns:1fr}.organ-node{min-height:0;padding:16px;width:100%;display:grid;grid-template-columns:12px 1fr;gap:0 12px}.organ-node strong{font-size:24px;grid-column:2;margin:0 0 6px}.organ-node .organ-dot{grid-column:1;grid-row:1;margin-top:8px}.organ-node>span:not(.organ-dot),.organ-node small{grid-column:2}.organ-node small{margin-top:7px}.organ-connector{height:32px}.organ-connector svg{height:32px;width:40px;transform:rotate(90deg);margin:0 auto}.shared-path{gap:6px 15px}.organ-detail{min-height:0}.visual-index-links{grid-template-columns:repeat(2,minmax(0,1fr))}.visual-index-links a{padding:10px 8px;font-size:11px;gap:7px}.visual-index>h2{font-size:15px}.flow-link{padding-left:35px;margin-left:12px;min-height:39px}.flow-link i{left:8px}.flow-split{grid-template-columns:1fr;padding-top:0;padding-left:20px;gap:15px;border-left:1px solid #7c90b5;margin-left:20px}.flow-split:before{display:none}.flow-branch:before{height:0;top:22px;left:-20px;width:20px;border-left:0;border-top:1px solid #7c90b5}.flow-branch:after{top:19px;left:-6px;transform:rotate(-45deg)}.flow-box{padding:15px}.flow-box h4{font-size:16px}.flow-box p{font-size:13px}.treatment-layers,.integration-grid{grid-template-columns:1fr;gap:13px}.threshold-strip>div{padding:12px 8px}.threshold-strip strong{font-size:28px}.threshold-strip span{font-size:11px}.threshold-strip small{font-size:10px}.purpose-grid{grid-template-columns:1fr;gap:24px}.purpose{display:grid;grid-template-columns:45px 1fr;column-gap:12px}.purpose-index{grid-row:1/5;font-size:32px;margin:0}.purpose h4,.purpose>strong,.purpose p{grid-column:2}.purpose .node-note{margin-top:10px!important}.potassium-bands{grid-template-columns:1fr}.potassium-band{border-right:0;border-bottom:1px solid #b8c5db;padding:15px 17px;border-top:0;border-left:5px solid #afbfda}.potassium-band:nth-child(2){border-left-color:#002fa7}.potassium-band.urgent-band{border-left-color:#17212c}.potassium-band>strong{font-size:29px;margin-bottom:12px}.follow-timeline{grid-template-columns:1fr;gap:24px;padding-top:0;padding-left:22px}.follow-timeline:before{width:1px;height:auto;top:5px;bottom:0;left:3px;right:auto}.time-stop{padding:0}.time-pin{top:5px;left:-23px}.time-stop h4{font-size:18px}.time-window strong{font-size:19px}.post-discharge{margin-top:20px}.ga-matrix{min-width:300px;border-spacing:3px}.ga-matrix th strong{font-size:15px}.ga-matrix td button{padding:7px 6px;min-height:62px}.ga-matrix th span{font-size:10px}.ga-matrix th,.ga-matrix td{width:25%}.matrix-output{font-size:12px}.graphic-note{font-size:12px;padding:11px 12px}}
@media print{.clinical-graphic{break-inside:auto;border-color:#888;margin:18pt 0;box-shadow:none;font-size:9pt}.graphic-heading{padding:10pt;background:#f4f4f4;break-after:avoid}.graphic-heading h3{font-size:14pt}.graphic-canvas{padding:12pt}.graphic-number{font-size:24pt}.graphic-subtitle,.graphic-caption{font-size:8pt}.flow-box,.flow-branch,.potassium-band,.time-stop,.organ-node{break-inside:avoid}.flow-box{padding:10pt}.flow-box h4{font-size:11pt}.flow-box p,.node-note,.graphic-note{font-size:8pt!important}.flow-box.outcome,.potassium-band.urgent-band,.urgent-note{background:white;color:black;border:2px solid black}.flow-box.outcome .node-label,.flow-box.outcome .node-note,.potassium-band.urgent-band>strong,.potassium-band.urgent-band>span{color:black}.visual-index,.organ-detail,.matrix-output{display:none}.organ-node{min-height:120pt}.organ-node strong{font-size:18pt}.ga-matrix{min-width:0}.ga-matrix td button{border:1px solid #666;min-height:42pt}.matrix-scroll{overflow:visible}.graphic-discrepancy{display:block}.graphic-discrepancy>p{display:block}.threshold-strip strong{font-size:22pt}.potassium-band>strong{font-size:20pt}.graphic-caption a{color:#000}.shared-path{font-size:8pt}.clinical-graphic *{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
'''

JS = r'''
const organExplanations={
  metabolismo:'<strong>Metabolismo.</strong> Adiposidad disfuncional, resistencia a la insulina, hiperglucemia, hipertensión y dislipidemia pueden favorecer lesión renal y cardiovascular. Identificar la comorbilidad permite elegir el beneficio que se busca.',
  rinon:'<strong>Riñón.</strong> El FGe y el CAC aportan información distinta. La función renal, el potasio y el volumen condicionan la seguridad y la selección del tratamiento, incluso con una HbA1c satisfactoria.',
  corazon:'<strong>Corazón.</strong> Congestión venosa e hipoperfusión requieren decisiones diferentes. Integrar síntomas, volumen, presión y ecocardiografía evita interpretar una creatinina aislada fuera de contexto.'
};
document.querySelectorAll('[data-organ]').forEach(button=>button.addEventListener('click',()=>{
  document.querySelectorAll('[data-organ]').forEach(other=>other.setAttribute('aria-pressed',String(other===button)));
  document.getElementById('organ-detail').innerHTML=organExplanations[button.dataset.organ];
}));
document.querySelectorAll('[data-ga-description]').forEach(button=>button.addEventListener('click',()=>{
  document.querySelectorAll('[data-ga-description]').forEach(other=>other.setAttribute('aria-pressed',String(other===button)));
  const decoder=document.createElement('textarea');decoder.innerHTML=button.dataset.gaDescription;
  document.getElementById('ga-detail').textContent=decoder.value;
}));
window.addEventListener('beforeprint',()=>document.querySelectorAll('.graphic-discrepancy').forEach(d=>{d.dataset.wasOpen=String(d.open);d.open=true}));
window.addEventListener('afterprint',()=>document.querySelectorAll('.graphic-discrepancy').forEach(d=>{d.open=d.dataset.wasOpen==='true';delete d.dataset.wasOpen}));
'''


def add_graphics(page):
    doc = BeautifulSoup(page, 'html.parser')
    graphs = [network(), matrix(), dm2(), confirm_ckd(), dm2_ckd(), diagnose_hf(), treat_hf(), integrated(), purposes(), creatinine(), potassium(), timeline()]
    parsed = [BeautifulSoup(g, 'html.parser').section for g in graphs]

    # Los destinos se derivan de los títulos/IDs existentes, no de offsets de texto.
    insertions = [(1, '2.4.'), (2, 'Algoritmo 1.'), (3, 'Algoritmo 2.'), (4, 'Algoritmo 3.'),
                  (5, 'Algoritmo 4.'), (6, 'Algoritmo 5.'), (7, 'Algoritmo 6.'),
                  (8, '4.1.'), (9, '5.2.'), (10, '5.4.'), (11, '6.1.')]
    doc.select_one('.hero .intro').insert_after(parsed[0])
    for graph_index, prefix in insertions:
        targets = [h for h in doc.select('#clinical h3') if h.get_text(' ', strip=True).startswith(prefix)]
        if len(targets) != 1:
            raise ValueError(f'No se encuentra un título único: {prefix}')
        targets[0].insert_after(parsed[graph_index])
        # El enlace de ampliación salta al texto que sigue al esquema.
        detail_id = parsed[graph_index]['id'].replace('grafico-', 'desarrollo-', 1)
        detail_anchor = doc.new_tag('a', id=detail_id, attrs={'class': 'clinical-detail-anchor'})
        parsed[graph_index].insert_after(detail_anchor)
        parsed[graph_index].select_one('.read-detail')['href'] = '#' + detail_id

    labels = ['Mapa CRM', 'FGe y albuminuria', 'DM2 por comorbilidad', 'Confirmar ERC', 'DM2 con ERC',
              'Diagnosticar IC', 'Tratar IC', 'Integrar el riesgo', 'Objetivos terapéuticos',
              'Creatinina y volumen', 'Potasio', 'Calendario de controles']
    nav_links = ''.join(f'<a href="#{g["id"]}"><b>{i:02d}</b><span>{label}</span></a>' for i, (g, label) in enumerate(zip(parsed, labels), 1))
    nav = BeautifulSoup(f'<nav class="visual-index" id="vista-grafica" aria-label="Índice de los 12 esquemas"><h2>Recorrer los 12 esquemas</h2><div class="visual-index-links">{nav_links}</div></nav>', 'html.parser').nav
    doc.select_one('.hero .quick').insert_before(nav)
    for target in doc.select('.toc,.mobile-nav'):
        link = doc.new_tag('a', href='#vista-grafica', attrs={'class': 'toc-h2'})
        link.string = '12 esquemas clínicos'
        if target.name == 'details':
            target.summary.insert_after(link)
        else:
            target.insert(0, link)
    action = doc.new_tag('a', href='#vista-grafica', attrs={'class': 'button'})
    action.string = 'Ver los 12 esquemas'
    doc.select_one('.actions').insert(0, action)
    doc.select_one('.intro').string = 'Evaluación, decisiones terapéuticas y seguimiento con 12 esquemas visuales, seis algoritmos y cuatro casos razonados. El desarrollo clínico completo se mantiene bajo cada esquema.'
    meta = doc.select_one('.meta')
    for strong in meta.select('strong'):
        if 'palabras' in strong.text:
            strong.string = strong.text.replace(',', '.')
    doc.select_one('.footer').string = 'Corte 30.09.2026 · Texto base del Markdown conservado íntegro · Esquemas explicativos derivados del mismo contenido · Fuentes y límites de prescripción en la revisión.'
    style = doc.new_tag('style', attrs={'id': 'estilos-graficos'})
    style.string = CSS
    doc.head.append(style)
    script = doc.new_tag('script', attrs={'id': 'interacciones-graficos'})
    script.string = JS
    doc.body.append(script)
    return str(doc)
