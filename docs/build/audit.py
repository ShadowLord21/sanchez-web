"""Audita que todas las clases usadas en un HTML esten compiladas en el CSS."""
import re
import io
import sys

html_path, css_path = sys.argv[1], sys.argv[2]
h = io.open(html_path, encoding='utf-8').read()
css = io.open(css_path, encoding='utf-8').read()

usadas = set()
for m in re.findall(r'class="([^"]*)"', h):
    usadas |= set(m.split())

ESPECIALES = set(".:/[]()#%,!<>&'\"")


def escapar(clase):
    """Tailwind escapa los caracteres especiales en el selector."""
    salida = []
    for ch in clase:
        if ch in ESPECIALES:
            salida.append(chr(92))
        salida.append(ch)
    return ''.join(salida)


falta = sorted(c for c in usadas if ('.' + escapar(c)) not in css)
print('clases usadas: {} | sin compilar: {}'.format(len(usadas), len(falta)))
for c in falta[:40]:
    print('    ' + c)
