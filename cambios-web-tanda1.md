# Cambios de diseño — Web Sánchez & Sánchez (tanda 1)

> Continuás el rediseño estilo Loro que ya venías haciendo (ver brief-rediseno-loro.md). Aplicá los cambios de abajo. Usá al máximo las skills **UI-UX-PRO-MAX** y la de **front-end design de Anthropic**. Todo **mobile-first**.

## Antes de empezar
1. Hacé un **commit de checkpoint** con el estado actual ("checkpoint antes de tanda 1 de cambios"). Si no hay repo git, inicializalo.
2. Mostrame un **plan** de cómo vas a aplicar estos 5 cambios y **esperá mi OK** antes de codear.
3. Trabajá **cambio por cambio**; al terminar cada uno, pará y contame.

## Reglas (no romper)
- **No cambies el contenido informativo**: textos, nombres, precios, descripciones, links de delivery, horarios, dirección, teléfono y redes quedan EXACTAMENTE igual.
- Las **fotos siguen como placeholders** claramente marcados (las subo yo después).
- **No toques** la config de deploy ni archivos de dominio/DNS (ej. CNAME).
- Si dudás entre "contenido" y "diseño", preguntame antes de tocarlo.

---

## Cambio 1 — Barra de navegación (header)
Los ítems del menú (Nosotros · Cómo pedir · Carta · Delivery · Ubicación) están **muy pegados** entre sí y no se ven bien. Rediseñá la navbar:
- Más **separación (espaciado)** entre los ítems para que respiren.
- Mejorá el diseño en general (jerarquía, hover, prolijidad), manteniendo la identidad (crema/terracota, tipografías actuales).

## Cambio 2 — Hero: 4 botones con distinto destino
En la portada, reemplazá los 2 botones actuales por **4 opciones**:
- **Menú del Día** → enlace interno: hace scroll suave a la sección Menú del Día **dentro del one-page**.
- **Delivery** → enlace interno: scroll suave a la sección Delivery **dentro del one-page**.
- **Ver la Carta** → va a una **página aparte** (la carta de comidas es su propia página).
- **Cafetería** → va a una **página aparte** (la cafetería es su propia página).

> Importante (QR): como la Carta pasa a ser **página aparte**, esa página tiene que tener una **URL estable** (ej. `/carta`). El QR que antes iba a `/#menu` va a apuntar ahora a esa página. Dejá la URL fija y avisá cuál es, que el QR lo regeneramos para que lleve ahí.

## Cambio 3 — Carta (página): slideshow "Promos para compartir" al inicio
Al **principio** de la página de la Carta, agregá una sección **"Promos para compartir"** con formato de la referencia (fotos verticales grandes, leyenda abajo, esquinas redondeadas):
- Formato **carrusel / slideshow horizontal** que **se mueve a mano** (deslizar con el dedo en mobile, flechas o drag en desktop). NO auto-play.
- Contenido: las promos para compartir (Crispi para 2 y 4, Imperdible, Reina Empanadas, y las torres cuando estén). Usar el contenido/precios que ya existen.

## Cambio 4 — Cafetería (página): slideshow de productos nuevos (auto-play) al inicio
Al **principio** de la página de Cafetería, agregá un **slideshow con los productos nuevos** (bagels, waffles, croissants, muffins, factura circular combinada, lengüita, lemon pie, volcán de chocolate, etc.):
- Mismo formato que el de la Carta (fotos verticales con leyenda, esquinas redondeadas).
- Diferencia: este **se mueve solo (auto-play)**, avanzando cada pocos segundos. Que igual se pueda pausar/mover a mano y que respete `prefers-reduced-motion`.

## Cambio 5 — Sección de foto "El plato del mediodía": 3 fotos a lo ancho
La sección de foto sola con la leyenda **"El plato del mediodía, listo para servir"** pasa de **una** foto a **tres** fotos verticales en fila, **ocupando todo el ancho** de la página (cada una con su leyenda). En mobile que se apilen o scrolleen bien.
*(Por ahora aplica solo a esa sección; si después querés lo mismo en las otras fotos solas, lo indico.)*

---

## Al terminar
- Mostrame un **resumen + diff** confirmando que ningún texto, precio, link, horario ni dato de contacto se modificó (solo diseño/estructura/interactividad).
- Verificá: navbar con buen espaciado; los 4 botones del hero van a donde corresponde (2 scroll interno, 2 a páginas aparte); el slideshow de la Carta se mueve a mano; el de Cafetería se mueve solo; la sección "plato del mediodía" muestra 3 fotos a lo ancho; nada se rompe en mobile; la Carta tiene URL estable para el QR.
- (Opcional) Corré la auditoría de **web-design-guidelines de Vercel** y corregí lo prioritario.
