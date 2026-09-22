---
description: Clasifica el corpus con los campos y el criterio que se decidan en clase
argument-hint: [campos separados por comas] [criterio] [corpus, por defecto corpus/]
---

# Clasificar

Organiza de una vez todo el corpus contra una estructura de categorías **que decide la
casa, no la máquina**.

**Campos:** $1 · **Criterio:** $2 · **Corpus:** $3

Si no viene corpus, usa `corpus/`. Si no vienen campos ni criterio, **no te los inventes
en silencio**: propón los de abajo como punto de partida, di que son un andamio para
tirarlo, y sigue con ellos.

## La parte que no es tuya

Los campos y el criterio salen del debate con el grupo. Este comando se ejecuta **después**
de esa conversación, no antes. Si te llegan vacíos, el andamio es:

- `tema` — la categoría temática principal
- `ambito` — europeo · estatal · autonómico · provincial o local
- `tipo` — normativa · financiación · mercado · tecnología · evento · proyecto · social
- `horizonte` — inmediato (este año) · medio (1-3 años) · largo (más de 3)
- `a_quien_afecta` — qué área de la Agencia debería leer esto

> El campo que convierte un boletín en una decisión es el último. Sin él, el boletín
> informa a todo el mundo en general y a nadie en particular.

Criterio de partida, también para discutirlo: *es pertinente lo que puede cambiar una
decisión de la Agencia —su planificación, sus proyectos, su normativa aplicable, su parque
de viviendas, su financiación o su posición pública—. Lo que solo es de interés general no
es pertinente, por muy importante que sea. Ante la duda entre dos categorías, manda el
efecto sobre la Agencia, no el tema del titular.*

La taxonomía de referencia son las nueve categorías del boletín del SVPE, que están en el
`CLAUDE.md`. **Recuerda en voz alta que son las del producto final** y que la de
clasificación hay que confirmarla con ellos.

## Cómo hacerlo

**Paso 0, y no se salta nunca.** Antes de tocar nada, copia `<corpus>/indice.csv` a
`<corpus>/indice-antes-de-clasificar.csv`. Es lo que permite volver atrás en diez
segundos si la salida sale mal, y esto se hace en directo delante de un grupo.

1. Lee `<corpus>/indice.csv` y, de cada noticia, **su ficha en `noticias/`**. Se clasifica
   leyendo el cuerpo, no el titular: clasificar por titular es justo lo que venimos a
   sustituir.
2. Asigna a cada noticia los campos pedidos, aplicando el criterio.
3. Escribe `<corpus>/clasificado.csv` con **las once columnas originales en su orden y, a
   continuación, las nuevas**. Añade además una columna `por_que` con la razón de la
   asignación en menos de quince palabras. Este fichero es el registro de lo que dijo la
   máquina antes de que nadie lo tocara: es la trazabilidad, no un borrador.
4. **Funde esas columnas nuevas dentro de `<corpus>/indice.csv`, emparejando por `id`.**
   El corpus es uno solo y va ganando columnas; no se crea un índice paralelo.
5. UTF-8 con BOM en los dos, como el resto.

## Reglas al clasificar

- Si una noticia encaja en más de una categoría, indica la principal y la secundaria, en
  ese orden.
- Si **no** encaja en ninguna, márcala `FUERA DE ÁMBITO`. No la fuerces: que sobre es
  información.
- Si es ambigua, márcala `DUDOSA` y di por qué.
- No inventes categorías que no estén en la lista acordada.

## La fusión, que es donde se rompen las cosas

**Fundir no es reemplazar.** En una sesión no se clasifican las 128 noticias: se
clasifican las que dé tiempo. Si escribes `indice.csv` solo con las filas clasificadas,
**borras el resto del corpus**.

La regla, entonces:

- Se recorre `indice.csv` entero, fila a fila.
- A la fila cuyo `id` esté clasificado se le añaden las columnas nuevas con sus valores.
- A la que no lo esté se le añaden **las mismas columnas, vacías**.
- Las once originales se quedan **intactas y en su orden**. Nunca se corrigen, se
  reordenan ni se reescriben: son la descarga, y la descarga no se discute.
- La cabecera pasa a tener las once de siempre más las nuevas, en el mismo orden para
  todas las filas.

Si algo no cuadra —un `id` que no existe, un número de columnas distinto entre filas—,
**párate y dilo**. No escribas un índice a medias: el visor lo lee y la sesión se cae.

## Esto va después de descargar, nunca antes

`descargar_corpus.py` reescribe `indice.csv` con sus once columnas y **descarta en
silencio cualquier otra**. Volver a descargar después de clasificar borra la
clasificación sin avisar. Si hay que ampliar el corpus: primero descargar, después
clasificar otra vez.

## El pre-filtro ya está puesto, y sirve para comparar

El corpus llega con `relevancia_prefiltro` (`alta`, `dudosa`, `fuera`), puesto por un
criterio tonto a propósito: mira palabras, no sentido.

**Comparar lo que marcó el pre-filtro con lo que decides tú leyendo el cuerpo es media
clase.** Al terminar, di explícitamente en cuántas coincidís y en cuántas no, y enseña dos
o tres casos donde el léxico y el sentido no dan lo mismo. Eso es, literalmente, la
diferencia entre el filtrado por palabra clave que ya tienen montado y el semántico.

## Cómo se comprueba que está bien

Las cinco preguntas de la sesión 1 [S1 00:49:07-00:49:33], reconstruidas de la grabación:
de dónde vienen los datos, si la IA ha declarado sus supuestos, si se puede defender el
resultado *«sin decir que lo dijo la IA»*, si se sabe que faltan datos, y si esto acerca a
una decisión.

Aplicadas aquí significan una cosa concreta: **el criterio está escrito**, así que
cualquiera puede coger el mismo corpus, aplicarlo y llegar al mismo sitio. Es lo contrario
de preguntarle a un chat, que —como se dijo en la sesión 2 [S2 00:20:13]— *«no deja
trazabilidad, no se repite igual mañana»*.

## Al terminar

- Cuántas noticias se han clasificado y cuántas se han quedado sin clasificar.
- Cuántas por cada valor de cada campo nuevo.
- Cuántas fuera de ámbito y cuántas dudosas.
- Dónde discrepa la clasificación del pre-filtro.
- Y cómo verlo: **basta con recargar el visor (F5)**. El índice ya lleva las columnas
  nuevas y aparecen solas, con sus filtros. No hay que cargar ningún fichero.

Si la salida no convence, se deshace copiando `indice-antes-de-clasificar.csv` encima de
`indice.csv`. Y si se prefiere mirar el resultado sin tocar el corpus, en el visor está
**Cargar CSV** para abrir `clasificado.csv` por separado.
