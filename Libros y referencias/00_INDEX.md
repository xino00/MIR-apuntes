---
tags: [referencia, indice, biblioteca]
fecha_actualizacion: 2026-04-20
description: "Inventario de PDFs y guías clínicas del vault organizado por especialidad"
---

# 📚 Biblioteca de referencias clínicas — INDEX

Inventario y mapeo del corpus de guías clínicas en `Libros y referencias/`. Cada PDF se ha asignado a una subcarpeta por especialidad para facilitar su uso como fuente primaria del fact-check del vault y como referencia rápida en guardia.

**Total:** 50 PDFs productivos en 10 subcarpetas + 9 archivos en `_archive/` (duplicados y notas en texto plano antiguas).

## Cómo usar este índice

- **Para auditar una nota del vault**: identifica la especialidad → subcarpeta correspondiente → PDF dedicado.
- **Si una especialidad no tiene PDF dedicado**: usar `01_General/Manual 12 Octubre 2022.pdf` como fallback + WebFetch a sociedad española actualizada.
- **Cuando una guía posterior actualiza al Manual 12 Oct 2022**: prevalece la guía nueva (marcar como `[OUTDATED-MANUAL]` en informes).

## Jerarquía de fuentes

```
1. PDF dedicado de la subcarpeta de especialidad (ej. 04_Neumologia/GEMA 5.5.pdf)
2. Manual 12 Octubre 2022 (capítulo correspondiente)
3. Sociedad española actualizada (SEC, SEN, SER, SEPAR, AEDV, SEEN, AEG, AEU, semFYC, SEHH, SEORL, SEP, SECOT, SEIMC)
4. Guía internacional (KDIGO, GINA, GOLD, IDSA, EULAR, ADA, ESC, AHA/ACC, EASL)
5. UpToDate / DynaMed
```

## Mapa de cobertura PDF → especialidad → notas del vault

### 01_General/

| Archivo | Año | Sociedad | Cubre |
|---|---|---|---|
| Manual 12 Octubre 2022.pdf | 2022 | H 12 Octubre | Fallback transversal todas las especialidades |

### 02_Cardiologia/  (15 guías · cobertura 100% Cardio)

| Archivo | Año | Sociedad | Notas que valida |
|---|---|---|---|
| ACC-AHA 2025 - SCA.pdf | 2025 | ACC/AHA/ACEP/NAEMSP/SCAI | [[Síndrome Coronario Agudo]], [[SCA - Tratamiento Medico (ACC-AHA 2025)]], [[SCA - Evaluación Inicial]], [[SCA - Reperfusión]], [[SCA - Manejo Hospitalario]], [[SCA - Complicaciones y Shock]], [[Cardiopatía isquémica]] |
| AHA 2026 - TEP.pdf | 2026 | AHA/ACC | [[TEP - Tromboembolismo Pulmonar]] |
| ESC 2015 - Pericardio.pdf | 2015 | ESC | [[Pericarditis Aguda]], [[Taponamiento Cardiaco]] |
| ESC 2018 - Sincope.pdf | 2018 | ESC | [[Síncope]] |
| ESC 2020 - Cardiopatias Congenitas Adulto.pdf | 2020 | ESC | [[Cardiopatías Congénitas del Adulto]] |
| ESC 2021 - Insuficiencia Cardiaca.pdf | 2021 | ESC | [[Insuficiencia cardiaca]], [[Insuficiencia cardiaca aguda]], [[Manejo Diurético Deterioro Renal ICA]], [[Síndrome Cardiorrenal]] |
| ESC 2022 - Arritmias Ventriculares y MSC.pdf | 2022 | ESC | [[Arritmias]] (parte ventricular) |
| ESC 2023 - Endocarditis.pdf | 2023 | ESC | [[Endocarditis Infecciosa]] |
| ESC 2023 - IC Focused Update.pdf | 2023 | ESC | [[Insuficiencia cardiaca]] (SGLT2i en HFmrEF/HFpEF) |
| ESC 2023 - Miocardiopatias.pdf | 2023 | ESC | [[Miocardiopatías]] |
| ESC 2024 - Fibrilacion Auricular.pdf | 2024 | ESC/EACTS | [[Fibrilación Auricular (FA)]], [[Escala CHA2DS2-VASc y HAS-BLED]] |
| ESC 2024 - HTA.pdf | 2024 | ESC | [[Tratamiento Farmacológico de la Hipertensión]], [[HTA - Clasificación PA]], [[HTA - Resistente]], [[HTA - Riesgo Cardiovascular]], [[HTA - Daño Orgánico]], [[HTA - Diagnóstico y Causas Secundarias]], [[HTA - Fisiopatología]], [[HTA - Poblaciones Especiales]], [[HTA - Medición PA]], [[HTA - Tratamiento No Farmacológico]] |
| ESC 2024 - PAD y Aorta.pdf | 2024 | ESC | [[Síndrome Aórtico Agudo y Enfermedad Aórtica]] |
| ESC 2025 - Miocarditis y Pericarditis.pdf | 2025 | ESC | [[Pericarditis Aguda]], [[Taponamiento Cardiaco]] (focused update) |
| ESC-EACTS 2025 - Valvulopatias.pdf | 2025 | ESC/EACTS | [[Valvulopatías]] |

### 03_Nefrologia/  (4 guías)

| Archivo | Año | Sociedad | Notas que valida |
|---|---|---|---|
| KDIGO 2024 - CKD.pdf | 2024 | KDIGO | Toda nota en `06_Nefrologia/` (ERC, FG, proteinuria) |
| UpToDate - Hyperkalemia Causes.pdf | 2024 | UpToDate | [[Hiperkaliemia]] (etiología) |
| UpToDate - Hyperkalemia Manifestations.pdf | 2024 | UpToDate | [[Hiperkaliemia]] (clínica/ECG) |
| UpToDate - Hyperkalemia Treatment.pdf | 2024 | UpToDate | [[Hiperkaliemia]] (tratamiento) |

### 04_Neumologia/  (2 guías)

| Archivo | Año | Sociedad | Notas que valida |
|---|---|---|---|
| GEMA 5.5.pdf | 2024 | SEPAR/SEAIC | [[Asma - Clasificación y Control]], asma aguda y crónica |
| GOLD 2026.pdf | 2025 | GOLD | EPOC estable, exacerbaciones |

**Sin PDF dedicado:** TBC, neumonías (CAP/HAP), derrame pleural, hemoptisis (ver también `09_Urgencias_FJD/HEMOPTISIS PROCEDIMIENTO.pdf`). Fallback: Manual + WebFetch SEPAR.

### 05_Infecciosas/  (4 guías)

| Archivo | Año | Sociedad | Notas que valida |
|---|---|---|---|
| PROA Antibioticos vs 23 abril.pdf | 2025 | PROA local | Antibioterapia empírica por foco |
| PROA FJD.pdf | 2024 | FJD | Protocolo institucional FJD |
| SEPSIS 2026.pdf | 2026 | SSC | Sepsis y shock séptico |
| Evans 2021 - Surviving Sepsis.pdf | 2021 | SSC (Evans et al) | Surviving Sepsis Campaign 2021 |

### 06_Neurologia/  (1 guía)

| Archivo | Año | Sociedad | Notas que valida |
|---|---|---|---|
| Manual Cefaleas 2026.pdf | 2026 | SEN | [[Cefaleas]] y subtipos (migraña, tensional, cluster) |

**Sin PDF dedicado:** ictus, epilepsia, demencia, vértigo central, polineuropatías. Fallback: Manual + WebFetch SEN/semFYC.

### 07_Hematologia/  (2 guías)

| Archivo | Año | Sociedad | Notas que valida |
|---|---|---|---|
| UpToDate - Anemia of Chronic Disease.pdf | 2024 | UpToDate | [[Anemia de trastornos crónicos]] |
| UpToDate - Diagnostic Approach to Anemia.pdf | 2024 | UpToDate | [[Anemia]] (algoritmo dx) |

**Sin PDF dedicado:** linfomas, leucemias, citopenias, coagulopatías, transfusión. Fallback: Manual + WebFetch SEHH/ASH.

### 08_Psiquiatria/  (3 guías)

| Archivo | Año | Sociedad | Notas que valida |
|---|---|---|---|
| GPC Trastorno Mental Grave + Sustancias.pdf | 2017 | GPC SNS | Patología dual psiquiátrica + adicciones |
| Identification and Treatment of AUD.pdf | 2024 | UpToDate | [[Abstinencia alcohólica]], AUD |
| Recognition and Management of Withdrawal Delirium.pdf | 2024 | UpToDate | [[Delirium tremens]], delirium por abstinencia |

**Sin PDF dedicado:** depresión, ansiedad, esquizofrenia, urgencias psiquiátricas. Fallback: Manual + WebFetch SEP.

### 09_Urgencias_FJD/  (17 PDFs + 3 docs · protocolos institucionales Fundación Jiménez Díaz)

#### Protocolos generales urgencias

| Archivo | Tipo | Cubre |
|---|---|---|
| HUFJD 11.3.6 - Cuidados Generales Manejo Inicial.pdf | Protocolo | Manejo inicial paciente urgente |
| ANAFILAXIA ADULTOS.pdf | Algoritmo | [[Anafilaxia]] |
| HEMOPTISIS PROCEDIMIENTO.pdf | Procedimiento | [[Hemoptisis]] |
| HUFJD POLITRAUMA v0.pdf | Protocolo | [[Politrauma]], traumatismos múltiples |
| PROTOCOLO HEMATURIA.pdf | Protocolo | [[Hematuria]] |
| Atencion de la Hematuria.doc | Documento | [[Hematuria]] (segunda fuente) |
| Atencion RAO Urgencias.doc | Documento | [[RAO - Retención Aguda de Orina]] |
| CODIGO SEPSIS.docx | Código | [[Sepsis]] (activación FJD) |
| SUJECION FISICA.pdf | Procedimiento | Contención mecánica en urgencias |
| SUMISION QUIMICA FJD.pdf | Procedimiento | Sumisión química / agitación |

### 10_Digestivo/  (1 guía)

| Archivo | Año | Sociedad | Notas que valida |
|---|---|---|---|
| ACG 2021 - HDA y Ulcera.pdf | 2021 | ACG (Laine et al, Am J Gastroenterol 2021;116:899-917) | [[Hemorragia Digestiva Alta (HDA)]] (Glasgow-Blatchford, transfusión Hb 7 g/dL, eritromicina pre-endoscopia, terapia endoscópica, IBP dosis altas 72h) |

**Sin PDF dedicado (pendiente):** HDB, EII, cirrosis y complicaciones, pancreatitis, colangitis. Fallback: Manual + AEG/SEPD/Baveno VII.

#### ORL (subcarpeta `09_Urgencias_FJD/ORL/`)

| Archivo | Cubre |
|---|---|
| Protocolos ORL.pdf | Compendio general ORL |
| Absceso Periamigdalino.pdf | [[Absceso Periamigdalino]] |
| Hipoacusia.pdf | [[Hipoacusia súbita]] |
| Manejo Epistaxis 2024.pdf | [[Epistaxis]] |
| Otalgia.pdf | [[Otalgia]] |
| Otologica Traumatica.pdf | [[Patología otológica traumática]] |
| Paralisis Facial.pdf | [[Parálisis Facial]] |
| Sd Vestibular.pdf | [[Síndrome Vestibular]] |
| Traumatismo Nasal.pdf | [[Traumatismo Nasal]] |
| Tumefaccion Glandular.pdf | [[Tumefacción Glandular]] |

## Especialidades sin PDF dedicado (Fase 2 fact-check con fallback)

| Especialidad | Fallback primario | Fallback web (sociedad) |
|---|---|---|
| Digestivo (parcial, falta HDB/EII/cirrosis) | Manual 12 Oct cap GI + `10_Digestivo/ACG 2021 - HDA y Ulcera.pdf` (solo HDA) | AEG, SEPD, ESGE, Baveno VII |
| Reumatología | Manual 12 Oct cap Reuma | SER, EULAR, ACR |
| Dermatología | Manual 12 Oct cap Derma | AEDV, EADV |
| Endocrinología | Manual 12 Oct cap Endo | SEEN, ADA, ATA, ESMO |
| Urología (parte) | Manual 12 Oct cap Uro + Hematuria FJD + RAO FJD | AEU |
| Traumatología (parte) | Manual 12 Oct cap Trauma + POLITRAUMA FJD | SECOT |

## Archivos archivados (`_archive/`)

Conservados pero fuera de uso productivo:

| Archivo | Motivo |
|---|---|
| ESC 2022 - Arritmias Ventriculares y MSC (duplicado).pdf | Byte-exacto del que está en `02_Cardiologia/` |
| ANAFILAXIA ADULTOS (raiz duplicado).pdf | Byte-exacto del que está en `09_Urgencias_FJD/` |
| 1_Libros de urgencias-generales.md | Nota antigua sin contenido relevante |
| 2_Guias Neurologia.md | Nota antigua sin contenido relevante |
| cefaleas.txt, kdigo2024.txt, manual.txt, chap32.txt | Texto plano scratch, sustituido por PDFs oficiales |
| Exploracion tobillo y antepie.txt | Migrado a [[Exploración de Rodilla, Tobillo y Antepié]] |

## Mantenimiento

- Cuando bajes una guía nueva, colocarla en su subcarpeta de especialidad con nombre normalizado (`<Sociedad> <Año> - <Tema>.pdf`).
- Si la guía sustituye a una vigente, mover la antigua a `_archive/` y actualizar este INDEX.
- Las subcarpetas siguen el glob `Libros[[:space:]]y[[:space:]]referencias/**/*.pdf` del `.gitattributes`, por lo que **todos los PDFs nuevos quedan automáticamente en LFS** sin acción adicional.

---

**Hub:** [[000_INICIO]] · **Auditoría asociada:** [[INDEX|Fact-check del vault]]
