# MIR · Apuntes de Medicina Familiar y Comunitaria

Apuntes clínicos de la residencia MIR de Medicina Familiar y Comunitaria (Madrid), escritos como un vault de [Obsidian](https://obsidian.md) y orientados a la práctica: consulta de Atención Primaria y guardias de urgencias.

**🌐 Léelos en la web: [mirapuntes.pages.dev](https://mirapuntes.pages.dev)**

> [!WARNING]
> Material personal de estudio y consulta rápida, en desarrollo. No sustituye el juicio clínico, las guías de práctica clínica oficiales ni la supervisión de un especialista. Puede contener errores, simplificaciones o información desactualizada: comprueba siempre dosis y pautas en la fuente original antes de aplicarlas.

## Qué hay

| Carpeta | Contenido |
|---|---|
| [`10_Patologias/`](10_Patologias/) | +250 notas de patología organizadas por especialidad |
| [`20_farmacos/`](20_farmacos/) | +140 fichas de fármacos (mecanismo, indicaciones, contraindicaciones, RAM, posología) |
| [`30_Urgencias/`](30_Urgencias/) | Guías de guardia (MUST), patología aguda, iónico y ácido-base, exploración física |
| [`50_Guardias/`](50_Guardias/) | Plantillas copia-pega para la guardia (curas, policlínica, boxes, COT, pediatría) |
| [`90_MOCs/`](90_MOCs/) | Índices de navegación: [portada](90_MOCs/000_INICIO.md) y un MOC por especialidad |
| [`Curso COT apuntes/`](Curso%20COT%20apuntes/) | Apuntes del curso de Cirugía Ortopédica y Traumatología (COT) |
| [`Libros y referencias/`](Libros%20y%20referencias/) | Biblioteca de fuentes primarias (PDF en Git LFS) |

Especialidades: cardiología, neurología, infecciosas, digestivo, neumología, nefrología, reumatología, hematología, endocrino, ORL, urología, traumatología, dermatología, psiquiatría, ginecología y heridas.

## Cómo usarlo

- **En el navegador**: [mirapuntes.pages.dev](https://mirapuntes.pages.dev), con buscador, enlaces entre notas y vista de grafo.
- **En Obsidian**: clona el repo y ábrelo como vault. Las notas usan wikilinks `[[...]]`, así que la navegación funciona en Obsidian o en la web, no en la vista de archivos de GitHub.

  ```bash
  git clone https://github.com/xino00/MIR-apuntes.git
  ```

  Los PDF de `Libros y referencias/` están en Git LFS; para descargarlos, ejecuta `git lfs pull` dentro del repo.

## Fuentes

El contenido sale de fuentes primarias, por este orden de preferencia: guías y documentos de referencia de cada especialidad, *Manual de Diagnóstico y Terapéutica Médica* del Hospital 12 de Octubre (2022), sociedades científicas españolas y guías internacionales (ESC, AHA/ACC, KDIGO, GOLD, GINA, IDSA…). Las fichas de fármacos se contrastan con la ficha técnica de [CIMA (AEMPS)](https://cima.aemps.es). Las notas citan su fuente, y las que han pasado una revisión llevan la fecha en `last_fact_checked`.

¿Has encontrado un error? Abre un [issue](https://github.com/xino00/MIR-apuntes/issues).

## Publicación

Cada push a `main` construye la web con [Quartz](https://quartz.jzhao.xyz) v4.5.2 y la despliega en Cloudflare Pages ([`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)). La configuración del sitio está en [`.github/quartz.config.ts`](.github/quartz.config.ts).

## Licencia

Juan Arenas Montiel. Contenido bajo licencia [CC BY-SA 4.0](LICENSE): puedes compartirlo y adaptarlo citando la autoría y manteniendo la misma licencia.
