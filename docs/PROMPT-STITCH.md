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

```
Es la pantalla más larga y más importante del sitio: 62 productos. El problema de diseño
central es que alguien pueda recorrerla desde el celular sin perderse ni cansarse.

CONTENIDO
Tres grandes grupos, con sus subcategorías:

COMIDAS
- Minutas con guarnición (7 productos, $17.000 a $23.500). Guarnición a elección:
  provenzal, ajillo, verdeo u oreganato.
- Ensaladas (6 productos, $17.000 a $19.500).
- Tartas (4 productos, $11.500 cada una).
- Lomito al pan (4 productos, $26.000 a $27.000). Chivito uruguayo, con papas fritas.
- Lomito al plato (3 productos, $25.000 a $32.000). Con papas fritas.

PIZZAS
- "Las de siempre" (11 productos).
- "Las de hoy" (11 productos).
- Porciones (6 productos, $1.200 a $4.800).
Las pizzas enteras tienen DOS precios según el tamaño: chica y grande
(por ejemplo, mozzarella $20.000 la chica y $24.000 la grande).

EMPANADAS
- 10 variedades, todas a $3.000.

CADA PRODUCTO TIENE
- Nombre.
- Precio (uno solo, o dos si es pizza entera).
- Una descripción corta de ingredientes, en la mayoría de los casos.
- Una foto, en la mayoría de los casos.

DOS SITUACIONES A RESOLVER
1. Nueve productos todavía no tienen foto. La solución no puede verse como un hueco roto
   ni como un error: tiene que convivir bien con los que sí la tienen, en la misma grilla.
2. El doble precio de las pizzas tiene que leerse con claridad, sin confundirse con un
   precio único raro.

ACCIONES QUE EL USUARIO TIENE QUE PODER HACER
- Saltar rápido entre comidas, pizzas y empanadas sin scrollear toda la página, y saber
  en todo momento en qué parte de la carta está.
- Ver un producto en detalle, con la foto más grande y la descripción completa.
- Pedir por WhatsApp, Mercado Pago, Rappi o PedidosYa.
- Ver dirección, horarios y ubicación.
```

---

## PANTALLA 3 — Cafetería

```
A diferencia de la carta, acá son muchos ítems de texto con precio y sin foto, así que el
problema es ordenar mucha información en poco espacio sin que se vuelva una lista infinita.

CONTENIDO
Ocho categorías con sus cantidades:
- Promos de todo el día (4 ítems, $5.200 a $11.500). Incluye además dos combos de desayuno
  destacados: uno clásico con café con leche a $8.000 y uno premium con tazón a $10.000,
  cada uno con opciones de acompañamiento a elección.
- Cafés e infusiones (11 ítems, $2.000 a $5.500), más dos extras (leche, crema).
- Especiales de la casa (2 ítems, $7.000): capuccinos con preparaciones propias.
- Licuados y bebidas (7 ítems, $2.500 a $9.000).
- Tortas y dulces (6 ítems, $8.500 cada una).
- Panadería y facturas (8 ítems, $1.000 a $6.000).
- Waffles (1 ítem, $4.000).
- Tostados y panes (8 ítems, $7.500 a $15.000).

Cada ítem tiene nombre y precio. Algunos llevan una aclaración breve
(por ejemplo "choco, crema, canela" o "pomelo o naranja").

ADEMÁS
Hay seis productos nuevos para destacar, con foto vertical: bagels, waffles, croissants
rellenos, muffins, tortas y volcán de chocolate.

ACCIONES QUE EL USUARIO TIENE QUE PODER HACER
- Encontrar rápido la categoría que busca sin recorrer las ocho.
- Ver los productos nuevos destacados.
- Pedir por WhatsApp, Mercado Pago, Rappi o PedidosYa.
- Ver dirección, horarios y ubicación.
```

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
