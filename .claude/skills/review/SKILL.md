---
name: revisar
description: Revisión de pares simulada calibrada al perfil de revista activo. Despacha árbitro-dominio y árbitro-métodos. Reemplaza a /review. ACTIVAR cuando el usuario diga "revisa el artículo", "evalúa el paper", "qué dirían los árbitros", "simula la revisión por pares", "quiero retroalimentación del paper".
argument-hint: "[archivo o --peer journal_key] [--paradigma cualitativo|cuantitativo|mixto]"
allowed-tools: Read,Grep,Glob,Write,Task
---

# Revisar

## Gestión de Estado (Ejecutar al Inicio y al Final)

**Al inicio:** Leer `state.json`.
- Verificar prerequisito: `redaccion.estado == "completado"`. Si no se cumple, abortar: "⚠ `/revisar` requiere que el manuscrito esté completo (`redaccion.estado = completado`)."
- Cargar `redaccion.perfil_revista_activo`, `proyecto.paradigma`, `proyecto.tipo_articulo`.

**Al final:** Actualizar en `state.json`:
- `ciclo_editorial.historial_revisiones` → añadir objeto `{fecha, veredicto, ruta_reportes}`
- `_meta.ultima_actualizacion` y `_meta.historial_skills_ejecutadas`

---

Ejecuta una revisión de pares simulada despachando dos árbitros independientes (`arbitro-dominio` y `arbitro-metodos`) calibrados al perfil de revista activo.

**Entrada:** `$ARGUMENTS` — ruta al manuscrito o `--peer [journal_key]`.

---

## Flujo

### Paso 1: Calibración de árbitros

1. Leer `state.json.redaccion.perfil_revista_activo`.
2. Si hay perfil activo, leer `informes/07_redaccion/journal_profiles/[journal_key].md`.
3. Identificar el paradigma desde `state.json.proyecto.paradigma`.

### Paso 2: Árbitro-Dominio (`arbitro-dominio`)

Evalúa la contribución sustantiva del manuscrito:
- Relevancia de la pregunta para la línea editorial de la revista.
- Posicionamiento en la literatura existente.
- Originalidad y contribución teórica/empírica.
- Coherencia del argumento de principio a fin.
- Ajuste entre las afirmaciones y la evidencia presentada.

Produce `informes/08_revision/peer_review_[fecha]/review_dominio.md`.

### Paso 3: Árbitro-Métodos (`arbitro-metodos`)

Evalúa el rigor metodológico según el paradigma del manuscrito:

**Si paradigma es Cuantitativo:**
- Validez de la estrategia de identificación causal.
- Supuestos explicitados y pruebas de robustez.
- Calidad de los datos y manejo de valores perdidos.
- Reproducibilidad del análisis.

**Si paradigma es Cualitativo:**
- Criterios de trustworthiness (credibilidad, transferibilidad, confirmabilidad, dependability).
- Reflexividad del investigador documentada.
- Trazabilidad de citas a `corpus_coded.csv`.
- Saturación teórica alcanzada y documentada.
- Análisis de casos negativos presente.
- Consistencia epistemológica (no mezcla de paradigmas).

**Si paradigma es Mixto:**
- Coherencia del diseño de integración (Creswell-Plano Clark).
- Joint display o estrategia de triangulación documentada.
- Rigor tanto en el componente cuantitativo como en el cualitativo.

Produce `informes/08_revision/peer_review_[fecha]/review_metodos.md`.

### Paso 4: Síntesis y Veredicto

Sintetizar ambas revisiones en `informes/08_revision/peer_review_[fecha]/synthesis.md`:

```markdown
## Síntesis de Revisión — [fecha]

**Árbitro-Dominio — Evaluación:**
[Resumen de fortalezas y debilidades]
**Puntuación Dominio:** [1-10]

**Árbitro-Métodos — Evaluación:**
[Resumen de fortalezas y debilidades]
**Puntuación Métodos:** [1-10]

**Veredicto:** [Accept / Minor Revisions / Major Revisions / Reject]

**Principales revisiones requeridas (ordenadas por prioridad):**
1. [Revisión mayor 1 — tipo: NUEVO_ANALISIS / CLARIFICACION / DESACUERDO / MENOR]
2. ...
```

---

## Principios
- **Calibración por Paradigma:** El árbitro-métodos no aplica criterios cuantitativos a diseños cualitativos.
- **Dos Voces Independientes:** Los dos árbitros no se comunican entre sí antes de producir sus reportes.
- **Veredicto Realista:** Calibrar la dureza de la revisión al nivel de la revista objetivo (el ASR es más exigente que una revista regional).
