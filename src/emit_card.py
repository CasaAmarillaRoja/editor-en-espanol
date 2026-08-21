# -*- coding: utf-8 -*-
import io, re, os
def datos(f, corte):
    src = io.open(f, encoding='utf-8').read(); src = src[:src.index(corte)]
    ns = {}; exec(compile(src, f, 'exec'), ns); return ns
def L(s):
    s = re.sub(r'<i>(.*?)</i>', r'*\1*', s); s = re.sub(r'<b>(.*?)</b>', r'**\1**', s)
    s = re.sub(r'<code>(.*?)</code>', r'`\1`', s); s = re.sub(r'<sup>(.*?)</sup>', r'^\1', s)
    return re.sub(r'<[^>]+>', '', s).strip()

man = datos('manual.py', '\nVER='); cur = datos('cursiva.py', '\nDEST=')
g2  = datos('gen2.py', '\nCHIP=')
o = []
o.append("""# PASADA OBLIGATORIA DE ESPAÑOL

Se inyecta solo cuando la traducción **produce español**. Si el resultado va a ser
inglés, esta sección no aparece.

**Léela entera antes de escribir la primera frase en español.** No es material de
consulta: es lo que hay que tener en la cabeza *mientras* se traduce, porque la mitad de
estos errores no producen duda. Un calco como `asumir` por *assume* se escribe con
plena confianza; si no lo tienes delante, no vas a ir a buscarlo.

## Cómo leer los veredictos

| Veredicto | Qué significa al traducir |
|---|---|
| `ERROR` · `NO CONSTA` | Infracción de la norma. No lo escribas |
| `EN PUGNA` · `AMBAS` · `DEPENDE` | Las dos formas valen. Elige una y **mantenla en todo el artículo** |
| `ACEPTADO` · `REGLA` | Correcto. **No lo «corrijas»** si aparece en el original o en tu borrador |

## Lo que no se puede fallar nunca

1. **Comillas angulares** « » como nivel exterior. Dentro, inglesas “ ”; en último lugar, simples ‘ ’. El Manual de estilo de es.wiki las prefiere.
2. **Títulos de sección en minúscula** salvo la inicial: `== Historia y desarrollo ==`, no `== Historia Y Desarrollo ==`. Lo exige el Manual de estilo de es.wiki.
3. **Títulos de obra**: solo la primera palabra y los nombres propios. *Cien años de soledad*, no *Cien Años De Soledad*.
4. **Raya de inciso pegada** al texto que encierra: `—así—`, no `— así —`.
5. **Intervalos con guion**, no con semirraya: `1998-2012`, no `1998–2012`.
6. **`billion` = mil millones**, no `billón`. Y `trillion` = billón. Error de dato, no de estilo.
7. **Millares con espacio fino** y solo en cantidades de más de cuatro cifras: `1 250 000`. Nunca coma ni punto. Los años, los artículos de ley y los códigos postales no se separan.
8. **Fechas**: `30 de octubre de 2020`, mes en minúscula. Nunca `Octubre 30, 2020`.
9. **Meses, días, gentilicios, idiomas y cargos en minúscula**: `lunes`, `enero`, `francés`, `inglés`, `el presidente`.
10. **Nada de gerundio de posterioridad**: no `Estudió en Santiago, yendo después a Bogotá`, sino `…y fue después a Bogotá`.
11. **El punto va fuera del cierre de comillas**: `Me dijo: «No te vayas».`
12. **El español elide el sujeto.** No encadenes `Él nació… Él estudió… Él publicó`.
""")

# --- calcos: lo más importante al traducir ---
NIV = {1:'NO CONSTA',2:'EN PUGNA',3:'ACEPTADO'}
o.append("\n## Falsos amigos: no los escribas sin comprobar\n")
o.append("Acepción inglesa en juego (Cambridge) frente a lo que el DLE recoge del español. "
         "Los recambios están cotejados contra los sinónimos que el DLE da para la palabra "
         "acusada, para que la cura no esté dentro de la enfermedad.\n")
for nombre, lista in (('Verbos', g2['V']), ('Adjetivos y adverbios', g2['A']), ('Sustantivos', g2['S'])):
    o.append('\n### %s\n' % nombre)
    o.append('| No escribas | Cuando el inglés dice | Escribe | Nivel |')
    o.append('|---|---|---|---|')
    for esd, end, esk, enk, men, mes, fix, lvl, nota in lista:
        if lvl == 3:
            o.append('| — | *%s* | `%s` **es correcto** | ACEPTADO |' % (L(end), L(esd)))
        else:
            o.append('| `%s` | *%s* — %s | %s | %s |' % (
                L(esd), L(end), L(men), L(fix), NIV[lvl]))

# --- cursiva o comillas ---
D = {'cursiva':'*cursiva*','comillas':'«comillas»','redonda':'redonda',
     'simples':'‘simples’','nunca':'sin resalte'}
o.append("\n## Cursiva, comillas o redonda\n")
o.append("**Regla madre:** la obra completa en *cursiva*; la pieza que vive dentro de otra "
         "obra entre «comillas». **Corolario:** si la mayúscula ya delimita el título, la "
         "cursiva sobra — *el Código Civil*, *la Biblia* van en redonda.\n")
o.append('| Qué es | Va en |')
o.append('|---|---|')
for titulo, filas in cur['G']:
    for cosa, dest, ej, nota, der in filas:
        o.append('| %s | %s — %s |' % (L(cosa), D[dest], L(ej)))

# --- norma: todo, ordenado ---
VERD = {'error':'ERROR','ambas':'AMBAS','depende':'DEPENDE','bien':'REGLA'}
MARCA = {'mal':'mal','bien':'bien','ambas':'vale'}
o.append("\n## Norma: ortotipografía, puntuación y gramática\n")
for sid, titulo, intro, reglas in man['S']:
    if sid == 'uso': continue
    o.append('\n### %s\n' % titulo)
    for t, ver, ejs, nota in reglas:
        ej = ' · '.join('%s: %s' % (MARCA[m], L(e)) for m, e in ejs)
        linea = '- **%s** `%s` — %s' % (L(t), VERD[ver], ej)
        if nota: linea += '  \n  %s' % L(nota)
        o.append(linea)

card = '\n'.join(o) + '\n'
dst = os.path.expanduser('~/claude-workspace/wiki-articles-claude/skills/wikipedia-translation/references/ES-CARD.md')
io.open(dst, 'w', encoding='utf-8').write(card)
print('ES-CARD.md: %d caracteres (%.1f KB)' % (len(card), len(card)/1024))
print('comparación: el RULES-CARD actual mide %d' % len(io.open(os.path.expanduser(
  '~/claude-workspace/wiki-articles-claude/skills/wikipedia-translation/references/RULES-CARD.md'),
  encoding='utf-8').read()))
