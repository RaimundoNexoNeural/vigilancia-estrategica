# Vigilancia de noticias — instrucciones de la carpeta

Esto es **un folio de instrucciones, no código**. Dice qué hay aquí, con qué formato tiene
que salir todo y qué no se hace nunca. Está en castellano y se lee de arriba abajo.

Cualquiera puede escribir uno. De hecho, este fichero **es** el contenido que se enseñó en
la sesión: automatización de tareas de vigilancia sin necesidad de integración técnica.

---

## Qué hay aquí

```
noticias.csv     todas las noticias, una por fila, con su texto dentro
fuentes.csv      los medios que se vigilan (se edita como una tabla)
index.html       el visor: abre noticias.csv y lo deja navegable
1-prompts/       las plantillas para cualquier chat de IA
2-skills/        lo mismo, empaquetado para Claude del navegador
3-comandos/      esta carpeta: los comandos de Claude Code
4-script/        el descargador en Python, opcional
```

Para ver el corpus: doble clic en `index.html` y botón **«Abrir un CSV»**.

---

## EL CONTRATO

Hay **tres vías** para llenar `noticias.csv`: ejecutar el script, hacerlo directamente sin
él, o pegar el resultado de un chat. **Las tres tienen que producir lo mismo.** Si una se
desvía, el visor deja de entenderlo. Este es el formato, y no se negocia.

### Un solo fichero: `noticias.csv`

UTF-8 **con BOM**, separado por comas, campos con comas o saltos de línea entrecomillados.
Once columnas, en este orden:

| Columna | Qué lleva | Valores |
|---|---|---|
| `id` | número de orden, empieza en 1 | |
| `titular` | el titular literal | |
| `fuente` | el nombre del medio | |
| `fecha` | `AAAA-MM-DD HH:MM` | |
| `url` | el enlace al original, siempre | |
| `cuerpo` | el texto del artículo, párrafos separados por línea en blanco | |
| `cuerpo_completo` | si se pudo recuperar el texto | `si` · `parcial` · `no` |
| `motivo_cuerpo` | por qué es parcial o no; vacío si es completo | |
| `palabras_cuerpo` | número de palabras del cuerpo | |
| `relevancia_prefiltro` | la etiqueta provisional | `alta` · `dudosa` · `fuera` |
| `motivo_prefiltro` | la razón de esa etiqueta, en una frase | |

**Por qué el texto va dentro del CSV y no en ficheros aparte:** porque así **todo cabe en
un fichero**. El visor se abre con doble clic sin servidor, el CSV se abre en LibreOffice,
y cualquier herramienta de IA puede producir el entregable completo — ChatGPT o Gemini
devuelven un CSV, no saben devolver ciento cuarenta ficheros en carpetas.

**El pre-filtro no borra nada.** Lo que no viene al caso se marca como `fuera` y se queda.
El ejercicio trata de aprender a descartar, y para eso hace falta tener algo que descartar.

### Los resultados del trabajo

Clasificar y seleccionar **enriquecen el mismo fichero, no crean ficheros paralelos**. El
corpus es uno solo y va ganando columnas. El orden es siempre:

1. **Copia de seguridad** antes de tocar nada: `noticias-antes-de-clasificar.csv` o
   `noticias-antes-de-seleccionar.csv`. Permite deshacer en diez segundos.
2. **Fundir las columnas nuevas emparejando por `id`.** Cada fila trabajada gana sus
   columnas; las demás las reciben vacías. **Nunca se reemplaza el fichero entero**: en
   una sesión se trabaja una parte, y reemplazar borraría el resto.
3. Seleccionar deja además el informe en `seleccion.md`.

> **Primero se descarga, después se clasifica. Nunca al revés.** El descargador reescribe
> `noticias.csv` con sus once columnas y descarta en silencio cualquier otra, así que
> volver a descargar después de clasificar **borra la clasificación**. Si hay que ampliar
> el corpus, se descarga y se vuelve a clasificar.

### Para deshacer

| Qué se quiere | Qué se copia sobre `noticias.csv` |
|---|---|
| Quitar la última selección | `noticias-antes-de-seleccionar.csv` |
| Quitar selección y clasificación | `noticias-antes-de-clasificar.csv` |
| Dejarlo como recién descargado | nada: se vuelve a ejecutar el descargador |

Las copias guardan **solo el estado inmediatamente anterior**: se rehacen en cada pasada.

---

## Las categorías contra las que se clasifica

Salieron del debate de la sesión del 23 de septiembre, dictadas por el equipo:

Políticas de vivienda · Políticas sociales y necesidades sociales · Administración
pública · Financiación y fondos europeos · Proyectos e innovación técnica · Eficiencia
energética y energía · Mercado: alquiler, compraventa e hipotecas · Suelo y urbanismo ·
Rehabilitación y edificación · Economía general · AVRA, imagen y posicionamiento

**No son definitivas y no hay que darlas por buenas.** Son un punto de partida para que la
casa las corrija. Si el equipo usa otras por dentro, mandan las suyas.

---

## Reglas que no se negocian

1. **Cada noticia, con su URL de origen.** Sin enlace no entra.
2. **No se inventa nada**: ni un titular, ni una cifra, ni una fecha, ni un enlace. Si no
   se tiene, se dice que no se tiene.
3. **Lo que no se pueda verificar se marca expresamente.** Distinguir siempre lo que dice
   la fuente de lo que se deduce.
4. **No se sale de esta carpeta.** Ni para leer ni para escribir.
5. **No se modifican el visor ni el script.** Están validados y funcionando.
6. **Al descargar sin script no se invoca el script** ni se crean ficheros de programa
   nuevos. Se puede usar la shell libremente y replicar en línea lo que hace, pero el
   objetivo es enseñar que se puede hacer sin él.

---

## Lo mismo, en tres envoltorios

Cada comando de `commands/` tiene su gemelo en `1-prompts/` y en `2-skills/`. **Dicen lo
mismo, con las mismas secciones y el mismo criterio.** La única diferencia:

- **El comando escribe el fichero.**
- **El prompt y la skill te devuelven el CSV y lo guardas tú.**

Eso permite que quien empiece con Gemini y luego se pase a Claude Code no tenga que
reaprender nada, y que un cambio de criterio se aplique en los tres sitios sin traducir.
