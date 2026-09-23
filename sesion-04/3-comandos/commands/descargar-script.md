---
description: Descarga noticias ejecutando el script de Python, que es más rápido
argument-hint: [fuentes o "todas"] [días, por defecto 14] [limpiar o acumular]
---

# Descargar con el script

**Para qué sirve.** Lo mismo que `/descargar-directo`, pero **ejecutando el programa** en
vez de hacerlo a mano. Tarda mucho menos y da siempre exactamente el mismo resultado.

**Fuentes:** $1 · **Periodo:** $2 días · **Modo:** $3

Si vienen vacíos: fuentes = `todas`, periodo = `14`, modo = `limpiar`.

> **Este comando escribe el fichero.** No tiene versión de prompt para otros chats,
> porque ningún chat puede ejecutar un programa en el ordenador de nadie. El equivalente
> para ellos es `1-prompts/01-extraer.md`.

## Qué hace

Traduce lo que te pidan a los parámetros del script y lo lanza:

| Lo que te piden | Lo que le pasas |
|---|---|
| fuentes concretas | `--fuentes "BOE,Construible"` |
| todas | *(no se pasa `--fuentes`: además busca fuentes nuevas)* |
| un periodo | `--dias N` |
| empezar de cero | `--limpiar` |
| añadir a lo que hay | *(no se pasa `--limpiar`)* |

La orden queda así:

```
python 4-script/descargar_noticias.py --dias 14 --limpiar
```

Enséñala en pantalla **antes** de ejecutarla, y cuando termine, resume la salida con tus
palabras. Lo que importa que se vea no es el programa: es que el resultado es el mismo
que el del otro comando.

## Qué devuelve

Exactamente el mismo `noticias.csv` que `/descargar-directo`, con las mismas once
columnas y en el mismo orden. **Esa es la gracia: son intercambiables.**

## Cuál de los dos usar

| | `/descargar-script` | `/descargar-directo` |
|---|---|---|
| Cómo lo hace | ejecuta un programa de Python | lo hace la IA, paso a paso |
| Tarda | segundos | varios minutos |
| ¿Da siempre lo mismo? | sí, es determinista | puede variar algo |
| ¿Hace falta Python? | **sí** | no |
| ¿Se puede replicar en otro chat? | no | **sí**, con el prompt 01 |
| Para qué sirve enseñarlo | que se vea que lo rápido y estable es el programa | que se vea que **no hace falta** programa |

En la práctica: **el script para trabajar, el directo para entender**. Y si un día no
tenéis Python delante, el directo sigue funcionando.

## Reglas innegociables

- No modifiques el script. Está validado.
- Si el script falla, **dilo y para**. No intentes arreglarlo sobre la marcha ni
  reescribirlo: para eso está `/descargar-directo`.
- No inventes resultados si la ejecución no ha terminado.

## Cómo sé que está bien

- El fichero `noticias.csv` existe y tiene más filas que antes (o las de esta tanda, si
  se limpió).
- La cabecera tiene las once columnas de siempre.
- El recuento que imprime el script cuadra con lo que se ve al abrir el visor.

## Al terminar

Di cuántas noticias hay, cuántas con texto completo, el reparto del pre-filtro y cuánto
ha tardado. Y recuerda que para verlo basta con recargar el visor.

## Si algo falla

- **`python no se reconoce como un comando`.** Python no está instalado o no está en el
  PATH. Dilo y ofrece `/descargar-directo`, que no lo necesita.
- **El script tarda mucho.** Es normal con todas las fuentes: entra en cada noticia una
  por una. Avisa de que está corriendo en vez de darlo por colgado.
- **Alguna fuente falla.** El script lo reporta al final y sigue con las demás. No es un
  error: internet es así.
