---
name: responder-arbitros
description: Clasifica comentarios de árbitros, los enruta al agente apropiado y produce carta de respuesta. Reemplaza a /revise. ACTIVAR cuando el usuario diga "hay que responder los comentarios del árbitro", "llegaron las revisiones", "tengo que corregir el paper según los reviewers", "procesa las observaciones del referee".
argument-hint: "[ruta_reportes_arbitros]"
allowed-tools: Read,Grep,Glob,Write,Edit,Task
---

# Responder-Arbitros

## Gestión de Estado (Ejecutar al Inicio y al Final)

**Al inicio:** Leer `state.json`.
- Verificar prerequisito: `ciclo_editorial.historial_revisiones` no vacío. Si está vacío, abortar: "⚠ `/responder-arbitros` requiere haber ejecutado `/revisar` primero."
- Cargar `redaccion.perfil_revista_activo`, `proyecto.paradigma`.

**Al final:** Actualizar en `state.json`:
- `ciclo_editorial.carta_respuesta_arbitros` → ruta de `paper/response_letter.md`
- `ciclo_editorial.historial_revisiones` → actualizar con estado `"respondido"`
- `redaccion.estado` → `"revision_completada"` (si todos los comentarios están resueltos)
- `_meta.ultima_actualizacion` y `_meta.historial_skills_ejecutadas`

---

Clasifica y resuelve los comentarios de árbitros, produciendo carta de respuesta con mapeo punto a punto.

**Entrada:** `$ARGUMENTS` — ruta a la carpeta con reportes de árbitros (ej. `informes/08_revision/peer_review_2026-04-16/`).

---

## Flujo

### Paso 1: Lectura y Clasificación de Comentarios

Leer todos los archivos de revisión. Para cada comentario individual:

```markdown
**Comentario [N]** — Árbitro [Dominio/Métodos], línea [X]
**Tipo:** [NUEVO_ANALISIS | CLARIFICACION | DESACUERDO | MENOR]
**Texto del comentario:** [cita literal]
**Acción requerida:** [descripción concisa]
**Agente responsable:** [analista-ia / escritor / Usuario]
```

**Tipos de comentario:**
- **NUEVO_ANALISIS:** Requiere re-análisis o datos adicionales → enrutar al `analista-ia` (`/analizar`).
- **CLARIFICACION:** Solo requiere edición de texto → enrutar al `escritor`.
- **DESACUERDO:** El autor disiente de la objeción → flag al usuario para redactar respuesta diplomática.
- **MENOR:** Tipografía, formato, estilo → `escritor` directo.

### Paso 2: Ejecución de Cambios

Para cada comentario, ejecutar la acción según el tipo:
- **NUEVO_ANALISIS:** Informar al usuario que se requiere re-análisis. Sugerir invocar `/analizar` con la instrucción específica.
- **CLARIFICACION / MENOR:** Editar directamente el manuscrito en `paper/sections/`.
- **DESACUERDO:** Redactar respuesta diplomática para la carta, sin modificar el manuscrito salvo acuerdo del usuario.

### Paso 3: Carta de Respuesta

Generar `paper/response_letter.md` con la siguiente estructura:

```markdown
# Carta de Respuesta a los Árbitros

**Manuscrito:** [título]
**Fecha de envío original:** [fecha]
**Fecha de revisión:** [fecha actual]

Estimado/a Editor/a:

Agradecemos los comentarios constructivos de los árbitros. A continuación respondemos punto a punto.

---

## Árbitro 1 (Dominio)

### Comentario 1.1
**Texto del árbitro:** "[cita literal]"
**Nuestra respuesta:** [explicación]
**Cambio en el manuscrito:** [descripción del cambio + referencia a la sección/página] o "Sin cambio — [justificación]"

[...]

---

## Árbitro 2 (Métodos)

[idem]

---

Quedamos a disposición para cualquier consulta adicional.

Atentamente,
[Autores]
```

---

## Principios
- **Respuesta Punto a Punto:** Cada comentario recibe respuesta explícita, nunca agrupada genéricamente.
- **Cambio Documentado:** Toda modificación al manuscrito queda referenciada en la carta (sección/página).
- **Desacuerdo Diplomático:** Cuando el autor disiente, la respuesta agradece la perspectiva, explica el razonamiento y ofrece alternativa si es posible.
- **No Regresión:** Las revisiones no pueden empeorar aspectos que el árbitro no cuestionó.
