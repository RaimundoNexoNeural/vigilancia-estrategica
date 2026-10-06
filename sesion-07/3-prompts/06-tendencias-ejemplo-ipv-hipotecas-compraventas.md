
INSTRUCCIONES. Actúa como un analista experto en estadística y series temporales. Te adjunto un libro de hoja de cálculo que contiene una hoja de datos ya cruzados. Quiero ESTUDIAR LAS TENDENCIAS de esos datos de forma rigurosa y justificada: cada resultado debe llevar su método, la razón de usarlo, sus supuestos y sus límites. Aplica exactamente las definiciones que te doy abajo. No saques conclusiones sobre causas ni hagas previsiones.

CONOCIMIENTO DEL LIBRO
- Hoja de datos cruzados: «Cruce» · una fila por territorio y trimestre · 1.560 filas (20 territorios × 78 trimestres), ordenadas por territorio y trimestre, bajo la cabecera de la fila 1
- Columnas: A = Territorio (nombre sin código; el total nacional se llama «Total nacional»); B = Trimestre (texto, por ejemplo 2026T2); C = índice de precios de la vivienda (índice o nivel; unidad: no consta); D = hipotecas sobre viviendas, número (flujo: suma de los tres meses del trimestre); E = compraventas de viviendas, total (flujo: suma de los tres meses del trimestre; unidad: no consta)
- Territorios: el total nacional y las 19 comunidades y ciudades autónomas · Periodo: de 2007T1 a 2026T2 · frecuencia trimestral
- Otras hojas del libro (las tres tablas originales, «Equivalencias», «Parámetros», «Notas», «Gráfica 1», «Gráfica 2», «Gráfica 3»): no se tocan.

PARÁMETROS DEL ESTUDIO (fijados antes de mirar los resultados; no los cambies para mejorar un resultado)
- Serie de referencia: C (índice de precios) · series que se comparan con ella: D (hipotecas) y E (compraventas)
- Territorio de interés: Andalucía · territorio de comparación: Total nacional · grupo de referencia: los otros 18 territorios (comunidades y ciudades autónomas, sin Andalucía)
- Periodos por año (s): 4
- Periodo de análisis de las variaciones: de 2008T1 a 2026T2 (74 trimestres, porque 2007 no tiene año anterior)
- Años para las fases: 2007, 2013 y 2025 (años completos; 2026 está incompleto)
- Corte entre los dos subperiodos de la relación: 2014T1, el trimestre del mínimo del índice de precios nacional (elección del analista, que condiciona los resultados); subperiodo 1: de 2008T1 a 2013T4; subperiodo 2: de 2014T1 a 2026T2
- Desfase máximo: 8 trimestres · umbral de relación apreciable: |r| ≥ 0,4 · nivel de confianza: 95 %

MÉTODO. Haz los análisis A, B, C y D, cada uno en una hoja nueva con ese nombre.

A. VARIACIONES («Variaciones»). Variación interanual de cada serie, territorio y trimestre: valor del trimestre dividido por el valor del mismo trimestre del año anterior, menos 1, en %. Los trimestres de 2007 quedan vacíos. Por qué: elimina la estacionalidad, deja las series en una unidad común y evita comparar niveles que comparten una tendencia por casualidad. Destaca la variación interanual de 2026T2 de cada serie en Andalucía y en el total nacional.

B. FASES («Fases»). Agrega cada serie por año (suma para hipotecas y compraventas, media para el índice de precios) y calcula, entre 2007 y 2013 y entre 2013 y 2025: el cambio acumulado en % y la tasa de crecimiento anual compuesta, TACC = (valor final / valor inicial)^(1 / número de años) − 1. Hazlo para Andalucía, para el total nacional y para cada territorio. Compara Andalucía con la mediana del grupo de referencia e indica su posición (1 = valor más bajo) entre los 19 territorios. Por qué: resume el ritmo de cada fase sin depender de un solo trimestre y sin estacionalidad.

C. RELACIÓN («Relación»). Coeficiente de correlación de Pearson (r) entre la variación interanual del índice de precios y la de cada una de las otras dos series, sin desfase, para Andalucía, para el total nacional y para cada territorio del grupo de referencia (resume el grupo con su mediana y su rango). Para Andalucía y para el total nacional indica además:
- n (número de observaciones) y un intervalo de confianza del 95 % con la transformación de Fisher: z = ATANH(r), error = 1 / RAIZ(n_ef − 3), límites = TANH(z ± 1,96 × error), con n_ef = n / 4. Se usa n / 4 porque las variaciones interanuales de trimestres consecutivos comparten datos y no son independientes. Si n_ef ≤ 3, deja el intervalo vacío.
- r y n en cada uno de los dos subperiodos.
Clasifica cada relación con esta regla, fijada de antemano:
- «No concluyente»: el intervalo de confianza del periodo completo incluye el 0, o |r| es menor que 0,4.
- «Robusta»: |r| ≥ 0,4, el intervalo no incluye el 0, y en los dos subperiodos r tiene el mismo signo y |r| ≥ 0,4.
- «Frágil»: |r| ≥ 0,4 y el intervalo no incluye el 0 en el periodo completo, pero no se mantiene (otro signo o |r| < 0,4) en algún subperiodo.
Por qué: una correlación de todo el periodo puede deberse a un único episodio común (por ejemplo, la crisis); los subperiodos comprueban si la relación se sostiene.

D. DESFASES («Desfases»). Para Andalucía, r entre la variación de cada una de las dos series (hipotecas y compraventas) y la del índice de precios desplazada de −8 a +8 trimestres (desfase positivo = hipotecas o compraventas preceden al índice). Entrega la tabla completa y un gráfico de barras por serie. Indica el desfase con mayor |r| y cuánto mejora respecto al desfase 0. Se calculan 17 correlaciones: el máximo es optimista, así que preséntalo como exploratorio y no como prueba de que una serie anticipa a otra.

SALIDA. Hazlo todo en una sola respuesta, con el texto en 700 palabras como máximo, en este orden:

1. PLAN. En 100 palabras como máximo: confirma los parámetros y señala lo que no se pueda hacer o no esté claro.

2. HOJAS. Crea las hojas «Variaciones», «Fases», «Relación» y «Desfases», y una hoja «Hallazgos».

3. COMPROBACIÓN. Elige una variación interanual, una correlación y una TACC; recalcúlalas por otro camino (por ejemplo, la correlación con PEARSON o con covarianza y desviaciones típicas) y escribe el resultado («coincide» o «no coincidía, corregido»). Indica el número de observaciones de cada análisis.

4. HALLAZGOS. En la hoja «Hallazgos» y en la respuesta, hasta 5 fichas ordenadas de más a menos robustas, con estas columnas: Hallazgo (una frase prudente), Dato (cifras con territorio y periodo), Cálculo (hoja y celdas), Método y por qué (máximo 40 palabras), Límites, Confianza (robusta, frágil o no concluyente). Incluye también las relaciones que NO se sostienen: son hallazgos.

5. PASOS PARA REPETIRLO. En 120 palabras como máximo: las funciones que has usado en cada análisis.

REGLAS
- NADA SE COPIA NI SE PEGA. Las hojas existentes no se modifican. Todo valor que venga de la hoja «Cruce», y todo cálculo, debe ser una FÓRMULA que lea de ella. Nunca escribas resultados ya calculados.
- Usa solo fórmulas que funcionen igual en Excel y en LibreOffice (por ejemplo SUMAR.SI.CONJUNTO o SUMIFS, PROMEDIO.SI.CONJUNTO o AVERAGEIFS, INDICE, COINCIDIR, CORREL, PEARSON, MEDIANA, MIN, MAX, K.ESIMO.MENOR, RAIZ, ATANH, TANH). No uses FILTRAR, ORDENAR, UNICOS, LET ni otras funciones de matriz dinámica.
- Si generas el fichero con código, escribe los nombres de las funciones en inglés (SUMIFS, INDEX, MATCH, CORREL…): es lo único que admite el formato del fichero.
- Cuando el criterio de un filtro sea «celda vacía», escríbelo como texto vacío (""). Nunca apuntes el criterio a una celda en blanco.
- Un vacío y un cero son cosas distintas. No imputes datos que faltan: un cálculo que dependa de un dato vacío queda vacío.
- No correlaciones niveles: solo variaciones. Una correlación entre dos series con tendencia puede ser casual.
- Los subperiodos, el umbral, el desfase máximo y las fases están fijados de antemano. Si quieres proponer otra división, preséntala aparte como prueba de sensibilidad y dilo.
- Cada afirmación lleva su cifra y la celda de donde sale. No uses «significativo» sin intervalo de confianza. No uses «causa», «provoca» ni «explica»: usa «se asocia con», «acompaña a» o «precede en el tiempo a». No hagas previsiones ni extrapolaciones.
- Distingue la tendencia de una serie (cómo cambia) de la relación entre dos series (cómo se mueven juntas).
- Cuenta solo lo que consta en el libro. Si algo no consta (unidad, base de un índice, fuente), escribe «no consta»; no escribas «euros» ni «porcentaje» si no se dice. Si afirmas algo por conocimiento general, márcalo con (CG).

