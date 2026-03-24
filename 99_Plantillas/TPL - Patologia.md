
<%*
let titulo = await tp.system.prompt("Nombre de la Patología:");
await tp.file.rename(titulo);
-%>
**Fecha de revisión:** <% tp.date.now("DD/MM/YYYY") %>
**Etiquetas:** #patologia <% tp.file.cursor(1) %>

---
> [!warning] 🚨 SIGNOS DE ALARMA (Red Flags)
> - Escribe aquí qué te debe asustar o requerir ingreso inmediato.

### 📋 Clínica Principal
- 

### 🔬 Diagnóstico / Criterios
- 

### 💊 Tratamiento
- **Urgencias / Agudo:** 
- **Mantenimiento / Alta:** 
### 🔗 Enlaces / Bibliografía
- [Consultar <% tp.file.title %> en OpenEvidence](https://www.openevidence.com/search?q=<% tp.file.title %>)
-