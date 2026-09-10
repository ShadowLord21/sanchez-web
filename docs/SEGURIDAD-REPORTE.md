# Reporte de verificación de seguridad — sanchez-sanchez.com.ar

**Fecha:** 2026-09-09
**Alcance:** sitio estático (HTML/CSS/JS sin backend) en GitHub Pages + Cloudflare
**Commit de checkpoint previo:** `6f04e70`

Leyenda: ✅ OK · 🔧 Corregido en código · ⚠️ Pendiente tuyo (Cloudflare/GitHub) · ➖ No aplica

---

## A. HTTPS / transporte

| Ítem | Estado | Detalle |
|---|---|---|
| HTTPS funciona | ✅ | `https://` responde 200 vía Cloudflare |
| **Redirección HTTP→HTTPS** | ⚠️ | **`http://` devuelve 200, NO redirige.** "Always Use HTTPS" está apagado |
| HSTS | ⚠️ | Ausente en la respuesta. Va en Cloudflare |
| Contenido mixto | ✅ | 0 recursos `http://` en el código |
| `upgrade-insecure-requests` | 🔧 | Incluido en la CSP |
| Cloudflare SSL Full (Strict) | ⚠️ | No verificable desde afuera, revisalo en el panel |

## B. Cabeceras de seguridad

Medido en vivo: **no hay ninguna cabecera de seguridad**. Valores definidos en `SEGURIDAD-INFRA.md`.

| Cabecera | Estado |
|---|---|
| Content-Security-Policy | 🔧 estricta por `<meta>` con hashes + ⚠️ versión header para Report-Only |
| Strict-Transport-Security | ⚠️ Cloudflare |
| X-Content-Type-Options | ⚠️ Cloudflare |
| Referrer-Policy | ⚠️ Cloudflare |
| Permissions-Policy | ⚠️ Cloudflare |
| Anti-clickjacking | ⚠️ `X-Frame-Options` en Cloudflare (`frame-ancestors` se ignora en meta) |

### La CSP que quedó
```
default-src 'self'; script-src 'self' 'sha256-…'; style-src 'self' 'sha256-…';
img-src 'self' data:; font-src 'self'; frame-src https://www.google.com;
connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'none';
upgrade-insecure-requests
```
**Sin `'unsafe-inline'` ni `'unsafe-eval'` en ninguna directiva.** Para lograrlo hubo que
convertir 55 atributos `style=""` inline en clases CSS (53 de ellos en la carta, eran las
fotos de producto) — ver sección "Cambios de código".

## C. Enlaces y recursos externos

| Ítem | Estado | Detalle |
|---|---|---|
| `rel="noopener noreferrer"` | 🔧 | Eran 21 links `target="_blank"`: 15 tenían solo `noopener`, **6 no tenían nada**. Ahora los 21 completos |
| Google Fonts | 🔧 | **Self-hosteadas.** 6 archivos `.woff2` (120 KB) en `assets/fonts/`. Ya no se pega a `fonts.googleapis.com` ni `fonts.gstatic.com` |
| SRI | ➖ | Ya no hay recursos de CDN que necesiten SRI |
| iframe de Maps | 🔧 | Tenía `loading="lazy"`; se le agregó `referrerpolicy="no-referrer-when-downgrade"` |

Beneficio extra del self-host: mejora de privacidad (Google ya no ve la IP de tus visitantes)
y la CSP queda mucho más simple.

## D. Secretos y datos

| Ítem | Estado |
|---|---|
| Claves/tokens en archivos | ✅ ninguno |
| **Historial completo de git** | ✅ escaneado (`sk-`, `ghp_`, `AKIA`, claves privadas) — limpio |
| Archivos `.env` / credenciales | ✅ nunca existieron en el historial |
| Datos sensibles en comentarios | ✅ ninguno |

## E. Exposición de archivos internos

**Este era el punto más importante y estaba mal encaminado.**

El sitio se publicaba desde la raíz del repo con `.nojekyll`, o sea que **todo** lo commiteado
iba a quedar público al pushear: `docs/PRD.md`, los 15 scripts de test, el reporte de TestSprite
y los 235 archivos de `.claude/` (8,6 MB de tooling, incluidas fuentes `.ttf`).

| Acción | Estado |
|---|---|
| Deploy publica solo la web | 🔧 workflow `deploy.yml` con lista explícita de archivos |
| `.claude/` fuera del repo | 🔧 `git rm --cached` + agregado al `.gitignore` (−8,6 MB) |
| Internos agrupados | 🔧 `testsprite_tests/` movido a `docs/testsprite_tests/` |
| `.git` expuesto | ✅ GitHub Pages nunca lo sirve |
| Source maps | ➖ no hay build |
| Cambiar Source a GitHub Actions | ⚠️ **paso 0 de la guía de infra** |

## F. Formularios / privacidad

| Ítem | Estado |
|---|---|
| Formularios | ➖ el sitio no tiene ninguno (los pedidos van por links externos) |
| Analytics / cookies | ➖ **no hay GA, GTM ni cookies propias.** No hace falta banner de consentimiento |
| Emails en texto plano | ✅ ninguno (solo teléfono vía `tel:`, que no es scrapeable como email) |
| `form-action 'none'` | 🔧 en la CSP, por si alguien inyecta un form |

> Si más adelante sumás analytics, ahí sí necesitás banner de consentimiento y política de
> privacidad por la Ley 25.326 de Protección de Datos Personales.

## G. Dependencias

➖ **No aplica.** No hay `package.json` ni `node_modules` — el sitio es HTML/CSS/JS puro sin
build. Nada que auditar con `npm audit`, y cero superficie de ataque por cadena de suministro.

## H. Otros

| Ítem | Estado | Detalle |
|---|---|---|
| Página 404 propia | 🔧 `404.html` con el diseño del sitio |
| `robots.txt` | 🔧 creado, con `Disallow` de internos y link al sitemap |
| `sitemap.xml` | 🔧 creado con las 3 páginas |
| Directory listing | ✅ GitHub Pages no lo hace |
| `console.log` / `debugger` | ✅ ninguno |
| Todos los links en https | ✅ verificado |
| **Sitio roto en la raíz** | 🔧 **encontrado y corregido** (ver abajo) |

---

## Hallazgo aparte: el deploy iba a romperse

Al comparar local contra el remoto: **hay 8 commits sin pushear**, y el sitio en vivo es del
6 de agosto. En el estado local, todo el sitio vivía en `/estilo-floria/` y **no había ningún
`index.html` en la raíz** → al pushear, `https://sanchez-sanchez.com.ar/` habría dado 404.

Corregido moviendo el sitio a la raíz. De paso, las URLs quedan más limpias:

| Antes | Ahora |
|---|---|
| `/estilo-floria/` | `/` |
| `/estilo-floria/carta/` | `/carta/` |
| `/estilo-floria/cafeteria/` | `/cafeteria/` |

---

## Organización de carpetas y git

**Renombrados** (minúsculas, sin espacios ni acentos), con todas las referencias actualizadas:

| Antes | Ahora |
|---|---|
| `assets/fotos/Cafe-con-Medialunas.jpg` | `cafe-con-medialunas.jpg` |
| `assets/fotos/Interior-del-Local.jpg` | `interior-del-local.jpg` |
| `assets/fotos/Vitrina-de-Panaderia.jpg` | `vitrina-de-panaderia.jpg` |
| `assets/logos/Logo-PedidoYa-1.png` | `pedidosya.png` |
| `assets/logos/Logo-mercado-pago.png` | `mercado-pago.png` |
| `assets/logos/Rappi-Logo.png` | `rappi.png` |
| `assets/pdf/Carta-Cafetería-_-Sánchez-_-Sánchez.pdf` | `carta-cafeteria.pdf` |
| `assets/img/Imagen interior.jpeg` | *(borrado, sin uso)* |

También borrados por no estar referenciados: `assets/img/about.svg`, `assets/img/hero-bg.svg`.

**`.gitignore` ampliado:** `node_modules/`, `.env*`, `*.pem`, `*.key`, `.DS_Store`, `Thumbs.db`,
`*.bak`, `*.tmp`, `*.orig`, `.claude/`, `docs/testsprite_tests/tmp/`.

**Estructura final:**
```
/                        ← lo que se publica
├── index.html  404.html  robots.txt  sitemap.xml  CNAME  .nojekyll
├── assets/     (fonts, fotos, img, logos, pdf)
├── carta/      cafeteria/
│
├── docs/                ← interno, NO se publica
│   ├── PRD.md  SEGURIDAD-REPORTE.md  SEGURIDAD-INFRA.md
│   └── testsprite_tests/
└── .github/workflows/deploy.yml
```

---

## Verificación: no se rompió nada

Todo comprobado en Chrome headless contra las 4 páginas, con las interacciones ejercitadas
(menú, acordeón, modal de producto, slider, selector de día):

| Chequeo | Resultado |
|---|---|
| Recursos bloqueados por CSP | **0** en las 4 páginas |
| Errores de consola | **0** |
| Requests fallidos (4xx/5xx) | **0** |
| Fuentes cargando (self-hosted) | ✅ |
| Recursos externos cargados | solo el iframe de Maps (permitido) |
| Referencias internas rotas | **0** (links, anclas y assets) |
| Menú móvil: abre / cierra con X / fondo / Escape | ✅ en las 3 páginas |
| Desktop sin regresiones | ✅ nav en fila, 14 px, hamburguesa oculta |

---

## Qué esperar en los verificadores

**Hoy (sin aplicar la infra):** securityheaders.com daría **F** y Observatory ~**0-15 / F**.

**Con la CSP por meta ya commiteada, pero sin tocar Cloudflare:** securityheaders.com sigue
dando F o D — ese sitio **solo mira headers HTTP**, no lee el `<meta>`.

**Después de aplicar las cabeceras en Cloudflare:**

| Herramienta | Esperado |
|---|---|
| securityheaders.com | **A** (o **A+** si sumás `preload` a HSTS más adelante) |
| Mozilla Observatory | **A+ / 100-115** — suma puntos por CSP estricta sin `unsafe-inline`, HSTS, `nosniff`, Referrer-Policy y clickjacking cubierto |
| SSL Labs | **A** (o A+ con HSTS largo). Depende de Cloudflare, no del sitio |

Si Observatory se queda en A en vez de A+, suele ser por `X-Frame-Options` sin `frame-ancestors`
en el header — se resuelve al pasar la CSP de meta a header (etapa 2 del rollout).

---

## Acciones priorizadas

### 🔴 Alta — hacelas antes o junto con el push
1. **Cambiar Pages Source a "GitHub Actions"** (si no, se publican los internos). Paso 0 de la guía.
2. **Activar "Always Use HTTPS"** en Cloudflare — hoy el sitio responde por HTTP sin redirigir.
3. **Verificar SSL/TLS en "Full (Strict)"** — si está en Flexible, el tramo a GitHub va sin cifrar.
4. **Tildar "Enforce HTTPS"** en GitHub Pages.

### 🟡 Media — esta semana
5. Crear la Transform Rule con las 7 cabeceras.
6. Sumar `Content-Security-Policy-Report-Only` y dejarla correr 2-4 semanas.
7. Activar **DNSSEC** (incluye cargar el registro DS en NIC Argentina).
8. Activar **Bot Fight Mode** y el **WAF managed ruleset**.

### 🟢 Baja — cuando quieras
9. Pasar la CSP de Report-Only a enforcement.
10. Evaluar `preload` en HSTS (recién a los 2-3 meses).
11. Optimizar las fotos pesadas (varias superan 3 MB; `bagels.jpg` pesa 2,7 MB).
12. Decidir qué hacer con la visibilidad del repo (sección 6 de la guía de infra).

---

## Mantenimiento: si tocás HTML, CSS o JS inline

La CSP usa **hashes SHA-256** de cada bloque `<style>` y `<script>` inline. Si cambiás aunque
sea un espacio dentro de esos bloques, **el hash deja de coincidir y el bloque se bloquea**.

Para regenerarlos:
```bash
python3 docs/scripts/regen_csp.py
```
Ese script recalcula los hashes de las 4 páginas y reescribe el `<meta>`. Corrélo siempre
después de editar estilos o scripts inline, y volvé a copiar el valor al header de Cloudflare
si ya lo tenías puesto ahí.
