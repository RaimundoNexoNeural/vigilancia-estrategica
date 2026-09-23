# Las skills de Claude

**Qué es esto.** Los mismos tres trabajos de la carpeta `1-prompts`, pero empaquetados
para que Claude los tenga aprendidos. En vez de pegar un texto largo cada vez, le pedís
la tarea en castellano y él ya sabe cómo hacerla.

**Para quién.** Para quien use **Claude en el navegador**. En la sesión eran cuatro
personas. **Funciona con la cuenta gratuita.**

**Qué hago primero.** Abrid [INSTALL.md](INSTALL.md). Son cinco minutos y se hace una
sola vez.

---

## Qué es una skill, en una frase

Un prompt que la herramienta se guarda y aplica sola cuando toca. Nada más. Como dijo el
docente en la sesión: *«el comando o la skill no es otra cosa que un prompt que yo puedo
llamar con una línea, en vez de tener que estar escribiéndolo todo el rato distinto»*.

Claude del navegador **no permite comandos**, pero **sí permite skills**. Por eso existe
esta carpeta.

---

## Las tres

| Carpeta | Qué hace | Cómo se la pedís |
|---|---|---|
| `extraer-noticias` | busca noticias y las devuelve en CSV | «extráeme noticias de vivienda de la última quincena» |
| `clasificar-noticias` | las ordena por vuestras categorías | «clasifícame estas noticias por tema y ámbito» |
| `seleccionar-noticias` | se queda con lo que merece el boletín | «selecciona las que deberían ir al boletín» |

Se usan **una detrás de otra**, igual que los prompts. Cada una coge lo que dejó la
anterior.

---

## Qué se puede cambiar, y dónde

Cada skill es un fichero de texto, `SKILL.md`, dentro de su carpeta. Se abre con el Bloc
de notas y se edita como cualquier texto.

| Qué queréis cambiar | Dónde se toca |
|---|---|
| Las fuentes que se vigilan | `extraer-noticias/SKILL.md`, bloque «Lo que hay que preguntar» |
| El periodo por defecto | `extraer-noticias/SKILL.md`, mismo bloque |
| Los temas que interesan | `extraer-noticias/SKILL.md`, bloque «Los temas que interesan» |
| Las categorías de clasificación | `clasificar-noticias/SKILL.md`, el andamio de partida |
| El criterio de pertinencia | `clasificar-noticias/SKILL.md`, «Criterio de partida» |
| El criterio de selección | `seleccionar-noticias/SKILL.md`, «Lo que hay que preguntar» |
| Las columnas del CSV | el bloque «Qué devolver» de cada una |

**Después de editar hay que volver a comprimir esa carpeta en ZIP y volver a subirla**,
sustituyendo la anterior. Es el único inconveniente de las skills frente a los prompts:
cambiarlas cuesta un minuto más.

Las dos primeras líneas del fichero —las que van entre `---`— son importantes: el `name`
es cómo se llama, y la `description` es lo que Claude lee para decidir si esta skill le
sirve para lo que le acaban de pedir. **Si cambiáis mucho lo que hace la skill, cambiad
también esa descripción**, o dejará de activarse cuando toca.

---

## Si no os funcionan las skills

No pasa nada, y no se pierde nada: **los prompts de `1-prompts` hacen exactamente lo
mismo**. Se copian, se pegan en el chat y funcionan en Claude, en Gemini, en ChatGPT y en
cualquier otro. Son más de escribir cada vez, pero no dependen de que vuestra cuenta
tenga la función activada.
