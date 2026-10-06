
INSTRUCCIONES. Te adjunto un libro de hoja de cálculo con varias hojas. Cada hoja contiene una tabla original de datos públicos. Quiero CRUZAR esas tablas: normalizar sus campos para que se puedan unir correctamente y crear, en una hoja nueva llamada «Cruce», los datos ya cruzados. No analices los datos ni saques conclusiones: solo prepara el cruce.

REGLA FUNDAMENTAL: NADA SE COPIA NI SE PEGA
- Las hojas originales no se modifican: no cambies ni borres ninguna de sus columnas ni de sus filas. Si necesitas columnas de ayuda en una hoja larga, añádelas a la derecha de la tabla, con el encabezado que empiece por «AUX_», y que sean fórmulas. En una hoja ancha no toques los datos: pon las ayudas en una hoja nueva.
- En la hoja «Cruce», cada valor que venga de una hoja original debe ser una FÓRMULA que lea de esa hoja original. No copies ni pegues valores ni escribas resultados como números fijos.
- Si para que el cruce sea correcto hace falta un cálculo o una estimación (sumar meses para obtener trimestres, hacer una media, convertir un periodo en otro, quitar un código del nombre de un territorio), hazlo con funciones en el propio libro que lean de las hojas originales. Nunca escribas el resultado ya calculado.
- Lo único que puede ir como texto fijo son las claves: la lista de territorios y de periodos de la hoja «Cruce» y la tabla de equivalencias de nombres. Todo lo demás, fórmulas.
- El objetivo es que yo pueda hacer clic en cualquier celda del cruce y ver de qué hoja y de qué filas sale su valor.

CONOCIMIENTO DEL LIBRO. Estas son las hojas y lo que sé de cada una (si has estudiado antes sus fichas en esta conversación, úsalas):

HOJA 1: [nombre de la hoja]
- Qué es: [una frase]
- Formato: [largo, con cabecera en la fila X; o ancho, con indicación de dónde están los territorios, las cabeceras de periodo y los valores]
- Periodo: [columna o columnas] · frecuencia [mensual, trimestral o anual] · formato del periodo [por ejemplo, 2026M07 o 2026T2]
- Territorio: [columna] · cómo se identifica un total [celda vacía, o un texto como «Total Nacional»] · particularidades de los nombres [códigos, espacios, filas que no se usan]
- Valor: [columna] · unidad [la que conste, o «no consta»] · símbolos que hay que tratar como falta de dato [por ejemplo, «n.s.»]
- Filtros que hay que aplicar (columna = valor): [lista]

HOJA 2: [mismos campos]

HOJA 3: [mismos campos; borra o añade bloques según el número de hojas]

DISEÑO DEL CRUCE
- Formato de la hoja «Cruce»: una fila por [territorio y periodo], con las columnas: [clave de territorio, clave de periodo, y una columna por cada serie cruzada]. El encabezado de cada columna debe decir qué categoría y qué medida contiene.
- Territorios que se incluyen: [lista o «todos»] · periodo común: [desde – hasta] · frecuencia del cruce: [la más baja de las series]
- Qué se hace con cada serie al pasar a la frecuencia del cruce: [suma, media o último valor de cada periodo]
- Hoja «Equivalencias»: una fila por territorio y una columna por hoja original, con el nombre exacto del territorio en cada una (y cómo se identifica el total; si es una celda vacía, escribe «(celda vacía)»). Las fórmulas del cruce usan esta tabla.
- Hoja «Parámetros»: una fila por serie del cruce, con las columnas: Serie, Hoja de origen, Columna del valor, Filtros aplicados (cada filtro en su propia celda: la columna y el valor, por ejemplo «General» o «Número de hipotecas»), Unidad (la que conste, o «no consta»), Frecuencia original y Cómo se agrega al trimestre. Las fórmulas de la hoja «Cruce» deben LEER los valores de los filtros de esta hoja en lugar de escribirlos dentro de la fórmula, de modo que cambiar un filtro en «Parámetros» (por ejemplo, de «General» a «Vivienda nueva») cambie el cruce, y que se vea qué campos se han usado.
- Tamaño esperado de la hoja «Cruce»: [número de filas]

TAREAS. Hazlo todo en una sola respuesta, en este orden:

1. PLAN. En 120 palabras como máximo: cómo vas a normalizar el territorio y el periodo en cada hoja, qué filtros aplicas y qué cálculos harás. Señala lo que no esté claro.

2. NORMALIZACIÓN. Crea las hojas «Equivalencias» y «Parámetros» y añade las columnas de ayuda («AUX_…») con fórmulas en las hojas largas que lo necesiten.

3. HOJA «CRUCE». Créala con fórmulas que lean de las hojas originales, según el diseño indicado, leyendo los filtros de la hoja «Parámetros». Si no hay datos para una combinación de territorio y periodo, o el valor es un símbolo en lugar de un número, la celda debe quedar vacía, no en 0. Si un periodo del cruce se calcula a partir de varios periodos más cortos, calcúlalo solo si están todos; si falta alguno, deja la celda vacía.

4. COMPROBACIÓN. Elige tres combinaciones de territorio y periodo, comprueba a mano en las hojas originales que los valores del cruce coinciden, comprueba que el número de filas es el esperado y escribe el resultado («coincide» o «no coincidía, corregido»).

5. NOTAS. En una hoja «Notas» del libro (no más de 150 palabras): filtros aplicados, cómo has tratado los totales, los vacíos y los ceros, y los límites del cruce.

ENTREGA. Si puedes modificar el libro (por ejemplo, Copilot en Excel), hazlo directamente en él. Si no puedes, entrégame el libro completo modificado para descargarlo; si tampoco puedes entregar el fichero, dilo claramente.

REGLAS
- Usa solo fórmulas que funcionen igual en Excel y en LibreOffice: por ejemplo SUMAR.SI.CONJUNTO o SUMIFS, CONTAR.SI.CONJUNTO o COUNTIFS, INDICE, COINCIDIR, IZQUIERDA, EXTRAE. No uses FILTRAR, ORDENAR, UNICOS, LET ni otras funciones de matriz dinámica.
- Si generas el fichero con código, escribe los nombres de las funciones en inglés (SUMIFS, COUNTIFS, INDEX, MATCH…): es lo único que admite el formato del fichero, y el programa las mostrará en el idioma del usuario.
- Antes de filtrar, mira qué valores distintos tiene cada columna. No uses como filtro una columna que tenga el mismo valor en todas las filas. Un total puede identificarse por una celda vacía en otra columna: léelo en el bloque de cada hoja y no lo supongas.
- Cuando el criterio de un filtro sea «celda vacía», escríbelo en la fórmula como texto vacío (""). Nunca apuntes el criterio a una celda en blanco: Excel la interpreta como 0 y no encuentra nada. Por eso, en «Equivalencias», donde un total se identifique por una celda vacía escribe el texto «(celda vacía)» y haz que la fórmula lo traduzca a "".
- No mezcles medidas distintas en una misma columna del cruce. Si una hoja las mezcla, filtra una y dime cuál.
- Un cero verdadero y la falta de dato son cosas distintas: no conviertas un vacío en 0.
- Cuenta solo lo que consta en las hojas. Si algo no consta (unidad, fuente), escribe «no consta» y no lo inventes. Si afirmas algo por conocimiento general, márcalo con (CG).
- No hagas análisis ni conclusiones sobre los datos.

