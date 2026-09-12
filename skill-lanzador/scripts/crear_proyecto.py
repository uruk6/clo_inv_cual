#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
crear_proyecto.py -- Arma el andamiaje completo de un proyecto nuevo de
investigacion en Ciencias Sociales / metodos mixtos (sistema clo_inv_cual):
carpetas, PROYECTO.md, MEMORY.md y state.json, listos para /iniciar-cs.

Uso:
    python crear_proyecto.py [ruta]     # por defecto, la carpeta actual
"""
import json
import sys
from pathlib import Path

CARPETAS = [
    "documentos_base",
    "informes/01_convocatoria",
    "informes/02_entrevista",
    "informes/03_estado_del_arte",
    "informes/04_propuesta",
    "informes/05_estrategia",
    "informes/06_analisis/memos",
    "informes/07_redaccion/journal_profiles",
    "informes/08_revision",
    "informes/09_envio",
    "informes/plans",
    "paper/figures",
    "paper/sections",
    "paper/tables",
    "data/raw",
    "data/cleaned",
    "scripts/python",
    "master_supporting_docs/fuentes_md",
]

PROYECTO_MD = """# 📋 Proyecto de Investigación — (sin inicializar)

> Este es el **tablero** de tu proyecto: te muestra siempre qué existe, dónde está y qué sigue.
> Para ponerlo en marcha, di **"empezar"** o **"por dónde empiezo"** y activaré `/iniciar-cs`.

**Institución:** —  ·  **Paradigma:** por definir
**Convocatoria:** por definir (si no hay claridad, se usa Minciencias por defecto)
**Última actualización:** —

---

## ¿Dónde queda cada cosa? (todos los entregables son `.md`)

| Carpeta / archivo | Qué contiene | Formato |
|---|---|---|
| `documentos_base/` | 🌱 Insumos semilla del proyecto (brief, instrucciones, convocatoria en bruto) | `.md` |
| `informes/04_propuesta/propuesta_final.md` | 🎯 La propuesta / anteproyecto para la convocatoria (versión limpia, sin referencias internas) | `.md` |
| `paper/main.md` | 📄 El artículo final y sus secciones (`paper/sections/`) | `.md` |
| `data/raw/` | 🧑 Tu material bruto (entrevistas, datos) — **lo aportas tú** | varios |
| `data/cleaned/` | Corpus estructurado y codificado | `.json` / `.csv` |
| `master_supporting_docs/Bibliography_base.bib` | 🔗 Tu biblioteca (exportada desde Zotero) — solo metadatos de cita | `.bib` |
| `master_supporting_docs/fuentes_md/` | 📚 Texto completo de cada fuente citada, un archivo por `citekey` | `.md` |
| `informes/` | 📊 **Todos** los informes del proceso (convocatoria, estado del arte, propuesta, estrategia, análisis, redacción, revisión, envío) | `.md` |
| `scripts/python/` | Los scripts de análisis | `.py` |

> Los documentos que **evidencian** tu proyecto son la **propuesta**, el **artículo** y los **reportes de calidad**, todos en `.md`, todos dentro de `informes/` (salvo el artículo, en `paper/`). Se exportan a Word/PDF con Pandoc.

---

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

Leyenda: ✅ completada · 🟡 en curso · ⬜ pendiente

---

## Lo que necesito de ti (🙋)
Estas 4 acciones son solo tuyas:
1. Confirmar las fuentes que encuentre y **vincular tu Zotero** (`Bibliography_base.bib`).
2. Aportar tu material empírico en `data/raw/`.
3. Aprobar los outlines antes de redactar y cerrar los `[PENDIENTE]`.
4. Aportar la convocatoria (o confirmar el default Minciencias).

## Próximo paso sugerido
👉 **Inicializar el proyecto** — dime *"empezar"* y activo `/iniciar-cs`.
"""

MEMORY_MD = """# Memoria del Proyecto (Ciencias Sociales)

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

[LEARN:bib] **Zotero Integration:** Usar la exportación "Better BibTeX" de Zotero para mantener `master_supporting_docs/Bibliography_base.bib` actualizado. Citación en Markdown estilo Pandoc (`[@clave]`).

## Lecciones de Diseño de la Skill

[LEARN:diseño] **Copiloto, no piloto:** las acciones del usuario (confirmar fuentes, vincular Zotero, aportar corpus, aprobar outlines) se señalizan con bloques `🙋 ACCIÓN DEL USUARIO`.

[LEARN:diseño] **Convocatoria antes que propuesta:** el perfil de convocatoria (apartados, límites, criterios) es el molde de la propuesta, igual que el perfil de revista es el molde del artículo. Default: Minciencias.

[LEARN:diseño] **Una sola carpeta de informes:** `propuesta/` y `quality_reports/` se fusionaron en `informes/` (9 subcarpetas numeradas por momento: 01_convocatoria → 09_envio). Nunca crear una carpeta de reportes nueva a nivel raíz.

[LEARN:diseño] **Documento externo vs. interno:** la propuesta tiene dos versiones — `informes/04_propuesta/propuesta.md` (borrador de trabajo, con marcadores) e `informes/04_propuesta/propuesta_final.md` (sanitizada, sin referencias internas al proceso ni marcadores, lista para el evaluador).
"""

BIBLIOGRAPHY_BIB = """% ============================================================
% Bibliography_base.bib — Bibliografía maestra del proyecto
% ------------------------------------------------------------
% Este archivo es la ÚNICA fuente de verdad para las citas del proyecto.
% Se sincroniza desde Zotero con el plugin "Better BibTeX"
% (exportación automática de la colección del proyecto a este archivo).
%
% 🙋 ACCIÓN DEL USUARIO: exporta tu colección de Zotero aquí y registra
% la ruta en state.json → bibliografia.ruta_bib.
%
% Formato de clave recomendado: [auth][year] (ej. Bourdieu1980).
% No borres esta cabecera. Las entradas nuevas van debajo.
% ============================================================
"""


def state_json_inicial():
    return {
        "_meta": {
            "version_schema": "1.3",
            "creado": "",
            "ultima_actualizacion": "",
            "historial_skills_ejecutadas": [],
        },
        "proyecto": {
            "nombre": "", "institucion": "", "paradigma": "",
            "diseno_cualitativo": "", "tipo_mixto": "", "tipo_articulo": "",
            "idioma_corpus": "es",
        },
        "documentos_base": {"ruta_carpeta": "documentos_base/", "documentos": []},
        "convocatoria": {
            "aplica": None, "nombre": "", "entidad": "",
            "ruta_perfil": "informes/01_convocatoria/convocatoria_profile.md",
            "fecha_cierre": "", "estado": "pendiente",
        },
        "bibliografia": {
            "ruta_bib": "master_supporting_docs/Bibliography_base.bib",
            "ruta_fuentes_md": "master_supporting_docs/fuentes_md/",
            "vinculado_zotero": False, "total_entradas": 0, "ultima_sincronizacion": "",
        },
        "etica": {
            "irb_aprobacion": "", "consentimientos_registrados": 0,
            "protocolo_anonimizacion": "", "ruta_declaracion_etica": "",
            "checklist_aplicado": False,
        },
        "descubrimiento": {
            "pregunta_investigacion": "", "ruta_spec": "informes/02_entrevista/",
            "ruta_lit_review": "informes/03_estado_del_arte/",
            "ruta_data_exploration": "informes/03_estado_del_arte/",
            "ruta_sources_exploration": "informes/03_estado_del_arte/",
            "referencias_nuevas_candidatas": [], "estado": "pendiente",
            "timestamp_completado": "",
        },
        "propuesta": {
            "ruta_documento": "informes/04_propuesta/propuesta.md",
            "ruta_documento_final": "", "apartados_completados": [],
            "score_evaluacion": None, "sanitizacion_externa_aplicada": False,
            "estado": "pendiente", "timestamp_completado": "",
        },
        "estrategia": {
            "ruta_memo": "", "posicion_epistemologica": "", "criterios_calidad": [],
            "tipo_saturacion": "", "estrategia_muestreo": "", "decision_records": [],
            "score_critic": None, "estado": "pendiente", "timestamp_completado": "",
        },
        "analisis": {
            "cuantitativo": {"ruta_dataset": "", "ruta_modelos": "",
                              "ruta_results_summary": "", "timestamp": ""},
            "cualitativo": {
                "ruta_corpus_raw": "data/raw/", "ruta_corpus_limpio": "data/cleaned/",
                "ruta_citas_json": "", "ruta_corpus_codificado": "", "ruta_memos": "",
                "ciclo_codificacion": "", "ruta_baseline_reflexivity": "",
                "citas_requieren_revision_manual": None, "kappa_intercoder": None,
                "timestamp": "",
            },
            "integracion_mixta": {"ruta_joint_display": "", "timestamp": ""},
            "errores_log": [], "estado": "pendiente",
        },
        "redaccion": {
            "secciones_completadas": [], "ruta_outline_aprobado": "",
            "ruta_paper_main": "paper/main.md", "perfil_revista_activo": "",
            "cobertura_codigos": {}, "estado": "pendiente", "timestamp_completado": "",
        },
        "ciclo_editorial": {
            "journal_objetivo": "", "estado_submission": "no_iniciado",
            "historial_revisiones": [], "carta_respuesta_arbitros": "",
        },
    }


def main():
    destino = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    destino.mkdir(parents=True, exist_ok=True)
    print(f"Proyecto: {destino}")

    for c in CARPETAS:
        p = destino / c
        p.mkdir(parents=True, exist_ok=True)
        (p / ".gitkeep").touch(exist_ok=True)
    print(f"  + {len(CARPETAS)} carpetas")

    archivos = {
        "PROYECTO.md": PROYECTO_MD,
        "MEMORY.md": MEMORY_MD,
        "master_supporting_docs/Bibliography_base.bib": BIBLIOGRAPHY_BIB,
    }
    for rel, contenido in archivos.items():
        ruta = destino / rel
        if not ruta.exists():
            ruta.write_text(contenido, encoding="utf-8")
            print(f"  + {rel}")
        else:
            print(f"  = ya existe, se conserva: {rel}")

    state_path = destino / "state.json"
    if not state_path.exists():
        state_path.write_text(json.dumps(state_json_inicial(), ensure_ascii=False, indent=2),
                               encoding="utf-8")
        print("  + state.json")
    else:
        print("  = ya existe, se conserva: state.json")

    print("\nListo. Sigue con la skill iniciar-cs para la bienvenida y la puesta en marcha.")


if __name__ == "__main__":
    main()
