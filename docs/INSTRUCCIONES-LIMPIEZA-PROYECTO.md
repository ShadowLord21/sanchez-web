# Instrucciones para Limpieza del Proyecto Sánchez & Sánchez

**Fecha:** 2026-08-27  
**Estado:** Proyecto con código mezclado de dos versiones - necesita limpieza

---

## 📋 Contexto del Proyecto

Este proyecto tiene la web de **Sánchez & Sánchez**, una pizzería y cafetería en Almagro, CABA.

### Situación Actual
- ✅ **Versión nueva (MANTENER):** `estilo-floria/cafeteria/index.html` - Rediseño completo con acordeón
- ❌ **Versión antigua (ELIMINAR):** Archivos obsoletos del diseño anterior
- ⚠️ **Problema:** Hay código duplicado, imágenes mezcladas y rutas rotas

### Versión Final a Mantener
El archivo **`estilo-floria/cafeteria/index.html`** contiene el diseño pulido con:
- Acordeón elegante para el menú de cafetería
- Paleta "Trattoria Moderna" (crema #FEFCF9, terracota #BF4A2B)
- Tipografía: DM Serif Display + DM Sans
- 8 secciones colapsables
- Estados de interacción completos (hover, focus, active)
- Responsive mobile optimizado
- Accesibilidad WCAG 2.2 AA

---

## 🎯 Objetivo de la Limpieza

**Mantener ÚNICAMENTE:**
1. La carpeta `estilo-floria/` con su estructura completa
2. Las imágenes realmente utilizadas en la versión nueva
3. Archivos de referencia necesarios (PDF de la carta)

**Eliminar TODO lo siguiente:**
- Archivos HTML antiguos en la raíz del proyecto
- Carpetas `cafeteria/` y `carta/` de la raíz (versiones antiguas)
- Carpetas `estilo-loro/` (diseño alternativo descartado)
- Archivos CSS/JS sueltos en la raíz (`styles.css`, `script.js`)
- Imágenes duplicadas o no utilizadas
- Archivos `.artifact.json`
- Screenshots de proceso (`image.png`, `image-1.png`, etc.)

---

## 📁 Estructura Final Deseada

```
D:\sanchez-web\
├── estilo-floria/
│   ├── index.html                    # Página principal
│   ├── cafeteria/
│   │   └── index.html               # ✅ VERSIÓN NUEVA (acordeón)
│   └── carta/
│       └── index.html               # Página de carta de pizzas
│
├── img/                             # Imágenes de productos
│   ├── empanada-*.jpeg
│   ├── pizza-*.jpeg/png
│   ├── tarta-*.jpeg
│   ├── lomito-*.jpeg
│   ├── comida-*.jpeg
│   └── placeholder-vertical-*.svg
│
├── Cafe-con-Medialunas.jpg         # Foto hero cafetería
├── Vitrina-de-Panaderia.jpg        # Foto feature cafetería
├── Interior-del-Local.jpg
├── Pizza-Fugazzeta.jpg
├── Empanadas.jpg
├── Faina.jpg
│
├── Logo-mercado-pago.png           # Logos delivery
├── Rappi-Logo.png
├── Logo-PedidoYa-1.png
│
└── Carta-Cafetería-_-Sánchez-_-Sánchez.pdf  # Referencia
```

---

## 🗑️ Archivos a ELIMINAR

### Archivos HTML obsoletos en raíz:
```
❌ index.html
❌ concepto-a.html
❌ concepto-b.html
❌ concepto-c.html
❌ concepto-loro.html
❌ floria-concepto-1.html
❌ floria-concepto-2.html
```

### Carpetas completas a eliminar:
```
❌ cafeteria/              # Versión antigua
❌ carta/                  # Versión antigua  
❌ estilo-loro/            # Diseño alternativo descartado
❌ .od-skills/             # Skills temporales de Open Design
❌ .file-versions/         # Versiones antiguas
```

### Archivos sueltos a eliminar:
```
❌ *.artifact.json         # Metadatos de Open Design
❌ styles.css              # CSS antiguo
❌ script.js               # JS antiguo
❌ web-spec.md            # Especificación antigua
❌ image.png, image-1.png, image-2.png ... image-8.png  # Screenshots
❌ mercado-pago-social-preview*.png  # Duplicados de logos
❌ Logo-PedidoYa.png      # Duplicado (mantener Logo-PedidoYa-1.png)
❌ Rappi-Logo.jpg         # Duplicado (mantener Rappi-Logo.png)
❌ MercadoPago-Logo.webp  # Duplicado (mantener Logo-mercado-pago.png)
❌ Atmospheric_shot_of_a_traditio.mp4  # Videos no usados
❌ Slow_motion_cinematic_loop_ha.mp4
❌ Imagen-Flotante-Acento-_pizza_.jpg
❌ Detalle-horno-_acento-circular_.jpg
```

---

## 🔧 Tareas de Limpieza

### 1. Verificar Rutas de Imágenes en la Versión Nueva

En `estilo-floria/cafeteria/index.html`, las imágenes están referenciadas como:
```html
<img src="../../Cafe-con-Medialunas.jpg">
<img src="../../Vitrina-de-Panaderia.jpg">
<img src="../../Logo-mercado-pago.png">
<img src="../../Rappi-Logo.png">
<img src="../../Logo-PedidoYa-1.png">
```

**Acción:** Verificar que estas rutas funcionen correctamente después de copiar el proyecto.

### 2. Eliminar Archivos Obsoletos

Ejecutar desde PowerShell en `D:\sanchez-web\`:

```powershell
# Eliminar archivos HTML antiguos de la raíz
Remove-Item "index.html", "concepto-*.html", "floria-concepto-*.html" -Force -ErrorAction SilentlyContinue

# Eliminar carpetas obsoletas
Remove-Item "cafeteria", "carta", "estilo-loro", ".od-skills", ".file-versions" -Recurse -Force -ErrorAction SilentlyContinue

# Eliminar archivos sueltos
Remove-Item "*.artifact.json", "styles.css", "script.js", "web-spec.md" -Force -ErrorAction SilentlyContinue

# Eliminar screenshots
Remove-Item "image.png", "image-*.png" -Force -ErrorAction SilentlyContinue

# Eliminar duplicados de logos
Remove-Item "mercado-pago-social-preview*.png", "Logo-PedidoYa.png", "Rappi-Logo.jpg", "MercadoPago-Logo.webp" -Force -ErrorAction SilentlyContinue

# Eliminar videos no usados
Remove-Item "*.mp4" -Force -ErrorAction SilentlyContinue

# Eliminar imágenes extra no usadas
Remove-Item "Imagen-Flotante-Acento-_pizza_.jpg", "Detalle-horno-_acento-circular_.jpg" -Force -ErrorAction SilentlyContinue
```

### 3. Validar Estructura Final

Después de la limpieza, verificar:
- [ ] Solo existe la carpeta `estilo-floria/`
- [ ] `estilo-floria/cafeteria/index.html` funciona correctamente
- [ ] Todas las imágenes referenciadas existen
- [ ] No hay archivos `.html` en la raíz del proyecto
- [ ] La carpeta `img/` contiene solo las imágenes de productos usadas

---

## 📝 Características de la Versión Nueva (Referencia)

### Diseño "Acordeón Elegante"
- **8 secciones colapsables:**
  1. Cafés e Infusiones (abierta por defecto)
  2. Especiales de la Casa
  3. Licuados y Bebidas
  4. Tortas y Dulces
  5. Panadería y Facturas
  6. Waffles
  7. Tostados y Panes
  8. Promos — Todo el Día

### Paleta de Colores
```css
--bg: #FEFCF9;           /* Crema cálido */
--bg-warm: #F8F4EE;      /* Fondo alternativo */
--surface: #FFFFFF;      /* Blanco puro */
--fg: #1A1816;           /* Texto principal */
--fg-muted: #6F6B66;     /* Texto secundario */
--border: #E9E4DC;       /* Bordes */
--accent: #BF4A2B;       /* Terracota (CTA, precios) */
```

### Tipografía
- **Display:** DM Serif Display (títulos, precios)
- **Body:** DM Sans (cuerpo, menú)

### Estados de Interacción
- ✅ Hover con fondo más oscuro (#DDD6CB)
- ✅ Active con color más intenso (#A33D23)
- ✅ Focus visible con outline de 2px
- ✅ Contraste mínimo 4.5:1 (WCAG AA)

### Responsive
- ✅ Mobile: padding reducido, fuentes escaladas
- ✅ Tablet: espaciado intermedio
- ✅ Desktop: layout completo
- ✅ Sin scroll horizontal en ningún breakpoint

### Accesibilidad
- ✅ `aria-label` descriptivos en headers
- ✅ `aria-hidden="true"` en iconos decorativos
- ✅ `aria-expanded` dinámico en acordeones
- ✅ Soporte de teclado (Enter, Space)
- ✅ `tabindex="0"` y `role="button"` en headers

---

## ⚠️ Advertencias

1. **NO modificar** el archivo `estilo-floria/cafeteria/index.html` durante la limpieza
2. **NO eliminar** la carpeta `img/` completa, solo imágenes no referenciadas
3. **Mantener** el PDF `Carta-Cafetería-_-Sánchez-_-Sánchez.pdf` como referencia
4. **Verificar** que los logos de delivery (Mercado Pago, Rappi, PedidosYa) funcionen
5. **Probar** la página en navegador después de la limpieza

---

## 🚀 Checklist Final

Después de ejecutar las tareas de limpieza:

- [ ] El proyecto tiene solo la carpeta `estilo-floria/`
- [ ] No hay archivos HTML en la raíz
- [ ] No hay carpetas `cafeteria/`, `carta/`, `estilo-loro/`
- [ ] Todas las imágenes referenciadas en el HTML existen
- [ ] La página `estilo-floria/cafeteria/index.html` se ve correctamente en el navegador
- [ ] Los links de Delivery funcionan
- [ ] El acordeón se expande/colapsa correctamente
- [ ] Responsive funciona en móvil, tablet y desktop
- [ ] No hay errores 404 de imágenes en la consola del navegador

---

## 📞 Contacto del Proyecto

**Restaurante:** Sánchez & Sánchez  
**Ubicación:** Av. Rivadavia 3399, Almagro, CABA  
**Teléfono:** 11 5927-3756  
**Instagram:** @sanchezysanchez_ok

---

**Última actualización:** 2026-08-27  
**Generado por:** Open Design + impeccable-design-polish skill
