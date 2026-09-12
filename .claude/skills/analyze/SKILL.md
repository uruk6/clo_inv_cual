---
name: analizar
description: Análisis de datos de extremo a extremo (Métodos Mixtos). Templates Python embebidos, ciclos de codificación, protocolo anti-alucinación y backtracking. Reemplaza a /analyze. ACTIVAR cuando el usuario diga "analiza los datos", "procesa el corpus", "codifica las entrevistas", "corre el análisis", "extrae las citas", "haz la codificación cualitativa", "analiza estadísticamente".
argument-hint: "[ruta del dataset o objetivo] Opciones: --dual [lang1,lang2]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash,Task
---

# Analizar

## Gestión de Estado (Ejecutar al Inicio y al Final)

**Al inicio:** Leer `state.json` en la raíz del proyecto.
- Verificar prerequisito: `estrategia.estado == "completado"`. Si no se cumple, abortar: "⚠ `/analizar` requiere que `/estrategia` haya completado el diseño metodológico (`estrategia.estado = completado` en `state.json`)."
- Cargar `estrategia.ruta_memo`, `proyecto.paradigma`, `proyecto.tipo_articulo`.

**Al final:** Actualizar en `state.json`:
- Cuantitativo: `analisis.cuantitativo.ruta_dataset`, `ruta_modelos`, `ruta_results_summary`, `timestamp`
- Cualitativo: `analisis.cualitativo.ruta_citas_json`, `ruta_corpus_codificado`, `ruta_memos`, `ciclo_codificacion`, `ruta_baseline_reflexivity`, `citas_requieren_revision_manual`, `kappa_intercoder`, `timestamp`
- Mixto: `analisis.integracion_mixta.ruta_joint_display`, `timestamp`
- Errores capturados: `analisis.errores_log`
- `analisis.estado` → `"completado"`
- `_meta.ultima_actualizacion` y `_meta.historial_skills_ejecutadas`

---

Ejecuta un análisis de datos integral despachando al **Analista-IA** (análisis/codificación), al **Curador-Corpus** (limpieza/estructuración) y al **coder-critic** (revisión).

**Entrada:** `$ARGUMENTS` — ruta del dataset o descripción del objetivo de investigación.

---

## Flujo de Trabajo

### Paso 1: Pre-Code Report (Obligatorio)

Antes de escribir cualquier código, el Analista-IA emite:

```markdown
## Pre-Code Report
**Estrategia/Memo:** [ruta o "no encontrado"]
**Paradigma:** [Cuantitativo / Cualitativo / Mixto — desde state.json]
**Tipo de Artículo:** [desde state.json.proyecto.tipo_articulo]
**Lenguaje:** [R / Python — desde CLAUDE.md]

**Enfoque Metodológico:** [Cuantitativo / Cualitativo / Mixto]
**Ciclo de codificación (si cuali):** [Teoría fundamentada A / Análisis Temático Reflexivo B]
**Pipeline de Scripts Planificado:**
- [ej: limpieza → segmentacion → extraccion_citas → codificacion → coocurrencias]

**Variables Clave / Categorías:**
- Resultado/Fenómeno: [nombre] → [nombre_codigo]
- Tratamiento/Contexto: [nombre] → [nombre_codigo]
- Libro de Códigos (si es cuali): [enlace o lista de categorías]

**Fuente de Datos:** [ruta o descripción del corpus/dataset]
**Trazabilidad:** [Confirmar si el flujo garantiza vínculo Cita ↔ Documento_Origen]

**Memo reflexivo baseline:** El investigador debe completar `informes/06_analisis/memos/baseline_reflexivity.md` antes de codificar. Este memo registra preconcepciones, expectativas teóricas y posicionamiento.

Procediendo a la implementación.
```

> 🙋 **ACCIÓN DEL USUARIO — Aportar corpus y baseline de reflexividad**
> Qué necesito: (1) tu material bruto (transcripciones, documentos, datos) en `data/raw/`; (2) que completes `informes/06_analisis/memos/baseline_reflexivity.md` **antes** de codificar (si el estudio es cualitativo).
> Por qué: no invento datos ni testimonios; y en cualitativo, tu posicionamiento previo es parte del rigor (INV-CS-3).
> Cómo: deja los archivos en `data/raw/` y escribe 1-2 párrafos de preconcepciones en el memo.
> Mientras tanto: preparo el Pre-Code Report y los scripts de extracción.

---

### Paso 2: Preparación de Datos y Curaduría de Corpus

Si los datos son brutos, despachar según el tipo:
- **Datos Estructurados:** Despachar **Ingeniero-Datos** para limpieza de CSVs, valores nulos y estadística descriptiva inicial.
- **Corpus de Texto (Cuali):** Despachar **Curador-Corpus** para preprocesar entrevistas/documentos, estructurando (`id_documento`, `hablante`, `segmentos[{texto, contexto}]`) antes del análisis.

---

### Paso 3a: Modo Cuantitativo (R/Python)

- Generar estadísticas descriptivas, correlaciones y modelos causales.
- Disciplina numérica: guards para floats, pre-asignación, `set.seed` / semilla explícita.
- Guardar salidas en `paper/tables/` y `paper/figures/`.

---

### Paso 3b: Modo Cualitativo Computacional (Python — Protocolo Anti-Alucinación)

El Analista-IA opera bajo **REGLA ANTI-ALUCINACIÓN ESTRICTA**: prohibido codificar leyendo el documento completo en un solo paso. Usar siempre scripts en dos fases secuenciales.

#### Ciclos de codificación (declarar cuál aplica en el Pre-Code Report):

**Opción A — Teoría fundamentada (Strauss-Corbin):**
1. Codificación abierta (primer pase, inductivo — usar `segment_corpus.py`).
2. Codificación axial (agrupar en categorías y subcategorías).
3. Codificación selectiva (identificar categoría central).

**Opción B — Análisis Temático Reflexivo (Braun & Clarke 2019):**
1. Familiarización con los datos.
2. Generación de códigos iniciales (`extract_quotes.py` + revisión).
3. Búsqueda de temas.
4. Revisión de temas.
5. Definición y denominación de temas.
6. Producción del informe.

---

#### Template 1 — Segmentación Inductiva (`segment_corpus.py`)

Usar cuando el enfoque es inductivo o abductivo (sin codebook previo).

```python
# ============================================================
# TEMPLATE BASE: segment_corpus.py
# Propósito: Segmentar corpus en unidades de significado SIN codebook
# Entradas: data/cleaned/[corpus].json
# Salidas: data/cleaned/segments_[corpus].json (candidatos para codificación abierta manual)
# INSTRUCCIÓN AL AGENTE: Completar únicamente las secciones marcadas [COMPLETAR]
# ============================================================
import json
import re
from pathlib import Path

# [COMPLETAR] Ruta del corpus
CORPUS_PATH = Path("data/cleaned/[COMPLETAR_nombre_corpus].json")
OUTPUT_PATH = Path("data/cleaned/segments_[COMPLETAR_nombre_corpus].json")

# [COMPLETAR] Tamaño mínimo de segmento en palabras (sugerido: 20-50)
MIN_WORDS = 20

with open(CORPUS_PATH, encoding="utf-8") as f:
    corpus = json.load(f)

segmentos = []
for doc in corpus:
    for i, seg in enumerate(doc["segmentos"]):
        texto = seg["texto"].strip()
        if len(texto.split()) >= MIN_WORDS:
            segmentos.append({
                "id_segmento": f"{doc['id_documento']}_S{i:04d}",
                "id_documento": doc["id_documento"],
                "hablante": doc.get("hablante", ""),
                "texto": texto,
                "contexto": seg.get("contexto", ""),
                "codigo_abierto": "",  # A completar manualmente o en Paso 2
                "notas": ""
            })

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(segmentos, f, ensure_ascii=False, indent=2)

print(f"[OK] Segmentos generados: {len(segmentos)} — guardados en {OUTPUT_PATH}")
print("[SIGUIENTE] Revisar manualmente y asignar 'codigo_abierto' a cada segmento.")
```

---

#### Template 2 — Extracción de Citas Deductiva (`extract_quotes.py`)

Usar cuando existe un codebook previo (enfoque deductivo).

```python
# ============================================================
# TEMPLATE BASE: extract_quotes.py
# Propósito: Extraer citas literales del corpus guiado por codebook
# Entradas: data/cleaned/[corpus].json
# Salidas: data/cleaned/temp_cites.json
# INSTRUCCIÓN AL AGENTE: Completar únicamente las secciones marcadas [COMPLETAR]
# ============================================================
import json
import re
from pathlib import Path

# [COMPLETAR] Rutas de entrada y salida
CORPUS_PATH = Path("data/cleaned/[COMPLETAR_nombre_corpus].json")
OUTPUT_PATH = Path("data/cleaned/temp_cites.json")

# [COMPLETAR] Palabras clave del libro de códigos (una lista por cada código general)
KEYWORDS = {
    "[COMPLETAR_codigo_1]": ["[termino_a]", "[termino_b]"],
    "[COMPLETAR_codigo_2]": ["[termino_c]", "[termino_d]"],
}

with open(CORPUS_PATH, encoding="utf-8") as f:
    corpus = json.load(f)

citas = []
for doc in corpus:
    for i, segmento in enumerate(doc["segmentos"]):
        texto = segmento["texto"]
        for codigo, terminos in KEYWORDS.items():
            if any(t.lower() in texto.lower() for t in terminos):
                citas.append({
                    "id_cita": f"{doc['id_documento']}_S{i:04d}",
                    "texto": texto,
                    "id_documento": doc["id_documento"],
                    "contexto": segmento.get("contexto", ""),
                    "codigo_candidato": codigo
                })

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(citas, f, ensure_ascii=False, indent=2)

print(f"[OK] Citas extraídas: {len(citas)} — guardadas en {OUTPUT_PATH}")
```

---

#### Template 3 — Codificación (`code_quotes.py`)

```python
# ============================================================
# TEMPLATE BASE: code_quotes.py
# Propósito: Mapear citas contra el libro de códigos
# Entradas: data/cleaned/temp_cites.json
# Salidas: data/cleaned/corpus_coded.csv (formato LARGO)
# INSTRUCCIÓN AL AGENTE: Completar únicamente las secciones marcadas [COMPLETAR]
# ============================================================
import pandas as pd
import json
from pathlib import Path

CITAS_PATH = Path("data/cleaned/temp_cites.json")
OUTPUT_PATH = Path("data/cleaned/corpus_coded.csv")

# [COMPLETAR] Libro de códigos: {codigo_general: {subcodigo: [palabras_clave]}}
CODEBOOK = {
    "[COMPLETAR_codigo_general_1]": {
        "[COMPLETAR_subcodigo_1a]": ["[keyword_1]", "[keyword_2]"],
        "[COMPLETAR_subcodigo_1b]": ["[keyword_3]"],
    },
}

# [COMPLETAR] Fuente teórica del libro de códigos (ej. "Bourdieu 1984", "Grounded")
FUENTE_TEORICA = "[COMPLETAR]"

with open(CITAS_PATH, encoding="utf-8") as f:
    citas = json.load(f)

resultados = []
for cita in citas:
    subcodigo_asignado = "[REVISAR_MANUAL]"
    tipo_codigo = "deductivo"
    for subcodigo, keywords in CODEBOOK.get(cita["codigo_candidato"], {}).items():
        if any(kw.lower() in cita["texto"].lower() for kw in keywords):
            subcodigo_asignado = subcodigo
            break
    # Soporte para códigos in vivo: si el subcódigo contiene comillas, es expresión emic
    if subcodigo_asignado.startswith('"') or subcodigo_asignado.startswith("'"):
        tipo_codigo = "in_vivo"
    resultados.append({
        "id_cita": cita["id_cita"],
        "id_documento": cita["id_documento"],
        "texto": cita["texto"],
        "codigo_general": cita["codigo_candidato"],
        "subcodigo_aplicado": subcodigo_asignado,
        "tipo_codigo": tipo_codigo,  # deductivo | inductivo | in_vivo
        "fuente_teorica": FUENTE_TEORICA
    })

# FORMATO LARGO: una fila por combinación (cita, código)
df = pd.DataFrame(resultados)
df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")
print(f"[OK] Citas codificadas: {len(df)} — guardadas en {OUTPUT_PATH}")
print(f"[AVISO] Citas que requieren revisión manual: {(df['subcodigo_aplicado'] == '[REVISAR_MANUAL]').sum()}")
```

**Nota sobre formato largo:** Una misma cita con 3 códigos genera 3 filas. Columnas obligatorias: `id_cita, id_documento, texto, codigo_general, subcodigo_aplicado, tipo_codigo (in_vivo|deductivo|inductivo), fuente_teorica`.

**Códigos in vivo:** Si la cita contiene una expresión emic significativa del participante, el subcódigo puede ser esa expresión literal entrecomillada. Ejemplo: `"el territorio nos duele"`. Marcar `tipo_codigo = in_vivo`.

---

#### Template 4 — Memos Analíticos (`generate_memos.py`)

```python
# ============================================================
# TEMPLATE BASE: generate_memos.py
# Propósito: Crear memos analíticos trazables
# Salidas: informes/06_analisis/memos/memo_[id].json
# ============================================================
import json
from pathlib import Path
from datetime import datetime

MEMOS_DIR = Path("informes/06_analisis/memos/")
MEMOS_DIR.mkdir(parents=True, exist_ok=True)

def crear_memo(id_memo: str, tipo: str, citas_asociadas: list, contenido: str):
    """
    tipo: "codigo" | "teorico" | "metodologico" | "reflexivo"
    citas_asociadas: lista de ID_Cita relacionadas
    """
    memo = {
        "id_memo": id_memo,
        "fecha": datetime.now().isoformat(),
        "tipo": tipo,
        "citas_asociadas": citas_asociadas,
        "contenido": contenido
    }
    ruta = MEMOS_DIR / f"memo_{id_memo}.json"
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(memo, f, ensure_ascii=False, indent=2)
    print(f"[OK] Memo guardado en {ruta}")
    return memo

# Ejemplo de uso:
# crear_memo("M001", "teorico", ["ENT02_S14", "ENT03_S07"],
#            "El concepto de campo (Bourdieu) emerge claramente en los testimonios de líderes comunitarios.")
```

---

#### Submodo ACD — Análisis Crítico del Discurso (Crítico-Social)

Cuando `proyecto.tipo_articulo == "Crítico-Social"` o el diseño es IAP, añadir al pipeline:

1. **Análisis descriptivo** (nivel textual): léxico, sintaxis, modalidad.
2. **Análisis interpretativo** (prácticas discursivas): producción, distribución, consumo.
3. **Análisis explicativo** (prácticas sociales): poder, ideología. *(Fairclough, van Dijk, Wodak)*

Registrar en `informes/06_analisis/acd_analysis.md`.

---

#### Resolución de Errores — Protocolo de Backtracking (3 pasos)

Si un script falla durante la ejecución, seguir estos pasos **antes de reescribir el código**:

**Paso 1 — Leer el error exacto:**
- Identificar la línea y tipo de error (KeyError, FileNotFoundError, JSONDecodeError, etc.).
- Verificar que `CORPUS_PATH` apunta a un archivo que existe y tiene el formato esperado.
- Si es `KeyError`: imprimir `print(corpus[0].keys())` para verificar nombres de campos.

**Paso 2 — Verificar integridad del corpus:**
- Abrir `data/cleaned/[corpus].json` y confirmar que cada elemento tiene `id_documento` y `segmentos`.
- Confirmar que cada segmento tiene el campo `texto`.
- Si la estructura difiere: ajustar las referencias de campo en el template (no reescribir toda la lógica).

**Paso 3 — Escalar al usuario:**
- Si el error persiste tras los pasos 1 y 2, reportar:
  - El error exacto (texto completo del traceback).
  - El estado de `temp_cites.json` (si existe, cuántas citas se extrajeron antes del fallo).
  - La estructura real del corpus (claves encontradas vs. esperadas).
- **No reintentar más de 2 veces con el mismo error sin escalar.**

El error queda registrado en `state.json.analisis.errores_log`.

---

### Paso 3c: Interoperabilidad REFI-QDA (Opcional)

Al finalizar la codificación, si el investigador necesita revisión en ATLAS.ti, NVivo o MAXQDA:

Generar `data/cleaned/corpus_coded.qdpx` en formato REFI-QDA (ISO 24617) usando plantilla XML estándar. Permite importar el proyecto codificado a cualquier software de análisis cualitativo.

---

### Paso 3d: Confiabilidad Intercoders

Si se realiza una segunda codificación (investigador humano o segundo codificador):

1. Calcular **porcentaje de acuerdo simple**.
2. Calcular **Kappa de Cohen** (dos codificadores) o **Fleiss Kappa** (más de dos).
3. Reportar en `informes/06_analisis/intercoder_reliability.md`.
   - κ > 0.80: excelente
   - 0.60–0.80: sustancial
   - <0.60: problemático (requiere recodificación consensuada)

Guardar `kappa_intercoder` en `state.json.analisis.cualitativo.kappa_intercoder`.

---

### Paso 4: Revisión de Código (coder-critic)

El **coder-critic** valida:
1. **Alineación con la Estrategia:** ¿El código implementa el pipeline cuali/cuanti definido en el memo?
2. **Protocolo Anti-Alucinación:** ¿Se usaron scripts intermedios para la codificación o se intentó leer todo de una vez? (Deducción crítica si falló).
3. **Formato largo confirmado:** ¿`corpus_coded.csv` tiene una fila por par (cita, código)?
4. **Trazabilidad:** ¿Cada cita tiene `id_cita` rastreable a `id_documento`?
5. **Calidad y Reproducibilidad:** set.seed, rutas relativas, comentarios explicativos.
6. **INV-CS-1 a INV-CS-6:** Verificar invariantes de contenido relevantes.

---

### Paso 5: Presentación de Resultados

1. **Resumen de Resultados:** Estimaciones clave o hallazgos cualitativos dominantes → `informes/06_analisis/results_summary.md`.
2. **Evidencia Primaria (cuali):** Lista de citas clave vinculadas a sus códigos.
3. **Salidas:** Tablas en `paper/tables/`, figuras en `paper/figures/`.
4. **Reporte de cobertura:** Cuántos de los Y códigos tienen al menos una cita representada → `informes/06_analisis/code_coverage_report.md`.

---

## Principios
- **Complementariedad:** No excluir lo cuantitativo; integrarlo en el reporte mixto.
- **Evidencia Textual:** En análisis cualitativo, la cita literal es el dato primario.
- **Trazabilidad Total:** Todo hallazgo debe poder rastrearse hasta el documento de origen (`id_documento`).
- **Scripts sobre Lectura Directa:** Siempre preferir scripts de Python para procesar texto.
- **Backtracking antes de Reescribir:** Ante un error, diagnosticar primero con el protocolo de 3 pasos.
- **Invariantes:** Verificar `content-invariants-cs.md` antes de presentar resultados.
