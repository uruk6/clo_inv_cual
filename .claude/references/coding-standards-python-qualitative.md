# Estándares de Codificación Python (Cualitativo)

Este documento rige el desarrollo de scripts para el análisis cualitativo computacional en el proyecto `clo_inv_cual`.

## Librerías Obligatorias

- **Pandas:** Para la gestión de tablas de citas y metadatos.
- **spaCy / NLTK:** Para procesamiento de lenguaje natural (tokenización, lematización, NER).
- **JSON:** Para el almacenamiento de corpus estructurados.
- **Scikit-learn:** Para análisis de clusters o matrices de coocurrencia.

## Estructura del Script de Extracción

Todo script de extracción (`extract_quotes.py`) debe seguir este patrón:

1. **Carga:** Leer el corpus desde `data/cleaned/`.
2. **Filtro:** Aplicar Regex o reglas de spaCy para identificar bloques de texto.
3. **Validación:** Comprobar que la cita extraída mantiene el vínculo con el `ID_Documento`.
4. **Guardado:** Exportar a un archivo intermedio (ej. `temp_cites.json`) con campos: `id_cita`, `texto`, `id_doc`, `contexto`.

## Reglas de Oro

- **Semillas de Aleatoriedad:** Si se usa análisis de tópicos (LDA), fijar `random_state`.
- **Comentarios Hermenéuticos:** El código debe incluir comentarios que expliquen la relación entre la regla técnica (ej. una Regex) y el concepto teórico que intenta capturar.
- **Rutas Relativas:** Usar siempre `os.path.join` o `pathlib` para asegurar la portabilidad entre sistemas.
