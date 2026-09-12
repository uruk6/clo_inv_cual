---
name: estrategia
description: Diseña la estrategia de investigación o el plan de pre-análisis (PAP) con bifurcación paradigmática (Cuantitativo/Cualitativo/Mixto). Despacha al agente estratega y a su par estratega-critic. Reemplaza a /strategize. ACTIVAR cuando el usuario diga "diseña la estrategia metodológica", "cómo abordo este estudio", "qué diseño de investigación uso", "haz el PAP", "plan de pre-análisis", "qué método aplico".
argument-hint: "[modo: estrategia | pap | pap interactivo] [pregunta de investigación o ruta de especificación]"
allowed-tools: Read,Grep,Glob,Write,Task
---

# Estrategia

## Gestión de Estado (Ejecutar al Inicio y al Final)

**Al inicio:** Leer `state.json` en la raíz del proyecto.
- Verificar prerequisito: `descubrimiento.estado == "completado"`. Si no se cumple, abortar: "⚠ `/estrategia` requiere que `/descubrir` haya completado la fase de descubrimiento (`descubrimiento.estado = completado` en `state.json`)."
- Cargar `descubrimiento.pregunta_investigacion`, `descubrimiento.ruta_spec` y `descubrimiento.ruta_lit_review`.

**Al final:** Actualizar en `state.json`:
- `estrategia.ruta_memo` → ruta del memo generado
- `estrategia.posicion_epistemologica` → posición detectada
- `estrategia.criterios_calidad` → lista de criterios aplicables
- `estrategia.tipo_saturacion` → tipo declarado (si cuali/mixto)
- `estrategia.estrategia_muestreo` → estrategia seleccionada
- `estrategia.score_critic` → puntuación del `estratega-critic` (escala 1-10)
- `estrategia.estado` → `"completado"`
- `estrategia.timestamp_completado` → fecha/hora actual
- `proyecto.paradigma` → paradigma detectado
- `_meta.ultima_actualizacion` y `_meta.historial_skills_ejecutadas`

Si `state.json` no existe, crearlo usando la plantilla en `clo_inv_cual/state.json`.

---

Diseña la estrategia de investigación despachando al agente **`estratega`** y a su par **`estratega-critic`**.

**Entrada:** `$ARGUMENTS` — palabra clave del modo seguida de la pregunta de investigación o ruta al archivo de especificación.

---

## Modos

### `/estrategia [pregunta]` — Diseño de la Estrategia de Investigación

**Agentes:** `estratega` → `estratega-critic`
**Salida:** Memo de estrategia + Decision Record.

---

### Paso 0: Detección Paradigmática (OBLIGATORIO — ejecutar primero)

Leer la especificación de investigación y clasificar en UNO de los siguientes paradigmas:

- **Cuantitativo:** Hipótesis testeable, variables medibles, inferencia estadística.
- **Cualitativo:** Comprensión de significados, experiencias subjetivas, fenómenos sociales.
- **Mixto:** Triangulación de datos numéricos y textuales en un mismo diseño.

Si el paradigma es **Cualitativo**, clasificar además en uno de los 7 diseños:
1. Fenomenológico (Husserl, Moustakas) — experiencia vivida.
2. Teoría fundamentada (Glaser-Strauss, Charmaz) — teoría emergente.
3. Etnográfico (clásico o crítico) — inmersión en comunidad.
4. Estudio de caso (Stake, Yin) — caso único o múltiple.
5. Narrativo (Clandinin, Riessman) — historias de vida.
6. Autoetnográfico (Ellis, Bochner) — yo como sujeto.
7. IAP / Investigación-Acción (Fals Borda, Freire) — transformación participativa.

El paradigma y diseño detectados determinan qué ruta del flujo se sigue. Declararlo explícitamente en el Reporte Pre-Estrategia.

---

### Paso 1: Reporte Pre-Estrategia (Obligatorio)

Antes de proponer cualquier estrategia, el Estratega debe emitir:

```markdown
## Reporte Pre-Estrategia
**Especificación de investigación:** [ruta o "no encontrada"]
**Revisión de literatura:** [ruta o "no encontrada"]
**Evaluación de datos/corpus:** [ruta o "no encontrada"]
**Perfil de dominio:** [cargado / no encontrado]

**Pregunta de investigación:** [una oración]
**Hallazgos clave de la literatura:**
- [Métodos usados anteriormente para esta pregunta]

**Posición Epistemológica:** [Post-positivista / Constructivista / Crítica / Pragmática / Decolonial-IAP]
**Paradigma Detectado:** [Cuantitativo / Cualitativo / Mixto]
**Diseño Cualitativo (si aplica):** [uno de los 7 listados en Paso 0]
**Ruta a seguir:** [Modo A: Causal | Modo B: Cualitativo | Modo C: Mixto]

Procediendo al diseño de la estrategia.
```

Si se elige posición **Decolonial-IAP**, añadir sección obligatoria "Participación de la comunidad en el diseño" con referentes: Fals Borda, Freire, Quijano, Mignolo, Sousa Santos.

---

### Paso 2a: Modo A — Estrategia Cuantitativa/Causal

Aplicar cuando el paradigma es Cuantitativo.

- Identificación causal: DiD, IV, RDD, SC o equivalente.
- Supuestos de identificación explícitos (tendencias paralelas, exclusión, continuidad).
- Pruebas de falsación y robustez (placebo, sensibilidad).
- PAP compatible con AEA/OSF/EGAP.
- Anticipar las 5 principales objeciones de revisor y cómo la estrategia las mitiga.

---

### Paso 2b: Modo B — Diseño Cualitativo

Aplicar cuando el paradigma es Cualitativo.

**Marco de Credibilidad Cualitativa (reemplaza "identificación causal"):**
- **Credibilidad:** ¿Los hallazgos representan fielmente las perspectivas de los participantes?
- **Transferibilidad:** ¿En qué contextos similares podrían aplicarse estos hallazgos?
- **Confirmabilidad:** ¿Puede un investigador externo rastrear el proceso analítico?
- **Dependability (Fiabilidad):** ¿Puede el proceso de investigación ser auditado y replicado en su lógica? Requiere registro explícito en `informes/05_estrategia/audit_trail.md`. *(Lincoln & Guba, 1985)*
- **Reflexividad:** ¿Cómo influye la posición del investigador en la interpretación?

**Tipología de saturación (declarar cuál aplica):**
- **Saturación de datos (Glaser-Strauss):** No emergen nuevos datos en las últimas 2-3 unidades.
- **Saturación de código:** Todos los códigos esperados aparecen y no surgen nuevos.
- **Saturación de significado (Hennink et al. 2017):** Los significados teóricos de los códigos están plenamente desarrollados.

**Estrategia de muestreo (obligatoria — declarar una):**
Intencional / Por conveniencia / Teórico / Bola de nieve / Máxima variación / Caso extremo / Caso típico / Caso crítico / Caso negativo.
Declarar n estimado inicial y criterio para detener.

**Análisis de casos negativos:**
Buscar activamente instancias que contradigan los patrones emergentes. Documentar en `informes/05_estrategia/negative_cases.md` cómo se integraron o transformaron la interpretación.

**Sección de Posicionamiento del Investigador (obligatoria):**
Trayectoria, relación con el campo, sesgos asumidos y reflexividad declarada.

---

### Paso 2c: Modo C — PAP Mixto

Aplicar cuando el paradigma es Mixto.

**Declarar el diseño según Creswell & Plano Clark (2018):**
- **Explicativo secuencial (QUAN → qual):** Cuanti primero, cuali explica hallazgos.
- **Exploratorio secuencial (QUAL → quan):** Cuali primero, cuanti generaliza.
- **Convergente paralelo (QUAN + QUAL):** Ambos en paralelo, integración al final.
- **Anidado (embedded):** Un método dentro del otro.
- **Transformativo:** Integración al servicio de un marco crítico/emancipatorio.
- **Multifase:** Proyectos en fases con múltiples diseños.

**Sección de Estrategia de Triangulación:**
- Cómo los datos cuantitativos y cualitativos se integrarán o contrastarán.
- Joint display: diagrama de flujo con puntos de interface.
- Secuenciación: cuándo se recogen y analizan cada tipo de datos.

Combina la sección de identificación cuantitativa (Modo A) con los criterios de credibilidad (Modo B).

---

### Paso 3: Par `estratega` → `estratega-critic`

El **`estratega-critic`** valida:
1. Coherencia entre pregunta de investigación y paradigma declarado.
2. Rigurosidad del marco de credibilidad o identificación causal.
3. Consistencia epistemológica (no mezcla de paradigmas sin declaración).
4. Calidad de los criterios de saturación y muestreo (si cuali/mixto).
5. Puntaje 1-10 con comentarios específicos por dimensión.

---

### Paso 4: Decision Record

Registrar las principales decisiones metodológicas en `informes/05_estrategia/decision_record_[fecha].md`:
- Paradigma elegido y justificación.
- Diseño cualitativo específico (si aplica).
- Criterios de credibilidad adoptados.
- Tipo de saturación declarado.

---

### `/estrategia pap [especificación]` — Plan de Pre-Análisis (PAP)

Redacta un plan de pre-análisis completo.

**Entrada:** `$ARGUMENTS` — ruta al archivo de especificación, un tema, o `interactivo`.

Si el modo es `interactivo`, realizar entrevista de 7 preguntas:

**Entrevista PAP Cualitativo/Mixto:**
1. ¿Cuál es el fenómeno o experiencia social que quieres comprender?
2. ¿Desde qué posición epistemológica abordas el estudio? (constructivista, crítica, decolonial, etc.)
3. ¿Cuál es tu campo o comunidad de estudio y cómo seleccionaste los casos?
4. ¿Qué marco teórico guía la interpretación de los datos?
5. ¿Cuáles son los criterios de selección de informantes o documentos? ¿Cómo sabrás que alcanzaste saturación?
6. ¿Cuál es tu posición como investigador/a respecto al fenómeno estudiado? (reflexividad)
7. ¿Tu investigación busca *interpretar* el fenómeno, *explicarlo* en su contexto, o *transformarlo* junto con los participantes? Si busca transformar, ¿cómo participan los sujetos en el diseño mismo del estudio?

**Entrevista PAP Cuantitativo** (conservar lógica original): preguntas sobre hipótesis, datos disponibles, variación para identificación, estrategia causal, pruebas de robustez.

---

## Principios
- **Estrategia antes del Código:** El memo de estrategia es el contrato que el Analista-IA debe seguir.
- **Consistencia Epistemológica:** No aplicar lógica causal a preguntas hermenéuticas ni viceversa.
- **Trazabilidad:** Toda decisión metodológica queda en el Decision Record.
- **Reflexividad:** En paradigmas cualitativos, el posicionamiento del investigador es parte del rigor, no un confesional opcional.
