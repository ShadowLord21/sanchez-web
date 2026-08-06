# Sánchez & Sánchez — sitio web

Landing one-page para Sánchez & Sánchez, pizzería y cafetería en Almagro (CABA), más de 20 años en el barrio.

## Qué es esto

Sitio estático (sin backend) hecho a partir del brief en `brief-web.md`. Ese archivo tiene la especificación completa: identidad de marca, paleta de colores, tipografías, secciones y **todo el contenido de la carta con precios**. Ante cualquier duda de contenido/diseño, `brief-web.md` es la fuente de verdad.

## Stack

HTML + CSS + JS vanilla (sin frameworks, sin build step, sin npm). Es intencional: es una landing de una sola página sin estado complejo ni datos dinámicos, así que un framework tipo React solo agregaría complejidad de tooling sin beneficio real.

- `index.html` — estructura y contenido de todas las secciones (hero, sobre nosotros, carta, delivery, ubicación/horarios, footer). Incluye JSON-LD (schema.org `Restaurant`) y meta tags Open Graph.
- `styles.css` — paleta e identidad del brief (marfil `#F7F2E9`, azul marino `#1C2B3A`/`#20303F`, terracota `#B24A2E`, dorado `#C9A24B`), mobile-first, Google Fonts (Cormorant Garamond + Montserrat).
- `script.js` — menú hamburguesa mobile, pestañas de la carta (Comidas/Pizzas/Empanadas/Cafetería/Menú del Día/Promos), y manejo de `#menu` como hash estable para el QR.
- `img/` — actualmente tiene **placeholders SVG** (`hero-bg.svg`, `about.svg`, `og-cover.svg`) generados a mano, con comentarios en `index.html` marcando dónde reemplazar por fotos reales. Pendiente: el dueño tiene que mandar fotos reales del local/comida.

## Deploy

- Repo: **https://github.com/ShadowLord21/sanchez-web** (público). Push directo a `main`, sin CI/CD ni Actions.
- Publicado con **GitHub Pages** (legacy build, sirve desde `main` / raíz). `.nojekyll` está presente para que Pages sirva los archivos tal cual sin pasarlos por Jekyll.
- `gh` CLI está instalado en `C:\Program Files\GitHub CLI\gh.exe` y autenticado como `ShadowLord21` (puede no estar en el PATH de todas las shells — usar ruta completa si `gh` no se reconoce).
- **Dominio propio**: `sanchez-sanchez.com.ar`, registrado en NIC Argentina (pago, ~$8.500 ARS). El archivo `CNAME` en la raíz del repo lo configura como dominio personalizado de GitHub Pages.
  - Nameservers delegados a **Cloudflare** (proxy/orange-cloud activado). Los registros A/AAAA/CNAME hacia las IPs de GitHub Pages están cargados en la zona de Cloudflare, no en el panel de NIC Argentina.
  - IPs de GitHub Pages usadas: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (+ AAAA equivalentes).
  - HTTPS lo sirve Cloudflare (certificado de Cloudflare, no el automático de GitHub — `https_enforced` en la API de Pages puede figurar en `false`, es esperado por el proxy).
  - **Nota**: por ser un dominio recién registrado, algunas redes con filtrado de seguridad DNS (p. ej. Palo Alto Networks Advanced DNS Security, común en redes universitarias/corporativas) lo bloquean por política de "newly registered domain" hasta que el dominio gana reputación. No es un problema del sitio — confirmado funcionando con `200 OK` vía consulta directa a Cloudflare.
  - El dueño quería originalmente `sanchezysanchez.com.ar` pero estaba ocupado por terceros; `sanchez-sanchez.com.ar` fue la alternativa elegida (los dominios no admiten el símbolo `&`).

## Pendientes conocidos

- Reemplazar `img/hero-bg.svg`, `img/about.svg`, `img/og-cover.svg` por fotos reales cuando el dueño las mande.
- En `brief-web.md` hay productos nuevos de cafetería (croissants rellenos, muffins, waffles, bagels, ciabattas) sin precio definido todavía — no están en la carta hasta que los definan.
- QR: una vez que el dominio esté completamente destrabado en todas las redes, el QR a la carta debe apuntar a `https://sanchez-sanchez.com.ar/#menu`.

## Preferencias del dueño (para tener en cuenta)

- No quiere reescribir esto en React ni sumar framework — prefiere mantenerlo simple mientras el sitio sea solo informativo/vidriera.
- Evaluó (y por ahora descartó) construir un sistema de pedidos propio tipo app de delivery; sigue usando WhatsApp/Mercado Pago Delivery/Rappi/PedidosYa como canales de pedido.
