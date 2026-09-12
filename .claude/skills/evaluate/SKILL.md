---
name: evaluar
description: Evaluación diagnóstica de cualquier componente del proceso de investigación — estado del arte, metodología, corpus, codebook, análisis, o coherencia global. No requiere el pipeline completo. Detecta dónde está el investigador, evalúa, y propone mejoras concretas. ACTIVAR cuando el usuario diga "evalúa mi metodología", "cómo está mi estado del arte", "revisa mi diseño de investigación", "qué tan bien está el corpus", "hay algún problema con mi codificación", "qué le falta a mi investigación", "diagnóstica el proyecto", "cómo voy con la investigación", "qué me recomiendas mejorar".
argument-hint: "[componente: lit | metodologia | corpus | codebook | analisis | proyecto] [--archivo ruta_opcional]"
allowed-tools: Read,Grep,Glob,Write,Task
---

# Evaluar

Evaluación diagnóstica flexible de cualquier componente del proceso de investigación. Funciona **desde cero** (si el proyecto acaba de comenzar) o **desde el punto donde está el investigador** (leyendo `state.json`).

**No bloquea por prerequisitos del pipeline.** Evalúa lo que existe, sea mucho o poco.

**Entrada:** `$ARGUMENTS` — componente a evaluar + ruta opcional a un archivo específico.

---

## Paso 0: Diagnóstico de Estado (Siempre Primero)

Antes de evaluar cualquier componente, leer:
1. `state.json` — qué fases están completadas, qué rutas de artefactos existen.
2. `MEMORY.md` — decisiones y hallazgos previos.
3. Si `state.json` no existe o está vacío → el investigador está en fase inicial. No abortar — adaptar la evaluación a lo que haya disponible.

Anunciar el diagnóstico inicial:

```markdown
## Diagnóstico de Estado del Proyecto

**Fases completadas:** [lista o "ninguna — proyecto en fase inicial"]
**Artefactos disponibles:** [lista de archivos clave encontrados]
**Paradigma detectado:** [desde state.json o "no declarado aún"]
**Punto de entrada:** [dónde está el investigador en el pipeline]

Procediendo a evaluar: [componente solicitado]
```

---

## Modos de Evaluación

### `/evaluar lit` — Evaluación del Estado del Arte

Evalúa la revisión de literatura existente, sin importar si fue producida con el sistema o externamente.

**Lee (lo que exista):**
- `informes/03_estado_del_arte/lit_review_*.md` o equivalente
- `Bibliography_base.bib` (claves disponibles)
- Especificación de investigación (`descubrimiento.ruta_spec` en state.json)

**Si no hay nada:** pedir al usuario que comparta la lista de referencias o el resumen de lo revisado.

**Dimensiones de evaluación:**

| Dimensión | Preguntas | Severidad si falla |
|---|---|---|
| **Cobertura temática** | ¿Están las corrientes teóricas principales? ¿Hay vacíos evidentes? | Alta |
| **Balance temporal** | ¿Hay clásicos fundacionales + estado del arte reciente? ¿Sesgo presentista o anticuario? | Media |
| **Diversidad geográfica** | ¿Solo literatura anglosajona? ¿Falta perspectiva latinoamericana? | Media |
| **Coherencia con la pregunta** | ¿La literatura seleccionada responde directamente a la pregunta de investigación? | Alta |
| **Diálogo con el vacío** | ¿Se identifica claramente qué no se sabe y por qué este estudio aporta? | Alta |
| **Honestidad bibliográfica** | ¿Hay citas no verificadas? ¿Claves BibTeX sin fuente real? | Crítica |
| **Revistas CS relevantes** | ¿Se incluyeron revistas latinoamericanas clave? (ver lista en `/descubrir lit`) | Media |

**Salida:** `informes/03_estado_del_arte/evaluacion_lit_[fecha].md` con:
- Puntuación por dimensión (1-5)
- Vacíos específicos identificados (con ejemplos de lo que falta)
- Lista de autores/corrientes ausentes que deberían estar
- Propuestas de búsqueda para cerrar los vacíos
- Acción recomendada: `/descubrir lit [tema específico faltante]`

---

### `/evaluar metodologia` — Evaluación del Diseño Metodológico

Evalúa la coherencia y rigor del diseño de investigación, con o sin un memo de estrategia formal.

**Lee (lo que exista):**
- `estrategia.ruta_memo` desde state.json
- Especificación de investigación
- Secciones de metodología del paper si existen

**Si no hay memo:** pedir al usuario que describa brevemente el diseño (3-5 oraciones).

**Dimensiones de evaluación:**

**Para todos los paradigmas:**

| Dimensión | Preguntas |
|---|---|
| **Coherencia pregunta-diseño** | ¿El tipo de pregunta (¿qué? / ¿cómo? / ¿por qué? / ¿cuánto?) justifica el método elegido? |
| **Declaración paradigmática** | ¿Está explícita la posición epistemológica? ¿Hay mezcla no declarada de paradigmas? |
| **Justificación del diseño** | ¿Por qué este diseño y no otro? ¿Se discuten alternativas descartadas? |
| **Viabilidad práctica** | ¿El diseño es ejecutable con los recursos y accesos del investigador? |

**Dimensiones adicionales para paradigma Cualitativo:**

| Dimensión | Preguntas |
|---|---|
| **Trustworthiness** | ¿Están los 4 criterios: credibilidad, transferibilidad, confirmabilidad, dependability? |
| **Saturación declarada** | ¿Se especifica qué tipo de saturación se buscará y cómo se evaluará? |
| **Muestreo** | ¿La estrategia de muestreo es coherente con el diseño cualitativo? |
| **Reflexividad** | ¿Está declarado el posicionamiento del investigador? |
| **Análisis de casos negativos** | ¿Se anticipa el mecanismo para integrar casos contrarios? |

**Dimensiones adicionales para paradigma Cuantitativo:**

| Dimensión | Preguntas |
|---|---|
| **Identificación causal** | ¿Está la fuente de variación exógena? ¿Los supuestos son plausibles? |
| **Pruebas de robustez** | ¿Se anticipan placebo tests, controles alternativos? |
| **Datos** | ¿Los datos son suficientes para la pregunta planteada? |

**Dimensiones adicionales para Mixtos:**

| Dimensión | Preguntas |
|---|---|
| **Diseño Creswell-Plano Clark** | ¿Se declaró el tipo (explicativo / exploratorio / convergente / anidado / transformativo)? |
| **Estrategia de integración** | ¿Cómo se integrarán los datos cuanti y cuali? ¿Hay joint display planificado? |
| **Coherencia interna** | ¿Los dos componentes comparten la pregunta central o son paralelos sin conexión? |

**Salida:** `informes/05_estrategia/evaluacion_metodologia_[fecha].md` con:
- Puntuación por dimensión (1-5) + severidad de problemas (Crítico / Mayor / Menor)
- Descripción específica de cada problema encontrado
- Propuestas de corrección concretas (con referencia a autores o marcos metodológicos)
- Acción recomendada: qué ajustar en `/estrategia` o en el memo

---

### `/evaluar corpus` — Evaluación del Corpus / Datos

Evalúa la calidad, representatividad y adecuación del corpus o dataset para la pregunta de investigación.

**Lee (lo que exista):**
- `data/raw/` — archivos de datos brutos
- `data/cleaned/` — corpus estructurado
- Especificación de investigación + memo de estrategia

**Si no hay corpus todavía:** evaluar el plan de corpus declarado en el memo o la especificación.

**Dimensiones de evaluación:**

| Dimensión | Preguntas | Para corpus... |
|---|---|---|
| **Representatividad** | ¿El corpus cubre adecuadamente los actores, contextos y temporalidades del fenómeno? | Cuali + Cuanti |
| **Saturación alcanzada** | ¿El volumen de datos es suficiente para el tipo de saturación declarado? | Cuali |
| **Sesgos de selección** | ¿Qué perspectivas o actores están sobrerrepresentados o ausentes? | Cuali |
| **Calidad de las fuentes** | ¿Las fuentes son auténticas, verificables, y adecuadas? (criterios archivísticos si aplica) | Cuali |
| **Estructura del corpus** | ¿Está estructurado correctamente (id_documento, hablante, segmentos, contexto)? | Cuali |
| **Validez de medición** | ¿Las variables miden lo que dicen medir? | Cuanti |
| **Valores perdidos** | ¿El tratamiento de missings es apropiado para el diseño? | Cuanti |
| **Consideraciones éticas** | ¿Hay consentimientos, anonimización, manejo de datos sensibles? | Ambos |

**Salida:** `informes/06_analisis/evaluacion_corpus_[fecha].md` con:
- Estado actual del corpus (existe / parcial / planificado)
- Problemas detectados por dimensión con severidad
- Acciones recomendadas (qué recopilar más, cómo restructurar, qué anonimizar)
- Si el corpus es insuficiente: acción → `/descubrir fuentes` o `/descubrir datos`

---

### `/evaluar codebook` — Evaluación del Libro de Códigos

Evalúa la consistencia interna, cobertura teórica y aplicabilidad del libro de códigos.

**Lee (lo que exista):**
- `master_supporting_docs/codebook.md` o equivalente
- `data/cleaned/corpus_coded.csv` (si ya hay codificación)
- Marco teórico de la especificación de investigación

**Si no hay codebook:** evaluar si la investigación lo requiere y proponer estructura inicial.

**Dimensiones de evaluación:**

| Dimensión | Preguntas |
|---|---|
| **Anclaje teórico** | ¿Cada código tiene una definición conceptual apoyada en literatura? |
| **Exhaustividad** | ¿Los códigos cubren todos los aspectos relevantes del fenómeno según la pregunta? |
| **Exclusividad mutua** | ¿Los códigos son suficientemente distintos o hay solapamiento ambiguo? |
| **Sensibilidad a lo emergente** | ¿Hay espacio para códigos inductivos / in vivo que no estaban en el libro original? |
| **Granularidad** | ¿El nivel de detalle (códigos generales / subcódigos) es adecuado para el análisis? |
| **Consistencia de aplicación** | Si hay corpus codificado: ¿los mismos segmentos reciben los mismos códigos? (ver kappa) |
| **Cobertura del corpus** | ¿Cuántos segmentos del corpus quedan sin código? ¿Hay códigos sin ninguna cita? |

**Salida:** `informes/06_analisis/evaluacion_codebook_[fecha].md` con:
- Diagnóstico código por código (si el codebook existe)
- Solapamientos detectados + propuesta de distinción
- Códigos ausentes sugeridos + justificación teórica
- Si hay `corpus_coded.csv`: estadísticas de cobertura y distribución
- Acción recomendada: ajustar codebook antes de continuar con `/analizar`

---

### `/evaluar analisis` — Evaluación del Pipeline de Análisis

Evalúa la solidez del análisis realizado: scripts, codificación, trazabilidad y anti-alucinación.

**Lee (lo que exista):**
- `scripts/python/` — scripts de análisis
- `data/cleaned/corpus_coded.csv`, `temp_cites.json`
- `informes/06_analisis/results_summary.md`
- `informes/06_analisis/memos/`

**Dimensiones de evaluación:**

| Dimensión | Preguntas |
|---|---|
| **Cumplimiento anti-alucinación** | ¿Se usaron scripts de extracción antes de codificar? ¿O se codificó por lectura directa? |
| **Trazabilidad** | ¿Cada cita en `corpus_coded.csv` tiene `id_cita` rastreable a `id_documento`? |
| **Formato de salida** | ¿`corpus_coded.csv` está en formato largo (una fila por cita-código)? |
| **Cobertura de códigos** | ¿Cuántos códigos del codebook tienen representación en el corpus codificado? |
| **Revisión manual** | ¿Cuántas citas tienen `[REVISAR_MANUAL]`? ¿Se han revisado? |
| **Coherencia con estrategia** | ¿El análisis implementa el diseño declarado en el memo de estrategia? |
| **Reproducibilidad** | ¿Los scripts tienen semillas, rutas relativas, comentarios? |
| **Memos analíticos** | ¿Se generaron memos en `informes/06_analisis/memos/`? ¿Hay baseline de reflexividad? |
| **Intercoder reliability** | Si hay segunda codificación: ¿se calculó kappa? ¿Está en rango aceptable (> 0.60)? |

**Salida:** `informes/06_analisis/evaluacion_analisis_[fecha].md` con:
- Semáforo por dimensión (🟢 / 🟡 / 🔴)
- Descripción específica de cada problema
- Verificación de INV-CS-1, INV-CS-3, INV-CS-4, INV-CS-6 (invariantes relevantes)
- Acción recomendada: qué corregir antes de pasar a `/redactar`

---

### `/evaluar proyecto` — Diagnóstico Global del Proyecto

Evalúa la coherencia y completitud de todo el proceso de investigación en su estado actual. Ideal para comenzar desde cero o para hacer un punto de control.

**Lee todo lo disponible** en el proyecto. No requiere que nada esté completo.

**Flujo:**

#### 1. Mapa de estado actual
Construir un mapa de lo que existe y lo que falta:

```markdown
## Estado Global del Proyecto — [fecha]

| Componente | Estado | Artefacto | Calidad estimada |
|---|---|---|---|
| Convocatoria (perfil) | [Cargada / Ausente / N/A] | [informes/01_convocatoria/convocatoria_profile.md o —] | |
| Propuesta / anteproyecto | [Completa / Parcial / Ausente] | [informes/04_propuesta/propuesta_final.md o —] | |
| Pregunta de investigación | [Definida / Parcial / Ausente] | [ruta o —] | [Alta/Media/Baja] |
| Marco teórico | [Definido / Parcial / Ausente] | [ruta o —] | |
| Estado del arte | [Completo / Parcial / Ausente] | [ruta o —] | |
| Diseño metodológico | [Definido / Parcial / Ausente] | [ruta o —] | |
| Corpus / datos | [Recopilado / Parcial / Planificado / Ausente] | [ruta o —] | |
| Libro de códigos | [Definido / Parcial / Ausente] | [ruta o —] | |
| Análisis | [Completo / Parcial / Ausente] | [ruta o —] | |
| Borrador del paper | [Completo / Parcial / Ausente] | [ruta o —] | |
| Protocolo ético | [Aplicado / Pendiente / N/A] | [ruta o —] | |
```

#### 2. Detección de inconsistencias transversales

- ¿La pregunta de investigación es coherente con el paradigma declarado?
- ¿El diseño metodológico es coherente con el tipo de corpus disponible?
- ¿El libro de códigos está anclado en el marco teórico?
- ¿Los resultados emergentes del análisis responden la pregunta original?
- ¿Hay cambios en el diseño que no se actualizaron en otros componentes?

#### 3. Diagnóstico de brechas críticas

Identificar qué está bloqueando el avance:

```markdown
## Brechas Críticas (ordenadas por prioridad)

1. **[Brecha]** — Impacto: [qué impide] — Acción: [skill a invocar]
2. ...

## Fortalezas actuales del proyecto

1. [Lo que está bien y debe conservarse]
2. ...
```

#### 4. Hoja de ruta personalizada

Proponer el próximo paso concreto y la secuencia recomendada:

```markdown
## Hoja de Ruta Recomendada

**Próximo paso inmediato:** [acción específica]
**Skill a activar:** [/skill modo]

**Secuencia sugerida:**
1. [paso 1] → [skill]
2. [paso 2] → [skill]
...

**Estimación de fases restantes:** [N fases] hasta tener un primer borrador completo
```

**Salida:** `informes/diagnostico_global_[fecha].md`

---

## Reglas Generales de Evaluación

1. **Nunca bloquear por prerequisitos.** Si un artefacto no existe, evaluar el plan o pedir al usuario que describa el estado.
2. **Críticos no editan.** Los reportes de evaluación solo proponen; no modifican archivos del proyecto.
3. **Severidad calibrada por fase:**
   - Proyecto en inicio → severidad constructiva (señalar el camino, no sancionar lo que falta)
   - Proyecto avanzado → severidad alta (los problemas no detectados ahora llegan al paper)
4. **Propuestas concretas.** Cada problema detectado tiene una acción específica: qué skill invocar, qué pregunta hacer, qué leer.
5. **Registrar en `state.json`:** Al final, actualizar `_meta.ultima_actualizacion` y `_meta.historial_skills_ejecutadas`.
6. **"What would change my mind":** Para cada problema mayor, especificar qué evidencia o acción resolvería la preocupación. No solo señalar — orientar.

---

## Tabla de Enrutamiento por Problema Detectado

| Problema detectado en `/evaluar` | Acción recomendada |
|---|---|
| No hay perfil de convocatoria | `/convocatoria [documento]` (o default Minciencias) |
| Propuesta ausente o incompleta | `/propuesta redactar` |
| Propuesta no competitiva vs criterios | `/propuesta evaluar` → luego `/propuesta adaptar` |
| Vacíos en literatura | `/descubrir lit [tema específico]` |
| Falta perspectiva latinoamericana | `/descubrir lit [tema]` con foco en revistas CS colombianas |
| Fuentes primarias insuficientes | `/descubrir fuentes [tema]` |
| Diseño metodológico incoherente | `/estrategia` (re-ejecutar o ajustar el memo) |
| Corpus insuficiente o mal estructurado | `/descubrir datos` o `/descubrir fuentes` + Curador-Corpus |
| Codebook con solapamientos | Revisar manualmente + re-ejecutar `/analizar` |
| Análisis sin trazabilidad | Re-ejecutar `/analizar` con los templates correctos |
| Paper con afirmaciones sin ancla | `/redactar` con Outline obligatorio |
| Paper listo para evaluación por pares | `/revisar --peer [journal_key]` |
| Protocolo ético ausente | `/descubrir etica [tipo]` |
