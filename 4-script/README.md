# El script de descarga

**Qué es esto.** Un programa que recorre los medios de `fuentes.csv`, entra en cada
noticia a por su texto y lo deja todo en `noticias.csv`. Lo que en la sesión tardaba
varios minutos con la IA, aquí tarda segundos.

**Para quién.** Para quien tenga curiosidad técnica o quiera actualizar el corpus a menudo.
**Es opcional**: el resto de la entrega funciona sin esto.

**Qué hago primero.** [INSTALL.md](INSTALL.md), que empieza diciéndoos si os hace falta.

---

## Qué hace, en cinco pasos

1. Lee de `fuentes.csv` qué medios vigilar.
2. Descarga el listado de cada uno y se queda con lo publicado en los últimos días.
3. A los medios generalistas y oficiales, que publican de todo, les aplica un filtro por
   tema. A los especializados no: se supone que todo lo suyo viene al caso.
4. **Entra en la página de cada noticia y le saca el texto del artículo.** Este es el paso
   que tarda, y el que de verdad importa: el resumen del listado está cortado a media
   frase y no sirve para clasificar después.
5. Le pone una etiqueta de relevancia provisional y lo escribe todo en `noticias.csv`.

**No borra nada.** Lo que no viene al caso se marca como `fuera`, pero se queda. Saber
cuánto ruido hay, y de dónde viene, es parte del trabajo.

---

## Cómo se usa

Desde la ventana negra, colocada en esta carpeta:

```
python descargar_noticias.py
```

Sin nada más, hace lo razonable: todas las fuentes, últimos 14 días, y además busca medios
nuevos por internet.

### Los parámetros que de verdad se usan

| Parámetro | Qué hace | Por defecto |
|---|---|---|
| `--dias N` | cuántos días hacia atrás | 14 |
| `--limpiar` | empieza de cero. Sin esto, **añade** a lo que hubiera | añade |
| `--fuentes "A,B"` | solo esos medios | todos |
| `--hilos N` | cuántas descargas a la vez. Bajarlo si la red va justa | 8 |

Ejemplos reales:

```
python descargar_noticias.py --dias 7 --limpiar
python descargar_noticias.py --fuentes "BOE,Construible"
python descargar_noticias.py --dias 30 --hilos 4
```

Para ver todos: `python descargar_noticias.py --help`.

---

## Qué deja

Un único `noticias.csv`, en la carpeta de arriba —junto al visor, que es donde tiene que
estar—, con once columnas. Están explicadas en la cabecera del propio script y en el
`CLAUDE.md` de `3-comandos`.

Se escribe en **UTF-8 con BOM**, que es lo que hace que LibreOffice y Excel abran los
acentos bien sin preguntar nada.

---

## Qué se puede cambiar sin saber programar

Dos cosas, y son las dos que vais a querer tocar:

### Los medios: `fuentes.csv`

Está en la carpeta principal. Se abre con LibreOffice Calc o con el Bloc de notas. Cuatro
columnas:

| Columna | Qué es |
|---|---|
| `nombre` | cómo queréis que aparezca en la tabla |
| `url` | la dirección del **listado** del medio (su «feed»), no la de su portada |
| `tipo` | `especializada` · `generalista` · `oficial` · `suscripcion` |
| `tope` | cuántas noticias coger como mucho de ese medio |

El `tipo` decide **una sola cosa**: los `generalista` y `oficial` pasan por el filtro de
temas —publican de todo—; los `especializada` y `suscripcion` no.

**Para añadir un medio**: una fila más. La dirección del listado suele ser la del medio
con `/feed` o `/rss` al final. Si no funciona, el script lo dirá al ejecutarse y seguirá
con los demás.

### Los temas: dentro del script

Abrid `descargar_noticias.py` con el Bloc de notas y buscad `CLAVES_TEMATICAS`. Está
señalado con un comentario grande que dice que es lo primero que vais a querer cambiar.

Es una lista de palabras. Reglas:

- **Sin tildes y en minúsculas.**
- **Basta la raíz**: `rehabilitac` vale para rehabilitación, rehabilitar y rehabilitado.
- Una por línea, entre comillas y con una coma detrás.

La lista que hay ahora salió de la sesión del 23, dictada por vosotros.

---

## Lo que el script no puede hacer

**No entra en medios de suscripción** más allá de lo que publiquen abierto, ni en nada que
pida usuario y contraseña.

**No entiende lo que lee.** Su etiqueta de relevancia mira palabras, no sentido: por eso
se llama *pre-filtro* y por eso el paso siguiente es clasificar con una IA, que sí lee el
texto. Comparar las dos es, literalmente, la diferencia entre el filtrado por palabra
clave que ya tenéis montado y el semántico.
