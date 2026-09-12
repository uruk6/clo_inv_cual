---
name: redactar
description: Redacta secciones de artículos académicos con outline obligatorio, taxonomía de 8 tipos, adaptador de revistas y ciclo de calidad. Reemplaza a /write. ACTIVAR cuando el usuario diga "redacta", "escribe", "mejora la redacción", "limpia el texto", "humaniza el paper", "elimina los patrones de IA", "carga normas de [revista]", "adapta para [revista]".
argument-hint: "[sección o modo: intro | metodologia | resultados | conclusion | abstract | full | humanizar | perfil | adaptar] [ruta o journal_key (opcional)]"
allowed-tools: Read,Grep,Glob,Write,Edit,WebFetch,Task
---

# Redactar

## Gestión de Estado (Ejecutar al Inicio y al Final)

**Al inicio:** Leer `state.json` en la raíz del proyecto.
- Para modo redactar: verificar `analisis.estado == "completado"`. Si no, abortar: "⚠ `/redactar` requiere análisis completado (`analisis.estado = completado` en `state.json`)."
- Para modo adaptar: verificar además `redaccion.perfil_revista_activo != ""`. Si está vacío, abortar: "⚠ Primero ejecuta `/redactar perfil [fuente]` para cargar un perfil de revista."
- Cargar `analisis.cualitativo.ruta_citas_json`, `analisis.cualitativo.ruta_corpus_codificado`, `analisis.cuantitativo.ruta_results_summary`, `proyecto.paradigma`.

**Al final:** Actualizar en `state.json`:
- `redaccion.secciones_completadas` → añadir sección redactada
- `redaccion.ruta_outline_aprobado` → ruta del outline aprobado
- `redaccion.perfil_revista_activo` → journal_key cargado (si aplica)
- `redaccion.cobertura_codigos` → mapa de cobertura
- `redaccion.estado` → `"completado"` (solo cuando full o todas las secciones)
- `redaccion.timestamp_completado`
- `_meta.ultima_actualizacion` y `_meta.historial_skills_ejecutadas`

---

Redacta secciones de artículos académicos mediante el agente **`escritor`** con par crítico **`escritor-critic`**.

**Entrada:** `$ARGUMENTS` — nombre de la sección o modo, opcionalmente seguido de la ruta del archivo.

---

## Modos

### `/redactar [sección]` — Redactar Sección del Artículo

Redacta: `intro`, `metodologia`, `resultados`, `conclusion`, `abstract`, o `full`.

**Agentes:** `escritor` → `escritor-critic`
**Salida:** Archivo Markdown en `paper/sections/*.md`

---

#### Paso 1: Recolección de Contexto (Mínima y Focalizada)

Leer **únicamente** las siguientes 3 fuentes antes de generar el Outline:

1. `informes/06_analisis/results_summary.md` — hallazgos y estimaciones del Analista-IA.
2. `data/cleaned/corpus_coded.csv` o `temp_cites.json` — citas literales disponibles (solo columnas: `id_cita`, `texto`, `codigo_general`).
3. `Bibliography_base.bib` — claves de citación disponibles (solo leer las claves, no el texto completo).

Las notas adicionales, perfiles de dominio y borradores previos se consultan **solo si la sección específica los requiere**, no de forma preventiva.

**Excepción — profundidad de fuente (INV-CS-17):** si el párrafo va a atribuir un argumento sustantivo a un autor (marco teórico, discusión), no basta con la clave BibTeX. Leer `master_supporting_docs/fuentes_md/[citekey].md` para ese autor específico antes de redactar esa oración, en vez de generalizar desde el título o el resumen de `lit_review_*.md`. Esto no viola la regla de lectura mínima: es lectura dirigida a la fuente exacta que se va a citar, no lectura preventiva de todo el corpus bibliográfico.

---

#### Paso 2: Detección de Tipo de Artículo (Taxonomía de 8 tipos)

Identificar el tipo desde `state.json.proyecto.tipo_articulo`:

1. **Cuantitativo-Correlacional** — variables, estadística descriptiva/correlacional.
2. **Cuantitativo-Causal** — estrategia de identificación, experimento/cuasi-experimento.
3. **Histórico-Hermenéutico** — interpretación de fuentes, contexto histórico.
4. **Fenomenológico** — descripción rica de experiencia vivida.
5. **Etnográfico** (incluye autoetnográfico) — thick description, inmersión.
6. **Estudio de Caso** (único o múltiple) — análisis en profundidad de caso(s).
7. **IAP / Investigación-Acción** — co-producción con participantes.
8. **Métodos Mixtos** (con subtipos Creswell-Plano Clark).

---

#### Paso 3: Generación del Outline (OBLIGATORIO — requiere aprobación antes de redactar)

Antes de escribir una sola oración, generar un Outline párrafo por párrafo:

```markdown
### P[N] — [Tipo de movimiento argumentativo]
- **Función:** [¿Qué hace este párrafo? Ej: enuncia el hallazgo central, provee evidencia cuantitativa, triangula con evidencia cualitativa, interpreta teóricamente]
- **Dato/Evidencia:** [Referencia exacta: número de tabla, ID_Cita, o clave BibTeX]
- **Texto de la cita o estadística:** [Fragmento literal si es cita, o valor numérico si es estadística]
- **Conexión:** [Cómo conecta con el anterior y el siguiente]
```

**Ejemplo para Resultados (Métodos Mixtos):**

```markdown
### P1 — Estadística descriptiva
- Función: Establecer el patrón cuantitativo central del estudio
- Dato: Tabla 1, columna "participacion_2022"
- Texto: "67% de los municipios rurales reportaron descenso en participación electoral"
- Conexión: Establece el fenómeno que los testimonios explicarán en P2

### P2 — Evidencia cualitativa (cita literal)
- Función: Anclar el patrón estadístico en la experiencia vivida
- Dato: ID_Cita = "ENT02_S14"
- Texto: "[fragmento literal de la cita extraída por el Analista-IA]"
- Código: participacion_comunitaria → resistencia_institucional
- Conexión: La experiencia ilustra el mecanismo que genera el patrón de P1

### P3 — Interpretación teórica
- Función: Vincular la evidencia empírica con el marco teórico
- Dato: [@Bourdieu1984]
- Texto: "El concepto de campo y la noción de habitus permiten..."
- Conexión: Cierra el argumento de P1-P2 y abre hacia las implicaciones
```

**El Outline debe ser presentado al usuario para aprobación antes de redactar.** Si aprueba, continuar. Si solicita cambios, ajustar el Outline primero.

---

#### Paso 4: Redacción párrafo por párrafo (usando Outline aprobado)

Redactar respetando estrictamente el Outline aprobado. Para cada párrafo:
- Usar exactamente la evidencia declarada en el Outline (no sustituir sin notificar).
- Respetar la voz/registro según el tipo de artículo (ver tabla de secciones).
- Aplicar formato de citas cualitativas (ver mini-guía abajo).
- Marcar con `[TBD: Cita Pendiente]` si el Analista-IA no extrajo la cita necesaria.
- Marcar con `[VERIFY: verificar dato]` si se usa un número sin confirmación.
- Marcar con `[PLACEHOLDER: descripción]` para contenido que el usuario debe completar.

**Sección "Posicionamiento del investigador" (obligatoria en tipos 3-7):**
- Trayectoria del investigador, relación con el campo, sesgos asumidos.
- Para tipo IAP: añadir rol en la comunidad y participación en el diseño.

---

#### Paso 5: Quality Self-Check (antes de presentar el borrador)

```markdown
**Quality Self-Check — /redactar**
- [ ] El Outline aprobado fue respetado en la estructura de párrafos
- [ ] Cada afirmación cualitativa tiene respaldo en un ID_Cita existente en corpus_coded.csv (INV-CS-4)
- [ ] Las citas textuales usan formato correcto (corta: en línea / larga: blockquote `>`)
- [ ] No hay afirmaciones interpretativas sin ancla en evidencia
- [ ] Los paradigmas no fueron mezclados sin declaración (INV-CS-5)
- [ ] El estilo de citación coincide con el perfil de revista activo (INV-CS-9)
- [ ] Extensión dentro de los límites de la revista (INV-CS-10)
- [ ] Secciones obligatorias presentes (INV-CS-12)
- [ ] Sin claves BibTeX indefinidas (INV-CS-13)
- [ ] Reporte de cobertura: X de Y códigos representados (INV-CS-14)
  - Códigos no representados: [lista]
  - Ratio de citación: Z% de citas extraídas utilizadas. Si <20%, justificar.
  - Diversidad de informantes: ninguna sección descansa >50% en un solo informante
- [ ] Posicionamiento del investigador incluido (si tipos 3-7)
- [ ] Declaraciones requeridas por la revista presentes (si perfil activo)
- [ ] Marcadores TBD/VERIFY/PLACEHOLDER indicados al usuario
- [ ] Afirmaciones sobre autores ancladas en master_supporting_docs/fuentes_md/, no solo en el resumen general (INV-CS-17)
- [ ] Sin abuso de incisos —/() ni patrón "afirmación + :" repetido en 3+ párrafos consecutivos (INV-CS-18)
```

---

## Tabla de Secciones por Tipo de Artículo

| Sección | Cuantitativo | Histórico-Hermenéutico | Crítico-Social | Fenomenológico | Etnográfico | Estudio de Caso | IAP | Métodos Mixtos |
|---|---|---|---|---|---|---|---|---|
| Introducción | Hipótesis → Diseño → Contribución | Contexto histórico → Fenómeno → Interpretación | Estructura de poder → Problema → Transformación | Experiencia → Pregunta vivencial → Relevancia | Campo → Comunidad → Perspectiva emic | Caso → Problema → Marco | Problema comunitario → Co-diseño | Problema → Gap metodológico → Triangulación |
| Metodología | Identificación y datos | Epistemología, fuentes, hermenéutica | Posicionamiento crítico, sujetos, campo | Reducción, bracketing, análisis eidético | Entrada al campo, diario, reflexividad | Selección del caso, unidades de análisis | Diagnóstico participativo, ciclos | Diseño anidado/secuencial, criterios integración |
| Resultados | Tablas de regresión + robustez | Citas textuales + interpretación contextual | Citas + análisis de estructuras de poder | Descripción fenomenológica rica | Viñetas etnográficas + análisis | Cadena evidencial + proposiciones | Narrativa participativa + reflexión | Estadística + triangulación cualitativa |
| Conclusión | Implicaciones de política | Reflexividad y nuevas preguntas históricas | Agenda de transformación | Esencias y nuevas comprensiones | Contribución etnográfica | Generalización analítica | Devolución a la comunidad | Validez cruzada y hallazgos integrados |
| Abstract | Pregunta, diseño, resultado con magnitud | Fenómeno, corpus, interpretación central | Problema, posición, hallazgo crítico | Fenómeno, participantes, esencias | Campo, comunidad, hallazgo etnográfico | Caso, pregunta, proposición | Problema, proceso, transformación | Pregunta, mix metodológico, hallazgo integrado |
| Posicionamiento | N/A | Obligatoria: trayectoria, relación con fuentes | Obligatoria + rol en la comunidad | Obligatoria: bracketing explícito | Obligatoria: diario de campo | Recomendada | Obligatoria + participación co-diseño | Según sección (3ra en cuanti, 1ra en cuali) |

**Columna "Voz predominante":**

| Tipo | Voz |
|---|---|
| Cuantitativo | 3ra persona impersonal |
| Histórico-Hermenéutico | 1ra persona del plural ("analizamos") |
| Crítico-Social | 1ra persona + voz participante |
| Fenomenológico | 1ra persona + descripción rica |
| Etnográfico | 1ra persona + thick description |
| Autoetnográfico | 1ra persona narrativa |
| IAP | 1ra persona plural colectiva |
| Métodos Mixtos | Según sección (3ra en cuanti, 1ra en cuali) |

---

## Mini-Guía de Citación Cualitativa

- **Cita corta** (<40 palabras): en línea, entre comillas tipográficas, atribución al final.
  Ejemplo: "El territorio nos duele" (Doña M., lideresa comunitaria, 2024, ENT02_S14).
- **Cita larga** (≥40 palabras): en blockquote Markdown (línea que empieza con `>`), atribución al final con ID_Cita.
- **Elisiones:** `[...]` (tres puntos entre corchetes).
- **Énfasis del investigador:** `[énfasis nuestro]` al final de la cita.
- **Pseudonimización:** nombres ficticios + rol + año. Tabla real en `data/cleaned/pseudonyms_map.csv` (interno, no publicable).

---

## Convenciones Markdown y Estilo

- **Formato base:** Markdown. El manuscrito vive en `paper/main.md` y las secciones en `paper/sections/*.md`.
- **Citación estilo Pandoc:** `[@Clave2024]` para cita parentética y `@Clave2024` para cita narrativa. Toda clave debe existir en `master_supporting_docs/Bibliography_base.bib`.
- **Estilo bibliográfico:** al exportar, Pandoc + `--citeproc` aplica el CSL que corresponde al perfil de revista/convocatoria (APA 7, Chicago, etc.). Ver tabla de mapeo en `/redactar perfil`.
- **Citas cualitativas largas:** blockquote Markdown (`>`) con `ID_Cita`.
- Mantener consistencia en la nomenclatura entre el código (Naming Map) y el texto.
- **Exportación opcional:** `pandoc paper/main.md --citeproc --bibliography master_supporting_docs/Bibliography_base.bib -o paper/main.docx` (o `.pdf`). Para Word con formato fino, apoyarse en la skill `docx`.

---

### `/redactar humanizar` — Limpieza de Patrones de IA

Aplica modo de humanización al borrador en `paper/` o en `informes/04_propuesta/propuesta.md`.

**Patrones léxicos a eliminar:** "en conclusión", "es fundamental destacar", "un enfoque matizado", "es importante señalar", "cabe destacar", "en este sentido", "a modo de cierre", "resulta evidente que", y similares (24 patrones en 4 categorías).

**Patrones estructurales a corregir (INV-CS-18):**
1. **Incisos con `—` o `( )` usados para aclarar en vez de argumentar:** localizar los incisos que contienen una idea que sostiene el argumento (no una fecha/sigla/cifra breve) y reescribir la oración integrando esa idea en la sintaxis principal, en vez de dejarla entre guiones o paréntesis.
   - Antes: "La participación comunitaria —entendida aquí como forma de resistencia territorial— se expresó en..."
   - Después: "La participación comunitaria, que en este estudio se entiende como una forma de resistencia territorial, se expresó en..."
2. **"Afirmación + `:` + explicación" repetido:** recorrer el documento párrafo por párrafo; si 3 o más consecutivos abren con ese patrón, reescribir variando la construcción (conector lógico, subordinada inicial, evidencia antes que la afirmación, pregunta resuelta en la prosa).

Reportar cuántas instancias de cada patrón (léxico y estructural) se corrigieron.

---

### `/redactar perfil [fuente]` — Cargar Normas de Revista

Ingesta normas editoriales y produce perfil estructurado en `informes/07_redaccion/journal_profiles/`.

**Fuentes aceptadas:**
1. **Clave precargada** en `.claude/references/journal-profiles-cs.md`. Ej: `/redactar perfil reis`
2. **Documento local** (PDF, DOCX, MD). Ej: `/redactar perfil master_supporting_docs/journals/reis.pdf`
3. **URL pública**. Ej: `/redactar perfil https://journals.sagepub.com/author-instructions/XYZ`
4. **Texto plano** con `--text`. Ej: `/redactar perfil --text "Max 8000 words. APA 7..."`

**Flujo:**
1. Leer la fuente (WebFetch si URL; extraer texto si PDF; directo si texto plano).
2. Extraer campos del perfil YAML (ver `.claude/references/journal-profiles-cs.md`). Marcar: `[EXTRAIDO]`, `[ASUMIDO]`, o `[VERIFICAR]`.
3. Guardar en `informes/07_redaccion/journal_profiles/[journal_key].md`.
4. Actualizar `state.json.redaccion.perfil_revista_activo`.
5. Presentar perfil resumido al usuario para validación.

**Tabla de mapeo estilo ↔ CSL (Pandoc):**

| Estilo | Archivo CSL (Pandoc `--csl`) | Cita en el texto |
|---|---|---|
| APA 7 | `apa.csl` | `[@Clave]` / `@Clave` |
| Chicago Author-Date | `chicago-author-date.csl` | `[@Clave]` / `@Clave` |
| Chicago Notes-Bib | `chicago-note-bibliography.csl` | `[@Clave]` (nota al pie) |
| Harvard | `harvard-cite-them-right.csl` | `[@Clave]` / `@Clave` |
| Vancouver | `vancouver.csl` | `[@Clave]` (numérica) |
| MLA | `modern-language-association.csl` | `[@Clave]` |
| Propio | Solicitar el `.csl` de la revista al usuario | — |

> En Markdown la cita es siempre `[@Clave]`/`@Clave`; el estilo visible lo determina el CSL al exportar con `pandoc --citeproc --csl <archivo>`. No hay que cambiar el texto para cambiar de estilo.

---

### `/redactar adaptar [journal_key]` — Adaptar Borrador a Perfil de Revista

Adapta el borrador al perfil activo o al especificado.

**Flujo:**
1. Leer perfil desde `informes/07_redaccion/journal_profiles/[journal_key].md`.
2. Aplicar transformaciones: longitud de abstract, estilo de citación (CSL), secciones obligatorias, declaraciones, límite de palabras.
3. Producir `paper/main_[journal_key].md` (NO sobrescribe `main.md`).
4. Generar `informes/07_redaccion/journal_adaptation_report_[journal_key].md`.

---

## Principios
- **Outline antes de Redactar:** Nunca escribir una sola oración sin outline aprobado.
- **Lectura Mínima:** Solo 3 fuentes en el paso de contexto; no lectura preventiva.
- **Evidencia sobre Intuición:** Nunca inventar resultados. Si el Analista-IA no extrajo la cita, usar `[TBD: Cita Pendiente]`.
- **Triangulación:** En artículos mixtos, buscar convergencia o divergencia entre datos numéricos y testimonios.
- **Limpieza de Patrones de IA:** Eliminar muletillas léxicas y estructurales (incisos —/(), "afirmación + :" repetida) en el paso de humanización, y también al redactar por primera vez.
- **Profundidad sobre Resumen:** Los argumentos de autor se citan desde `master_supporting_docs/fuentes_md/`, no desde el resumen general del estado del arte (INV-CS-17).
- **Invariantes:** Verificar `content-invariants-cs.md` (INV-CS-1 a INV-CS-15) antes de presentar cualquier borrador.
- **`escritor-critic`:** Toda sección pasa por revisión adversarial antes de presentarse al usuario.
