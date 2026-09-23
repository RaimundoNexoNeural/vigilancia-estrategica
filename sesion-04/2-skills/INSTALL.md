# Cómo instalar las skills en Claude

**Qué vais a conseguir.** Que en vuestro Claude del navegador podáis escribir «extráeme
las noticias de la última quincena» y que él sepa exactamente cómo hacerlo, sin tener que
pegar un prompt largo cada vez.

**Cuánto tarda.** Cinco minutos, y se hace una sola vez.

---

## Lo que hace falta

- Una cuenta de Claude en <https://claude.ai>. **Vale la gratuita.**
- Nada más. No hay que instalar ningún programa.

---

## Paso 1 · Comprimir cada skill en un ZIP

Claude no acepta carpetas sueltas: necesita un fichero `.zip` por cada skill.

En esta carpeta hay tres carpetas:

```
extraer-noticias
clasificar-noticias
seleccionar-noticias
```

Para cada una:

1. **Clic derecho** sobre la carpeta.
2. **Enviar a** → **Carpeta comprimida (en zip)**.
3. Os deja al lado un fichero `extraer-noticias.zip`. Ese es el que se sube.

*(En Windows 11 la opción se llama «Comprimir en archivo ZIP».)*

Repetidlo con las tres. Acabaréis con tres `.zip`.

---

## Paso 2 · Subirlas a Claude

1. Entrad en <https://claude.ai>.
2. Abajo a la izquierda, pulsad **vuestro nombre** → **Configuración**.
3. Buscad el apartado **Capacidades** (o *Skills*).
4. Pulsad **Subir skill** y elegid uno de los ZIP.
5. Repetid con los otros dos.

Si no encontráis el apartado, es que vuestra cuenta todavía no lo tiene activado: no
pasa nada, **usad los prompts de la carpeta `1-prompts`**, que hacen exactamente lo mismo
pegándolos en el chat.

---

## Paso 3 · Comprobar que funciona

Abrid una conversación nueva en Claude y escribid:

> Extráeme noticias de vivienda de los últimos 7 días

Si la skill está bien instalada, Claude os preguntará de qué fuentes y de qué periodo, en
vez de ponerse a inventar por su cuenta. **Esa pregunta es la señal de que ha funcionado.**

---

## Cómo se usan a partir de ahora

No hay que invocarlas con ningún símbolo raro. **Se pide en castellano y ya está**:

- «Extráeme las noticias de la última quincena de estas fuentes: …»
- «Clasifícame estas noticias por tema, ámbito y a quién afectan»
- «Selecciona las que deberían ir al boletín»

Claude reconoce solo cuál de las tres le toca por lo que le pedís.

---

## Qué cambia respecto a los comandos de Claude Code

Es útil saberlo para no perderse:

| | Skills (esta carpeta) | Comandos (carpeta `3-comandos`) |
|---|---|---|
| Dónde | Claude del navegador | Claude Code, en vuestro ordenador |
| Cuesta | gratis | requiere suscripción de pago |
| Cómo se llama | pidiéndoselo en castellano | escribiendo `/clasificar` |
| Qué hace con el resultado | **os lo da en el chat** y lo guardáis vosotros | **escribe el fichero** él solo |
| Puede leer vuestros ficheros | solo lo que le subáis al chat | sí, los de la carpeta |

Lo importante: **el contenido es el mismo**. Un skill, un comando y un prompt de esta
entrega dicen exactamente lo mismo con tres envoltorios distintos. Si mañana os pasáis de
uno a otro, no hay nada que reaprender.

---

## Si algo falla

**No aparece el apartado de skills.** No todas las cuentas lo tienen. Usad `1-prompts`.

**Sube el ZIP pero dice que el formato no es válido.** Comprobad que dentro del ZIP está
directamente el `SKILL.md`, y no otra carpeta con el `SKILL.md` dentro. Si al abrir el
ZIP veis una carpeta, comprimid desde dentro.

**La skill está pero Claude no la usa.** Decídselo explícitamente: «usa la skill de
extraer noticias». Y si aun así no, pegad el prompt de `1-prompts`, que funciona siempre.
