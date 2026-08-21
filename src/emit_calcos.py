# -*- coding: utf-8 -*-
"""Genera el fichero de calcos CON los artículos completos de ambos diccionarios.

El fichero condensado que había antes solo llevaba la acepción en juego. Eso basta
para decidir, pero no para justificar: sin el artículo entero no se ve que el español
sí cubre parte del campo inglés, que es lo que evita señalar como calco un uso legítimo.
"""
import io, json, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
def R(n): return os.path.join(AQUI, n)

ES = json.load(io.open(R('es_full.json'), encoding='utf-8'))
EN = json.load(io.open(R('en_full.json'), encoding='utf-8'))

def datos(f, corte):
    s = io.open(R(f), encoding='utf-8').read(); s = s[:s.index(corte)]
    ns = {}; exec(compile(s, f, 'exec'), ns); return ns
G = datos('gen2.py', '\nCHIP=')

def L(s):
    s = re.sub(r'<i>(.*?)</i>', r'*\1*', s); s = re.sub(r'<b>(.*?)</b>', r'**\1**', s)
    s = re.sub(r'<code>(.*?)</code>', r'`\1`', s)
    return re.sub(r'<[^>]+>', '', s).strip()

NIV = {1: 'NO CONSTA', 2: 'EN PUGNA', 3: 'ACEPTADO'}
o = ["""# Calcos del inglés: los artículos completos

Los 92 pares, cada uno con **el artículo entero de los dos diccionarios**: Cambridge
para el inglés, DLE para el español. La acepción que está en juego va marcada con `←`.

Van completos a propósito. Casi todas estas palabras son polisémicas y **parte de su
campo inglés sí existe en español**: *dramatic* tiene tres sentidos y el español cubre
dos. Con el artículo entero delante se ve de un golpe qué se puede señalar y qué no; con
un resumen, no — y señalar un uso legítimo hace más daño que dejar pasar el calco.

Los recambios están cotejados contra la lista de sinónimos que el DLE publica para la
palabra acusada, para que la cura no esté dentro de la enfermedad.

| Nivel | Qué significa |
|---|---|
| `NO CONSTA` | El DLE no recoge esa acepción. Error señalable |
| `EN PUGNA` | La recoge, pero restringida a un campo o región, o el DPD la censura. Delata por frecuencia, no por error |
| `ACEPTADO` | Recogida sin reservas. **No lo señales nunca** |
"""]

def bloque(nombre, lista):
    o.append('\n## %s\n' % nombre)
    for esd, end, esk, enk, men, mes, fix, lvl, nota in lista:
        o.append('### `%s` ← *%s* — %s\n' % (L(esd), L(end), NIV[lvl]))
        ing = EN.get(enk, [])
        o.append('**Cambridge, *%s*** — %d %s' % (
            L(enk), len(ing), 'acepción' if len(ing) == 1 else 'acepciones'))
        for s in ing:
            m = ' ←' if men and men.lower() in s.lower() else ''
            o.append('- %s%s' % (s, m))
        esp = ES.get(esk, [])
        cab = '**DLE, *%s*** — %d %s' % (L(esk), len(esp),
              'acepción' if len(esp) == 1 else 'acepciones')
        if not mes: cab += ' · **ninguna recoge el sentido inglés**'
        o.append('\n' + cab)
        for s in esp:
            m = ' ←' if mes and mes.lower() in s.lower() else ''
            o.append('- %s%s' % (s, m))
        o.append('\n**Escribe:** %s' % ('no hace falta cambiar nada' if fix == '—' else L(fix)))
        if nota: o.append('\n**Nota:** %s' % L(nota))
        o.append('')

bloque('Verbos', G['V']); bloque('Adjetivos y adverbios', G['A']); bloque('Sustantivos', G['S'])
txt = '\n'.join(o) + '\n'
for d in sys.argv[1:]:
    io.open(d, 'w', encoding='utf-8').write(txt)
    print('%s  %.1f KB' % (d.replace(os.path.expanduser('~'), '~'), len(txt) / 1024))
