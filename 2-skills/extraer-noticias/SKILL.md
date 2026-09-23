---
name: extraer-noticias
description: Reúne noticias recientes de unas fuentes dadas sobre vivienda, suelo, alquiler, rehabilitación, urbanismo, eficiencia energética y políticas públicas, y las devuelve en un CSV listo para abrir en el visor. Úsala cuando pidan recopilar, buscar o descargar noticias para vigilancia del entorno.
---

# Extraer noticias

Reúne lo publicado sobre los temas de vigilancia de una agencia pública de vivienda, con
su fuente y su enlace, y lo devuelve en CSV.

## Lo que hay que preguntar antes de empezar

Si la persona no lo ha dicho, pregunta **las dos cosas a la vez, en un solo mensaje**, y
propón un valor por defecto para cada una:

1. **De qué fuentes.** Por defecto: Brains Real Estate News, Inmodiario, Construible,
   Innovando en la Construcción, OVACEN, Fotocasa Research, Expansión (inmobiliario),
   20minutos (vivienda), El Periódico de la Energía, Demócrata, BOE y la sala de prensa
   de la Comisión Europea.
2. **Qué periodo.** Por defecto, los últimos 14 días. Siempre relativo a hoy.

Si contesta «lo que propongas», tira con los valores por defecto y dilo en una línea.

## Los temas que interesan

Vivienda · alquiler · compraventa de vivienda · hipotecas · suelo y urbanismo ·
rehabilitación · construcción y edificación · eficiencia energética y energía ·
políticas de vivienda · políticas sociales y necesidades sociales · administración
pública · proyectos de innovación y fondos europeos · economía general cuando afecte a
la vivienda (IPC, inflación, tipos) · y cualquier mención a AVRA o a la Agencia de
Vivienda y Rehabilitación de Andalucía.

## Cómo hacerlo

1. Busca en internet, fuente por fuente, lo publicado dentro del periodo.
2. Entra en cada noticia y quédate con el texto del artículo, no con el resumen del
   listado. El resumen está cortado a media frase y no sirve para clasificar después.
3. Descarta lo anterior al periodo, aunque parezca relevante.
4. A cada noticia ponle una etiqueta de relevancia provisional:
   - `alta` — el ámbito de la Agencia aparece en el titular o de forma repetida
   - `dudosa` — lo toca de refilón; hay que leerlo para decidir
   - `fuera` — no aparece el ámbito; candidata a descarte

**No borres lo que marques como `fuera`.** Se queda en la tabla, marcado. Saber cuánto
ruido hay, y de dónde viene, es parte del trabajo de vigilancia.

## Qué devolver

Un bloque de código con un CSV, con esta cabecera exacta:

```
id,titular,fuente,fecha,url,cuerpo,cuerpo_completo,palabras_cuerpo,relevancia_prefiltro,motivo_prefiltro
```

| Columna | Qué lleva |
|---|---|
| `id` | número de orden, desde 1 |
| `titular` | literal, sin reescribir |
| `fuente` | nombre del medio |
| `fecha` | AAAA-MM-DD |
| `url` | enlace exacto |
| `cuerpo` | el texto del artículo, todo el que hayas podido obtener |
| `cuerpo_completo` | `si` / `parcial` / `no` |
| `palabras_cuerpo` | cuántas palabras tiene el cuerpo |
| `relevancia_prefiltro` | `alta` / `dudosa` / `fuera` |
| `motivo_prefiltro` | la razón, en menos de quince palabras |

Después del CSV, di cuántas noticias has encontrado por fuente y cuáles no pudiste
consultar.

## Reglas, y son innegociables

- **Cero invención**: ni un titular, ni una cifra, ni una URL. Si no tienes el enlace
  exacto, la noticia no entra.
- No completes con conocimiento previo tuyo: solo lo publicado en el periodo.
- No agrupes ni interpretes todavía. Aquí solo se recoge.

## Antes de entregar, responde a esto

1. ¿De dónde viene cada dato? Debe bastar con abrir su enlace.
2. ¿Qué has dado por supuesto? Decláralo.
3. ¿Podría defenderse esto sin decir que lo hizo una IA?
4. ¿Qué falta? ¿Qué fuentes no pudiste consultar?
5. ¿Esto acerca a una decisión, o es ruido?

## Al terminar, recuérdalo

Que el CSV se guarda en un fichero `.csv` y se abre con el visor (`index.html`, botón
**«Abrir un CSV»**), o con LibreOffice Calc eligiendo UTF-8 y coma como separador.
