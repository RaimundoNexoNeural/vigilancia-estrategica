# Prompt 3 · SELECCIONAR

**Para qué sirve.** De lo ya clasificado, quedarse con lo que merece llegar a alguien. No
es resumir: es **priorizar con un criterio explícito y escrito**, que es lo que hace el
resultado auditable y repetible. Eso es lo que no tiene preguntarle a un chat.

**El hueco:** `CRITERIO DE SELECCIÓN`. Uno solo, y lo dicta la casa.

---

## La plantilla

```
Actúa como analista de vigilancia de una agencia pública de vivienda y
rehabilitación. Te paso el conjunto de noticias ya clasificado.

CRITERIO DE SELECCIÓN
[  ▸ AQUÍ EL CRITERIO ◂  ]

QUÉ QUIERO DE VUELTA

1) LAS SELECCIONADAS. Para cada una, en un máximo de 50 palabras:
   - QUÉ HA PASADO
   - POR QUÉ IMPORTA a la Agencia
   - QUÉ HABRÍA QUE VIGILAR a partir de ahora
   Añade su URL.

2) LOS TEMAS DEL CONJUNTO. Tres a cinco temas que se repiten entre todo el
   material, con las noticias que sostienen cada uno. Los temas salen de lo
   que hay, no de lo que suele haber.

3) LO QUE SE DESCARTA Y POR QUÉ. Agrupado por motivo, no una por una.

4) LOS HALLAZGOS, clasificados con estos cuatro nombres:
   - RUIDO: aparece mucho sobre algo concreto, pero no cambia decisiones.
   - TENDENCIA EMERGENTE: se repite y empieza a afectar a un grupo.
   - SEÑAL DÉBIL: empieza a parecer algo que podría cambiar el escenario.
   - CAMBIO ESTRUCTURAL: ya ha cambiado el escenario.
   En las señales débiles, di explícitamente QUÉ HARÍA FALTA VER para
   confirmarlas.

5) LO QUE NO PUEDES SABER. Qué preguntas no puedes responder con este material
   y qué información habría que ir a buscar fuera para responderlas.

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

---

## Los cuatro nombres del bloque 4 son vuestros, no míos

Salieron en la sesión 2 [S2 01:16:41-01:18:17]:

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

## El contraste crítico: en voz alta y sin herramienta

Cuando tengáis la salida delante, tres preguntas:

1. **¿Qué ha acertado?**
2. **¿Qué se ha dejado fuera que vosotros sí habríais metido?**
3. **¿Qué de esto no firmaríais sin comprobarlo?**

La respuesta a la tercera es la que hay que escribir, porque es **vuestro procedimiento de
verificación**. Una salida con criterio explícito se puede auditar; una respuesta de chat,
no.

Esto ya tiene nombre en vuestras sesiones. Es hacer de **abogado del diablo** con la
herramienta —*«tengo que hacer el abogado del diablo con el chato para que no me limite el
pensamiento»* [S2 01:04:11]— y es la **supervisión humana**, el *human in the loop* del
que hablasteis [S2 00:46:59].

Y hay una variante que salió de vosotros mismos [S2 01:24:15]: usar una herramienta para
**controlar** la salida de otra —pedirle que verifique y que dé los enlaces concretos—.
*«Ese cruce entre ellas es muy productivo.»* Funciona, y no cuesta nada probarlo.
