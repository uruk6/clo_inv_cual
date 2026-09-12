---
name: iniciar
description: Puerta de entrada y onboarding del asistente de investigación en ciencias sociales. Explica qué hace la skill, qué produce y dónde, cuál es el rol del usuario, e inicializa el proyecto. ACTIVAR cuando el usuario diga "empezar", "no sé por dónde empezar", "qué es esto", "cómo funciona", "qué hace esta skill", "quiero usar el asistente de investigación", "ayúdame a arrancar", "primera vez", "inicializa el proyecto", o cuando no exista aún `PROYECTO.md`.
argument-hint: "(sin argumentos) o [nombre del proyecto]"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Iniciar — Bienvenida y Puesta en Marcha

Esta skill orienta a quien nunca ha usado el asistente y deja el proyecto listo para trabajar. Se ejecuta una vez al principio (o cuando el usuario está perdido).

## Paso 0: Detectar si es primera vez

Leer `state.json` y buscar `PROYECTO.md` en la raíz.
- Si `proyecto.nombre` está vacío o no existe `PROYECTO.md` → es primera vez: ejecutar la bienvenida completa (Pasos 1-4).
- Si ya está inicializado → dar la bienvenida corta: mostrar el estado actual (desde `PROYECTO.md`) y proponer el siguiente paso.

---

## Paso 1: Explicar qué es esto (breve, sin jerga)

Presentar este mensaje, adaptado:

```markdown
👋 Soy tu copiloto de investigación en ciencias sociales. Te acompaño **desde la propuesta hasta el artículo publicable**, en 7 momentos:

1. 🎯 **Propuesta / Convocatoria** — formular la idea y ajustarla a la convocatoria a la que te postulas.
2. 🔎 **Descubrir** — pregunta de investigación, literatura, datos/fuentes y ética.
3. 🧭 **Estrategia** — el diseño metodológico (cuali / cuanti / mixto).
4. ⚙️ **Analizar** — procesar el corpus o los datos con trazabilidad total.
5. ✍️ **Redactar** — escribir el documento sección por sección, anclado en evidencia.
6. 🧑‍⚖️ **Revisar** — simular árbitros y responder sus comentarios.
7. 📦 **Enviar** — empaquetar para la revista o la convocatoria.

**No tienes que saber los comandos.** Escríbeme en lenguaje natural lo que quieres hacer y yo activo la fase correcta.

**Qué produzco y dónde:** todo queda en archivos `.md` legibles dentro de tu proyecto. Todos los informes y reportes, de cualquier fase, viven en **una sola carpeta: `informes/`**. El tablero **`PROYECTO.md`** te muestra siempre qué existe, dónde está y qué sigue.

**Qué necesito de ti:** hay 4 cosas que solo tú puedes hacer — confirmar las fuentes que encuentro, vincular tu biblioteca de Zotero, aportar tu material (entrevistas/datos) y aprobar lo que redacto. Te las iré pidiendo con un aviso 🙋 en el momento justo.
```

Referir a `.claude/references/roles-usuario-ia.md` para el contrato completo de roles.

---

## Paso 2: Intake mínimo (una pregunta a la vez, no abrumar)

Preguntar en orden y esperar respuesta:

1. **¿Cómo se llama tu proyecto o tema?** (aunque sea provisional)
2. **¿Desde qué institución trabajas?** (opcional)
3. **¿Te estás postulando a una convocatoria?** (financiación, anteproyecto de grado, call de revista, o ninguna)
   - Si sí y tiene el documento/texto: "Perfecto, después lo cargamos con `/convocatoria`."
   - Si sí pero no tiene claridad: "Podemos usar por defecto el formato de **Minciencias**."
4. **¿Usas Zotero para tus referencias?** (sí/no)
   - Si sí: anticipar el 🙋 de exportar el `.bib` (ver `zotero-workflow.md`), sin bloquear todavía.
5. **¿Qué material ya tienes?** (solo una idea / borrador / entrevistas o datos / bibliografía)
6. **¿Tienes documentos iniciales del proyecto?** (instrucciones de tu asesor, un brief institucional, la convocatoria en PDF/DOCX, un borrador de idea)
   - Si sí: "Los guardamos en `documentos_base/`, convertidos a Markdown, para que cualquier informe pueda consultarlos directamente." Ver Paso 3bis.

No exigir todo: con el nombre del proyecto basta para arrancar.

---

## Paso 3: Inicializar el proyecto

1. Si no existe el andamiaje, crearlo:
   `documentos_base/ informes/{01_convocatoria,02_entrevista,03_estado_del_arte,04_propuesta,05_estrategia,06_analisis/memos,07_redaccion/journal_profiles,08_revision,09_envio,plans}/ paper/sections/ paper/tables/ paper/figures/ data/raw/ data/cleaned/ scripts/python/ master_supporting_docs/fuentes_md/`
2. Si no existe, crear `state.json` desde la plantilla y rellenar `proyecto.nombre`, `proyecto.institucion`, `convocatoria.aplica`.
3. Rellenar los placeholders de `CLAUDE.md` (`[NOMBRE DEL PROYECTO]`, `[TU INSTITUCIÓN]`) con los datos del intake.
4. Si no existe `master_supporting_docs/Bibliography_base.bib`, crear el archivo semilla con cabecera.
5. Generar/actualizar `PROYECTO.md` (ver plantilla en Paso 4).
6. Actualizar `_meta.ultima_actualizacion` y `_meta.historial_skills_ejecutadas`.

---

## Paso 3bis: Documentos base (si el usuario aportó alguno en el intake)

Si en la pregunta 6 del intake el usuario mencionó instrucciones, un brief, o la convocatoria en PDF/DOCX:

1. Para cada documento aportado, aplicar el flujo de `.claude/references/fuentes-pdf-workflow.md` (caso "Documento base"): extraer el texto **completo** (no resumir), anteponer la cabecera de relevancia, y guardar en `documentos_base/[slug-descriptivo].md`.
2. Registrar cada uno en `state.json.documentos_base.documentos` (`{nombre, ruta, tipo, fecha_conversion}`).
3. Si alguno de los documentos es la convocatoria misma, avisar: "Esto también lo puedo perfilar con `/convocatoria` para extraer apartados, límites y criterios."

Si el usuario no tiene documentos iniciales todavía, no bloquear — `documentos_base/` puede poblarse en cualquier momento posterior.

---

## Paso 4: Generar el tablero `PROYECTO.md`

Crear en la raíz del proyecto (este es el "mapa" que el usuario consultará siempre):

```markdown
# 📋 [Nombre del Proyecto]

**Institución:** [institución]  ·  **Paradigma:** [o "por definir"]
**Convocatoria:** [nombre / "ninguna" / "Minciencias (default)"]
**Última actualización:** [fecha]

---

## ¿Dónde está cada cosa?

| Carpeta | Qué contiene | Formato |
|---|---|---|
| `documentos_base/` | Insumos semilla del proyecto (brief, instrucciones, convocatoria en bruto) | `.md` |
| `informes/` | **Todos** los informes del proceso, organizados por momento (01_convocatoria → 09_envio) | `.md` |
| `paper/` | El artículo (`main.md`) y sus secciones | `.md` |
| `data/raw/` | Tu material bruto (entrevistas, datos) — 🧑 lo aportas tú | varios |
| `data/cleaned/` | Corpus estructurado y codificado | `.json` / `.csv` |
| `master_supporting_docs/Bibliography_base.bib` | Tu biblioteca (desde Zotero) — solo metadatos de cita | `.bib` |
| `master_supporting_docs/fuentes_md/` | Texto completo de cada fuente citada, un archivo por `citekey` | `.md` |
| `scripts/python/` | Los scripts de análisis | `.py` |

> Los **entregables** que evidencian tu proyecto son archivos `.md`: la propuesta (`informes/04_propuesta/propuesta_final.md`), el artículo y los reportes de calidad en `informes/`. Se pueden exportar a Word/PDF con Pandoc.

## Estado de las fases

| Fase | Estado | Entregable |
|---|---|---|
| 🎯 Convocatoria | ⬜ pendiente | `informes/01_convocatoria/convocatoria_profile.md` |
| 🔎 Descubrir | ⬜ pendiente | `informes/03_estado_del_arte/lit_review_*.md` |
| 📝 Propuesta | ⬜ pendiente | `informes/04_propuesta/propuesta_final.md` |
| 🧭 Estrategia | ⬜ pendiente | `informes/05_estrategia/decision_record_*.md` |
| ⚙️ Analizar | ⬜ pendiente | `data/cleaned/corpus_coded.csv` |
| ✍️ Redactar | ⬜ pendiente | `paper/main.md` |
| 🧑‍⚖️ Revisar | ⬜ pendiente | `informes/08_revision/peer_review_*/` |
| 📦 Enviar | ⬜ pendiente | `paper/submission_*/` |

## Lo que necesito de ti ahora (🙋)
- [ ] [acción pendiente más próxima, ej. "Vincular Zotero" o "Cargar la convocatoria"]

## Próximo paso sugerido
👉 [acción concreta] — se activa diciendo: "[frase natural]"
```

Marcar cada fase con ✅ completada / 🟡 en curso / ⬜ pendiente según `state.json`.

---

## Paso 5: Proponer el primer paso real

Según el intake, recomendar y ofrecer activar:
- ¿Hay convocatoria? → `/convocatoria [documento o texto]` (o default Minciencias).
- ¿Solo una idea? → `/descubrir entrevista [tema]`.
- ¿Ya hay literatura/datos? → `/evaluar proyecto` para diagnosticar desde donde esté.

Cerrar recordando: "Cuando quieras ver el estado completo, dime *cómo va el proyecto* y actualizo `PROYECTO.md`."

---

## Principios
- **Una pregunta a la vez.** No abrumar con formularios largos.
- **Mostrar, no solo decir.** El usuario termina el onboarding con `PROYECTO.md` visible y un próximo paso claro.
- **El usuario no necesita comandos.** Traducir su lenguaje natural a la fase correcta.
- **Roles explícitos.** Señalar desde el inicio las 4 acciones que son suyas (ver `roles-usuario-ia.md`).
