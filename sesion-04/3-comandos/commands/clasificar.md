---
description: Clasifica las noticias con los campos y el criterio que se decidan
argument-hint: [campos separados por comas] [criterio] [fichero, por defecto noticias.csv]
---

# Clasificar

**Para qué sirve.** Ordenar de una vez todas las noticias contra **una estructura de
categorías que decide la casa, no la máquina**.

**Campos:** $1 · **Criterio:** $2 · **Fichero:** $3

Si no viene fichero, usa `noticias.csv`. Si no vienen campos ni criterio, **no te los
inventes en silencio**: propón los de abajo, di que son un andamio para tirarlo, y sigue
con ellos.

> **Este comando escribe el fichero.** La versión para pegar en cualquier chat es
> `1-prompts/02-clasificar.md`.

## Lo que tienes que rellenar

Los campos y el criterio **salen del debate con el grupo**. Este comando se ejecuta
*después* de esa conversación, no antes.

Andamio de partida:

- `tema_principal` — la categoría temática principal
- `tema_secundaria` — la segunda, si encaja en dos
- `ambito` — europeo · estatal · autonómico · provincial o local
- `tipo` — normativa · financiación · mercado · tecnología · evento · proyecto · social
- `horizonte` — inmediato (este año) · medio (1-3 años) · largo (más de 3)
- `a_quien_afecta` — qué área de la casa debería leer esto

> El campo que convierte un boletín en una decisión es el último. Sin él, el boletín
> informa a todo el mundo en general y a nadie en particular.

Categorías de partida para `tema_principal`, las que salieron de la sesión del 23:

> Políticas de vivienda · Políticas sociales y necesidades sociales · Administración
> pública · Financiación y fondos europeos · Proyectos e innovación técnica · Eficiencia
> energética y energía · Mercado: alquiler, compraventa e hipotecas · Suelo y urbanismo ·
> Rehabilitación y edificación · Economía general · AVRA, imagen y posicionamiento

Criterio de partida, también para discutirlo:

> Es pertinente lo que puede cambiar una decisión de la Agencia: su planificación, sus
> proyectos, su normativa aplicable, su parque de viviendas, su financiación o su
> posición pública. Lo que solo es de interés general no es pertinente, por muy
> importante que sea. Ante la duda entre dos categorías, manda el efecto sobre la
> Agencia, no el tema del titular.

## Qué hace

**Paso 0, y no se salta nunca.** Antes de tocar nada, copia el fichero a
`noticias-antes-de-clasificar.csv`. Es lo que permite volver atrás en diez segundos si la
salida sale mal, y esto se hace en directo delante de un grupo.

1. Lee el fichero y, de cada noticia, **la columna `cuerpo`**. Se clasifica leyendo el
   texto, no el titular: clasificar por titular es justo lo que venimos a sustituir.
2. Asigna a cada noticia los campos pedidos, aplicando el criterio.
3. **Funde las columnas nuevas dentro del mismo fichero, emparejando por `id`.**

## Qué devuelve

El mismo `noticias.csv`, con **las columnas de siempre intactas y en su orden**, y las
nuevas a continuación. Más una columna `por_que` con la razón de la asignación en menos
de quince palabras. UTF-8 con BOM.

### La fusión, que es donde se rompen las cosas

**Fundir no es reemplazar.** En una sesión no se clasifican las 145 noticias: se
clasifican las que dé tiempo. Si escribes el fichero solo con las filas clasificadas,
**borras el resto**.

- Se recorre el fichero entero, fila a fila.
- A la fila cuyo `id` esté clasificado se le añaden las columnas nuevas con sus valores.
- A la que no lo esté se le añaden **las mismas columnas, vacías**.
- Las columnas originales se quedan **intactas y en su orden**. Nunca se corrigen, se
  reordenan ni se reescriben: son la descarga, y la descarga no se discute.

Si algo no cuadra —un `id` que no existe, filas con distinto número de columnas—,
**párate y dilo**. No escribas un fichero a medias: el visor lo lee y la sesión se cae.

## Reglas innegociables

- Si encaja en más de una categoría, la principal y la secundaria, en ese orden.
- Si **no** encaja en ninguna, márcala `FUERA DE ÁMBITO`. No la fuerces: que sobre es
  información.
- Si es ambigua, márcala `DUDOSA` y di por qué.
- No inventes categorías que no estén en la lista acordada.
- No resumas ni valores todavía: aquí solo se ordena.

## El pre-filtro ya está puesto, y sirve para comparar

El fichero llega con `relevancia_prefiltro`, puesto por un criterio **tonto a propósito**:
mira palabras, no sentido.

**Comparar lo que marcó el pre-filtro con lo que decides tú leyendo el texto es media
clase.** Al terminar, di en cuántas coincidís y en cuántas no, y enseña dos o tres casos
donde el léxico y el sentido no dan lo mismo.

## Cómo sé que está bien

Las cinco preguntas de la sesión 1: de dónde vienen los datos, si se han declarado los
supuestos, si se puede defender *«sin decir que lo dijo la IA»*, si se sabe que faltan
datos, y si esto acerca a una decisión.

Aplicadas aquí significan una cosa concreta: **el criterio está escrito**, así que
cualquiera puede coger el mismo material, aplicarlo y llegar al mismo sitio. Es lo
contrario de preguntarle a un chat, que *«no deja trazabilidad, no se repite igual
mañana»*.

## Al terminar

- Cuántas noticias se han clasificado y cuántas se han quedado sin clasificar.
- Cuántas por cada valor de cada campo nuevo.
- Cuántas fuera de ámbito y cuántas dudosas.
- Dónde discrepa la clasificación del pre-filtro.
- Y cómo verlo: **basta con recargar el visor**. Las columnas nuevas aparecen solas, con
  sus filtros.

## Si algo falla

- **Deshacer**: copiar `noticias-antes-de-clasificar.csv` sobre `noticias.csv`.
- **Se corta a mitad.** Continúa en bloques de 25, con las mismas columnas y **sin
  cambiar el criterio**, que es el error más común al trocear.
- **Esto va después de descargar, nunca antes.** El script reescribe `noticias.csv` con
  sus once columnas y descarta el resto sin avisar: volver a descargar después de
  clasificar **borra la clasificación**.
