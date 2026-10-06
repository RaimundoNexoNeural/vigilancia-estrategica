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

---

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

---

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

---

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

---

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

---

LECTURA: fichero leído entero: una hoja llamada «Tabla 4» con 62 filas de territorio y 92 columnas de datos (rango físico de 89 × 168, con celdas vacías); no es una tabla limpia.

FICHA: suelo_urbano_precio_m2_ccaa_provincias_trimestral_36400500.xlsx

| Campo | Resumen |
|---|---|
| Qué es | Precio medio del metro cuadrado de suelo urbano por comunidad autónoma y provincia (título de la hoja). |
| Cómo está organizado | Formato ancho: una fila por territorio y una columna por trimestre. 62 filas × 92 columnas de datos, bajo 13 filas de título y cabecera; territorios en la columna B. |
| Cobertura | 2004T1–2026T2 (90 trimestres) más 2 columnas de variación (trimestral e interanual) · trimestral · total nacional, comunidades, provincias y «Ceuta y Melilla» juntas. |
| Unidad | euros/m2 (consta en el fichero) |
| ⚠️ Puntos críticos | 1) Cabecera en dos niveles (año en una fila, trimestre «1º»–«4º» en otra): hay que reconstruir el periodo. 2) 76 celdas con símbolos en lugar de número: 59 «n.s.» y 17 «.». 3) Nada indica si una fila es comunidad o provincia: solo el orden. 4) Ceuta y Melilla vienen en una sola fila. |
| Lo que no consta | Qué significan «n.s.» y «.»; la fuente; cómo se calcula el precio medio. |

COLUMNAS

| Columna | Tipo | Ejemplo | Qué significa |
|---|---|---|---|
| A | vacía | — | Sin datos |
| B (territorio) | texto | Andalucía | Nombre; total, comunidad o provincia |
| 90 columnas de trimestres | número y texto | 174,75 | Euros/m2 de un trimestre |
| 2 columnas finales | número | — | Variación trimestral e interanual |

---

LECTURA: fichero leído entero: 8 hojas con la misma estructura, 64 filas de territorio por hoja; no es una tabla limpia.

FICHA: valor_tasado_vivienda_libre_ccaa_trimestral_35101000.xlsx

| Campo | Resumen |
|---|---|
| Qué es | Valor tasado medio de vivienda libre por comunidad y provincia (título de las hojas). |
| Cómo está organizado | Formato ancho: una fila por territorio y una columna por trimestre, en 8 hojas por tramos de años (1995–1998 … 2023–2026). 64 filas × 16 columnas de datos por hoja, bajo filas de título; territorios en la columna B. |
| Cobertura | 1995T1–2026T2 (126 trimestres) · trimestral · total nacional, comunidades, provincias y Ceuta y Melilla (juntas y por separado). Solo la última hoja añade 2 columnas de variación. |
| Unidad | euros / m2 (consta en el fichero) |
| ⚠️ Puntos críticos | 1) Hay que unir 8 hojas; la cabecera es de dos niveles (año y trimestre «1º»–«4º»). 2) 108 celdas vacías (Ceuta y Melilla en los primeros años) y 17 celdas con «n.r» en la hoja 2011–2014. 3) Nada indica si una fila es comunidad o provincia: solo el orden. 4) Los nombres de territorio no llevan código numérico y alguno va sin acento (p. ej. «Araba/Alava»). |
| Lo que no consta | La fuente; si es un precio de venta o una tasación; cómo se calcula la media. |

COLUMNAS

| Columna | Tipo | Ejemplo | Qué significa |
|---|---|---|---|
| A | vacía | — | Sin datos |
| B (territorio) | texto | Andalucía | Nombre; total, comunidad o provincia |
| 16 columnas de trimestres por hoja | número | 513,4 | Euros/m2 de un trimestre |
| 2 columnas finales (solo última hoja) | número | 2,9 | Variación trimestral y anual |

---

LECTURA: fichero leído entero: una hoja llamada «Tabla 3.1» con 63 filas de territorio y 219 columnas de datos; no es una tabla limpia.

FICHA: viviendas_libres_iniciadas_mensual_32100500.xlsx

| Campo | Resumen |
|---|---|
| Qué es | Número de viviendas libres iniciadas, series mensuales, por territorio (título de la hoja). |
| Cómo está organizado | Formato ancho: una fila por territorio y una columna por mes. 63 filas de datos × 219 columnas de datos, bajo filas de título y cabecera; territorios en la columna B. |
| Cobertura | 2008M01–2026M03 (219 meses) · mensual · total nacional, comunidades y provincias. |
| Unidad | vivienda (consta en el fichero) |
| ⚠️ Puntos críticos | 1) Cabecera en dos niveles (año cada 12 columnas y mes abreviado, con variantes como «Abr», «Agos.», «Jul. »): hay que reconstruir el periodo. 2) 3 celdas con «ND» (la leyenda dice «No proporciona datos»). 3) Nada indica si una fila es comunidad o provincia: solo el orden. 4) Una nota dice que son datos estimados. |
| Lo que no consta | La fuente; cómo se estiman los datos; por qué terminan en marzo de 2026. |

COLUMNAS

| Columna | Tipo | Ejemplo | Qué significa |
|---|---|---|---|
| A | vacía | — | Sin datos |
| B (territorio) | texto | Andalucía | Nombre; total, comunidad o provincia |
| 219 columnas de meses | número y texto | 5.759 | Viviendas iniciadas en un mes |

---

LECTURA: fichero leído entero: una hoja llamada «Tabla 3.2» con 63 filas de territorio y 219 columnas de datos; no es una tabla limpia.

FICHA: viviendas_libres_terminadas_mensual_32101000.xlsx

| Campo | Resumen |
|---|---|
| Qué es | Número de viviendas libres terminadas, series mensuales, por territorio (título de la hoja). |
| Cómo está organizado | Formato ancho: una fila por territorio y una columna por mes. 63 filas de datos × 219 columnas de datos, bajo filas de título y cabecera; territorios en la columna B. |
| Cobertura | 2008M01–2026M03 (219 meses) · mensual · total nacional, comunidades y provincias. |
| Unidad | vivienda (consta en el fichero) |
| ⚠️ Puntos críticos | 1) Cabecera en dos niveles (año cada 12 columnas y mes abreviado, con variantes como «Agos.» y «Jul. »): hay que reconstruir el periodo. 2) Nada indica si una fila es comunidad o provincia: solo el orden. 3) El nombre «Extremadura (1)» lleva una llamada a nota que el fichero no explica, y «Comunitat Valenciana» no se escribe igual que en el fichero anual de terminadas («Comunidad Valenciana»). 4) Una nota dice que son datos estimados. |
| Lo que no consta | La fuente; cómo se estiman los datos; qué significa «(1)». |

COLUMNAS

| Columna | Tipo | Ejemplo | Qué significa |
|---|---|---|---|
| A | vacía | — | Sin datos |
| B (territorio) | texto | Andalucía | Nombre; total, comunidad o provincia |
| 219 columnas de meses | número | 9.940 | Viviendas terminadas en un mes |

---

LECTURA: fichero leído entero: una hoja llamada «Tabla 3.1.» con 63 filas de territorio y 35 columnas de datos; no es una tabla limpia.

FICHA: viviendas_libres_iniciadas_anual_32200500.xlsx

| Campo | Resumen |
|---|---|
| Qué es | Número de viviendas libres iniciadas, series anuales, por territorio (título de la hoja). |
| Cómo está organizado | Formato ancho: una fila por territorio y una columna por año. 63 filas de datos × 35 columnas de datos, bajo filas de título y cabecera; territorios en la columna B. |
| Cobertura | 1991–2025 (35 años) · anual · total nacional, comunidades y provincias. |
| Unidad | vivienda (consta en el fichero) |
| ⚠️ Puntos críticos | 1) Es la versión anual del fichero mensual de iniciadas: mismos territorios, otra frecuencia; no mezclarlas. 2) Nada indica si una fila es comunidad o provincia: solo el orden. 3) Algunos nombres llevan espacios sobrantes al final (p. ej. «Almería           »). 4) Una nota dice que son datos estimados. Sin celdas vacías ni símbolos. |
| Lo que no consta | La fuente; cómo se estiman los datos; si el año es natural. |

COLUMNAS

| Columna | Tipo | Ejemplo | Qué significa |
|---|---|---|---|
| A | vacía | — | Sin datos |
| B (territorio) | texto | Andalucía | Nombre; total, comunidad o provincia |
| 35 columnas de años | número | 28.729 | Viviendas iniciadas en un año |

---

LECTURA: fichero leído entero: una hoja llamada «Tabla 3.2.» con 63 filas de territorio y 35 columnas de datos; no es una tabla limpia.

FICHA: viviendas_libres_terminadas_anual_32201000.xlsx

| Campo | Resumen |
|---|---|
| Qué es | Número de viviendas libres terminadas, series anuales, por territorio (título de la hoja). |
| Cómo está organizado | Formato ancho: una fila por territorio y una columna por año. 63 filas de datos × 35 columnas de datos, bajo filas de título y cabecera; territorios en la columna B. |
| Cobertura | 1991–2025 (35 años) · anual · total nacional, comunidades y provincias. |
| Unidad | vivienda (consta en el fichero) |
| ⚠️ Puntos críticos | 1) Es la versión anual del fichero mensual de terminadas: mismos territorios (dos nombres se escriben distinto, como «Comunidad Valenciana»), otra frecuencia; no mezclarlas. 2) Nada indica si una fila es comunidad o provincia: solo el orden. 3) Algunos nombres llevan espacios sobrantes al final (p. ej. «Almería           »). 4) Una nota dice que son datos estimados. Sin celdas vacías ni símbolos. |
| Lo que no consta | La fuente; cómo se estiman los datos; si el año es natural. |

COLUMNAS

| Columna | Tipo | Ejemplo | Qué significa |
|---|---|---|---|
| A | vacía | — | Sin datos |
| B (territorio) | texto | Andalucía | Nombre; total, comunidad o provincia |
| 35 columnas de años | número | 45.099 | Viviendas terminadas en un año |
