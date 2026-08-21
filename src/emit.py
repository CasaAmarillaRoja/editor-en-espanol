# -*- coding: utf-8 -*-
import io, os, re, unicodedata

def datos(fichero, corte):
    src = io.open(fichero, encoding='utf-8').read()
    src = src[:src.index(corte)]
    ns = {}
    exec(compile(src, fichero, 'exec'), ns)
    return ns

def limpio(s):
    s = re.sub(r'<i>(.*?)</i>', r'*\1*', s)
    s = re.sub(r'<b>(.*?)</b>', r'**\1**', s)
    s = re.sub(r'<code>(.*?)</code>', r'`\1`', s)
    s = re.sub(r'<sup>(.*?)</sup>', r'^\1', s)
    s = re.sub(r'<[^>]+>', '', s)
    return s.strip()

DEST = os.path.expanduser('~/.claude/skills/editor-en-espanol/references')
os.makedirs(DEST, exist_ok=True)

# ---------- 1. gramática y ortografía (manual.py) ----------
man = datos('manual.py', '\nVER=')
VERD = {'error':'ERROR','ambas':'AMBAS','depende':'DEPENDE','bien':'REGLA'}
MARCA = {'mal':'mal','bien':'bien','ambas':'vale'}
orto_ids = {'acentuacion','coma','otros-signos','comillas','interrogacion',
            'mayusculas','cursiva','cifras','espacios','dialogos'}
buckets = {'orto':[], 'gram':[]}
for sid, titulo, intro, reglas in man['S']:
    dst = 'orto' if sid in orto_ids else 'gram'
    b = ['\n## %s\n' % titulo]
    if intro: b.append('_%s_\n' % limpio(intro))
    for t, ver, ejs, nota in reglas:
        b.append('### %s — `%s`' % (limpio(t), VERD[ver]))
        for m, e in ejs:
            b.append('- **%s** · %s' % (MARCA[m], limpio(e)))
        if nota: b.append('\n%s' % limpio(nota))
        b.append('')
    buckets[dst].append('\n'.join(b))

CAB = ('# %s\n\nDestilado del *Libro de estilo de la lengua española* (RAE-ASALE).\n\n'
       'Veredictos: `ERROR` se corrige sin preguntar · `AMBAS` y `DEPENDE` **no se tocan**, '
       'se proponen · `REGLA` es la norma positiva que hay que conocer.\n')
io.open(DEST+'/norma-ortotipografia.md','w',encoding='utf-8').write(
    CAB % 'Norma: ortotipografía, puntuación y cifras' + ''.join(buckets['orto']))
io.open(DEST+'/norma-gramatica.md','w',encoding='utf-8').write(
    CAB % 'Norma: gramática de uso' + ''.join(buckets['gram']))

# ---------- 2. cursiva o comillas (cursiva.py) ----------
cur = datos('cursiva.py', '\nDEST=')
D = {'cursiva':'*cursiva*','comillas':'«comillas»','redonda':'redonda',
     'simples':'‘simples’','nunca':'sin resalte'}
out = ['# Cursiva, comillas o redonda\n',
 '**Regla madre:** la obra completa va en *cursiva*; la pieza que vive dentro de otra obra va entre «comillas».\n',
 '**Corolario:** si la mayúscula ya delimita el título, la cursiva sobra — de ahí que *el Código Civil*, '
 '*la Biblia* y *Alianza Universidad* vayan en redonda.\n',
 '**Comillas:** angulares « » fuera, inglesas “ ” dentro, simples ‘ ’ en último lugar. '
 'El orden de anidamiento es obligatorio; la preferencia por las angulares es recomendación de la RAE, '
 'pero **regla de la casa aquí: siempre angulares**. En Wikipedia en español la respalda su Manual de estilo.\n',
 '**Puntuación:** el punto, la coma, el punto y coma y los dos puntos van **siempre después** del cierre de comillas.\n']
for titulo, filas in cur['G']:
    out.append('\n## %s\n' % titulo)
    out.append('| Qué es | Va en | Ejemplo | Nota |')
    out.append('|---|---|---|---|')
    for cosa, dest, ej, nota, der in filas:
        n = limpio(nota) + (' _(deducido de la regla madre; el corpus no lo nombra)_' if der else '')
        out.append('| %s | %s | %s | %s |' % (limpio(cosa), D[dest], limpio(ej).replace('|','\\|'), n or '—'))
io.open(DEST+'/cursiva-y-comillas.md','w',encoding='utf-8').write('\n'.join(out)+'\n')

# ---------- 3. calcos del inglés (gen2.py) ----------
g2 = datos('gen2.py', '\nCHIP=')
NIV = {1:'NO CONSTA',2:'EN PUGNA',3:'ACEPTADO'}
out = ['# Calcos semánticos del inglés\n',
 'Cada fila: la acepción inglesa en juego (Cambridge) frente a lo que el DLE recoge de la palabra española.\n',
 '`NO CONSTA` = el DLE no recoge esa acepción; es error señalable. '
 '`EN PUGNA` = la recoge pero restringida o el DPD la censura; delata por frecuencia, no por error. '
 '`ACEPTADO` = **no lo señales nunca**.\n',
 '\nLos recambios están cotejados contra la lista de sinónimos que el DLE da para la palabra acusada, '
 'para que la cura no esté dentro de la enfermedad.\n']
for nombre, lista in (('Verbos', g2['V']), ('Adjetivos y adverbios', g2['A']), ('Sustantivos', g2['S'])):
    out.append('\n## %s\n' % nombre)
    out.append('| Par | Acepción inglesa en juego | Qué dice el DLE | Escribe esto | Nivel |')
    out.append('|---|---|---|---|---|')
    for esd, end, esk, enk, men, mes, fix, lvl, nota in lista:
        dle = limpio(mes) if mes else '**no consta**'
        f = '—' if fix == '—' else limpio(fix)
        out.append('| `%s` ← *%s* | %s | %s | %s | %s |' % (
            limpio(esd), limpio(end), limpio(men), dle.replace('|','\\|'), f, NIV[lvl]))
        if nota:
            out.append('| | | | | %s |' % limpio(nota).replace('|','\\|')[:300])
io.open(DEST+'/calcos-del-ingles.md','w',encoding='utf-8').write('\n'.join(out)+'\n')

for f in sorted(os.listdir(DEST)):
    print('%-32s %6d bytes' % (f, os.path.getsize(DEST+'/'+f)))
