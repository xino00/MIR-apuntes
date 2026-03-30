<%*
let fecha = tp.date.now("DD-MM-YYYY");
let tipo = await tp.system.prompt("¿Dónde es la guardia? (Ej: Urgencias, Planta, UCI):");
let titulo = `Guardia ${fecha} - ${tipo}`;
await tp.file.rename(titulo);
-%>
**Fecha:** <% tp.date.now("DD/MM/YYYY") %>
**Ubicación:** <% tipo %>
**Etiquetas:** #guardia 

---
> [!todo] 📝 TAREAS PENDIENTES GLOBALES
> - [ ] Revisar analíticas pendientes
> - [x] Firmar altas
> - [ ] <% tp.file.cursor(1) %>

### 🛏️ PACIENTES / PENDIENTES DE PRUEBAS
*(Recuerda: Solo iniciales y número de cama/box)*

- **Box ___:** [Iniciales]. Pendiente de: 
	- [ ] Analítica
	- [ ] Rx Tórax
	- [ ] Valoración por [Especialidad]

- **Box ___:** [Iniciales]. Pendiente de:
	- [ ] 
	- [ ] 

### 🔄 PASE DE GUARDIA (Para el compañero del turno siguiente)
- 

### 💡 NOTAS RÁPIDAS (Para pasar a Casos Clínicos el fin de semana)
-