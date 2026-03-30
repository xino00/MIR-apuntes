---
tags:
  - meta
  - organizacion
fecha: 2026-03-30
---

# Auditoría del Vault — Notas faltantes, temas futuros y cambios estructurales

> Estado actual: **275 archivos markdown** · 128 fármacos · 8 especialidades · 6 MOCs

---

## A) Notas que faltan por prioridad

### PRIORIDAD ALTA — Imprescindibles para guardia y rotaciones activas

**Neurología (solo 4 notas de cefaleas — la laguna más grande)**
- [ ] Ictus - Código Ictus y Manejo Agudo
- [ ] Ictus - Prevención Secundaria
- [ ] Crisis Epiléptica y Status Epiléptico
- [ ] Vértigo - Diagnóstico Diferencial (Central vs Periférico)
- [ ] Delirium / Síndrome Confusional Agudo

**Digestivo (solo dolor abdominal)**
- [ ] Hemorragia Digestiva Alta y Baja
- [ ] Pancreatitis Aguda
- [ ] Cirrosis y Descompensaciones (ascitis, PBE, encefalopatía hepática, SHR)
- [ ] EII - Brote Agudo

**Urgencias / Cross-specialty**
- [ ] Anafilaxia (material en `00_Inbox/guías 2026 anafilaxia.md` pendiente de procesar)
- [ ] Intoxicaciones Agudas (alcohol, BZD, paracetamol, CO)
- [ ] Politraumatismo - Valoración ABCDE
- [ ] Cetoacidosis Diabética / Estado Hiperosmolar
- [ ] Hipoglucemia

**Hematología**
- [ ] Anticoagulación - Manejo y Reversión (reversión DOAC, bridging)
- [ ] Neutropenia Febril
- [ ] Trombocitopenia - Diagnóstico Diferencial (PTI/TTP/HIT)

**Infecciosas**
- [ ] Meningitis y Encefalitis
- [ ] Endocarditis Infecciosa (criterios Duke)

**Cardiología (enlaces rotos en MOC)**
- [ ] Escala CHA2DS2-VASc y HAS-BLED
- [ ] Criterios de Framingham

### PRIORIDAD MEDIA — Rotaciones próximos 1-2 meses

**Nuevas especialidades:**
- [ ] Endocrinología: DM2 crónico, hipo/hipertiroidismo, insuficiencia suprarrenal, dislipemia
- [ ] Psiquiatría: agitación psicomotriz, riesgo suicida, crisis de ansiedad, depresión mayor
- [ ] Dermatología: toxicodermias/urgencias, infecciones cutáneas, lesiones sospechosas

**Huecos en especialidades existentes:**
- [ ] Neumología: NAC independiente, derrame pleural, neumotórax
- [ ] Nefrología: síndrome nefrítico/nefrótico, cólico renal/litiasis
- [ ] Reumatología: gota/cristales, artritis séptica, artritis reumatoide
- [ ] Urgencias: quemaduras, retención aguda de orina, epistaxis

### PRIORIDAD BAJA — Horizonte 3-6 meses

- [ ] ORL (otitis, faringoamigdalitis, cuerpo extraño)
- [ ] Oftalmología (ojo rojo, pérdida brusca de visión)
- [ ] Neurología profunda (neuropatías, EM brote agudo, Parkinson)
- [ ] Hematología profunda (linfoma/mieloma sospecha, indicaciones de transfusión)
- [ ] Infecciosas (tuberculosis, VIH/PEP)
- [ ] Pediatría patológica (fiebre por edad, bronquiolitis, GEA pediátrica)

---

## B) Temas futuros a desarrollar

### Nuevas carpetas en `10_Patologias/`

| Carpeta | Justificación                                                |
|---|---|
| `09_Endocrino/` | DM, tiroides, lípidos — pan de cada día en MFyC              |
| `10_Psiquiatria/` | Agitación, riesgo suicida, ansiedad — frecuente en urgencias |
| `11_Dermatologia/` | Mayor volumen en consulta de AP                              |
| `12_ORL/` | Otitis, faringitis, epistaxis — básico en AP                 |
| `13_Oftalmologia/` | Ojo rojo, pérdida de visión — triaje en urgencias            |
| `14_Pediatria/` | Ampliar más allá de las notas de dosis de guardia            |

### Nuevas subcarpetas en `30_Urgencias/`
- `Toxicologia/` — intoxicaciones
- `Trauma/` — politraumatismo, quemaduras, heridas

### Series transversales (largo plazo)
- [ ] Preoperatorio (valoración preanestésica)
- [ ] Cuidados Paliativos (manejo sintomático)
- [ ] Geriatría (VGI, fragilidad, polifarmacia)
- [ ] Medicina Preventiva (cribados, vacunación)

---

## C) Cambios estructurales pendientes

### C1. Resolver duplicado SCA
- `Síndrome Coronario Agudo (SCA).md` — 32 líneas, índice/hub
- `Síndrome Coronario Agudo.md` — 238 líneas, nota clínica completa
- **Acción:** Fusionar aliases del hub en la nota completa. Eliminar el de 32 líneas.

### C2. Resolver enlaces rotos (orphan links)

| Enlace roto | Dónde | Acción |
|---|---|---|
| `[[Escala CHA2DS2-VASc y HAS-BLED]]` | MOC Cardio | Crear en `01_Cardio/` |
| `[[Criterios de Framingham]]` | MOC Cardio | Crear en `01_Cardio/` |
| `[[MOC - Manual 12 de Octubre Urgencias]]` | MOC Urgencias | Crear como índice del Manual PDF o eliminar enlace |
| `[[Sdme Hemofagocitico]]` | MOC Hemato | Mover de `00_Inbox/` a `08_Hematologia/` |

### C3. Triaje del Inbox

| Archivo | Destino |
|---|---|
| `guías 2026 anafilaxia.md` | Procesar → `30_Urgencias/Patologia_Aguda/Anafilaxia.md` |
| `Sdme Hemofagocitico.md` | Mover → `08_Hematologia/Síndrome Hemofagocítico (HLH).md` |

### C4. MOCs que faltan

- [ ] `MOC - DIGESTIVO.md`
- [ ] `MOC - NEFROLOGIA.md`
- [ ] `MOC - REUMATOLOGIA.md`
- [ ] `MOC - ENDOCRINOLOGIA.md`
- [ ] Eventualmente: Dermatología, Psiquiatría, ORL, Oftalmología

### C5. Actualizar CLAUDE.md
- [ ] Añadir `08_Hematologia/` a la estructura
- [ ] Actualizar conteo de archivos
- [ ] Añadir carpetas nuevas según se creen

### C6. Actualizar 000_INICIO.md
- [ ] Añadir nuevos MOCs a "Especialidades"
- [ ] Agrupar por área (médica / quirúrgica / AP) cuando crezca

### C7. Inconsistencias de nombres

| Problema | Acción |
|---|---|
| `Manejo_Diuretico_Deterioro_Renal_ICA.md` (underscores) | Renombrar con espacios |
| `EPOC reagudizado.md` vs `EPOC - Exacerbación y Manejo Agudo.md` | Revisar solapamiento → fusionar si redundante |

---

## Secuencia de implementación

| Fase | Contenido | Plazo estimado |
|---|---|---|
| **1 — Limpieza** ✅ | Duplicado SCA, triaje inbox, 3 MOCs, orphan links, CLAUDE.md, INICIO.md | Completada 2026-03-30 |
| **2 — Notas críticas** | Neuro (ictus, epilepsia, vértigo, delirium), Digestivo (HDA, pancreatitis, cirrosis), Urgencias (anafilaxia, intoxicaciones), Endocrino emergencias, Hemato (anticoagulación) | 1-2 semanas |
| **3 — Expansión media** | Abrir Psiquiatría/Dermatología/Endocrino, rellenar Neumo/Nefro/Reuma | 1-2 meses |
| **4 — Profundidad** | ORL, Oftalmología, Pediatría, series transversales, poblar casos clínicos | 3-6 meses |
