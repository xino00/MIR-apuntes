<%*
let servicio = await tp.system.prompt("Servicio consultado (Ej: Cardiología, Neurología):");
let iniciales = await tp.system.prompt("Iniciales del paciente:");
let fecha = tp.date.now("DD-MM-YYYY");
let titulo = `Opinion ${servicio} - ${iniciales} - ${fecha}`;
await tp.file.rename(titulo);
-%>
**Fecha:** <% tp.date.now("DD/MM/YYYY") %>
**Servicio consultado:** <% servicio %>
**Etiquetas:** #opinion #interconsulta #<% servicio.toLowerCase().replace(/\s+/g, "_") %>

---

> [!question] ❓ PREGUNTA CLÍNICA
> ¿Qué queremos saber del especialista?
> <% tp.file.cursor(1) %>

### 👤 Paciente (¡ANONIMIZADO!)
- **Perfil:** (edad aproximada, sexo)
- **Antecedentes relevantes:**
- **Motivo de consulta/ingreso:**

### 🩺 Situación Actual
- **Clínica:**
- **Exploración relevante:**
- **Pruebas complementarias clave:**

---

### 💬 RESPUESTA DEL ESPECIALISTA
**Fecha respuesta:**
**Especialista (iniciales/código):**

> [!success] Opinión
>

### 📋 PLAN ACORDADO
- [ ]
- [ ]

### 💡 Perla Aprendida
> [!tip] Aprendizaje
>
