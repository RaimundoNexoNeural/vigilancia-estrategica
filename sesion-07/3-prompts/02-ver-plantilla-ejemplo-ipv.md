
INSTRUCCIONES. Quiero que construyas con el fichero que te he adjuntado las gráficas que te defino más abajo, exactamente como las defino. No elijas tú otras gráficas ni cambies mis ajustes; si algún ajuste es imposible o engañoso, dímelo antes de dibujar y propón una alternativa. Si ya has estudiado el fichero antes en esta conversación, usa ese estudio y no lo repitas.

CONOCIMIENTO DEL FICHERO
- Nombre de la hoja con los datos originales: in
- Columna con el periodo o la fecha: Periodo
- Columna con el territorio o la categoría: Comunidades y Ciudades Autónomas
- Columna con el valor: Total
- Columnas que sirven para filtrar y sus valores: «General, vivienda nueva y de segunda mano» = General; «Índices y tasas» = Índice o Variación anual
- Cómo se identifica un total (por ejemplo, el total nacional): es la fila con la columna «Comunidades y Ciudades Autónomas» vacía (la columna «Total Nacional» vale «Nacional» en todas las filas y no sirve para filtrar)
- Unidad: no consta

HERRAMIENTAS
- Programa de hoja de cálculo: Excel

GRÁFICA 1
- Título: Índice general de precio de la vivienda: total nacional y comunidades (2007T1–2026T2)
- Tipo: líneas
- Qué mide (medida y filtros): «General, vivienda nueva y de segunda mano» = General, «Índices y tasas» = Índice
- Series: una por territorio; cuántas: 20; cuáles: el total nacional y las 19 comunidades y ciudades autónomas (el total nacional destacado con una línea más gruesa)
- Periodo o categorías en el eje horizontal: de 2007T1 a 2026T2, con una etiqueta por año
- Eje vertical: mínimo automático, máximo automático (ajustado al rango de los datos, sin forzar el cero)
- Orden: cronológico
- Valores escritos sobre la gráfica: no
- Límites y avisos: no mezclar con las variaciones; no escribir «euros»

GRÁFICA 2
- Título: Índice general de precio de la vivienda por comunidad, 2026T2
- Tipo: barras horizontales
- Qué mide (medida y filtros): «General, vivienda nueva y de segunda mano» = General, «Índices y tasas» = Índice, Periodo = 2026T2
- Series: una sola, con una barra por territorio; cuántas: 19; cuáles: las 19 comunidades y ciudades autónomas (sin el total nacional)
- Periodo o categorías en el eje horizontal: las 19 comunidades, sin el código numérico del nombre
- Eje vertical: mínimo 100, máximo 116 (eje recortado a propósito para ver las diferencias; hay que decirlo en la ficha)
- Orden: de mayor a menor
- Valores escritos sobre la gráfica: sí
- Límites y avisos: no es una comparación de precios reales entre comunidades, solo de la posición de cada índice en ese trimestre

GRÁFICA 3
- Título: Variación anual del índice general: total nacional y cinco comunidades (2007T1–2026T2)
- Tipo: líneas
- Qué mide (medida y filtros): «General, vivienda nueva y de segunda mano» = General, «Índices y tasas» = Variación anual
- Series: una por territorio; cuántas: 6; cuáles: el total nacional, Andalucía, Cataluña, Madrid, País Vasco y Comunitat Valenciana
- Periodo o categorías en el eje horizontal: de 2007T1 a 2026T2, con una etiqueta por año
- Eje vertical: mínimo automático, máximo automático, con una línea de referencia en 0
- Orden: cronológico
- Valores escritos sobre la gráfica: no
- Límites y avisos: no mezclar con el índice; las celdas vacías no se dibujan

FORMATO DE LA RESPUESTA. Hazlo todo en una sola respuesta, en este orden:

1. CONFIRMACIÓN. Una línea por gráfica con lo que has entendido (tipo, medida, nº de series, eje). Si algo de lo que te he pedido es imposible, ambiguo o engañoso, dilo aquí.

2. LAS GRÁFICAS. Muéstramelas de verdad, sea cual sea tu herramienta:
- Si puedes modificar el fichero (por ejemplo, Copilot en Excel), crea cada gráfica en una hoja nueva del libro. Si no puedes, dibújalas con código, enséñamelas en la conversación y entrégame también el fichero modificado si puedes generarlo.
- Si ni siquiera puedes dibujarlas, dilo claramente en lugar de describirlas con palabras.

3. CÓMO SE HA HECHO. Para cada gráfica, una ficha corta:
- Datos: columnas usadas, filtros aplicados y, para cada tabla auxiliar, qué rango o qué fórmula alimenta cada serie.
- Qué muestra y qué NO puede mostrar.
- Valor máximo y valor mínimo de lo que se dibuja, cada uno con su fecha o categoría.
- COMPROBACIÓN: confirma que esos máximos y mínimos, y un valor concreto de cada tabla auxiliar, coinciden con los de la hoja original, y escribe el resultado («coincide» o «no coincidía, corregido»).

4. CÓMO HACERLA YO. Pasos numerados, para alguien sin experiencia, para construir cada gráfica dentro del fichero con el programa indicado (nombre de la hoja, qué columnas seleccionar, cómo filtrar y qué tipo de gráfica elegir). Si la herramienta ya la ha creado en el libro, indica solo dónde está y cómo cambiarla.

REGLAS DE TRABAJO CON EL FICHERO
- Los datos se leen siempre de la hoja original, que no se modifica. Nada de copiar ni pegar valores: si necesitas filtrar o agrupar, crea una tabla auxiliar cuyas celdas sean fórmulas que lean de la hoja original.
- Usa solo fórmulas que funcionen igual en Excel y en LibreOffice (por ejemplo SUMAR.SI.CONJUNTO o SUMIFS, e INDICE). No uses FILTRAR, ORDENAR, UNICOS ni otras funciones de matriz dinámica.
- Si generas el fichero con código, escribe los nombres de las funciones en inglés (SUMIFS, INDEX…): es lo único que admite el formato del fichero, y el programa las mostrará en el idioma del usuario.
- Antes de filtrar, mira qué valores distintos tiene cada columna. No uses como filtro una columna que tenga el mismo valor en todas las filas. Si una fila de totales se identifica por una celda vacía en otra columna, filtra por esa celda vacía.
- Cuenta solo lo que ves en el fichero. Si algo no consta (unidad, base de un índice, fuente), escribe «no consta» y no lo inventes; no escribas «euros» ni «porcentaje» si el fichero no lo dice.
- Si afirmas algo por conocimiento general y no porque conste en el fichero, márcalo con (CG).
- No mezcles en una misma gráfica medidas distintas (por ejemplo, un índice con una variación). Si el fichero las mezcla en una columna, sepáralas con un filtro y dime cuál has usado.
- Si el fichero tiene totales y subcategorías, usa la misma categoría en todas las gráficas o explica por qué cambias.
- Si hay filas de totales, celdas vacías o símbolos en lugar de números, dime cómo los has tratado.
- Lo que declares en las fichas (series, filtros, ejes) debe ser lo que de verdad contiene el fichero, no solo la imagen de la conversación.
- Respeta los ajustes de eje que te he dado. Si el eje vertical no empieza en cero, dilo en el título o en la ficha.
- Eje de tiempo con pocas etiquetas legibles y sin solaparse, leyenda clara y nombres de territorio sin códigos innecesarios.
- No hagas todavía ningún análisis ni saques conclusiones: esto es solo para ver los datos.

