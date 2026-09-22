# Vigilancia estratégica — carpeta de trabajo de la sesión

Esto es un **folio de instrucciones**, no código. Dice qué hay en esta carpeta, con qué
formato tiene que salir todo y qué no se hace nunca. Cualquiera puede escribir uno: está
en castellano y se lee de arriba abajo.

---

## Qué hay aquí

```
corpus/          lo descargado
  noticias/      una ficha .md por noticia, legible por sí sola
  indice.csv     la tabla del corpus — manda las columnas del visor
  datos/         series de datos abiertos, cada CSV con su ficha .md
  datos.js       índice de esos conjuntos
prompts/         las tres plantillas que se llevan los alumnos
script/          los dos descargadores en Python y fuentes.csv
visor/           la tabla navegable, en el navegador
```

Para ver el corpus: `servir-visor.bat`, y abrir <http://127.0.0.1:8080/visor/>.

> **En el material publicado la disposición cambia un poco**: el visor no está en
> `visor/`, sino que es el `index.html` de la raíz, y se levanta con `abrir-visor.bat`.
> Todo lo demás —`corpus/`, `prompts/`, `script/`— está igual, así que este contrato
> vale para las dos.

---

## EL CONTRATO

Hay **dos vías** para llenar el corpus: ejecutar los scripts de `script/`, o hacerlo
directamente sin ellos. **Las dos tienen que producir exactamente lo mismo.** Si una se
desvía, el visor deja de leer el índice y la sesión se cae. Este es el formato, y no se
negocia.

### Cada noticia: un fichero Markdown

Ruta y nombre: `corpus/noticias/AAAAMMDD_NNN_titular-en-minusculas.md`, donde `AAAAMMDD`
es la fecha de publicación, `NNN` el número de orden con tres dígitos, y el titular sin
acentos, en minúsculas y con guiones, cortado a 60 caracteres.

Codificación: **UTF-8 con BOM**. Sin BOM, el navegador adivina mal y se rompen los
acentos.

Estructura, en este orden exacto:

```markdown
---
titular: El titular tal cual lo publica el medio
fuente: Nombre de la fuente
fecha: 2026-09-22 19:42
url: https://…
cuerpo_completo: si
relevancia_prefiltro: alta
---

# El titular tal cual lo publica el medio

**Nombre de la fuente** · 2026-09-22 19:42 · [ver original](https://…)

> La entradilla, si la hay, como cita.

Primer párrafo del cuerpo.

Segundo párrafo del cuerpo.
```

Si no se ha podido recuperar el texto, en lugar del cuerpo va, en cursiva, que no se pudo
recuperar y que el enlace lleva al original. Si hay algo que advertir —un muro de pago,
una página cortada—, va al final separado por `---` y en cursiva.

### El índice: `corpus/indice.csv`

**Once columnas, en este orden, sin excepción.** CSV con BOM, separado por comas, campos
con comas o comillas entrecomillados.

| Columna | Qué lleva |
|---|---|
| `id` | número de orden, empieza en 1 |
| `archivo` | ruta relativa: `noticias/AAAAMMDD_NNN_titular.md` |
| `titular` | el titular literal |
| `fuente` | el nombre de la fuente |
| `fecha` | `AAAA-MM-DD HH:MM` |
| `url` | el enlace al original, siempre |
| `cuerpo_completo` | `si`, `parcial` o `no` |
| `motivo_cuerpo` | por qué es parcial o no; vacío si es completo |
| `palabras_cuerpo` | número de palabras del cuerpo |
| `relevancia_prefiltro` | `alta`, `dudosa` o `fuera` |
| `motivo_prefiltro` | la razón de esa etiqueta, en una frase |

Valores cerrados: `cuerpo_completo` solo puede ser `si`, `parcial` o `no`.
`relevancia_prefiltro` solo puede ser `alta`, `dudosa` o `fuera`.

**El pre-filtro no borra nada.** Lo que no viene al caso se marca como `fuera` y se queda
en el corpus: el ejercicio de la sesión trata justamente de aprender a descartar, y para
eso hace falta tener algo que descartar.

### Los resultados de la sesión

Clasificar **enriquece el índice, no crea un índice paralelo**. El corpus es uno solo y va
ganando columnas. El orden es siempre este:

1. Copiar `corpus/indice.csv` a `corpus/indice-antes-de-clasificar.csv`. Siempre, y antes
   de tocar nada. Es lo que permite deshacer en diez segundos.
2. Escribir la salida cruda en `corpus/clasificado.csv`, con **las once columnas
   originales en su orden y las nuevas a continuación**. Es el registro de qué dijo la
   máquina antes de que nadie lo tocara: sin él no hay trazabilidad.
3. **Fundir en `corpus/indice.csv` emparejando por `id`.** Cada fila clasificada gana sus
   columnas nuevas; las filas que no se hayan clasificado se quedan con esas columnas
   vacías. **Nunca se reemplaza el fichero entero**: en una sesión se clasifica una parte
   del corpus, y reemplazar borraría el resto.

Seleccionar hace lo mismo un escalón más arriba: copia de seguridad en
`indice-antes-de-seleccionar.csv`, el informe en `corpus/seleccion.md`, y tres columnas
más fundidas por `id` en `indice.csv` — `seleccionada` (`si` / `no`), `motivo_seleccion`
y `criterio_seleccion`, que guarda la frase con la que se decidió. Así lo elegido se
filtra en el visor, y dentro de dos semanas se sabe de dónde salió.

Si se le pasa una **etiqueta**, esas tres columnas llevan su sufijo
(`seleccionada_ancho`…) y **dos selecciones distintas conviven** en vez de pisarse.

### Para deshacer

| Qué se quiere | Qué se copia sobre `indice.csv` |
|---|---|
| Quitar la última selección | `indice-antes-de-seleccionar.csv` |
| Quitar selección y clasificación | `indice-antes-de-clasificar.csv` |
| Dejarlo como recién descargado | nada: se vuelve a ejecutar el descargador |

Las copias guardan **solo el estado inmediatamente anterior**: se rehacen en cada pasada.

> **Primero se descarga, después se clasifica. Nunca al revés.** `descargar_corpus.py`
> reescribe `indice.csv` con sus once columnas y descarta en silencio cualquier otra, así
> que volver a descargar después de clasificar **borra la clasificación**. Si hay que
> ampliar el corpus, se descarga y se vuelve a clasificar.

---

## La taxonomía contra la que se clasifica

Estas son las nueve categorías de primer nivel del boletín quincenal del SVPE de AVRA:

1. Mercados y economía
2. Políticas de vivienda
3. Financiación pública
4. Otras políticas públicas
5. Necesidades sociales y de vivienda
6. AVRA, imagen y posicionamiento
7. Novedades
8. Eventos
9. Proyectos e innovación técnica

**Cuidado con darlas por buenas.** Son las del **producto final**, el boletín. No hay
confirmación de que sean las mismas con las que se clasifica por dentro, que puede ser un
conjunto distinto y más detallado. **Hay que preguntarlo**, y si la respuesta es otra,
manda la suya.

---

## Reglas que no se negocian

1. **Cada elemento, con su URL de origen.** Sin enlace no entra.
2. **No se inventa nada**: ni un titular, ni una cifra, ni una fecha, ni un enlace. Si no
   se tiene, se dice que no se tiene.
3. **Lo que no se pueda verificar se marca expresamente.** Distinguir siempre lo que dice
   la fuente de lo que se deduce.
4. **No se sale de esta carpeta.** Ni para leer ni para escribir.
5. **No se modifican el visor ni los scripts.** Están validados y funcionando.
6. **Al descargar sin script no se invocan los scripts existentes** ni se crean ficheros
   de script nuevos. Se puede usar la shell libremente y replicar en línea lo que hacen,
   pero el objetivo es enseñar que se puede hacer sin ellos.

---

## Por qué esto es el contenido de la sesión

El contenido aprobado número 5 del módulo es *«automatización ligera de tareas de
vigilancia sin necesidad de integración técnica»*. Este fichero **es** ese contenido: un
texto en castellano que fija el formato de salida, el criterio y los límites. No hay nada
aquí que requiera saber programar.

Lo mismo vale para los ficheros de `.claude/commands/`: cada uno es un encargo escrito.
Lo que se ejecuta en pantalla es exactamente el texto que los alumnos se llevan en
`prompts/`, adaptado para funcionar pegado en cualquier chat.
