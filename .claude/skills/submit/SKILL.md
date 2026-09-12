---
name: enviar
description: Gate de submission. Verifica cumplimiento del perfil de revista, invariantes de contenido y produce paquete de envío completo. Reemplaza a /submit. ACTIVAR cuando el usuario diga "prepara el envío a [revista]", "lista para submission", "empaqueta el paper", "quiero enviar a [revista]", "finaliza para envío".
argument-hint: "[journal_key]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash,Task
---

# Enviar

## Gestión de Estado (Ejecutar al Inicio y al Final)

**Al inicio:** Leer `state.json`.
- Verificar prerequisito: `redaccion.estado == "completado"`. Si no se cumple, abortar: "⚠ `/enviar` requiere manuscrito completo (`redaccion.estado = completado`)."
- Verificar que `redaccion.perfil_revista_activo != ""`. Si está vacío, abortar: "⚠ Primero ejecuta `/redactar perfil [journal_key]` para cargar las normas de la revista."
- Cargar el perfil completo desde `informes/07_redaccion/journal_profiles/[journal_key].md`.

**Al final:** Actualizar en `state.json`:
- `ciclo_editorial.journal_objetivo` → nombre de la revista
- `ciclo_editorial.estado_submission` → `"listo_para_envio"`
- `_meta.ultima_actualizacion` y `_meta.historial_skills_ejecutadas`

---

Ejecuta el gate final antes del envío a la revista. Verifica todas las invariantes y produce el paquete de envío.

**Entrada:** `$ARGUMENTS` — `journal_key` de la revista objetivo.

---

## Flujo

### Paso 1: Verificación de Prerequisitos

```markdown
## Checklist de Prerequisitos
- [ ] redaccion.estado == "completado" en state.json
- [ ] Perfil de revista activo y validado por el usuario
- [ ] Quality Self-Check de /redactar pasado (sin ítems bloqueantes)
- [ ] Carta de respuesta a árbitros disponible (si es resubmisión)
```

### Paso 2: Verificación de Invariantes de Contenido (INV-CS-1 a INV-CS-15)

Ejecutar el checklist completo de `content-invariants-cs.md`. Reportar:

```markdown
## Verificación de Invariantes
- [✓/✗] INV-CS-1: Trazabilidad de citas
- [✓/✗] INV-CS-2: Pseudonimización
- [✓/✗] INV-CS-3: Reflexividad/posicionamiento
- [✓/✗] INV-CS-4: Ancla empírica en afirmaciones cualitativas
- [✓/✗] INV-CS-5: Paradigmas no mezclados sin declaración
- [✓/✗] INV-CS-6: Libro de códigos previo
- [✓/✗] INV-CS-7: Declaración ética
- [✓/✗] INV-CS-8: Disponibilidad de datos
- [✓/✗] INV-CS-9: Estilo de citación conforme
- [✓/✗] INV-CS-10: Extensión dentro de límites
- [✓/✗] INV-CS-11: Palabras clave conformes
- [✓/✗] INV-CS-12: Secciones obligatorias presentes
- [✓/✗] INV-CS-13: Sin claves BibTeX indefinidas
- [✓/✗] INV-CS-14: Reporte de cobertura generado
- [✓/✗] INV-CS-15: Devolución a comunidad (si IAP)

**Invariantes fallidas:** [lista — bloquean el envío hasta resolverse]
```

Si alguna invariante falla, **no continuar**. Informar al usuario qué debe corregirse.

### Paso 3: Adaptación Final al Perfil

Si `/redactar adaptar [journal_key]` no se ejecutó, ejecutarlo ahora.
Verificar que `paper/main_[journal_key].md` existe y exporta sin errores al formato del perfil
(`pandoc paper/main_[journal_key].md --citeproc --bibliography master_supporting_docs/Bibliography_base.bib --csl <estilo>.csl -o <manuscript>.<ext>`).

### Paso 4: Compilación del Paquete de Envío

Crear directorio `paper/submission_[journal_key]_[fecha]/` con:

```
submission_[journal_key]_[fecha]/
├── manuscript_source.md               # Fuente Markdown (con citas [@clave])
├── manuscript.[docx|pdf]              # Exportado con Pandoc según formato del perfil
├── manuscript_anonymized.[ext]        # Versión sin datos de autor (si doble ciego)
├── figures/                           # Figuras en formato requerido
│   └── fig_[N].[pdf|tiff|png]
├── tables/                            # Tablas si el perfil las exige separadas
├── supplementary/                     # Material suplementario (si aplica)
├── declarations/
│   ├── conflict_of_interest.md        # Plantilla completada
│   ├── ethics_statement.md            # Si aplica
│   ├── data_availability.md           # Si aplica
│   └── credit_authors.md              # Si aplica
├── cover_letter.md                    # Carta de presentación autogenerada
└── response_letter.md                 # Carta de respuesta (si es resubmisión)
```

### Paso 5: Carta de Presentación (Cover Letter)

Generar `paper/submission_[journal_key]/cover_letter.md`:

```markdown
# Cover Letter / Carta de Presentación

**Fecha:** [fecha]
**Revista:** [nombre completo]
**Editor/a:** [si se conoce]

Estimado/a Editor/a:

Adjuntamos el manuscrito titulado "[título]" para su consideración en [nombre de la revista].

**Contribución:** [2-3 oraciones sobre la contribución específica del trabajo]

**Relevancia para la revista:** [1-2 oraciones sobre por qué encaja en la línea editorial]

**Declaraciones:**
- El manuscrito no ha sido enviado simultáneamente a otra revista.
- Todos los autores han aprobado la versión final.
- [Otras declaraciones requeridas según el perfil]

Quedamos a su disposición para cualquier consulta.

Atentamente,
[Nombre del autor/a de correspondencia]
[Institución]
[Email]
```

### Paso 6: Checklist de Envío Final

Generar `informes/09_envio/submission_checklist_[journal_key]_[fecha].md`:

```markdown
## Submission Checklist — [journal_key] — [fecha]

**Verificación de formato:**
- [ ] Manuscrito exportado en formato correcto: [docx/pdf según perfil] desde `manuscript_source.md`
- [ ] Abstract: [N] palabras (máx. [max_perfil])
- [ ] Manuscrito: [N] palabras (máx. [max_perfil])
- [ ] Palabras clave: [N] (rango: [min]-[max] según perfil)
- [ ] Secciones obligatorias: [lista verificada]

**Verificación de declaraciones:**
- [ ] Conflicto de intereses: [incluido / N/A]
- [ ] Declaración ética: [incluido / N/A]
- [ ] Disponibilidad de datos: [incluido / N/A]
- [ ] CRediT de autores: [incluido / N/A]
- [ ] Uso de IA generativa: [incluido / N/A]

**Archivos incluidos:**
- [ ] Manuscrito (con datos de autor)
- [ ] Manuscrito anonimizado (si doble ciego)
- [ ] Figuras ([N] archivos en [formato])
- [ ] Cover letter
- [ ] Response letter (si resubmisión)

**Sistema de envío:** [sistema_envio del perfil]
**URL de envío:** [url_guidelines del perfil]

**Estado:** LISTO PARA ENVÍO ✓
```

---

## Principios
- **Gate Bloqueante:** Las invariantes fallidas impiden el empaquetado hasta resolverse.
- **No Sobrescribir:** El paquete de envío va en un directorio nuevo fechado; nunca sobrescribe `paper/main.md`.
- **Versión Anonimizada:** Si la revista usa doble ciego, generar la versión sin datos de autor automáticamente.
- **Trazabilidad Final:** El checklist de envío queda en `informes/09_envio/` como registro permanente.
