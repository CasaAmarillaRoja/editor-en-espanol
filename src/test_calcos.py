# -*- coding: utf-8 -*-
"""Integridad de los calcos. Lo que busca son degradaciones silenciosas:
un marcador de acepción que no casa no rompe nada, simplemente deja de marcar,
y la entrada pierde justo lo que la hace verificable."""
import io, json, os, re, sys

A = os.path.dirname(os.path.abspath(__file__)); R = lambda n: os.path.join(A, n)
ES = json.load(io.open(R('es_full.json'), encoding='utf-8'))
EN = json.load(io.open(R('en_full.json'), encoding='utf-8'))
src = io.open(R('gen2.py'), encoding='utf-8').read()
ns = {}; exec(compile(src[:src.index('\nCHIP=')], 'gen2.py', 'exec'), ns)
PARES = ns['V'] + ns['A'] + ns['S']

fallos = []
def check(cond, msg):
    if not cond: fallos.append(msg)

N = len(PARES)

# --- el conteo que citan los documentos tiene que ser el de los datos ---
H = os.path.expanduser('~')
DOCS = [H + '/.claude/skills/editor-en-espanol/SKILL.md',
        H + '/.claude/skills/editor-en-espanol/README.md',
        H + '/claude-workspace/wiki-articles-claude/skills/wiki-editor-espanol/SKILL.md',
        H + '/claude-workspace/wiki-articles-claude/skills/wiki-editor-espanol/ES-CARD.md']
NES = sum(len(v) for v in ES.values()); NEN = sum(len(v) for v in EN.values())
for d in DOCS:
    if not os.path.exists(d):
        fallos.append('falta el documento %s' % d.replace(H, '~')); continue
    t = io.open(d, encoding='utf-8').read()
    for n in re.findall(r'(?:Los |los |\b)(\d+) (?:calcos|pares|falsos amigos)\b', t):
        check(int(n) == N, '%s: dice %s calcos, hay %d' % (os.path.basename(d), n, N))
    for n in re.findall(r'(\d+) acepciones del DLE', t):
        check(int(n) == NES, '%s: dice %s acepciones del DLE, hay %d' % (os.path.basename(d), n, NES))
    for n in re.findall(r'(\d+) acepciones de Cambridge', t):
        check(int(n) == NEN, '%s: dice %s de Cambridge, hay %d' % (os.path.basename(d), n, NEN))
    # los calcos tienen que estar DENTRO del documento obligatorio, no referenciados
    if d.endswith(('SKILL.md', 'ES-CARD.md')) and 'wiki-editor' in d or d.endswith('/editor-en-espanol/SKILL.md'):
        pass
    check('calcos-del-ingles' not in t and 'calcos-completos' not in t,
          '%s: referencia un fichero de calcos que ya no existe' % os.path.basename(d))

# --- los 93 pares tienen que estar embebidos en los dos ficheros obligatorios ---
for d in (DOCS[0], DOCS[3]):
    if not os.path.exists(d): continue
    t = io.open(d, encoding='utf-8').read()
    faltan = [p[0] for p in PARES if '`%s` ←' % p[0] not in t]
    check(not faltan, '%s: faltan %d pares embebidos: %s'
          % (os.path.basename(d), len(faltan), ', '.join(faltan[:5])))
    check(t.count('en Cambridge (') >= N, '%s: faltan artículos de Cambridge' % os.path.basename(d))
    check(t.count('en el DLE (') >= N, '%s: faltan artículos del DLE' % os.path.basename(d))

vistos = {}
for esd, end, esk, enk, men, mes, fix, lvl, nota in PARES:
    et = '%s←%s' % (esd, end)
    check(et not in vistos, 'par duplicado: %s' % et); vistos[et] = 1
    check(lvl in (1, 2, 3), '%s: nivel inválido %r' % (et, lvl))

    # las claves de búsqueda tienen que existir en los diccionarios
    check(esk in ES, '%s: falta «%s» en es_full.json' % (et, esk))
    check(enk in EN, '%s: falta «%s» en en_full.json' % (et, enk))
    if esk not in ES or enk not in EN: continue
    check(len(ES[esk]) > 0, '%s: entrada española vacía' % et)
    check(len(EN[enk]) > 0, '%s: entrada inglesa vacía' % et)

    # el marcador inglés tiene que casar, o la flecha nunca sale
    hits = [s for s in EN[enk] if men.lower() in s.lower()]
    check(len(hits) >= 1, '%s: el marcador inglés «%s» no casa con ninguna acepción' % (et, men))
    check(len(hits) <= 1, '%s: el marcador inglés «%s» casa con %d acepciones' % (et, men, len(hits)))

    # el marcador español, igual, cuando lo hay
    if mes is not None:
        h = [s for s in ES[esk] if mes.lower() in s.lower()]
        check(len(h) >= 1, '%s: el marcador español «%s» no casa' % (et, mes))
        check(len(h) <= 1, '%s: el marcador español «%s» casa con %d' % (et, mes, len(h)))

    # coherencia veredicto ↔ datos
    if lvl == 1:
        check(mes is None, '%s: NO CONSTA pero señala una acepción del DLE' % et)
        check(fix != '—', '%s: NO CONSTA sin recambio' % et)
    if lvl == 3:
        check(mes is not None, '%s: ACEPTADO pero no señala qué acepción lo ampara' % et)

print('pares: %d · acepciones DLE: %d · acepciones Cambridge: %d'
      % (len(PARES), sum(len(v) for v in ES.values()), sum(len(v) for v in EN.values())))
if fallos:
    print('\n%d FALLOS:' % len(fallos))
    for f in fallos: print('  ·', f)
    sys.exit(1)
print('todo correcto')
