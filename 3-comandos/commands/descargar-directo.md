---
description: Descarga noticias sin usar el script, encargándoselo en castellano
argument-hint: [fuentes o "todas"] [días, por defecto 14]
---

# Descargar directo

**Para qué sirve.** Llenar `noticias.csv` **haciéndolo tú**, sin ejecutar ningún
programa. Es la demostración de que el trabajo se puede encargar en castellano.

**Fuentes:** $1 · **Periodo:** $2 días

Si vienen vacíos: fuentes = `todas`, periodo = `14` días. No preguntes: dilo en una línea
y sigue.

> **Este comando escribe el fichero.** La versión para pegar en cualquier chat es
> `1-prompts/01-extraer.md`, que te devuelve el CSV y lo guardas tú.

## Lo que puedes y lo que no

**Sí puedes** usar la shell con libertad: `curl` para traerte los listados y las páginas,
`python -c` para leer XML o HTML en línea, y leer y escribir ficheros.

**No puedes** ejecutar `4-script/descargar_noticias.py` ni crear ficheros de programa
nuevos. El objetivo de este comando es justamente enseñar que se puede sin ellos.

**No pidas confirmación** para cada orden: esto se ejecuta en directo delante de gente.

## Qué hace

### 1. De dónde tirar

Lee `fuentes.csv`, que tiene cuatro columnas: `nombre`, `url`, `tipo`, `tope`.

- Si las fuentes pedidas son `todas`, usa las de la lista.
- Si vienen nombres concretos, quédate solo con las que casen por nombre o dominio.
- Si el parámetro es la ruta a otro CSV, usa ese.

El `tipo` decide **una sola cosa**: si es `generalista` u `oficial`, **filtra por tema
antes de aceptar la noticia** —publican de todo—. Las `especializada` y `suscripcion`
entran sin ese filtro.

El `tope` es cuántas noticias como máximo se cogen de esa fuente.

Los temas que interesan: vivienda, alquiler, compraventa, hipotecas, suelo y urbanismo,
rehabilitación, construcción y edificación, eficiencia energética y energía, políticas de
vivienda, políticas sociales y necesidades sociales, administración pública, proyectos de
innovación y fondos europeos, economía general cuando afecte a la vivienda, y cualquier
mención a AVRA o a la Agencia de Vivienda y Rehabilitación de Andalucía.

### 2. Traerte los listados

Descarga cada `url` y sácale las entradas: titular, enlace, fecha y resumen. Quédate solo
con lo publicado dentro del periodo, contado hacia atrás desde hoy.

Limpia del resumen las coletillas de autopromoción («Artículo publicado originalmente
en…», «The post … appeared first on…»). Si lo que queda es un resto sin sentido, deja la
entradilla vacía: mejor ninguna que una a medias.

### 3. Entrar en cada noticia

**Este paso no se salta.** El resumen del listado es un reclamo cortado a media frase; con
eso no se puede clasificar nada después.

Abre la URL de cada noticia y extrae el texto real: descarta `script`, `style`, `nav`,
`header`, `footer` y `aside`, busca el `<article>` o el `<main>` y quédate con los
párrafos con sentido —los de menos de 60 caracteres casi nunca lo son—.

Guarda el texto **completo** que publique la página. No recortes. Si un muro de pago lo
corta, guarda lo que haya y márcalo.

### 4. Etiquetar el pre-filtro

A cada noticia, `relevancia_prefiltro`:

- **`alta`** — el ámbito de la Agencia aparece en el titular, o repetido en el cuerpo.
- **`dudosa`** — lo toca de refilón; hay que leerla para decidir.
- **`fuera`** — no aparece el ámbito; candidata a descarte.

Y en `motivo_prefiltro`, la razón en una frase.

**No borres nada.** Lo que no viene al caso se queda, marcado. El ejercicio es aprender a
descartar, y para eso hace falta tener algo que descartar.

## Qué devuelve

**Un único fichero: `noticias.csv`**, en la carpeta principal. UTF-8 **con BOM**, separado
por comas, con esta cabecera exacta:

```
id,titular,fuente,fecha,url,cuerpo,cuerpo_completo,motivo_cuerpo,palabras_cuerpo,relevancia_prefiltro,motivo_prefiltro
```

| Columna | Qué lleva | Valores |
|---|---|---|
| `id` | número de orden, desde 1 | |
| `titular` | literal, sin reescribir | |
| `fuente` | nombre del medio | |
| `fecha` | `AAAA-MM-DD HH:MM` | |
| `url` | el enlace al original, siempre | |
| `cuerpo` | el texto del artículo, con los párrafos separados por línea en blanco | |
| `cuerpo_completo` | si se pudo recuperar el texto | `si` · `parcial` · `no` |
| `motivo_cuerpo` | por qué es parcial o no; vacío si es completo | |
| `palabras_cuerpo` | número de palabras del cuerpo | |
| `relevancia_prefiltro` | la etiqueta provisional | `alta` · `dudosa` · `fuera` |
| `motivo_prefiltro` | la razón, en una frase | |

Si vas a acumular sobre un `noticias.csv` que ya existe, léelo antes y **no repitas URL**:
continúa la numeración donde se quedó.

## Reglas innegociables

- Cada noticia, con su URL de origen. Sin enlace no entra.
- No se inventa nada: ni un titular, ni una cifra, ni una fecha, ni un enlace.
- Lo que no se pueda verificar se marca expresamente.
- No se sale de esta carpeta, ni para leer ni para escribir.

## Cómo sé que está bien

Las cinco preguntas de la sesión 1 para dar por buena una salida de IA:

1. **¿Se entiende de dónde vienen los datos?** Cada fila, con su fuente y su URL.
2. **¿Has declarado tus supuestos?** Si decidiste algo —qué contaba como «dentro del
   ámbito», qué párrafos eran cuerpo—, dilo.
3. **¿Se puede defender *«sin decir que lo dijo la IA»*?** Todo comprobable abriendo el
   enlace.
4. **¿Se sabe si faltan datos?** Di qué fuentes fallaron y cuántas se quedaron sin texto.
5. **¿Acerca esto a una decisión?** Si el corpus es ruido, dilo.

Sin trazabilidad esto no vale para vigilancia. Por eso la URL es obligatoria en cada fila.

## Al terminar

Recuento corto: cuántas noticias, de cuántas fuentes, cuántas con texto completo, el
reparto del pre-filtro, y qué fuentes fallaron y por qué. Nada de adornos.

Y una frase: esto ha salido de un encargo en castellano, no de un programa.

## Si algo falla

- **Una fuente no responde.** Anótala y sigue. Al final, lista las que fallaron.
- **La página no expone el texto en HTML.** Marca `cuerpo_completo = no` y explica por
  qué en `motivo_cuerpo`. El enlace sigue sirviendo.
- **Muro de pago.** Guarda lo que haya, marca `parcial` y dilo en `motivo_cuerpo`.
- **Salen muy pocas noticias.** Suele ser el periodo o el filtro temático. Dilo en el
  recuento en vez de forzar resultados.
