# Cómo abrir el visor

Hay dos formas. La primera no requiere instalar nada y es la recomendada.

## 1. En el navegador, sin instalar nada

Abrid esta dirección: *(pendiente de publicar — os la pasaré por el chat)*

Funciona en cualquier equipo y en cualquier navegador, también dentro de la
Agencia, y no hay nada que instalar ni que configurar.

## 2. En local, con `abrir-visor.bat`

Si tenéis la carpeta descargada y queréis abrirla sin conexión:

1. Doble clic en **`abrir-visor.bat`**.
2. Se abre una ventana negra y, detrás, el navegador con el visor.
3. **Dejad la ventana negra abierta** mientras lo uséis. Para cerrarlo, cerradla.

Si el puerto 8080 está ocupado, se le puede dar otro: abrid una consola en esta
carpeta y escribid `abrir-visor.bat 8081`.

### Necesita Python

Es lo único que hace falta, y **no hay que instalar ninguna librería**: el visor es
una página suelta y el servidor viene incluido en Python. Si el `.bat` no encuentra
Python os lo dirá y os recordará la dirección publicada, que hace lo mismo.

Python se descarga en <https://www.python.org/downloads/>. En un equipo corporativo
puede que necesitéis permisos de vuestro departamento de informática: si es así, no
merece la pena pelearse — usad la dirección publicada.

## Por qué el `index.html` no funciona con doble clic

Si descomprimís el ZIP y hacéis doble clic en `index.html`, **la página saldrá
vacía**. No está rota: el navegador prohíbe que una página abierta desde el disco
lea los ficheros de su propia carpeta, y el visor necesita leer `corpus/indice.csv`.

Por eso existe el `.bat`, que sirve la carpeta como si fuera un sitio web local.

Lo que sí funciona a doble clic, sin nada más: las noticias de `corpus/noticias/`
son ficheros de texto, y los datos de `corpus/datos/` son CSV que abre Excel.

## Los ficheros de Claude Code

`CLAUDE.md` y `.claude/commands/` son las instrucciones que se usaron en pantalla.
**No hacen falta para nada de lo anterior.** Están por si alguien usa Claude Code y
quiere reproducir la sesión en su equipo: basta con abrirlo en esta carpeta y los
comandos aparecen solos.

La carpeta se llama `.claude`, con un punto delante. Se ve con normalidad en el
Explorador de Windows; el punto es solo la convención que usa la herramienta para
encontrarla.

Y lo importante: **no hace falta Claude Code para nada**. Lo que de verdad se lleva
uno de la sesión son las tres plantillas de `prompts/`, y esas funcionan pegadas en
cualquier chat, incluso gratuito.
