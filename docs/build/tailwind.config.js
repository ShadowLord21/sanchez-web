/* ===================================================================
   CSS del sitio: config de Tailwind
   ===================================================================

   El sitio NO carga Tailwind: no puede, porque la CSP es estricta y no
   permite scripts de terceros. El CSS se compila UNA VEZ aca y se
   commitea ya armado en assets/css/app.css.

   PARA RECOMPILAR (hace falta despues de tocar clases en el HTML):

       cd docs/build
       npm install        (solo la primera vez)
       npm run css

   PARA AUDITAR que no falte ninguna clase:

       python audit.py ../../carta/index.html ../../assets/css/app.css

   Las unicas que pueden figurar como faltantes sin ser un problema son
   material-symbols-outlined (viene de assets/fonts/fonts.css) y las
   sombras arbitrarias, que el minificador escribe rgba(x,y,z,.04) sin el
   cero y por eso el auditor no las encuentra.

   Esta config salio tal cual de los diseños de Google Stitch. Las clases
   propias que Stitch usa pero no define (icon-fill, no-scrollbar,
   scrollbar-none, animate-in, fade-in, zoom-in-95, data-sin-foto) estan
   escritas a mano en input.css.

   iconos.txt tiene los nombres de Material Symbols que usa el sitio: la
   fuente esta subseteada a esos. Si aparece uno nuevo hay que sumarlo ahi
   y volver a pedir el subset a Google.
   =================================================================== */
module.exports = Object.assign({ darkMode: "class", theme: { extend: { "colors": { "tertiary-fixed-dim": "#dec0b8", "surface-container-high": "#ece7e1", "on-background": "#1d1c17", "on-error-container": "#93000a", "on-surface": "#1d1c17", "on-secondary-fixed-variant": "#663e00", "on-surface-variant": "#58413d", "on-tertiary-container": "#ceb1a9", "on-tertiary": "#ffffff", "primary-fixed-dim": "#ffb4a6", "inverse-primary": "#ffb4a6", "surface-container-lowest": "#ffffff", "surface-variant": "#e7e2db", "secondary-fixed": "#ffddba", "tertiary-fixed": "#fcdcd3", "on-error": "#ffffff", "inverse-surface": "#32302c", "on-secondary-container": "#6f4300", "outline": "#8c716c", "surface": "#fef9f2", "error": "#ba1a1a", "primary-fixed": "#ffdad4", "secondary": "#875300", "surface-container": "#f2ede6", "on-primary-fixed": "#400200", "background": "#fef9f2", "on-primary-container": "#ff9d8b", "outline-variant": "#e0bfb9", "tertiary-container": "#59433d", "surface-container-low": "#f8f3ec", "surface-bright": "#fef9f2", "secondary-fixed-dim": "#ffb964", "inverse-on-surface": "#f5f0e9", "surface-dim": "#ded9d3", "tertiary": "#402d28", "on-secondary": "#ffffff", "primary": "#690600", "secondary-container": "#fdae49", "on-tertiary-fixed-variant": "#57423c", "on-primary-fixed-variant": "#891d0e", "surface-container-highest": "#e7e2db", "surface-tint": "#ab3523", "on-secondary-fixed": "#2b1700", "on-primary": "#ffffff", "primary-container": "#8b1e0f", "error-container": "#ffdad6", "on-tertiary-fixed": "#281713" }, "borderRadius": { "DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem" }, "spacing": { "space-sm": "0.5rem", "space-lg": "1.5rem", "space-xs": "0.25rem", "space-xl": "2.5rem", "gutter": "1rem", "margin": "2rem", "space-md": "1rem", "margin-mobile": "1rem", "gutter-mobile": "0.75rem" }, "fontFamily": { "headline-lg-mobile": [ "Vollkorn" ], "body-lg": [ "Be Vietnam Pro" ], "caption": [ "Be Vietnam Pro" ], "body-md": [ "Be Vietnam Pro" ], "headline-sm": [ "Vollkorn" ], "display-lg-mobile": [ "Vollkorn" ], "headline-lg": [ "Vollkorn" ], "headline-md": [ "Vollkorn" ], "label-lg": [ "Be Vietnam Pro" ], "display-lg": [ "Vollkorn" ], "label-md": [ "Be Vietnam Pro" ], "title-md": [ "Be Vietnam Pro" ] }, "fontSize": { "headline-lg-mobile": [ "26px", { "lineHeight": "32px", "fontWeight": "600" } ], "body-lg": [ "16px", { "lineHeight": "26px", "fontWeight": "400" } ], "caption": [ "11px", { "lineHeight": "14px", "letterSpacing": "0.02em", "fontWeight": "500" } ], "body-md": [ "14px", { "lineHeight": "22px", "fontWeight": "400" } ], "headline-sm": [ "20px", { "lineHeight": "26px", "fontWeight": "600" } ], "display-lg-mobile": [ "32px", { "lineHeight": "38px", "letterSpacing": "-0.01em", "fontWeight": "700" } ], "headline-lg": [ "32px", { "lineHeight": "40px", "fontWeight": "600" } ], "headline-md": [ "24px", { "lineHeight": "30px", "fontWeight": "600" } ], "label-lg": [ "14px", { "lineHeight": "18px", "letterSpacing": "0.02em", "fontWeight": "600" } ], "display-lg": [ "44px", { "lineHeight": "52px", "letterSpacing": "-0.02em", "fontWeight": "700" } ], "label-md": [ "12px", { "lineHeight": "16px", "letterSpacing": "0.04em", "fontWeight": "600" } ], "title-md": [ "18px", { "lineHeight": "24px", "fontWeight": "600" } ] } } } }, {
  content: [
    '../../index.html',
    '../../carta/index.html',
    '../../cafeteria/index.html',
    '../../404.html',
  ],
});
