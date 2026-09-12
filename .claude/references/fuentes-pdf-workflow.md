# Flujo PDF/DOCX → Markdown — Fuentes de Texto Completo

> Cada vez que el usuario aporte un documento en PDF o DOCX (un paper, un libro, la convocatoria, instrucciones de su asesor), este documento se convierte a Markdown **íntegro** — no a un resumen — y se guarda con una cabecera de relevancia. Esto es lo que permite que `/propuesta`, `/redactar` y cualquier informe **profundicen en la fuente real** en vez de quedarse en el resumen general del estado del arte (ver principio "Profundidad de fuente obligatoria").

Aplica en dos contextos, con la misma mecánica pero destino distinto:

| Contexto | Quién lo dispara | Dónde se guarda | Nombre del archivo |
|---|---|---|---|
| **Fuente bibliográfica** (paper, libro, capítulo citable) | `bibliotecario` durante `/descubrir lit`, o cuando el usuario pasa un PDF suelto | `master_supporting_docs/fuentes_md/` | `[citekey].md` |
| **Documento base** (convocatoria, instrucciones, brief inicial — no citable) | `/iniciar` o `/convocatoria` | `documentos_base/` | `[slug-descriptivo].md` |

---

## Paso 1 — Extraer el texto completo

1. Leer el PDF/DOCX con la herramienta de lectura (soporta PDF nativamente).
2. Transcribir **el texto íntegro** a Markdown, preservando la estructura original: títulos (`#`/`##`), párrafos, citas, tablas, notas al pie relevantes.
3. **Prohibido resumir en este paso.** El objetivo es tener el argumento completo disponible para citar con profundidad después, no un abstract. Si una parte es ilegible (escaneo de baja calidad), marcarla `[ILEGIBLE: descripción]` y seguir.
4. Para DOCX o PDFs nativos (con capa de texto) largos, se puede apoyar en `pandoc archivo.docx -o archivo.md` como primer paso mecánico, pero siempre revisar y corregir el resultado — pandoc no entiende columnas, notas al pie complejas ni figuras.

## Paso 2 — Nombrar el archivo

**Fuentes bibliográficas:**
- Si la referencia ya está confirmada y vinculada en `Bibliography_base.bib`, usa exactamente esa clave Better BibTeX (`[Autor][Año]`, ej. `GarciaCanclini1990.md`) — la misma que se cita en el texto como `[@GarciaCanclini1990]` (ver `zotero-workflow.md`).
- Si la referencia todavía es `[NUEVA_CANDIDATA]` (no confirmada por el usuario ni importada a Zotero), usa la misma convención de forma provisional y dilo explícitamente: `GarciaCanclini1990_PROVISIONAL.md`. Cuando el usuario confirme e importe la referencia real, renombra el archivo a la clave definitiva y actualiza cualquier referencia cruzada.

**Documentos base:** slug descriptivo en minúsculas con guiones, sin citekey (no son citables): `convocatoria-terminos-referencia.md`, `instrucciones-asesor-2026-07.md`.

## Paso 3 — Anteponer la cabecera de relevancia (obligatoria)

Antes del contenido transcrito, siempre:

```markdown
---
citekey: GarciaCanclini1990          # omitir/adaptar si es documento_base
titulo_original: "Culturas híbridas: estrategias para entrar y salir de la modernidad"
autor_es: "García Canclini, Néstor"
año: 1990
fuente_original: "ruta al PDF/DOCX o URL de origen"
convertido: 2026-07-16
estado_bib: YA_EN_BIB | NUEVA_CANDIDATA | PROVISIONAL | N/A
---

## Relevancia para el proyecto

**Elementos clave de este documento:**
- [concepto, hallazgo o argumento central 1]
- [concepto, hallazgo o argumento central 2]

**Dónde se usará:**
- [ej. "Estado del arte — corriente sobre hibridación cultural"; "Marco teórico — concepto de campo"; "Metodología — referente para el diseño etnográfico"; "Documentos base — define los apartados obligatorios que /convocatoria debe perfilar"]

---

## Texto completo

[contenido íntegro transcrito, con la jerarquía de encabezados del original]
```

La sección "Relevancia para el proyecto" la completa quien dispara la conversión (bibliotecario, o la skill que procesa el documento base) — nunca se deja vacía ni genérica ("es relevante para el proyecto" no es una respuesta válida).

## Paso 4 — Registrar

- Fuentes bibliográficas → añadir la ruta en `state.json.bibliografia` (implícito: vive en `fuentes_md/`, no hace falta campo nuevo por archivo) y mencionarlo en el reporte de `/descubrir lit`.
- Documentos base → añadir un objeto a `state.json.documentos_base.documentos` (`{nombre, ruta, tipo, fecha_conversion}`).

---

## Reglas

- **Texto completo, no resumen.** El resumen ya existe en `lit_review_*.md`; este archivo es la fuente para profundizar cuando el resumen no basta.
- **Nunca inventar contenido** al transcribir: si una sección es ilegible o falta, marcarlo, no rellenarlo.
- **Un archivo por documento.** No concatenar varias fuentes en un solo `.md`.
- **La cabecera de relevancia no es opcional.** Sin ella, el escritor no sabe para qué sirve el documento dentro de la propuesta/artículo.
