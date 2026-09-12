# Contrato de Roles — Usuario ↔ IA

> Esta skill es un **copiloto**, no un piloto automático. Hay decisiones y aportes que solo el investigador puede hacer. Este documento define quién hace qué en cada fase para que nadie se pierda. Cada SKILL lo referencia en sus puntos de traspaso ("handoffs").

## Convención de señalización

Cuando en cualquier fase se necesite una acción del investigador, la IA lo marca con un bloque visible:

```
🙋 ACCIÓN DEL USUARIO — [título corto]
Qué necesito de ti: [descripción concreta]
Por qué: [para qué sirve en el proyecto]
Cómo hacerlo: [pasos o formato esperado]
Mientras tanto: [qué hago yo o qué queda en pausa]
```

La IA **no avanza** más allá de un handoff bloqueante hasta que el usuario responde. Los handoffs no bloqueantes se listan pero no detienen el flujo.

---

## Quién hace qué, por fase

| Fase | 🧑 El usuario aporta / decide | 🤖 La IA hace |
|---|---|---|
| **Inicio (`/iniciar`)** | Nombre del proyecto, institución, si hay convocatoria, si usa Zotero, qué materiales tiene, y cualquier documento inicial (brief, instrucciones, convocatoria en PDF/DOCX) | Crea el andamiaje, el tablero `PROYECTO.md`, inicializa `state.json` y convierte los documentos iniciales a `documentos_base/*.md` |
| **Convocatoria (`/convocatoria`)** | El texto o el documento de la convocatoria (o pide el default Minciencias) | Extrae apartados, límites y criterios → perfil de convocatoria |
| **Descubrir — entrevista** | Responde la entrevista de investigación (fenómeno, motivación, campo, posición) | Formaliza la pregunta y el paradigma en una especificación |
| **Descubrir — literatura** | **Confirma qué referencias encontradas son pertinentes** e **importa las elegidas a Zotero** | Busca, puntúa proximidad, marca `[NUEVA_CANDIDATA]`, reporta saturación |
| **Descubrir — datos/fuentes** | Confirma acceso real a datos/fuentes; consigue permisos de archivo | Evalúa factibilidad (A-D) y sesgo archivístico |
| **Zotero** | **Exporta su biblioteca a `.bib` y la vincula al proyecto** (ver `zotero-workflow.md`) | Verifica que cada cita `[@clave]` exista en el `.bib` |
| **Ética** | Aporta aprobación IRB/comité y consentimientos | Genera el checklist ético y plantillas |
| **Estrategia** | Aprueba el diseño metodológico y la posición epistemológica | Propone diseño, saturación, muestreo, reflexividad |
| **Análisis** | **Aporta las transcripciones/corpus**; completa `baseline_reflexivity.md`; **revisa las citas marcadas `[REVISAR_MANUAL]`** | Estructura el corpus, extrae citas por script, codifica, calcula cobertura |
| **Propuesta / Redacción** | **Aprueba cada outline** antes de redactar; completa los marcadores `[PENDIENTE]` y `[VERIFICAR]`; revisa qué se limpió al generar `propuesta_final.md` | Redacta según outline, ancla en evidencia, preserva la voz; sanitiza la versión externa (sin referencias internas al proceso) |
| **Revisión** | Decide qué observaciones de árbitros acepta o disiente | Simula árbitros y sintetiza veredicto |
| **Envío** | Confirma datos de autor, financiación y declaraciones | Empaqueta el envío y verifica invariantes |

---

## Las 4 acciones del usuario que más se olvidan

Estas son responsabilidad **exclusiva** del investigador y la IA no puede hacerlas por él:

1. **Confirmar las fuentes encontradas.** La IA propone referencias con `[NUEVA_CANDIDATA]`; tú decides cuáles entran al proyecto. Una referencia sin confirmar no se cita.
2. **Vincular Zotero al proyecto.** Exportar la biblioteca a `master_supporting_docs/Bibliography_base.bib` (Better BibTeX) y avisar para registrar la ruta en `state.json`. Sin esto, no hay verificación de citas.
3. **Aportar el material empírico.** Transcripciones, documentos o datos van en `data/raw/`. La IA no inventa datos: sin corpus no hay análisis.
4. **Aprobar los outlines y completar los marcadores.** Nada se redacta sin outline aprobado; los `[PENDIENTE]`/`[VERIFICAR]` los cierra el investigador.

---

## Qué NO hace la IA (límites)

- No inventa citas, datos ni hallazgos (los marca como pendientes).
- No importa referencias a Zotero por ti (es tu curaduría intelectual).
- No decide por ti el paradigma ni el veredicto de publicación (lo propone y lo argumenta).
- No sobrescribe tus documentos originales: las versiones nuevas van fechadas o en carpetas nuevas.
