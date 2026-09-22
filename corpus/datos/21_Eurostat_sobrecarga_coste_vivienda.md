# Tasa de sobrecarga del coste de la vivienda: España y la UE

| | |
|---|---|
| **Qué mide** | Porcentaje de población que dedica más del 40 % de su renta disponible a la vivienda. Es el indicador europeo de esfuerzo residencial. |
| **Quién lo publica** | Eurostat (Oficina Estadística de la Unión Europea) |
| **Operación estadística** | ilc_lvho07a — conjunto de datos de Eurostat |
| **Periodicidad** | Anual |
| **Periodo que cubre este fichero** | 2020 a 2025 |
| **Ámbito territorial** | España y Unión Europea (27) |
| **Filas** | 1836 |
| **Descargado** | 22/09/2026 a las 20:13 |

## De dónde sale

```
https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/ilc_lvho07a?format=JSON&geo=ES&geo=EU27_2020&lastTimePeriod=6
```

Esta tabla no está escrita a mano en ningún sitio: el script pregunta al
organismo qué publica sobre vivienda y la encuentra sola. Si mañana aparece
otra, entrará igual.

## Columnas del CSV

- `periodo` — trimestre en formato AAAA-Qn
- `anio`, `trimestre` — el mismo periodo, desglosado
- `ambito` — España o Unión Europea (27)
- `indicador` / `unidad` — qué mide la fila y en qué unidad
- `valor` — el dato

## Cómo leerlo

Un **índice** no son euros: es una referencia comparada con un año base. Un
índice de 111 con base 2015 = 100 significa que el precio es un 11 % superior
al de 2015. Para comparar territorios se usan las variaciones, no los niveles.

Los datos están filtrados a **España y Unión Europea (27)**. La fuente publica el resto
de territorios en la misma tabla.
