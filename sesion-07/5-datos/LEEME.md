# Datos de la sesión 7

Datos públicos, descargados el 5 de octubre de 2026 y guardados en hoja de cálculo (`.xlsx`). Cada fichero tiene su ficha en `4-fichas`.

## Ficheros

| Fichero | Fuente | Periodicidad | Rango | Territorio |
|---|---|---|---|---|
| `ine/ipv_precio_vivienda_ccaa_trimestral_t80270.xlsx` | INE, Índice de Precios de Vivienda (tabla 80270) | trimestral | 2007T1–2026T2 | 19 comunidades y ciudades autónomas, y nacional |
| `ine/hipotecas_ccaa_mensual_t76316.xlsx` | INE, Estadística de Hipotecas (tabla 76316) | mensual | 2003M01–2026M07 | 19 y nacional |
| `ine/hipotecas_tipo_interes_nacional_mensual_t76315.xlsx` | INE, Estadística de Hipotecas (tabla 76315) | mensual | 2009M01–2026M07 | solo nacional |
| `ine/compraventas_viviendas_ccaa_provincias_mensual_t6150.xlsx` | INE, Transmisiones de Derechos de la Propiedad (tabla 6150) | mensual | 2007M01–2026M07 | comunidades y 52 provincias |
| `ine/alquiler_ipva_ccaa_anual_t59056.xlsx` | INE, Índice de Precios de Vivienda en Alquiler (tabla 59056) | anual | 2011–2024 | comunidades (faltan dos) |
| `ministerio/suelo_urbano_precio_m2_…_36400500.xlsx` | Ministerio de Transportes y Movilidad Sostenible, Boletín Estadístico | trimestral | 2004–2026T2 | comunidades y provincias |
| `ministerio/valor_tasado_vivienda_libre_…_35101000.xlsx` | Ministerio (ídem) | trimestral | 1995–2026T2 | comunidades y provincias (8 hojas) |
| `ministerio/viviendas_libres_iniciadas_…` y `…terminadas_…` (mensual y anual) | Ministerio (ídem) | mensual y anual | 2008–2026M03 y 1991–2025 | comunidades y provincias |

Si necesitas volver a descargarlos: `https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/<tabla>.csv` (INE, CSV con punto y coma) y `https://apps.fomento.gob.es/BoletinOnline2/sedal/<código>.XLS` (Ministerio, XLS; el código es el número final del nombre del fichero).

## Libros de cruce (`libros-de-cruce`)

- `libro-de-partida-ipv-hipotecas-compraventas.xlsx`: tres hojas con los datos originales del índice de precios, las hipotecas y las compraventas, sin ningún cambio. Es el punto de partida del paso 4.
- `ejemplo-cruce-hecho-con-copilot.xlsx`: el mismo libro con el cruce ya hecho por Copilot en Excel (hojas de equivalencias, «Cruce» y «Notas», y columnas de ayuda «AUX_…»), con una versión anterior del mensaje del paso 4. Se verificó celda a celda contra los ficheros originales. Tiene unas 389.000 fórmulas: en Excel se abre enseguida; en LibreOffice, si tiene que recalcularlas, tarda varios minutos.

## Avisos

- El índice de precios es un **índice**, no euros, y no sirve para comparar niveles entre comunidades. El importe de las hipotecas parece estar en miles de euros (el fichero no lo dice; se deduce al dividir por el número de hipotecas).
- Los ficheros del Ministerio tienen filas de título y los periodos en columnas: no son una tabla limpia.
- El alquiler tiene 54 celdas con «..» como texto (sin dato).
