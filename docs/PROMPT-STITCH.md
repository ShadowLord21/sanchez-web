# Prompts para Google Stitch — rediseño visual de Sánchez & Sánchez

**Enfoque:** estos prompts le dan a Stitch el **contenido y las funciones** que cada pantalla
tiene que cubrir, sin dictarle el diseño. La resolución visual (layout, jerarquía, paleta,
tipografía, componentes) queda a su criterio.

**Cómo usar:** Stitch trabaja de a una pantalla. Pegá el **Contexto** y después el bloque de
la pantalla que quieras generar. Para las pantallas siguientes, volvé a pegar el Contexto
primero así mantiene coherencia.

Al final hay una sección de **restricciones técnicas** que **no** va para Stitch.

---

## CONTEXTO (pegar antes de cada pantalla)

```
Diseñá el sitio de "Sánchez & Sánchez", pizzería y cafetería de barrio en Av. Rivadavia 3399,
Almagro, Ciudad de Buenos Aires. Hace más de 20 años en el mismo lugar; es un clásico del
barrio para familias, vecinos y gente de paso.

Diseñalo mobile-first: casi todo el tráfico entra desde el celular. La versión de escritorio
importa, pero la decisión de diseño siempre se resuelve a favor del celular.

Quien entra busca una de tres cosas, casi siempre apurado:
ver la carta con precios, pedir delivery, o saber dónde queda y hasta qué hora abre.

Tono: cálido, de barrio, con oficio y tradición, pero con una ejecución actual y prolija.
Las fotos de los platos son el activo más fuerte del sitio y conviene que tengan protagonismo.
Son fotos reales, de comida, con tonos cálidos sobre madera o fondos oscuros.

Todo el texto en español rioplatense (voseo): "Carta", "Pedí ahora", "Visitanos".

Tenés libertad total para definir paleta, tipografías, retícula, estilo de componentes y
cómo resolver cada sección. Lo que sigue es el contenido que tiene que estar y lo que el
usuario tiene que poder hacer, no una indicación de cómo debe verse.
```

---

## PANTALLA 1 — Inicio

```
INFORMACIÓN QUE TIENE QUE TRANSMITIR
- Qué es el lugar y dónde queda: pizzería y cafetería en Almagro, CABA.
- Que lleva más de 20 años en el barrio: es su principal argumento de confianza.
- Su historia: más de dos décadas en Av. Rivadavia; pizzas a la piedra, empanadas caseras
  y cocina de siempre; y un rincón de cafetería para desayunar o merendar con medialunas
  recién hechas, tortas caseras y tostados.
- Prueba social: cuatro reseñas reales de Google, todas de 5 estrellas, de clientes del
  barrio. Mencionan la atención, las medialunas, el café, las pizzas a la piedra y un combo
  llamado "La Escaloneta".
- El Menú del Día: $20.000, incluye plato principal + bebida + café o postre.
  Disponible de lunes a viernes de 12 a 16 hs, solo efectivo. Hay cuatro platos distintos
  por cada día de la semana. Además hay una opción de invierno (guiso de lentejas o pastel
  de papa) y una opción especial de bife a caballo con papas fritas a $21.000.
- Que hacen pedidos para llevar.

ACCIONES QUE EL USUARIO TIENE QUE PODER HACER
- Ir a la carta de la pizzería y a la de la cafetería.
- Ver qué hay de menú del día para cada día de lunes a viernes (debería arrancar mostrando
  el día actual).
- Pedir por WhatsApp, Mercado Pago, Rappi o PedidosYa.
- Ver la dirección, los horarios y cómo llegar (hay un mapa embebido).
- Llamar por teléfono e ir a las redes.

DATOS DE CONTACTO
Av. Rivadavia 3399, CABA (Almagro / Balvanera)
Lunes a Viernes 7:00 a 00:00 · Sábados y Domingos 8:00 a 01:00
Teléfono 11 5927-3756 · Instagram @sanchezysanchez_ok · TikTok @sanchezysanchez2006
```

---

## PANTALLA 2 — Carta

> **Usá esta versión corta.** La carta real tiene 62 productos, pero pedirle todo a Stitch
> hace que falle. Con esta muestra alcanza: los 6 productos elegidos cubren **todas** las
> variantes de tarjeta que existen en el sitio. Una vez que el diseño guste, se replica
> al resto en el código.

```
Diseñá la pantalla de la carta de la pizzería.

1) PROMOS — ARRIBA DE TODO, ES LO PRIMERO QUE SE VE
Son la oferta más rentable del local y tienen que destacarse por encima del resto de la
carta. Cada una es un combo: lo que incluye es tan importante como el precio.

- Muzza grande + bebida grande — $26.000
- 6 empanadas a elección + muzza grande + bebida grande — $35.000
- Fugazzeta rellena + bebida grande + 4 porciones de faina — $44.000
- 2 porciones de muzza + 2 faina + bebida chica — $10.500
- Muzza grande + jamón y morrón grande + bebida grande — $40.000

Y aparte, una promo de TAKE AWAY (solo para llevar), que conviene diferenciar visualmente
de las anteriores porque es otra modalidad:
- Muzza grande + 2 faina — $12.000

2) EL RESTO DE LA CARTA
Se divide en tres grupos: Comidas, Pizzas y Empanadas. En total son 62 productos, así que
en celular NO pueden mostrarse todos de corrido: el usuario elige un grupo y ve solamente
ese, cambiando de grupo sin recargar ni perder el lugar. Las tarjetas van de a dos por
fila para que entren más productos por pantalla.

Productos de ejemplo:
- Mozzarella (pizza entera). Chica $20.000 / Grande $24.000.
- Napolitana (porción). $3.700.
- Empanada de carne. $3.000. "Carne cortada a cuchillo, cebolla y huevo".

Todos los productos tienen foto.

DOS COSAS QUE TIENE QUE RESOLVER LA TARJETA
- Las pizzas enteras tienen DOS precios (chica y grande). Tienen que leerse con claridad,
  sin confundirse con un precio único raro.
- Algunos productos tienen una descripción corta de ingredientes y otros no.

Diseñá también la vista de detalle que se abre al tocar una tarjeta, con la foto más
grande, el nombre, la descripción completa y el precio.

3) Incluí el bloque de delivery (WhatsApp, Mercado Pago, Rappi, PedidosYa) y el de
ubicación con dirección, horarios y mapa.
```

> **Por qué el filtro por grupo:** medido en el sitio actual, la carta completa son
> 31.091 px de alto, o sea **37 pantallas** de scroll en un celular. Con filtro por grupo
> y dos columnas baja a **~5 pantallas**.

**Para replicar después** (no va en el prompt, es el inventario real):

| Grupo | Subcategorías | Productos |
|---|---|---|
| Comidas | Minutas (7), Ensaladas (6), Tartas (4), Lomito al pan (4), Lomito al plato (3) | 24 |
| Pizzas | Las de siempre (11), Las de hoy (11), Porciones (6) | 28 |
| Empanadas | — | 10 |
| | | **62** |

---

## PANTALLA 3 — Cafetería

> **También reducida**, por el mismo motivo: son 47 ítems en 8 categorías. Con 3 categorías
> de muestra alcanza para ver cómo resuelve la lista, el ítem con aclaración y el combo
> destacado.

```
Diseñá la pantalla de la cafetería. Acá no hay fotos de producto: son listas de ítems con
precio. El problema es ordenar mucha información en poco espacio sin que se vuelva una
lista infinita de scrollear.

En total son 8 categorías. Mostrá estas 3 como ejemplo, y dejá indicadas las otras 5
(Licuados y Bebidas, Tortas y Dulces, Panadería y Facturas, Waffles, Tostados y Panes):

PROMOS — TODO EL DÍA
Dos combos destacados, que merecen más peso visual que el resto:
- "Clásico — café con leche". $8.000. Acompañalo con: 2 tostones con huevo y palta,
  tostado de jamón y queso, o croissant de jamón y queso.
- "Premium — tazón". $10.000. Acompañalo con: bagel a elección o waffle.
Y una lista común:
- Café con leche + 3 medialunas. $5.200.
- Licuado o café con leche + torta. $11.500.

CAFÉS E INFUSIONES
- Café expreso. $3.000.
- Café con leche. $3.500.
- Capuccino. $5.500.
- Té con 2 medialunas. $3.000.

ESPECIALES DE LA CASA
- Capuccino "Sánchez". $7.000. Aclaración: "choco, crema, canela".
- Capuccino Italiano. $7.000. Aclaración: "crema, choco rallado".

El usuario tiene que poder encontrar rápido la categoría que busca sin recorrer las ocho.

Sumá arriba una franja de productos nuevos destacados, con foto vertical: bagels, waffles,
croissants rellenos, muffins, tortas y volcán de chocolate.

Incluí también el bloque de delivery (WhatsApp, Mercado Pago, Rappi, PedidosYa) y el de
ubicación con dirección, horarios y mapa.
```

**Para replicar después** (inventario real): Promos (4 + 2 combos), Cafés e infusiones (11 + 2 extras),
Especiales de la casa (2), Licuados y bebidas (7), Tortas y dulces (6), Panadería y facturas (8),
Waffles (1), Tostados y panes (8). **Total 47 ítems.**

---

## PRESENTE EN LAS TRES PANTALLAS

```
- Identidad del local y navegación entre inicio, carta, cafetería, delivery y ubicación.
  En celular tiene que resolverse sin ocupar toda la pantalla y con una salida clara.
- Bloque de delivery y pedidos con cuatro opciones: WhatsApp, Mercado Pago, Rappi y
  PedidosYa. Es la principal acción de conversión del sitio y conviene que esté siempre
  a mano desde el celular.
- Bloque de ubicación y contacto: dirección, horarios, teléfono, redes y mapa.
- Pie de página.
```

---

## PANTALLA 4 — Error 404 (opcional)

```
Una página para cuando el enlace no existe. Tiene que avisar que no se encontró la página,
mantener la identidad del sitio, y ofrecer salidas: inicio, carta y cafetería.
```

---

# Restricciones técnicas — NO mandar a Stitch

Para cuando vuelva el diseño y haya que integrarlo. El sitio es **HTML + CSS + JavaScript
puro**, sin framework ni build, en GitHub Pages detrás de Cloudflare.

| Restricción | Por qué | Qué implica |
|---|---|---|
| **CSP estricta sin `unsafe-inline`** | Protección anti-XSS ya auditada e implementada | **Nada de atributos `style=""` en el HTML.** Todo va en el `<style>` o en clases. Tras cada cambio: `python3 docs/scripts/regen_csp.py` |
| **Fuentes self-hosteadas** | Privacidad: el sitio no hace ningún pedido a Google | Si Stitch propone otra tipografía, hay que bajar los `.woff2` a `assets/fonts/` y sumarlos a `fonts.css`. Nunca un `<link>` a fonts.googleapis.com |
| **Sin frameworks** | No hay build ni dependencias | Si el diseño viene en Tailwind o React, se traduce a CSS plano |
| **Imágenes optimizadas** | Se bajó de 107 MB a 7,4 MB | Fotos de producto a 900 px máx, JPEG calidad 82 |
| **Accesibilidad** | Ya implementada | Contraste 4.5:1, `aria-expanded` donde corresponda, foco visible, teclado, zonas táctiles de 44 px |
| **Mobile real probado** | Hubo bugs reales de hitbox y de menú | Revalidar con el script de verificación antes de publicar |

**No se cambia el contenido:** nombres de productos, precios, descripciones, teléfono,
dirección, horarios y enlaces de delivery. El refactor es visual.
