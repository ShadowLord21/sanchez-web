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

## 2 — Cabeceras de seguridad (Cloudflare)

### ¿Qué es esto, en criollo?

Cuando alguien entra a tu sitio, el servidor manda **dos cosas**: la página que se ve, y un
conjunto de "instrucciones invisibles" para el navegador que se llaman **cabeceras** (headers).
Esas instrucciones dicen cosas como *"a este sitio entrá siempre por HTTPS"* o *"no permitas
que otra web me meta adentro de un marco para estafar a mis clientes"*.

Hoy tu sitio **no manda ninguna** de esas instrucciones. Eso es lo que vamos a arreglar acá.

GitHub Pages no deja configurarlas (es un hosting muy simple). Pero como tu dominio pasa por
**Cloudflare**, Cloudflare puede agregarlas al vuelo: la página sale de GitHub, pasa por
Cloudflare, Cloudflare le agrega las instrucciones, y recién ahí llega al visitante.

Eso se configura con lo que Cloudflare llama una **regla de transformación de respuesta**.
Es una sola regla que dice: *"a todo lo que salga de este dominio, agregale estas 7 cabeceras"*.
Se hace una vez y queda andando para siempre.

---

### Paso a paso

**1.** Entrá a https://dash.cloudflare.com e iniciá sesión.

**2.** En la pantalla principal te aparece la lista de tus dominios. Hacé clic en
**`sanchez-sanchez.com.ar`**.

> Importante: la regla se configura **dentro del dominio**, no en la pantalla general de la cuenta.

**3.** En el menú de la izquierda buscá **Rules** (Reglas). Hacé clic.

**4.** Ahí adentro vas a ver una de estas dos cosas, según la versión del panel:

- **Opción A:** un submenú que dice **Transform Rules** → entrá y elegí la pestaña
  **Modify Response Header** (Modificar cabecera de respuesta).
- **Opción B (panel nuevo):** una pantalla **Overview** con un botón **Create rule** →
  al hacer clic te deja elegir el tipo, y elegís **Response Header Transform Rule**.

En ambos casos terminás en el mismo formulario. Si no encontrás ninguna, usá el buscador
de arriba del panel y escribí "Transform".

**5.** Hacé clic en **Create rule** (Crear regla).

**6.** En **Rule name** (nombre de la regla) poné: `Cabeceras de seguridad`

**7.** Te va a preguntar a qué peticiones aplicar la regla. Elegí la opción
**All incoming requests** (todas las peticiones entrantes).

> Si tu panel no ofrece esa opción y te obliga a armar un filtro, poné:
> Field = `Hostname`, Operator = `equals`, Value = `sanchez-sanchez.com.ar`

**8.** Abajo está la parte de **Then** (entonces) / **Response Header Modifications**.
Ahí vas a cargar las 7 cabeceras, **una por una**. Para cada una:

- Hacé clic en **+ Add header** / **Set new header** (agregar cabecera)
- En el desplegable de acción elegí **Set static** (valor fijo)
- En **Header name** escribí el nombre de la columna izquierda de la tabla
- En **Value** pegá exactamente el texto de la columna derecha
- Repetí para la siguiente

| # | Header name | Value | Para qué sirve |
|---|---|---|---|
| 1 | `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` | Obliga al navegador a usar siempre HTTPS durante un año |
| 2 | `X-Content-Type-Options` | `nosniff` | Evita que el navegador "adivine" tipos de archivo y ejecute algo que no debe |
| 3 | `Referrer-Policy` | `strict-origin-when-cross-origin` | No filtra a otros sitios la URL exacta desde la que vino el visitante |
| 4 | `X-Frame-Options` | `SAMEORIGIN` | Impide que otra web meta tu sitio en un marco para hacerse pasar por vos |
| 5 | `Permissions-Policy` | `camera=(), microphone=(), geolocation=(), payment=(), usb=(), magnetometer=(), gyroscope=(), accelerometer=(), interest-cohort=()` | Bloquea cámara, micrófono, ubicación, etc. Tu sitio no los usa |
| 6 | `Cross-Origin-Opener-Policy` | `same-origin` | Aísla tu pestaña de otras ventanas que quieran manipularla |
| 7 | `X-DNS-Prefetch-Control` | `off` | Evita consultas DNS anticipadas innecesarias |

**9.** Hacé clic en **Deploy** (o **Save and Deploy**). Listo, ya está activo — no hace falta
tocar nada en GitHub ni volver a subir el sitio.

---

### Cómo saber si funcionó

Esperá 1 o 2 minutos y entrá a:

**https://securityheaders.com/?q=sanchez-sanchez.com.ar**

Antes de este paso te daba **F**. Después de cargar las 7 cabeceras tiene que darte **A**.

Si te sigue dando F:
- Verificá que el dominio en Cloudflare tenga la nubecita **naranja** (proxied) y no gris.
  Con la nube gris, el tráfico no pasa por Cloudflare y la regla nunca se aplica.
- Revisá que la regla figure como **Enabled** / activa en la lista de reglas.

### Sobre `preload` en HSTS

Vas a ver que la cabecera 1 admite agregarle `; preload` al final. **No lo hagas todavía.**

`preload` mete tu dominio en una lista que viene *precargada dentro de los navegadores*.
Es prácticamente irreversible: si algún día necesitás que algo funcione por HTTP, sacarlo de
esa lista tarda meses. Dejá la cabecera como está 2 o 3 meses, confirmá que todo anda bien,
y recién ahí evaluá sumar `; preload` y registrar el dominio en https://hstspreload.org

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
