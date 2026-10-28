# Prompts para Google Stitch — rediseño visual de Sánchez & Sánchez

**Cómo usar este archivo:** Stitch trabaja mejor de a una pantalla por vez. Pegá primero el
**Bloque A** (contexto y estilo) y generá la Home. Después, para cada pantalla siguiente,
volvé a pegar el Bloque A seguido del bloque de esa pantalla, así mantiene la coherencia.

Al final está la sección **"Restricciones técnicas"** — esa NO se la mandes a Stitch, es para
cuando haya que integrar el diseño al código.

---

## BLOQUE A — Contexto y estilo (pegar siempre primero)

```
Diseñá el sitio web de "Sánchez & Sánchez", una pizzería y cafetería de barrio en
Av. Rivadavia 3399, Almagro, Ciudad de Buenos Aires, Argentina. Lleva más de 20 años
en el mismo lugar y es un clásico del barrio: familias, vecinos y gente de paso.

AUDIENCIA Y PRIORIDAD
La enorme mayoría entra desde el celular, buscando tres cosas: ver la carta con precios,
pedir delivery, o saber dónde queda y hasta qué hora abre. Diseñá mobile-first (360-430 px
de ancho) y recién después la versión de escritorio. Cada decisión tiene que favorecer
"encontrar rápido lo que busco", no el lucimiento visual.

PERSONALIDAD
Cálido, de barrio, con oficio. Nada corporativo ni minimalista frío. Que transmita comida
casera y tradición, pero con una ejecución moderna y prolija. Las fotos de los platos son
el corazón del sitio: tienen que respirar y verse apetitosas.

IDIOMA
Todo en español rioplatense (voseo). Usá "Carta", "Pedí ahora", "Visitanos", "Menú del Día".

PALETA ACTUAL (podés proponer una evolución, pero mantené la familia cálida)
- Fondo crema: #FEFCF9
- Fondo alternativo: #F8F4EE
- Texto principal: #1A1816
- Texto secundario: #6F6B66
- Acento terracota (precios, botones, detalles): #BF4A2B
- Bordes sutiles: #E9E4DC
- Verde (datos de "para llevar"): #3D6B4F

TIPOGRAFÍA ACTUAL
- Títulos: DM Serif Display (serif, con carácter)
- Texto y UI: DM Sans
Podés proponer otra combinación serif + sans, pero mantené el contraste entre un título
con personalidad y un cuerpo muy legible.

ELEMENTOS PRESENTES EN LAS TRES PANTALLAS
1. Barra superior fija con el nombre "Sánchez & Sánchez" a la izquierda y, en celular,
   un botón hamburguesa a la derecha que despliega el menú (Nosotros, Carta, Cafetería,
   Delivery, Ubicación). En escritorio esos links van en fila dentro de la barra.
2. Sección "Delivery y Pedidos": cuatro tarjetas cuadradas con los logos de WhatsApp,
   Mercado Pago, Rappi y PedidosYa. Es la principal acción de conversión del sitio.
3. Sección "Visitanos": dirección, horarios (Lun a Vie 7:00-00:00, Sáb y Dom 8:00-01:00),
   teléfono 11 5927-3756, Instagram, TikTok y un mapa embebido.
4. Pie de página.
5. Solo en celular: una barra fija abajo con dos botones de acceso rápido
   ("Ver carta" y "Pedir por WhatsApp").
```

---

## PANTALLA 1 — Home

```
Diseñá la pantalla de inicio con estas secciones, en este orden:

1. HERO
   Título grande "Sánchez & Sánchez", bajada: "Pizzería y Cafetería en el corazón de
   Almagro, con el sabor de siempre desde hace más de 20 años." Una foto grande del
   frente del local de noche (cartel rojo iluminado). Un distintivo chico que diga
   "Almagro · CABA" y otro que diga "+20 años".
   Cuatro botones de acción: "Ver la Carta", "Cafetería", "Menú del Día", "Delivery".

2. CINTA ANIMADA
   Una franja horizontal oscura con texto que se desplaza: "Pizza a la piedra ·
   Empanadas caseras · Cafetería · Menú del día · Delivery".

3. NUESTRA HISTORIA
   Dos fotos (una grande del frente del local, una más chica superpuesta con el equipo)
   y a su lado tres párrafos sobre los más de 20 años en Almagro, las pizzas a la piedra
   y las empanadas caseras, y el rincón de cafetería.

4. RESEÑAS DEL BARRIO
   Cuatro testimonios reales de Google con 5 estrellas, nombre del autor y la etiqueta
   "Local Guide". Sobre fondo oscuro. En celular tienen que ir apilados uno debajo del
   otro, nunca superpuestos.

5. MENÚ DEL DÍA
   Precio destacado $20.000, texto "Plato principal + bebida + café o postre".
   Cinco pestañas (Lunes a Viernes) que cambian la lista de 4 platos de ese día.
   La del día actual aparece seleccionada sola. Dos tarjetas extra: "Opción Invierno"
   y "Opción Especial" ($21.000). Aclaración: "Lunes a Viernes de 12 a 16 hs · Solo efectivo".

6. DELIVERY Y PEDIDOS (ver Bloque A)
7. VISITANOS (ver Bloque A)
8. PIE DE PÁGINA
```

---

## PANTALLA 2 — Carta

```
Diseñá la pantalla de la carta de la pizzería. Es la pantalla más importante y más larga
del sitio: tiene 62 productos. El desafío de diseño es que se pueda recorrer sin perderse.

ESTRUCTURA
1. Encabezado con fondo oscuro: arriba "La carta" en letra chica y el título "Nuestra Carta".

2. Barra de categorías fija (sticky) justo debajo de la barra superior, que se queda
   visible al scrollear: tres pestañas redondeadas "Comidas", "Pizzas", "Empanadas".
   Al tocar una, lleva a esa sección; la pestaña de la sección que estás mirando se
   resalta sola. En celular la barra scrollea horizontalmente.

3. SECCIÓN COMIDAS, con estas subcategorías:
   - "Minutas + Guarnición" (7 productos) — aclaración: "A elección: provenzal, ajillo,
     verdeo u oreganato"
   - "Ensaladas" (6)
   - "Tartas" (4) — $11.500 c/u
   - "Lomito al Pan" (4) — "Chivito uruguayo, con papas fritas"
   - "Lomito al Plato" (3) — "Con papas fritas"

4. SECCIÓN PIZZAS:
   - "Las de Siempre" (11) — precios "Chica / Grande"
   - "Las de Hoy" (11) — precios "Chica / Grande"
   - "Porciones" (6) — precio único

5. SECCIÓN EMPANADAS (10) — $3.000 c/u

TARJETA DE PRODUCTO (es el elemento que más se repite, cuidalo)
Foto arriba (proporción 4:3, la foto llena todo el ancho), y debajo: nombre, una
descripción corta de ingredientes, y el precio destacado en terracota.
Algunos productos todavía no tienen foto: diseñá también la variante SIN foto, que no
tiene que verse rota ni como un hueco, sino como una tarjeta de solo texto que convive
bien con las otras en la misma grilla.
Las pizzas tienen DOS precios (chica y grande): mostralos diferenciados y claros, con
una etiqueta chiquita que diga qué es cada uno. Que no se lea como un solo precio raro.
Grilla: 1 columna en celular, 2 en tablet, 3 en escritorio.

VENTANA DE DETALLE (modal)
Al tocar una tarjeta se abre una ventana con la foto más grande, el nombre, la
descripción completa y el precio. Se cierra con una X, tocando el fondo oscurecido,
o con la tecla Escape.

6. DELIVERY Y PEDIDOS, VISITANOS y PIE (ver Bloque A)
```

---

## PANTALLA 3 — Cafetería

```
Diseñá la pantalla de la cafetería. A diferencia de la carta, acá los productos son
muchos ítems de texto con precio (sin foto), así que se organizan en acordeones.

1. Encabezado con fondo oscuro y una foto de café con medialunas de fondo atenuada.
   Arriba "Para desayunar o hacer una pausa" y el título "Cafetería".

2. CARRUSEL "Productos nuevos"
   Seis fotos verticales (proporción 3:4) que se desplazan solas de forma continua:
   Bagels, Waffles, Croissants rellenos, Muffins, Tortas, Volcán de Chocolate.
   Con flechas para moverlo a mano, y que también se pueda arrastrar con el dedo.

3. "Nuestra Cafetería" — ocho secciones plegables (acordeón), en este orden:
   - "Promos — Todo el Día" (4 ítems) — abierta por defecto, las otras cerradas
   - "Cafés e Infusiones" (11)
   - "Especiales de la Casa" (2)
   - "Licuados y Bebidas" (7)
   - "Tortas y Dulces" (6)
   - "Panadería y Facturas" (8)
   - "Waffles" (1)
   - "Tostados y Panes" (8)

   Cada sección: encabezado con el nombre y un ícono + que rota a × al abrirse.
   Adentro, una lista donde cada ítem tiene nombre a la izquierda, precio en terracota
   a la derecha, y una línea de puntos uniéndolos (estilo carta de restaurante).
   Algunos ítems llevan una aclaración chica en itálica debajo del nombre
   (ej: "choco, crema, canela").
   La sección de Promos además tiene dos tarjetas destacadas de combos de desayuno
   ($8.000 y $10.000).

4. DELIVERY Y PEDIDOS, VISITANOS y PIE (ver Bloque A)
```

---

## PANTALLA 4 — Error 404 (opcional)

```
Diseñá una página de error 404 simple y con la identidad del sitio: un mensaje breve
("No encontramos esta página"), una explicación de una línea, y tres botones:
"Ir al inicio", "Ver la carta" y "Cafetería".
```

---

# Restricciones técnicas (NO mandar a Stitch — leer al integrar)

El sitio es **HTML + CSS + JavaScript puro**, sin framework ni build, publicado en GitHub
Pages detrás de Cloudflare. Cuando llegue el diseño de Stitch, hay que adaptarlo a esto:

| Restricción | Por qué | Qué implica |
|---|---|---|
| **CSP estricta sin `unsafe-inline`** | Protección contra XSS, ya implementada y auditada | **No se pueden usar atributos `style=""` en el HTML.** Todo estilo va en el bloque `<style>` o en clases. Después de cada cambio hay que correr `python3 docs/scripts/regen_csp.py` |
| **Fuentes self-hosteadas** | Privacidad y CSP: el sitio no hace ningún pedido a Google | Si Stitch propone una tipografía nueva, hay que descargar los `.woff2` a `assets/fonts/` y sumarla a `fonts.css`. No usar `<link>` a fonts.googleapis.com |
| **Sin frameworks** | El sitio no tiene build ni dependencias | Si el diseño viene con Tailwind o React, hay que traducirlo a CSS plano |
| **Imágenes optimizadas** | Se bajó de 107 MB a 7,4 MB | Fotos de producto a 900 px máx, JPEG calidad 82. Hay un script de referencia en el historial |
| **Mobile-first probado** | El 90% del tráfico es celular | Se arreglaron bugs reales de hitbox y de menú. Conviene revalidar con el script `sec_verify.py` |
| **Accesibilidad** | Ya está implementada | Mantener contraste 4.5:1, `aria-expanded` en acordeones y menú, foco visible, soporte de teclado y zonas táctiles de 44 px mínimo |

**Contenido que NO hay que cambiar:** nombres de productos, precios, descripciones,
teléfono, dirección, horarios y los enlaces de delivery. El refactor es visual.
