# Cómo instalar Python para usar el script

> **Esto es opcional. Del todo.** Todo lo demás de esta entrega funciona sin Python: el
> visor se abre con doble clic, los prompts se pegan en Gemini y las skills van en Claude.
> El script solo sirve para descargar noticias nuevas de golpe, rápido y sin depender de
> ninguna IA.
>
> **Si en vuestro ordenador de trabajo no podéis instalar programas, saltaos esta carpeta
> entera.** No os perdéis nada del ejercicio.

---

## Qué hace falta

Solo **Python 3**. Ninguna librería más, ningún `pip install`, nada que se pueda quedar a
medias: el script está escrito solo con lo que Python trae de fábrica.

---

## Paso 1 · Mirar si ya lo tenéis

Puede que sí. Para comprobarlo:

1. Menú Inicio, escribid `cmd`, Intro. Se abre una ventana negra.
2. Escribid esto y pulsad Intro:

   ```
   python --version
   ```

**Si responde algo como `Python 3.11.5`**, ya está. Id al paso 3.

**Si dice que no reconoce el comando, o se abre la Microsoft Store**, no lo tenéis.
Seguid al paso 2.

---

## Paso 2 · Instalarlo

1. Abrid <https://www.python.org/downloads/>.
2. Pulsad el botón grande amarillo **«Download Python»**.
3. Ejecutad el fichero descargado.
4. **MUY IMPORTANTE:** en la primera pantalla, antes de pulsar nada, marcad la casilla de
   abajo que dice **«Add python.exe to PATH»**.

   Si no la marcáis, Python se instala pero la ventana negra no lo encuentra, y parecerá
   que no está. Es el error más común.

5. Pulsad **«Install Now»** y esperad.
6. Cerrad la ventana negra y abrid una nueva. Repetid el paso 1 para comprobar.

### Si estáis en un ordenador de la Agencia

Es posible que no os deje instalar. Dos opciones: pedirlo a vuestro departamento de
informática, o —más sensato— **no pelearos y usar el resto de la entrega**, que no lo
necesita.

---

## Paso 3 · Ejecutar el script

1. Abrid el **Explorador de Windows** en la carpeta donde está `descargar_noticias.py`.
2. Pulsad en la **barra de dirección** de arriba, borradla, escribid `cmd` y pulsad Intro.
   Se abre la ventana negra **ya colocada en esa carpeta**.
3. Escribid:

   ```
   python descargar_noticias.py --dias 7 --limpiar
   ```

4. Va contando lo que hace. Con todas las fuentes puede tardar varios minutos, porque
   entra en cada noticia a por su texto.

Cuando termine, tendréis el `noticias.csv` actualizado en la carpeta de arriba, y solo hay
que **recargar el visor** para verlo.

---

## Si algo falla

**`python no se reconoce como un comando`.** No está instalado, o no se marcó «Add
python.exe to PATH». Se arregla reinstalando y marcando esa casilla.

**Se abre la Microsoft Store al escribir `python`.** Es un Python falso que trae Windows.
Instalad el de python.org como dice el paso 2.

**Tarda muchísimo.** Es normal: entra en cada noticia una por una. Probad con `--dias 3`
para que sean menos, o con `--fuentes "Construible,BOE"` para limitarlo a dos medios.

**Alguna fuente falla.** El script lo dice al final y sigue con las demás. No es un error
vuestro: hay webs que se caen o que bloquean las descargas.

**No aparece `noticias.csv`.** Mirad en la carpeta de arriba, no en esta: el script lo
escribe junto al visor, que es donde tiene que estar.
