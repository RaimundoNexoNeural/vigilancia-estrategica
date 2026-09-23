---
name: seleccionar-noticias
description: De un conjunto de noticias ya clasificado, selecciona las que merecen llegar a un boletín aplicando un criterio explícito, y devuelve el CSV marcado más un informe con temas, descartes, hallazgos y límites. Úsala cuando pidan seleccionar, priorizar, filtrar para boletín o preparar un informe de vigilancia.
---

# Seleccionar noticias

De todo lo clasificado, quedarse con lo que merece llegar a alguien. **No es resumir: es
priorizar con un criterio explícito y escrito**, que es lo que hace el resultado
auditable y repetible.

## Lo que hay que preguntar antes de empezar

**El criterio de selección.** Uno solo, y lo dicta la casa. Si no lo dan, propón este y
di expresamente que es para discutirlo:

> Selecciona lo que cumpla al menos una: obliga o puede obligar a la Agencia a hacer algo
> distinto de lo que hace; abre o cierra una vía de financiación; afecta al parque
> público de viviendas o a su rehabilitación; menciona a la Agencia o a Andalucía de
> forma directa; o es una tecnología o método que cambia cómo se construye o se
> rehabilita. Máximo quince seleccionadas; si hay más candidatas, prioriza por efecto
> sobre la Agencia, no por importancia general.

**Advierte de una cosa, porque es el aprendizaje del ejercicio:** el número de
seleccionadas depende de la frase, no de la herramienta. Con el criterio de arriba salen
unas quince de 145; con solo «lo que obligue a la Agencia a hacer algo distinto», salen
tres. Si al usuario le parecen pocas, lo que hay que cambiar es el criterio.

## Qué devolver

**Primero, el CSV completo**: todas las columnas que traía, en su orden, más estas tres
al final:

| Columna | Qué lleva |
|---|---|
| `seleccionada` | `si` / `no`. Nunca en blanco |
| `motivo_seleccion` | en las elegidas, qué parte del criterio cumple |
| `criterio_seleccion` | el criterio literal, **igual en todas las filas**, para que dentro de dos semanas se sepa con qué frase se decidió |

**Después, el informe**, con cinco bloques:

**1 · Las seleccionadas.** Cada una en 50 palabras como mucho: qué ha pasado, por qué
importa a la Agencia, y qué habría que vigilar a partir de ahora. Con su URL.

**2 · Los temas del conjunto.** Tres a cinco que se repitan, con las noticias que
sostienen cada uno. Los temas salen de lo que hay, no de lo que suele haber.

**3 · Lo que se descarta y por qué.** Agrupado por motivo, no una por una.

**4 · Los hallazgos**, con estos cuatro nombres, que son el vocabulario de la casa:

- **Ruido**: aparece mucho sobre algo concreto, pero no cambia decisiones.
- **Tendencia emergente**: se repite y empieza a afectar a un grupo.
- **Señal débil**: empieza a parecer algo que podría cambiar el escenario.
- **Cambio estructural**: ya ha cambiado el escenario.

En las señales débiles, di **explícitamente qué haría falta ver para confirmarlas**.

**5 · Lo que no puedes saber.** Qué preguntas no se pueden responder con este material y
qué habría que ir a buscar fuera.

Este quinto bloque está puesto a propósito. La IA sintetiza lo que ya existe; las
preguntas difíciles de un sistema de vigilancia maduro exigen **producir información que
todavía no existe** —consultar a empresas, mandar un formulario, ir al dato primario—.
Declarar el propio límite es lo que convierte esto en un punto de partida para el
analista, y no en un informe que alguien firma sin comprobar.

## Reglas, y son innegociables

- Cero invención: ni cifras, ni citas, ni enlaces. Todo sale del material.
- Si una afirmación no está sostenida por una noticia concreta, no la hagas.
- Distingue siempre lo que dice la fuente de lo que infieres tú, y márcalo.
- No adornes ni valores positivamente el resultado.

## Antes de entregar, responde a esto

1. ¿De dónde sale cada afirmación?
2. ¿Qué has dado por supuesto al aplicar el criterio?
3. ¿Podría defenderse esta selección sin decir que la hizo una IA?
4. ¿Qué falta para que esto esté completo?
5. ¿Acerca esto a una decisión concreta? ¿A cuál?

## Al terminar, propón el contraste crítico

Tres preguntas, para hacerlas en voz alta y sin herramienta:

1. ¿Qué ha acertado?
2. ¿Qué se ha dejado fuera que vosotros sí habríais metido?
3. **¿Qué de esto no firmaríais sin comprobarlo?**

La respuesta a la tercera es la que hay que escribir, porque es el procedimiento de
verificación de la casa. Es hacer de **abogado del diablo** con la herramienta.

Y una variante que funciona: **usar otra herramienta para controlar esta salida**,
pidiéndole que verifique y que dé los enlaces concretos.
