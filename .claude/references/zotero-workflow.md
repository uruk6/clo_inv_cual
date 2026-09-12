# Flujo de Trabajo Zotero + Bibliografía

Cómo conectar tu gestor de referencias (Zotero) con el proyecto `clo_inv_cual`. Este es uno de los pasos que **solo el investigador puede hacer** (ver `roles-usuario-ia.md`).

---

## Por qué importa

El proyecto verifica **cada cita** contra un único archivo: `master_supporting_docs/Bibliography_base.bib`. Si una clave citada como `[@Bourdieu1980]` no está en ese archivo, la IA la marca como `⚠ CITA NO EN BIBLIOTECA`. Por eso hay que mantener el `.bib` sincronizado con tu Zotero.

**El `.bib` es solo metadato.** El texto completo de cada fuente (para citar con profundidad, no solo de nombre) vive aparte, en `master_supporting_docs/fuentes_md/[citekey].md` — ver `.claude/references/fuentes-pdf-workflow.md`. Cuando importes un PDF a Zotero, si quieres que el asistente pueda profundizar en su argumento, pásaselo también para que lo convierta y lo guarde con el mismo `citekey`.

---

## Paso 1 — Configurar Zotero (una sola vez)

1. Instala **Zotero** y el plugin **Better BibTeX** (menú *Herramientas → Complementos*).
2. En *Better BibTeX*, fija el formato de **clave de citación** como `[auth][year]` → produce claves tipo `Bourdieu1980`, `GarciaCanclini1990`. Estas son las que usarás en el texto como `[@Bourdieu1980]`.

## Paso 2 — Crear la colección del proyecto

Crea en Zotero una colección con el nombre de tu proyecto y arrastra ahí todas las referencias que vas confirmando durante `/descubrir lit`.

> 🙋 **Confirmación de fuentes:** cuando la IA te presente referencias marcadas `[NUEVA_CANDIDATA]`, tú decides cuáles importar a esta colección. Ese acto de curaduría es tuyo: una referencia que no confirmas, no entra al proyecto.

## Paso 3 — Exportar y VINCULAR el `.bib` al proyecto

1. Clic derecho sobre la colección → **Export Collection**.
2. Formato: **Better BibTeX**. Marca **"Keep updated"** para que la exportación se re-genere automáticamente cuando agregues referencias.
3. Guarda el archivo exactamente como:
   `master_supporting_docs/Bibliography_base.bib` (dentro de la carpeta del proyecto).
4. Avísale a la IA: *"ya vinculé mi Zotero"*. La IA registrará en `state.json`:
   - `bibliografia.ruta_bib` → la ruta del `.bib`
   - `bibliografia.vinculado_zotero` → `true`
   - `bibliografia.total_entradas` y `bibliografia.ultima_sincronizacion`

> 🙋 **ACCIÓN DEL USUARIO — Vincular Zotero**
> Qué necesito: el archivo `.bib` exportado en `master_supporting_docs/Bibliography_base.bib`.
> Por qué: sin él no puedo verificar ninguna cita.
> Cómo: pasos 1-3 de arriba (Better BibTeX → Export → "Keep updated").
> Mientras tanto: puedo redactar dejando las citas como `[VERIFICAR]`, pero no confirmarlas.

## Paso 4 — Citar en el texto (Markdown / Pandoc)

- **Cita parentética:** `[@Bourdieu1980]` → (Bourdieu, 1980).
- **Cita narrativa:** `@Bourdieu1980` → Bourdieu (1980).
- **Con página:** `[@Bourdieu1980, p. 45]`.
- **Varias:** `[@Bourdieu1980; @GarciaCanclini1990]`.

El estilo visible (APA 7, Chicago, etc.) lo aplica Pandoc al exportar, según el `.csl` del perfil de revista/convocatoria activo. **No cambies el texto para cambiar de estilo.**

## Paso 5 — Verificación de citas

Antes de finalizar cualquier sección, la IA (agente `escritor` + `escritor-critic`) comprueba que toda clave `[@...]` exista en `Bibliography_base.bib`. Las que no existan se marcan `⚠ CITA NO EN BIBLIOTECA: [clave]` para que las importes o corrijas.

## Exportar el documento final

```bash
pandoc paper/main.md --citeproc \
  --bibliography master_supporting_docs/Bibliography_base.bib \
  --csl apa.csl -o paper/main.docx
```

Cambia `apa.csl` por el estilo de la revista y `.docx` por `.pdf` si lo necesitas. Para Word con formato institucional fino, apóyate en la skill `docx`.

---

## Reglas

- **Sincroniza antes de redactar.** Cada vez que agregues un PDF a Zotero, deja que Better BibTeX re-exporte el `.bib` antes de pedir redacción.
- **Nunca edites el `.bib` a mano** para "arreglar" una cita: corrige en Zotero y re-exporta, así no se desincroniza.
- **Honestidad bibliográfica:** la IA nunca inventa una entrada. Si falta, te la pide.
