# -*- coding: utf-8 -*-
"""Lanza toda la verificación: datos, reconstrucción y hooks."""
import hashlib, io, os, subprocess, sys

A = os.path.dirname(os.path.abspath(__file__)); H = os.path.expanduser('~')
SALIDAS = [H + '/.claude/skills/editor-en-espanol/SKILL.md',
           H + '/.claude/skills/editor-en-espanol/references/norma-ortotipografia.md',
           H + '/.claude/skills/editor-en-espanol/references/norma-gramatica.md',
           H + '/.claude/skills/editor-en-espanol/references/cursiva-y-comillas.md',
           H + '/claude-workspace/wiki-articles-claude/skills/wiki-editor-espanol/ES-CARD.md']
PLUGIN = H + '/claude-workspace/wiki-articles-claude'
fallos = []

def paso(nombre, fn):
    print('\n== %s ==' % nombre)
    try:
        fn(); print('   ok')
    except Exception as e:
        fallos.append(nombre); print('   FALLA: %s' % e)

def datos():
    r = subprocess.run([sys.executable, os.path.join(A, 'test_calcos.py')],
                       capture_output=True, text=True)
    print('   ' + r.stdout.strip().replace('\n', '\n   '))
    if r.returncode: raise AssertionError('integridad de datos')

def firma():
    return {p: hashlib.sha256(io.open(p, 'rb').read()).hexdigest()[:12]
            for p in SALIDAS if os.path.exists(p)}

def reconstruccion():
    antes = firma()
    faltan = [p for p in SALIDAS if p not in antes]
    if faltan: raise AssertionError('no existen: %s' % ', '.join(faltan))
    for _ in range(2):
        r = subprocess.run([sys.executable, os.path.join(A, 'build.py')],
                           capture_output=True, text=True)
        if r.returncode: raise AssertionError('build.py falló: %s' % r.stderr.strip()[-200:])
    despues = firma()
    movidos = [os.path.basename(p) for p in antes if antes[p] != despues.get(p)]
    if movidos: raise AssertionError('la reconstrucción cambió: %s' % ', '.join(movidos))
    print('   %d ficheros idénticos tras dos reconstrucciones' % len(antes))

def hooks():
    r = subprocess.run(['node', '--test', 'tests/hooks-es.test.mjs'],
                       cwd=PLUGIN, capture_output=True, text=True)
    for l in r.stdout.splitlines():
        if l.startswith(('✔', '✖', 'ℹ pass', 'ℹ fail')): print('   ' + l)
    if r.returncode: raise AssertionError('tests de hooks')

paso('integridad de los datos', datos)
paso('reconstrucción estable', reconstruccion)
paso('hooks e inyección', hooks)

print('\n' + ('%d BLOQUES FALLAN: %s' % (len(fallos), ', '.join(fallos)) if fallos
              else 'Todo verificado.'))
sys.exit(1 if fallos else 0)
