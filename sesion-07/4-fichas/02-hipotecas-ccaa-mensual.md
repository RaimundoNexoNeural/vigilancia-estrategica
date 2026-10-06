LECTURA: fichero leído entero: 67.920 filas de datos (67.921 con la cabecera) y 5 columnas, en una hoja llamada «in».

FICHA: hipotecas_ccaa_mensual_t76316.xlsx

| Campo | Resumen |
|---|---|
| Qué es | Series mensuales del número y del importe de hipotecas, por territorio y por naturaleza de la finca. |
| Cómo está organizado | Formato largo: cada fila es un valor de un territorio, una naturaleza de finca, una medida y un mes. 67.920 filas × 5 columnas. |
| Cobertura | 2003M01–2026M07 (283 meses) · mensual · total nacional y 19 comunidades y ciudades autónomas, todos en la misma columna (el total nacional es el texto «Total Nacional»). |
| Unidad | no consta (ni para el número ni para el importe) |
| ⚠️ Puntos críticos | 1) «Número e importe» mezcla dos medidas con unidades distintas (número de hipotecas e importe): hay que filtrar una. 2) «Naturaleza de la finca» mezcla totales y subcategorías (Total fincas, Total fincas rústicas, Total fincas urbanas, Viviendas, Solares, Otros): no sumarlas. 3) 1.938 valores iguales a 0, sin saber si son ceros reales o falta de dato. 4) Sin celdas vacías ni símbolos de texto. |
| Lo que no consta | La unidad del importe (ni si va en miles); la fuente; si cuenta hipotecas firmadas o inscritas. |

COLUMNAS

| Columna | Tipo | Ejemplo | Qué significa |
|---|---|---|---|
| Comunidades Autonomas | texto | 01 Andalucía | Territorio, con «Total Nacional» incluido |
| Naturaleza de la finca | texto | Viviendas | Tipo de finca (6 valores, solapados) |
| Número e importe | texto | Número de hipotecas | Medida (2 valores) |
| Periodo | texto | 2026M07 | Mes |
| Total | número | 8.136 | Valor de la medida |
