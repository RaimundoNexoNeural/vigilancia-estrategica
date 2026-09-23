---
description: Selecciona lo que merece llegar al boletín, con un criterio explícito
argument-hint: [criterio] [fichero, por defecto noticias.csv] [etiqueta opcional]
---

# Seleccionar

**Para qué sirve.** De todo lo clasificado, quedarse con lo que merece llegar a alguien.
**No es resumir: es priorizar con un criterio explícito y escrito**, que es lo que hace
el resultado auditable y repetible.

**Criterio:** $1 · **Fichero:** $2 · **Etiqueta:** $3

Si no viene fichero, usa `noticias.csv`. Si no viene criterio, propón el de abajo, di que
es para discutirlo, y sigue con él.

> **Este comando escribe el fichero.** La versión para pegar en cualquier chat es
> `1-prompts/03-seleccionar.md`.

## Lo que tienes que rellenar

Criterio de partida:

> Selecciona lo que cumpla al menos una: obliga o puede obligar a la Agencia a hacer algo
> distinto de lo que hace; abre o cierra una vía de financiación; afecta al parque
> público de viviendas o a su rehabilitación; menciona a la Agencia o a Andalucía de
> forma directa; o es una tecnología o método que cambia cómo se construye o se
> rehabilita. Máximo quince seleccionadas; si hay más candidatas, prioriza por efecto
> sobre la Agencia, no por importancia general.

**El número que salga depende de la frase, no de la herramienta.** Con este criterio
salen unas quince de 145. Con solo «lo que obligue a la Agencia a hacer algo distinto»,
salen tres. Si parecen pocas, lo que hay que cambiar es el criterio, y eso es justamente
lo que hay que enseñar.

## Qué hace

**Paso 0.** Copia el fichero a `noticias-antes-de-seleccionar.csv`. Siempre, y antes de
tocar nada.

Después, tres cosas, y cada una se ve en un sitio distinto:

| Dónde | Qué |
|---|---|
| **En el chat** | el informe entero, que es lo que se lee en voz alta y se discute |
| **`seleccion.md`** | ese mismo informe en un fichero, para llevárselo |
| **`noticias.csv`** | tres columnas nuevas, para poder filtrarlo en el visor |

## Qué devuelve

### Las tres columnas del fichero

Fundidas por `id`, igual que al clasificar:

- `seleccionada` — `si` en las elegidas, `no` en el resto. **Nunca en blanco**, porque el
  filtro del visor necesita los dos valores para poder contar.
- `motivo_seleccion` — en las elegidas, qué parte del criterio cumple. Vacío en las demás.
- `criterio_seleccion` — **el criterio literal, el mismo texto en todas las filas.** Es lo
  que permite saber, mirando solo el fichero, con qué frase se decidió esto. Sin esta
  columna, dentro de dos semanas nadie sabe de dónde salió la selección.

Al recargar el visor se filtra por `seleccionada = si` y **las elegidas quedan solas en
pantalla**, con toda su clasificación al lado.

**Con etiqueta**, las tres columnas llevan su sufijo (`seleccionada_boletin`…) y **dos
selecciones distintas conviven** en vez de pisarse. Si te piden repetir con otro criterio,
**sugiere tú la etiqueta** en vez de sobrescribir: así se pueden comparar. La etiqueta se
normaliza: minúsculas, sin acentos, sin espacios.

### El informe, en `seleccion.md`

**1 · Las seleccionadas.** Cada una en 50 palabras como mucho: qué ha pasado, por qué
importa a la Agencia, y qué habría que vigilar a partir de ahora. Con su URL.

**2 · Los temas del conjunto.** Tres a cinco que se repitan, con las noticias que
sostienen cada uno. Los temas salen de lo que hay, no de lo que suele haber.

**3 · Lo que se descarta y por qué.** Agrupado por motivo, no una por una.

**4 · Los hallazgos**, con el vocabulario de la casa: **ruido** (aparece mucho pero no
cambia decisiones), **tendencia emergente** (se repite y empieza a afectar a un grupo),
**señal débil** (empieza a parecer algo que podría cambiar el escenario) y **cambio
estructural** (ya lo ha cambiado). En las señales débiles, di **qué haría falta ver para
confirmarlas**.

**5 · Lo que no puedes saber.** Qué preguntas no se pueden responder con este material y
qué habría que buscar fuera. Este bloque está puesto a propósito: la IA sintetiza lo que
ya existe, y las preguntas difíciles exigen **producir información que todavía no
existe**. Declarar el propio límite es lo que convierte esto en un punto de partida para
el analista, y no en un informe que alguien firma sin comprobar.

## Reglas innegociables

- Cero invención: ni cifras, ni citas, ni enlaces. Todo sale del material.
- Si una afirmación no está sostenida por una noticia concreta, no la hagas.
- Distingue siempre lo que dice la fuente de lo que infieres tú, y márcalo.
- No adornes ni valores positivamente el resultado.
- No toques ninguna columna anterior.

## Cómo sé que está bien

Al entregar, lanza estas tres preguntas al grupo y **espera**:

1. ¿Qué ha acertado?
2. ¿Qué se ha dejado fuera que vosotros sí habríais metido?
3. **¿Qué de esto no firmaríais sin comprobarlo?**

La respuesta a la tercera es la que hay que escribir, porque es el procedimiento de
verificación de la casa. Es hacer de **abogado del diablo** con la herramienta, y es la
**supervisión humana** de la que se habló en la sesión 2. En la del 22 lo pidieron
expresamente: *«hacernos nuestra propia metodología o protocolo de abogados del diablo»*.
Esto es el primer folio de ese protocolo.

Y hay una variante que aportó el propio equipo: usar una herramienta para **controlar** la
salida de otra, pidiéndole que verifique y dé los enlaces concretos. *«Ese cruce entre
ellas es muy productivo.»*

## Si algo falla

- **Deshacer la última selección**: copiar `noticias-antes-de-seleccionar.csv` sobre
  `noticias.csv`. Esa copia guarda **solo el estado inmediatamente anterior**.
- **Quitar selección y clasificación de golpe**: copiar
  `noticias-antes-de-clasificar.csv`.
- **Dejarlo como recién descargado**: volver a ejecutar el descargador.
- **Al descargar noticias nuevas se pierden estas columnas**, porque el descargador solo
  conoce las suyas. No es un fallo: el orden es descargar, luego clasificar, luego
  seleccionar. Como el criterio quedó escrito en `criterio_seleccion`, repetirlo es
  copiar una frase.
