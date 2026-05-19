---
date: 2026-05-19
specialty: Hematología
status: "9 hallazgos no aplicados por source policy (sin PDF en vault)"
---

# Discrepancias al aplicar fact-check de Hematología — 2026-05-19

## Resumen

De los **18 hallazgos** del informe `08_Hematologia.md`:
- **9 APLICADOS** (Sec 1 parcial — ver commit principal)
- **9 NO APLICADOS** por falta de PDF de referencia en `Libros y referencias/08_Hematologia/`

Decisión basada en source policy: **no redactar contenido clínico desde conocimiento general** ([[feedback-source-policy]]).

## Tabla de hallazgos pendientes

| # | Sev | Nota | Cita en la nota | Razón skip | PDF necesario | Acción propuesta |
|---|---|---|---|---|---|---|
| 4 | 🟠 | Anemia Ferropénica | "Respuesta esperada: reticulocitosis 5-10 días" (L78) | Auditor: "El PDF disponible no contiene este punto numérico exacto" | UpToDate *Treatment of iron deficiency anemia in adults* | Descargar PDF y reauditar |
| 5 | 🟢 | Anemia Ferropénica | "Sulfato ferroso 325 mg/8 h" (L75) | Stoffel 2017 *Lancet Haematol* + UpToDate Treatment IDA no en vault | UpToDate *Treatment of IDA* + Stoffel 2017 | Descargar PDFs; régimen días alternos es 1.ª elección actual |
| 6 | 🟢 | Anemia Ferropénica | "Hb <7-8 g/dL, o <10 g/dL con cardiopatía isquémica" (L101) | UpToDate *RBC transfusion thresholds* no en vault; controversia post-MINT 2023 | UpToDate *Indications/Hb thresholds for RBC transfusion* + MINT 2023 NEJM | Descargar + revisar |
| 8 | 🟢 | Anemia Macrocítica | "Cianocobalamina 1000 µg/día v.o. = IM si mucosa intacta" (L72) | UpToDate *Treatment of vitamin B12/folate deficiencies* no en vault | UpToDate *Treatment of B12 and folate deficiencies* | Descargar para confirmar dosis y vía |
| 9 | 🟠 | Anemia Macrocítica | "B12 equívoco 200-400 pg/mL" (L63-64) | Umbral 200-350 vs 200-400 no especificado en PDF descargado | UpToDate *Diagnosis of B12 deficiency* (cap. específico) | Descargar + actualizar a 200-350 |
| 10 | 🟠 | Anemia Hemolítica - Abordaje | "Crisis hemolítica grave (Hb <6-7 g/dL) → transfusión urgente" (L18) | UpToDate no usa umbral fijo; *AIHA management* + *Transfusion thresholds* no en vault | UpToDate *AIHA treatment* + *RBC transfusion thresholds* | Descargar + reformular a criterios genéricos |
| 12 | 🟢 | Anemia Hemolítica - Abordaje | "AIHA caliente: Prednisona 1 mg/kg/día; refractaria rituximab" (L109) | UpToDate *Warm AIHA treatment* no en vault | UpToDate *Treatment of warm AIHA in adults* | Descargar + actualizar (rituximab ahora más temprano) |
| 17 | 🟢 | Pancitopenia | "Aplasia: médula hipocelular (<25%)" (L83) | Criterios Camitta 1976 no en PDF descargado | UpToDate *Aplastic anemia: Pathogenesis, clinical manifestations* + Camitta 1976 *Blood* | Descargar + añadir criterio Camitta |
| **18** | **🔴** | **Sdme Hemofagocitico** | Nota esencialmente vacía (L11: "Calcular SCORE HEMOFAGOCITICO") | **No hay PDF en `07_Hematologia/`. Fallback fallido.** Mortalidad >50% sin tratamiento — nota crítica para urgencias | UpToDate *Clinical features and diagnosis of HLH in adults* + HLH-2004 (Henter) + HScore (Fardet 2014) + Guía SEHH | **PRIORIDAD ALTA — descargar y reescribir nota completa** con: definición HLH primario vs secundario (MAS), criterios HLH-2004 (5/8), HScore (≥169), tratamiento dex+etopósido HLH-94/2004 |

## Plan de acción recomendado

### Prioridad 1 (🔴 seguridad clínica)
- **H18 HLH:** Descargar UpToDate HLH + HLH-2004 original + Fardet 2014 + Guía SEHH. Reescribir `Sdme Hemofagocitico.md` completa. Es la única nota crítica del fact-check sin aplicar — relevante porque está enlazada desde 3 notas como red flag de derivación urgente.

### Prioridad 2 (🟠 desviaciones moderadas)
- **H4, H9, H10:** Tres hallazgos moderados que afectan a decisiones terapéuticas (Fe oral, B12 equívoco, transfusión en hemólisis). Descargar UpToDate Treatment IDA + B12/folate diagnosis + AIHA treatment + Transfusion thresholds.

### Prioridad 3 (🟢 refinamientos menores)
- H5 régimen Fe días alternos (Stoffel 2017)
- H6 umbrales transfusión post-MINT 2023
- H8 dosis B12 oral vs IM
- H12 rituximab AIHA temprano
- H17 criterios Camitta aplasia

## Notas con cambios reales aplicados (commit principal)

✅ Anemia - Abordaje General (H1+H2+H3)
✅ Anemia Normocítica (H13)
✅ ACD-AI (H14+H16)
✅ Anemia Microcítica (frontmatter; H7 ya correcto)
✅ Anemia Hemolítica - Abordaje (frontmatter; H11 ya correcto; H10 y H12 pendientes — ver tabla arriba)

## Notas sin tocar (pendientes de PDFs)

⏸ Anemia Ferropénica (H4, H5, H6)
⏸ Anemia Macrocítica (H8, H9)
⏸ Pancitopenia (H17)
⏸ Sdme Hemofagocitico (H18 🔴)

---

**Generado por:** /factcheck-apply (skill)
**Workflow:** Solo se aplican hallazgos verificables con PDFs declarados como fuente en el vault. Reauditar tras descargar PDFs faltantes.
