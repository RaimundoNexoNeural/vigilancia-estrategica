---
name: clasificar-noticias
description: Clasifica un conjunto de noticias contra unas categorías y un criterio que decide el usuario, y devuelve el CSV original con columnas nuevas de clasificación. Úsala cuando pidan clasificar, categorizar, ordenar o etiquetar noticias de vigilancia.
---

# Clasificar noticias

Ordena un conjunto de noticias contra **una estructura de categorías que decide la casa,
no la máquina**.

## Lo que hay que preguntar antes de empezar

Si la persona no lo ha dicho, pregunta **las dos cosas a la vez** y propón el andamio de
abajo como punto de partida, diciendo expresamente que es para tirarlo:

1. **Qué campos** quiere, y qué valores admite cada uno.
2. **Qué criterio** se aplica al decidir.

Andamio de partida:

```
tema_principal   la categoría temática principal (lista de abajo)
tema_secundaria  la segunda, si encaja en dos
ambito           europeo / estatal / autonómico / provincial o local
tipo             normativa · financiación · mercado · tecnología · evento ·
                 proyecto · social
horizonte        inmediato (este año) / medio (1-3 años) / largo (más de 3)
a_quien_afecta   qué área de la casa debería leer esto
```

Categorías de partida para `tema_principal`, salidas de la sesión del 23 de septiembre:

> Políticas de vivienda · Políticas sociales y necesidades sociales · Administración
> pública · Financiación y fondos europeos · Proyectos e innovación técnica · Eficiencia
> energética y energía · Mercado: alquiler, compraventa e hipotecas · Suelo y urbanismo ·
> Rehabilitación y edificación · Economía general · AVRA, imagen y posicionamiento

Criterio de partida:

> Es pertinente lo que puede cambiar una decisión de la Agencia: su planificación, sus
> proyectos, su normativa aplicable, su parque de viviendas, su financiación o su
> posición pública. Lo que solo es de interés general no es pertinente, por muy
> importante que sea. Ante la duda entre dos categorías, manda el efecto sobre la
> Agencia, no el tema del titular.

**Di en voz alta que el campo que convierte un boletín en una decisión es
`a_quien_afecta`.** Sin él, el boletín informa a todo el mundo en general y a nadie en
particular.

## Cómo hacerlo

1. Lee **el texto de cada noticia**, no su titular. Clasificar por titular es justo lo
   que se viene a sustituir.
2. Asigna los campos pedidos aplicando el criterio.
3. Devuelve el CSV.

## Qué devolver

Un bloque de código con el CSV: **todas las columnas que traía cada noticia, en su mismo
orden, y a continuación las nuevas**. Más una última columna `por_que` con la razón de
la asignación en menos de quince palabras.

No quites columnas. No reordenes las que ya había. Las nuevas van al final.

Al terminar: cuántas por cada valor de cada campo, cuántas fuera de ámbito y cuántas
dudosas.

## Reglas, y son innegociables

- No inventes noticias, ni cifras, ni categorías que no estén en la lista acordada.
- Si encaja en más de una categoría: la principal y la secundaria, en ese orden.
- Si **no** encaja en ninguna, márcala `FUERA DE ÁMBITO`. No la fuerces: que sobre es
  información.
- Si es ambigua, márcala `DUDOSA` y di por qué.
- No resumas ni valores todavía: aquí solo se ordena.

## El contraste que hay que enseñar

Si el material trae una columna `relevancia_prefiltro`, está puesta por un criterio
**tonto a propósito**: mira palabras, no sentido.

Al terminar, **di en cuántas coincidís y en cuántas no**, y enseña dos o tres casos donde
el léxico y el sentido no dan lo mismo. Esa es, literalmente, la diferencia entre el
filtrado por palabra clave y el semántico.

## Antes de entregar, responde a esto

1. ¿En qué te has basado para cada asignación?
2. ¿Qué has supuesto sobre lo que significa cada categoría?
3. ¿Podría defenderse esta clasificación sin decir que la hizo una IA?
4. ¿Qué noticias no supiste clasificar, y por qué?
5. ¿Sirve esto para decidir algo, o solo para ordenar?

## Si la respuesta se corta

Es el límite de contexto, no un fallo. Continúa en bloques de 25 noticias **con la misma
tabla y las mismas columnas**, y no cambies el criterio a mitad: es el error más común al
trocear.
