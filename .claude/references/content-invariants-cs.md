# Invariantes de Contenido — Ciencias Sociales (CS)

> Estas invariantes son contratos de calidad obligatorios para todos los artefactos producidos en `clo_inv_cual/`. Cada SKILL.md debe referenciarlas en su Quality Self-Check. Una mejora está incompleta si viola alguna invariante.

---

## INV-CS-1 — Trazabilidad de citas

Toda cita textual en el manuscrito tiene un `ID_Cita` rastreable a `data/cleaned/corpus_coded.csv`.  
**Verificación:** `grep "ENT" paper/sections/*.md` debe retornar solo IDs presentes en `corpus_coded.csv`.

## INV-CS-2 — Pseudonimización

Toda cita textual usa pseudónimo + rol + año (ej. "Doña M., lideresa comunitaria, 2024").  
La tabla real de correspondencias reside en `data/cleaned/pseudonyms_map.csv` (archivo interno, no publicable).  
**Verificación:** Ningún nombre real aparece en `paper/sections/*.md` sin estar en `pseudonyms_map.csv`.

## INV-CS-3 — Declaración de reflexividad/posicionamiento

Las secciones de artículos con diseño Histórico-Hermenéutico, Crítico-Social, Fenomenológico, Etnográfico, Autoetnográfico o IAP incluyen una declaración de reflexividad/posicionamiento del investigador.  
**Verificación:** `informes/06_analisis/memos/baseline_reflexivity.md` existe y la sección de Metodología contiene referencia a la posición del investigador.

## INV-CS-4 — Ancla empírica obligatoria

Ninguna afirmación cualitativa carece de ancla en evidencia (cita con ID_Cita, documento referenciado, o registro de observación).  
**Verificación:** Cada oración interpretativa en resultados va seguida de `(ID_Cita)` o `[@clave]`.

## INV-CS-5 — No mezcla de paradigmas sin declaración

Los paradigmas no se mezclan sin integración declarada. No se aplica lógica causal (hipótesis nula, p-value) a preguntas hermenéuticas, ni se usa lenguaje interpretativo en secciones diseñadas para inferencia estadística.  
**Verificación:** `proyecto.paradigma` en `state.json` coincide con el lenguaje metodológico dominante de cada sección.

## INV-CS-6 — Libro de códigos previo

Los códigos teóricos están definidos en el libro de códigos **antes** de aplicarlos en el manuscrito.  
**Verificación:** `master_supporting_docs/codebook.md` (o equivalente) existe y cada `codigo_general` en `corpus_coded.csv` tiene entrada en ese documento.

## INV-CS-7 — Declaración ética para estudios con sujetos humanos

Estudios con entrevistas, observación, historia oral, o datos sensibles incluyen una declaración ética explícita.  
**Verificación:** `informes/06_analisis/ethics_checklist.md` existe y la sección de Metodología contiene el párrafo de aprobación ética.

## INV-CS-8 — Declaración de disponibilidad de datos

La sección de declaraciones del manuscrito especifica qué datos se comparten (corpus, scripts) y cuáles se protegen (transcripciones brutas, `pseudonyms_map.csv`) con justificación (consentimiento, sensibilidad).  
**Verificación:** El manuscrito contiene sección "Disponibilidad de datos" o equivalente.

## INV-CS-9 — Consistencia de estilo de citación

El estilo de citación del manuscrito coincide con el perfil de revista activo en `state.json.redaccion.perfil_revista_activo`.  
**Verificación:** Si `perfil_revista_activo != ""`, el `.csl` declarado para la exportación Pandoc corresponde al `estilo_citacion` del perfil (ver tabla de mapeo en `/redactar perfil`). Las citas en el texto usan `[@clave]`/`@clave`.

## INV-CS-10 — Límites de extensión

La longitud del abstract y el total del manuscrito no exceden los máximos declarados en el perfil de revista/convocatoria activo.  
**Verificación:** `wc -w paper/main.md` (o el conteo de palabras del cuerpo, excluyendo referencias) ≤ `longitud_maxima_palabras` del perfil.

## INV-CS-11 — Palabras clave conformes

El número y formato de palabras clave coincide con el perfil de revista (cantidad mínima/máxima, fuente: libres o tesauro).  
**Verificación:** Contar palabras clave en `\keywords{}` y comparar con `palabras_clave_cantidad` del perfil.

## INV-CS-12 — Secciones obligatorias presentes

Las secciones obligatorias de la revista/convocatoria están presentes en el manuscrito y nombradas exactamente según lo especificado en el perfil (`titulo_estandar_metodo`, etc.).  
**Verificación:** `secciones_obligatorias` del perfil son subconjunto de los encabezados Markdown (`#`/`##`) del manuscrito.

## INV-CS-13 — Claves BibTeX válidas

Ninguna cita `[@clave]` o `@clave` referencia una clave inexistente en `master_supporting_docs/Bibliography_base.bib`.  
**Verificación:** Extraer las claves citadas en `paper/**/*.md` (patrón `@[A-Za-z0-9_]+`) y confirmar que todas existen como `@entrada{clave,` en el `.bib`. Al exportar, `pandoc --citeproc` no debe emitir `[WARNING] Citeproc: citation ... not found`.

## INV-CS-14 — Reporte de cobertura de códigos

El reporte de cobertura de códigos existe en `informes/06_analisis/` (no dentro del manuscrito). Indica cuántos de los `Y` códigos en `corpus_coded.csv` tienen al menos una cita representada en el paper.  
**Verificación:** Archivo `informes/06_analisis/code_coverage_report.md` existe y fue generado en la sesión de `/redactar`.

## INV-CS-15 — Devolución a la comunidad (IAP)

Para investigaciones de Investigación-Acción Participativa (IAP), el proyecto documenta el mecanismo de devolución de resultados a la comunidad participante.  
**Verificación:** Si `proyecto.diseno_cualitativo == "IAP"`, existe `informes/06_analisis/devolucion_comunidad.md`.

## INV-CS-16 — Documento externo, sin referencias internas al proceso

Todo documento que será leído/evaluado por alguien externo al proyecto (propuesta final, manuscrito de envío) no menciona agentes del asistente ("el Bibliotecario encontró...", "el Analista-IA calculó..."), rutas del proyecto (`state.json`, `informes/`, `data/cleaned/`), ni marcadores técnicos internos (`ID_Cita`, `[NUEVA_CANDIDATA]`, `[PENDIENTE]`, `[VERIFICAR]`). El argumento se sostiene por sí mismo, como lo escribiría el investigador.  
**Verificación:** `grep -iE "bibliotecario|analista-ia|escritor|state\.json|informes/|documentos_base/|\[PENDIENTE|\[VERIFICAR|\[ASUMIDO|ID_Cita" informes/04_propuesta/propuesta_final.md paper/main*.md` no debe retornar coincidencias.

## INV-CS-17 — Profundidad de fuente obligatoria

Ninguna afirmación sobre un autor o corriente teórica se construye solo desde el resumen general del estado del arte (`lit_review_*.md`). Cuando existe `master_supporting_docs/fuentes_md/[citekey].md`, el argumento citado debe reflejar el texto completo de esa fuente, no una generalización de su título o abstract.  
**Verificación:** Para cada `[@clave]` citado con una afirmación sustantiva (no solo referencia de paso), confirmar que existe `master_supporting_docs/fuentes_md/[clave].md` o `[clave]_PROVISIONAL.md`; si no existe, la afirmación debe estar marcada `[VERIFICAR: profundizar fuente]`.

## INV-CS-18 — Prosa sin muletillas estructurales de IA

Más allá de las muletillas léxicas (`/redactar humanizar`), la prosa no abusa de incisos entre `—` o `( )` para aclaraciones que deberían integrarse en el argumento del párrafo, ni repite el patrón "afirmación + `:` + explicación" como apertura de párrafos consecutivos.  
**Verificación:** En cualquier sección de `paper/` o `informes/04_propuesta/propuesta_final.md`, ningún tramo de 3+ párrafos consecutivos abre con el patrón "oración + dos puntos"; los incisos con `—`/`( )` que contienen información argumentativa (no una cifra o fecha breve) están reescritos como parte de la oración.

---

## Checklist de Verificación Rápida

```markdown
- [ ] INV-CS-1: Todas las citas tienen ID_Cita en corpus_coded.csv
- [ ] INV-CS-2: Pseudónimos usados; pseudonyms_map.csv es interno
- [ ] INV-CS-3: Declaración de reflexividad presente (si cuali/mixto)
- [ ] INV-CS-4: Afirmaciones cualitativas tienen ancla empírica
- [ ] INV-CS-5: Paradigmas no mezclados sin declaración
- [ ] INV-CS-6: Libro de códigos definido antes del análisis
- [ ] INV-CS-7: Declaración ética presente (si sujetos humanos)
- [ ] INV-CS-8: Declaración de disponibilidad de datos incluida
- [ ] INV-CS-9: Estilo de citación coincide con perfil de revista
- [ ] INV-CS-10: Extensión dentro de los límites de la revista
- [ ] INV-CS-11: Palabras clave conformes al perfil
- [ ] INV-CS-12: Secciones obligatorias presentes y nombradas correctamente
- [ ] INV-CS-13: Sin claves BibTeX indefinidas
- [ ] INV-CS-14: informes/06_analisis/code_coverage_report.md generado
- [ ] INV-CS-15: Devolución a comunidad documentada (si IAP)
- [ ] INV-CS-16: Sin referencias internas al proceso en documentos externos (propuesta_final.md, manuscrito)
- [ ] INV-CS-17: Citas sustantivas ancladas en master_supporting_docs/fuentes_md/, no solo en el resumen general
- [ ] INV-CS-18: Sin abuso de incisos —/() ni patrón "afirmación + :" repetido en párrafos consecutivos
```

*Referencia original: `clo-author/.claude/rules/content-invariants.md` (INV-1 a INV-21 para economía empírica).*
