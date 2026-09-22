---
description: Llena el corpus ejecutando los descargadores de script/
argument-hint: [noticias|datos|ambos] [fuentes o "todas"] [días]
---

# Descargar con script

Llena el corpus ejecutando los descargadores que ya existen en `script/`.

**Qué descargar:** $1 · **Fuentes:** $2 · **Periodo:** $3 días

Si algún parámetro viene vacío, usa estos valores: qué = `ambos`, fuentes = `todas`,
periodo = `14` días. No preguntes por ellos: dilo en una línea y sigue.

## Qué ejecutar

Traduce los parámetros a las órdenes correspondientes y **ejecútalas**, sin pedir
confirmación.

**Noticias** (si $1 es `noticias` o `ambos`):

```
python script/descargar_corpus.py --limpiar --dias <periodo>
```

Si las fuentes **no** son `todas`, añade `--fuentes "<lo que haya pedido>"`. El script lo
acepta de dos formas: una ruta a un CSV de fuentes, o una lista de nombres separados por
comas que acota la lista de `script/fuentes.csv`.

Sin `--fuentes`, el script usa las trece fuentes de la lista **y además descubre fuentes
nuevas**: pregunta a Google News qué medios están cubriendo los temas de vigilancia y
sondea sus feeds. Eso tarda unos 20 segundos más y suele traer medios andaluces que no
estaban en la lista. Merece la pena decirlo en voz alta cuando pase.

**Datos abiertos** (si $1 es `datos` o `ambos`):

```
python script/descargar_datos.py --limpiar
```

Si las fuentes no son `todas`, añade `--fuentes "<proveedores>"`. Los proveedores
disponibles son `INE`, `Eurostat` y `datos.gob.es`.

## Qué contar mientras corre

Esto se está proyectando. Mientras se ejecuta, explica en una o dos frases **qué está
pasando de verdad**, no lo que se ve:

- que el script no está inventando nada: entra en la URL de cada noticia y se trae el
  texto que publica la página;
- que el periodo va en relativo («los últimos 14 días»), así que la misma orden sirve
  dentro de dos semanas sin tocar nada;
- que las fuentes no están dentro del código, están en `script/fuentes.csv`, y añadir un
  medio es añadir una línea.

## Al terminar

Da un recuento corto y honesto, con estas cifras y nada más:

- cuántas noticias han entrado y de cuántas fuentes;
- cuántas tienen el texto completo, cuántas parcial y cuántas ninguno;
- el reparto del pre-filtro: `alta`, `dudosa`, `fuera`;
- cuántos conjuntos de datos y cuántas filas, si se han descargado;
- el tiempo que ha tardado.

Si alguna fuente ha fallado, **dilo**, con el motivo en media línea. No lo escondas: que
una fuente se caiga es normal y forma parte de lo que se está enseñando.

Recuerda al final que el resultado se ve en el visor:
`servir-visor.bat` y <http://127.0.0.1:8080/visor/>.

## Límites

- No modifiques los scripts. Están validados.
- No cambies el formato de salida: lo fija el contrato del `CLAUDE.md`.
