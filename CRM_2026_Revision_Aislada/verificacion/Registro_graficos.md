# Revisión de los esquemas del HTML

Fecha: 30 de septiembre de 2026. Petición: «Hazlo con más gráficos el HTML».

## Alcance

Se han añadido 12 esquemas nativos de HTML/CSS, con conectores SVG sencillos en el mapa CRM. No hay imágenes incrustadas, bibliotecas externas ni recursos de red necesarios para representar los diagramas. Las explicaciones proceden del Markdown de esta misma revisión; esta ampliación visual no incorpora fuentes clínicas nuevas ni modifica sus límites documentales o regulatorios.

| Esquema | Desarrollo clínico de origen |
|---|---|
| 01. Mapa CRM | Sección 1: relaciones entre metabolismo, función renal y corazón |
| 02. Matriz renal interactiva | Sección 2.4: G1–G5 y A1–A3; unidades, cronicidad y otros marcadores |
| 03. Selección en DM2 | Algoritmo 1 |
| 04. Confirmación de ERC | Algoritmo 2 |
| 05. DM2 con ERC | Algoritmo 3 |
| 06. Diagnóstico de IC | Algoritmo 4 |
| 07. Tratamiento de IC | Algoritmo 5 |
| 08. Integración del riesgo | Algoritmo 6 |
| 09. Finalidades del tratamiento | Sección 4.1 |
| 10. Creatinina y volumen | Sección 5.2 |
| 11. Potasio | Sección 5.4 |
| 12. Calendario de controles | Sección 6.1 |

## Integridad y comprobaciones

- Markdown original: 13.599 palabras y 98.153 bytes. SHA256 conservado: `55ba2b03fc3eae03b0645fbf632cca44cfb0fb1b15e25777ddeccf9bdda99e05`.
- El generador lee el Markdown canónico; ya no lo reconstruye ni lo sobrescribe. Tras retirar únicamente los esquemas añadidos del HTML, su texto coincide con el renderizado del Markdown.
- Se conservan las 11 tablas y los 54 encabezados de la revisión base. La matriz añade una tabla explicativa.
- Los 83 enlaces internos resuelven a destinos existentes. No hay identificadores duplicados. Cada esquema ofrece enlace a su fuente y al desarrollo correspondiente; 11 enlaces de ampliación saltan directamente al texto posterior al gráfico.
- Los seis algoritmos tienen una conducta final explícita. Se han revisado los límites y las excepciones que podrían perderse al resumir: cronicidad, G1/G2 A1 sin daño adicional, sospecha de IC con péptido bajo, población renal específica de semaglutida, un único ARM, diferencias entre creatinina y FGe, y contexto de descongestión.
- Las discrepancias entre ESC/ERA y los anexos de IC en hiperpotasemia permanecen visibles, abiertas por defecto. El esquema distingue el límite inclusivo de 6,0 del límite estricto de algunos anexos. No presenta una franja de seguridad universal.
- Comprobadas las 18 selecciones de la matriz renal en navegador y la activación por teclado. Se verificó el texto de salida, incluyendo los signos `<` y `>` de G5/A1/A3. La matriz clasifica; no calcula un riesgo individual.
- Comprobado el cambio de explicación al seleccionar Riñón en el mapa CRM.
- Comprobado el salto desde el gráfico de diagnóstico de IC a su párrafo de población y explicación completa.
- Revisión visual en escritorio de 1280 × 720 y móvil de 390 × 844. Sin desbordamiento horizontal del documento ni del texto de los esquemas. La matriz cabe en su contenedor móvil de 303 píxeles; las ramas se apilan en una sola columna.
- Corregida accesibilidad de las flechas: solo el trazo decorativo queda oculto; las condiciones escritas permanecen accesibles.
- Consola de la página sin errores capturados durante la revisión. Restablecido el tamaño de ventana tras la prueba móvil.

Las comprobaciones de esta edición se realizaron mediante HTTP local. No se afirma una nueva prueba de apertura `file://` ni una revisión de impresión en PDF. La validación visual no constituye validación clínica externa.

## Recuperación y reproducción

Copia previa: `antes_graficos_20260930_112546/`, dentro de esta carpeta de verificación. Conserva el HTML anterior, su generador y el informe estructural previo.

Generación: `python3 verificacion/generar_html.py`, desde la carpeta de la revisión. `graficos_crm.py` contiene los esquemas y su presentación; `validacion_estructural.json` recoge los tamaños, huellas y resultados actuales. El registro clínico original permanece en `Registro_de_verificacion.md`.
