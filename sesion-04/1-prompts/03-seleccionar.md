# Prompt 3 · SELECCIONAR

**Para qué sirve.** De todo lo clasificado, quedarse con lo que merece llegar a alguien.
No es resumir: es **priorizar con un criterio explícito y escrito**, que es lo que hace
el resultado auditable y repetible. Eso es exactamente lo que no tiene preguntarle a un
chat.

**Lo que tenéis que rellenar:** un solo hueco, el `CRITERIO DE SELECCIÓN`. Y lo dicta la
casa.

> **El prompt te devuelve el CSV y el informe, y los guardas tú.** Si usáis Claude Code,
> el comando `/seleccionar` hace lo mismo escribiendo los ficheros él solo.

---

## La plantilla

```
Actúa como analista de vigilancia de una agencia pública de vivienda y
rehabilitación. Te paso el conjunto de noticias ya clasificado.

CRITERIO DE SELECCIÓN
[  ▸ AQUÍ EL CRITERIO ◂  ]

QUÉ QUIERO DE VUELTA

PRIMERO, el CSV completo: todas las columnas que ya traía, en su orden, más
estas tres nuevas al final:
  seleccionada        si / no. Nunca en blanco.
  motivo_seleccion    en las elegidas, qué parte del criterio cumple
  criterio_seleccion  el criterio literal que te he dado, igual en todas las
                      filas, para que dentro de dos semanas se sepa con qué
                      frase se decidió esto

DESPUÉS, el informe, con cinco bloques:

1) LAS SELECCIONADAS. Para cada una, en 50 palabras como mucho:
   - QUÉ HA PASADO
   - POR QUÉ IMPORTA a la Agencia
   - QUÉ HABRÍA QUE VIGILAR a partir de ahora
   Con su URL.

2) LOS TEMAS DEL CONJUNTO. Tres a cinco temas que se repiten, con las
   noticias que sostienen cada uno. Los temas salen de lo que hay, no de lo
   que suele haber.

3) LO QUE SE DESCARTA Y POR QUÉ. Agrupado por motivo, no una por una.

4) LOS HALLAZGOS, con estos cuatro nombres:
   - RUIDO: aparece mucho sobre algo concreto, pero no cambia decisiones.
   - TENDENCIA EMERGENTE: se repite y empieza a afectar a un grupo.
   - SEÑAL DÉBIL: empieza a parecer algo que podría cambiar el escenario.
   - CAMBIO ESTRUCTURAL: ya ha cambiado el escenario.
   En las señales débiles, di QUÉ HARÍA FALTA VER para confirmarlas.

5) LO QUE NO PUEDES SABER. Qué preguntas no se pueden responder con este
   material y qué habría que ir a buscar fuera para responderlas.

REGLAS, Y SON INNEGOCIABLES
- Cero invención: ni cifras, ni citas, ni enlaces. Todo sale del material.
- Si una afirmación no está sostenida por una noticia concreta, no la hagas.
- Distingue siempre lo que dice la fuente de lo que infieres tú. Márcalo.
- No adornes ni valores positivamente el resultado.

ANTES DE DARME NADA, RESPONDE A ESTO
  1. ¿De dónde sale cada afirmación?
  2. ¿Qué has dado por supuesto al aplicar el criterio?
  3. ¿Podría yo defender esta selección sin decir que la hizo una IA?
  4. ¿Qué falta para que esto esté completo?
  5. ¿Acerca esto a una decisión concreta? ¿A cuál?
```

---

## Cómo se rellena el hueco

Ejemplo de criterio, para discutirlo y cambiarlo:

```
Selecciona lo que cumpla al menos una:
 - Obliga o puede obligar a la Agencia a hacer algo distinto de lo que hace.
 - Abre o cierra una vía de financiación.
 - Afecta al parque público de viviendas o a su rehabilitación.
 - Menciona a la Agencia o a Andalucía de forma directa.
 - Es una tecnología o método que cambia cómo se construye o se rehabilita.
Máximo 15 seleccionadas. Si hay más candidatas, prioriza por efecto sobre la
Agencia, no por importancia general.
```

### El número que salga depende de la frase que pongáis, y eso es lo importante

En la sesión se probaron los dos extremos sobre el mismo corpus de 145 noticias:

| Criterio | Seleccionadas |
|---|---|
| Solo «lo que obligue a la Agencia a hacer algo distinto» | **3** |
| El criterio ancho de arriba, con sus cinco condiciones | **15** |

Misma máquina, mismo material, **una frase distinta**. Si os salen pocas, el problema no
es la herramienta: es el criterio. Cambiadlo y volved a lanzarlo.

---

## Los cuatro nombres del bloque 4 son vuestros, no nuestros

Salieron en la sesión 2:

> *«el ruido, aparece mucho ruido sobre algo concreto pero no cambia decisiones»* ·
> *«tendencia emergente, se repite y empieza a afectar a un grupo»* · *«señal débil,
> empieza a parecer algo que podría cambiar el escenario»* · y el cambio estructural.

Meterlos dentro del prompt hace que la herramienta os devuelva la información **en el
vocabulario con el que ya trabajáis**, en vez de en el suyo. Es un detalle pequeño que
ahorra mucha traducción después.

---

## El bloque 5 es el importante

`LO QUE NO PUEDES SABER` está puesto a propósito.

La IA sintetiza lo que ya existe. Las preguntas difíciles de un sistema de vigilancia
maduro exigen **producir información que todavía no existe**: consultar a las empresas,
mandar un formulario, ir al dato primario. Obligar al modelo a declarar su propio límite
es lo que convierte la salida en un punto de partida para el analista, y no en un informe
que alguien firma sin comprobar.

---

## Cómo sé que está bien: el contraste crítico

Con la salida delante, tres preguntas **en voz alta y sin herramienta**:

1. ¿Qué ha acertado?
2. ¿Qué se ha dejado fuera que vosotros sí habríais metido?
3. **¿Qué de esto no firmaríais sin comprobarlo?**

La respuesta a la tercera es la que hay que escribir, porque es **vuestro procedimiento
de verificación**. Una salida con criterio explícito se puede auditar; una respuesta de
chat, no.

Esto ya tiene nombre entre vosotros: es hacer de **abogado del diablo** con la
herramienta, y es la **supervisión humana** de la que hablasteis. En la sesión del 22
pedisteis tener *«vuestra propia metodología o protocolo de abogados del diablo»*. Esto
es el primer folio de ese protocolo.

Y hay una variante que salió de vosotros mismos: **usar una herramienta para controlar la
salida de otra** —pedirle que verifique y que dé los enlaces concretos—. *«Ese cruce
entre ellas es muy productivo.»* Funciona, y no cuesta nada probarlo.

---

## Si algo falla

**Selecciona demasiadas o demasiado pocas.** Es el criterio, no la herramienta. Ver la
tabla de arriba.

**El informe sale bien pero el CSV no.** Pedidlos por separado: primero el CSV, y en un
segundo mensaje el informe. Es más fiable que pedir las dos cosas de una vez.

**Se inventa una cita o un dato.** Por eso está la regla de cero invención y el bloque de
verificación. Comprobad las cifras de las seleccionadas: son pocas y se hace en dos
minutos.
