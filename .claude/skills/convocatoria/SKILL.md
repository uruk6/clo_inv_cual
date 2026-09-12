---
name: convocatoria
description: Carga y perfila la convocatoria a la que se postula el proyecto (financiación, anteproyecto de grado o call de revista). Extrae apartados obligatorios, límites de extensión y criterios de evaluación. ACTIVAR cuando el usuario diga "me postulo a una convocatoria", "carga la convocatoria", "estos son los términos de referencia", "qué apartados pide la convocatoria", "formato de entrega", "límites del proyecto", "convocatoria de Minciencias", "términos de referencia", "TDR".
argument-hint: "[fuente: ruta a documento | URL | --texto \"...\" | minciencias | anteproyecto-grado]"
allowed-tools: Read, Write, Edit, Grep, Glob, WebFetch
---

# Convocatoria

Perfila la convocatoria o el formato de entrega al que debe ajustarse la propuesta. Es el análogo, para la fase de propuesta, del perfil de revista para el artículo.

## Gestión de Estado

**Al inicio:** Leer `state.json`.
**Al final:** Actualizar `state.json.convocatoria` (`aplica`, `nombre`, `entidad`, `ruta_perfil`, `fecha_cierre`, `estado`), `_meta.ultima_actualizacion` y `_meta.historial_skills_ejecutadas`. Actualizar también el tablero `PROYECTO.md`.

**Entrada:** `$ARGUMENTS` — la fuente de la convocatoria.

---

## Fuentes aceptadas

1. **Documento local** (PDF, DOCX, MD) con los términos de referencia → leer el archivo (usar la skill `pdf`/`docx` si hace falta extraer texto).
2. **URL** de la convocatoria → `WebFetch`.
3. **Texto plano** → `/convocatoria --texto "apartados, límites, criterios..."`.
4. **Clave precargada** → `/convocatoria minciencias` o `/convocatoria anteproyecto-grado` (ver `.claude/references/convocatoria-profiles.md`).
5. **Sin claridad** → usar por defecto el preset **`minciencias`** y avisar al usuario que se puede afinar luego con el documento oficial.

> 🙋 **ACCIÓN DEL USUARIO — Aportar la convocatoria**
> Qué necesito: el documento, la URL o el texto de los términos de referencia; o confírmame que uso el default de Minciencias.
> Por qué: la propuesta debe respetar exactamente los apartados, límites y criterios de la convocatoria.
> Cómo: pásame el archivo/enlace, o dime "usa Minciencias por defecto".

---

## Paso 1 — Extraer el perfil

Del documento (o del preset) extraer, marcando cada campo `[EXTRAIDO]`, `[ASUMIDO]` o `[VERIFICAR]`:

- **Apartados obligatorios y opcionales** (en el orden exigido).
- **Límites**: extensión total, resumen, formato de archivo.
- **Anexos requeridos** (CvLAC, GrupLAC, avales, cartas, presupuesto).
- **Criterios de evaluación con su ponderación** (deben sumar 100 o la escala que use la convocatoria) y puntaje mínimo de aprobación.
- **Componentes especiales**: presupuesto, cronograma, productos/resultados esperados, consideraciones éticas.
- **Fecha de cierre.**

Usar la plantilla YAML de `.claude/references/convocatoria-profiles.md`.

## Paso 2 — Guardar el perfil

Guardar en `informes/01_convocatoria/convocatoria_profile.md` (perfil YAML + resumen legible). Registrar la ruta en `state.json.convocatoria.ruta_perfil` y `convocatoria.aplica = true`.

Si la fuente es un documento local (PDF/DOCX) y todavía no existe su versión Markdown en `documentos_base/`, aplicar primero `.claude/references/fuentes-pdf-workflow.md` (caso "Documento base") para dejar el texto completo de la convocatoria en `documentos_base/` antes de extraer el perfil — así el perfil queda trazable a la fuente íntegra, no solo a la lectura puntual del PDF.

## Paso 3 — Presentar y confirmar

Mostrar al usuario un **resumen legible** (no el YAML crudo):

```markdown
## Convocatoria cargada: [nombre]
**Entidad:** [...] · **Cierre:** [fecha o "verificar"]
**Formato de entrega:** [extensión] · [formato archivo]

**Apartados obligatorios:** [lista numerada]
**Criterios de evaluación:**
| Criterio | Peso |
|---|---|
| ... | ..% |

**Anexos requeridos:** [lista]
**Campos a verificar contra el documento oficial:** [los marcados [ASUMIDO]/[VERIFICAR]]
```

Advertir explícitamente sobre los campos `[ASUMIDO]`/`[VERIFICAR]` y pedir confirmación o el documento oficial.

## Paso 4 — Proponer el siguiente paso

- Si aún no hay pregunta de investigación → `/descubrir entrevista [tema]`.
- Si ya hay descubrimiento/estrategia → `/propuesta redactar` para construir el documento ajustado a estos apartados.

---

## Principios
- **La convocatoria manda el formato.** Los apartados y límites del perfil son el contrato que `/propuesta` debe cumplir.
- **Transparencia de supuestos.** Nunca presentar un campo `[ASUMIDO]` como oficial; siempre pedir verificación.
- **Default seguro.** Sin claridad, Minciencias — pero avisando que es genérico.
