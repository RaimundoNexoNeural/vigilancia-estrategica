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
