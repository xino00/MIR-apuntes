# MIR · Apuntes

Vault de Obsidian de un residente de **Medicina de Familia** en Madrid. Centro de referencia clínica durante rotaciones hospitalarias, guardias de urgencias y registro de casos clínicos.

## 🌐 Acceso

**Sitio público:** https://mirapuntes.pages.dev

> Desplegado automáticamente con Quartz + Cloudflare Pages en cada push a main

## 📚 Estructura del Vault

```
10_Patologias/          Patología crónica/electiva por especialidad
  01_Cardio/            02_Neuro/  03_Infecciosas/  04_Digestivo/
  05_Neumologia/        06_Nefrologia/  07_Reumatologia/

20_farmacos/            128 fichas de fármacos (una por archivo)

30_Urgencias/           Hub central de guardia
  Patologia_Aguda/      Shock, SDRA, IRA, Dolor torácico, Disnea
  Ionico_AcidoBase/     Iones, equilibrio ácido-base
  Exploracion_Fisica/   Exploración de Rodilla, Tobillo y Antepié

40_Casos clinicos/      Casos clínicos anónimos

50_Guardias/            Registros de guardia por fecha

60_Pase de planta/      Notas de pase

90_MOCs/                Índices de navegación por especialidad

99_Plantillas/          Plantillas Templater para automatizar

Libros y referencias/   PDFs (Manual 12 Octubre, KDIGO 2024, Sepsis 2026, etc.)
```

## 🛠️ Tecnologías

- **Obsidian** — Editor y motor de búsqueda local
- **Quartz v4** — Generador de sitio estático desde wikilinks
- **Cloudflare Pages** — Hosting + CI/CD
- **GitHub Actions** — Automatización del deploy

## 📖 Notas sobre el contenido

Todas las notas siguen esta estructura:

1. **YAML frontmatter** — Metadatos (tags, especialidad, fecha)
2. **Definición** — ¿Qué es?
3. **Etiología** — ¿Por qué ocurre?
4. **Diagnóstico** — ¿Cómo se diagnostica?
5. **Tratamiento** — ¿Cómo se trata?
6. **Wikilinks** — Referencias a otras notas y MOCs

> **Importante:** Se usan wikilinks (`[[Note Name]]`) para navegación. Los links en YAML frontmatter deben ser texto plano.

## 🖥️ Uso local

1. **Clonar el repositorio:**
   ```bash
   git clone git@github.com:xino00/MIR-apuntes.git
   cd MIR-apuntes
   ```

2. **Abrir con Obsidian:**
   - Descargar Obsidian desde https://obsidian.md
   - File → Open vault as folder → selecciona la carpeta clonada
   - Las configuraciones de plugins ya están en `.obsidian/`

3. **Plantillas disponibles:**
   - `TPL - Farmaco.md` — Ficha de fármaco
   - `TPL - Patologia.md` — Nota de patología
   - `TPL - Casos clinicos.md` — Caso clínico anónimo
   - `TPL - Guardia.md` — Registro de guardia
   - `TPL - PASE DE PLANTA.md` — Nota de pase

## 🔄 Sincronización automática

Existe un cron que ejecuta `sync.sh` cada día a las 22:00, haciendo commit + push de cambios. Los cambios se despliegan automáticamente a https://mirapuntes.pages.dev en ~2 minutos.

Para sincronizar manualmente:
```bash
./sync.sh
```

## 🔌 Obsidian Local REST API

El vault tiene el plugin **Local REST API** activo. Mientras Obsidian esté abierto:

```bash
# Leer la nota activa
curl http://localhost:27123/active/ \
  -H "Authorization: Bearer YOUR_TOKEN"

# Abrir una nota específica
curl -X POST "http://localhost:27123/open/10_Patologias%2F01_Cardio%2FFA.md" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

Puerto HTTP: **27123** | HTTPS: **27124**

## 📄 Licencia

Sin licencia explícita — contenido privado de uso personal y educativo.

---

Hecho con ❤️ y muchas guardias de urgencias
