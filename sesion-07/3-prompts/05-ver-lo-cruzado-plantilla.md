
INSTRUCCIONES. Te adjunto un libro de hoja de cálculo que contiene una hoja de datos ya cruzados (resultado de unir varias tablas originales). Quiero VISUALIZAR esos datos cruzados con las gráficas que te defino más abajo, exactamente como las defino. No elijas tú otras gráficas ni cambies mis ajustes; si algún ajuste es imposible o engañoso, dímelo antes de dibujar y propón una alternativa. No analices los datos ni saques conclusiones: esto es solo para verlos.

CONOCIMIENTO DEL LIBRO
- Hoja de datos cruzados: [nombre de la hoja] · una fila por [territorio y periodo] · [número de filas] filas
- Columnas: [letra y contenido de cada una: territorio, periodo y cada serie, con su categoría, su medida y su unidad (o «no consta»)]
- Territorios: [número y lista resumida] · Periodo: [desde – hasta] · frecuencia [mensual, trimestral o anual]
- Otras hojas del libro (tablas originales, equivalencias, parámetros, notas): no se tocan.
- Cómo se identifica un total (por ejemplo, el total nacional): [texto que aparece en la hoja]

HERRAMIENTAS
- Programa de hoja de cálculo: [Excel o LibreOffice]

GRÁFICA 1
- Título: [título]
- Tipo: [líneas / barras horizontales / barras agrupadas / dispersión con los puntos unidos en orden cronológico / mapa de calor]
- Series que se dibujan: [columnas del cruce]
- Territorio o territorios: [uno, varios o todos]
- Transformación: [ninguna / base 100 en [periodo base] / dos ejes verticales / otra]
- Periodo o categorías: [desde – hasta, o lista]
- Ejes: mínimo [valor o «automático»], máximo [valor o «automático»]
- Orden: [cronológico / de mayor a menor por una serie / otro]
- Valores escritos sobre la gráfica: [sí / no]
- Límites y avisos: [qué no debe mezclarse ni mostrarse]

GRÁFICA 2
- Título: [título]
- Tipo: [tipo]
- Series que se dibujan: [columnas del cruce]
- Territorio o territorios: [territorios]
- Transformación: [transformación]
- Periodo o categorías: [periodo o lista]
- Ejes: mínimo [valor o «automático»], máximo [valor o «automático»]
- Orden: [orden]
- Valores escritos sobre la gráfica: [sí / no]
- Límites y avisos: [límites]

GRÁFICA 3
- Título: [título]
- Tipo: [tipo]
- Series que se dibujan: [columnas del cruce]
- Territorio o territorios: [territorios]
- Transformación: [transformación]
- Periodo o categorías: [periodo o lista]
- Ejes: mínimo [valor o «automático»], máximo [valor o «automático»]
- Orden: [orden]
- Valores escritos sobre la gráfica: [sí / no]
- Límites y avisos: [límites]

(Si necesitas menos de tres gráficas, borra las que sobren.)

FORMATO DE LA RESPUESTA. Hazlo todo en una sola respuesta, con el texto en 600 palabras como máximo (sin contar las gráficas), en este orden:

1. CONFIRMACIÓN. Una línea por gráfica con lo que has entendido (tipo, series, territorio, transformación, ejes). Si algo de lo que te he pedido es imposible, ambiguo o engañoso, dilo aquí.

2. LAS GRÁFICAS. Muéstramelas de verdad, sea cual sea tu herramienta:
- Si puedes modificar el libro (por ejemplo, Copilot en Excel), crea cada gráfica en una hoja nueva («Gráfica 1», «Gráfica 2»…).
- Si no puedes, dibújalas con código, enséñamelas en la conversación y entrégame también el libro modificado para descargarlo, con las gráficas en hojas nuevas, si puedes generarlo.
- Si ni siquiera puedes dibujarlas, dilo claramente en lugar de describirlas con palabras.

3. CÓMO SE HA HECHO. Para cada gráfica, una ficha corta:
- Datos: columnas del cruce usadas, filtros aplicados y, para cada tabla auxiliar, qué rango o qué fórmula alimenta cada serie.
- Transformación aplicada y fórmula usada.
- Qué muestra y qué NO puede mostrar.
- Valor máximo y valor mínimo de cada serie dibujada, con su territorio y su periodo.
- COMPROBACIÓN: confirma que esos máximos y mínimos, y un valor concreto de cada tabla auxiliar, coinciden con los de la hoja del cruce, y escribe el resultado («coincide» o «no coincidía, corregido»).

4. CÓMO HACERLA YO. Pasos numerados, para alguien sin experiencia, para construir cada gráfica con el programa indicado (nombre de la hoja, qué columnas seleccionar, cómo hacer la transformación y qué tipo de gráfica elegir). Si la herramienta ya la ha creado en el libro, indica solo dónde está y cómo cambiarla.

REGLAS DE TRABAJO CON EL LIBRO
- NADA SE COPIA NI SE PEGA. Las hojas existentes no se modifican. Cada gráfica lee directamente de la hoja del cruce o de una tabla auxiliar, situada en la hoja nueva de esa gráfica, cuyas celdas sean FÓRMULAS que lean de la hoja del cruce. Cualquier cálculo (elegir un territorio, pasar a base 100, ordenar) se hace con funciones que lean de la hoja del cruce; nunca escribas valores ya calculados.
- Usa solo fórmulas que funcionen igual en Excel y en LibreOffice (por ejemplo SUMAR.SI.CONJUNTO o SUMIFS, INDICE, COINCIDIR). No uses FILTRAR, ORDENAR, UNICOS, LET ni otras funciones de matriz dinámica.
- Si generas el fichero con código, escribe los nombres de las funciones en inglés (SUMIFS, INDEX, MATCH…): es lo único que admite el formato del fichero, y el programa las mostrará en el idioma del usuario.
- Cuando el criterio de un filtro sea «celda vacía», escríbelo como texto vacío (""). Nunca apuntes el criterio a una celda en blanco: Excel la interpreta como 0 y no encuentra nada.
- Un vacío y un cero son cosas distintas: una celda vacía no se dibuja como 0 (déjala como hueco). Si una transformación divide por un valor base que está vacío o es 0, deja la celda vacía.
- Series con unidades distintas no se dibujan en el mismo eje sin transformar. Si usas una transformación (por ejemplo, base 100), di cuál es el periodo base y recuerda que esa elección condiciona la lectura.
- Cuenta solo lo que consta en el libro. Si algo no consta (unidad, base de un índice, fuente), escribe «no consta» y no lo inventes; no escribas «euros» ni «porcentaje» si no se dice. Si afirmas algo por conocimiento general, márcalo con (CG).
- Lo que declares en las fichas (series, territorios, transformación, ejes) debe ser lo que de verdad contiene el libro, no solo la imagen de la conversación.
- Respeta los ajustes de eje que te he dado. Si el eje vertical no empieza en cero, dilo en el título o en la ficha.
- Eje de tiempo con pocas etiquetas legibles y sin solaparse, leyenda clara, título con lo que realmente se mide y nombres de territorio sin códigos innecesarios.
- No hagas ningún análisis ni saques conclusiones: esto es solo para ver los datos.

