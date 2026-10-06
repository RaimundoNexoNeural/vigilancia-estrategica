LECTURA: fichero leído entero: 84.600 filas de datos (84.601 con la cabecera) y 6 columnas, en una hoja llamada «in».

FICHA: compraventas_viviendas_ccaa_provincias_mensual_t6150.xlsx

| Campo | Resumen |
|---|---|
| Qué es | Series mensuales de una cantidad de viviendas por territorio y por régimen y estado de la vivienda. |
| Cómo está organizado | Formato largo: cada fila es un valor de un territorio, un régimen y estado, y un mes. 84.600 filas × 6 columnas. |
| Cobertura | 2007M01–2026M07 (235 meses) · mensual · total nacional, 19 comunidades y 52 provincias. |
| Unidad | no consta |
| ⚠️ Puntos críticos | 1) Tres niveles territoriales en las mismas columnas: 1.175 filas de total nacional (comunidad vacía), 22.325 de comunidad (provincia vacía) y 61.100 de provincia: no sumarlos entre sí. 2) «Régimen y estado» tiene 5 valores solapados (total, nueva, usada, libre, protegida). 3) 117 valores iguales a 0, sin saber si son ceros reales o falta de dato. 4) «Total Nacional» vale lo mismo en todas las filas: no sirve para filtrar. |
| Lo que no consta | La unidad; la fuente; qué se cuenta exactamente (compraventas, inscripciones u otra cosa). |

COLUMNAS

| Columna | Tipo | Ejemplo | Qué significa |
|---|---|---|---|
| Total Nacional | texto | Total Nacional | Constante en todas las filas |
| Comunidades y Ciudades Autónomas | texto | 01 Andalucía | Comunidad; vacío = total nacional |
| Provincias | texto | 04 Almería | Provincia; vacío = total de comunidad o nacional |
| Régimen y estado | texto | Viviendas: Total | Corte de la vivienda (5 valores) |
| Periodo | texto | 2026M07 | Mes |
| Total | número | 12.239 | Cantidad de viviendas |
