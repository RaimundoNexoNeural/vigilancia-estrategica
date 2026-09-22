---
description: Llena el corpus sin usar los scripts, respetando el mismo contrato
argument-hint: [noticias|datos|ambos] [fuentes o "todas"] [días]
---

# Descargar sin script

Llena el corpus **haciéndolo tú**, sin invocar los descargadores de `script/`. El
resultado tiene que ser indistinguible del que dejan ellos: mismas fichas, mismas once
columnas, mismo orden. Si se desvía, el visor deja de leerlo.

**Qué descargar:** $1 · **Fuentes:** $2 · **Periodo:** $3 días

Valores por defecto si vienen vacíos: qué = `noticias`, fuentes = `todas`, periodo = `14`
días. No preguntes: dilo en una línea y sigue.

## Lo que puedes y lo que no

**Sí puedes** usar la shell con libertad: `curl` para traerte feeds y páginas, `python -c`
para parsear XML o HTML en línea, y las herramientas de lectura y escritura de ficheros.
Puedes replicar en línea lo que hacen los scripts.

**No puedes**: ejecutar `script/descargar_corpus.py` ni `script/descargar_datos.py`, ni
crear ficheros de script nuevos. El objetivo de este comando es enseñar que el trabajo se
puede encargar en castellano, sin programa de por medio.

**No pidas confirmación** para cada orden de shell. Esto se está impartiendo en directo.

## Cómo hacerlo

### 1. De dónde tirar

Lee `script/fuentes.csv`. Tiene cuatro columnas: `nombre`, `url`, `tipo`, `tope`.

- Si las fuentes pedidas son `todas`, usa las de la lista.
- Si vienen nombres concretos, quédate solo con las que casen por nombre o dominio.
- Si el parámetro es una ruta a otro CSV, usa ese.

El `tipo` decide una sola cosa: si la fuente es `generalista` u `oficial`, **filtra por
tema antes de aceptar la noticia** —publican de todo y aquí solo interesa vivienda, suelo,
alquiler, rehabilitación, construcción, urbanismo, hipotecas, edificación y energía
aplicada a la vivienda—. Las `especializada` y `suscripcion` entran sin ese filtro.

El `tope` es cuántas noticias como máximo se cogen de esa fuente.

### 2. Traerte los feeds

Descarga cada `url` y sácale las entradas: titular, enlace, fecha de publicación y
resumen. Quédate solo con lo publicado dentro del periodo pedido, contado hacia atrás
desde hoy.

Limpia del resumen las coletillas de autopromoción que meten los feeds («Artículo
publicado originalmente en…», «The post … appeared first on…»). Si lo que queda es un
resto sin sentido, deja la entradilla vacía: mejor ninguna que una a medias.

### 3. Entrar en cada noticia

**Este es el paso que no se puede saltar.** El resumen del RSS es un reclamo cortado a
media frase; con eso no se puede clasificar nada.

Abre la URL de cada noticia y extrae el texto real del artículo: descarta `script`,
`style`, `nav`, `header`, `footer` y `aside`, busca el `<article>` o el `<main>` y quédate
con los párrafos con sentido —los de menos de 60 caracteres casi nunca lo son—.

Guarda el texto **completo** que publique la página. No recortes. Si un muro de pago lo
corta, guarda lo que haya y márcalo.

### 4. Etiquetar el pre-filtro

A cada noticia le pones `relevancia_prefiltro`:

- **`alta`**: el ámbito de la Agencia aparece en el titular, o de forma repetida en el
  cuerpo.
- **`dudosa`**: lo toca de refilón; hay que leerla para decidir.
- **`fuera`**: no aparece el ámbito; candidata a descarte.

Y en `motivo_prefiltro`, la razón en una frase.

**No borres nada.** Lo que no viene al caso se queda, marcado. El ejercicio de la sesión
es aprender a descartar, y para eso hace falta tener algo que descartar.

### 5. Escribir

Fichas en `corpus/noticias/` e índice en `corpus/indice.csv`, **exactamente con el formato
del `CLAUDE.md`**: UTF-8 con BOM, las siete claves de metadatos en su orden, y las once
columnas del índice en su orden. Vuelve a leerlo antes de escribir si tienes dudas.

Si vas a acumular sobre un corpus que ya existe, lee el índice anterior y **no repitas
URL**: continúa la numeración donde se quedó.

### 6. Datos abiertos

Si $1 es `datos` o `ambos`, trae también series de datos abiertos sobre vivienda, suelo o
construcción, de fuentes oficiales —INE, Eurostat, datos.gob.es—, y déjalas en
`corpus/datos/` como CSV plano con una ficha `.md` al lado que diga qué mide, quién lo
publica, qué periodo cubre, en qué unidad y con qué URL se descarga. Nada de códigos sin
traducir ni fechas en milisegundos.

## Cómo se comprueba que está bien

Antes de dar por terminado, repasa las cinco preguntas que se dieron en la
sesión 1 [S1 00:49:07-00:49:33] para dar por buena una salida de IA. Reconstruidas de la
grabación, que en ese tramo va justa:

1. **¿Se entiende de dónde vienen los datos?** Cada ficha, con su fuente y su URL.
2. **¿Ha declarado la IA sus supuestos?** Si has decidido algo —qué contaba como «dentro
   del ámbito», qué párrafos eran cuerpo y cuáles no—, dilo.
3. **¿Se puede defender el resultado *«sin decir que lo dijo la IA»*?** Todo tiene que
   ser comprobable abriendo el enlace.
4. **¿Se sabe si faltan datos?** Di qué fuentes fallaron y cuántas noticias se quedaron
   sin texto.
5. **¿Acerca esto a una decisión?** Si el corpus es ruido, dilo.

Y lo que se dijo sobre la trazabilidad [S2 00:36:41]: *«la recuperación aumentada no hace
infalible a la IA, hace que responda con mejor contexto y permite verificar de dónde
[viene] la información y hay trazabilidad»*. Por eso la URL es obligatoria en cada fila:
**sin trazabilidad esto no vale para vigilancia**.

## Al terminar

Recuento corto: cuántas noticias, de cuántas fuentes, cuántas con texto completo, el
reparto del pre-filtro, y qué fuentes fallaron y por qué. Nada de adornos.

Y di en una frase lo que importa: esto ha salido de un encargo en castellano, no de un
programa.
