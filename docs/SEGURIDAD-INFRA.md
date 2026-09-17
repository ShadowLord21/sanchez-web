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

## 1 — HTTPS forzado

**Cloudflare:**
1. SSL/TLS → **Edge Certificates** → activar **Always Use HTTPS**
2. En la misma pantalla → activar **Minimum TLS Version: 1.2**
3. SSL/TLS → **Overview** → poner el modo en **Full**
   (Si está en "Flexible", el tramo Cloudflare↔GitHub va sin cifrar — cambialo sí o sí.)

> ### ⛔ NO pongas "Full (Strict)" sin leer esto
>
> **Full (Strict)** exige que el origen (GitHub Pages) tenga un certificado válido para
> `sanchez-sanchez.com.ar`. Y acá está la trampa:
>
> **GitHub Pages no puede emitir ese certificado mientras el dominio esté proxeado por
> Cloudflare** (nube naranja). GitHub valida el dominio resolviéndolo y espera ver sus propios
> servidores (`185.199.108-111.153`); ve las IPs de Cloudflare y nunca emite el certificado.
>
> Síntomas de haberlo activado igual:
> - En GitHub → Settings → Pages, **Enforce HTTPS aparece en gris** ("unavailable... a
>   certificate has not yet been issued")
> - El sitio devuelve **error 526** de Cloudflare — o sea, **se cae**
>
> (Nos pasó exactamente esto el 17/09/2026.)

### Las dos configuraciones válidas

**Opción A — Proxy activo + SSL "Full"** *(recomendada por simplicidad)*
- Los visitantes ven HTTPS válido: el certificado lo aporta Cloudflare
- El tramo Cloudflare↔GitHub va cifrado, pero sin validar el certificado del origen
- **Enforce HTTPS de GitHub queda "unavailable" para siempre, y está bien**: la redirección
  la hace "Always Use HTTPS" de Cloudflare
- Conservás WAF, Bot Fight Mode y caché

**Opción B — Llegar a "Full (Strict)"** *(más seguro, más pasos)*
1. Cloudflare → **DNS** → clic en la **nube naranja** del registro para dejarla **gris** (DNS only)
2. Esperá a que GitHub emita el certificado (15 min a 1 h). Sabés que está listo cuando en
   Settings → Pages podés **tildar Enforce HTTPS**
3. Tildá **Enforce HTTPS**
4. Volvé la nube a **naranja**
5. Recién ahí poné **Full (Strict)**

Durante el paso 1-2 el sitio funciona, pero sin WAF y con la IP de origen expuesta.

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

## 3 — CSP (Content-Security-Policy)

### ¿Qué es esto, en criollo?

La CSP es una **lista blanca**: le dice al navegador *"en esta página, solo cargá cosas de
estos lugares y nada más"*. Si mañana alguien logra inyectar un script malicioso en tu sitio,
el navegador se niega a ejecutarlo porque no está en la lista.

Es la protección más fuerte contra XSS, y también la más delicada: si la lista queda mal
armada, **bloqueás cosas tuyas** y el sitio se rompe (se ve sin estilos, el menú no abre, etc.).

### Lo que ya está hecho

En el código **ya hay una CSP estricta**, puesta como etiqueta `<meta>` dentro de cada página.
La verifiqué en un navegador real sobre las 4 páginas ejercitando menú, acordeón, modal y
slider: **0 recursos bloqueados**. O sea que la protección ya está funcionando para tus visitantes.

### Entonces, ¿por qué hacer algo más?

Por dos motivos:

1. **securityheaders.com no la ve.** Ese sitio solo mira cabeceras HTTP, no lee el HTML. Por eso
   te va a seguir marcando "Content-Security-Policy" en rojo aunque esté funcionando.
2. **Hay dos cosas que el `<meta>` no puede hacer** (es una limitación del estándar, no un error):
   - `frame-ancestors` (anti-clickjacking) — por eso en el punto 2 pusimos `X-Frame-Options`
   - el modo **Report-Only**, que es el que permite probar sin romper nada

Poniéndola también como cabecera en Cloudflare cubrís esos dos huecos.

---

### El valor exacto a pegar

Está en el archivo **`docs/csp-header.txt`** del repo. Abrilo, copiá la línea larga
(la que empieza con `default-src 'self';`) y esa es la que va en Cloudflare.

> ⚠️ **No copies el `<meta>` de `index.html`.** Cada página tiene hashes distintos, y una
> cabecera HTTP se aplica a **todas** por igual. El archivo `csp-header.txt` tiene la
> combinación de las 4 páginas — es el único valor que funciona para todas.

---

### Etapa 1 — Probar sin romper nada (2 a 4 semanas)

En modo **Report-Only** el navegador **no bloquea nada**: solo anota en la consola lo que
*habría* bloqueado. Es una prueba sin riesgo.

**1.** Cloudflare → tu dominio → **Rules** → la regla `Cabeceras de seguridad` que creaste en el
punto 2 → **Edit**

**2.** Agregá una cabecera más (igual que las otras 7):
- **Header name:** `Content-Security-Policy-Report-Only`
- **Value:** la línea larga de `docs/csp-header.txt`

**3.** **Deploy**

**4.** Durante las semanas siguientes, cada tanto abrí el sitio en la compu, apretá **F12**
(abre las herramientas de desarrollador), andá a la pestaña **Console** y navegá un poco:
entrá a Carta, abrí una tarjeta de producto, abrí el menú, mirá Cafetería.

- **Si no aparece nada en rojo** → todo bien, podés pasar a la etapa 2
- **Si aparece algo tipo** `Refused to load ... because it violates the following Content
  Security Policy directive` → anotá el mensaje completo y mandámelo. Significa que hay algo
  legítimo que la lista no contempla, y hay que ajustarla antes de activarla en serio.

### Etapa 2 — Activarla de verdad

Cuando pasaron 2-4 semanas sin mensajes rojos:

**1.** Volvé a editar la misma regla en Cloudflare

**2.** En esa cabecera, cambiá **solo el nombre**:
- de `Content-Security-Policy-Report-Only`
- a `Content-Security-Policy`

(el valor queda igual)

**3.** **Deploy**

**4.** Verificá en https://securityheaders.com/?q=https://sanchez-sanchez.com.ar/ — ahí sí
tendría que desaparecer el rojo y darte **A+**.

> **Si algo se rompe después de activarla:** volvé a ponerle `-Report-Only` al nombre del
> header y hacé Deploy. El sitio vuelve a la normalidad en segundos, porque el `<meta>` del
> código sigue protegiendo igual.

---

### ⚠️ Mantenimiento: cada vez que se toque el código

La CSP usa **huellas digitales (hashes)** de los bloques de estilos y scripts que están dentro
del HTML. Si se cambia aunque sea un espacio en esos bloques, la huella deja de coincidir y
**el navegador bloquea ese bloque** (el sitio se vería roto).

Por eso, después de cualquier edición de estilos o scripts hay que correr:

```bash
python3 docs/scripts/regen_csp.py
```

Eso recalcula todo y reescribe tanto los `<meta>` de las páginas como `docs/csp-header.txt`.
Si ya tenés la cabecera cargada en Cloudflare, **acordate de pegar el valor nuevo ahí también**,
porque si no van a quedar desincronizados.

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
