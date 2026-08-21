# -*- coding: utf-8 -*-
"""Construye las dos skills. No hay capa opcional: los calcos van dentro de lo que
el modelo lee obligatoriamente — el SKILL.md en la suelta, la tarjeta inyectada en
la del plugin. Un fichero de referencia que el modelo decide abrir nunca se abre;
el propio hook del plugin existe por haberlo comprobado.
"""
import io, json, os, re

A = os.path.dirname(os.path.abspath(__file__))
R = lambda n: os.path.join(A, n)
H = os.path.expanduser('~')
SKILL  = os.path.join(H, '.claude/skills/editor-en-espanol')
PLUGIN = os.path.join(H, 'claude-workspace/wiki-articles-claude/skills/wiki-editor-espanol')

ES = json.load(io.open(R('es_full.json'), encoding='utf-8'))
EN = json.load(io.open(R('en_full.json'), encoding='utf-8'))
def datos(f, corte):
    s = io.open(R(f), encoding='utf-8').read()[:None]
    s = s[:s.index(corte)]; ns = {}; exec(compile(s, f, 'exec'), ns); return ns
G = datos('gen2.py', '\nCHIP=')
N = len(G['V']) + len(G['A']) + len(G['S'])
NES = sum(len(v) for v in ES.values())
NEN = sum(len(v) for v in EN.values())
def L(s):
    s = re.sub(r'<i>(.*?)</i>', r'*\1*', s); s = re.sub(r'<b>(.*?)</b>', r'**\1**', s)
    s = re.sub(r'<code>(.*?)</code>', r'`\1`', s)
    return re.sub(r'<[^>]+>', '', s).strip()

NIV = {1: 'NO CONSTA', 2: 'EN PUGNA', 3: 'ACEPTADO'}

def calcos(nivel_titulo='##'):
    """Los pares con los dos artículos enteros. Devuelve markdown embebible."""
    o = [f"""{nivel_titulo} Los {N} calcos, con los dos artículos completos

Son {N} pares. Cada uno lleva **el artículo entero de los dos diccionarios** — Cambridge para el
inglés, DLE para el español — y la acepción en juego marcada con `←`.

Van completos porque el resumen miente por omisión. Casi todas estas palabras son
polisémicas y **parte de su campo inglés sí existe en español**: *dramatic* tiene tres
sentidos y el español cubre dos. Con solo la acepción acusada delante, un uso legítimo
como «asumió el cargo» —acepción 2 del DLE— se marca como calco. Y señalar un uso
legítimo hace más daño que dejar pasar el calco.

| Nivel | Qué haces |
|---|---|
| `NO CONSTA` | El DLE no recoge esa acepción. Corriges |
| `EN PUGNA` | La recoge restringida a un campo o región, o el DPD la censura. Delata por frecuencia, no por error: lo propones |
| `ACEPTADO` | Recogida sin reservas. **No lo señalas nunca** |

Los recambios están cotejados contra la lista de sinónimos que el DLE publica para la
palabra acusada, para que la cura no esté dentro de la enfermedad.
"""]
    sub = nivel_titulo + '#'
    for nombre, lista in (('Verbos', G['V']), ('Adjetivos y adverbios', G['A']),
                          ('Sustantivos', G['S'])):
        o.append('\n%s %s\n' % (sub, nombre))
        for esd, end, esk, enk, men, mes, fix, lvl, nota in lista:
            o.append('%s# `%s` ← *%s* — %s\n' % (sub, L(esd), L(end), NIV[lvl]))
            ing = EN.get(enk, [])
            o.append('*%s* en Cambridge (%d):' % (L(enk), len(ing)))
            for s in ing:
                o.append('- %s%s' % (s, ' ←' if men and men.lower() in s.lower() else ''))
            esp = ES.get(esk, [])
            cab = '\n*%s* en el DLE (%d)' % (L(esk), len(esp))
            o.append(cab + (':' if mes else ' · **ninguna recoge el sentido inglés**:'))
            for s in esp:
                o.append('- %s%s' % (s, ' ←' if mes and mes.lower() in s.lower() else ''))
            o.append('\n**Escribe:** %s' % ('no hace falta cambiar nada' if fix == '—' else L(fix)))
            if nota: o.append('**Nota:** %s' % L(nota))
            o.append('')
    return '\n'.join(o)

# ---------- 1. SKILL.md de la suelta: calcos dentro ----------
f = os.path.join(SKILL, 'SKILL.md'); s = io.open(f, encoding='utf-8').read()
s = re.sub(r'\n## Los \d+ calcos.*?(?=\n## Referencias)', '', s, flags=re.S)
marca = '\n## Referencias'
assert marca in s
s = s.replace(marca, '\n' + calcos('##') + marca)
# la tabla de referencias ya no menciona ficheros de calcos
s = re.sub(r'\n\| `references/calcos[^\n]*\|', '', s)
s = re.sub(r'\n{3,}', '\n\n', s)
io.open(f, 'w', encoding='utf-8').write(s)
print('SKILL.md (suelta)      %6.1f KB' % (len(s)/1024))

# ---------- 2. ES-CARD.md del plugin: calcos completos, no la tabla ----------
f = os.path.join(PLUGIN, 'ES-CARD.md'); s = io.open(f, encoding='utf-8').read()
# idempotente: casa la cabecera original y la ya generada
m = re.search(r'\n## (?:Falsos amigos|Los \d+ calcos)', s)
assert m, 'no encuentro la sección de calcos en ES-CARD.md'
ini, fin = m.start(), s.index('\n## Cursiva, comillas o redonda')
s = s[:ini] + '\n' + calcos('##') + s[fin:]
s = re.sub(r'\n{3,}', '\n\n', s)
io.open(f, 'w', encoding='utf-8').write(s)
print('ES-CARD.md (plugin)    %6.1f KB' % (len(s)/1024))

# ---------- 3. fuera la basura resumida ----------
for p in (os.path.join(SKILL, 'references/calcos-del-ingles.md'),
          os.path.join(SKILL, 'references/calcos-completos.md'),
          os.path.join(PLUGIN, 'calcos-completos.md')):
    if os.path.exists(p): os.remove(p); print('borrado  %s' % p.replace(H, '~'))

# ---------- 4. los conteos citados a mano, derivados ----------
def contar(ruta, sust):
    p = os.path.join(*ruta); t = io.open(p, encoding='utf-8').read(); o = t
    for pat, rep in sust:
        t = re.sub(pat, rep, t)
    if t != o:
        io.open(p, 'w', encoding='utf-8').write(t); print('conteos  %s' % p.replace(H, '~'))

nums = [(r'\b\d+ calcos\b', '%d calcos' % N),
        (r'\bLos \d+ calcos\b', 'Los %d calcos' % N),
        (r'\blos \d+ calcos\b', 'los %d calcos' % N),
        (r'\blos \d+ falsos amigos\b', 'los %d falsos amigos' % N),
        (r'\b\d+ pares\b', '%d pares' % N),
        (r'\b\d+ acepciones en total\b', '%d acepciones en total' % (NES + NEN)),
        (r'\b\d+ acepciones del DLE\b', '%d acepciones del DLE' % NES),
        (r'\b\d+ acepciones de Cambridge\b', '%d acepciones de Cambridge' % NEN),
        (r'\b\d+ del DLE y \d+ de Cambridge\b', '%d del DLE y %d de Cambridge' % (NES, NEN)),
        (r'\b\d+ acepciones\b(?=\.)', '%d acepciones' % (NES + NEN))]
for ruta in ((SKILL, 'SKILL.md'), (SKILL, 'README.md'),
             (PLUGIN, 'SKILL.md'), (PLUGIN, 'ES-CARD.md')):
    contar(ruta, nums)
print('\ntotales: %d pares · %d acepciones DLE · %d Cambridge' % (N, NES, NEN))
