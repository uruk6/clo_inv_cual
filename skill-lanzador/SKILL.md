---
name: clo_inv_cual
description: Punto de entrada único del sistema de investigación en Ciencias Sociales y métodos mixtos (clo_inv_cual). Arma de una vez toda la estructura de carpetas de un proyecto nuevo (documentos_base/, informes/01-09, paper/, data/, master_supporting_docs/, scripts/python/, PROYECTO.md, MEMORY.md, state.json) y activa la bienvenida conversacional. ACTIVAR cuando el usuario diga "/clo_inv_cual", "arranca un proyecto de investigación cualitativa", "quiero empezar una investigación en ciencias sociales", "nuevo proyecto de métodos mixtos", "monta el proyecto de investigación cualitativa aquí".
argument-hint: "[ruta o nombre del proyecto] (opcional, por defecto la carpeta actual)"
allowed-tools: Read, Write, Bash, Skill
---

# clo_inv_cual — Arranque de un proyecto nuevo

Esta skill es el **único punto de entrada** del sistema. No hace falta que el usuario conozca
ninguna de las 11 sub-skills (`iniciar-cs`, `convocatoria`, `descubrir`, `propuesta`, `estrategia`,
`analizar`, `redactar`, `evaluar-cs`, `revisar`, `responder-arbitros`, `enviar`) ni los 15 agentes:
todas ya están instaladas globalmente y se activan solas conforme avanza el proyecto.

## Qué hacer al activarse

1. **Determinar la carpeta destino.** Si el usuario dio una ruta o un nombre de proyecto en el
   argumento, usarla (se crea si no existe). Si no dio nada:
   - Si la carpeta actual está vacía o el usuario ya dijo "aquí", usar la carpeta actual.
   - Si no, preguntar en una línea: "¿En qué carpeta armo el proyecto? (nombre nuevo, o 'aquí' para
     usar la carpeta actual)".

2. **Construir el andamiaje**, ejecutando:
   ```bash
   python "~/.claude/skills/clo_inv_cual/scripts/crear_proyecto.py" [ruta_destino]
   ```
   Esto crea las 18 carpetas del proyecto (con `.gitkeep`), `PROYECTO.md`, `MEMORY.md` y
   `state.json`, todos en blanco/plantilla — nunca sobrescribe algo que ya exista.

3. **Si el usuario ya dio información del proyecto** en el mismo mensaje que activó esta skill
   (nombre, institución, tema, pregunta de investigación, convocatoria a la que se postula, etc.),
   no la descartes: pásala de una vez a la skill `iniciar-cs` para que la incorpore en la
   conversación de arranque en vez de volver a preguntarla.

4. **Activar la skill `iniciar-cs`** (usar la herramienta Skill) para la bienvenida, el contrato de
   roles, y la inicialización conversacional de `PROYECTO.md`/`state.json` con los datos reales del
   proyecto. Esta skill ya vive instalada globalmente — no requiere que el usuario la invoque a mano.

## Nota sobre el origen

Este sistema viene de la plantilla de proyecto `clo_inv_cual` (repositorio privado en GitHub del
docente: `uruk6/clo_inv_cual`), promovida a skills+agentes globales el 2026-09-12 para poder usarse
en cualquier carpeta con solo `/clo_inv_cual`, sin clonar el repositorio cada vez. El repositorio
original sigue existiendo como plantilla de referencia y como respaldo versionado del sistema
completo.
