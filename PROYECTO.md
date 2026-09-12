# 📋 Proyecto de Investigación — (sin inicializar)

> Este es el **tablero** de tu proyecto: te muestra siempre qué existe, dónde está y qué sigue.
> Para ponerlo en marcha, di **"empezar"** o **"por dónde empiezo"** y activaré `/iniciar`.

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
Estas 4 acciones son solo tuyas (ver `.claude/references/roles-usuario-ia.md`):
1. Confirmar las fuentes que encuentre y **vincular tu Zotero** (`Bibliography_base.bib`).
2. Aportar tu material empírico en `data/raw/`.
3. Aprobar los outlines antes de redactar y cerrar los `[PENDIENTE]`.
4. Aportar la convocatoria (o confirmar el default Minciencias).

## Próximo paso sugerido
👉 **Inicializar el proyecto** — dime *"empezar"* y activo `/iniciar`.
