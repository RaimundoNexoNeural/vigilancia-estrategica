# Los comandos de Claude Code

**Qué es esto.** Los mismos tres trabajos de `1-prompts`, pero como comandos que se llaman
escribiendo `/clasificar` y que **escriben los ficheros ellos solos**.

**Para quién.** Para quien tenga **Claude de pago**. En la sesión era una persona. Es la
única parte de esta entrega que cuesta dinero, y **no os perdéis nada si no la usáis**.

**Qué hago primero.** Leed el apartado «¿os hace falta esto?» de
[INSTALL.md](INSTALL.md). Responde honestamente que probablemente no, y os ahorra el rato.

---

## Qué es un comando, en una frase

Un prompt guardado que se llama con una línea. Como se dijo en la sesión: *«el comando o
la skill no es otra cosa que un prompt que yo puedo llamar directamente con una línea, en
vez de tener que estar escribiéndolo todo el rato distinto»*.

Lo que añade frente a un prompt normal: **Claude Code puede leer y escribir ficheros de
vuestra carpeta**. Por eso el comando os deja el `noticias.csv` hecho, en vez de daros el
texto para que lo peguéis vosotros.

---

## Los cuatro

| Comando | Qué hace | Su gemelo en `1-prompts` |
|---|---|---|
| `/descargar-script` | descarga **ejecutando el programa**. Segundos | *(ninguno: un chat no puede ejecutar programas)* |
| `/descargar-directo` | descarga **sin el programa**, buscando Claude | `01-extraer.md` |
| `/clasificar` | ordena por vuestras categorías | `02-clasificar.md` |
| `/seleccionar` | se queda con lo que merece el boletín | `03-seleccionar.md` |

### La diferencia entre los dos de descargar

Es la que más costó explicar en clase, así que aquí va en una tabla:

| | `/descargar-script` | `/descargar-directo` |
|---|---|---|
| Cómo lo hace | ejecuta un programa de Python | lo hace la IA, entrando en cada noticia |
| Tarda | segundos | varios minutos |
| ¿Da siempre lo mismo? | **sí**, es determinista | puede variar algo |
| ¿Necesita Python? | sí | **no** |
| ¿Se puede replicar en Gemini? | no | **sí**, con el prompt 01 |
| Para qué sirve verlo | que lo rápido y estable es el programa | que **no hace falta** programa |

En la práctica: **el script para trabajar, el directo para entender**. Producen
exactamente el mismo fichero.

---

## Qué se puede cambiar, y dónde

Los comandos son ficheros de texto en `commands/`. Se abren con el Bloc de notas.

| Qué queréis cambiar | Dónde se toca |
|---|---|
| Los medios que se vigilan | `fuentes.csv`, en la carpeta principal |
| Los temas que interesan | `commands/descargar-directo.md`, apartado «De dónde tirar» |
| Las categorías de clasificación | `commands/clasificar.md`, «Lo que tienes que rellenar» |
| El criterio de pertinencia | `commands/clasificar.md`, «Criterio de partida» |
| El criterio de selección | `commands/seleccionar.md`, «Lo que tienes que rellenar» |
| Las columnas del CSV | `CLAUDE.md`, la tabla del contrato |
| Las reglas generales | `CLAUDE.md`, «Reglas que no se negocian» |

**`CLAUDE.md` es el fichero importante.** Claude lo lee siempre, antes de cualquier
comando. Ahí está el formato del CSV y las reglas que valen para todo. Si cambiáis el
formato, cambiadlo ahí.

Los cambios tienen efecto **en la siguiente orden que escribáis**. No hay que reiniciar
nada.

> **Guardad vuestra versión.** En la próxima sesión se pidió que quien haya modificado sus
> fuentes o sus categorías las comparta, para trabajar ya con material vuestro de verdad.

---

## Lo que no se entrega, y por qué

En la sesión se usó también un fichero `settings.local.json`, que es el que evitaba que
Claude pidiera permiso a cada paso. **No se entrega**, por dos razones: sus reglas nombran
carpetas internas del proyecto de formación, y es preferible que Claude os pregunte hasta
que tengáis confianza con la herramienta.

Cuando os canse que pregunte, la propia ventana os ofrece **«no volver a preguntar»** para
cada orden concreta, y se va construyendo sola.

---

## Los tres envoltorios

Cada comando dice **exactamente lo mismo** que su prompt y que su skill: mismas secciones,
mismo criterio, mismas reglas. Lo único que cambia:

- **El comando escribe el fichero.**
- **El prompt y la skill os devuelven el CSV y lo guardáis vosotros.**

Si algún día os pasáis de uno a otro, no hay nada que reaprender. Y si cambiáis un
criterio, cambiadlo en los tres sitios para que no se separen.
