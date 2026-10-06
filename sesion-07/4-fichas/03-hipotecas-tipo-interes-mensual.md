LECTURA: fichero leído entero: 1.266 filas de datos (1.267 con la cabecera) y 4 columnas, en una hoja llamada «in».

FICHA: hipotecas_tipo_interes_nacional_mensual_t76315.xlsx

| Campo | Resumen |
|---|---|
| Qué es | Series mensuales de un valor por tipo de interés (total, fijo, variable) y por naturaleza de la finca. |
| Cómo está organizado | Formato largo: cada fila es un valor de un tipo de interés, una naturaleza de finca y un mes. 1.266 filas × 4 columnas. |
| Cobertura | 2009M01–2026M07 (211 meses) · mensual · sin columna de territorio: una sola serie para todo el fichero. |
| Unidad | no consta (los valores van de 1,75 a 6,79) |
| ⚠️ Puntos críticos | 1) No hay territorio: no se puede cruzar por comunidad, solo por fecha. 2) «Tipo de interés» incluye «Total» además de «Fijo» y «Variable»: es otro corte, no sumarlo con ellos. 3) «Naturaleza de la finca» incluye «Total fincas» y «Viviendas»: elegir una. 4) Sin celdas vacías ni símbolos de texto. |
| Lo que no consta | La unidad (porcentaje u otra); el territorio al que se refiere; la fuente. |

COLUMNAS

| Columna | Tipo | Ejemplo | Qué significa |
|---|---|---|---|
| Tipo de interés | texto | Total | Total, fijo o variable |
| Naturaleza de la finca | texto | Total fincas | Total fincas o viviendas |
| Periodo | texto | 2026M07 | Mes |
| Total | número | 3,31 | Valor de la medida |
