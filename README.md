# MIR · Apuntes

Vault de Obsidian de un residente de **Medicina de Familia** en Madrid. Centro de referencia clínica durante rotaciones hospitalarias, guardias de urgencias y registro de casos clínicos anónimos.

## 🌐 Acceso

**Sitio público:** 👉 **https://mirapuntes.pages.dev**

> Desplegado automáticamente con Quartz + Cloudflare Pages en cada push a `main`

---

## 📚 Estructura del Vault

| Carpeta | Contenido | Archivos |
|---------|-----------|----------|
| **10_Patologias/** | Patología crónica/electiva por especialidad (7 servicios: Cardio, Neuro, Infecciosas, Digestivo, Neumología, Nefrología, Reumatología) | ~200 |
| **20_farmacos/** | Fichas de fármacos (una por archivo) | 128 |
| **30_Urgencias/** | Protocolos de guardia urgente (Patología aguda, Iones, Exploración física) | 15+ |
| **40_Casos_clinicos/** | Casos anónimos de pacientes | Plantilla lista |
| **50_Guardias/** | Logs de guardia por fecha | ~150 |
| **60_Pase_planta/** | Notas de pase de planta | Plantilla lista |
| **90_MOCs/** | Índices de navegación por especialidad | 10+ |
| **99_Plantillas/** | Plantillas Obsidian (Templater) | 5 |
| **Libros y referencias/** | PDFs (Manual 12 Octubre, KDIGO 2024, Sepsis 2026, etc.) | Versionados con Git LFS |

---

## 🛠️ Tecnologías

- **Obsidian** — Editor y motor de búsqueda local
- **Quartz v4** — Generador de sitio estático desde wikilinks
- **Cloudflare Pages** — Hosting + deploy automático
- **GitHub Actions** — CI/CD con validación de builds
- **Git LFS** — Versionado eficiente de PDFs grandes

---

## 📖 Convenciones de contenido

Todas las notas médicas siguen esta estructura:

```markdown
---
tags: [especialidad, tipo]
specialty: Especialidad
date: YYYY-MM-DD
---

## Definición
¿Qué es?

## Etiología
¿Por qué ocurre?

## Diagnóstico
¿Cómo se diagnostica?

## Tratamiento
¿Cómo se trata?

## Referencias
[[MOC - Especialidad]]
[[Nota relacionada]]
```

**Reglas importantes:**
- Usa `[[wikilinks]]` para referencias internas (Obsidian las detecta)
- En YAML frontmatter, NO uses wikilinks — usa texto plano
- Cada nota nueva debe agregarse al MOC correspondiente

---

## 🚀 Inicio rápido

### Clonar y abrir localmente

```bash
# 1. Clonar (incluye PDFs con Git LFS)
git clone git@github.com:xino00/MIR-apuntes.git
cd MIR-apuntes

# 2. Instalar Git LFS (si no lo tienes)
git lfs install

# 3. Descargar archivos LFS
git lfs pull
```

### Abrir en Obsidian

1. Descargar desde https://obsidian.md
2. **File** → **Open vault as folder** → selecciona la carpeta clonada
3. Las configuraciones (plugins, temas) ya están en `.obsidian/`

### Plantillas disponibles

| Plantilla | Uso |
|-----------|-----|
| `TPL - Farmaco.md` | Nueva ficha de fármaco |
| `TPL - Patologia.md` | Nueva nota de patología |
| `TPL - Casos clinicos.md` | Caso clínico anónimo |
| `TPL - Guardia.md` | Registro de guardia |
| `TPL - PASE DE PLANTA.md` | Pase de planta |

---

## 🔄 Sincronización

### Automática (cron)

Cada día a las **22:00**, un cron ejecuta `sync.sh`:
- Detección automática de cambios
- Commit con fecha/hora
- Push a main
- Deploy a https://mirapuntes.pages.dev (~2 minutos)

### Manual

```bash
./sync.sh
```

---

## 🔌 Obsidian Local REST API

El vault tiene el plugin **Local REST API** para programación local.

**⚠️ IMPORTANTE:** Nunca guardes el token en git (incluso en repos privados). Usa variables de entorno.

```bash
# 1. Generar token en Obsidian Settings → Local API → Generate new token

# 2. Guardar en variable de entorno:
export OBSIDIAN_API_TOKEN="<tu_token>"

# 3. Usar en scripts:
curl http://localhost:27123/active/ -H "Authorization: Bearer $OBSIDIAN_API_TOKEN"
```

Puerto HTTP: **27123** | HTTPS: **27124**

Ver `.CLAUDE.md` para más detalles.

---

## 📄 Licencia & Privacidad

- Sin licencia explícita
- Contenido privado de uso personal y educativo
- Los PDFs versionados con Git LFS son referencias clínicas públicas

---

**Hecho con ❤️ durante rotaciones hospitalarias y guardias de urgencias**
