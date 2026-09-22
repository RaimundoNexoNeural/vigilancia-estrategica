# Prompt 1 · EXTRAER

**Para qué sirve.** Reunir lo publicado sobre unos temas en un periodo, con su fuente y su
enlace, sin montar nada ni instalar nada. Es automatización ligera: se guarda una vez y se
reutiliza cada quincena cambiando dos huecos.

**Dónde funciona.** En cualquier herramienta con acceso a internet: ChatGPT con búsqueda,
Claude con búsqueda, Perplexity, Gemini. Si la que usas no sale a internet, este prompt no
puede hacer su trabajo: para eso está el corpus ya descargado.

**Los dos huecos:** `FUENTES` y `PERIODO`. Nada más.

---

## La plantilla

Copia desde aquí, rellena los dos corchetes y pégalo.

```
Actúa como analista de un sistema de vigilancia del entorno de una agencia
pública de vivienda y rehabilitación.

FUENTES
Busca exclusivamente en estas fuentes:
[  ▸ AQUÍ LAS FUENTES ◂  ]

PERIODO
Solo contenido publicado en [  ▸ LOS ÚLTIMOS 14 DÍAS ◂  ].
Descarta cualquier cosa anterior, aunque sea relevante.

TEMAS
Vivienda y mercado inmobiliario · políticas públicas de vivienda · financiación
y ayudas · rehabilitación y eficiencia energética · construcción industrializada
· normativa y regulación · suelo y urbanismo · necesidades sociales y acceso a
la vivienda.

QUÉ QUIERO DE VUELTA
Una tabla con una fila por elemento y estas columnas, en este orden:
  1. FECHA de publicación (AAAA-MM-DD)
  2. FUENTE
  3. TITULAR literal, sin reescribir
  4. RESUMEN en una sola frase
  5. URL exacta
  6. RELEVANCIA: alta, dudosa o fuera
  7. POR QUÉ esa relevancia, en menos de quince palabras

CÓMO ASIGNAS LA RELEVANCIA
  alta    el ámbito de la Agencia aparece en el titular o de forma repetida
  dudosa  lo toca de refilón; hay que leerlo para decidir
  fuera   no aparece el ámbito; candidato a descarte

No elimines lo que marques como "fuera": déjalo en la tabla, marcado. Saber
cuánto ruido hay, y de dónde viene, es parte del trabajo.

REGLAS, Y SON INNEGOCIABLES
- No inventes ningún titular, ninguna cifra y ninguna URL. Si no tienes el
  enlace exacto, no incluyas la entrada.
- No completes con conocimiento previo tuyo: solo lo publicado en el periodo.
- Si de una fuente no hay nada en el periodo, escribe "sin novedades" y sigue.
- No agrupes ni interpretes todavía. Aquí solo se recoge.

ANTES DE DARME LA TABLA, RESPONDE A ESTO
  1. ¿De dónde viene cada dato? (debe bastar con abrir su enlace)
  2. ¿Qué supuestos has tenido que hacer? Decláralos.
  3. ¿Podría yo defender esto sin decir que lo dijo una IA?
  4. ¿Qué falta? ¿Qué fuentes no has podido consultar?
  5. ¿Esto acerca a una decisión, o es ruido?

Y dime cuántos elementos has encontrado por fuente.
```

---

## Cómo se rellenan los huecos

**FUENTES** — las que ya se vigilan. Para la sesión:

> Brains Real Estate News, Inmodiario, Construible, Innovando en la Construcción, OVACEN,
> Fotocasa Research, Expansión (inmobiliario), 20minutos (vivienda), Demócrata, BOE, sala
> de prensa de la Comisión Europea.

**PERIODO** — **siempre en relativo**: «los últimos 14 días», «la última quincena», «desde
el lunes pasado». Nunca una fecha fija, para que la plantilla siga funcionando dentro de
dos semanas sin tocarla.

---

## Por qué está ese bloque de cinco preguntas al final

No es relleno. Son **los cinco criterios que se dieron en la sesión 1**
[S1 00:49:07-00:49:33] para dar por buena una salida de IA: entender de dónde vienen los
datos, que la IA declare sus supuestos, poder defender la recomendación *«sin decir que lo
dijo la IA»*, saber si faltan datos, y que la salida acerque a la decisión.

Lo que hace este prompt es **obligar a la herramienta a contestarlas ella misma**, en vez
de dejarlo a que os acordéis. Es la diferencia entre tener un criterio y aplicarlo.

Y por eso la URL es obligatoria en cada fila. Como se dijo en la sesión 2 [S2 00:36:41],
*«la recuperación aumentada no hace infalible a la IA, hace que responda con mejor
contexto y permite verificar de dónde [viene] la información y hay trazabilidad»*. Sin
trazabilidad esto no sirve para vigilancia.

---

## Lo que este prompt no puede hacer

No entra en fuentes de suscripción, ni en bases de datos jurídicas de pago, ni en nada que
pida credenciales. Esas sí se pueden incorporar desde vuestro propio sistema,
configurándolas con vuestras claves, que es exactamente lo que ya hacéis con los 209
canales de la plataforma.

Y un aviso sobre la herramienta, no sobre el prompt: un chat suelto *«no conoce vuestro
contexto… no deja trazabilidad, no se repite igual mañana»* [S2 00:20:13]. Escribir el
criterio, como aquí, es lo que hace que mañana dé lo mismo.
