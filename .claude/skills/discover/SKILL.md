---
name: descubrir
description: Fase de descubrimiento que combina entrevistas, búsqueda de literatura, hallazgo de datos, fuentes primarias y checklist ético. Reemplaza a /discover. ACTIVAR cuando el usuario diga "tengo una idea sobre X", "quiero investigar X", "busca literatura de X", "qué se ha escrito sobre X", "busca datos de X", "busca archivos históricos de X", "necesito fuentes primarias", "protocolo ético para X".
argument-hint: "[modo: entrevista | lit | datos | fuentes | etica | idear] [tema o consulta]"
allowed-tools: Read,Grep,Glob,Write,Edit,WebSearch,WebFetch,Task
---

# Descubrir

## Gestión de Estado (Ejecutar al Inicio y al Final)

**Al inicio:** Leer `state.json` en la raíz del proyecto (o crearlo si no existe usando la plantilla en `clo_inv_cual/state.json`).
- Prerequisito mínimo: `proyecto.nombre` definido. Si está vacío, sugerir al usuario que lo complete.

**Al final de cada modo:** Actualizar en `state.json`:
- `/descubrir entrevista` → `descubrimiento.pregunta_investigacion`, `descubrimiento.ruta_spec` (`informes/02_entrevista/especificacion_investigacion.md`), `proyecto.tipo_articulo`
- `/descubrir lit` → `descubrimiento.ruta_lit_review` (`informes/03_estado_del_arte/lit_review_[tema].md`), `descubrimiento.referencias_nuevas_candidatas`
- `/descubrir datos` → `descubrimiento.ruta_data_exploration` (`informes/03_estado_del_arte/data_exploration_[tema].md`)
- `/descubrir fuentes` → `descubrimiento.ruta_sources_exploration` (`informes/03_estado_del_arte/sources_exploration_[tema].md`)
- Al completar entrevista + lit: `descubrimiento.estado = "completado"`, `descubrimiento.timestamp_completado`
- `_meta.ultima_actualizacion` y `_meta.historial_skills_ejecutadas`

Todos los informes que produce `/descubrir` (en cualquier modo) van dentro de `informes/`, nunca en una carpeta nueva ni suelta en la raíz.

---

Inicia la fase de Descubrimiento de la investigación. Dirige a los agentes apropiados según el modo especificado.

**Entrada:** `$ARGUMENTS` — un modo seguido de un tema o consulta.

---

## Modos

### `/descubrir entrevista [tema]` — Entrevista de Investigación

Realiza una entrevista conversacional estructurada para formalizar una idea de investigación.

**Agentes:** Conversación directa.
**Salida:** Especificación de investigación + Perfil de dominio.

**Detección de paradigma al inicio de la entrevista:** Clasificar en Cuantitativo / Cualitativo / Mixto antes de elegir las preguntas.

#### Entrevista Cualitativa (usar cuando el paradigma es cualitativo o mixto):

1. **Fenómeno:** ¿Qué experiencia, proceso o fenómeno social quieres comprender en profundidad?
2. **Motivación:** ¿Por qué este fenómeno en este contexto específico? ¿Qué lo hace relevante ahora?
3. **Marco teórico:** ¿Qué teorías o autores iluminan tu comprensión inicial del fenómeno?
4. **Campo:** ¿Con quiénes o con qué documentos trabajarás? ¿Cómo accederás a ellos?
5. **Posición:** ¿Cuál es tu relación con el fenómeno o la comunidad estudiada?
6. **Contribución:** ¿Qué perspectiva o comprensión nueva esperas aportar a la literatura?

#### Entrevista Cuantitativa (usar cuando el paradigma es cuantitativo):

1. ¿Cuál es la hipótesis o pregunta causal que quieres responder?
2. ¿Qué fuente de variación exógena o diseño cuasi-experimental podrías explotar?
3. ¿Qué datos están disponibles y cuál es su cobertura temporal/geográfica?
4. ¿Cuál es la variable de resultado y cómo se mide?
5. ¿Cuáles son las principales amenazas a la identificación causal?
6. ¿Qué experimentos naturales o cambios de política podrían funcionar como instrumentos?

---

### `/descubrir lit [tema]` — Revisión de Literatura

Busca y sintetiza literatura académica.

**Agentes:** `bibliotecario` → `bibliotecario-critic`.
**Salida:** Bibliografía anotada (tabla una-fila-por-referencia, ver formato obligatorio abajo) + entradas BibTeX + mapa de la frontera del conocimiento.

**Bases de datos y motores de búsqueda — usar varias, nunca limitarse a Google Académico:**

| Base/motor | Cobertura | Acceso |
|---|---|---|
| Google Scholar | General, multidisciplinar | Abierto |
| OpenAlex (openalex.org / API) | General, metadatos abiertos masivos | Abierto |
| CORE (core.ac.uk) | Agregador de repositorios de acceso abierto | Abierto |
| BASE (base-search.net) | Motor académico (Bielefeld) | Abierto |
| DOAJ (doaj.org) | Revistas 100% acceso abierto | Abierto |
| Semantic Scholar | General, con grafo de citación | Abierto |
| SciELO | Iberoamérica, texto completo | Abierto |
| Redalyc | Iberoamérica, texto completo | Abierto |
| Dialnet | España/Iberoamérica | Abierto (registro) |
| CLACSO (biblioteca virtual) | Ciencias sociales latinoamericanas | Abierto |
| LA Referencia | Repositorios institucionales latinoamericanos | Abierto |
| Latindex | Directorio/catálogo de revistas latinoamericanas | Abierto |

**Regla:** cada ronda de búsqueda debe declarar en qué bases se buscó (mínimo 3, combinando al menos una generalista y una regional/CS). Nunca reportar una ronda que solo use Google Académico.

**Revistas de búsqueda (ampliar siempre al dominio CS):**

**Economía y métodos cuantitativos** (conservar del original):
- American Economic Review, JPE, QJE, Econometrica, RES, JDE, JPAM, AEJ, etc.

**Sociología:**
- American Sociological Review, Sociological Methods & Research, Revista Española de Investigaciones Sociológicas (REIS)

**Ciencia Política:**
- American Political Science Review, Latin American Research Review, Política y Gobierno

**Antropología:**
- American Ethnologist, Journal of Latin American Studies

**Métodos cualitativos:**
- Qualitative Inquiry, Qualitative Research, International Journal of Qualitative Methods

**Colombia (prioritarias):**
- Revista de Estudios Sociales (Uniandes)
- Revista Colombiana de Sociología (UNAL)
- Análisis Político (IEPRI, UNAL)
- Universitas Humanística (Javeriana)
- Nómadas (IESCO-U. Central)
- Tabula Rasa (U. Colegio Mayor de Cundinamarca)
- Revista CS (Icesi)
- Revista Colombiana de Antropología (ICANH)
- Co-herencia (EAFIT)

**Cono Sur / Latinoamérica:**
- Desacatos (CIESAS, México), Íconos (FLACSO Ecuador), Nueva Sociedad (FES)
- Revista Mexicana de Sociología (IIS-UNAM), Estudios Sociológicos (COLMEX)
- Apuntes (U. del Pacífico, Perú), Revista Nuestramérica
- Revista Latinoamericana de Ciencias Sociales (FLACSO), Perfiles Latinoamericanos, América Latina Hoy

**Repositorios adicionales:**
- CLACSO (clacso.org) — repositorio de ciencias sociales latinoamericanas
- DIALNET — revistas académicas en español
- REDALYC — acceso abierto a revistas latinoamericanas

**Cadenas de citación:** Seguir referencias hacia atrás (lo que citan) y hacia adelante (quién los cita).

**Formato obligatorio de la bibliografía anotada — una fila por referencia individual:**

Nunca agrupar varias referencias bajo un mismo elemento de búsqueda o un tema general ("varios artículos sobre X en revistas de sociología" no es una entrada válida). Cada paper/libro/capítulo encontrado es su propia fila, con la revista o fuente exacta nombrada, para que el usuario pueda rastrear uno por uno qué buscar:

```markdown
| Clave BibTeX | Autor(es) | Año | Revista/Fuente exacta | Título | Base donde se encontró | Proximidad (1-5) | Estado | Enlace/DOI |
|---|---|---|---|---|---|---|---|---|
| GarciaCanclini1990 | García Canclini, N. | 1990 | Grijalbo (libro) | Culturas híbridas | CLACSO | 5 | [YA_EN_BIB] | [url/doi] |
| Perez2021 | Pérez, A.; Gómez, L. | 2021 | Revista de Estudios Sociales | El territorio como categoría... | Redalyc | 4 | [NUEVA_CANDIDATA] | [url/doi] |
```

**Puntuación de proximidad (1-5):** Asignar a cada paper de forma individual, en su propia fila.

**Verificación cruzada con `Bibliography_base.bib`:**
1. Leer `master_supporting_docs/Bibliography_base.bib` (solo claves BibTeX, no resúmenes).
2. Para cada referencia encontrada, marcar: `[YA_EN_BIB]` si la clave existe, `[NUEVA_CANDIDATA]` si es propuesta nueva.
3. No insertar claves nuevas automáticamente. Presentar al usuario lista de `[NUEVA_CANDIDATA]` para que decida cuáles importar vía Zotero.

**Texto completo para las referencias centrales (profundidad, no solo metadato):**
Para las referencias con proximidad 4-5 (las que probablemente se citen con argumento, no solo de pasada), aplicar `.claude/references/fuentes-pdf-workflow.md` y dejar su texto completo en `master_supporting_docs/fuentes_md/[citekey].md` (o `[citekey]_PROVISIONAL.md` si aún no está en el `.bib`). Esto es lo que permite que `/propuesta` y `/redactar` citen el argumento real de la fuente en vez de quedarse en el resumen de este reporte.

> 🙋 **ACCIÓN DEL USUARIO — Confirmar fuentes y vincular Zotero**
> Qué necesito: que revises la lista de `[NUEVA_CANDIDATA]` y **confirmes cuáles importas** a tu colección de Zotero; luego re-exporta el `.bib` a `master_supporting_docs/Bibliography_base.bib` y avísame.
> Por qué: la curaduría de fuentes es tuya; yo no importo referencias por ti, y sin el `.bib` actualizado no puedo verificar las citas.
> Cómo: ver `.claude/references/zotero-workflow.md` (pasos 2-3).
> Mientras tanto: guardo las candidatas en `descubrimiento.referencias_nuevas_candidatas` y sigo con el mapa de literatura.

Al terminar, si el usuario confirma que vinculó el `.bib`, actualizar `state.json.bibliografia` (`vinculado_zotero`, `total_entradas`, `ultima_sincronizacion`).

**Indicador de Saturación de Literatura:**
Tras cada ronda de búsqueda, el Bibliotecario reporta:
- Nuevos conceptos únicos encontrados en esta ronda: [N]
- Porcentaje de referencias que ya estaban en rondas anteriores: [%]
- **Señal de saturación:** Si más del 70% de los papers encontrados ya estaban en la base, la revisión ha alcanzado cobertura suficiente.

**Balance temporal:** Reportar distribución por década:
- <1980: N referencias (clásicos fundacionales)
- 1980-1999: N
- 2000-2014: N
- 2015-2024: N (estado del arte)
Alertar si >70% está en una sola década (sesgo presentista o anticuario).

---

### `/descubrir datos [requisitos]` — Descubrimiento de Datos

Encuentra y evalúa datasets para la pregunta de investigación.

**Agentes:** `explorador` → `explorador-critic`.
**Salida:** Fuentes de datos clasificadas con grados de factibilidad (A-D) y evaluación de validez de medición.

**Grados de factibilidad:** A (disponible y descargable), B (acceso con solicitud), C (acceso restringido/costoso), D (inaccesible en la práctica).

---

### `/descubrir fuentes [tema]` — Búsqueda de Fuentes Primarias

Identifica y evalúa archivos históricos, documentos institucionales, colecciones de entrevistas y otras fuentes primarias.

**Agentes:** `explorador` → `explorador-critic`.
**Salida:** Inventario de fuentes primarias con evaluación de acceso y calidad archivística.

**Tipos de material:**
- Textuales (documentos, prensa, archivos institucionales)
- Audiovisuales (grabaciones, fotografías, cine documental)
- Historia oral (colecciones universitarias, centros de memoria)
- Digitales (redes sociales, foros, blogs, e-mails, Twitter/X académico)
- Corporales/performativos (observación participante, registros etnográficos)

**Flujo:**
1. Leer la especificación de investigación para entender período, geografía y tipo de fenómeno.
2. Buscar en categorías:
   - Archivos nacionales y regionales (ej. Archivo General de la Nación)
   - Archivos institucionales (ministerios, organizaciones, sindicatos)
   - Colecciones de historia oral (universidades, centros de memoria)
   - Hemerotecas digitales (prensa histórica)
   - Repositorios de datos cualitativos (QUALIDATA, UK Data Archive, ICPSR qualitative)
3. Para cada fuente, reportar:
   - Nombre y organismo custodio
   - Tipo de material
   - Cobertura temporal y geográfica
   - Acceso (público / restringido / consulta presencial)
   - **Evaluación archivística (5 criterios):**
     1. **Autenticidad:** ¿Hay certeza del origen y autoría?
     2. **Representatividad:** ¿El archivo refleja o silencia ciertos actores?
     3. **Completitud del corpus:** ¿Están disponibles los materiales clave o hay vacíos?
     4. **Sesgo de selección:** ¿Qué criterios determinaron qué se archivó?
     5. **Acceso ético/legal:** ¿Requiere permisos, anonimización o acuerdos de confidencialidad?
4. Generar tabla de fuentes con grado de factibilidad (A-D).
5. Guardar en `informes/03_estado_del_arte/sources_exploration_[tema].md`.

---

### `/descubrir etica [tipo_estudio]` — Checklist Ético

Genera protocolo ético según el tipo de estudio y población.

**Agentes:** Conversación directa (sin agente externo).
**Salida:** `informes/06_analisis/ethics_checklist.md` + actualización de `state.json.etica.*`.

**Flujo:**
1. Clasificar el tipo de estudio: entrevistas / archivos sensibles / historia oral / etnografía / observación / ACD / IAP / menores / víctimas / pueblos indígenas.
2. Producir `informes/06_analisis/ethics_checklist.md` con:
   - **Consentimiento informado:** plantilla adaptada al tipo.
   - **Protocolo de anonimización:** pseudónimos, redacted, k-anonimato.
   - **Permisos de archivo** (si aplica).
   - **Comité de ética requerido:** IRB / Comité institucional.
   - **Protocolo de manejo de trauma** (si aplica a víctimas).
   - **Sensibilidad cultural:** consulta previa, libre e informada (si aplica a pueblos indígenas).
   - **Devolución de resultados a la comunidad.**
3. Actualizar `state.json.etica.*`.

---

### `/descubrir idear [tema]` — Ideación de Investigación

Genera preguntas de investigación estructuradas e hipótesis a partir de un tema o dataset.

**Salida:** Ideas de investigación con estrategias empíricas potenciales.

---

## Principios
- **Honestidad Bibliográfica:** Nunca inventar citas. Marcar las no verificadas con `% NO VERIFICADA`.
- **Cadenas de Citación:** Seguir las referencias hacia atrás y hacia adelante.
- **Evaluación de Datos:** Un dataset perfecto pero inaccesible no es útil. Priorizar la factibilidad real.
- **Rigor Archivístico:** Las fuentes primarias requieren evaluación de autenticidad y sesgo de selección, no solo de acceso.
- **Ética desde el Diseño:** El checklist ético no es un trámite final sino parte del diseño metodológico.
