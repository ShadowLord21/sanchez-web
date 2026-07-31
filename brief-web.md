# Brief de proyecto — Sitio web Sánchez & Sánchez

> Este documento es la especificación para construir la web. Pegáselo a **Claude Code** y pedile: *"Construí esta web one-page según el brief, en un proyecto listo para publicar."*

---

## 1. Resumen

- **Negocio:** Sánchez & Sánchez — Pizzería y Cafetería en Almagro (CABA). Más de 20 años en el barrio.
- **Tipo de sitio:** One-page (una sola página con secciones y navegación con scroll suave).
- **Objetivo principal:** presencia e imagen de marca profesional + mostrar la carta con precios + facilitar el pedido por delivery.
- **Mobile-first:** la mayoría va a entrar desde el celular (incluido el QR que apunta a la carta), así que el diseño tiene que verse impecable en teléfono antes que en desktop.
- **Sin backend:** HTML/CSS/JS estático. Idealmente un `index.html` autocontenido o un proyecto simple (index.html + styles.css + script.js + /img).

---

## 2. Identidad de marca y estilo

Estilo **moderno para web** pero basado en la identidad de las cartas (que ya existen). Elegante, cálido, apetitoso.

**Paleta**
- Fondo marfil: `#F7F2E9`
- Azul marino (texto fuerte / secciones oscuras): `#1C2B3A` / `#20303F`
- Terracota (acento principal): `#B24A2E`
- Terracota apagado / marrón: `#9C4A2E`
- Dorado (detalles/líneas): `#C9A24B`
- Gris texto: `#2b3a47`

**Tipografías** (Google Fonts)
- Títulos: **Cormorant Garamond** (700 / 600, y itálica para subtítulos).
- Cuerpo / UI: **Montserrat** (300–600).

**Detalles visuales**
- Secciones alternando fondo marfil y bandas azul marino.
- Acentos en terracota y líneas finas doradas.
- Fotos grandes de comida (usar placeholders si no hay fotos aún; dejar comentado dónde reemplazar).
- Botones con hover, navegación fija arriba (sticky) con scroll suave a cada sección.

---

## 3. Secciones (en orden)

### a) Hero / Portada
- Nombre: **Sánchez & Sánchez**
- Bajada: *"Pizzería y Cafetería en Almagro · desde hace más de 20 años"*
- Botones: **Ver la carta** (scroll a #menu) y **Pedir delivery** (scroll a #delivery).
- Imagen de fondo apetitosa (pizza / mesa servida) con overlay para legibilidad.

### b) Sobre Nosotros
- Texto sobre los 20 años en Almagro, la pizza, las empanadas y la cafetería; un lugar de barrio para familias y vecinos. (Redactar 1–2 párrafos cálidos; puedo ajustarlos después.)

### c) Carta / Menú  → **id="menu"** (IMPORTANTE: este ancla es el destino del QR)
- Mostrar la carta **con precios** (detalle completo en la sección 5).
- Organizada por categorías con pestañas o navegación interna: **Comidas · Pizzas · Empanadas · Cafetería · Menú del Día · Promos**.
- Que sea muy cómoda de leer en el celular (es lo que la gente va a ver al escanear el QR).

### d) Delivery y Pedidos → **id="delivery"**
Botones grandes con los links (abren en pestaña nueva):
- **WhatsApp:** https://wa.me/5491159273756?text=Hola!%20Vi%20su%20perfil%20en%20Instagram%20y%20quer%C3%ADa%20hacer%20una%20consulta%20o%20pedido.
- **Mercado Pago Delivery:** https://mpago.li/29KUdv2
- **Rappi:** https://www.rappi.com.ar/restaurantes/246491-sanchez-y-sanchez
- **PedidosYa:** https://www.pedidosya.com.ar/restaurantes/buenos-aires/sanchez-sanchez-pizzeria-cafeteria-6809ea11-e8ea-4e61-ba31-1dc91a1868e1-menu?origin=shop_list

### e) Ubicación y Horarios → **id="contacto"**
- Dirección: **Av. Rivadavia 3399, CABA** (Almagro / Balvanera).
- Mapa embebido de Google Maps: https://maps.app.goo.gl/sHR2jj1Aox3E63NW9
- **Horarios:** Lunes a Viernes de 7:00 a 00:00 · Sábados y Domingos de 8:00 a 1:00.
- Teléfono: **11 5927-3756**
- Instagram: **@sanchezysanchez_ok** (link https://instagram.com/sanchezysanchez_ok)
- TikTok: (dejar botón preparado)

### f) Footer
- Logo/nombre, dirección, teléfono, redes, y un "Hacemos pedidos para llevar".

---

## 4. QR a la carta

- La sección de la carta debe tener el ancla **`#menu`** estable.
- Una vez publicada la web (con su URL definitiva, ej. `https://sanchezysanchez.com`), el QR se genera apuntando a **`https://TU-DOMINIO/#menu`** para que la gente escanee y caiga directo en la carta.
- Sugerencia: que la web recuerde el hash y abra la sección Carta directamente si se entra con `/#menu`.
- El QR lo puedo generar yo apenas tengas la URL final publicada.

---

## 5. Contenido de la carta (con precios)

### COMIDAS

**Minutas + Guarnición** *(a elección: provenzal, ajillo, verdeo u oreganato)*
- Milanesa — $21.000
- Milanesa Napolitana — $23.500
- Suprema — $18.500
- Suprema Napolitana — $22.000
- Pollo Deshuesado — $17.000
- Pollo Argentino — $19.000
- Pollo a la Mostaza — $21.500

**Ensaladas**
- Caesar — $17.000 (pollo, lechuga, croutons, parmesano, aderezo caesar)
- Brie — $19.500 (rúcula, queso brie, tomates secos, panceta crocante)
- Lucero — $18.000 (pollo, rúcula, tomates secos, huevo, cebolla colorada)
- Lucero con Atún — $19.500
- Amelia — $19.500 (atún, lechuga, zanahoria, huevo, arroz, cebolla colorada)
- Caprese — $18.000 (mozzarella, tomate, albahaca, aceitunas)

**Tartas** — $11.500 c/u: Jamón y Queso · Calabaza y Mozzarella · Pascualina · Vegetales y Pollo

**Lomito al Pan** *(chivito uruguayo, con papas fritas)*
- Clásico — $26.000 · Natural — $26.000 · Canadiense — $27.000 · De la Casa — $27.000

**Lomito al Plato** *(con papas fritas)*
- Natural — $25.000 · De la Casa para 1 — $26.000 · De la Casa para 2 — $32.000

### PIZZAS (Chica / Grande)

**Las de Siempre**
- Mozzarella — $20.000 / $24.000
- Jamón — $27.000 / $31.000
- Morrón — $23.000 / $30.000
- Jamón y Morrón — $24.500 / $33.000
- Napolitana — $25.000 / $33.000
- Provolone — $24.000 / $33.000
- Fugazzeta — $24.000 / $33.000
- Fugazzeta Rellena Gourmet — $34.000 / $43.000
- Fugazza — $18.000 / $22.000
- Cuatro Quesos — $25.000 / $34.500
- Queso Brie — $27.000 / $33.000

**Las de Hoy**
- Rústica — $24.500 / $33.000
- Caprese — $26.500 / $32.000
- Parma — $26.500 / $29.500
- Especial "Sánchez" — $28.000 / $34.000
- Espinaca con Salsa Blanca — $26.500 / $30.500
- Queso Azul Argentino — $26.500 / $30.000
- Carbonara — $28.000 / $30.500
- Vegetariana — $25.000 / $29.000
- Papas a Caballo — $27.500 / $33.000
- Peperoni — $25.000 / $33.000
- Calabresa — $26.000 / $33.000

**Empanadas** — $3.000 c/u: carne · carne picante · carne cheeseburger · roquefort · pollo · jamón y queso · choclo · cebolla y queso · verdura y queso · caprese · picante y jamón

**Porciones**: Mozzarella $3.300 · Napolitana $3.700 · Jamón y Morrón $4.100 · Fugazzeta $4.800 · Faina $1.200 · Faina Rellena $1.500

### CAFETERÍA

**Cafés e infusiones**: Expreso $2.700 · Americano $2.900 · Ristretto $2.000 · Doble $3.600 · Café con leche $3.200 · Capuccino $5.000 · Submarino $5.500 · Leche $1.000 · Extra crema $1.500 · Té $2.300 · Té con 2 medialunas $3.000
**Especiales**: Capuccino "Sánchez" $7.000 · Capuccino Italiano $7.000
**Panadería**: Medialunas/facturas $900 · Medialunas rellenas j&q $2.300
**Tortas y dulces**: Brownie manzana $7.500 · Brownie chocolate $7.500 · Chocotorta $7.500 · Cheesecake $7.500 · Tiramisú $7.500
**Tostados**: Tostado mixto triple $7.500 · Italiano en miga $10.000 · Olímpico en miga $10.000 · Jamón crudo y queso $15.000
**Promos cafetería**: Armá tu Tazón (café con leche + acompañamiento) desde $7.000 · Café c/leche + 3 medialunas $4.900 · Americano + medialunas j&q $5.100 · Licuado + torta $11.500 · C/leche + tostadas, queso y jugo $5.100

> Nota: hay productos nuevos de cafetería (croissants rellenos, muffins, waffles, bagels, ciabattas) que **aún no tienen precio definido**. Dejarlos fuera de la web por ahora o marcarlos "próximamente"; se agregan cuando tengan precio.

### MENÚ DEL DÍA — $20.000 *(Lunes a Viernes de 12 a 16 hs · solo efectivo)*
Plato principal + bebida + café o postre. Rota por día (4 opciones + opción invierno). Opción Especial: Bife a Caballo + Papas — $21.000.

### PROMOS
- Crispi para 2 — $24.000 · Crispi para 4 — $34.000
- Imperdible (2 pizzas chicas + bebida 1,75 L) — $38.000
- Hamburguesa completa + papas + bebida — $18.000
- Reina Empanadas (docena) — $29.000 · Super Lunes (docena + 3 de regalo) — $29.000
- Dulce Tentación (docena de medialunas) — $8.300
- Happy Hour: 20 a 22 hs, 2x1 en tragos y chopps · (Lun a Mié 18 a 19 hs — $6.300)

---

## 6. Requisitos técnicos

- Responsive / mobile-first. Testear en pantalla de celular.
- Navegación sticky con scroll suave a #menu, #delivery, #contacto.
- Botones de delivery abren en pestaña nueva (`target="_blank" rel="noopener"`).
- Mapa de Google embebido.
- SEO básico: `<title>`, meta description, Open Graph (para que se vea bien al compartir), y datos de negocio local (schema.org LocalBusiness/Restaurant con dirección, horarios y teléfono).
- Performance: imágenes optimizadas, fuentes cargadas eficientemente.
- Dejar comentado en el código dónde reemplazar fotos y textos.

## 7. Publicación (para después)
- Opciones simples y gratuitas: **Netlify**, **Vercel** o **GitHub Pages**.
- Una vez publicada, pasame la URL y genero el **QR → /#menu**.
