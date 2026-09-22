---
description: Prioriza lo ya clasificado con el criterio de selección que se acuerde
argument-hint: [criterio de selección] [corpus, por defecto corpus/] [etiqueta opcional]
---

# Seleccionar

De todo lo clasificado, quedarse con lo que merece llegar a alguien. **No es resumir: es
priorizar con un criterio explícito y escrito**, que es lo que hace el resultado auditable
y repetible.

**Criterio:** $1 · **Sobre:** $2 · **Etiqueta:** $3

Si no viene corpus, usa `corpus/`. Si no viene criterio, propón el de abajo, di que es
para discutirlo, y sigue con él.

## Criterio de partida

*Selecciona lo que cumpla al menos una: obliga o puede obligar a la Agencia a hacer algo
distinto de lo que hace; abre o cierra una vía de financiación; afecta al parque público
de viviendas o a su rehabilitación; menciona a la Agencia o a Andalucía de forma directa;
o es una tecnología o método que cambia cómo se construye o se rehabilita. Máximo quince
seleccionadas. Si hay más candidatas, prioriza por efecto sobre la Agencia, no por
importancia general.*

## Qué tienes que entregar

Tres cosas, y cada una se ve en un sitio distinto:

| Dónde | Qué |
|---|---|
| **En el chat** | el informe entero, que es lo que se lee en voz alta y se discute |
| **`corpus/seleccion.md`** | ese mismo informe en un fichero, para llevárselo |
| **`corpus/indice.csv`** | dos columnas nuevas, para poder verlo en el visor |

### Las tres columnas del índice

Igual que al clasificar: **copia antes** `indice.csv` a
`indice-antes-de-seleccionar.csv`, y después añade emparejando por `id`:

- `seleccionada` — `si` en las elegidas, `no` en el resto. **Nunca en blanco**, porque el
  filtro del visor necesita los dos valores para poder contar.
- `motivo_seleccion` — en las elegidas, qué parte del criterio cumple, en una frase.
  Vacío en las demás.
- `criterio_seleccion` — **el criterio literal, el mismo texto en las 128 filas.** Es lo
  que permite saber, mirando solo el fichero, con qué frase se decidió esto. Sin esta
  columna, dentro de dos semanas nadie sabe de dónde salió la selección.

Así, al recargar el visor, se filtra por `seleccionada = si` y **las elegidas quedan solas
en pantalla, con toda su clasificación al lado**. Es la demostración de que el criterio
escrito hace el mismo recorrido que haría una persona, pero sobre 128 noticias.

No toques ninguna de las columnas anteriores, ni las once de la descarga ni las de
clasificar.

### Si hay etiqueta, la selección no pisa la anterior

**Sin etiqueta**, las tres columnas se llaman como arriba y **una segunda pasada
sobrescribe la primera**. Es lo normal: se prueba un criterio, no convence, se repite.

**Con etiqueta** —el tercer argumento: `ancho`, `estrecho`, `financiacion`…— las columnas
pasan a llamarse `seleccionada_ancho`, `motivo_seleccion_ancho` y
`criterio_seleccion_ancho`. Entonces **las dos selecciones conviven** y se pueden comparar
columna contra columna en el visor.

Eso es justo lo que hay que enseñar: mismo corpus, dos frases, dos resultados. Si te
piden repetir con otro criterio, **sugiere tú la etiqueta** en vez de sobrescribir.

La etiqueta se normaliza: minúsculas, sin acentos, sin espacios.

### Cómo se borra una selección

Hay que decírselo si lo preguntan, porque no es evidente:

- **Deshacer la última**: copiar `indice-antes-de-seleccionar.csv` sobre `indice.csv`.
  Ojo, esa copia solo guarda el estado **inmediatamente anterior**: se rehace en cada
  pasada.
- **Quitar selección y clasificación de golpe**: copiar
  `indice-antes-de-clasificar.csv` sobre `indice.csv`.
- **Dejarlo como recién descargado**: volver a ejecutar el descargador, que reescribe el
  índice con sus once columnas.

Y la consecuencia que hay que avisar: **al descargar noticias nuevas se pierden todas
estas columnas**, porque el descargador solo conoce las once. No es un fallo: el orden es
descargar, luego clasificar, luego seleccionar. Si se amplía el corpus, se repiten los
dos pasos — y como el criterio quedó escrito en `criterio_seleccion`, repetirlo es copiar
una frase.

### El informe

Escribe `corpus/seleccion.md` con cinco bloques, en este orden:

**1 · Las seleccionadas.** Por cada una, en 50 palabras como mucho: qué ha pasado, por qué
importa a la Agencia, y qué habría que vigilar a partir de ahora. Con su URL.

**2 · Los temas del conjunto.** Tres a cinco temas que se repiten, con las noticias que
sostienen cada uno. Los temas salen de lo que hay, no de lo que suele haber.

**3 · Lo que se descarta y por qué.** Agrupado por motivo, no una por una.

**4 · Señales débiles.** Y aquí conviene usar el vocabulario que ya tienen. En la sesión 2
se dieron cuatro tipos de hallazgo [S2 01:16:41-01:18:17]:

> *«el ruido, aparece mucho ruido sobre algo concreto pero no cambia decisiones»* ·
> *«tendencia emergente, se repite y empieza a afectar a un grupo»* · *«señal débil,
> empieza a parecer algo que podría cambiar el escenario»* · y el cambio estructural.

Clasifica lo que encuentres con esos cuatro nombres, y en las señales débiles di
**explícitamente qué haría falta ver para confirmarlas**.

**5 · Lo que no puedes saber.** Qué preguntas no se pueden responder con este material y
qué información habría que ir a buscar fuera.

Este bloque quinto está puesto a propósito. La IA sintetiza lo que ya existe; las
preguntas difíciles de un sistema de vigilancia maduro exigen **producir información que
todavía no existe** —consultar a empresas, mandar un formulario, ir al dato primario—.
Obligarte a declarar tu propio límite es lo que convierte esto en un punto de partida
para el analista, y no en un informe que alguien firma sin comprobar.

## Reglas

- Cero invención: ni cifras, ni citas, ni enlaces. Todo sale del material.
- Si una afirmación no está sostenida por una noticia concreta, no la hagas.
- Distingue siempre lo que dice la fuente de lo que infieres tú, y márcalo.
- No adornes ni valores positivamente el resultado.

## El contraste crítico, que se hace en voz alta y sin herramienta

Al entregar, lanza estas tres preguntas al grupo y **espera**:

1. ¿Qué ha acertado?
2. ¿Qué se ha dejado fuera que vosotros sí habríais metido?
3. ¿Qué de esto **no firmaríais** sin comprobarlo?

La respuesta a la tercera es la que hay que escribir, porque es el procedimiento de
verificación de la casa.

Esto tiene nombre y ellos ya lo conocen: es hacer de **abogado del diablo** con la
herramienta, como se dijo en la sesión 2 [S2 01:04:11] — *«tengo que hacer el abogado del
diablo con el chato para que no me limite el pensamiento»*—, y es la **supervisión
humana** de la que se habló en [S2 00:46:59]: *«es el human in the loop… el humano
interactúa»*.

Y hay una variante que aportó el propio equipo [S2 01:24:15]: usar una
herramienta para **controlar** la salida de otra, pedirle que verifique y que dé los
enlaces concretos. *«Ese cruce entre ellas es muy productivo.»* Si hay tiempo, merece la
pena hacerlo en directo.
