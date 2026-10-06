
INSTRUCCIONES. Te adjunto un libro de hoja de cálculo con tres hojas. Cada hoja contiene una tabla original de datos públicos. Quiero CRUZAR esas tablas: normalizar sus campos para que se puedan unir correctamente y crear, en una hoja nueva llamada «Cruce», los datos ya cruzados. No analices los datos ni saques conclusiones: solo prepara el cruce.

REGLA FUNDAMENTAL: NADA SE COPIA NI SE PEGA
- Las hojas originales no se modifican: no cambies ni borres ninguna de sus columnas, filas ni nombres. Si necesitas columnas de ayuda, añádelas a la derecha de la tabla, con el encabezado que empiece por «AUX_», y que sean fórmulas.
- En la hoja «Cruce», cada valor que venga de una hoja original debe ser una FÓRMULA que lea de esa hoja original. No copies ni pegues valores ni escribas resultados como números fijos.
- Si para que el cruce sea correcto hace falta un cálculo o una estimación (sumar meses para obtener trimestres, convertir un mes en su trimestre, quitar el código del nombre de un territorio), hazlo con funciones en el propio libro que lean de las hojas originales. Nunca escribas el resultado ya calculado.
- Lo único que puede ir como texto fijo son las claves: la lista de territorios y de trimestres de la hoja «Cruce» y la tabla de equivalencias de nombres. Todo lo demás, fórmulas.
- El objetivo es que yo pueda hacer clic en cualquier celda del cruce y ver de qué hoja y de qué filas sale su valor.

CONOCIMIENTO DEL LIBRO

HOJA «ipv_precio_vivienda_ccaa_trimes»
- Qué es: índice de precios de la vivienda y tres tasas de variación, por territorio y trimestre.
- Formato largo, con cabecera en la fila 1. Periodo: columna E · trimestral · formato 2026T2 (de 2007T1 a 2026T2, 78 trimestres)
- Territorio: columna B, con el código delante (por ejemplo, 01 Andalucía) · el total nacional es la celda VACÍA de la columna B (la columna A vale «Nacional» en todas las filas y no sirve para filtrar)
- Valor: columna F · unidad: no consta
- Filtros que hay que aplicar: columna C = General; columna D = Índice (la columna D mezcla el índice con tres variaciones)

HOJA «hipotecas_ccaa_mensual_t76316»
- Qué es: número e importe de hipotecas, por territorio, naturaleza de la finca y mes.
- Formato largo, con cabecera en la fila 1. Periodo: columna D · mensual · formato 2026M07 (de 2003M01 a 2026M07)
- Territorio: columna A, con el código delante (por ejemplo, 01 Andalucía) · el total nacional es el texto «Total Nacional» en esa misma columna
- Valor: columna E · unidad: no consta
- Filtros que hay que aplicar: columna B = Viviendas; columna C = Número de hipotecas (la columna C mezcla número e importe, que son medidas distintas)

HOJA «compraventas_viviendas_ccaa_pro»
- Qué es: cantidad de viviendas compradas y vendidas, por territorio, régimen y mes.
- Formato largo, con cabecera en la fila 1. Periodo: columna E · mensual · formato 2026M07 (de 2007M01 a 2026M07)
- Territorio: columna B (comunidad, con el código delante) y columna C (provincia). Una fila de total nacional tiene B y C vacías; una fila de comunidad tiene B rellena y C vacía; una fila de provincia tiene las dos rellenas. La columna A vale «Total Nacional» en todas las filas y no sirve para filtrar.
- Valor: columna F · unidad: no consta
- Filtros que hay que aplicar: columna C vacía (para no mezclar provincias con comunidades); columna D = Viviendas: Total (las demás categorías de la columna D se solapan con ella)

DISEÑO DEL CRUCE
- Hoja «Cruce» en formato largo: una fila por territorio y trimestre, con estas columnas: Territorio, Trimestre, Índice de precios (General) (de la hoja del IPV), Hipotecas sobre viviendas, número (de la hoja de hipotecas, suma de los tres meses del trimestre), Compraventas de viviendas (total) (de la hoja de compraventas, suma de los tres meses del trimestre). El encabezado de cada columna debe decir qué categoría y qué medida contiene.
- Territorios: el total nacional y las 19 comunidades y ciudades autónomas (20 en total). Clave normalizada: el nombre sin el código numérico inicial (por ejemplo, «Andalucía»); el total nacional se llamará «Total nacional», aunque en cada hoja se identifique de forma distinta.
- Hoja «Equivalencias»: una fila por territorio y una columna por hoja original, con el nombre exacto de ese territorio en cada una (para el total nacional, cómo se identifica en cada una; si es una celda vacía, escribe «(celda vacía)»). Las fórmulas del cruce usan esta tabla para encontrar cada territorio en cada hoja.
- Hoja «Parámetros»: una fila por serie del cruce, con las columnas: Serie, Hoja de origen, Columna del valor, Filtros aplicados (cada filtro en su propia celda: la columna y el valor, por ejemplo «General» o «Número de hipotecas»), Unidad (la que conste, o «no consta»), Frecuencia original y Cómo se agrega al trimestre. Las fórmulas de la hoja «Cruce» deben LEER los valores de los filtros de esta hoja en lugar de escribirlos dentro de la fórmula, de modo que cambiar un filtro en «Parámetros» (por ejemplo, de «General» a «Vivienda nueva») cambie el cruce, y que se vea qué campos se han usado.
- Clave de periodo normalizada: el trimestre en el formato del IPV (2026T2). Los meses de las hojas de hipotecas y compraventas se convierten a su trimestre (enero a marzo = T1, abril a junio = T2, julio a septiembre = T3, octubre a diciembre = T4).
- Periodo común: de 2007T1 a 2026T2. No se incluye 2026T3 porque solo hay un mes (2026M07) y el trimestre estaría incompleto.
- Tamaño esperado de la hoja «Cruce»: 1.560 filas (20 territorios × 78 trimestres), sin contar la cabecera.

TAREAS. Hazlo todo en una sola respuesta, en este orden:

1. PLAN. En 120 palabras como máximo: cómo vas a normalizar el territorio y el periodo en cada hoja, qué filtros aplicas y qué cálculos harás. Señala lo que no esté claro.

2. NORMALIZACIÓN. Crea las hojas «Equivalencias» y «Parámetros» y añade las columnas de ayuda («AUX_…») con fórmulas en las hojas originales que las necesiten: la clave de territorio normalizada y, en las hojas de hipotecas y compraventas, el trimestre.

3. HOJA «CRUCE». Créala con fórmulas que lean de las hojas originales, según el diseño indicado, leyendo los filtros de la hoja «Parámetros». Si no hay datos para una combinación de territorio y trimestre, la celda debe quedar vacía, no en 0. Un trimestre de hipotecas o de compraventas solo se calcula si están sus tres meses; si falta alguno, deja la celda vacía.

4. COMPROBACIÓN. Elige tres combinaciones de territorio y trimestre (una de ellas, Andalucía en 2026T2, y otra, el total nacional en 2026T2, para comprobar las tres formas de identificarlo), comprueba a mano en las hojas originales que los valores del cruce coinciden, comprueba que el número de filas es el esperado y escribe el resultado («coincide» o «no coincidía, corregido»).

5. NOTAS. En una hoja «Notas» del libro (no más de 150 palabras): filtros aplicados, cómo has tratado los totales, los vacíos y los ceros, y los límites del cruce.

ENTREGA. Si puedes modificar el libro (por ejemplo, Copilot en Excel), hazlo directamente en él. Si no puedes, entrégame el libro completo modificado para descargarlo; si tampoco puedes entregar el fichero, dilo claramente.

REGLAS
- Usa solo fórmulas que funcionen igual en Excel y en LibreOffice: por ejemplo SUMAR.SI.CONJUNTO o SUMIFS, CONTAR.SI.CONJUNTO o COUNTIFS, INDICE, COINCIDIR, IZQUIERDA, EXTRAE. No uses FILTRAR, ORDENAR, UNICOS, LET ni otras funciones de matriz dinámica.
- Si generas el fichero con código, escribe los nombres de las funciones en inglés (SUMIFS, COUNTIFS, INDEX, MATCH…): es lo único que admite el formato del fichero, y el programa las mostrará en el idioma del usuario.
- Cuando el criterio de un filtro sea «celda vacía», escríbelo en la fórmula como texto vacío (""). Nunca apuntes el criterio a una celda en blanco: Excel la interpreta como 0 y no encuentra nada. Por eso, en «Equivalencias», donde un total se identifique por una celda vacía escribe el texto «(celda vacía)» y haz que la fórmula lo traduzca a "".
- No mezcles medidas distintas en una misma columna del cruce.
- Un cero verdadero y la falta de dato son cosas distintas: no conviertas un vacío en 0.
- Cuenta solo lo que consta en las hojas. Si algo no consta (unidad, fuente), escribe «no consta» y no lo inventes. Si afirmas algo por conocimiento general, márcalo con (CG).
- No hagas análisis ni conclusiones sobre los datos.

