# PRD — Sitio Web Sánchez & Sánchez

**Fecha:** 2026-09-04
**Estado:** En desarrollo activo (contenido e imágenes en carga progresiva)

---

## 1. Resumen del producto

Sitio web institucional y de carta digital para **Sánchez & Sánchez**, pizzería y cafetería ubicada en Av. Rivadavia 3399, Almagro/Balvanera (CABA), con más de 20 años en el barrio.

El sitio cumple tres funciones principales:
1. **Vidriera de marca** — comunicar la identidad del local (historia, ambiente, ubicación).
2. **Carta digital navegable** — mostrar todos los productos de pizzería con foto, descripción y precio.
3. **Canal de conversión** — dirigir al usuario a pedir por WhatsApp, Mercado Pago, Rappi o PedidosYa, o a visitar el local.

No es un e-commerce: no hay carrito ni pago dentro del sitio. Cada canal de pedido redirige a una app/servicio externo.

---

## 2. Usuarios objetivo

- **Clientes del barrio** que buscan el menú, el horario o cómo pedir delivery, mayormente **desde el celular**.
- **Clientes nuevos** que llegan por redes sociales o búsqueda y quieren evaluar la propuesta (fotos de platos, precios, ubicación) antes de ir o pedir.
- **El dueño/administrador del local**, que actualiza fotos, precios y descripciones de productos con frecuencia (perfil no técnico).

Prioridad de diseño: **mobile-first**. La mayoría de las interacciones (tocar botones, deslizar sliders, abrir el menú) ocurren en pantallas táctiles chicas.

---

## 3. Arquitectura del sitio

Sitio estático multi-página (HTML + CSS + JS embebido, sin build ni framework), pensado para hosting simple (GitHub Pages, dominio propio vía `CNAME`).

```
estilo-floria/
├── index.html              → Home
├── carta/index.html        → Carta (pizzería)
└── cafeteria/index.html    → Cafetería

assets/
├── img/                    → fotos de productos, organizadas por categoría
│   ├── empanadas/, ensaladas/, lomitos/, minutas/, pizzas/, porciones/, tartas/
│   ├── cafeteria-nuevos/   → fotos del slider "Productos nuevos"
│   ├── home/               → fotos del Home (hero, "Nuestra historia")
│   ├── meta/               → imagen para redes sociales (og:image)
│   └── placeholders/       → placeholders todavía en uso
├── fotos/                  → fotos generales del local (interior, cafetería)
├── logos/                  → logos de apps de delivery (MercadoPago, Rappi, PedidosYa)
└── pdf/                    → carta de cafetería en PDF (referencia)
```

Cada página es autocontenida (su propio `<style>` y `<script>`), replicando el mismo sistema de diseño para consistencia.

---

## 4. Páginas y funcionalidad

### 4.1 Home (`/estilo-floria/`)
- **Hero**: título, bajada, foto del frente del local, 4 botones de acción (Ver la Carta, Cafetería, Menú del Día, Delivery).
- **Marquee** decorativo con las especialidades del local.
- **Nuestra Historia**: texto institucional + foto principal (frente del local) + foto flotante (equipo).
- **Reseñas del barrio**: collage de 4 testimonios reales (Google), apilado en mobile/tablet para evitar superposición, tipo "collage" solo en desktop ancho.
- **Menú del Día**: precio, opciones por día de la semana (selector Lunes a Viernes, con detección automática del día actual), opción especial e invierno.
- **Delivery y Pedidos**: 4 tarjetas (WhatsApp, Mercado Pago, Rappi, PedidosYa) con logos reales.
- **Visitanos**: dirección, horarios, teléfono, redes sociales, mapa embebido de Google Maps.
- **Footer** + **barra sticky de pedido** (mobile): accesos rápidos a Carta y WhatsApp, siempre visible.

### 4.2 Carta (`/estilo-floria/carta/`)
- **Slider "Promos para compartir"**: **desactivado temporalmente** (comentado en el HTML) hasta contar con fotos reales de las promociones.
- **Pestañas sticky** de categorías (Comidas / Pizzas / Empanadas) con scroll suave y resaltado automático según la sección visible.
- **Grillas de productos** por categoría, cada tarjeta con foto (o sin foto si todavía no se cargó), nombre, descripción y precio; al tocarla abre un **modal** con el detalle ampliado.
  - Pizzas con precio doble (Chica/Grande) muestran ambos precios etiquetados, en la tarjeta y en el modal.
  - Categorías: Minutas + Guarnición, Ensaladas, Tartas, Lomito al Pan, Lomito al Plato, Pizzas ("Las de Siempre" y "Las de Hoy"), Porciones, Empanadas.
- **Delivery y Pedidos**: mismas 4 tarjetas que en el Home (unificadas en diseño).
- **Contacto**: dirección, horarios, teléfono, mapa.

### 4.3 Cafetería (`/estilo-floria/cafeteria/`)
- **Slider "Productos nuevos"**: fotos reales (Bagels, Waffles, Croissants rellenos, Muffins, Tortas, Volcán de Chocolate), sin etiqueta "Próximamente" (ya se retiró).
- **Acordeón de categorías** (Promos primero y único abierto por defecto; luego Cafés e Infusiones, Especiales de la Casa, Licuados y Bebidas, Tortas y Dulces, Panadería y Facturas, Waffles, Tostados y Panes).
- **Delivery y Pedidos** y **Contacto**: igual que en las otras páginas.

---

## 5. Interacción y comportamiento (mobile-first)

- **Sliders/carruseles** (Carta y Cafetería): scroll continuo automático (vía `requestAnimationFrame`, loop infinito sin cortes), controles de flecha, y **arrastre táctil/mouse** (apoyar el dedo y deslizar) para navegar manualmente.
- **Menú hamburguesa**: overlay a pantalla completa en mobile; se corrigió un bug donde el menú cerrado (con `opacity:0`) seguía interceptando toques en toda la página por falta de `pointer-events:none`.
- **Anchors internos**: todas las secciones con destino de scroll tienen `scroll-margin-top` ajustado al alto real de la barra de navegación fija (y de las pestañas sticky en Carta), para que el destino no quede tapado.
- **Modal de producto** (Carta): foco atrapado dentro del modal, cierre con click en el fondo, botón X o tecla Escape.
- Sin frameworks de JS: vanilla JS por página, sin dependencias externas de build.

---

## 6. Sistema de diseño

**Paleta "Trattoria Moderna":**
| Token | Valor | Uso |
|---|---|---|
| `--bg` | `#FEFCF9` | Fondo general (crema cálido) |
| `--bg-warm` | `#F8F4EE` | Fondo alternativo de secciones |
| `--fg` | `#1A1816` | Texto principal / fondos oscuros |
| `--fg-muted` | `#6F6B66` | Texto secundario |
| `--accent` | `#BF4A2B` | Terracota — CTAs, precios, acentos |
| `--border` | `#E9E4DC` | Bordes sutiles |

**Tipografía:** DM Serif Display (títulos, precios) + DM Sans (cuerpo, UI).

**Accesibilidad:** contraste mínimo 4.5:1, `aria-label`/`aria-expanded` en controles interactivos, soporte de teclado en acordeones y modal, `focus-visible` en todos los elementos interactivos.

---

## 7. Contenido y assets — estado actual

| Categoría | Estado |
|---|---|
| Fotos de Empanadas (10), Ensaladas (6), Tartas (4), Lomitos (7) | ✅ Completo, con foto y descripción real |
| Minutas (Milanesa, Suprema, Pollo a la Mostaza) | ✅ Foto y descripción; faltan Pollo Deshuesado y Pollo Argentino |
| Pizzas | ✅ 13 con foto real; **9 pendientes de foto** (Fugazza, Cuatro Quesos, Queso Brie, Parma, Queso Azul, Vegetariana, Calabresa, Pollo Deshuesado, Pollo Argentino) — se muestran sin recuadro de imagen hasta tenerla |
| Porciones | ✅ Con fotos propias |
| Slider "Productos nuevos" (Cafetería) | ✅ Completo con fotos reales |
| Slider "Promos para compartir" (Carta) | ⏸️ Desactivado, pendiente de fotos |
| Logos de delivery, fotos del local, PDF de carta cafetería | ✅ Cargados |

**Convención de assets:** carpetas por categoría dentro de `assets/img/`, nombres de archivo en minúsculas y sin espacios (kebab-case), reemplazo directo de placeholders SVG por fotos reales a medida que están disponibles.

---

## 8. Fuera de alcance (no incluido en este sitio)

- Carrito de compras o pago integrado.
- Sistema de reservas.
- Panel de administración/CMS — las actualizaciones de contenido se hacen editando el HTML directamente.
- Multi-idioma (el sitio es 100% en español rioplatense).

---

## 9. Próximos pasos conocidos

1. Conseguir fotos reales para las 9 pizzas/minutas restantes y reactivar sus recuadros de imagen.
2. Conseguir fotos de las promociones y reactivar el slider "Promos para compartir" en Carta.
3. Decidir destino final de archivos sueltos sin uso (`about.svg`, `hero-bg.svg`, `Imagen interior.jpeg`).
4. Definir si se publica el sitio en un dominio propio (ya existe `CNAME` apuntando a `sanchez-sanchez.com.ar`) o se mantiene en modo desarrollo.
