---
aliases: [Gasometría, Interpretación Ácido-Base, Anión Gap, Delta Gap]
tags: [urgencias, uci, fisiologia, gasometria, acido_base]
---
# Trastornos Ácido-Base - 1. Lectura Sistemática (Los 5 Pasos)

**Basado en:** *Manual 12 de Octubre (Cap. 46) y Fundamentos de Cuidados Críticos*

Leer una gasometría arterial requiere un abordaje estructurado para no omitir patologías mixtas ocultas que podrían amenazar la vida del paciente.

### Valores normales centrales

| Parámetro | Rango normal | Ideal |
|---|---|---|
| **pH** | 7.35 – 7.45 | 7.40 |
| **PaCO₂** | 35 – 45 mmHg | 40 |
| **HCO₃⁻** | 22 – 26 mEq/L | 24 |

---

## 🧭 Los 5 Pasos de la Lectura Sistemática

| Paso | Pregunta clave | Output |
|---|---|---|
| **1** | ¿pH ácido, alcalino o normal? | Acidemia / Alcalemia / Mixto oculto |
| **2** | ¿Quién explica el pH: HCO₃⁻ o pCO₂? | Trastorno primario (4 opciones) |
| **3** | ¿La compensación cae en el rango esperado? | Detecta segundo trastorno |
| **4** | ¿Hay aniones no medidos? *(solo en acidosis metabólica)* | AG elevado vs AG normal |
| **5** | ¿La caída de HCO₃⁻ es proporcional al ↑AG? *(solo si AG elevado)* | Detecta tercer trastorno |

---

### Paso 1: Mirar el pH (Identificar el estado primario)

- **pH < 7.35:** Acidemia. Predominio de ácido.
- **pH > 7.45:** Alcalemia. Predominio de base.
- **pH Normal (7.35 – 7.45):** O paciente sano, o **trastorno mixto perfectamente compensado** (ej: Vómitos + [[Shock]]).

> [!warning] pH normal NO siempre es benigno
> Una gasometría con **pH normal pero pCO₂ y/o HCO₃⁻ anormales ES un trastorno mixto grave.** No archives la GSA hasta haber comprobado pCO₂ y HCO₃⁻.

---

### Paso 2: Identificar el trastorno primario

Compara la dirección del pH con los niveles de PaCO₂ y HCO₃⁻. El valor que "explica" el desvío del pH es el trastorno primario.

|  | **pH bajo (Acidosis)** | **pH alto (Alcalosis)** |
|---|---|---|
| **Metabólica** *(HCO₃⁻ desviado)* | HCO₃⁻ bajo | HCO₃⁻ alto |
| **Respiratoria** *(pCO₂ desviada)* | pCO₂ alta | pCO₂ baja |

---

### Paso 3: Calcular la compensación esperada

El cuerpo *nunca* hipercompensa: el pH no superará 7.40 en la dirección contraria basándose solo en compensación fisiológica. Si la compensación **no** cae en el rango esperado, hay un segundo trastorno oculto.

**Trastornos metabólicos → compensación pulmonar (rápida, minutos/horas):**

| Trastorno | Fórmula esperada | Truco rápido |
|---|---|---|
| Acidosis metabólica | `pCO₂ = (1.5 × HCO₃⁻) + 8 [± 2]` *(Winter)* | pCO₂ esperada ≈ últimos 2 decimales del pH (pH 7.28 → pCO₂ ~28) |
| Alcalosis metabólica | `pCO₂ = (0.7 × HCO₃⁻) + 21 [± 2]` | — |

**Trastornos respiratorios → compensación renal (lenta, 3 – 5 días):**

| Trastorno | Aguda *(por cada ↑ o ↓ 10 mmHg pCO₂)* | Crónica *(por cada ↑ o ↓ 10 mmHg pCO₂)* |
|---|---|---|
| Acidosis respiratoria | HCO₃⁻ sube **1** mEq/L | HCO₃⁻ sube **3 – 4** mEq/L |
| Alcalosis respiratoria | HCO₃⁻ baja **2** mEq/L | HCO₃⁻ baja **4 – 5** mEq/L |

---

### Paso 4: Calcular el Anión Gap (brecha aniónica)

**SÓLO** se calcula en *Acidosis Metabólica*. Busca aniones "no medidos" (lactato, cetonas, tóxicos).

> **Fórmula:** `Anión Gap (AG) = Na⁺ - (Cl⁻ + HCO₃⁻)` · **Normal:** 10 – 12 mEq/L

| AG | Tipo de acidosis | Mecanismo | Causas típicas |
|---|---|---|---|
| **> 12** (elevado) | Normoclorémica | Adición de ácido | MUDPILES / GOLDMARK |
| **< 12** (normal) | Hiperclorémica | Pérdida de HCO₃⁻ | Diarrea, ATR |

> [!warning] Corrección por albúmina (crítica y muy olvidada)
> Por cada **1 g/dL** que baje la albúmina respecto a 4, el AG esperado baja **2.5 puntos**.
> *Ejemplo:* Paciente desnutrido con albúmina 2 → un AG "normal" de 10 es realmente **anormal y alto** (debería ser ~7).

---

### Paso 5: Calcular el Delta Ratio (Δ/Δ Gap)

**SÓLO** si el Anión Gap está elevado. En una acidosis con AG elevado pura, por cada 1 mEq/L que sube el AG, el HCO₃⁻ debería bajar exactamente 1 mEq/L. Si no cumplen esta proporción, hay un **tercer** trastorno.

> **Fórmula:** `Δ/Δ = (AG medido - 12) / (24 - HCO₃⁻ medido)`

| Delta Ratio | Interpretación | Ejemplo clínico |
|---|---|---|
| **< 0.4** | Acidosis hiperclorémica (AG normal) concurrente pura | — |
| **0.4 – 0.8** | Mixto: Acidosis AG↑ + Acidosis AG normal | Sepsis + diarrea profunda |
| **1.0 – 2.0** | Acidosis AG elevado pura | Acidosis láctica, cetoacidosis |
| **> 2.0** | Mixto: Acidosis AG↑ + Alcalosis metabólica concurrente | Cetoacidosis + vómitos intensos · EPOC hipercapneico previo |

---

**Serie Ácido-Base:** [[Trastornos Ácido-Base - 1. Lectura Sistemática]] · [[Trastornos Ácido-Base - 2. Acidosis Metabólica]] · [[Trastornos Ácido-Base - 3. Alcalosis Metabólica]] · [[Trastornos Ácido-Base - 4. Trastornos Respiratorios]]
