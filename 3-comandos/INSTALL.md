# Cómo montar los comandos en Claude Code

**Qué vais a conseguir.** Escribir `/clasificar` en una ventana y que Claude os ordene las
145 noticias solo, escribiendo el fichero él mismo.

**Cuánto tarda.** Unos quince minutos la primera vez, casi todos esperando a que se
instale Claude Code.

---

## Antes de empezar: ¿os hace falta esto?

**Seguramente no.** Leed esto antes de invertir el rato:

| | Necesita | Lo que hace |
|---|---|---|
| `1-prompts` | nada | lo mismo, pegando un texto en el chat |
| `2-skills` | Claude gratis en el navegador | lo mismo, pidiéndoselo en castellano |
| `3-comandos` | **Claude Code, de pago** | lo mismo, **y escribe los ficheros él** |

La diferencia real es solo esa última: que el comando **guarda el resultado en el disco**
en vez de dárselo en el chat para que lo copiéis. Si eso no os hace falta, usad los
prompts y ahorraos la instalación.

Seguid aquí si: tenéis ya Claude de pago, o queréis ver cómo funciona por dentro.

---

## Lo que hace falta

- **Una suscripción de pago a Claude.** Claude Code viene incluido en los planes Pro y
  Max, pero **no está en la cuenta gratuita**. Es la única parte de esta entrega que
  cuesta dinero.
- **Windows 10 u 11**, que es lo que tenéis.
- Unos 500 MB de disco.

---

## Paso 1 · Qué es Claude Code

Es Claude, pero **funcionando dentro de vuestro ordenador** en vez de en una página web.
La diferencia práctica: puede **leer y escribir los ficheros de una carpeta**. Por eso
puede dejaros el `noticias.csv` hecho, en vez de daros el texto para que lo peguéis.

No tiene botones. Se escribe en una ventana negra. Parece más difícil de lo que es:
**se le habla en castellano igual que en el chat**.

---

## Paso 2 · Instalarlo

1. Abrid <https://claude.com/claude-code> en el navegador.
2. Seguid las instrucciones de instalación para Windows que aparecen ahí.
3. Cuando termine, abrid el menú Inicio, escribid `cmd` y pulsad Intro. Se abre una
   ventana negra.
4. Escribid `claude` y pulsad Intro.
5. La primera vez os pedirá entrar con vuestra cuenta: se abre el navegador, entráis, y
   listo.

Si en el paso 4 dice que no reconoce el comando, es que la instalación no ha terminado o
hay que cerrar y volver a abrir la ventana negra.

---

## Paso 3 · Preparar la carpeta

Aquí es donde se copia el material. **Prestad atención a este paso**, porque el nombre de
la carpeta importa.

1. Abrid el **Explorador de Windows** y colocaos en la carpeta donde tenéis descomprimido
   este material. La que contiene `index.html` y `noticias.csv`.
2. Dentro de ella, **cread una carpeta nueva y llamadla exactamente `.claude`** — con el
   punto delante.

   *Windows no deja crear carpetas que empiecen por punto desde el menú normal.* Truco:
   creadla con el nombre `.claude.` —con punto delante **y detrás**— y al pulsar Intro
   Windows quita el de atrás solo.

3. Copiad dentro de `.claude` la carpeta **`commands`** que está aquí, en `3-comandos`.
4. Copiad el fichero **`CLAUDE.md`** de esta carpeta a la carpeta principal, la que tiene
   `index.html`.

Al final tiene que quedar así:

```
la carpeta del material/
  index.html
  noticias.csv
  fuentes.csv
  CLAUDE.md          ← copiado desde 3-comandos
  .claude/
    commands/        ← copiada desde 3-comandos
      clasificar.md
      descargar-directo.md
      descargar-script.md
      seleccionar.md
```

---

## Paso 4 · Arrancar

1. En el Explorador, con la carpeta principal abierta, pulsad en la **barra de dirección**
   de arriba, borradla, escribid `cmd` y pulsad Intro. Se abre la ventana negra **ya
   colocada en esa carpeta**, que es lo que hace falta.
2. Escribid `claude` y pulsad Intro.
3. Escribid `/` y esperad un segundo: **tienen que aparecer los cuatro comandos** en una
   lista.

**Si aparecen, está montado.** Si no, revisad que la carpeta se llama `.claude` con punto
y que dentro hay otra llamada `commands`.

---

## Paso 5 · Probarlo

Escribid esto y pulsad Intro:

```
/clasificar
```

Sin parámetros os propondrá unas categorías de partida y os dirá que son un andamio para
cambiarlas. Eso ya es señal de que funciona.

---

## Os va a pedir permiso, y está bien que lo haga

La primera vez que un comando quiera ejecutar algo o escribir un fichero, **Claude se
parará y os preguntará**. Saldrá algo como «¿permites ejecutar esto?».

**No es un fallo ni un problema de configuración.** Es la protección: no hace nada en
vuestro ordenador sin que alguien lo autorice. Es exactamente el *human in the loop* del
que se habló en clase, pero aplicado a la máquina.

Qué hacer: leedlo, y si es lo que habíais pedido, aceptad. Si os da la opción de **«no
volver a preguntar»** para esa orden concreta, podéis usarla y dejará de interrumpir.

---

## Los cuatro comandos

Cada uno está explicado a fondo en su fichero, dentro de `commands/`. Resumen:

| Comando | Qué hace |
|---|---|
| `/descargar-script` | descarga noticias **ejecutando el programa**. Rápido |
| `/descargar-directo` | descarga noticias **sin el programa**, haciéndolo Claude |
| `/clasificar` | ordena las noticias por vuestras categorías |
| `/seleccionar` | se queda con lo que merece el boletín |

Se usan con parámetros entre comillas. Por ejemplo:

```
/clasificar "tema, ambito, a_quien_afecta" "lo que pueda cambiar una decisión de la Agencia"
```

---

## Si algo falla

**`claude` no se reconoce como comando.** La instalación no terminó, o hay que cerrar la
ventana negra y abrirla de nuevo.

**Los comandos no salen al escribir `/`.** Casi siempre es la carpeta: tiene que llamarse
`.claude` (con punto) y contener `commands`. Y hay que arrancar Claude **desde la carpeta
del material**, no desde otro sitio.

**Dice que no encuentra `noticias.csv`.** Arrancasteis Claude desde otra carpeta. Cerrad,
colocaos en la del material y repetid el paso 4.

**Se queda parado pidiendo permiso.** Es lo normal. Ver el apartado de arriba.

**No os apañáis.** No pasa absolutamente nada: usad `1-prompts`. El contenido es el mismo
y no requiere instalar nada.
