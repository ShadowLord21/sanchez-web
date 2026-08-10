# Brief de rediseño — Web Sánchez & Sánchez (estilo tipo Loro)

> Pegale esto a **Claude Code** en el proyecto de la web y pedile: *"Leé brief-rediseno-loro.md y rediseñá la web según el brief. Primero mostrame el plan y esperá mi OK."*

---

## 1. Objetivo

Rediseñar la web **one-page** del restaurante Sánchez & Sánchez (pizzería y cafetería en Almagro) para que tenga un look **moderno, cálido y muy visual**, inspirado en el estilo del sitio de **Loro** (loroeats.com): fondo crema, acento terracota, y **fotos grandes de comida intercaladas por todos lados**.

Se rediseña **el aspecto, la distribución y la experiencia**, y se agregan imágenes e interactividad. **NO se cambia la información** (textos, nombres, precios, descripciones, links, horarios, contacto): esa sale del contenido que ya existe en el proyecto y queda igual.

---

## 2. Inspiración (qué replicar del estilo Loro, con nuestra marca)

Adoptar los **patrones de diseño y de experiencia**, NO copiar sus fotos, logo ni textos (eso es de ellos). Lo que queremos imitar:

- **Fondo crema cálido** + acento **terracota**, tipografía con carácter.
- **Fotos grandes en formato vertical (portrait), intercaladas cada pocas secciones**, con una **leyenda en itálica** debajo y, cuando corresponde, un pequeño sello **"Nuevo"**. Esto es lo central: la web tiene que sentirse "llena de fotos", no un listado plano.
- **Menú dividido en secciones** claras; cada ítem con **nombre + precio en la misma línea** y **descripción debajo** en letra más chica.
- **Pestañas** arriba del menú para cambiar de categoría y una barra **"Ir a:"** (jump-to) para saltar a cada sección con scroll suave.
- **Botones de pedido/delivery siempre visibles** (sticky).
- Un bloque simpático tipo **"Cómo pedir"** con pasos (aprovechando el QR).
- **Footer** con newsletter (opcional), logo, redes y datos.

---

## 2.b Analizá la referencia PRIMERO (hacelo antes de diseñar)

Antes de escribir nada, estudiá la página de referencia para entender bien el estilo:

- **URL:** https://www.loroeats.com/locations/houston/kirby/menu/
- Traela con **WebFetch** para ver su estructura: cómo ordenan las secciones, cómo intercalan las fotos, cómo muestran nombre/precio/descripción.
- Si tenés una **herramienta de navegador disponible** (Playwright / Chrome DevTools MCP): abrí la página, sacá **capturas en desktop y en mobile**, y analizá el layout, el espaciado, el tamaño y la ubicación de las fotos verticales, la tipografía, los sellos "Nuevo", las pestañas y las transiciones.
- Si **no** tenés navegador disponible: pedile al dueño **3-4 capturas** de la página (desktop y celular) para tener la referencia visual exacta, y esperá esas imágenes antes de definir el diseño.

Recordá: se replica el **estilo y la estructura**, NO las fotos, el logo ni los textos de Loro.

## 3. Skills a usar

Aprovechá al máximo las skills instaladas **"UI-UX-PRO-MAX"** y la de **front-end design de Anthropic**. Si está disponible, al final corré la auditoría **web-design-guidelines de Vercel** y corregí lo prioritario.

---

## 4. Estilo visual

- **Paleta:** fondo marfil/crema `#F7F2E9`, acento terracota `#B24A2E` (y `#9C4A2E`), azul marino para texto fuerte `#1C2B3A`, dorado para detalles `#C9A24B`.
- **Tipografías:** títulos **Cormorant Garamond** (elegante), cuerpo **Montserrat**. Mantener coherencia con las cartas impresas.
- **Fotos:** grandes, verticales, apetitosas, con leyenda en itálica. (Ver punto 8: por ahora placeholders.)
- **Detalles:** líneas finas doradas, sellos "Nuevo" en terracota, hover en botones, transiciones suaves, sin recargar.

---

## 5. Estructura de la web (one-page, secciones en orden)

1. **Hero / Portada** — nombre Sánchez & Sánchez, bajada ("Pizzería y Cafetería en Almagro · +20 años"), una foto grande de fondo (placeholder) y botones **Ver la carta** y **Pedir delivery**.
2. **Cómo pedir** — 2-3 pasos simples (ej. "Escaneá el QR / Mirá la carta / Pedí en el mostrador o por delivery"), estilo tarjetas.
3. **Sobre nosotros** — 1-2 párrafos cálidos sobre los 20 años en Almagro (usar el texto que ya está).
4. **Carta / Menú**  → **id="menu"** (destino del QR, NO cambiar):
   - Pestañas: **Comidas · Pizzas · Empanadas · Cafetería · Menú del Día · Promos**.
   - Barra "Ir a:" con las secciones.
   - Ver detalle del patrón en el punto 6.
5. **Delivery y pedidos** → **id="delivery"** — botones grandes (abren en pestaña nueva): WhatsApp, Mercado Pago, Rappi, PedidosYa.
6. **Ubicación y horarios** → **id="contacto"** — dirección (Av. Rivadavia 3399), mapa de Google embebido, horarios (Lun-Vie 7-00, Sáb-Dom 8-1), teléfono, Instagram.
7. **Footer** — logo/nombre, redes, "Hacemos pedidos para llevar", y newsletter opcional.

---

## 6. Patrón de la Carta (el corazón del rediseño)

**Tarjeta de producto — estilo "Featured Items" de Loro (referencia clave):**
- Mostrar los productos en una **grilla de tarjetas**: 3 por fila en desktop, 2 en tablet, 1 en mobile. Espaciado generoso.
- Anatomía de cada tarjeta:
  - **Foto grande arriba**, ocupando todo el ancho de la tarjeta, esquinas superiores redondeadas (relación aprox. 4:3).
  - **Cuerpo blanco** debajo (esquinas inferiores redondeadas, sombra suave), sobre el fondo crema de la sección.
  - **Nombre** del producto en negrita.
  - **Descripción** en 1-2 líneas, en color de acento, **recortada con "…"** si es larga.
  - **Precio** abajo a la izquierda.
  - **Botón circular "+"** abajo a la derecha.
- **Interacción:** al tocar el "+" (o cualquier parte de la tarjeta) se abre una **vista ampliada (modal/overlay)** con la **foto grande, la descripción completa y el precio**. IMPORTANTE: NO es un carrito de compra (no vendemos online); el "+" es "ver más". El modal se cierra fácil (X o clic afuera) y anda perfecto en celular.
- Además de las tarjetas, intercalá **fotos verticales grandes con leyenda** entre secciones (ver punto siguiente), para el efecto "muy visual" de Loro.
- **Fotos intercaladas al estilo Loro:** entre las secciones (y dentro de las más largas) insertar **fotos verticales grandes con leyenda en itálica**, no solo dentro de las tarjetas. La página tiene que sentirse muy visual.
- Sellos **"Nuevo"** en los productos nuevos (bagels, waffles, croissants rellenos, muffins, lemon pie, volcán de chocolate, etc.).
- Mantener el contenido/precios exactamente como están hoy en el proyecto.

---

## 6.c Componentes extra tipo Loro (sumar)

- **Destacados (carrusel arriba del menú):** una fila/carrusel horizontal de **fotos verticales grandes** con leyenda en itálica y sello **"Nuevo"** cuando corresponda, tipo la sección "Featured" de Loro. Acá van los **productos estrella, novedades y promos** (ej.: pizzas top, empanadas, torres a futuro, combos de desayuno, lemon pie/volcán nuevos). Debe scrollear con el dedo en mobile.
- **Pestañas de categoría (sticky):** arriba del menú, pestañas para cambiar de grupo tipo Loro (Food/Drink). Para nosotros: **Comidas · Pizzas · Empanadas · Cafetería · Menú del Día · Promos**. Que queden fijas al scrollear y salten con scroll suave. Debajo, opcionalmente, la barra secundaria "Ir a:" para sub-secciones.
- **Bloque "Cómo pedir":** 3 pasos simples y visuales, tipo el "How to Loro". Ejemplo:
  1. Escaneá el QR o mirá la carta acá.
  2. Elegí lo tuyo (comida, pizza, café).
  3. Pedí en el mostrador o por delivery (Rappi / Mercado Pago / PedidosYa / WhatsApp).
  Con iconos simples y el mismo estilo cálido.

## 7. Menú del Día (dentro de la carta)

- Mostrar automáticamente el menú del **día actual** detectando el día con JavaScript (ej.: si hoy es jueves, muestra jueves).
- Un selector/pestañas para ver los otros días (lunes a viernes).
- Como es solo Lun-Vie: si es sábado o domingo, mostrar un aviso amable ("El menú del día está disponible de lunes a viernes") y dejar el selector para navegar los días.

---

## 8. Fotos (importante)

- Por ahora **usar placeholders** claramente identificados (con un texto/overlay tipo "FOTO: [producto]") y dejar **comentado en el código dónde va cada foto real**, para reemplazarlas fácil después.
- El dueño va a subir las fotos reales una vez terminado el diseño.
- No uses imágenes de Loro ni de terceros; solo placeholders neutros o de stock libre marcados como temporales.

---

## 9. PROTECCIONES (antes de empezar)

1. Hacé un **commit de git** del estado actual con el mensaje "backup antes de rediseño estilo Loro". Si no hay repo git, inicializalo y commiteá.
2. **No modifiques el contenido informativo**: textos, nombres, precios, descripciones, links de delivery, horarios, dirección, teléfono y redes quedan EXACTAMENTE igual.
3. Mantené estable la **URL/ancla del QR** (`/#menu`).
4. No toques la config de deploy ni archivos de dominio/DNS (ej. el archivo **CNAME**).

---

## 10. Cómo trabajar

5. Primero mostrame un **PLAN**: la nueva estructura, cómo vas a resolver las fotos intercaladas, el modal de producto y la lógica del menú del día. **Esperá mi OK** antes de escribir código.
6. Trabajá **sección por sección**; al terminar cada una, pará y contame qué hiciste.
7. **Mobile-first**: tiene que verse y funcionar impecable en celular (mucha gente entra por el QR).
8. Dejá el **preview local con recarga automática** andando (Live Server o dev server) y pasame la URL para ir viendo.
9. Si dudás si algo es "contenido" o "diseño", preguntame antes de cambiarlo.

---

## 11. Al terminar

10. Mostrame un **resumen + diff** confirmando que ningún texto, precio, link, horario ni dato de contacto fue modificado; que solo cambió el diseño, la estructura y se agregaron fotos (placeholders) e interactividad.
11. Verificá: botones de delivery funcionando, modal abre/cierra bien, menú del día muestra el día correcto, nada se rompe en mobile, y el ancla `#menu` intacta.
12. (Opcional) Corré la auditoría de **web-design-guidelines de Vercel** y corregí lo prioritario (accesibilidad y performance primero).

---

**Nota de derechos:** el diseño se inspira en la estructura y el estilo de Loro, pero se construye 100% original con la marca, el contenido y (a futuro) las fotos de Sánchez & Sánchez. No se copian imágenes, logo ni textos de Loro.
