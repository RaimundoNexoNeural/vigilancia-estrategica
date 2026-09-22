# Prompt 2 · CLASIFICAR

**Para qué sirve.** Organizar de una vez un volumen de información que sería lento de
ordenar a mano, contra una estructura de categorías **que decide la casa, no la máquina**.

**Los dos huecos:** `CAMPOS` y `CRITERIO`. Se rellenan en la sesión, con lo que salga del
debate, porque son la parte que no puede poner el docente: son vuestras.

**Qué le das de comer.** Las noticias que tengas: el resultado del prompt 1, un lote de
ficheros del corpus, o un pegote de titulares con sus enlaces. Con dos o tres basta para
ver cómo funciona; el efecto real se ve con cincuenta.

---

## La plantilla

```
Actúa como documentalista de un sistema de vigilancia del entorno de una agencia
pública de vivienda y rehabilitación.

Te paso un conjunto de noticias. Cada una trae titular, fuente, fecha, URL y el
cuerpo del artículo.

CAMPOS
Clasifica cada noticia asignándole estos campos:
[  ▸ AQUÍ LOS CAMPOS ◂  ]

CRITERIO
Aplica este criterio al clasificar:
[  ▸ AQUÍ EL CRITERIO ◂  ]

QUÉ QUIERO DE VUELTA
Una tabla con una fila por noticia: identificador, titular abreviado, los campos
anteriores, y una última columna POR QUÉ con la razón de la asignación en menos
de quince palabras.

Dámelo en formato CSV, con la fila de cabecera, para poder abrirlo.

REGLAS, Y SON INNEGOCIABLES
- No inventes noticias, ni cifras, ni categorías que no estén en la lista.
- Si una noticia encaja en más de una categoría, indica la principal y la
  secundaria, en ese orden.
- Si una noticia NO encaja en ninguna, márcala FUERA DE ÁMBITO. No la fuerces.
  Que sobre es información.
- Si una noticia es ambigua, márcala DUDOSA y di por qué.
- Clasifica leyendo el cuerpo, no el titular.
- No resumas ni valores todavía: aquí solo se ordena.

ANTES DE DARME LA TABLA, RESPONDE A ESTO
  1. ¿En qué te has basado para cada asignación?
  2. ¿Qué supuestos has hecho sobre lo que significa cada categoría?
  3. ¿Podría yo defender esta clasificación sin decir que la hizo una IA?
  4. ¿Qué noticias no has sabido clasificar, y por qué?
  5. ¿Sirve esta clasificación para decidir algo, o solo para ordenar?

Al final: cuántas por categoría, cuántas fuera de ámbito y cuántas dudosas.
```

---

## Cómo se rellenan los huecos

### CAMPOS

Son la estructura de clasificación de la casa. **No se dan hechos: se construyen en la
sesión.** El punto de partida es lo que ya usáis; la pregunta es qué falta.

Andamio para tirarlo si no sirve:

```
- TEMA: la categoría temática principal (vuestra lista)
- ÁMBITO: europeo / estatal / autonómico / provincial o local
- TIPO: normativa · financiación · mercado · tecnología · evento · proyecto · social
- HORIZONTE: inmediato (este año) / medio (1-3 años) / largo (más de 3 años)
- A QUIÉN AFECTA: qué área de la casa debería leer esto
```

> El campo que convierte un boletín en una decisión es el último. Sin él, el boletín
> informa a todo el mundo en general y a nadie en particular.

### CRITERIO

Es lo que distingue «relevante» de «pertinente». Ejemplo, también para discutirlo:

```
Es pertinente lo que puede cambiar una decisión de la Agencia: su planificación,
sus proyectos, su normativa aplicable, su parque de viviendas, su financiación o
su posición pública. Lo que solo es de interés general no es pertinente, por muy
importante que sea.
Ante la duda entre dos categorías, manda el efecto sobre la Agencia, no el tema
del titular.
```

### La taxonomía de referencia

Las nueve categorías de primer nivel del boletín del SVPE: Mercados y economía · Políticas
de vivienda · Financiación pública · Otras políticas públicas · Necesidades sociales y de
vivienda · AVRA, imagen y posicionamiento · Novedades · Eventos · Proyectos e innovación
técnica.

**Ojo:** esas son las del **boletín**, que es el producto final. No tienen por qué ser las
mismas con las que clasificáis por dentro. Si son otras, mandan las vuestras.

---

## El truco que hace que esto se entienda

El corpus llega con una etiqueta de relevancia puesta por un criterio **tonto a
propósito**: mira palabras, no sentido.

Comparar lo que marcó ese pre-filtro con lo que decide la IA leyendo el cuerpo entero es,
literalmente, la diferencia entre **el filtrado por palabra clave que ya tenéis montado** y
el semántico. Cuando no coinciden, mirad por qué: casi siempre es una noticia que usa las
palabras correctas para otra cosa, o una que habla de lo vuestro sin nombrarlo.

---

## Cómo sabéis que la salida vale

Las cinco preguntas del final de la plantilla son **los cinco criterios de la sesión 1**
[S1 00:49:07-00:49:33]. Aplicadas a clasificar, significan una cosa muy concreta: **el
criterio está escrito**, así que otra persona puede coger el mismo material, aplicarlo y
llegar al mismo sitio.

Eso es exactamente lo contrario de preguntarle a un chat, que *«no deja trazabilidad, no
se repite igual mañana»* [S2 00:20:13].

---

## Si la respuesta se corta

Es el límite de contexto, no un fallo. Partidlo en bloques de 25 noticias y pedid que
continúe con la misma tabla y las mismas columnas. Y comprobad que no ha cambiado el
criterio a mitad: es el error más común cuando se trocea.
