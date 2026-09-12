# CLAUDE.MD -- Investigación en Ciencias Sociales y Métodos Mixtos

**Proyecto:** [NOMBRE DEL PROYECTO]
**Institución:** [TU INSTITUCIÓN]
**Campo:** Ciencias Sociales (Sociología, Antropología, Ciencia Política, etc.)
**Enfoque:** Métodos Mixtos / Cualitativo Computacional
**Rama:** main

---

## Inicio de Sesión (Ejecutar Siempre)

Al comenzar cualquier sesión en este proyecto:
1. Leer `state.json` para conocer el estado actual del pipeline.
2. Leer `MEMORY.md` para recuperar hallazgos y decisiones previas.
3. **Onboarding:** si no existe `PROYECTO.md` o `proyecto.nombre` está vacío, o el usuario parece perdido ("qué es esto", "por dónde empiezo", "cómo funciona"), activar `/iniciar` para dar la bienvenida y poner en marcha el proyecto.
4. Si ya está inicializado, anunciar brevemente el estado desde `PROYECTO.md`: qué fase está activa, qué sigue y qué acción del usuario está pendiente (🙋).

---

## Enrutamiento Automático de Solicitudes

> **REGLA PRINCIPAL:** Cuando el usuario hace una solicitud en lenguaje natural, identificar la intención y activar la skill correspondiente SIN esperar a que el usuario escriba el comando `/skill`. Confirmar verbalmente qué skill se está activando.

### Tabla de Enrutamiento

| Si el usuario dice algo como... | Activar |
|---|---|
| "qué es esto", "por dónde empiezo", "cómo funciona", "primera vez", "ayúdame a arrancar" | `/iniciar` |
| "tengo instrucciones/documentos iniciales", "este es el brief del proyecto", "aquí está lo que me dio mi asesor" | `/iniciar documentos-base [archivo]` (ver Paso 3bis) |
| "me postulo a una convocatoria", "carga la convocatoria", "estos son los términos de referencia", "formato de entrega", "TDR" | `/convocatoria [fuente]` |
| "redacta la propuesta", "arma el anteproyecto", "construye el proyecto para la convocatoria" | `/propuesta redactar` |
| "evalúa mi propuesta", "cómo va mi anteproyecto", "revisa el proyecto contra los criterios" | `/propuesta evaluar` |
| "quiero empezar una investigación", "tengo una idea sobre X", "estoy pensando en estudiar X" | `/descubrir entrevista [tema]` |
| "busca literatura sobre X", "qué se ha escrito sobre X", "necesito referencias de X" | `/descubrir lit [tema]` |
| "busca datos sobre X", "qué datos existen para X", "dónde encuentro datos de X" | `/descubrir datos [tema]` |
| "busca archivos históricos de X", "necesito fuentes primarias de X" | `/descubrir fuentes [tema]` |
| "revisa los aspectos éticos", "necesito el protocolo ético", "cómo manejo el consentimiento" | `/descubrir etica [tipo]` |
| "diseña la estrategia", "cómo abordo metodológicamente X", "qué diseño uso" | `/estrategia [pregunta]` |
| "haz el PAP", "necesito el plan de pre-análisis" | `/estrategia pap [spec]` |
| "analiza los datos", "corre el análisis", "procesa el corpus", "codifica las entrevistas" | `/analizar [dataset]` |
| "redacta la introducción / metodología / resultados / conclusión / abstract" | `/redactar [sección]` |
| "escribe el paper completo", "redacta todo el artículo" | `/redactar full` |
| "mejora la redacción", "limpia el texto", "elimina los patrones de IA", "humaniza el texto" | `/redactar humanizar` |
| "carga las normas de [revista]", "configura el perfil de [revista]", "quiero enviar a [revista]" | `/redactar perfil [revista]` |
| "adapta el paper a [revista]", "formatea para [revista]" | `/redactar adaptar [journal_key]` |
| "evalúa mi metodología", "cómo está mi diseño", "hay problemas con el diseño de investigación" | `/evaluar metodologia` |
| "evalúa el estado del arte", "qué le falta a la literatura", "cómo está la revisión bibliográfica" | `/evaluar lit` |
| "evalúa el corpus", "qué tan bien están los datos", "hay problemas con las entrevistas" | `/evaluar corpus` |
| "evalúa el codebook", "hay inconsistencias en la codificación", "revisa el libro de códigos" | `/evaluar codebook` |
| "evalúa el análisis", "hay problemas en el pipeline", "revisa la codificación cualitativa" | `/evaluar analisis` |
| "cómo va el proyecto", "diagnostica todo", "qué me falta", "por dónde empiezo", "qué sigue" | `/evaluar proyecto` |
| "revisa el artículo", "simula la revisión por pares", "qué dirían los árbitros", "evalúa el paper" | `/revisar [--peer journal_key]` |
| "responde los comentarios", "procesa las revisiones del árbitro", "hay que corregir el paper" | `/responder-arbitros [ruta_reportes]` |
| "prepara el envío", "empaqueta para enviar", "lista para submission" | `/enviar [journal_key]` |
| "pipeline completo", "arranca la investigación desde cero sobre X" | Orquestador → pipeline completo |

### Reglas de Enrutamiento

1. **Confirmar antes de ejecutar:** Antes de activar una skill, anunciar: "Voy a activar `/skill modo` porque detecté que quieres [intención]. ¿Confirmas?"
2. **Preguntar si hay ambigüedad:** Si la solicitud puede mapearse a dos skills, preguntar cuál es la intención.
3. **Verificar prerequisitos:** Antes de activar, verificar en `state.json` que los prerequisitos estén cumplidos. Si no, informar qué falta.
4. **No requerir comando explícito:** El usuario puede hablar en lenguaje natural — no necesita conocer los comandos.

---

## Principios Fundamentales

- **Planificar Primero** — Entrar en modo plan antes de tareas no triviales; guardar planes en `informes/plans/`.
- **Regla Anti-Alucinación** — Todo análisis cualitativo debe basarse en el flujo: **Extracción de Citas (Scripts) → Codificación Teórica**. Prohibido codificar por "intuición" de lectura directa.
- **Evidencia Textual** — La cita literal es el dato primario. No hay hallazgo sin evidencia rastreable (`ID_Cita`).
- **Pares Creador-Crítico** — Cada agente creador tiene un crítico pareado que valida el rigor. Los críticos nunca crean artefactos.
- **Memoria Auto-Gestionada** — Los hallazgos emergentes y decisiones de codificación se guardan en `MEMORY.md`.
- **Estado Persistente** — Toda fase actualiza `state.json` y el tablero `PROYECTO.md`. Leerlos siempre antes de actuar.
- **Copiloto, no piloto** — Hay acciones que solo el investigador puede hacer (confirmar fuentes, vincular Zotero, aportar corpus, aprobar outlines). Señalizarlas con un bloque **🙋 ACCIÓN DEL USUARIO** y no avanzar más allá de un handoff bloqueante. Ver `.claude/references/roles-usuario-ia.md`.

---

## Skills — Referencia Rápida

| Comando | Trigger natural | Qué hace |
|---------|----------------|----------|
| `/iniciar` | "por dónde empiezo..." | Bienvenida, contrato de roles, inicializa el proyecto y `PROYECTO.md` |
| `/convocatoria` | "carga la convocatoria..." | Perfila apartados, límites y criterios (default Minciencias) |
| `/propuesta redactar` | "arma el anteproyecto..." | Propuesta en `.md` ajustada a la convocatoria |
| `/propuesta evaluar` | "evalúa mi propuesta..." | Calificación contra los criterios ponderados |
| `/descubrir entrevista` | "tengo una idea sobre..." | Entrevista de investigación → especificación |
| `/descubrir lit` | "busca literatura sobre..." | Revisión bibliográfica + BibTeX |
| `/descubrir datos` | "busca datos de..." | Datasets con grados A-D de factibilidad |
| `/descubrir fuentes` | "busca archivos de..." | Fuentes primarias + evaluación archivística |
| `/descubrir etica` | "protocolo ético para..." | Checklist ético completo |
| `/estrategia` | "diseña la estrategia..." | Bifurcación cuanti/cuali/mixto + Modos A/B/C |
| `/estrategia pap` | "haz el PAP..." | Plan de pre-análisis |
| `/analizar` | "analiza / codifica..." | Pipeline Python, templates, anti-alucinación |
| `/redactar [sección]` | "redacta la intro / resultados..." | Outline → borrador con evidencia |
| `/redactar humanizar` | "mejora la redacción..." | Limpieza de 24 patrones de IA |
| `/redactar perfil` | "normas de [revista]..." | Carga perfil editorial |
| `/redactar adaptar` | "formatea para [revista]..." | Adapta paper al perfil activo |
| `/evaluar proyecto` | "cómo va el proyecto / qué me falta..." | Diagnóstico global + hoja de ruta |
| `/evaluar lit` | "evalúa el estado del arte..." | Cobertura, balance temporal, vacíos |
| `/evaluar metodologia` | "evalúa la metodología..." | Rigor paradigmático, trustworthiness |
| `/evaluar corpus` | "evalúa los datos / el corpus..." | Representatividad, estructura, ética |
| `/evaluar codebook` | "evalúa el codebook..." | Consistencia, cobertura, anclaje teórico |
| `/evaluar analisis` | "evalúa el análisis..." | Anti-alucinación, trazabilidad, kappa |
| `/revisar` | "revisa el artículo..." | Árbitro-Dominio + Árbitro-Métodos |
| `/responder-arbitros` | "responde los comentarios..." | R&R con carta de respuesta |
| `/enviar` | "prepara el envío..." | Gate final + paquete de submission |

---

## Pipeline de Investigación

```
/iniciar                → bienvenida, roles, documentos_base/, inicializa PROYECTO.md
       ↓
/convocatoria           → informes/01_convocatoria/convocatoria_profile.md
       ↓
/descubrir entrevista   → informes/02_entrevista/ (pregunta y paradigma)
       ↓
/descubrir lit          → informes/03_estado_del_arte/ + Bibliography_base.bib + master_supporting_docs/fuentes_md/  (🙋 confirmar fuentes + vincular Zotero)
       ↓
/propuesta              → informes/04_propuesta/propuesta.md → propuesta_final.md (entregable de fase inicial, sanitizado)
       ↓
/estrategia             → informes/05_estrategia/ (diseño metodológico, Modo A/B/C según paradigma)
       ↓
/analizar               → informes/06_analisis/ + data/cleaned/corpus_coded.csv  (🙋 aportar corpus)
       ↓
/redactar               → outline aprobado → borrador con evidencia (paper/main.md), perfiles en informes/07_redaccion/
       ↓
/revisar                → informes/08_revision/ (árbitros calibrados al perfil de revista)
       ↓
/responder-arbitros     → R&R con carta punto a punto (paper/response_letter.md)
       ↓
/enviar                 → paquete final + informes/09_envio/submission_checklist
```

> La **propuesta** es el entregable de la fase inicial (para la convocatoria); el **artículo** es el producto final. Ambos son `.md`. Todos los informes y reportes de calidad de todas las fases viven en una sola carpeta, `informes/`, organizada por momento. El tablero `PROYECTO.md` muestra siempre dónde está cada entregable.

Cada fase actualiza `state.json`. Cada fase verifica que la anterior esté completada.

### Entrada Flexible con `/evaluar`

```
/evaluar proyecto   ← entrada desde cualquier punto del pipeline
       ├── /evaluar lit          ← evalúa solo el estado del arte
       ├── /evaluar metodologia  ← evalúa solo el diseño
       ├── /evaluar corpus       ← evalúa solo los datos/entrevistas
       ├── /evaluar codebook     ← evalúa solo el libro de códigos
       └── /evaluar analisis     ← evalúa solo el pipeline de análisis
```

`/evaluar` no requiere que el pipeline esté completo. Lee lo que existe y propone mejoras concretas con la skill a activar para resolverlas.

---

## Estructura de Carpetas

```
clo_inv_cual/
├── PROYECTO.md                  # 📋 Tablero-manifiesto: estado y mapa de entregables
├── CLAUDE.md                    # Este archivo (reglas y enrutamiento)
├── state.json                   # Estado del pipeline (v1.3)
├── MEMORY.md                    # Hallazgos y decisiones persistentes
├── .claude/
│   ├── skills/                  # /iniciar, /convocatoria, /descubrir, /propuesta, /estrategia, /analizar, /redactar, /evaluar, /revisar, /responder-arbitros, /enviar
│   ├── agents/                  # bibliotecario(+critic), explorador(+critic), estratega(+critic), analista-ia, ingeniero-datos, corpus-curator, coder-critic, escritor(+critic), arbitro-dominio, arbitro-metodos, orquestador
│   └── references/              # content-invariants-cs, journal-profiles-cs, convocatoria-profiles, roles-usuario-ia, zotero-workflow, coding-standards, fuentes-pdf-workflow
├── documentos_base/              # 🌱 Insumos semilla del proyecto (brief, instrucciones, convocatoria en bruto) — SIEMPRE en .md
├── informes/                     # 📊 TODOS los informes/reportes del proceso, uno por momento — nunca dispersos
│   ├── 01_convocatoria/          #   convocatoria_profile.md
│   ├── 02_entrevista/            #   especificación de investigación
│   ├── 03_estado_del_arte/       #   lit_review_*.md, evaluacion_lit_*.md, sources/data_exploration_*.md
│   ├── 04_propuesta/             #   propuesta.md (borrador) + propuesta_final.md (sanitizada, sin referencias internas)
│   ├── 05_estrategia/            #   decision_record_*.md, negative_cases.md, audit_trail.md
│   ├── 06_analisis/              #   results_summary.md, code_coverage_report.md, ethics_checklist.md, intercoder_reliability.md, memos/
│   ├── 07_redaccion/             #   journal_profiles/, journal_adaptation_report_*.md
│   ├── 08_revision/              #   peer_review_[fecha]/
│   ├── 09_envio/                 #   submission_checklist_*.md
│   └── plans/                    #   planes de tareas no triviales (transversal)
├── paper/                        # 📄 Entregable final: main.md + sections/*.md + submission_[journal]_[fecha]/
├── data/
│   ├── raw/                      # 🧑 material bruto que aporta el usuario
│   └── cleaned/                  # corpus_coded.csv, temp_cites.json, pseudonyms_map.csv
├── scripts/python/
└── master_supporting_docs/
    ├── Bibliography_base.bib     # 🔗 vinculado desde Zotero (Better BibTeX) — solo metadatos de cita
    └── fuentes_md/                # 📚 texto completo de cada fuente, un .md por citekey (ver fuentes-pdf-workflow.md)
```

**Entregables del proyecto (todos `.md`, exportables a Word/PDF con Pandoc):** la **propuesta** (`informes/04_propuesta/propuesta_final.md`), el **artículo** (`paper/main.md`) y los **reportes de calidad** (`informes/**/*.md`). El tablero `PROYECTO.md` los lista con su ruta y estado.

**Regla de una sola carpeta de informes:** ningún artefacto de reporte/evaluación/diagnóstico se crea fuera de `informes/`. Si una skill necesita guardar un informe y no está claro en qué subcarpeta, usar la que corresponda al momento del pipeline que lo produce (ver tabla del Pipeline arriba), nunca crear una carpeta nueva a nivel raíz.

---

## Configuración de Salida

- **Formato de documentos:** Markdown (`.md`). Propuesta y artículo se escriben en Markdown y se exportan a Word/PDF con Pandoc.
- **Lenguaje Principal de Análisis:** Python (Pandas, spaCy, NLTK).
- **Lenguaje Estadístico:** R (opcional para modelos mixtos).
- **Organización de Salida:** `by-script`.
- **Referenciación:** Zotero (Better BibTeX) → `Bibliography_base.bib`; citas Pandoc `[@clave]` / `@clave`; estilo visible vía `.csl` al exportar. Ver `.claude/references/zotero-workflow.md`.

---

## Estado Actual del Proyecto

| Componente | Archivo | Estado | Descripción |
|-----------|------|--------|-------------|
| Corpus | `data/cleaned/` | [Pendiente] | Estructuración de entrevistas |
| Análisis | `scripts/python/` | [Pendiente] | Pipeline de extracción de citas |
| Paper | `paper/main.md` | [Borrador] | Estructura inicial (Markdown) |
| Pipeline | `state.json` | Inicializado | Todas las fases en `pendiente` |
