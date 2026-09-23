# Prompt 2 · CLASIFICAR

**Para qué sirve.** Ordenar de una vez un montón de noticias contra **una estructura de
categorías que decidís vosotros, no la máquina**. Es el paso que convierte una lista en
algo que se puede filtrar y repartir.

**Qué le dais de comer.** El CSV del prompt 1, el `noticias.csv` que viene en esta
carpeta, o un pegote de titulares con sus enlaces. Con dos o tres noticias se ve cómo
funciona; el efecto de verdad se ve con cincuenta.

**Lo que tenéis que rellenar:** dos huecos, `CATEGORÍAS` y `CRITERIO`. Son la parte que
no puede poner nadie de fuera: son vuestras.

> **El prompt te devuelve el CSV y lo guardas tú.** Si usáis Claude Code, el comando
> `/clasificar` hace esto mismo escribiendo el fichero él solo.

---

## La plantilla

```
Actúa como documentalista de un sistema de vigilancia del entorno de una
agencia pública de vivienda y rehabilitación.

Te paso un conjunto de noticias. Cada una trae titular, fuente, fecha, URL y
el texto del artículo.

CATEGORÍAS
Clasifica cada noticia asignándole estos campos:
[  ▸ AQUÍ LOS CAMPOS Y SUS VALORES POSIBLES ◂  ]

CRITERIO
Aplica este criterio al decidir:
[  ▸ AQUÍ EL CRITERIO ◂  ]

QUÉ QUIERO DE VUELTA
Un CSV con TODAS las columnas que ya traía cada noticia, en su mismo orden, y
a continuación las columnas nuevas de la clasificación.

No quites ninguna columna de las que te he dado. No reordenes las que ya
había. Añade las nuevas al final.

Añade además una última columna llamada por_que, con la razón de la
asignación en menos de quince palabras.

REGLAS, Y SON INNEGOCIABLES
- No inventes noticias, ni cifras, ni categorías que no estén en mi lista.
- Si una noticia encaja en más de una categoría, indica la principal y la
  secundaria, en ese orden.
- Si una noticia NO encaja en ninguna, márcala FUERA DE ÁMBITO. No la
  fuerces. Que sobre es información.
- Si una noticia es ambigua, márcala DUDOSA y di por qué.
- Clasifica leyendo el texto, no el titular.
- No resumas ni valores todavía: aquí solo se ordena.

ANTES DE DARME LA TABLA, RESPONDE A ESTO
  1. ¿En qué te has basado para cada asignación?
  2. ¿Qué has supuesto sobre lo que significa cada categoría?
  3. ¿Podría yo defender esta clasificación sin decir que la hizo una IA?
  4. ¿Qué noticias no has sabido clasificar, y por qué?
  5. ¿Sirve esto para decidir algo, o solo para ordenar?

Al final: cuántas por categoría, cuántas fuera de ámbito y cuántas dudosas.
```

---

## Cómo se rellenan los dos huecos

### CATEGORÍAS

Esto es lo vuestro. **No se da hecho: se construye.** Lo que sigue es un andamio para
tirarlo en cuanto tengáis algo mejor:

```
- tema_principal: la categoría temática principal
- tema_secundaria: la segunda, si encaja en dos
- ambito: europeo / estatal / autonómico / provincial o local
- tipo: normativa · financiación · mercado · tecnología · evento · proyecto · social
- horizonte: inmediato (este año) / medio (1-3 años) / largo (más de 3)
- a_quien_afecta: qué área de la casa debería leer esto
```

Y para `tema_principal`, la lista que salió de la sesión del 23:

> Políticas de vivienda · Políticas sociales y necesidades sociales · Administración
> pública · Financiación y fondos europeos · Proyectos e innovación técnica ·
> Eficiencia energética y energía · Mercado: alquiler, compraventa e hipotecas ·
> Suelo y urbanismo · Rehabilitación y edificación · Economía general ·
> AVRA, imagen y posicionamiento

> **El campo que convierte un boletín en una decisión es `a_quien_afecta`.** Sin él, el
> boletín informa a todo el mundo en general y a nadie en particular.

### CRITERIO

Es lo que distingue «relevante» de «pertinente». Ejemplo, también para discutirlo:

```
Es pertinente lo que puede cambiar una decisión de la Agencia: su
planificación, sus proyectos, su normativa aplicable, su parque de viviendas,
su financiación o su posición pública. Lo que solo es de interés general no es
pertinente, por muy importante que sea.
Ante la duda entre dos categorías, manda el efecto sobre la Agencia, no el
tema del titular.
```

---

## Qué devuelve, y el momento que merece la pena

Un CSV con las columnas de antes **más las nuevas**. Al cargarlo en el visor, las
columnas nuevas aparecen solas, cada una con su filtro.

Y aquí está lo interesante: **el corpus ya viene con una etiqueta de relevancia puesta
por un criterio tonto a propósito**, que mira palabras y no sentido. Es la columna
`relevancia_prefiltro`.

**Comparad lo que marcó ese pre-filtro con lo que decide la IA leyendo el texto entero.**
Eso es, literalmente, la diferencia entre el filtrado por palabra clave que ya tenéis
montado y el semántico. Cuando no coinciden, mirad por qué: casi siempre es una noticia
que usa las palabras correctas para otra cosa, o una que habla de lo vuestro sin
nombrarlo.

En la sesión salió un ejemplo perfecto: una noticia sobre la **Directiva Europea de Agua
Potable** que el pre-filtro mandó *fuera* —no dice «vivienda»— y que resulta que impone
obligaciones sobre las instalaciones interiores de los edificios. Es decir, sobre el
parque que gestionáis.

---

## Cómo sé que está bien

Las cinco preguntas del final son los cinco criterios de la sesión 1. Aplicadas a
clasificar significan una cosa muy concreta: **el criterio está escrito**, así que otra
persona puede coger el mismo material, aplicarlo y llegar al mismo sitio.

Eso es exactamente lo contrario de preguntarle a un chat, que —como se dijo en la sesión
2— *«no deja trazabilidad, no se repite igual mañana»*.

---

## Si algo falla

**La respuesta se corta.** Es el límite de contexto, no un fallo. Partidlo en bloques de
25 noticias y pedid que continúe con la misma tabla y las mismas columnas. **Comprobad
que no ha cambiado el criterio a mitad**: es el error más común al trocear.

**Se inventa una categoría que no está en vuestra lista.** Repetid recordándole la regla
y, si insiste, es señal de que falta una categoría de verdad. Añadidla.

**Lo mete todo en la misma categoría.** Casi siempre es que el criterio está poco
concreto. Añadid un par de ejemplos: «una noticia sobre X va a la categoría Y».

**Devuelve menos filas de las que le disteis.** Ha descartado por su cuenta. Recordadle
que nada se elimina, que lo que no encaje se marca FUERA DE ÁMBITO.
