# editor-en-espanol

Skill de Claude para corregir textos en español contra la norma de la RAE-ASALE.

Corrige ortotipografía, puntuación, acentuación, mayúsculas, concordancia, pronombres y
expresiones numéricas, resuelve qué va en cursiva y qué entre comillas, y señala los
calcos semánticos del inglés y las marcas de que un texto viene traducido.

## La regla que la gobierna

**No corrige lo que la norma ya admite.** Buena parte de las reglas del español no son
«mal o bien», sino «las dos valen» o «depende de la zona»: el *Libro de estilo* dice
«ambas son válidas» constantemente. Por eso cada regla lleva veredicto, y solo se aplica
sin preguntar lo que es error comprobable. Lo demás se propone.

| Veredicto | Qué hace |
|---|---|
| `ERROR` · `NO CONSTA` | Corrige sin preguntar |
| `EN PUGNA` · `AMBAS` · `DEPENDE` | No lo toca. Lo lista para que decidas |
| `ACEPTADO` · `REGLA` | No lo menciona. Está para que no lo señales por error |

## Instalación

Copia la carpeta en `~/.claude/skills/editor-en-espanol/`. Se invoca con
`/editor-en-espanol`, o sola cuando el contexto lo pide.

## Contenido

| Fichero | Qué lleva |
|---|---|
| `SKILL.md` | El procedimiento y **los 92 calcos con los dos artículos de diccionario enteros** — 792 acepciones. Van dentro, no en una referencia aparte: lo que el modelo tiene que decidir abrir no se abre |
| `references/norma-ortotipografia.md` | Acentuación, coma, comillas, raya, mayúsculas, cifras, espacios, diálogos |
| `references/norma-gramatica.md` | Concordancia, pronombres, verbo, relativos, grafías confundibles |
| `references/cursiva-y-comillas.md` | 56 casos: cursiva, «comillas», redonda o sin resalte |
| `src/` | Los datos verificados y los generadores. `build.py` reconstruye las dos skills, para que las copias no puedan divergir |
| `references/marcas-de-traduccion.md` | Marcas ortotipográficas y sintácticas de origen inglés |

## Edición para Wikipedia

Para prosa que va a un artículo de Wikipedia existe `wiki-editor-espanol`, dentro del
plugin [wiki-articles-claude](https://github.com/CasaAmarillaRoja/wiki-articles-claude).
Son las mismas reglas con el Manual de estilo de es.wiki por encima de la RAE donde
difieren, y protege el wikitext. Misma relación que hay entre `humanizer` y
`wiki-humanizer`.

## Fuentes

La norma se destila del *Libro de estilo de la lengua española*, la *Ortografía*, la
*Nueva gramática* y el *Diccionario panhispánico de dudas* (RAE-ASALE). Las acepciones
españolas se citan del *DLE* y las inglesas del *Cambridge Dictionary*, consultadas
entrada por entrada.
