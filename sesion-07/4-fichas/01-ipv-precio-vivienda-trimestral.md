LECTURA: fichero leído entero: 18.720 filas de datos (18.721 con la cabecera) y 6 columnas, en una hoja llamada «in».

FICHA: ipv_precio_vivienda_ccaa_trimestral_t80270.xlsx

| Campo | Resumen |
|---|---|
| Qué es | Series trimestrales de un índice y de tres tasas de variación, para vivienda general, nueva y de segunda mano, por territorio. |
| Cómo está organizado | Formato largo: cada fila es un valor de un territorio, un tipo de vivienda, una medida y un trimestre. 18.720 filas × 6 columnas. |
| Cobertura | 2007T1–2026T2 (78 trimestres) · trimestral · total nacional y 19 comunidades y ciudades autónomas (nombre con código, p. ej. «01 Andalucía»). |
| Unidad | no consta |
| ⚠️ Puntos críticos | 1) La columna «Total Nacional» vale «Nacional» en las 18.720 filas: no sirve para filtrar; el total nacional son las 936 filas con el territorio vacío. 2) «Índices y tasas» mezcla el índice y tres variaciones: hay que elegir una antes de graficar. 3) 1.248 celdas vacías en el valor: Ceuta y Melilla solo tienen datos en «General» (624 por ciudad). 4) Sin símbolos de texto en el valor. |
| Lo que no consta | La fuente; la base del índice; si las variaciones son porcentajes. |

COLUMNAS

| Columna | Tipo | Ejemplo | Qué significa |
|---|---|---|---|
| Total Nacional | texto | Nacional | Constante en todas las filas |
| Comunidades y Ciudades Autónomas | texto | 01 Andalucía | Territorio; vacío = total nacional |
| General, vivienda nueva y de segunda mano | texto | General | Tipo de vivienda (3 valores) |
| Índices y tasas | texto | Índice | Medida (índice y 3 variaciones) |
| Periodo | texto | 2026T2 | Trimestre |
| Total | número | 111,095 | Valor de la medida |
