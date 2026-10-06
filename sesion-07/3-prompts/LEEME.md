# Mensajes de la sesión 7: los seis pasos

Cada paso tiene una versión **genérica** (la IA propone; pocos huecos) y una **plantilla** rellenable, con su **ejemplo ya relleno** del caso de la sesión (precio de la vivienda, hipotecas y compraventas). Cada fichero contiene solo el texto del mensaje: ábrelo, copia todo y pégalo en el chat. Los huecos están entre corchetes, y los valores por defecto, ya escritos.

| Paso | Fichero | Qué hace | Qué adjuntar |
|---|---|---|---|
| 1 · Comprender | `01-comprender-ficha-corta.md` · `01-comprender-ficha-larga.md` | Una ficha de un fichero: qué es, cómo está organizado, qué trampas tiene y qué no consta | Un fichero de datos (`5-datos`) |
| 2 · Ver | `02-ver-generico.md` · `02-ver-plantilla.md` · `02-ver-plantilla-ejemplo-ipv.md` | Gráficas de un fichero, con cómo se han hecho y los pasos para hacerlas | El mismo fichero (mejor en el mismo chat del paso 1) |
| 3 · Relacionar | `03-relacionar.md` | Qué cruces merecen la pena y qué datos nuevos traer | El catálogo de fichas (`4-fichas/00-catalogo-fichas.md`), adjunto o pegado al final |
| 4 · Cruzar | `04-cruzar-plantilla.md` · `04-cruzar-ejemplo-ipv-hipotecas-compraventas.md` | Una hoja «Cruce» con los datos unidos, todo con fórmulas | Un libro con una hoja por tabla (`5-datos/libros-de-cruce`) |
| 5 · Ver lo cruzado | `05-ver-lo-cruzado-plantilla.md` · `05-ver-lo-cruzado-ejemplo-ipv-hipotecas-compraventas.md` | Gráficas del libro cruzado, con las series en una misma escala | El libro con la hoja «Cruce» |
| 6 · Tendencias | `06-tendencias-plantilla.md` · `06-tendencias-ejemplo-ipv-hipotecas-compraventas.md` | Variaciones, fases, correlaciones con su incertidumbre y desfases | El libro con la hoja «Cruce» |

Lee la **guía del flujo** (`2-guia-del-flujo.pdf`) antes de empezar: explica cada paso y qué comprobar.

## Qué cambiar

- **Plantillas:** todo lo que va entre corchetes (hojas, columnas, filtros, series, ejes, periodos). Los ejemplos ya están rellenados para el caso de la sesión.
- **Genéricos:** solo los pocos parámetros del principio (qué quieres ver, número de gráficas, programa).
- **El programa:** los mensajes dicen «Excel» por defecto; escribe «LibreOffice» si es el tuyo.
- **Nombres de hojas del paso 4:** el ejemplo usa los nombres reales del libro de partida (Excel corta los nombres de pestaña a 31 caracteres). Si tu libro tiene otros, cámbialos en el mensaje.

## Qué se ha probado, con franqueza

- **1:** probado con el índice de precios de la vivienda en cuatro herramientas. El chat de Copilot en SharePoint se equivocó dos veces en la estructura: no lo uses para este paso.
- **2:** las versiones anteriores se probaron en Gemini, ChatGPT y Copilot; la versión final incorpora los ajustes de esas pruebas (datos leídos de la hoja original, todas las series, ejes legibles, comprobación contra el original).
- **3:** la primera versión se probó en tres herramientas. La versión final es más breve (tres tablas, 900 palabras como máximo) y no se ha vuelto a probar.
- **4:** la primera versión se probó en Copilot en Excel con un resultado correcto, que se verificó celda a celda (`5-datos/libros-de-cruce/ejemplo-cruce-hecho-con-copilot.xlsx`). La versión final añade una hoja de parámetros y una regla sobre celdas vacías, y no se ha vuelto a probar.
- **5:** se probó con resultados desiguales según la herramienta.
- **6:** es el más exigente y **no se ha probado todavía en una herramienta**. Puede que una cuenta gratuita no lo complete: en ese caso, pide un análisis cada vez.

En todos los pasos, **comprueba tú** un valor contra el original: la IA puede equivocarse de formas que no se ven a simple vista.
