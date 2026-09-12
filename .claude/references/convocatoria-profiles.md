# Perfiles de Convocatoria — Referencia

> Un "perfil de convocatoria" es el equivalente, para la fase de **propuesta**, de lo que el "perfil de revista" es para el artículo: captura los **apartados obligatorios**, los **límites de extensión** y los **criterios de evaluación** de la convocatoria a la que el investigador se postula.
>
> Se usa con `/convocatoria [fuente]` y `/propuesta`. Cada campo se marca `[EXTRAIDO]` (del documento oficial), `[ASUMIDO]` (convención) o `[VERIFICAR]` (requiere confirmación del usuario). **Las convocatorias cambian cada año: verifica siempre contra el documento oficial vigente.**

---

## Plantilla genérica de perfil

```yaml
convocatoria_key: ""
nombre: ""
entidad: ""              # p.ej. Minciencias, vicerrectoría de investigación, revista X
tipo: ""                 # financiacion | anteproyecto_grado | call_revista
url_terminos: ""
fecha_cierre: ""
estado_perfil: "borrador"

# --- Formato de entrega ---
apartados_obligatorios: []     # lista ordenada de secciones exigidas
apartados_opcionales: []
limite_extension: ""           # p.ej. "20 páginas" o "8000 palabras"
limite_resumen: ""             # p.ej. "300 palabras"
formato_archivo: ""            # docx | pdf
anexos_requeridos: []          # CvLAC, GrupLAC, aval institucional, cartas, presupuesto

# --- Criterios de evaluación (ponderados, suman 100) ---
criterios_evaluacion: []       # [{criterio, peso, descripcion}]
puntaje_minimo_aprobacion: null

# --- Componentes especiales ---
requiere_presupuesto: false
requiere_cronograma: false
productos_esperados: []        # categorías de resultados esperados
consideraciones_eticas: false

notas: ""
```

---

## minciencias — Convocatoria de Proyectos de Investigación (DEFAULT)

> Preset por defecto cuando el usuario no tiene claridad sobre la convocatoria. Basado en la estructura típica de las convocatorias de Minciencias (Colombia) para proyectos de CTeI en ciencias sociales y humanas. **Marcado mayormente `[ASUMIDO]` — ajústalo al documento de la convocatoria específica del año.**

```yaml
convocatoria_key: minciencias
nombre: "Convocatoria de Proyectos de Investigación — Minciencias (genérica)"
entidad: "Ministerio de Ciencia, Tecnología e Innovación (Colombia)"
tipo: financiacion
url_terminos: ""            # [VERIFICAR — depende de la convocatoria del año]
fecha_cierre: ""            # [VERIFICAR]
estado_perfil: "borrador"

apartados_obligatorios:
  - "Título"
  - "Resumen ejecutivo"
  - "Planteamiento del problema y pregunta de investigación"
  - "Estado del arte / Marco teórico y conceptual"
  - "Objetivos (general y específicos)"
  - "Metodología"
  - "Resultados/Productos esperados"
  - "Impactos esperados"
  - "Cronograma de actividades"
  - "Presupuesto y su justificación"
  - "Consideraciones éticas"
  - "Bibliografía / Referencias"
apartados_opcionales:
  - "Estrategia de comunicación y apropiación social del conocimiento"
  - "Trayectoria del grupo de investigación"

limite_extension: "20-30 páginas (cuerpo del proyecto)"   # [ASUMIDO — VERIFICAR]
limite_resumen: "300-500 palabras"                          # [ASUMIDO]
formato_archivo: "pdf"                                      # [ASUMIDO]
anexos_requeridos:
  - "CvLAC de los investigadores"
  - "GrupLAC del grupo de investigación"
  - "Aval institucional"
  - "Carta de aval del comité de ética (si aplica)"

criterios_evaluacion:
  - { criterio: "Calidad técnica y científica (coherencia problema-objetivos-metodología, estado del arte)", peso: 40, descripcion: "Rigor y solidez de la propuesta" }
  - { criterio: "Pertinencia e impacto esperado", peso: 25, descripcion: "Relevancia social/científica y productos esperados" }
  - { criterio: "Capacidad e idoneidad del equipo/grupo", peso: 20, descripcion: "Trayectoria (GrupLAC/CvLAC)" }
  - { criterio: "Viabilidad (cronograma y presupuesto)", peso: 15, descripcion: "Factibilidad y justificación del gasto" }
puntaje_minimo_aprobacion: 70   # [ASUMIDO — VERIFICAR]

requiere_presupuesto: true
requiere_cronograma: true
productos_esperados:
  - "Generación de nuevo conocimiento (artículos, libros)"
  - "Fortalecimiento de la CTeI y formación de recurso humano (tesis, jóvenes investigadores)"
  - "Apropiación social del conocimiento (eventos, cartillas, divulgación)"
consideraciones_eticas: true

notas: "Estructura típica de Minciencias. La ponderación y los apartados varían por convocatoria y por año — SIEMPRE cargar el documento oficial vigente con /convocatoria [documento]. Para proyectos con comunidades, articular con el checklist ético (/descubrir etica) y, si es IAP, con la devolución a la comunidad."
```

---

## anteproyecto-grado — Anteproyecto / Proyecto de Grado (plantilla institucional genérica)

```yaml
convocatoria_key: anteproyecto-grado
nombre: "Anteproyecto de grado (formato institucional genérico)"
entidad: "Universidad / programa académico"
tipo: anteproyecto_grado
estado_perfil: "borrador"

apartados_obligatorios:
  - "Título"
  - "Planteamiento del problema"
  - "Pregunta de investigación"
  - "Justificación"
  - "Objetivos (general y específicos)"
  - "Marco teórico / Estado del arte"
  - "Metodología"
  - "Consideraciones éticas"
  - "Cronograma"
  - "Referencias (APA 7)"
apartados_opcionales:
  - "Presupuesto"
  - "Anexos (instrumentos)"

limite_extension: "15-25 páginas"      # [ASUMIDO — depende del programa]
limite_resumen: "250 palabras"          # [ASUMIDO]
formato_archivo: "docx"
anexos_requeridos:
  - "Aval del director/asesor"

criterios_evaluacion:
  - { criterio: "Claridad y pertinencia del problema y la pregunta", peso: 25, descripcion: "" }
  - { criterio: "Solidez del marco teórico y estado del arte", peso: 25, descripcion: "" }
  - { criterio: "Coherencia metodológica", peso: 30, descripcion: "Ajuste pregunta-diseño" }
  - { criterio: "Viabilidad y redacción académica", peso: 20, descripcion: "" }
puntaje_minimo_aprobacion: 3.0   # escala 0.0-5.0 [ASUMIDO]

requiere_presupuesto: false
requiere_cronograma: true
consideraciones_eticas: true
notas: "Formato genérico de anteproyecto de pregrado/posgrado. Ajustar a la rúbrica específica del programa."
```

---

## Índice de claves

| Clave | Tipo | Entidad | Uso |
|---|---|---|---|
| `minciencias` | Financiación | Minciencias (CO) | **Default** cuando no hay claridad |
| `anteproyecto-grado` | Anteproyecto | Universidad | Trabajos de grado |

*Para una convocatoria específica: `/convocatoria [documento o URL o texto]` y el sistema extrae el perfil a `informes/01_convocatoria/convocatoria_profile.md`.*
