# Memoria del Proyecto (Ciencias Sociales)

Registro de aprendizajes, decisiones metodológicas y temas emergentes que persisten entre sesiones.

---

## Decisiones Metodológicas

[LEARN:metodo] **Estructuración del Corpus:** Las transcripciones deben convertirse a formato JSON estructurado (`hablante`, `texto`, `metadatos`) antes de cualquier análisis para garantizar la trazabilidad de las citas.

[LEARN:metodo] **Protocolo de Codificación:** Se prefiere la codificación deductiva inicial (basada en el marco teórico) seguida de una fase inductiva para capturar temas emergentes no previstos.

## Temas y Categorías Emergentes

*Anotar aquí los códigos que surgen del análisis del Analista-IA.*

- [TEMA:Ejemplo] Descripción del tema y evidencia inicial encontrada.

## Lecciones del Workflow

[LEARN:workflow] **Extracción antes de Codificar:** Siempre ejecutar el script de extracción de citas literales (`scripts/python/extract_quotes.py`) para poblar la base de evidencia antes de redactar la sección de resultados.

[LEARN:workflow] **Validación de Citas:** Verificar que cada `ID_Cita` en el paper coincida exactamente con el registro en `data/cleaned/corpus_coded.csv` (formato largo: una fila por par cita-código).

## Bibliografía y Referencias

[LEARN:bib] **Zotero Integration:** Usar la exportación "Better BibTeX" de Zotero para mantener `master_supporting_docs/Bibliography_base.bib` actualizado. Claude debe leer este archivo antes de usar `/redactar`. Citación en Markdown estilo Pandoc (`[@clave]`). Ver `.claude/references/zotero-workflow.md`.

## Lecciones de Diseño de la Skill

[LEARN:diseño] **Copiloto, no piloto:** las acciones del usuario (confirmar fuentes, vincular Zotero, aportar corpus, aprobar outlines) se señalizan con bloques `🙋 ACCIÓN DEL USUARIO`. Ver `.claude/references/roles-usuario-ia.md`.

[LEARN:diseño] **Convocatoria antes que propuesta:** el perfil de convocatoria (apartados, límites, criterios) es el molde de la propuesta, igual que el perfil de revista es el molde del artículo. Default: Minciencias.

[LEARN:diseño] **Una sola carpeta de informes (2026-07-16):** `propuesta/` y `quality_reports/` se fusionaron en `informes/` (9 subcarpetas numeradas por momento: 01_convocatoria → 09_envio). Nunca crear una carpeta de reportes nueva a nivel raíz. Nuevas carpetas: `documentos_base/` (insumos semilla en `.md`) y `master_supporting_docs/fuentes_md/` (texto completo de fuentes por `citekey`, ver `.claude/references/fuentes-pdf-workflow.md`). `state.json` → schema 1.3.

[LEARN:diseño] **Documento externo vs. interno (2026-07-16):** la propuesta tiene dos versiones — `informes/04_propuesta/propuesta.md` (borrador de trabajo, con marcadores) e `informes/04_propuesta/propuesta_final.md` (sanitizada, sin referencias internas al proceso ni marcadores, lista para el evaluador). Ver INV-CS-16.

---
*Última actualización: 2026-07-16*
