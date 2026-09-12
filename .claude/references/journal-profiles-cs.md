# Perfiles de Revistas — Ciencias Sociales (CS)

> Perfiles precargados para uso con `/redactar perfil` y `/redactar adaptar`. Cada campo marcado como `[ASUMIDO]` se basa en convención del campo; `[EXTRAIDO]` indica dato obtenido directamente de las normas editoriales; `[VERIFICAR]` requiere confirmación del usuario.

---

## res — Revista de Estudios Sociales (Uniandes, Colombia)

```yaml
journal_key: res
nombre_completo: "Revista de Estudios Sociales"
editorial: "Universidad de los Andes, Colombia"
url_guidelines: "https://revistas.uniandes.edu.co/journal/res/information/authors"
fecha_extraccion: "2026-04-16"
fuente_extraccion: "precargado"
estado_perfil: "borrador"

area_disciplinar: "Ciencias Sociales, Humanidades"
paradigmas_aceptados: [cualitativo, cuantitativo, mixto, teorico, ensayo]
enfoque_regional: "latinoamericano / global"
revision_por_pares: "doble_ciego"

idioma_primario: "es"
idioma_secundario: "en"
longitud_maxima_palabras: 8000  # [ASUMIDO]
longitud_abstract_palabras: 150
tipo_abstract: "narrativo"
estructura_abstract: []
palabras_clave_cantidad: [5, 7]  # [ASUMIDO]
palabras_clave_fuente: "libres"

estilo_citacion: "Chicago-AuthorDate"  # [ASUMIDO]
usa_biblatex_biber: true
formato_referencias_en_texto: "(Autor año)"

secciones_obligatorias: [Introducción, Desarrollo, Conclusiones, Referencias]
secciones_opcionales: [Agradecimientos]
titulo_estandar_metodo: "Metodología"

declaracion_conflicto_intereses: true
declaracion_etica: true  # [ASUMIDO]
declaracion_disponibilidad_datos: false  # [ASUMIDO]
declaracion_consentimiento_informado: true
declaracion_credit_autores: false
declaracion_financiamiento: true
declaracion_agradecimientos: true
uso_de_ia_generativa: null  # [VERIFICAR]

formato_tablas: "inline"
formato_figuras: "inline"
resolucion_minima_figuras_dpi: 300  # [ASUMIDO]
formato_archivos_figuras: [pdf, png, tiff]

formato_archivo_final: "docx"  # [ASUMIDO]
plantilla_latex_url: ""
plantilla_word_url: ""  # [VERIFICAR]
sistema_envio: "OJS"
tiempo_respuesta_tipico_semanas: 12  # [ASUMIDO]
tasa_aceptacion_estimada: null
indexacion: [Scopus, WoS-ESCI, Redalyc, Scielo, Latindex]

permite_preprint: true  # [ASUMIDO]
politica_open_access: "gold"
embargo_meses: 0

notas_investigador: ""
```

---

## rcs — Revista Colombiana de Sociología (UNAL)

```yaml
journal_key: rcs
nombre_completo: "Revista Colombiana de Sociología"
editorial: "Universidad Nacional de Colombia"
url_guidelines: "https://revistas.unal.edu.co/index.php/recs/about/submissions"
fecha_extraccion: "2026-04-16"
fuente_extraccion: "precargado"
estado_perfil: "borrador"

area_disciplinar: "Sociología"
paradigmas_aceptados: [cualitativo, cuantitativo, mixto, teorico, ensayo]
enfoque_regional: "colombiano / latinoamericano"
revision_por_pares: "doble_ciego"

idioma_primario: "es"
idioma_secundario: "en"
longitud_maxima_palabras: 9000  # [ASUMIDO]
longitud_abstract_palabras: 200
tipo_abstract: "narrativo"
estructura_abstract: []
palabras_clave_cantidad: [4, 6]
palabras_clave_fuente: "libres"

estilo_citacion: "APA7"  # [ASUMIDO]
usa_biblatex_biber: true
formato_referencias_en_texto: "(Autor, año, p. X)"

secciones_obligatorias: [Introducción, Metodología, Resultados, Conclusiones, Referencias]
secciones_opcionales: [Agradecimientos, Anexos]
titulo_estandar_metodo: "Metodología"

declaracion_conflicto_intereses: true
declaracion_etica: true
declaracion_disponibilidad_datos: false
declaracion_consentimiento_informado: true
declaracion_credit_autores: false
declaracion_financiamiento: true
declaracion_agradecimientos: true
uso_de_ia_generativa: null  # [VERIFICAR]

formato_tablas: "inline"
formato_figuras: "inline"
resolucion_minima_figuras_dpi: 300
formato_archivos_figuras: [pdf, png]

formato_archivo_final: "docx"
plantilla_latex_url: ""
plantilla_word_url: ""  # [VERIFICAR]
sistema_envio: "OJS"
tiempo_respuesta_tipico_semanas: 16  # [ASUMIDO]
tasa_aceptacion_estimada: null
indexacion: [Scielo, Redalyc, Latindex, DOAJ]

permite_preprint: true
politica_open_access: "gold"
embargo_meses: 0

notas_investigador: ""
```

---

## ap — Análisis Político (IEPRI-UNAL)

```yaml
journal_key: ap
nombre_completo: "Análisis Político"
editorial: "Instituto de Estudios Políticos y Relaciones Internacionales (IEPRI), Universidad Nacional de Colombia"
url_guidelines: "https://revistas.unal.edu.co/index.php/anpol/about/submissions"
fecha_extraccion: "2026-04-16"
fuente_extraccion: "precargado"
estado_perfil: "borrador"

area_disciplinar: "Ciencia Política, Relaciones Internacionales"
paradigmas_aceptados: [cualitativo, cuantitativo, mixto, teorico, ensayo]
enfoque_regional: "colombiano / latinoamericano"
revision_por_pares: "doble_ciego"

idioma_primario: "es"
idioma_secundario: "en"
longitud_maxima_palabras: 9000  # [ASUMIDO]
longitud_abstract_palabras: 200
tipo_abstract: "narrativo"
estructura_abstract: []
palabras_clave_cantidad: [4, 6]
palabras_clave_fuente: "libres"

estilo_citacion: "Chicago-AuthorDate"  # [ASUMIDO]
usa_biblatex_biber: true
formato_referencias_en_texto: "(Autor año)"

secciones_obligatorias: [Introducción, Desarrollo, Conclusiones, Referencias]
secciones_opcionales: []
titulo_estandar_metodo: "Metodología"  # [ASUMIDO]

declaracion_conflicto_intereses: true
declaracion_etica: false  # [ASUMIDO — énfasis político, no necesariamente IRB]
declaracion_disponibilidad_datos: false
declaracion_consentimiento_informado: false
declaracion_credit_autores: false
declaracion_financiamiento: true
declaracion_agradecimientos: true
uso_de_ia_generativa: null

formato_tablas: "inline"
formato_figuras: "inline"
resolucion_minima_figuras_dpi: 300
formato_archivos_figuras: [pdf, png]

formato_archivo_final: "docx"
plantilla_latex_url: ""
plantilla_word_url: ""
sistema_envio: "OJS"
tiempo_respuesta_tipico_semanas: 12
tasa_aceptacion_estimada: null
indexacion: [Scielo, Redalyc, Latindex]

permite_preprint: true
politica_open_access: "gold"
embargo_meses: 0

notas_investigador: ""
```

---

## rcs-icesi — Revista CS (Icesi)

```yaml
journal_key: rcs-icesi
nombre_completo: "Revista CS"
editorial: "Universidad Icesi, Cali, Colombia"
url_guidelines: "https://www.icesi.edu.co/revistas/index.php/revista_cs/about/submissions"
fecha_extraccion: "2026-04-16"
fuente_extraccion: "precargado"
estado_perfil: "borrador"

area_disciplinar: "Ciencias Sociales"
paradigmas_aceptados: [cualitativo, cuantitativo, mixto, teorico, ensayo]
enfoque_regional: "latinoamericano / colombiano"
revision_por_pares: "doble_ciego"

idioma_primario: "es"
idioma_secundario: "en"
longitud_maxima_palabras: 10000  # [ASUMIDO]
longitud_abstract_palabras: 200
tipo_abstract: "narrativo"
estructura_abstract: []
palabras_clave_cantidad: [4, 7]
palabras_clave_fuente: "libres"

estilo_citacion: "APA7"
usa_biblatex_biber: true
formato_referencias_en_texto: "(Autor, año)"

secciones_obligatorias: [Introducción, Metodología, Resultados, Discusión, Conclusiones, Referencias]
secciones_opcionales: [Agradecimientos]
titulo_estandar_metodo: "Metodología"

declaracion_conflicto_intereses: true
declaracion_etica: true
declaracion_disponibilidad_datos: false
declaracion_consentimiento_informado: true
declaracion_credit_autores: false
declaracion_financiamiento: true
declaracion_agradecimientos: true
uso_de_ia_generativa: null

formato_tablas: "inline"
formato_figuras: "inline"
resolucion_minima_figuras_dpi: 300
formato_archivos_figuras: [pdf, png, jpg]

formato_archivo_final: "docx"
plantilla_latex_url: ""
plantilla_word_url: ""
sistema_envio: "OJS"
tiempo_respuesta_tipico_semanas: 16
tasa_aceptacion_estimada: null
indexacion: [Scielo, Redalyc, Latindex, DOAJ]

permite_preprint: true
politica_open_access: "gold"
embargo_meses: 0

notas_investigador: ""
```

---

## uh — Universitas Humanística (Javeriana)

```yaml
journal_key: uh
nombre_completo: "Universitas Humanística"
editorial: "Pontificia Universidad Javeriana, Bogotá"
url_guidelines: "https://revistas.javeriana.edu.co/index.php/univhumanistica/about/submissions"
fecha_extraccion: "2026-04-16"
fuente_extraccion: "precargado"
estado_perfil: "borrador"

area_disciplinar: "Ciencias Humanas y Sociales, Filosofía, Antropología"
paradigmas_aceptados: [cualitativo, teorico, ensayo, historico-hermeneutico]
enfoque_regional: "latinoamericano / colombiano"
revision_por_pares: "doble_ciego"

idioma_primario: "es"
idioma_secundario: "en"
longitud_maxima_palabras: 8000  # [ASUMIDO]
longitud_abstract_palabras: 200
tipo_abstract: "narrativo"
estructura_abstract: []
palabras_clave_cantidad: [4, 6]
palabras_clave_fuente: "libres"

estilo_citacion: "Chicago-AuthorDate"  # [ASUMIDO]
usa_biblatex_biber: true
formato_referencias_en_texto: "(Autor año)"

secciones_obligatorias: [Introducción, Desarrollo, Conclusiones, Referencias]
secciones_opcionales: []
titulo_estandar_metodo: ""  # no siempre aplica para ensayos

declaracion_conflicto_intereses: false
declaracion_etica: false
declaracion_disponibilidad_datos: false
declaracion_consentimiento_informado: false
declaracion_credit_autores: false
declaracion_financiamiento: true
declaracion_agradecimientos: true
uso_de_ia_generativa: null

formato_tablas: "inline"
formato_figuras: "inline"
resolucion_minima_figuras_dpi: 300
formato_archivos_figuras: [pdf, png]

formato_archivo_final: "docx"
plantilla_latex_url: ""
plantilla_word_url: ""
sistema_envio: "OJS"
tiempo_respuesta_tipico_semanas: 16
tasa_aceptacion_estimada: null
indexacion: [Scielo, Redalyc, Latindex]

permite_preprint: true
politica_open_access: "gold"
embargo_meses: 0

notas_investigador: ""
```

---

## reis — Revista Española de Investigaciones Sociológicas

```yaml
journal_key: reis
nombre_completo: "Revista Española de Investigaciones Sociológicas"
editorial: "Centro de Investigaciones Sociológicas (CIS), España"
url_guidelines: "http://www.reis.cis.es/REIS/html/es/autores/normas.html"
fecha_extraccion: "2026-04-16"
fuente_extraccion: "precargado"
estado_perfil: "borrador"

area_disciplinar: "Sociología"
paradigmas_aceptados: [cuantitativo, cualitativo, mixto, teorico]
enfoque_regional: "ibérico / europeo"
revision_por_pares: "doble_ciego"

idioma_primario: "es"
idioma_secundario: "en"
longitud_maxima_palabras: 8000
longitud_abstract_palabras: 150
tipo_abstract: "narrativo"
estructura_abstract: []
palabras_clave_cantidad: [4, 6]
palabras_clave_fuente: "libres"

estilo_citacion: "APA7"  # [ASUMIDO — ver normas actualizadas]
usa_biblatex_biber: true
formato_referencias_en_texto: "(Autor, año)"

secciones_obligatorias: [Introducción, Metodología, Resultados, Conclusiones, Referencias]
secciones_opcionales: [Agradecimientos, Notas]
titulo_estandar_metodo: "Metodología"

declaracion_conflicto_intereses: true
declaracion_etica: true
declaracion_disponibilidad_datos: false
declaracion_consentimiento_informado: false
declaracion_credit_autores: false
declaracion_financiamiento: true
declaracion_agradecimientos: true
uso_de_ia_generativa: null

formato_tablas: "inline"
formato_figuras: "inline"
resolucion_minima_figuras_dpi: 300
formato_archivos_figuras: [pdf, png, tiff]

formato_archivo_final: "docx"
plantilla_latex_url: ""
plantilla_word_url: ""
sistema_envio: "OJS"
tiempo_respuesta_tipico_semanas: 16
tasa_aceptacion_estimada: null
indexacion: [Scopus, WoS-ESCI, Scielo, Latindex]

permite_preprint: false  # [ASUMIDO]
politica_open_access: "hybrid"
embargo_meses: 12

notas_investigador: ""
```

---

## asr — American Sociological Review

```yaml
journal_key: asr
nombre_completo: "American Sociological Review"
editorial: "SAGE / American Sociological Association"
url_guidelines: "https://journals.sagepub.com/author-instructions/ASR"
fecha_extraccion: "2026-04-16"
fuente_extraccion: "precargado"
estado_perfil: "borrador"

area_disciplinar: "Sociología"
paradigmas_aceptados: [cuantitativo, cualitativo, mixto, teorico]
enfoque_regional: "global"
revision_por_pares: "doble_ciego"

idioma_primario: "en"
idioma_secundario: ""
longitud_maxima_palabras: 12000
longitud_abstract_palabras: 150
tipo_abstract: "narrativo"
estructura_abstract: []
palabras_clave_cantidad: [3, 6]
palabras_clave_fuente: "libres"

estilo_citacion: "ASA"  # American Sociological Association style
usa_biblatex_biber: false  # preferible .bst ASA
formato_referencias_en_texto: "(Autor año)"

secciones_obligatorias: [Introduction, Methods, Results, Discussion, Conclusion, References]
secciones_opcionales: [Acknowledgments, Appendix]
titulo_estandar_metodo: "Data and Methods"

declaracion_conflicto_intereses: true
declaracion_etica: true
declaracion_disponibilidad_datos: true
declaracion_consentimiento_informado: true
declaracion_credit_autores: false
declaracion_financiamiento: true
declaracion_agradecimientos: true
uso_de_ia_generativa: true  # [ASUMIDO — política 2024+]

formato_tablas: "separado_al_final"
formato_figuras: "archivo_aparte"
resolucion_minima_figuras_dpi: 300
formato_archivos_figuras: [tiff, eps, pdf]

formato_archivo_final: "docx"
plantilla_latex_url: ""
plantilla_word_url: ""
sistema_envio: "Scholar One"
tiempo_respuesta_tipico_semanas: 8
tasa_aceptacion_estimada: 0.05
indexacion: [Scopus, WoS-Q1, JSTOR]

permite_preprint: true
politica_open_access: "hybrid"
embargo_meses: 12

notas_investigador: "Impacto muy alto. Alta exigencia metodológica. Preferred: manuscripts that make clear theoretical and empirical contributions."
```

---

## qi — Qualitative Inquiry (SAGE)

```yaml
journal_key: qi
nombre_completo: "Qualitative Inquiry"
editorial: "SAGE Publications"
url_guidelines: "https://journals.sagepub.com/author-instructions/QIX"
fecha_extraccion: "2026-04-16"
fuente_extraccion: "precargado"
estado_perfil: "borrador"

area_disciplinar: "Metodología Cualitativa, Ciencias Sociales"
paradigmas_aceptados: [cualitativo, teorico, ensayo, autoetnografico]
enfoque_regional: "global"
revision_por_pares: "doble_ciego"

idioma_primario: "en"
idioma_secundario: ""
longitud_maxima_palabras: 8000  # [ASUMIDO]
longitud_abstract_palabras: 150
tipo_abstract: "narrativo"
estructura_abstract: []
palabras_clave_cantidad: [5, 7]
palabras_clave_fuente: "libres"

estilo_citacion: "APA7"
usa_biblatex_biber: true
formato_referencias_en_texto: "(Autor, año)"

secciones_obligatorias: [Introduction, Methodology, Analysis, Discussion, Conclusion, References]
secciones_opcionales: []
titulo_estandar_metodo: "Methodology"

declaracion_conflicto_intereses: true
declaracion_etica: true
declaracion_disponibilidad_datos: false
declaracion_consentimiento_informado: true
declaracion_credit_autores: false
declaracion_financiamiento: true
declaracion_agradecimientos: true
uso_de_ia_generativa: true  # [ASUMIDO]

formato_tablas: "inline"
formato_figuras: "inline"
resolucion_minima_figuras_dpi: 300
formato_archivos_figuras: [pdf, tiff, png]

formato_archivo_final: "docx"
plantilla_latex_url: ""
plantilla_word_url: ""
sistema_envio: "Scholar One"
tiempo_respuesta_tipico_semanas: 12
tasa_aceptacion_estimada: null
indexacion: [Scopus, WoS-ESCI]

permite_preprint: true
politica_open_access: "hybrid"
embargo_meses: 12

notas_investigador: "Acepta ensayos experimentales, poesía investigativa, autoetnografía. Alta apertura a formas no convencionales."
```

---

## qr — Qualitative Research (SAGE)

```yaml
journal_key: qr
nombre_completo: "Qualitative Research"
editorial: "SAGE Publications"
url_guidelines: "https://journals.sagepub.com/author-instructions/QRJ"
fecha_extraccion: "2026-04-16"
fuente_extraccion: "precargado"
estado_perfil: "borrador"

area_disciplinar: "Metodología Cualitativa"
paradigmas_aceptados: [cualitativo, mixto, teorico]
enfoque_regional: "global"
revision_por_pares: "doble_ciego"

idioma_primario: "en"
idioma_secundario: ""
longitud_maxima_palabras: 9000  # [ASUMIDO]
longitud_abstract_palabras: 200
tipo_abstract: "narrativo"
estructura_abstract: []
palabras_clave_cantidad: [5, 7]
palabras_clave_fuente: "libres"

estilo_citacion: "APA7"
usa_biblatex_biber: true
formato_referencias_en_texto: "(Autor, año)"

secciones_obligatorias: [Introduction, Methods, Analysis, Discussion, Conclusion, References]
secciones_opcionales: []
titulo_estandar_metodo: "Methods"

declaracion_conflicto_intereses: true
declaracion_etica: true
declaracion_disponibilidad_datos: false
declaracion_consentimiento_informado: true
declaracion_credit_autores: false
declaracion_financiamiento: true
declaracion_agradecimientos: true
uso_de_ia_generativa: true

formato_tablas: "inline"
formato_figuras: "inline"
resolucion_minima_figuras_dpi: 300
formato_archivos_figuras: [pdf, tiff]

formato_archivo_final: "docx"
plantilla_latex_url: ""
plantilla_word_url: ""
sistema_envio: "Scholar One"
tiempo_respuesta_tipico_semanas: 10
tasa_aceptacion_estimada: null
indexacion: [Scopus, WoS-Q1]

permite_preprint: true
politica_open_access: "hybrid"
embargo_meses: 12

notas_investigador: "Más metodológico que QI; exige reflexión explícita sobre epistemología y rigor."
```

---

## larr — Latin American Research Review

```yaml
journal_key: larr
nombre_completo: "Latin American Research Review"
editorial: "Latin American Studies Association (LASA) / Cambridge University Press"
url_guidelines: "https://larr.lasa.international/submit"
fecha_extraccion: "2026-04-16"
fuente_extraccion: "precargado"
estado_perfil: "borrador"

area_disciplinar: "Estudios Latinoamericanos interdisciplinarios"
paradigmas_aceptados: [cualitativo, cuantitativo, mixto, historico-hermeneutico, teorico]
enfoque_regional: "latinoamericano"
revision_por_pares: "doble_ciego"

idioma_primario: "en"
idioma_secundario: "es"
longitud_maxima_palabras: 10000
longitud_abstract_palabras: 200
tipo_abstract: "narrativo"
estructura_abstract: []
palabras_clave_cantidad: [5, 7]
palabras_clave_fuente: "libres"

estilo_citacion: "Chicago-AuthorDate"
usa_biblatex_biber: true
formato_referencias_en_texto: "(Autor año)"

secciones_obligatorias: [Introduction, Methods, Analysis, Conclusion, References]
secciones_opcionales: [Acknowledgments]
titulo_estandar_metodo: "Data and Methods"

declaracion_conflicto_intereses: true
declaracion_etica: true
declaracion_disponibilidad_datos: true
declaracion_consentimiento_informado: false
declaracion_credit_autores: false
declaracion_financiamiento: true
declaracion_agradecimientos: true
uso_de_ia_generativa: null

formato_tablas: "inline"
formato_figuras: "inline"
resolucion_minima_figuras_dpi: 300
formato_archivos_figuras: [pdf, tiff, png]

formato_archivo_final: "docx"
plantilla_latex_url: ""
plantilla_word_url: ""
sistema_envio: "Editorial Manager"
tiempo_respuesta_tipico_semanas: 12
tasa_aceptacion_estimada: null
indexacion: [Scopus, WoS-SSCI, Redalyc]

permite_preprint: true
politica_open_access: "gold"
embargo_meses: 0

notas_investigador: "Acepta también artículos en español. Revista clave para investigación latinoamericana con alcance internacional."
```

---

## rms — Revista Mexicana de Sociología (IIS-UNAM)

```yaml
journal_key: rms
nombre_completo: "Revista Mexicana de Sociología"
editorial: "Instituto de Investigaciones Sociales, UNAM"
url_guidelines: "http://www.sociologica.unam.mx/normas"
fecha_extraccion: "2026-04-16"
fuente_extraccion: "precargado"
estado_perfil: "borrador"

area_disciplinar: "Sociología"
paradigmas_aceptados: [cualitativo, cuantitativo, mixto, teorico]
enfoque_regional: "mexicano / latinoamericano"
revision_por_pares: "doble_ciego"

idioma_primario: "es"
idioma_secundario: "en"
longitud_maxima_palabras: 9000  # [ASUMIDO]
longitud_abstract_palabras: 150
tipo_abstract: "narrativo"
estructura_abstract: []
palabras_clave_cantidad: [4, 6]
palabras_clave_fuente: "libres"

estilo_citacion: "Chicago-AuthorDate"
usa_biblatex_biber: true
formato_referencias_en_texto: "(Autor año)"

secciones_obligatorias: [Introducción, Metodología, Análisis, Conclusiones, Referencias]
secciones_opcionales: []
titulo_estandar_metodo: "Metodología"

declaracion_conflicto_intereses: false
declaracion_etica: false
declaracion_disponibilidad_datos: false
declaracion_consentimiento_informado: false
declaracion_credit_autores: false
declaracion_financiamiento: true
declaracion_agradecimientos: true
uso_de_ia_generativa: null

formato_tablas: "inline"
formato_figuras: "inline"
resolucion_minima_figuras_dpi: 300
formato_archivos_figuras: [pdf, png]

formato_archivo_final: "docx"
plantilla_latex_url: ""
plantilla_word_url: ""
sistema_envio: "OJS"
tiempo_respuesta_tipico_semanas: 20  # [ASUMIDO]
tasa_aceptacion_estimada: null
indexacion: [Scopus, WoS-ESCI, Scielo, Redalyc]

permite_preprint: true
politica_open_access: "gold"
embargo_meses: 0

notas_investigador: ""
```

---

## iconos — Íconos (FLACSO Ecuador)

```yaml
journal_key: iconos
nombre_completo: "Íconos — Revista de Ciencias Sociales"
editorial: "FLACSO Ecuador"
url_guidelines: "https://revistas.flacsoandes.edu.ec/iconos/about/submissions"
fecha_extraccion: "2026-04-16"
fuente_extraccion: "precargado"
estado_perfil: "borrador"

area_disciplinar: "Ciencias Sociales"
paradigmas_aceptados: [cualitativo, cuantitativo, mixto, critico-social, teorico]
enfoque_regional: "latinoamericano / andino"
revision_por_pares: "doble_ciego"

idioma_primario: "es"
idioma_secundario: "en"
longitud_maxima_palabras: 8000
longitud_abstract_palabras: 200
tipo_abstract: "narrativo"
estructura_abstract: []
palabras_clave_cantidad: [4, 6]
palabras_clave_fuente: "libres"

estilo_citacion: "APA7"
usa_biblatex_biber: true
formato_referencias_en_texto: "(Autor, año)"

secciones_obligatorias: [Introducción, Metodología, Análisis, Conclusiones, Referencias]
secciones_opcionales: []
titulo_estandar_metodo: "Metodología"

declaracion_conflicto_intereses: true
declaracion_etica: true
declaracion_disponibilidad_datos: false
declaracion_consentimiento_informado: true
declaracion_credit_autores: false
declaracion_financiamiento: true
declaracion_agradecimientos: true
uso_de_ia_generativa: null

formato_tablas: "inline"
formato_figuras: "inline"
resolucion_minima_figuras_dpi: 300
formato_archivos_figuras: [pdf, png]

formato_archivo_final: "docx"
plantilla_latex_url: ""
plantilla_word_url: ""
sistema_envio: "OJS"
tiempo_respuesta_tipico_semanas: 16
tasa_aceptacion_estimada: null
indexacion: [Scopus, WoS-ESCI, Scielo, Redalyc, Latindex]

permite_preprint: true
politica_open_access: "gold"
embargo_meses: 0

notas_investigador: "Temáticas crítico-sociales, poder, movimientos sociales. Muy relevante para investigación andino-latinoamericana."
```

---

## Índice de Claves

| Clave | Nombre | País/Región | Área |
|---|---|---|---|
| `res` | Revista de Estudios Sociales | Colombia | CC.SS. generales |
| `rcs` | Revista Colombiana de Sociología | Colombia | Sociología |
| `ap` | Análisis Político | Colombia | Ciencia Política |
| `rcs-icesi` | Revista CS | Colombia | CC.SS. generales |
| `uh` | Universitas Humanística | Colombia | Humanidades |
| `reis` | REIS | España | Sociología |
| `asr` | American Sociological Review | Global | Sociología (top) |
| `qi` | Qualitative Inquiry | Global | Metodología cuali |
| `qr` | Qualitative Research | Global | Metodología cuali |
| `larr` | Latin American Research Review | Latinoamérica | Interdisciplinar |
| `rms` | Revista Mexicana de Sociología | México | Sociología |
| `iconos` | Íconos FLACSO | Ecuador / Latinoam. | CC.SS. críticas |

*Para añadir un perfil nuevo: ejecutar `/redactar perfil [fuente]` y el sistema creará el archivo en `informes/07_redaccion/journal_profiles/[key].md`.*
