
INSTRUCCIONES. Te adjunto un libro de hoja de cálculo que contiene una hoja de datos ya cruzados (resultado de unir varias tablas originales). Quiero VISUALIZAR esos datos cruzados con las gráficas que te defino más abajo, exactamente como las defino. No elijas tú otras gráficas ni cambies mis ajustes; si algún ajuste es imposible o engañoso, dímelo antes de dibujar y propón una alternativa. No analices los datos ni saques conclusiones: esto es solo para verlos.

CONOCIMIENTO DEL LIBRO
- Hoja de datos cruzados: «Cruce» · una fila por territorio y trimestre · 1.560 filas (20 territorios × 78 trimestres) bajo la cabecera de la fila 1
- Columnas: A = Territorio (el nombre sin código; el total nacional se llama «Total nacional»); B = Trimestre (texto, por ejemplo 2026T2); C = índice de precios de la vivienda (categoría General; unidad: no consta); D = hipotecas sobre viviendas, número (suma de los tres meses del trimestre); E = compraventas de viviendas, total (suma de los tres meses del trimestre; unidad: no consta). Las columnas C, D y E tienen unidades distintas: no se pueden dibujar en el mismo eje sin transformarlas.
- Territorios: el total nacional y las 19 comunidades y ciudades autónomas · Periodo: de 2007T1 a 2026T2 · frecuencia trimestral
- Otras hojas del libro (las tres tablas originales, «Equivalencias», «Parámetros», «Notas»): no se tocan.

HERRAMIENTAS
- Programa de hoja de cálculo: Excel

GRÁFICA 1
- Título: Andalucía: precio, hipotecas y compraventas de vivienda (base 100 = 2007T1)
- Tipo: líneas
- Series que se dibujan: C (índice de precios), D (hipotecas) y E (compraventas)
- Territorio o territorios: Andalucía
- Transformación: base 100 en 2007T1, es decir, cada serie dividida por su propio valor de 2007T1 y multiplicada por 100; la transformación debe hacerse con fórmulas que lean de la hoja «Cruce»
- Periodo o categorías: de 2007T1 a 2026T2, con una etiqueta por año
- Ejes: mínimo automático, máximo automático (ajustado al rango de los datos, sin forzar el cero)
- Orden: cronológico
- Valores escritos sobre la gráfica: no
- Límites y avisos: la base 2007T1 es el primer trimestre y condiciona la lectura; no escribir «euros» ni «porcentaje»; no mezclar series sin transformar

GRÁFICA 2
- Título: Andalucía: índice de precios frente a compraventas, un punto por trimestre
- Tipo: dispersión con los puntos unidos en orden cronológico
- Series que se dibujan: C (índice de precios) en el eje horizontal y E (compraventas) en el eje vertical
- Territorio o territorios: Andalucía
- Transformación: ninguna
- Periodo o categorías: de 2007T1 a 2026T2 (78 puntos); rotula el primero (2007T1) y el último (2026T2)
- Ejes: mínimo automático, máximo automático en los dos ejes (sin forzar el cero)
- Orden: cronológico (la línea une los puntos en el orden del tiempo)
- Valores escritos sobre la gráfica: solo en el primer y el último punto
- Límites y avisos: cada punto es un trimestre; la gráfica no demuestra ninguna causa; los ejes no empiezan en cero y hay que decirlo

GRÁFICA 3
- Título: Comunidades y ciudades autónomas en 2026T2: precio, hipotecas y compraventas (base 100 = 2007T1)
- Tipo: barras horizontales agrupadas (tres barras por territorio)
- Series que se dibujan: C (índice de precios), D (hipotecas) y E (compraventas), cada una en base 100
- Territorio o territorios: las 19 comunidades y ciudades autónomas (sin el total nacional)
- Transformación: para cada territorio y cada serie, el valor de 2026T2 dividido por el valor de 2007T1 y multiplicado por 100, con fórmulas que lean de la hoja «Cruce»
- Periodo o categorías: un solo periodo, 2026T2 (con base 2007T1)
- Ejes: mínimo 0, máximo automático
- Orden: de mayor a menor según el índice de precios
- Valores escritos sobre la gráfica: no
- Límites y avisos: la base 2007T1 condiciona la lectura; las comunidades se comparan entre sí en variación frente a su propio punto de partida, no en niveles

FORMATO DE LA RESPUESTA. Hazlo todo en una sola respuesta, con el texto en 600 palabras como máximo (sin contar las gráficas), en este orden:

1. CONFIRMACIÓN. Una línea por gráfica con lo que has entendido (tipo, series, territorio, transformación, ejes). Si algo de lo que te he pedido es imposible, ambiguo o engañoso, dilo aquí.

2. LAS GRÁFICAS. Muéstramelas de verdad, sea cual sea tu herramienta:
- Si puedes modificar el libro (por ejemplo, Copilot en Excel), crea cada gráfica en una hoja nueva («Gráfica 1», «Gráfica 2», «Gráfica 3»).
- Si no puedes, dibújalas con código, enséñamelas en la conversación y entrégame también el libro modificado para descargarlo, con las gráficas en hojas nuevas, si puedes generarlo.
- Si ni siquiera puedes dibujarlas, dilo claramente en lugar de describirlas con palabras.

3. CÓMO SE HA HECHO. Para cada gráfica, una ficha corta:
- Datos: columnas del cruce usadas, filtros aplicados y, para cada tabla auxiliar, qué rango o qué fórmula alimenta cada serie.
- Transformación aplicada y fórmula usada.
- Qué muestra y qué NO puede mostrar.
- Valor máximo y valor mínimo de cada serie dibujada, con su territorio y su periodo.
- COMPROBACIÓN: confirma que esos máximos y mínimos, y un valor concreto de cada tabla auxiliar, coinciden con los de la hoja del cruce, y escribe el resultado («coincide» o «no coincidía, corregido»).

4. CÓMO HACERLA YO. Pasos numerados, para alguien sin experiencia, para construir cada gráfica con Excel (nombre de la hoja, qué columnas seleccionar, cómo hacer la transformación y qué tipo de gráfica elegir). Si la herramienta ya la ha creado en el libro, indica solo dónde está y cómo cambiarla.

REGLAS DE TRABAJO CON EL LIBRO
- NADA SE COPIA NI SE PEGA. Las hojas existentes no se modifican. Cada gráfica lee directamente de la hoja «Cruce» o de una tabla auxiliar, situada en la hoja nueva de esa gráfica, cuyas celdas sean FÓRMULAS que lean de la hoja «Cruce». Cualquier cálculo (elegir un territorio, pasar a base 100, ordenar) se hace con funciones que lean de «Cruce»; nunca escribas valores ya calculados.
- Usa solo fórmulas que funcionen igual en Excel y en LibreOffice (por ejemplo SUMAR.SI.CONJUNTO o SUMIFS, INDICE, COINCIDIR). No uses FILTRAR, ORDENAR, UNICOS, LET ni otras funciones de matriz dinámica.
- Si generas el fichero con código, escribe los nombres de las funciones en inglés (SUMIFS, INDEX, MATCH…): es lo único que admite el formato del fichero, y el programa las mostrará en el idioma del usuario.
- Un vacío y un cero son cosas distintas: una celda vacía no se dibuja como 0 (déjala como hueco). Si una transformación divide por un valor base que está vacío o es 0, deja la celda vacía.
- Series con unidades distintas no se dibujan en el mismo eje sin transformar. Di cuál es el periodo base y recuerda que esa elección condiciona la lectura.
- Cuenta solo lo que consta en el libro. Si algo no consta (unidad, base de un índice, fuente), escribe «no consta» y no lo inventes; no escribas «euros» ni «porcentaje» si no se dice. Si afirmas algo por conocimiento general, márcalo con (CG).
- Lo que declares en las fichas (series, territorios, transformación, ejes) debe ser lo que de verdad contiene el libro, no solo la imagen de la conversación.
- Respeta los ajustes de eje que te he dado. Si el eje vertical no empieza en cero, dilo en el título o en la ficha.
- Eje de tiempo con pocas etiquetas legibles y sin solaparse, leyenda clara, título con lo que realmente se mide y nombres de territorio sin códigos innecesarios.
- No hagas ningún análisis ni saques conclusiones: esto es solo para ver los datos.

