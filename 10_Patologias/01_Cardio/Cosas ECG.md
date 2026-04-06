---
tags:
  - ECG
  - cardiologia
  - urgencias
  - diagnostico
aliases:
  - Electrocardiograma
  - EKG
  - Electro
---

# ECG - Guía de Interpretación

> [!tip] Sistemática de lectura (Método Dubin)
> **1. Frecuencia** → **2. Ritmo** → **3. Eje** → **4. Hipertrofia** → **5. Infarto** → **6. Misceláneos**
>
> Seguir SIEMPRE este orden. Nunca saltar directamente al "hallazgo llamativo".

---

## 1. Bases del ECG

### Derivaciones

**Plano frontal** (miembros): I, II, III, aVR, aVL, aVF — valoran la actividad eléctrica en el plano coronal.

**Plano horizontal** (precordiales): V1 → V6 — valoran la actividad eléctrica en el plano transversal. La progresión normal de R va aumentando de V1 a V6 (la "zona de transición" donde R = S suele estar en V3-V4).

| Grupo de derivaciones | Territorio miocárdico | Arteria coronaria |
|---|---|---|
| V1-V4 | Anterior (septo + pared anterior) | Descendente anterior (DA) |
| V5-V6, I, aVL | Lateral | Circunfleja (Cx) o DA |
| II, III, aVF | Inferior (diafragmático) | Coronaria derecha (CD) o Cx |
| V3R-V4R | Ventrículo derecho | CD proximal |
| V7-V9 | Posterior | Cx o CD |

### Complejo PQRST normal

![[ecg_normal.svg]]

| Componente | Qué representa | Valor normal |
|---|---|---|
| **Onda P** | Despolarización auricular | <0.12s duración, <2.5mm altura |
| **Intervalo PR** | Conducción AV (desde inicio P hasta inicio QRS) | 0.12–0.20s (3–5 cuadraditos) |
| **Complejo QRS** | Despolarización ventricular | <0.12s (<3 cuadraditos) |
| **Segmento ST** | Meseta del potencial de acción ventricular | Isoeléctrico (en la línea basal) |
| **Onda T** | Repolarización ventricular | Concordante con QRS (misma dirección) |
| **Intervalo QT** | Despolarización + repolarización ventricular total | QTc <0.44s hombres, <0.46s mujeres |
| **Onda U** | Repolarización de fibras de Purkinje (o M-cells) | Pequeña, misma dirección que T |

> [!info] Calibración estándar
> Velocidad: **25 mm/s** → 1 cuadradito (1mm) = 0.04s, 1 cuadrado grande (5mm) = 0.2s
> Voltaje: **10 mm/mV** → 1 cuadradito = 0.1mV, 1 cuadrado grande = 0.5mV

### Corrección del QT (QTc)

Fórmula de **Bazett** (la más usada): QTc = QT / √RR

Fórmula de **Fredericia** (más precisa en frecuencias extremas): QTc = QT / ∛RR

**QTc prolongado:** >0.44s (hombres), >0.46s (mujeres). Riesgo de Torsade de Pointes si >0.50s.

---

## 2. Frecuencia

### Método de las tripletas (Dubin)

Localiza una onda R que caiga sobre (o cerca de) una línea gruesa. Cuenta las líneas gruesas hasta la siguiente R: **"300, 150, 100, 75, 60, 50"**.

![[ecg_frecuencia.svg]]

### Tabla de divisiones finas (cuadraditos entre R-R)

| Cuadraditos | FC | Cuadraditos | FC |
|---|---|---|---|
| 5 (1 cuadrado grande) | 300 | 15 | 100 |
| 6 | 250 | 17 | 88 |
| 7 | 214 | 18 | 83 |
| 8 | 187 | 19 | 79 |
| 9 | 167 | 20 | 75 |
| 10 | 150 | 21 | 71 |
| 11 | 136 | 22 | 68 |
| 12 | 125 | 23 | 65 |
| 13 | 115 | 24 | 62 |
| 14 | 107 | 25 | 60 |

> Fórmula exacta: **FC = 1500 / (nº cuadraditos entre R-R)**

### Para bradicardia o ritmos irregulares

Contar QRS en un trazo de **6 segundos** (30 cuadrados grandes) y multiplicar × 10.

### Definiciones

- **Bradicardia sinusal:** FC < 60 lpm
- **Frecuencia normal:** 60–100 lpm
- **Taquicardia sinusal:** FC > 100 lpm

---

## 3. Ritmo

### Ritmo sinusal normal — criterios

1. Onda P positiva en II y negativa en aVR (origen en nodo SA)
2. Cada P seguida de un QRS
3. Cada QRS precedido de una P
4. Intervalo PR constante (0.12–0.20s)
5. RR regular (variación <10%)
6. FC 60–100 lpm

> [!warning] Siempre inspeccionar
> - ¿Hay **P antes de cada QRS**? ¿**QRS después de cada P**?
> - ¿Los intervalos **PR** son constantes? (si no → bloqueo AV)
> - ¿El **QRS** es estrecho (<0.12s) o ancho? (si ancho → BRD/BRI)
> - ¿El **eje** está desviado? (si sí → sospechar hemibloqueo)

### Ritmos irregulares

#### Arritmia sinusal
Ritmo irregular que varía con la respiración. Todas las ondas P son idénticas. **Es normal** (especialmente en jóvenes).

#### Fibrilación auricular (FA)

![[ecg_fa.svg]]

Múltiples focos auriculares descargan caóticamente → línea basal fibrilatoria irregular (sin ondas P identificables). La respuesta ventricular es **irregularmente irregular**.

Claves diagnósticas:
- Ausencia de ondas P → línea basal "fibrilatoria" o plana irregular
- Intervalos RR completamente irregulares
- QRS generalmente estrecho (salvo aberrancia o BRH previo)
- FC ventricular variable (controlada <110 lpm vs rápida)

#### Flutter auricular

![[ecg_flutter.svg]]

Un foco auricular único descarga rápidamente a **~300 lpm** generando ondas en **"diente de sierra"** (ondas F). La conducción AV suele ser 2:1 (FC ~150), 3:1 o 4:1.

> [!tip] Regla práctica
> **Taquicardia regular a ~150 lpm** con QRS estrecho → sospechar **flutter 2:1** hasta que se demuestre lo contrario. Hacer maniobras vagales o dar adenosina para "desenmascarar" las ondas F.

#### Marcapaso migratorio
Ritmo irregular. Las ondas P cambian de morfología (≥3 morfologías diferentes). FC <100 lpm. Si FC >100 → Taquicardia Auricular Multifocal (TAM).

### Pulsos prematuros

| Tipo | Origen | P previa | QRS | Pausa compensatoria |
|---|---|---|---|---|
| **PAC** (extrasístole auricular) | Foco auricular ectópico | P' diferente a la sinusal | Estrecho (habitual) | Incompleta |
| **PJC** (extrasístole juncional) | Unión AV | P retrógrada (negativa en II) o ausente | Estrecho | Variable |
| **CVP** (extrasístole ventricular) | Foco ventricular | Ausente (disociación) | **Ancho, bizarro** | Completa |

> CVP multifocal (≥2 morfologías), en corridas (≥3 seguidas = TV no sostenida), o con R sobre T → mayor riesgo arrítmico.

### Ritmos de escape

Cuando el nodo SA falla o hay bloqueo, un foco de automaticidad inferior toma el mando:

| Nivel de escape | FC intrínseca | Morfología QRS |
|---|---|---|
| **Auricular** | 60–80 lpm | Estrecho (normal) |
| **Juncional** | 40–60 lpm | Estrecho (normal) |
| **Ventricular** | 20–40 lpm | **Ancho** (idioventricular) |

### Taquiarritmias

| FC | Tipo |
|---|---|
| 150–250 lpm | Taquicardia paroxística |
| 250–350 lpm | Aleteo (flutter) |
| 350–450+ lpm | Fibrilación |

#### Taquicardias de QRS estrecho (<0.12s) — origen supraventricular

- **Taquicardia sinusal:** P normales, respuesta a estímulo (fiebre, dolor, hipovolemia…)
- **TPSV (taquicardia paroxística supraventricular):** Inicio y fin bruscos. Reentrada nodal (TRIN) es la más frecuente. FC 150–250.
- **TAP (Taquicardia auricular paroxística):** Foco auricular irritable. P' ectópicas visibles.
- **Flutter auricular:** Ondas F en diente de sierra.
- **FA con respuesta ventricular rápida.**

#### Taquicardias de QRS ancho (≥0.12s) — asumir ventricular hasta demostrar lo contrario

![[ecg_tv.svg]]

##### TV monomórfica
Foco ventricular único. QRS ancho, regular, rápido (150–250 lpm). **Morfología constante.**

Criterios de **Brugada** para diferenciar TV de TSV con aberrancia:
1. ¿Ausencia de RS en todas las precordiales? → TV
2. ¿Intervalo R-S > 100ms en alguna precordial? → TV
3. ¿Disociación AV? → TV
4. ¿Criterios morfológicos en V1-V2 y V6? → TV

> [!danger] Si duda: tratar como TV
> Una TSV con aberrancia tratada como TV no mata. Una TV tratada como TSV sí puede matar.

##### Torsade de Pointes (TV polimórfica con QT largo)

![[ecg_torsade.svg]]

QRS ancho con eje que "gira" alrededor de la línea basal (patrón de huso: crescendo-decrescendo). Asociada a **QT largo** (congénito o adquirido por fármacos/iones).

Tratamiento: **sulfato de magnesio** IV (1-2g en bolo) + corregir causa (suspender fármaco, corregir K⁺). Isoproterenol o marcapasos temporal si recurrente. **NO amiodarona** (alarga QT).

#### Fibrilación ventricular

![[ecg_fv.svg]]

Actividad eléctrica caótica sin gasto cardíaco efectivo → **parada cardíaca**. Tratamiento: **desfibrilación inmediata** + RCP.

### Bloqueos

#### Bloqueo sinusal (SA)
El nodo SA no consigue despolarizar las aurículas → pausa (falta un ciclo P-QRS-T completo). Puede seguirse de un latido de escape.

#### Bloqueos auriculoventriculares (BAV)

##### BAV de 1er grado

![[ecg_bav1.svg]]

**PR prolongado (>0.20s = >1 cuadrado grande)** pero todas las P conducen. No es un bloqueo verdadero sino un retraso. No requiere tratamiento por sí solo.

##### BAV de 2° grado — Mobitz I (Wenckebach)

![[ecg_bav2w.svg]]

**PR se alarga progresivamente** en cada latido hasta que una P no conduce (se "pierde" un QRS). Luego el ciclo se reinicia. El bloqueo suele ser a nivel del nodo AV (suprahisiano). Generalmente **benigno** (vagotónico, deportistas, fármacos).

##### BAV de 2° grado — Mobitz II

![[ecg_bav2m.svg]]

PR **constante** en los latidos conducidos, pero de forma súbita e inesperada una P no conduce. El bloqueo es infrahisiano (His-Purkinje). **Mayor riesgo de progresión a BAV completo** → valorar marcapasos.

> [!danger] Mobitz II ≠ Wenckebach
> Wenckebach: PR se alarga → benigno, suprahisiano.
> Mobitz II: PR fijo, pérdida súbita → peligroso, infrahisiano. **Valorar marcapasos.**

##### BAV 2:1
No se puede clasificar como Wenckebach o Mobitz porque no hay dos PR consecutivos para comparar. Clave: si QRS estrecho → probablemente suprahisiano. Si QRS ancho → probablemente infrahisiano.

##### BAV de 3er grado (completo)

![[ecg_bav3.svg]]

**Disociación AV completa.** Las P marchan a su ritmo (auricular, ~60-80 lpm) y los QRS al suyo (ritmo de escape juncional 40-60 o ventricular 20-40 lpm). **No hay relación entre P y QRS.**

- QRS estrecho → escape juncional (más estable)
- QRS ancho → escape ventricular (menos fiable, mayor riesgo de asistolia)

Tratamiento: **marcapasos** (transitorio → definitivo). Si inestable: atropina, cronotropos, marcapasos transcutáneo.

#### Bloqueos de rama del haz de His

> [!info] Criterio de anchura
> QRS ≥ 0.12s (3 cuadraditos) = bloqueo completo de rama
> QRS 0.10–0.12s = bloqueo incompleto de rama

##### Bloqueo de rama derecha (BRD)

![[ecg_brd.svg]]

Patrón **rSR'** en V1-V2 ("orejas de conejo"), con S empastada en I y V6.

Criterios:
- QRS ≥ 0.12s
- rSR' en V1-V2 (R' > r)
- S ancha/empastada en I, aVL, V5-V6
- T negativa en V1-V2 (cambios secundarios de repolarización)

> El BRD puede ser normal como hallazgo aislado. Valorar contexto: si aparece de novo puede indicar TEP, sobrecarga derecha o cardiopatía.

##### Bloqueo de rama izquierda (BRI)

![[ecg_bri.svg]]

Criterios:
- QRS ≥ 0.12s
- QS profunda o rS en V1 (ausencia de r o r mínima)
- R ancha, mellada/empastada en I, aVL, V5-V6
- Ausencia de q en V5-V6
- T negativa en derivaciones con R dominante (I, aVL, V5-V6)

> [!warning] BRI y diagnóstico de infarto
> El BRI enmascara los cambios de infarto en el ECG. Si sospecha de SCA con BRI → usar **criterios de Sgarbossa** (modificados por Smith):
> 1. Elevación ST ≥1mm concordante con QRS (5 puntos)
> 2. Depresión ST ≥1mm en V1-V3 (3 puntos)
> 3. Ratio ST/S ≥ 0.25 en derivación con S dominante (criterio de Smith)
> ≥3 puntos Sgarbossa → alta especificidad para IAM

#### Hemibloqueos (fasciculares)

| | Hemibloqueo anterior izquierdo (HBAI) | Hemibloqueo posterior izquierdo (HBPI) |
|---|---|---|
| **Eje** | Desviación izquierda extrema (más allá de -45°) | Desviación derecha (>+120°) |
| **Patrón** | qR en I y aVL; rS en II, III, aVF | rS en I y aVL; qR en II, III, aVF |
| **QRS** | <0.12s (no ensancha significativamente) | <0.12s |
| **Frecuencia** | Común (fascículo anterosuperior es largo y delgado) | Raro (fascículo posteroinferior es grueso y corto — necesita daño severo) |

> Bloqueo bifascicular = BRD + HBAI (el más frecuente) o BRD + HBPI. Bloqueo trifascicular = bifascicular + BAV 1° → riesgo de BAV completo.

---

## 4. Eje eléctrico

### Determinación rápida (método de los cuadrantes)

Mira la polaridad del QRS en **derivación I** y **aVF**:

| I | aVF | Cuadrante | Interpretación |
|---|---|---|---|
| (+) | (+) | 0° a +90° | **Normal** |
| (+) | (−) | 0° a −90° | **DEI** (desviación eje izquierdo) |
| (−) | (+) | +90° a ±180° | **DED** (desviación eje derecho) |
| (−) | (−) | −90° a ±180° | **Eje extremo / indeterminado** |

![[ecg_eje.svg]]

### Eje en grados (más preciso)

1. Determina el cuadrante (I y aVF)
2. Busca la derivación donde el QRS es más **isoeléctrico** (R ≈ S)
3. El eje es **perpendicular** a esa derivación, en el cuadrante ya determinado

### Causas de desviación del eje

| DEI | DED |
|---|---|
| HBAI | HBPI |
| HVI | HVD |
| IAM inferior | TEP |
| Obesidad, embarazo, ascitis | EPOC (corazón vertical) |
| Ritmo ventricular izquierdo | Neumotórax izquierdo |

### Rotación en el plano horizontal (precordiales)

Busca la derivación precordial donde el QRS es isoeléctrico (zona de transición):
- **Normal:** transición en V3-V4
- **Rotación horaria** (transición en V5-V6): EPOC, HVD → el VD "mira" más derivaciones
- **Rotación antihoraria** (transición en V1-V2): HVI → el VI domina antes

---

## 5. Hipertrofia

### Hipertrofia auricular

| | HAD (P pulmonale) | HAI (P mitrale) |
|---|---|---|
| **Onda P en II** | Picuda y alta (>2.5mm) | Ancha (>0.12s), bimodal/mellada |
| **Onda P en V1** | Componente inicial alto (difásica con primera parte positiva grande) | Componente terminal negativo grande y ancho (difásica con parte negativa profunda) |
| **Causas** | Cor pulmonale, EPOC, TEP, estenosis tricuspídea, cardiopatías congénitas | Estenosis mitral, insuficiencia mitral, HVI, miocardiopatía |

### Hipertrofia ventricular derecha (HVD)

Criterios:
- R > S en V1 (inversión de la progresión normal)
- Onda R dominante en V1 con S persistente en V5-V6
- Desviación del eje a la derecha (DED)
- Patrón de strain derecho: ST deprimido con T negativa en V1-V3
- Rotación horaria en plano horizontal

> Los criterios de HVD son inseguros si hay BRD asociado.

### Hipertrofia ventricular izquierda (HVI)

#### Criterios de voltaje (sensibilidad limitada pero alta especificidad si hay strain)

**Sokolow-Lyon:** S en V1 + R en V5 o V6 ≥ **35mm**

**Cornell:** R en aVL + S en V3 > **28mm** (hombres) o > **20mm** (mujeres)

**Derivación aVL aislada:** R en aVL > **11mm**

#### Patrón de strain (sobrecarga)

Depresión ST asimétrica con T invertida en derivaciones laterales (I, aVL, V5-V6): la "descarga" va hacia abajo gradualmente y vuelve bruscamente hacia arriba.

> [!info] Limitaciones
> Los criterios de voltaje tienen baja sensibilidad (~20-50%) pero alta especificidad (~85-95%). El patrón de strain aumenta la probabilidad. El ecocardiograma es el gold standard para confirmar HVI.

---

## 6. Infarto / Isquemia

### La triada del infarto agudo

![[ecg_sca.svg]]

| Hallazgo ECG | Significado | Cronología |
|---|---|---|
| **T hiperagudas** (picudas, simétricas, anchas) | Isquemia precoz (minutos) | Primero en aparecer |
| **Elevación ST** (convexa hacia arriba) | Lesión/daño agudo transmural | Minutos-horas |
| **Ondas Q** (patológicas: >0.04s o >1/3 del QRS) | Necrosis | Horas-días (permanentes) |
| **T invertidas** (simétricas) | Isquemia subaguda | Horas-semanas |

> **Evolución típica:** T hiperagudas → elevación ST → aparecen Q → ST se normaliza → T se invierte → (semanas-meses) T puede normalizarse pero Q persiste.

### SCACEST — criterios de elevación ST

**Elevación ST en ≥2 derivaciones contiguas:**
- ≥2.5mm en V2-V3 en hombres <40 años
- ≥2.0mm en V2-V3 en hombres ≥40 años
- ≥1.5mm en V2-V3 en mujeres
- ≥1.0mm en el resto de derivaciones

> [!warning] Siempre buscar cambios recíprocos (imagen en espejo)
> La presencia de **depresión ST recíproca** en derivaciones opuestas aumenta enormemente la especificidad para IAM.

### Localización del infarto y arteria culprit

| Territorio | Derivaciones con cambios | Arteria |
|---|---|---|
| **Anterior extenso** | V1-V6 | DA proximal (antes de S1) |
| **Anteroseptal** | V1-V4 | DA (septal) |
| **Anterior** | V3-V4 | DA (media) |
| **Lateral** | I, aVL (± V5-V6) | Cx o DA diagonal |
| **Inferior** | II, III, aVF | CD (80%) o Cx (20%) |
| **Posterior** | V7-V9 (o espejo: R alta + depresión ST en V1-V3) | CD o Cx |
| **Ventrículo derecho** | V3R-V4R (+ inferior) | CD proximal |

> [!tip] IAM inferior: ¿CD o Cx?
> - Elevación ST III > II → CD
> - Elevación ST II > III → Cx
> - Depresión ST en I y aVL → CD
> - Siempre hacer **derivaciones derechas** (V3R-V4R) en todo IAM inferior para descartar extensión a VD

### SCASEST (infarto sin elevación ST)

Hallazgos posibles:
- Depresión ST (≥0.5mm): isquemia subendocárdica
- Inversión de T (simétricas, profundas): isquemia transmural
- **Síndrome de Wellens:** T invertidas profundas y simétricas en V2-V3 (tipo A: T bifásica; tipo B: T profundamente invertida). Indica **estenosis crítica de DA proximal** → riesgo inminente de IAM anterior extenso. Contraindicada la ergometría.
- ECG normal (no excluye SCA — seriación de troponinas)

### Diagnóstico diferencial de elevación ST

No toda elevación ST es un IAM:
- **Pericarditis:** elevación ST difusa + cóncava ("sonriente") + depresión PR + sin cambios recíprocos
- **Repolarización precoz benigna:** elevación ST cóncava en V2-V5 con muesca en J, en jóvenes sanos
- **Aneurisma ventricular:** elevación ST crónica con ondas Q (post-IAM antiguo)
- **Brugada:** elevación ST en V1-V3 con morfología específica
- **Takotsubo:** elevación ST + T invertidas profundas difusas + disfunción apical transitoria
- **Hiperkaliemia:** pseudo-elevación ST con T picudas y QRS ancho

---

## 7. Misceláneos

### Tromboembolismo pulmonar (TEP)

![[ecg_tep.svg]]

Hallazgos clásicos (baja sensibilidad pero alta especificidad cuando presentes):
- **S1Q3T3:** S profunda en I + Q patológica en III + T invertida en III
- Taquicardia sinusal (lo más frecuente)
- BRD agudo (transitorio, a menudo incompleto)
- Sobrecarga derecha aguda: DED, ondas T invertidas V1-V4
- Depresión ST en II
- P pulmonale

> El ECG normal NO excluye TEP. La taquicardia sinusal es el hallazgo más frecuente. El patrón S1Q3T3 completo aparece en menos del 20% de los TEP.

### Alteraciones electrolíticas

#### Hiperkaliemia

![[ecg_hiperk.svg]]

Progresión según niveles de K⁺:
- **Leve (5.5–6.5 mEq/L):** T picudas, simétricas, estrechas ("en tienda de campaña")
- **Moderada (6.5–7.5 mEq/L):** PR prolongado → P aplanada/ausente + QRS ensanchado
- **Severa (>7.5 mEq/L):** Patrón sinusoidal (fusión QRS-T) → riesgo inminente de FV/asistolia

> [!danger] Tratamiento urgente si QRS ancho o patrón sinusoidal
> **Gluconato cálcico 10% IV** (estabiliza membrana) → Insulina + glucosa, salbutamol nebulizado (redistribución) → Resinas/diuréticos/diálisis (eliminación)

#### Hipokaliemia

![[ecg_hipok.svg]]

Hallazgos:
- Aplanamiento de onda T
- Onda U prominente (puede superar a la T → "falso QT largo")
- Depresión ST
- Prolongación QT (real)
- Riesgo de arritmias ventriculares (CVP, TV, Torsade) especialmente si toma digoxina

#### Calcio

| Hipercalcemia | Hipocalcemia |
|---|---|
| QT **acortado** (a expensas del ST) | QT **prolongado** (a expensas del ST) |
| Riesgo de bradicardia, BAV | Riesgo de Torsade de Pointes |

### Efectos farmacológicos en el ECG

#### Digoxina ("efecto digitálico" ≠ intoxicación)

Efecto terapéutico (no significa toxicidad):
- Descenso ST con concavidad ("cubeta digitálica" o "bigote de Salvador Dalí")
- Aplanamiento/inversión de T
- QT acortado

Signos de **toxicidad digitálica:**
- Bradicardia: bloqueo SA, BAV (cualquier grado)
- Taquiarritmias: TAP con bloqueo, taquicardia juncional, CVP multifocal, TV bidireccional
- Arritmia patognomónica: **TAP con bloqueo AV variable**

> La intoxicación digitálica combina bloqueos (depresión de conducción) con focos irritables (aumento de automaticidad).

#### Fármacos que prolongan QT

Antiarrítmicos (amiodarona, sotalol, quinidina), antipsicóticos, macrólidos, fluoroquinolonas, antieméticos (ondansetrón), antifúngicos…

> Siempre verificar QTc basal y en seguimiento. Riesgo de Torsade si QTc >0.50s. Consultar www.crediblemeds.org.

### Patrones especiales

#### Síndrome de Brugada

![[ecg_brugada.svg]]

Canalopatía con riesgo de muerte súbita por FV. Patrón en V1-V2 con **derivaciones altas** (V1-V2 en 2° espacio intercostal):
- **Tipo 1 (diagnóstico):** Elevación ST ≥2mm con descenso cóncavo ("aleta de tiburón") seguido de T negativa
- **Tipo 2:** Elevación ST en "silla de montar"
- **Tipo 3:** Elevación ST <1mm

> Solo el tipo 1 es diagnóstico. El tipo 1 espontáneo o inducido por flecainida/ajmalina + síncope/TV/FV/historia familiar de muerte súbita → **indicación de DAI**.

#### Wolff-Parkinson-White (WPW)

![[ecg_wpw.svg]]

Vía accesoria (haz de Kent) que conduce impulsos de aurículas a ventrículos sin pasar por el nodo AV:
- **PR corto** (<0.12s): no hay retardo del nodo AV
- **Onda delta** (empastamiento inicial del QRS): pre-excitación ventricular
- **QRS ancho** (>0.10s): fusión entre conducción por vía accesoria y vía normal

> [!danger] WPW + FA = EMERGENCIA
> La FA puede conducir por la vía accesoria a frecuencias muy rápidas → FV. **CONTRAINDICADOS:** verapamilo, diltiazem, digoxina, adenosina (bloquean nodo AV, favorecen conducción por vía accesoria). Tratamiento: **procainamida** IV o cardioversión eléctrica si inestable.

#### Pericarditis aguda

Evolución en 4 estadios:
1. **Agudo:** Elevación ST difusa y cóncava ("sonriente") + depresión PR (especialmente en II, III, aVF). Sin cambios recíprocos (excepto aVR: depresión ST + elevación PR)
2. **Subagudo precoz:** ST se normaliza, T se aplana
3. **Subagudo tardío:** T se invierte (difusamente)
4. **Resolución:** Normalización

Claves para diferenciar de IAM:
- Elevación ST difusa (no por territorio coronario)
- Concavidad superior ("sonriente" vs "convexa" del IAM)
- Depresión PR
- Sin ondas Q
- Sin cambios recíprocos (salvo aVR)

#### Onda J (de Osborn)

Deflexión positiva que aparece en el punto J (unión QRS-ST). Significativa si ≥2mm en ≥2 derivaciones contiguas.

Causas:
- **Hipotermia** (la más clásica): tamaño proporcional al grado de hipotermia
- Repolarización precoz benigna
- Hipercalcemia
- Lesión cerebral aguda
- Fibrilación ventricular idiopática

#### Marcapasos artificiales

Espiga de marcapasos: línea vertical fina ("spike") antes de la onda que estimula:
- **Spike + P:** marcapasos auricular
- **Spike + QRS ancho:** marcapasos ventricular (electrodo en VD → morfología BRI)
- **Spike + P + Spike + QRS:** marcapasos bicameral (secuencial AV)

Funciones básicas: demanda (sensa ritmo propio, inhibe si FC adecuada), frecuencia fija (asíncrono).

---

## 8. Sistemática de lectura — Checklist de guardia

> [!abstract] Checklist rápida para interpretar un ECG
>
> **DATOS BÁSICOS**
> - [ ] Nombre, fecha, calibración (25mm/s, 10mm/mV)
> - [ ] ¿ECG previo disponible para comparar?
>
> **1. FRECUENCIA**
> - [ ] ¿Bradicardia (<60)? ¿Normal (60-100)? ¿Taquicardia (>100)?
>
> **2. RITMO**
> - [ ] ¿Ritmo sinusal? (P+ en II, P ante cada QRS, QRS tras cada P)
> - [ ] ¿Regular o irregular?
> - [ ] ¿PR constante y normal (0.12-0.20s)?
> - [ ] ¿QRS estrecho (<0.12s)?
>
> **3. EJE**
> - [ ] QRS en I: ¿positivo o negativo?
> - [ ] QRS en aVF: ¿positivo o negativo?
> - [ ] Cuadrante: Normal / DEI / DED / Extremo
>
> **4. ONDAS E INTERVALOS**
> - [ ] Onda P: ¿normal? ¿alta (HAD)? ¿ancha (HAI)?
> - [ ] PR: ¿prolongado (BAV 1°)? ¿corto (WPW)?
> - [ ] QRS: ¿ancho? ¿patrón BRD/BRI?
> - [ ] Q patológicas: ¿>0.04s o >1/3 del QRS?
> - [ ] Progresión de R en precordiales: ¿normal?
>
> **5. SEGMENTO ST y ONDA T**
> - [ ] ¿Elevación ST? → ¿En qué derivaciones? ¿Cambios recíprocos?
> - [ ] ¿Depresión ST?
> - [ ] ¿T invertidas?
> - [ ] ¿T picudas (hiperkaliemia)?
>
> **6. INTERVALO QT**
> - [ ] QTc: ¿<0.44s (H) / <0.46s (M)?
>
> **7. BUSCAR PATRONES ESPECÍFICOS**
> - [ ] ¿Signos de HVI/HVD?
> - [ ] ¿S1Q3T3 (TEP)?
> - [ ] ¿Onda delta (WPW)?
> - [ ] ¿Brugada?
> - [ ] ¿Alteraciones iónicas?

---

## Enlaces

- [[MOC - Urgencias]]
- [[MOC - Cardiologia]]
- Referencia: *Dubin: Interpretación de ECG* — [[Hojas de referencia ECG.pdf]]
- [ECG-Hispana (Dubin online)](https://www.ecg-hispana.com)
- [Life in the Fast Lane - ECG Library](https://litfl.com/ecg-library/)

---

*Nota creada: 01/04/2026*
*Basada en: Dubin (Interpretación de ECG), guías ESC/AHA, UpToDate*
