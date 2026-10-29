# Build del CSS

El sitio publicado **no depende de esto**: el CSS se compila una vez y se
commitea en `assets/css/app.css`. Esta carpeta no se publica.

## Para qué

Los diseños de Google Stitch (`docs/stitch/codigo/`) vienen en Tailwind con
una config propia. El sitio no puede cargar el CDN de Tailwind (CSP estricta,
sin `unsafe-inline` y sin pedidos a terceros), así que se compila la **misma
config, exacta**, a un CSS estático.

`tailwind.config.js` es la config extraída tal cual del HTML de Stitch. Si
Stitch cambia, hay que volver a extraerla — no editarla a mano.

## Cómo

    cd docs/build
    npm install
    npm run css

Sale en `assets/css/app.css`.

## Auditar

    python audit.py ../../index.html ../../assets/css/app.css

Lista las clases usadas en el HTML que no quedaron en el CSS. Las únicas
que deben faltar son `material-symbols-outlined` (viene de `fonts.css`),
`scrollbar-none` y `day-tab` (no son de Tailwind).

Ojo: el minificador escribe `rgba(x,y,z,.04)` sin el cero, así que las
sombras arbitrarias pueden aparecer como faltantes siendo un falso positivo.

## Íconos

`iconos.txt` tiene los 39 nombres de Material Symbols que usan los diseños.
La fuente está subseteada a esos íconos y self-hosteada en `assets/fonts/`.
Si aparece un ícono nuevo, hay que sumarlo ahí y volver a pedir el subset.
