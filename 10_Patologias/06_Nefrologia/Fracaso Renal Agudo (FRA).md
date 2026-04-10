---
aliases: [FRA, Fracaso Renal Agudo, Lesión Renal Aguda, LRA, AKI]
tags: [urgencias, nefro, patologia, consensos]
---
# Fracaso Renal Agudo (FRA)

**Fuente:** Guías KDIGO (Update 2023/2024), Consensos ADQI (2020-2024), Manual 12 de Octubre Cap. 35.
**Concepto clave:** Deterioro brusco de la función renal que resulta en retención de productos nitrogenados (Urea, Creatinina) y alteración de la homeostasis hidroelectrolítica. Es un síndrome crítico, más allá de un simple "valor de laboratorio alterado".

## 📏 1. Definición y Estadios (KDIGO 2023 / ADQI)

El diagnóstico clásico requiere al menos uno de los tres criterios funcionales KDIGO. No obstante, el consenso de ADQI introdujo el concepto de **FRA Subclínico** detectado por biomarcadores.

- **Criterios Clásicos (El diagnóstico exige ≥ 1):**
  1. Aumento de **Creatinina ≥ 0,3 mg/dl** en las últimas 48h.
  2. Aumento de **Creatinina ≥ 1,5 veces** el valor basal en los últimos 7 días.
  3. **Oliguria:** Diuresis < 0,5 ml/kg/h durante 6 horas.

- **Nuevo Paradigma (Biomarcadores de Estrés):**
  - **FRA Subclínico:** Paciente con Creatinina y diuresis normales (criterios clásicos negativos), pero con elevación de **TIMP-2** e **IGFBP7** (Test *NephroCheck* > 0.3). Identifica túbulos en estrés previo al fracaso funcional inminente.

### Clasificación de Gravedad (Estadios KDIGO)
| Estadio | Criterio Creatinina (Cr sérica) | Criterio Diuresis (Flujo Urinario) |
| :---: | :--- | :--- |
| **1** | Aumento de 1,5 a 1,9 veces la basal **o** incremento ≥ 0,3 mg/dl | < 0,5 ml/kg/h durante 6-12 horas |
| **2** | Aumento de 2,0 a 2,9 veces el basal | < 0,5 ml/kg/h durante ≥ 12 horas |
| **3** | Aumento ≥ 3,0 veces el basal **o** Cr ≥ 4,0 mg/dl **o** inicio de TRS | < 0,3 ml/kg/h durante ≥ 24 h **o** Anuria ≥ 12 h |
*(TRS = Terapia de Reemplazo Renal)*

## 🗂️ 2. Diagnóstico Diferencial Genérico

> [!important] Abordaje Secuencial
> En Urgencias, **siempre descartar primero lo postrenal (obstructivo)** clínico o por ecografía, **después intentar revertir lo prerrenal**, y si no responde, asumir daño **parenquimatoso**.

1. **FRA Prerrenal (Funcional) [60%]:** Riñón estructuralmente sano que sufre hipoperfusión o alteración hemodinámica. Reversible si se restaura el flujo o se reduce la congestión.
   - *Causas:* 
     - **Hipovolemia Real:** Hemorragia, deshidratación, pérdida digestiva, diuréticos excesivos.
     - **Hipovolemia Efectiva (Bajo Gasto):** IC severa, [[Shock]] cardiogénico, Cirrosis (S. Hepatorrenal).
     - **Nefropatía Congestiva (↑ Presión Venosa):** Típico del S. Cardiorrenal. El aumento de la presión en la vena renal se transmite retrógradamente al capilar peritubular.
   
   ```mermaid
   graph TD
       subgraph "Insuficiencia Cardíaca / Sobrecarga"
       IC[Fallo de Bomba] --> PVC[↑ Presión Venosa Central / PVC]
       end
       
       PVC --> VR[↑ Presión Vena Renal]
       VR --> Pcap[↑ Presión Capilar Peritubular]
       
       subgraph "Fenómenos Renales"
       Pcap --> Edema[Edema Intersticial Renal]
       Edema --> Pbowman[↑ Presión Cápsula de Bowman]
       Pbowman -- "Oposición física al filtrado" --> GFR[↓ Tasa de Filtrado Glomerular / FRA]
       end
       
       style GFR fill:#f96,stroke:#333,stroke-width:2px
   ```
2. **FRA Parenquimatoso (Intrínseco) [35%]:** Daño estructural renal.
   - *Necrosis Tubular Aguda (NTA):* La más frecuente (85% de las renales). Causada por FRA prerrenal severo/mantenido (Isquémica) o nefrotóxicos (Aminoglucósidos, Contrastes yodados, Mioglobina por rabdomiólisis).
   - *Nefritis Intersticial Aguda (NIA):* Reacción alérgica inmune (Fármacos como betalactámicos o AINEs).
   - *Patología Glomerular o Vascular:* Glomerulonefritis aguda, Vasculitis, Ateroembolia de colesterol, Microangiopatía Trombótica.
3. **FRA Postrenal (Obstructivo) [5%]:** Bloqueo del flujo urinario (requiere obstrucción **bilateral** en pacientes con dos riñones, o unilateral en monorrenos).
   - *Causas:* Hipertrofia prostática (HBP), neoplasias pélvicas, litiasis bilateral. Se descarta fácilmente con POCUS/Ecografía buscando **hidronefrosis**.

## 🔬 3. Índices Urinarios en Urgencias (Prerrenal vs. NTA)

Para diferenciar un riñón sano hipoperfundido (intentará retener avidez por el sodio y el agua) de un túbulo necrótico (NTA, que pierde su capacidad de reabsorber):

| Parámetro | Prerrenal (El túbulo funciona y retiene) | Parenquimatoso / NTA (Túbulo "roto") |
| :--- | :--- | :--- |
| **Sodio en orina (Na)** | < 20 mEq/L *(Retiene Na)* | > 40 mEq/L *(Fuga Na)* |
| **FeNa** (Fracción de Excreción de Sodio) | **< 1 %** | **> 2 %** |
| **FeUrea** (Fracción de Excreción de Urea) | **< 35 %** *(Útil si está tomando diuréticos)* | **> 50 %** |
| **Osmolaridad urinaria** | > 500 mOsm/kg *(Orina muy concentrada)* | < 350 mOsm/kg *(Isoestenuria. No concentra)* |
| **Sedimento** | Normal o cilindros **hialinos** | Cilindros **granulosos marrones** ("Muddy brown") |
*(Recuerda: Si el paciente ya toma diuréticos previos (furosemida/tiazidas), el Sodio y la FeNa estarán falsamente elevados, por lo que la **FeUrea es más fiable**).*

## 💊 4. Manejo Crítico Basado en Nueva Evidencia (STARRT-AKI)

### 1. Manejo General y Fluidoterapia
- Suspender tajantemente **nefrotóxicos** e hipotensores (IECAs, ARA-II, AINEs, Aminoglucósidos, Contrastes).
- Optimizar volemia: **Evitar exceso fisiológico de suero salino al 0.9%** (su alta carga de cloro induce vasoconstricción renal y acidosis hiperclorémica). **Preferencia por cristaloides balanceados** (Plasmalyte, Ringer Lactato).
- Mantener TAM suficiente (Noradrenalina de elección) para asegurar Presión de Perfusión Renal.

### 2. Test de Estrés con Furosemida (FST - ADQI)
Indicado en pacientes euvolémicos o sobrecargados con FRA Estadio 1-2 incipiente para predecir si el túbulo sigue vivo o precisará Diálisis pronto.
- **Pauta:** Furosemida 1 mg/kg IV (o 1,5 mg/kg si ya usaba diuréticos previos).
- **Interpretación:** Respuesta < 200 ml de diuresis en 2 horas indica alta probabilidad de progresión a FRA Estadio 3 (predice daño tubular grave irrecuperable con tratamiento conservador).

### 3. Terapias de Reemplazo Renal (TRS/TRR): El Paradigma STARRT-AKI
Los macoensayos clínicos de alto impacto mundiales (*STARRT-AKI* publicado en NEJM y *AKIKI 2* en Lancet) revolucionaron la práctica clínica sobre **cuándo iniciar diálisis**:
- **La Estrategia Diferida (Espera Vigilante) es SUPERIOR:** No existe beneficio de supervivencia al iniciar la diálisis "temprano" o de forma profiláctica. De hecho, aumenta el riesgo de dependencia crónica de la diálisis y de eventos adversos (hipotensión intradiálisis, infecciones de catéter). No se debe iniciar TRS a no ser que existan las clásicas indicaciones absolutas.
- **¿Cuándo Sí iniciar urgentemente? (Reglas Absolutas AEIOU):**
  - **A**cidosis metabólica grave refractaria (pH < 7.15) de origen primario renal.
  - **E**lectrolitos: [[Hiperpotasemia]] o Hipermagnesemia con alteraciones ECG refractarias a tratamiento médico extremo.
  - **I**ntoxicaciones dializables (Litio, Etilenglicol, Metanol, Salicilatos).
  - **O**verload (Sobrecarga de volumen refractaria - ej. Edema Agudo de Pulmón que no responde a diuréticos agresivos).
  - **U**remia sintomática (Pericarditis urémica, Encefalopatía urémica o Diátesis hemorrágica por BUN > 110 mg/dL).

## 🔗 Enlaces Relacionados
- [[Síndrome Cardiorrenal]]
- [[Shock]]
- [[Trastornos Ácido-Base - 2. Acidosis Metabólica|Acidosis Metabólica]]
