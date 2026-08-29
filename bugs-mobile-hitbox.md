# Bug crítico en MOBILE — Hitboxes desalineadas y redirecciones equivocadas

## Resumen del problema

En **mobile** (en desktop anda bien) hay un problema general de interacción: **el área clickeable real (la "hitbox") de los elementos está desalineada o desplazada respecto de lo que se ve**. Al tocar un título, un texto o una imagen, el recuadro que efectivamente recibe el toque **no está sobre lo que toqué**, sino corrido (normalmente **más arriba**, o con otra forma). Consecuencia: los toques caen sobre el elemento equivocado y la página **redirige constantemente a lugares que no corresponden** (sobre todo a las secciones "Visitanos" y "Delivery y Pedidos" del Home, o entre páginas).

Hay **dos problemas entrelazados** que hay que resolver juntos:

- **A) Elementos que NO deberían ser interactivos están redirigiendo.** Títulos, subtítulos, descripciones e imágenes decorativas disparan navegación a secciones. No deberían hacer nada al tocarlos.
- **B) Los controles REALES no funcionan porque una capa/elemento desplazado les roba el toque.** Pestañas de categorías, acordeones, tarjetas de producto y slideshows: al tocarlos, una hitbox corrida intercepta el toque y redirige, en vez de ejecutar su acción.

> **Nota:** todo esto pasa **solo en mobile/touch**; en desktop las funciones andan bien. El foco del arreglo es el comportamiento táctil y el responsive.

---

## Causa raíz (hipótesis para investigar)

El síntoma "toco una cosa pero la hitbox aparece corrida arriba / con otra forma" apunta a una o varias de estas causas. Revisar todas:

1. **Secciones o contenedores enteros envueltos en `<a>` o con `onclick`** apuntando a otra sección/página. Eso explica que al tocar cualquier parte (título, descripción, imagen) de una sección se dispare una redirección. **Los títulos, descripciones e imágenes decorativas NO deben estar dentro de un enlace ni tener handlers de click.**
2. **Desfasaje entre la posición visual y la hitbox por transforms / animaciones de scroll-reveal.** Si un elemento se muestra con `transform: translateY(...)` (o animaciones de aparición) y la animación o el estado inicial queda mal, el highlight/hit target puede quedar corrido respecto de lo que se ve. Revisar animaciones de entrada, `transform`, `will-change`, y estados que no se resetean.
3. **Capas superpuestas invisibles** (elementos `position:absolute/fixed`, márgenes negativos, overlays, o un `<a>` más grande que su contenido visible) que quedan **por encima y corridas** e interceptan el toque. Ajustar `z-index` y aplicar `pointer-events:none` a las capas puramente decorativas.
4. **Anclas rotas/erróneas.** Enlaces que apuntan a un `id` equivocado o inexistente hacen "saltar a cualquier lado". Cada enlace interno debe apuntar a un `id` real y correcto.
5. **Controles (tabs/acordeones/slideshow/tarjetas) tapados por otro elemento** con hitbox desplazada, por eso "no dejan tocarlos" y redirigen.

---

## Comportamiento correcto esperado (regla general)

- **Títulos, subtítulos, descripciones e imágenes decorativas:** NO son clickeables. Al tocarlos no pasa nada.
- **Logo del header:** lleva al inicio del Home (misma acción en todas las páginas). Nada más.
- **Botones y enlaces reales:** su hitbox coincide exactamente con lo que se ve, y llevan a su destino correcto.
- **Controles (pestañas de categoría, acordeones, slideshow, tarjetas de producto):** ejecutan su función (scroll a la sección / abrir-cerrar / mover slide / abrir modal), sin redirigir.

---

## Lista detallada de errores (17)

### Home (`index.html`)

1. **Logo "Sánchez & Sánchez" (header).** Al tocarlo redirige a la Carta; y estando en la Carta, al tocarlo de nuevo redirige a la sección "Visitanos" del Home. Hitbox desplazada.
   → **Esperado:** el logo lleva al inicio del Home, consistente en todas las páginas. No a Carta ni a Visitanos.
2. **Título del hero "Sánchez & Sánchez" (grande).** Al tocarlo redirige a "Visitanos".
   → **Esperado:** no clickeable (es un título).
3. **Descripción del hero** ("Pizzería y Cafetería en el corazón de Almagro… hace más de 20 años"). Al tocarla redirige a "Visitanos".
   → **Esperado:** no clickeable.
4. **Los 4 botones del hero** (Ver la Carta / Cafetería / Menú del Día / Delivery). A veces salta una hitbox **corrida hacia arriba** que los recubre y redirige mal.
   → **Esperado:** cada botón con su hitbox exacta y su destino: Ver la Carta → `/carta/`; Cafetería → `/cafeteria/`; Menú del Día → `#menudeldia` (scroll interno); Delivery → `#delivery` (scroll interno).
15. **Imagen del "Menú del Día"** (la pizza con "$20.000"). Al tocarla redirige a "Visitanos".
   → **Esperado:** imagen decorativa, no clickeable.
16. **Título "Delivery y Pedidos"** ("PEDÍ AHORA / Delivery y Pedidos"). Al tocarlo redirige a "Visitanos".
   → **Esperado:** no clickeable. (Las 4 tarjetas de delivery sí deben abrir sus apps: WhatsApp, Mercado Pago, Rappi, PedidosYa.)
17. **Título "Visitanos"** (sección ubicación/contacto). Al tocarlo scrollea a cualquier parte de la página.
   → **Esperado:** no clickeable.

### Carta (`/carta/`)

5. **Encabezado "LA CARTA / Nuestra Carta"** (inicio de la página). Al tocarlo redirige a la página de Cafetería.
   → **Esperado:** no clickeable.
6. **Barra de categorías (Comidas / Pizzas / Empanadas).** Una hitbox desplazada encima no deja tocarlas; al tocar redirige a "Delivery y pedidos" del Home.
   → **Esperado:** cada pestaña hace scroll a su sección dentro de la Carta (`#comidas`, `#pizzas`, `#empanadas`), con hitbox exacta.
7. **Slideshow "Promos para compartir".** Al tocar las imágenes aparece una hitbox en la parte superior que manda a "Visitanos".
   → **Esperado:** tocar la imagen no redirige (a lo sumo avanza el slide); los controles del slideshow funcionan.
8. **Título de la sección "Pizzas" ("LAS DE SIEMPRE / Chica / Grande").** Al tocarlo redirige a "Delivery" del Home. (Es el destino al que debería llevar la pestaña del error 6.)
   → **Esperado:** no clickeable.
9. **Foto intercalada "Pizza a la piedra, recién salida del horno".** Mismo error de imagen/hitbox al tocarla.
   → **Esperado:** decorativa, no clickeable.
10. **Tarjeta de producto "Jamón" (Pizzas).** Al tocar la imagen redirige a "Visitanos" en vez de abrir el modal del producto. En otras tarjetas no se vio, pero **revisar TODAS las tarjetas de producto**.
   → **Esperado:** tocar la tarjeta (o su imagen) abre el modal del producto (foto + descripción + precio). Nunca redirige.

### Cafetería (`/cafeteria/`)

11. **Slideshow "Productos nuevos".** Igual que el error 7: al tocar las imágenes salta la hitbox desplazada arriba y redirige.
   → **Esperado:** tocar la imagen no redirige; el slideshow funciona.
12. **Foto intercalada "Nuestra vitrina, siempre fresca".** Mismo error de imagen/hitbox.
   → **Esperado:** decorativa, no clickeable.
13. **Encabezado "Nuestra Cafetería".** Mismo error de hitbox al tocarlo.
   → **Esperado:** no clickeable.
14. **Acordeones de categorías (TODOS):** Cafés e Infusiones, Especiales de la Casa, Licuados y Bebidas, Tortas y Dulces, Panadería y Facturas, Waffles, Tostados y Panes, Promos — Todo el Día. Al tocar el botón (+/×) para abrir o cerrar cualquiera, redirige a algún apartado del Home. **NINGUNO funciona.**
   → **Esperado:** el botón (+/×) abre/cierra su sección (acordeón) en mobile, sin redirigir.

---

## Cómo trabajar (para Claude Code)

1. **Commit de checkpoint** antes de tocar nada.
2. Reproducí los bugs en **viewport mobile / emulación de dispositivo**, recorriendo las 3 páginas.
3. Corregí de forma sistemática (no caso por caso aislado): buscá el/los patrones comunes (secciones envueltas en `<a>`, transforms que desplazan la hitbox, overlays con `z-index`/`pointer-events` mal, anclas erróneas) y arreglá de raíz.
4. **Arreglá el PATRÓN COMÚN, no cada caso por separado.** La mayoría de estos 17 bugs seguramente vienen del mismo culpable (o de 1-2 culpables) que se repite en varias secciones — por ejemplo, un componente/sección envuelto en `<a>`, o una animación/transform que desplaza la hitbox. Identificá esa causa de fondo y corregila de raíz para que se arreglen todos juntos y NO vuelvan a aparecer. Evitá parches sueltos por elemento. En el reporte final, decime cuál fue el patrón/causa principal.
5. Aplicá el comportamiento esperado de cada error de la lista.
5. **No cambies el contenido** (textos, precios, links, etc.) ni el diseño visual: esto es corrección de comportamiento/hitboxes/responsive.
6. No toques el CNAME ni la config de deploy.

## Verificación final

- Probá en **varios tamaños de celular** (chico y grande) las 3 páginas.
- Confirmá uno por uno los 17 casos: que los títulos/descripciones/imágenes decorativas **no hagan nada**, que los 4 botones del hero, las pestañas de categoría, las tarjetas de producto (abren modal), los slideshows y los acordeones **funcionen y no redirijan**, y que **ninguna hitbox quede corrida** respecto de lo que se ve.
- Verificá que **desktop siga andando igual** (no romper lo que ya funcionaba).
- Pasame la lista de qué causaba cada bug y cómo lo arreglaste.
