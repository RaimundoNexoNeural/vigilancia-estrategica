
INSTRUCCIONES. Actúa como un analista experto en estadística y series temporales. Te adjunto un libro de hoja de cálculo que contiene una hoja de datos ya cruzados. Quiero ESTUDIAR LAS TENDENCIAS de esos datos de forma rigurosa y justificada: cada resultado debe llevar su método, la razón de usarlo, sus supuestos y sus límites. Aplica exactamente las definiciones que te doy abajo. No saques conclusiones sobre causas ni hagas previsiones.

CONOCIMIENTO DEL LIBRO
- Hoja de datos cruzados: [nombre de la hoja] · una fila por [territorio y periodo] · [número de filas] filas, ordenadas por territorio y periodo
- Columnas: [letra y contenido de cada una: territorio, periodo y cada serie, con su medida y su unidad (o «no consta»)]
- Tipo de cada serie: [«índice o nivel» (se promedia dentro de un año) o «flujo» (se suma dentro de un año)]
- Territorios: [número y lista resumida] · Periodo: [desde – hasta] · frecuencia [mensual, trimestral o anual]
- Otras hojas del libro (tablas originales, equivalencias, parámetros, notas, gráficas): no se tocan.

PARÁMETROS DEL ESTUDIO (fijados antes de mirar los resultados; no los cambies para mejorar un resultado)
- Serie de referencia (la que se quiere entender): [columna]
- Series que se comparan con ella: [columnas]
- Territorio de interés: [territorio] · territorio de comparación: [total] · el resto de territorios (todos menos esos dos) forma el «grupo de referencia»
- Periodos por año (s): [4 si es trimestral, 12 si es mensual]
- Periodo de análisis de las variaciones: [desde – hasta]
- Años para las fases: [año inicial], [año de giro], [año final], todos años completos
- Corte entre los dos subperiodos de la relación: [periodo] (justifica en una línea por qué se ha elegido)
- Desfase máximo: [L] periodos · umbral de relación apreciable: |r| ≥ [0,4] · nivel de confianza: 95 %

MÉTODO. Haz los análisis A, B, C y D, cada uno en una hoja nueva con ese nombre.

A. VARIACIONES («Variaciones»). Variación interanual de cada serie, territorio y periodo: valor del periodo dividido por el valor del mismo periodo del año anterior, menos 1, en %. Los periodos sin año anterior quedan vacíos. Por qué: elimina la estacionalidad, deja las series en una unidad común y evita comparar niveles que comparten una tendencia por casualidad. Destaca la variación del último periodo en el territorio de interés y en el de comparación.

B. FASES («Fases»). Agrega cada serie por año (suma si es un flujo, media si es un índice o nivel) y calcula, entre el año inicial y el de giro y entre el de giro y el final: el cambio acumulado en % y la tasa de crecimiento anual compuesta, TACC = (valor final / valor inicial)^(1 / número de años) − 1. Hazlo para el territorio de interés, para el de comparación y para cada territorio. Compara el territorio de interés con la mediana del grupo de referencia e indica su posición (1 = valor más bajo) entre todos. Por qué: resume el ritmo de cada fase sin depender de un solo periodo y sin estacionalidad.

C. RELACIÓN («Relación»). Coeficiente de correlación de Pearson (r) entre la variación interanual de la serie de referencia y la de cada una de las otras series, sin desfase, para el territorio de interés, el de comparación y cada territorio del grupo de referencia (resume el grupo con su mediana y su rango). Para el territorio de interés y el de comparación indica además:
- n (número de observaciones) y un intervalo de confianza del 95 % con la transformación de Fisher: z = ATANH(r), error = 1 / RAIZ(n_ef − 3), límites = TANH(z ± 1,96 × error), con n_ef = n / s. Se usa n / s porque las variaciones interanuales de periodos consecutivos comparten datos y no son independientes. Si n_ef ≤ 3, deja el intervalo vacío.
- r y n en cada uno de los dos subperiodos (antes y después del corte).
Clasifica cada relación con esta regla, fijada de antemano:
- «No concluyente»: el intervalo de confianza del periodo completo incluye el 0, o |r| es menor que el umbral.
- «Robusta»: |r| ≥ umbral, el intervalo no incluye el 0, y en los dos subperiodos r tiene el mismo signo y |r| ≥ umbral.
- «Frágil»: |r| ≥ umbral y el intervalo no incluye el 0 en el periodo completo, pero no se mantiene (otro signo o |r| < umbral) en algún subperiodo.
Por qué: una correlación de todo el periodo puede deberse a un único episodio común (por ejemplo, una crisis); los subperiodos comprueban si la relación se sostiene.

D. DESFASES («Desfases»). Para el territorio de interés, r entre la variación de cada serie comparada y la de la serie de referencia desplazada de −L a +L periodos (desfase positivo = la serie comparada precede a la de referencia). Entrega la tabla completa y un gráfico de barras por serie. Indica el desfase con mayor |r| y cuánto mejora respecto al desfase 0. Se calculan 2L + 1 correlaciones: el máximo es optimista, así que preséntalo como exploratorio y no como prueba de que una serie anticipa a otra.

E. AGRUPACIÓN (opcional, solo si puedes ejecutar código; si no, omítela). Agrupa los territorios con k-medias sobre las TACC de cada fase, estandarizadas (media 0, desviación 1), con k entre 2 y 5 elegido por el coeficiente de silueta y una semilla fija. Entrega la tabla territorio–grupo, el tamaño y el centro de cada grupo y el código. Avisa de que estos resultados NO son fórmulas del libro.

SALIDA. Hazlo todo en una sola respuesta, con el texto en 700 palabras como máximo, en este orden:

1. PLAN. En 100 palabras como máximo: confirma los parámetros y señala lo que no se pueda hacer o no esté claro.

2. HOJAS. Crea las hojas A, B, C y D (y la E si procede) y una hoja «Hallazgos».

3. COMPROBACIÓN. Elige una variación interanual, una correlación y una TACC; recalcúlalas por otro camino (por ejemplo, la correlación con PEARSON o con covarianza y desviaciones típicas) y escribe el resultado («coincide» o «no coincidía, corregido»). Indica el número de observaciones de cada análisis.

4. HALLAZGOS. En la hoja «Hallazgos» y en la respuesta, hasta 5 fichas ordenadas de más a menos robustas, con estas columnas: Hallazgo (una frase prudente), Dato (cifras con territorio y periodo), Cálculo (hoja y celdas), Método y por qué (máximo 40 palabras), Límites, Confianza (robusta, frágil o no concluyente). Incluye también las relaciones que NO se sostienen: son hallazgos.

5. PASOS PARA REPETIRLO. En 120 palabras como máximo: las funciones que has usado en cada análisis.

REGLAS
- NADA SE COPIA NI SE PEGA. Las hojas existentes no se modifican. Todo valor que venga de la hoja de datos cruzados, y todo cálculo, debe ser una FÓRMULA que lea de ella (la excepción es la agrupación, que debe avisarse). Nunca escribas resultados ya calculados.
- Usa solo fórmulas que funcionen igual en Excel y en LibreOffice (por ejemplo SUMAR.SI.CONJUNTO o SUMIFS, PROMEDIO.SI.CONJUNTO o AVERAGEIFS, INDICE, COINCIDIR, CORREL, PEARSON, MEDIANA, MIN, MAX, K.ESIMO.MENOR, RAIZ, ATANH, TANH). No uses FILTRAR, ORDENAR, UNICOS, LET ni otras funciones de matriz dinámica.
- Si generas el fichero con código, escribe los nombres de las funciones en inglés (SUMIFS, INDEX, MATCH, CORREL…): es lo único que admite el formato del fichero.
- Cuando el criterio de un filtro sea «celda vacía», escríbelo como texto vacío (""). Nunca apuntes el criterio a una celda en blanco.
- Un vacío y un cero son cosas distintas. No imputes datos que faltan: un cálculo que dependa de un dato vacío queda vacío.
- No correlaciones niveles: solo variaciones. Una correlación entre dos series con tendencia puede ser casual.
- Los subperiodos, el umbral, el desfase máximo y las fases están fijados de antemano. Si quieres proponer otra división, preséntala aparte como prueba de sensibilidad y dilo.
- Cada afirmación lleva su cifra y la celda de donde sale. No uses «significativo» sin intervalo de confianza. No uses «causa», «provoca» ni «explica»: usa «se asocia con», «acompaña a» o «precede en el tiempo a». No hagas previsiones ni extrapolaciones.
- Distingue la tendencia de una serie (cómo cambia) de la relación entre dos series (cómo se mueven juntas).
- Cuenta solo lo que consta en el libro. Si algo no consta (unidad, base de un índice, fuente), escribe «no consta»; no escribas «euros» ni «porcentaje» si no se dice. Si afirmas algo por conocimiento general, márcalo con (CG).

