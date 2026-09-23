# Los prompts

**Qué es esto.** Tres textos preparados para pegar en cualquier chat de inteligencia
artificial. Hacen el mismo trabajo que se enseñó en la sesión: reunir noticias,
clasificarlas y quedarse con lo que importa.

**Para quién.** Para todos. **No hay que instalar nada, ni pagar nada, ni saber nada
técnico.** Si tenéis Gemini abierto en el navegador, ya podéis usarlos.

**Qué hago primero.** Abrid `01-extraer.md`, copiad el recuadro grande, rellenad los dos
corchetes y pegadlo en Gemini. Eso es todo.

---

## Los tres, y en qué orden

Se usan **uno detrás de otro**, no todos a la vez. Cada uno coge lo que dejó el anterior.

| | Qué hace | Qué le dais | Qué devuelve |
|---|---|---|---|
| **01 · Extraer** | busca noticias y las recoge | las fuentes y el periodo | un CSV de noticias |
| **02 · Clasificar** | las ordena por vuestras categorías | ese CSV, y vuestras categorías | el mismo CSV con columnas nuevas |
| **03 · Seleccionar** | se queda con lo que merece la pena | ese CSV, y vuestro criterio | el CSV marcado, y un informe |

Se hacen por fases a propósito. Pedirle las tres cosas de golpe a un chat da un resultado
peor y, sobre todo, imposible de comprobar: no sabríais en qué paso se equivocó.

**Si no queréis empezar por el 01**, no hace falta: en la carpeta de arriba está
`noticias.csv` con 145 noticias ya descargadas. Podéis empezar directamente por el 02.

---

## Cómo se rellenan los huecos

Dentro de cada plantilla hay trozos así:

```
[  ▸ AQUÍ LAS FUENTES ◂  ]
```

**Eso es lo que tenéis que sustituir**, corchetes incluidos. Nada más. El resto del texto
se queda tal cual.

Cada fichero explica qué poner en sus huecos y trae un ejemplo para copiar y modificar.

---

## Qué se puede cambiar, y dónde

Esta es la parte que de verdad importa, porque **el material que se entregó no es el
vuestro todavía**. Las fuentes y las categorías son las que parecieron razonables al
preparar la sesión. Las vuestras son otras.

| Qué queréis cambiar | Dónde se toca |
|---|---|
| Los medios que se vigilan | el hueco `FUENTES` de `01-extraer.md`, y `fuentes.csv` en la carpeta de arriba |
| Cuántos días hacia atrás | el hueco `PERIODO` de `01-extraer.md` |
| Los temas que interesan | el bloque `TEMAS QUE INTERESAN` de `01-extraer.md` |
| Las categorías de clasificación | el hueco `CATEGORÍAS` de `02-clasificar.md` |
| Qué cuenta como «pertinente» | el hueco `CRITERIO` de `02-clasificar.md` |
| Qué merece llegar al boletín | el hueco `CRITERIO DE SELECCIÓN` de `03-seleccionar.md` |
| Las columnas que devuelve | el bloque `QUÉ QUIERO DE VUELTA` de cada uno |

Son ficheros de texto normales: se abren con el Bloc de notas y se guardan igual. No hay
nada que compilar ni que validar.

> **Guardad vuestra versión.** En la próxima sesión se pidió que quien haya modificado
> sus fuentes o sus categorías las comparta, para que los casos de uso siguientes se
> hagan ya con material vuestro de verdad y no con el de ejemplo.

---

## Ver el resultado

Los tres devuelven un CSV. Para mirarlo:

- **En el visor**: abrid `index.html` (carpeta de arriba), pulsad **«Abrir un CSV»** y
  elegid el fichero. Tabla con filtros, y al pinchar una fila se lee la noticia entera.
- **En LibreOffice Calc**: doble clic en el fichero. Al abrirlo os preguntará por el
  formato: aseguraos de que el **juego de caracteres es UTF-8** y de que el **separador
  es la coma**. Si no, los acentos salen rotos.

**Si el CSV sale con alguna columna de más o de menos, el visor no se rompe**: pinta las
que haya. Está hecho así a propósito, porque cada herramienta de IA devuelve las cosas un
poco distintas.

---

## Hacer vuestros propios prompts

Estos tres resuelven lo que se vio en clase. El día que necesitéis otro —para otra tarea,
otro tipo de documento, otro trabajo repetitivo— tenéis dos caminos:

**Copiar la estructura de estos.** Fijaos en que todos tienen las mismas partes: quién
tiene que ser la IA, qué le dais, qué queréis de vuelta, las reglas innegociables, y las
preguntas de verificación al final. Esa estructura funciona para casi cualquier encargo.

**Usar PromptCowboy** (<https://promptcowboy.ai>), que es gratuito y se recomendó en la
sesión. Le contáis en una frase lo que queréis, él lo convierte en un prompt bien
estructurado y además os hace preguntas para afinarlo. Muy útil cuando tenéis la idea
pero no sabéis cómo ordenarla.

---

## Lo que estos prompts no pueden hacer

**No entran en fuentes de suscripción**, ni en bases de datos jurídicas de pago, ni en
nada que pida usuario y contraseña. Eso sí se puede incorporar desde vuestro propio
sistema, configurándolo con vuestras claves, que es lo que ya hacéis con los canales de
la plataforma.

**Y un aviso sobre la herramienta, no sobre el prompt:** un chat suelto *«no conoce
vuestro contexto, no deja trazabilidad, no se repite igual mañana»*. Escribir el criterio,
como aquí, es precisamente lo que hace que mañana dé lo mismo.
