# Prompt 1 · EXTRAER

**Para qué sirve.** Reunir lo que se ha publicado sobre vuestros temas en los últimos
días, con su fuente y su enlace, y que os lo devuelva en una tabla que se abre en el
visor.

**Dónde funciona.** En Gemini, ChatGPT, Claude o Perplexity, en su versión gratuita.
Eso sí: **la herramienta tiene que poder buscar en internet**. Si la vuestra no sale a
buscar, este prompt no puede hacer su trabajo — para eso está el `noticias.csv` que ya
viene descargado.

**Lo que tenéis que rellenar:** dos huecos, `FUENTES` y `PERIODO`. Nada más.

> **El prompt te devuelve el CSV y lo guardas tú.** Si usáis Claude Code, el comando
> `/descargar-directo` hace esto mismo pero escribiendo el fichero él solo.

---

## La plantilla

Copiad desde la primera línea del recuadro hasta la última, rellenad los dos corchetes
y pegadlo en el chat.

```
Actúa como analista de un sistema de vigilancia del entorno de una agencia
pública de vivienda y rehabilitación.

FUENTES
Busca exclusivamente en estas fuentes:
[  ▸ AQUÍ LAS FUENTES ◂  ]

PERIODO
Solo contenido publicado en [  ▸ LOS ÚLTIMOS 14 DÍAS ◂  ].
Descarta cualquier cosa anterior, aunque te parezca relevante.

TEMAS QUE INTERESAN
Vivienda · alquiler · compraventa de vivienda · hipotecas · suelo y urbanismo
· rehabilitación · construcción y edificación · eficiencia energética y
energía · políticas de vivienda · políticas sociales y necesidades sociales
· administración pública · proyectos de innovación y fondos europeos ·
economía general cuando afecte a la vivienda (IPC, inflación, tipos) · y
cualquier mención a AVRA o a la Agencia de Vivienda y Rehabilitación de
Andalucía.

QUÉ QUIERO DE VUELTA
Un CSV, con esta fila de cabecera exacta y una fila por noticia:

id,titular,fuente,fecha,url,cuerpo,cuerpo_completo,palabras_cuerpo,relevancia_prefiltro,motivo_prefiltro

Qué va en cada columna:
  id                    número de orden, empezando en 1
  titular               el titular literal, sin reescribirlo
  fuente                el nombre del medio
  fecha                 AAAA-MM-DD
  url                   el enlace exacto a la noticia
  cuerpo                el texto del artículo. Todo el que puedas obtener.
                        Si solo tienes el resumen, pon el resumen.
  cuerpo_completo       si / parcial / no, según lo que hayas podido obtener
  palabras_cuerpo       cuántas palabras tiene lo que has puesto en cuerpo
  relevancia_prefiltro  alta / dudosa / fuera
  motivo_prefiltro      por qué esa etiqueta, en menos de quince palabras

CÓMO ASIGNAS LA RELEVANCIA
  alta    el ámbito de la Agencia aparece en el titular o de forma repetida
  dudosa  lo toca de refilón; hay que leerlo para decidir
  fuera   no aparece el ámbito; candidata a descarte

No elimines lo que marques como "fuera": déjalo en la tabla, marcado. Saber
cuánto ruido hay, y de dónde viene, es parte del trabajo.

REGLAS, Y SON INNEGOCIABLES
- No inventes ningún titular, ninguna cifra y ninguna URL. Si no tienes el
  enlace exacto, no incluyas la entrada.
- No completes con lo que tú ya sepas: solo lo publicado en el periodo.
- Si de una fuente no hay nada, dilo al final y sigue.
- No agrupes ni interpretes todavía. Aquí solo se recoge.

ANTES DE DARME LA TABLA, RESPONDE A ESTO
  1. ¿De dónde viene cada dato? (debe bastar con abrir su enlace)
  2. ¿Qué has dado por supuesto? Decláralo.
  3. ¿Podría yo defender esto sin decir que lo dijo una IA?
  4. ¿Qué falta? ¿Qué fuentes no has podido consultar?
  5. ¿Esto acerca a una decisión, o es ruido?

Y dime cuántas noticias has encontrado por fuente.
```

---

## Cómo se rellenan los dos huecos

### FUENTES

Los medios que queréis vigilar. Para empezar, los que se usaron en la sesión:

> Brains Real Estate News, Inmodiario, Construible, Innovando en la Construcción,
> OVACEN, Fotocasa Research, Expansión (inmobiliario), 20minutos (vivienda),
> El Periódico de la Energía, Demócrata, BOE, y la sala de prensa de la Comisión Europea.

**Cambiadlos.** Esa lista es la que le pareció razonable al docente, no la vuestra. La
lista completa con sus direcciones está en `fuentes.csv`, en la carpeta de arriba.

### PERIODO

**Siempre en relativo**: «los últimos 14 días», «la última quincena», «desde el lunes
pasado». Nunca una fecha fija — así la plantilla sigue funcionando dentro de dos meses
sin tocarla.

---

## Qué devuelve, y qué hacer con ello

Un CSV. Para verlo:

1. Copiad la respuesta y guardadla en un fichero con extensión `.csv`, o descargadlo si
   la herramienta os da el botón.
2. Abrid `index.html` (el visor), pulsad **«Abrir un CSV»** y elegidlo.

**Si la tabla sale con alguna columna de más o de menos, no pasa nada: el visor no se
rompe.** Pinta las columnas que haya. Lo único que conviene que no falte es `titular`,
`url`, `relevancia_prefiltro` y `cuerpo`.

---

## Cómo sé que está bien

Las cinco preguntas del final no son relleno: son **los cinco criterios que se dieron en
la sesión 1** para dar por buena una salida de IA. Entender de dónde vienen los datos,
que declare sus supuestos, poder defender el resultado *«sin decir que lo dijo la IA»*,
saber si faltan datos, y que acerque a una decisión.

Lo que hace este prompt es **obligar a la herramienta a contestarlas ella misma**, en vez
de dejarlo a que os acordéis.

Y por eso la URL es obligatoria en cada fila: sin poder abrir el enlace y comprobarlo,
esto no sirve para vigilancia.

---

## Si algo falla

**Se corta a mitad.** Es lo normal con muchas noticias. Escribid: «continúa desde la
noticia N con la misma tabla y las mismas columnas». Y comprobad que no ha cambiado el
criterio a mitad, que es el error más habitual al trocear.

**Devuelve pocas noticias.** Casi siempre es el periodo: probad con más días. Si sigue
pasando, puede que la herramienta no esté buscando en internet de verdad — pedidle
expresamente que busque.

**Se inventa enlaces.** Pasa. Por eso la regla está escrita en mayúsculas dentro del
prompt. Comprobad tres o cuatro al azar: si alguno no abre, no os fiéis del resto y
repetid recordándole la regla.

**No entra en las fuentes de pago.** No puede, y no hay vuelta de hoja. Esas se
incorporan desde vuestro propio sistema, con vuestras claves.
