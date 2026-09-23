# Empezad por aquí

Material de la sesión **Vigilancia Estratégica Aumentada con IA**, para la Agencia de
Vivienda y Rehabilitación de Andalucía. Curso coordinado por el Instituto de Estudios
Cajasol.

Esta es la única página que hace falta leer. Son dos minutos.

---

## Lo primero: ved que funciona

**Doble clic en `index.html`.** Se abre en vuestro navegador.

Pulsad **«Abrir un CSV»** → **«Elegir fichero»** y elegid **`noticias.csv`**, que está
en esta misma carpeta.

Ya está. **145 noticias** reales, descargadas durante la sesión, con sus filtros. Pinchad
en cualquier fila y se lee el artículo entero.

> **No hay que instalar nada para esto.** Ni Python, ni permisos, ni una cuenta. Es una
> página que funciona desde vuestro disco duro.
>
> Al abrirla os dirá que pulséis «Abrir un CSV». No es un error: el navegador no deja que
> una página abierta desde el disco lea ficheros por su cuenta, así que hay que elegirlo a
> mano. Es una sola vez.

---

## Qué es todo esto

Un **circuito de tres pasos** para vigilar el entorno con ayuda de una IA:

**Extraer** → reunir lo publicado sobre vuestros temas, con su fuente y su enlace.
**Clasificar** → ordenarlo contra vuestras categorías, no las de la máquina.
**Seleccionar** → quedarse con lo que merece llegar a alguien, con un criterio escrito.

Lo importante no son las herramientas: es que **el criterio queda escrito**. Por eso se
puede auditar, repetir dentro de dos semanas y defender sin decir que lo hizo una IA.

---

## A qué carpeta ir

Según lo que tengáis. **Las cuatro hacen el mismo trabajo**: cambia el envoltorio, no el
contenido.

| Si tenéis… | Id a | Hace falta instalar |
|---|---|---|
| **Gemini, ChatGPT o cualquier chat** | **`1-prompts`** | **nada** |
| **Claude en el navegador** | `2-skills` | nada, se suben tres ficheros |
| **Claude de pago (Claude Code)** | `3-comandos` | sí, y cuesta dinero |
| **Ganas de trastear con Python** | `4-script` | sí, pero es opcional |

**Si dudáis, id a `1-prompts`.** Es la vía principal, funciona con cuenta gratuita y es la
que usa casi todo el mundo del grupo.

---

## Qué hay en esta carpeta

| | |
|---|---|
| `index.html` | el visor. Doble clic y funciona |
| `noticias.csv` | las 145 noticias de la sesión, con su texto dentro |
| `fuentes.csv` | los medios que se vigilan. **Este lo vais a querer cambiar** |
| `1-prompts` | las plantillas para pegar en cualquier chat |
| `2-skills` | lo mismo, para Claude del navegador |
| `3-comandos` | lo mismo, para Claude Code |
| `4-script` | el descargador en Python |

Cada carpeta tiene su `README.md` —qué es y cómo se usa— y, las que lo necesitan, un
`INSTALL.md` con los pasos exactos.

---

## Esto todavía no es vuestro

Y es la parte que más importa.

Las fuentes y las categorías que vienen son **las que parecieron razonables al preparar la
sesión**. Las vuestras son otras: en clase ya salieron bastantes que no estaban.

Todos los ficheros son **texto normal**: se abren con el Bloc de notas y se guardan igual.
No hay nada que compilar ni que validar. Dentro de las plantillas veréis huecos así:

```
[  ▸ AQUÍ LAS CATEGORÍAS ◂  ]
```

Eso es lo que hay que sustituir. El README de cada carpeta dice exactamente qué línea se
toca para cambiar fuentes, temas, categorías, criterios o columnas.

> **Guardad vuestra versión.** En la próxima sesión se pidió que quien haya modificado sus
> fuentes o sus categorías las comparta, para que los casos siguientes se hagan ya con
> material vuestro de verdad y no con el de ejemplo.

---

## Dos cosas prácticas

**Para abrir el CSV en LibreOffice Calc**: doble clic. Al abrirlo pregunta por el formato:
aseguraos de que el juego de caracteres es **UTF-8** y el separador es la **coma**. Si no,
los acentos salen rotos.

**Si un CSV sale con alguna columna de más o de menos, el visor no se rompe**: pinta las
que haya. Está hecho así a propósito, porque cada herramienta de IA devuelve las cosas un
poco distintas. Lo único que conviene que no falte es `titular`, `url`,
`relevancia_prefiltro` y `cuerpo`.

---

## Una advertencia honesta

Nada de esto sustituye vuestro criterio. La IA sintetiza lo que ya existe; las preguntas
difíciles de un sistema de vigilancia maduro exigen **producir información que todavía no
existe** —preguntar a las empresas, mandar un formulario, ir al dato primario—.

Por eso todas las plantillas terminan pidiéndole a la herramienta que declare **lo que no
puede saber**. Esa parte es la vuestra.
