---
aliases:
  - Fact-check FA en urgencias 2026-10-30
tags: [cardio]
description: Errores de la nota original de FA y del bloque de FA de Protocolos Rápidos, con fuente y corrección aplicada.
fecha: 2026-10-30
estado: aplicado en la rama worktree-fa-flujograma, sin commit
---

# Cardio — FA en urgencias

Revisión hecha al construir [[FA en Urgencias - Flujograma.canvas|el flujograma de FA en urgencias]]. El «texto original» es el de la versión anterior a esta revisión (commit `f349b45`).

**Fuentes:** ESC 2024 FA (ehae176) · ESC 2026 IC (ehag100) · ESC 2026 ERC (ehag098) · Manual 12 de Octubre 2022, cap. 16 · fichas técnicas (FT) de CIMA. Por tema manda la ESC más reciente. No hay guía ESC de FA posterior a 2024 (comprobado en escardio.org el 2026-10-30).

**Alcance:** secciones de frecuencia, ritmo, FA preexcitada y anticoagulación. La ablación y AF-CARE no se han revisado a fondo.

## [[Fibrilación Auricular (FA)]]

### Hallazgo 1 · 🔴 Flecainida i.v. a dosis oral
- **Texto original:** «Flecainida **200-300 mg v.o. / i.v.**».
- **Fuente:** ESC 2024, tabla 13: oral 200-300 mg; i.v. 1-2 mg/kg en 10 min. FT Apocard: 2 mg/kg en ≥ 10 min, máx. 150 mg.
- **Corrección:** dosis separadas por vía, con las dos referencias i.v.

### Hallazgo 2 · 🔴 FA preexcitada ausente
- **Texto original:** no la mencionaba, y recomendaba BB, verapamilo y digoxina sin excepción.
- **Fuente:** ESC 2024, tabla 12, nota a: todos los frenadores y la amiodarona i.v. contraindicados en WPW; §9.11: CVE inmediata con compromiso. Manual §1.5.4.
- **Corrección:** nueva sección «🚫 FA preexcitada», con la discrepancia sobre flecainida (ESC 2024 la permite; Manual tabla 7 la contraindica).

### Hallazgo 3 · 🔴 Definición de IC-FEr desactualizada
- **Texto original:** calcioantagonistas contraindicados solo si FEVI ≤ 40 %; `fuente:` citaba ESC HF 2021/2023.
- **Fuente:** ESC 2026 IC: elimina IC-FEm; IC-FEr = FEVI < 50 % con IC. Verapamilo y diltiazem, y también flecainida, propafenona y dronedarona, se evitan en IC-FEr (§9.1.1.5, §9.4).
- **Corrección:** criterio añadido y nuevo apartado «Con insuficiencia cardiaca».

### Hallazgo 4 · 🔴 Amiodarona i.v.: contraindicación de ficha técnica no declarada
- **Texto original:** amiodarona i.v. en cardiopatía, sin aviso.
- **Fuente:** FT Trangorex 4.3: «La administración IV está contraindicada en caso de hipotensión, insuficiencia respiratoria grave, miocardiopatía o insuficiencia cardiaca». ESC 2024 (I A para cardiovertir; IIb B para frenar) y ESC 2026 IC (IIb C) sí la contemplan.
- **Corrección:** discrepancia declarada; decidir con Cardiología.

### Hallazgo 5 · 🟠 Propofol en paciente inestable
- **Texto original:** «Ineastabilidad Hemodinámica: […] Sello con Propofol o Midazolam».
- **Fuente:** Manual, fig. 1: propofol contraindicado en inestabilidad, TAS < 100, disfunción ventricular grave o alergia al huevo; alternativa midazolam + etomidato.
- **Corrección:** sedación reescrita, erratas corregidas.

### Hallazgo 6 · 🟠 Metoprolol con atribuciones invertidas
- **Texto original:** «2,5 mg en 5 min (ESC) vs 2,5-5 mg en 2 min, máximo 15 mg (Manual)».
- **Fuente:** es al revés. ESC 2024, tabla 12: 2,5-5 mg en 2 min, máx. 15 mg. Manual, tabla 9: «2,5 mg/5 min».
- **Corrección:** atribuciones corregidas y pauta de FT Beloken añadida.

### Hallazgo 7 · 🟠 Verapamilo atribuido al Manual sin estar en él
- **Texto original:** «5-10 mg i.v. en 2 min, repetible 10 mg a los 15-30 min (Manual)».
- **Fuente:** Manual, tabla 9: 2,5-10 mg/5 min, igual que ESC 2024. La pauta se parece a FT Manidon: 5-10 mg en ≥ 2 min y 10 mg a los 30 min.
- **Corrección:** atribuido a la FT. Añadido diltiazem i.v. de la ESC, sin presentación i.v. en CIMA.

### Hallazgo 8 · 🟠 Digoxina atribuida al Manual sin estar en él
- **Texto original:** «0,5 mg seguido de 0,25 mg cada 6-8 h hasta carga de 1-1,5 mg (Recomendación estricta Manual)» y «3ª línea».
- **Fuente:** Manual, tabla 9: 0,5 mg, máx. 1,5 mg; 2.ª línea. ESC 2024: 0,5 mg (0,75-1,5 mg/24 h divididos). FT Kern: 0,5-1 mg, la mitad primero y el resto cada 4-8 h.
- **Corrección:** las tres pautas atribuidas y ajuste renal añadido.

### Hallazgo 9 · 🟠 Frecuencia «de elección en agudos con mala tolerancia»
- **Texto original:** «Estrategia de elección en agudos con mala tolerancia».
- **Fuente:** ESC 2024, rec. tabla 15: inestabilidad atribuible a la FA → CVE (I C). Frenar es la terapia inicial en agudo (rec. tabla 14, I B), no el tratamiento del inestable.
- **Corrección:** reescrito, con la distinción entre FA causa y FA secundaria (§7.1.2, §9.1).

### Hallazgo 10 · 🟠 Calcioantagonistas como «2ª línea»
- **Texto original:** «2ª Línea (Calcioantagonistas no DHP)».
- **Fuente:** ESC 2024, rec. tabla 14: primera elección con FEVI > 40 % (I B). Manual, tabla 9: 1.ª línea.
- **Corrección:** cambiado.

### Hallazgo 11 · 🟠 Anticoagulación en ERC desactualizada e incompleta
- **Texto original:** AVK «reservado» para FG < 15; sin dosis de apixabán con ClCr 15-29; scores sin límite renal.
- **Fuente:** ESC 2026 ERC, rec. tabla 26: FG 15-29 anti-Xa (IIa); FG < 15 individualizar (IIa C), AVK o apixabán 2,5 mg/12 h sin diálisis (IIb C), anti-Xa a dosis baja en diálisis (IIb C). Rec. tabla 25: no usar scores con FG < 30 (III). FT Eliquis: 2,5 mg/12 h con ClCr 15-29; no recomendado con ClCr < 15 o diálisis.
- **Corrección:** línea de ERC añadida, con la discrepancia ESC/FT.

### Hallazgo 12 · 🟠 Omisiones de seguridad en cardioversión farmacológica
- **Texto original:** sin corte renal de flecainida ni ventana de vernakalant; vernakalant sin dosis.
- **Fuente:** ESC 2024, tabla 13: flecainida no con CrCl < 35. FT Apocard y ESC 2026 ERC: reducir dosis. FT Brinavess: no en las 4 h antes o después de antiarrítmicos i.v. de clase I o III.
- **Corrección:** añadidos. El canvas recoge además otras contraindicaciones de FT.

### Hallazgo 13 · 🟢 Cita de la recomendación III C recortada
- **Texto original:** cita con «TEE» y sin la segunda cláusula.
- **Fuente:** ESC 2024, rec. tabla 15: «…or there is scope to wait for spontaneous cardioversion».
- **Corrección:** cita completa.

### Hallazgo 14 · 🟢 Rangos incompletos
- **Texto original:** bisoprolol 2,5-10 mg/24 h y amiodarona 900 mg/24 h sin indicar la fuente.
- **Fuente:** ESC 2024: bisoprolol 1,25-20 mg/24 h; amiodarona 900-1200 mg/24 h. Manual: 2,5-10 mg/24 h y 900 mg/24 h.
- **Corrección:** ambos atribuidos.

## [[03 - Protocolos Rápidos Boxes Urgencias]]

### Hallazgo 15 · 🟠 Mismos errores en el bloque de FA
- **Texto original:** propofol en inestable; flecainida «2 mg/kg en 10-20 min» sin máximo; digoxina «0,25 mg/6-8 h»; calcioantagonistas de «2ª línea»; criterios de ritmo atribuidos a la ESC (son de Manual, tabla 6); FG < 15 como contraindicación absoluta de ACOD; sin FA preexcitada; inestabilidad sin distinguir FA causa de FA secundaria.
- **Corrección:** aplicado en el bloque de FA, con las mismas fuentes.

### Hallazgo 16 · ⚪ Bloque duplicado y vacío, sin resolver
- **Situación:** el archivo repite su contenido; en la segunda copia, la sección de FA tiene «Control de frecuencia» y «Control de ritmo» vacíos. Solo se actualizaron su línea de scores y la tabla ACOD/AVK.
- **Pendiente:** decidir si se elimina la copia. No se ha tocado por ser un cambio ajeno al FA.

## Tabla de verificación del canvas
Contraste hecho por un subagente independiente con los originales y revisado después. ✅ verificado · ⚠ no verificable o sin fuente primaria.

| Dato | Fuente y sección | Estado |
|---|---|---|
| ECG confirma la FA, I A | ESC 2024, rec. tabla 1 | ✅ |
| Inestabilidad = hipoperfusión | Manual, fig. 1 | ✅ |
| Lista TAS < 90, frialdad, oliguria, acidosis, consciencia, EAP, dolor | Solo nota Arritmias; marcada como lectura práctica | ⚠ |
| Hasta 83 % a sinusal en 48 h tras tratar la causa | ESC 2024 §9.1 | ✅ |
| Amiodarona, digoxina o landiolol para frenar, IIb B | ESC 2024, rec. tabla 14 | ✅ |
| Amiodarona o digoxina en IC-FEr inestable, IIb C | ESC 2026 IC, rec. tabla 15 | ✅ |
| CVE urgente I C | ESC 2024, rec. tabla 15; ESC 2026 IC, rec. tabla 15 | ✅ |
| Iniciar ACO lo antes posible, IIa B | ESC 2024, rec. tabla 15 y fig. 12 | ✅ |
| Propofol 0,5-1 mg/kg y contraindicaciones | Manual, fig. 1 | ✅ |
| Midazolam 2-3 mg + etomidato 0,3 mg/kg | Manual, fig. 1 | ✅ |
| Etomidato 0,15 mg/kg + opiáceo | Manual §2.7.1 | ✅ |
| CVE FA 150-200 J; flutter 50-100 J; TV polimorfa 360 J | Manual, fig. 1 y §1.5.7 | ✅ |
| Energía máxima fija mejor que escalada baja | ESC 2024 §7.2.2 | ✅ |
| Sepsis, desencadenante más frecuente | ESC 2024 §9.5 | ✅ |
| Flecainida y propafenona no para convertir flutter | ESC 2024, tabla 13 | ✅ |
| Frenadores y amiodarona i.v. prohibidos en WPW | ESC 2024, tabla 12, nota a | ✅ |
| Flecainida en preexcitada: permitida / contraindicada | ESC 2024 §9.11 / Manual, tabla 7 | ✅ |
| Ibutilida y diltiazem i.v. no constan | API CIMA, 2026-10-30 | ✅ |
| FC < 110, IIa B; combinación, IIa C | ESC 2024, rec. tabla 14 | ✅ |
| Metoprolol 2,5-5 mg en 2 min, máx. 15 mg | ESC 2024, tabla 12 | ✅ |
| Metoprolol hasta 5 mg a 1-2 mg/min, total 10-15 mg | FT Beloken 4.2 | ✅ |
| Metoprolol «2,5 mg/5 min» | Manual, tabla 9; ambiguo («en» o «cada») | ⚠ |
| Esmolol, landiolol, verapamilo, diltiazem, digoxina, amiodarona | ESC 2024, tabla 12 | ✅ |
| Las mismas por FT | FT Brevibloc, Rapibloc, Manidon, Kern, Trangorex 4.2 | ✅ |
| IC-FEr = FEVI < 50 % | ESC 2026 IC, §3 | ✅ |
| BB I C y digoxina IIa C en IC-FEr estable | ESC 2026 IC, rec. tabla 15 | ✅ |
| Amiodarona i.v. contraindicada en hipotensión o IC | FT Trangorex 4.3 | ✅ |
| Landiolol: contraindicaciones | FT Rapibloc 4.3 | ✅ |
| Esperar hasta 48 h, IIa B | ESC 2024, rec. tabla 15 | ✅ |
| Sinusal espontáneo 55-66 % en 24 h, 69 % en 48 h | ESC 2024 §7.2.3 | ✅ |
| No CV > 24 h sin ACO o ETE, III C | ESC 2024, rec. tabla 15 | ✅ |
| ETE I B; ACO 3 semanas I B; repetir ETE IIa C; ≥ 4 semanas | ESC 2024, rec. tabla 15 y §7.2.1 | ✅ |
| Amiloidosis: ETE siempre, evitar digoxina | ESC 2026 IC §12.3 | ✅ |
| No CVF si QTc > 500 ms, BAV, disfunción sinusal, III C | ESC 2024, rec. tabla 17 | ✅ |
| Flecainida i.v. 1-2 mg/kg en 10 min; oral 200-300 mg | ESC 2024, tabla 13 | ✅ |
| Flecainida i.v. 2 mg/kg en ≥ 10 min, máx. 150 mg | FT Apocard 4.2 | ✅ |
| Flecainida con ClCr < 35: no usar / reducir | ESC 2024, tabla 13 / FT Apocard y ESC 2026 ERC | ✅ |
| Propafenona i.v. 1,5-2 mg/kg en 10 min; oral 450-600 mg | ESC 2024, tabla 13 | ✅ |
| Propafenona 1 mg/kg (0,5-2) en 3-5 min; QRS/QTc +20 % | FT Rytmonorm 4.2 | ✅ |
| Vernakalant 3 + 2 mg/kg; máx. 339 y 226 mg; 5 mg/kg/24 h; ventana de 4 h | ESC 2024, tabla 13; FT Brinavess | ✅ |
| Amiodarona 300 mg + 900-1200 mg/24 h; Manual 900 mg | ESC 2024, tabla 13; Manual, tabla 7 | ✅ |
| Amiodarona 5 mg/kg → 10-20 mg/kg/24 h, límite 1200 mg | FT Trangorex 4.2 | ✅ |
| Vernakalant 50 % en 10 min; amiodarona 44 % | ESC 2024, tabla 13 | ✅ |
| ACO ≥ 4 semanas tras CV; opcional < 24 h y bajo riesgo | ESC 2024, fig. 12 y §7.2.1 | ✅ |
| CHA₂DS₂-VA ≥ 2 I; = 1 IIa; MCH y amiloidosis I B | ESC 2024, rec. tabla 6 | ✅ |
| Scores de sangrado no para decidir, III B | ESC 2024, rec. tabla 12 | ✅ |
| Scores no con FG < 30, III | ESC 2026 ERC, rec. tabla 25 | ✅ |
| Dosis de apixabán, dabigatrán, edoxabán, rivaroxabán | ESC 2024, tabla 11 | ✅ |
| Apixabán 2,5 mg/12 h con ClCr 15-29; no con < 15 o diálisis | FT Eliquis | ✅ |
| FG ≥ 30 I A; 15-29 IIa; < 15 IIa C; AVK o apixabán IIb C; diálisis IIb C | ESC 2026 ERC, rec. tabla 26 | ✅ |
| Embarazo: CVE I C; BB sin atenolol; HBPM o AVK; ACOD no | ESC 2024 §9.8 y rec. tabla 28 | ✅ |
| SCA: triple terapia hasta 1 semana I; hasta 1 mes IIa | ESC 2024, fig. 14 | ✅ |
| Hemorragia: interrumpir I C; CCP IIa C; antídoto IIa B | ESC 2024, rec. tabla 13 | ✅ |
| Sin criterios de alta o ingreso | Búsqueda en ESC, IC y Manual, no lectura íntegra | ⚠ |
| Tarjetas «Alta», «Observación», «Dejar documentado» | Lectura práctica, marcada en la tarjeta | ⚠ |

## Sin revisar
- Tabla de dosis de ACOD en `03 - Protocolos Rápidos`.
- Fichas de `20_farmacos/`. `Flecainida.md` da 10-30 min de infusión; la FT dice ≥ 10 min, y ≤ 30 min solo en IC o TV persistente.
- Notas [[Arritmias]] y [[Insuficiencia cardiaca aguda]], que aún citan guías anteriores a las de 2026 de IC.
