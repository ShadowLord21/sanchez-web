#!/usr/bin/env python3
"""
Regenera la Content-Security-Policy de las paginas del sitio.

La CSP usa hashes SHA-256 de cada bloque <style> y <script> inline. Si se edita
cualquiera de esos bloques, el hash deja de coincidir y el navegador BLOQUEA el
bloque. Hay que correr este script despues de tocar estilos o scripts inline.

Uso (desde la raiz del repo):
    python3 docs/scripts/regen_csp.py

Si ya cargaste la CSP como header en Cloudflare, acordate de copiar el valor
nuevo alla tambien (el <meta> y el header tienen que coincidir).
"""

import base64
import hashlib
import pathlib
import re
import sys

# Cada pagina y las directivas extra que necesita
PAGES = {
    "index.html": "frame-src https://www.google.com; ",
    "carta/index.html": "frame-src https://www.google.com; ",
    "cafeteria/index.html": "frame-src https://www.google.com; ",
    "404.html": "",
}

META_RE = r'\s*<meta http-equiv="Content-Security-Policy"[^>]*>'


def sha256_csp(text: str) -> str:
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    return "'sha256-" + base64.b64encode(digest).decode() + "'"


def build_csp(html: str, extra: str) -> str:
    scripts = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", html, re.S)
    styles = re.findall(r"<style[^>]*>(.*?)</style>", html, re.S)

    script_hashes = " ".join(sha256_csp(s) for s in scripts)
    style_hashes = " ".join(sha256_csp(s) for s in styles)

    return (
        "default-src 'self'; "
        f"script-src 'self'{' ' + script_hashes if script_hashes else ''}; "
        f"style-src 'self'{' ' + style_hashes if style_hashes else ''}; "
        "img-src 'self' data:; "
        "font-src 'self'; "
        f"{extra}"
        "connect-src 'self'; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "form-action 'none'; "
        "upgrade-insecure-requests"
    )


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[2]
    changed = 0
    todos_script: list[str] = []
    todos_style: list[str] = []

    for rel, extra in PAGES.items():
        path = root / rel
        if not path.exists():
            print(f"  AVISO: no existe {rel}, salteado")
            continue

        html = path.read_text(encoding="utf-8")
        html_sin_meta = re.sub(META_RE, "", html)

        # acumular hashes de todas las paginas para la version header
        for s in re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", html_sin_meta, re.S):
            h = sha256_csp(s)
            if h not in todos_script:
                todos_script.append(h)
        for s in re.findall(r"<style[^>]*>(.*?)</style>", html_sin_meta, re.S):
            h = sha256_csp(s)
            if h not in todos_style:
                todos_style.append(h)

        csp = build_csp(html_sin_meta, extra)
        meta = f'<meta http-equiv="Content-Security-Policy" content="{csp}">'

        viewport = re.search(r'<meta name="viewport"[^>]*>', html_sin_meta)
        if not viewport:
            print(f"  ERROR: {rel} no tiene <meta name=\"viewport\">, salteado")
            continue

        nuevo = (
            html_sin_meta[: viewport.end()] + "\n" + meta + html_sin_meta[viewport.end():]
        )

        if nuevo != html:
            path.write_text(nuevo, encoding="utf-8")
            changed += 1
            print(f"  actualizado  {rel}")
        else:
            print(f"  sin cambios  {rel}")

    # --- Version header para Cloudflare ---
    # Un header HTTP aplica a TODAS las paginas, asi que lleva la union de los
    # hashes de todas. Ademas suma frame-ancestors, que en <meta> se ignora.
    header_csp = (
        "default-src 'self'; "
        f"script-src 'self' {' '.join(todos_script)}; "
        f"style-src 'self' {' '.join(todos_style)}; "
        "img-src 'self' data:; "
        "font-src 'self'; "
        "frame-src https://www.google.com; "
        "connect-src 'self'; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "form-action 'none'; "
        "frame-ancestors 'self'; "
        "upgrade-insecure-requests"
    )
    salida = root / "docs" / "csp-header.txt"
    salida.write_text(
        "# Valor para pegar en Cloudflare (Transform Rule -> Set static).\n"
        "# Etapa 1: nombre del header = Content-Security-Policy-Report-Only\n"
        "# Etapa 2: nombre del header = Content-Security-Policy\n"
        "# Generado por docs/scripts/regen_csp.py - no editar a mano.\n\n"
        + header_csp + "\n",
        encoding="utf-8",
    )

    print(f"\n{changed} archivo(s) actualizado(s).")
    print(f"Valor para Cloudflare escrito en: docs/csp-header.txt")
    if changed:
        print("OJO: si ya cargaste la CSP como header en Cloudflare, actualizala con ese valor.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
