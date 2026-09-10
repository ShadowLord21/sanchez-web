# Guía de infraestructura — pasos que tenés que aplicar vos

Todo lo que sigue va en los paneles de **GitHub** y **Cloudflare**. Yo no tengo acceso, así que
te lo dejo con los pasos exactos. Están ordenados por prioridad.

---

## ⚠️ PASO 0 — Hacer ESTO antes de pushear

El sitio se movió: antes vivía en `/estilo-floria/`, ahora está en la raíz del repo.
Y el deploy pasa a hacerse con GitHub Actions (para no publicar `docs/` ni `.claude/`).

**Si pusheás sin hacer este paso, el deploy viejo va a publicar también las carpetas internas.**

1. GitHub → repo `sanchez-web` → **Settings** → **Pages**
2. En **Build and deployment** → **Source**, cambiá de "Deploy from a branch" a **"GitHub Actions"**
3. Recién ahí hacé `git push`

El workflow (`.github/workflows/deploy.yml`) ya está en el repo y publica **solo**:
`index.html`, `404.html`, `robots.txt`, `sitemap.xml`, `CNAME`, `.nojekyll`, `assets/`, `carta/`, `cafeteria/`.

> **Alternativa sin Actions:** si preferís seguir con "Deploy from a branch", borrá `.nojekyll` y
> creá un `_config.yml` con `exclude: [docs, .claude, .github]`. Es más frágil; recomiendo Actions.

---

## 1 — HTTPS forzado (ALTA prioridad, hoy está mal)

Verificado: `http://sanchez-sanchez.com.ar/` responde **200 OK en vez de redirigir a HTTPS**.

**GitHub:**
1. Settings → Pages → tildar **Enforce HTTPS**

**Cloudflare:**
1. SSL/TLS → **Overview** → poner el modo en **Full (Strict)**
   (Si está en "Flexible", el tramo Cloudflare↔GitHub va sin cifrar — cambialo sí o sí.)
2. SSL/TLS → **Edge Certificates** → activar **Always Use HTTPS**
3. En la misma pantalla → activar **Minimum TLS Version: 1.2**

---

## 2 — Cabeceras de seguridad (Cloudflare Transform Rules)

GitHub Pages no permite setear headers, así que van en Cloudflare.

**Ruta:** Cloudflare → **Rules** → **Transform Rules** → **Modify Response Header** → *Create rule*

- **Nombre:** `Security headers`
- **If:** `Hostname equals sanchez-sanchez.com.ar` (o "All incoming requests")
- **Then → Set static:** agregá una entrada por cada fila:

| Header | Valor |
|---|---|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `X-Frame-Options` | `SAMEORIGIN` |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=(), payment=(), usb=(), magnetometer=(), gyroscope=(), accelerometer=(), interest-cohort=()` |
| `Cross-Origin-Opener-Policy` | `same-origin` |
| `X-DNS-Prefetch-Control` | `off` |

### Sobre `preload` en HSTS
**No lo agregues todavía.** `preload` es prácticamente irreversible (queda embebido en los
navegadores). Recomendación: dejá `max-age=31536000; includeSubDomains` funcionando 2-3 meses,
confirmá que ningún subdominio necesite HTTP, y recién ahí sumá `; preload` y registralo en
https://hstspreload.org

---

## 3 — CSP: rollout en dos etapas

En el código **ya quedó una CSP estricta por `<meta>`**, con hashes SHA-256 de cada bloque
inline. Verificada en navegador real: **0 recursos bloqueados** en las 4 páginas.

Lo que el `<meta>` **no** puede hacer (limitación del estándar):
- `frame-ancestors` → por eso arriba pusimos `X-Frame-Options`
- modo **Report-Only** → no existe vía meta
- reporting endpoint

Por eso conviene además la versión header, con el rollout que pediste:

### Etapa 1 — Report-Only (2 a 4 semanas)
En la misma Transform Rule agregá:

| Header | Valor |
|---|---|
| `Content-Security-Policy-Report-Only` | *(pegar el contenido del `<meta>` de `index.html`, agregando `frame-ancestors 'self';`)* |

El valor exacto lo sacás de `index.html`, atributo `content` del `<meta http-equiv="Content-Security-Policy">`.

Durante ese período revisá si algo se rompe. **Ojo:** si tocás el HTML/CSS/JS inline, los hashes
cambian y hay que regenerarlos (ver `docs/SEGURIDAD-REPORTE.md`, sección "Mantenimiento").

### Etapa 2 — Enforcement
Si en 2-4 semanas no hubo reportes, renombrá el header a `Content-Security-Policy`
y borrá el `-Report-Only`.

---

## 4 — DNS y protección (Cloudflare)

1. **DNSSEC:** DNS → Settings → **Enable DNSSEC**. Cloudflare te da un registro DS que hay que
   cargar en **NIC Argentina** (donde tenés el dominio `.com.ar`). Sin ese paso queda a medias.
2. **Bot Fight Mode:** Security → Bots → activar **Bot Fight Mode** (gratis).
3. **WAF:** Security → WAF → **Managed Rules** → activar el ruleset gratuito de Cloudflare.
4. **Rate limiting** (opcional, plan gratis da 1 regla): Security → WAF → Rate limiting rules.
   Ej: más de 100 requests por minuto desde una IP → Managed Challenge.
5. **Always Online** (opcional): Caching → Configuration → activar. Sirve la última copia
   cacheada si GitHub Pages se cae.

---

## 5 — Verificación posterior

Cuando tengas todo aplicado, corré:

- https://securityheaders.com/?q=sanchez-sanchez.com.ar
- https://observatory.mozilla.org/analyze/sanchez-sanchez.com.ar
- https://www.ssllabs.com/ssltest/analyze.html?d=sanchez-sanchez.com.ar

Qué esperar está detallado en `docs/SEGURIDAD-REPORTE.md`.

---

## 6 — Opcional: privacidad del repositorio

El repo `ShadowLord21/sanchez-web` es público (necesario para Pages en plan gratuito).
Con el workflow nuevo, `docs/` y `.claude/` **ya no se publican en el dominio**, pero
**siguen siendo visibles en github.com** para cualquiera.

Si el PRD o los reportes de test te resultan sensibles, tenés dos caminos:
- Mover esos documentos a un repo privado aparte, o
- Pasar el repo a privado (requiere GitHub Pro para seguir usando Pages con dominio propio).

No hay credenciales ni datos personales ahí — es información de negocio.
