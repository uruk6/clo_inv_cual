---
name: propuesta
description: Construye, evalúa y adapta la propuesta / anteproyecto de investigación ajustada a los apartados, límites y criterios de la convocatoria activa. Es el entregable de la fase inicial, previo al artículo. ACTIVAR cuando el usuario diga "redacta la propuesta", "arma el anteproyecto", "construye el proyecto para la convocatoria", "evalúa mi propuesta", "cómo va mi anteproyecto", "ajusta la propuesta a los límites", "revisa el proyecto contra los criterios".
argument-hint: "[modo: redactar | evaluar | adaptar] [apartado opcional]"
allowed-tools: Read, Grep, Glob, Write, Edit, Task
---

# Propuesta

Construye el documento de **propuesta / anteproyecto** que evidencia el proyecto ante la convocatoria. Usa el agente `escritor` (outline obligatorio) y respeta el perfil de convocatoria activo.

## Gestión de Estado

**Al inicio:** Leer `state.json`.
- Cargar `convocatoria.ruta_perfil` (`informes/01_convocatoria/convocatoria_profile.md`; si vacío, sugerir `/convocatoria` primero; se puede continuar con estructura genérica avisando).
- Cargar lo disponible de `descubrimiento` (pregunta, lit review) y `estrategia` (memo) para nutrir la propuesta.

**Al final:** Actualizar `state.json.propuesta` (`ruta_documento`, `ruta_documento_final`, `apartados_completados`, `score_evaluacion`, `sanitizacion_externa_aplicada`, `estado`, `timestamp_completado`), `_meta.*` y el tablero `PROYECTO.md`.

**Entrada:** `$ARGUMENTS` — modo (`redactar` por defecto) y, opcionalmente, un apartado específico.

---

## Modo `redactar` — Construir la propuesta

### Paso 1 — Cargar el molde de la convocatoria
Leer `informes/01_convocatoria/convocatoria_profile.md`. Los **apartados obligatorios** de ese perfil son la estructura del documento; los **límites** son el techo de extensión.

Si no hay perfil de convocatoria, usar la estructura genérica de anteproyecto (problema, pregunta, justificación, objetivos, marco, metodología, ética, cronograma, referencias) y avisar que conviene cargar la convocatoria real.

### Paso 2 — Mapear evidencia disponible a cada apartado
Construir una tabla de cobertura antes de redactar:

```markdown
| Apartado exigido | Fuente disponible en el proyecto | Estado |
|---|---|---|
| Planteamiento del problema | descubrimiento.ruta_spec (informes/02_entrevista/) | ✅ / parcial / falta |
| Estado del arte | informes/03_estado_del_arte/lit_review_*.md | ... |
| Metodología | estrategia.ruta_memo (informes/05_estrategia/) | ... |
| Objetivos | [derivar de la pregunta] | ... |
| Presupuesto | [🙋 lo aporta el usuario] | ... |
```

Marcar como `[PENDIENTE: usuario]` los apartados que requieren datos que solo el investigador tiene (presupuesto, cronograma detallado, avales, equipo).

**Profundidad de fuente obligatoria (no redactar desde el resumen general):** para el estado del arte y cualquier apartado que cite literatura, no te bases únicamente en `informes/03_estado_del_arte/lit_review_*.md` — ese es un mapa, no la fuente. Antes de afirmar un argumento de un autor, consulta `master_supporting_docs/fuentes_md/[citekey].md` (texto completo) para citar el argumento real, con matices y evidencia del propio documento. Si una referencia clave todavía no tiene su `.md` de texto completo, pídeselo al Bibliotecario (`.claude/references/fuentes-pdf-workflow.md`) antes de redactar esa parte, en vez de generalizar desde el título o el resumen.

### Paso 3 — Outline obligatorio (aprobación antes de redactar)
Para cada apartado, presentar un outline párrafo por párrafo (función, evidencia/referencia `[@clave]`, conexión) y **esperar aprobación**. Despachar al agente `escritor` (par `escritor-critic`).

### Paso 4 — Redactar en Markdown (borrador de trabajo)
Producir `informes/04_propuesta/propuesta.md` (documento único, borrador de trabajo) o `informes/04_propuesta/[apartado].md` si se pide un apartado suelto.
- Respetar el orden y los nombres de apartado del perfil de convocatoria.
- Citación `[@clave]` verificada contra `Bibliography_base.bib`.
- Marcar `[PENDIENTE]`/`[VERIFICAR]` lo que el usuario debe completar.
- No exceder el límite de extensión; avisar si se acerca.
- `propuesta.md` es el **borrador de trabajo**: puede y debe tener marcadores `[PENDIENTE]`/`[VERIFICAR]` mientras se construye. La versión que se somete a la convocatoria es otra (ver Paso 5).

### Paso 5 — Sanitización externa (gate obligatorio antes de dar la propuesta por lista)

La propuesta la va a leer y calificar alguien externo al proceso (un evaluador de la convocatoria). Ese documento **no puede** delatar que fue construido con este asistente ni contener nada que solo tiene sentido dentro del proyecto interno.

1. Verificar que **todos** los `[PENDIENTE]`/`[VERIFICAR]`/`[ASUMIDO]` estén resueltos con el usuario. Si queda alguno sin resolver, no generar la versión final — informar cuáles faltan.
2. Barrer el texto y eliminar/reescribir cualquier referencia interna al proceso: nombres de agentes ("el Bibliotecario encontró...", "el Analista-IA calculó..."), rutas del proyecto (`state.json`, `informes/`, `data/cleaned/`), menciones a "el sistema", "la IA identificó", marcadores técnicos (`ID_Cita`, `[NUEVA_CANDIDATA]`), o cualquier meta-comentario sobre cómo se construyó el documento. El argumento debe sostenerse por sí mismo, como lo escribiría el investigador.
3. Generar la copia limpia en `informes/04_propuesta/propuesta_final.md` (nunca sobrescribe `propuesta.md`, que sigue siendo el borrador de trabajo).
4. Registrar `state.json.propuesta.ruta_documento_final` y `sanitizacion_externa_aplicada = true`.
5. Presentar al usuario un resumen de qué se limpió (para que confirme que no se perdió nada importante).

### Paso 6 — Quality Self-Check
```markdown
- [ ] Todos los apartados obligatorios de la convocatoria están presentes y nombrados igual
- [ ] Extensión dentro del límite del perfil
- [ ] Coherencia problema → pregunta → objetivos → metodología
- [ ] Citas [@clave] existentes en Bibliography_base.bib
- [ ] Argumentos de literatura anclados en master_supporting_docs/fuentes_md/, no solo en el resumen del lit review
- [ ] Consideraciones éticas incluidas (si la convocatoria las exige)
- [ ] Marcadores [PENDIENTE]/[VERIFICAR] señalados al usuario (en el borrador)
- [ ] propuesta_final.md generada, sin marcadores ni referencias internas al proceso (Paso 5)
```

---

## Modo `evaluar` — Calificar la propuesta contra los criterios

Simula la evaluación de la convocatoria usando sus **criterios ponderados**.

1. Leer `informes/04_propuesta/propuesta.md` (o `propuesta_final.md` si ya existe) y los `criterios_evaluacion` del perfil.
2. Para cada criterio, dar puntaje y justificación con evidencia del texto.
3. Producir `informes/04_propuesta/evaluacion_propuesta_[fecha].md`:

```markdown
## Evaluación de la Propuesta — [convocatoria] — [fecha]

| Criterio | Peso | Puntaje | Ponderado | Observación |
|---|---|---|---|---|
| Calidad técnica y científica | 40% | x/100 | ... | ... |
| Pertinencia e impacto | 25% | ... | ... | ... |
| ... | ... | ... | ... | ... |
| **Total** | 100% | | **N/100** | |

**Veredicto estimado:** [Financiable / Requiere ajustes / No competitiva]
**Frente al puntaje mínimo ([min]):** [por encima / por debajo]

### Debilidades por criterio (priorizadas)
1. [criterio] — [problema concreto] → [acción: skill a invocar]

### Fortalezas a conservar
- ...
```

Ser honesto y calibrado: si no es competitiva, decirlo con evidencia.

---

## Modo `adaptar` — Ajustar a límites y apartados

Cuando la propuesta excede el límite o le faltan/sobran apartados:
1. Comparar la estructura actual contra `apartados_obligatorios` del perfil.
2. Reordenar/renombrar apartados para calzar con el formato exigido.
3. Recortar al límite de extensión priorizando lo que puntúa en los criterios.
4. Guardar como `informes/04_propuesta/propuesta_[convocatoria_key].md` (no sobrescribe el original).
5. Reportar cambios en `informes/04_propuesta/adaptacion_propuesta_[fecha].md`.
6. Si la adaptación se hace sobre `propuesta_final.md` (ya sanitizada), repetir el Paso 5 (Sanitización externa) sobre el resultado antes de entregarlo.

---

## Principios
- **La convocatoria es el molde.** Apartados, orden, límites y criterios salen del perfil, no de una plantilla genérica.
- **Outline antes de redactar.** Nada se escribe sin aprobación.
- **Evidencia sobre relleno.** Reutilizar los artefactos de descubrimiento y estrategia; lo que falte se marca `[PENDIENTE]`.
- **Profundidad sobre resumen.** Los argumentos de literatura se anclan en el texto completo de la fuente (`master_supporting_docs/fuentes_md/`), no en el resumen general del estado del arte.
- **Documento externo, no interno.** La versión que se entrega (`propuesta_final.md`) es un documento que un evaluador externo va a juzgar: no puede mencionar agentes, rutas del proyecto ni el proceso que la produjo.
- **Roles claros.** Presupuesto, cronograma, avales y equipo los aporta el usuario (ver `roles-usuario-ia.md`).
- **Puente al artículo:** una vez financiado/aprobado, la propuesta alimenta `/estrategia` y `/redactar` para el artículo final.
