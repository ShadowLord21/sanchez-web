# Salida de Google Stitch

Dejá acá lo que devolvió Stitch, con estos nombres.

## capturas/
Una imagen por pantalla (png o jpg):

- `inicio.png`
- `carta.png`
- `carta-detalle.png`   (la vista de producto ampliado, si la generó)
- `cafeteria.png`
- `404.png`

Si una pantalla es muy larga y la captura queda cortada, partila:
`carta-1.png`, `carta-2.png`, etc.

## codigo/
El HTML que da el botón de código de Stitch, uno por pantalla:

- `inicio.html`
- `carta.html`
- `cafeteria.html`
- `404.html`

---

## Qué vamos a revisar

Stitch inventa contenido. Al mirarlo, lo separamos en dos:

1. **Contenido inventado** → se saca siempre. Productos, precios, descripciones,
   horarios, teléfonos o secciones que Stitch se mandó solo. El contenido real
   del sitio está fijo y no se toca.

2. **Decisiones visuales** → se discuten. Paleta, tipografía, cómo resolvió las
   tarjetas, el filtro por grupo, la jerarquía de las promos. Acá sí se elige
   qué sirve y qué no.

Lo que no entra por restricción técnica (Tailwind, fuentes de Google, `style=""`)
está documentado en `../PROMPT-STITCH.md`, al final. Eso no es un problema del
diseño: se traduce.
