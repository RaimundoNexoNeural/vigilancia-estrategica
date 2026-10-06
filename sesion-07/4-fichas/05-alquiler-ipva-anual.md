LECTURA: fichero leído entero: 1.512 filas de datos (1.513 con la cabecera) y 6 columnas, en una hoja llamada «in».

FICHA: alquiler_ipva_ccaa_anual_t59056.xlsx

| Campo | Resumen |
|---|---|
| Qué es | Series anuales de un índice y de una variación anual, por territorio y tipo de edificación. |
| Cómo está organizado | Formato largo: cada fila es un valor de un territorio, un tipo de edificación, una medida y un año. 1.512 filas × 6 columnas. |
| Cobertura | 2011–2024 (14 años) · anual · total nacional y 17 comunidades y ciudades autónomas (faltan las de código 15 y 16; el fichero no las nombra). |
| Unidad | no consta |
| ⚠️ Puntos críticos | 1) 54 celdas con «..» (texto) en lugar de número, todas en «Variación anual» de 2011 (18 territorios × 3 tipos de edificación). 2) «Tipo de dato» mezcla índice y variación anual: elegir una. 3) Solo 14 puntos por serie, y «Periodo» es un número (año), no texto como en otros ficheros. 4) «Total Nacional» vale lo mismo en todas las filas: el total son las 84 filas con comunidad vacía. |
| Lo que no consta | La base del índice; la fuente; qué significa «..». |

COLUMNAS

| Columna | Tipo | Ejemplo | Qué significa |
|---|---|---|---|
| Total Nacional | texto | Total Nacional | Constante en todas las filas |
| Comunidades y Ciudades Autónomas | texto | 01 Andalucía | Territorio; vacío = total nacional |
| Tipo de edificación | texto | Vivienda colectiva | Total, colectiva o unifamiliar |
| Tipo de dato | texto | Índice | Índice o variación anual |
| Periodo | número | 2024 | Año |
| Total | número y texto | 122,92 | Valor; 54 celdas con «..» |
