# Hipotecas constituidas sobre el total de fincas por naturaleza de la finca. Resultados nacionales y por comunidades autonomas.

| | |
|---|---|
| **Qué mide** | Hipotecas constituidas sobre el total de fincas por naturaleza de la finca. Resultados nacionales y por comunidades autonomas.. Serie publicada dentro de la operación «Estadística de Hipotecas». |
| **Quién lo publica** | Instituto Nacional de Estadística (INE) |
| **Operación estadística** | HPT — Estadística de Hipotecas |
| **Periodicidad** | Mensual |
| **Periodo que cubre este fichero** | 2025-06-30 a 2026-05-31 |
| **Ámbito territorial** | España y Andalucía |
| **Filas** | 288 |
| **Descargado** | 22/09/2026 a las 20:13 |

## De dónde sale

```
https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/76316?nult=12
```

Esta tabla no está escrita a mano en ningún sitio: el script pregunta al
organismo qué publica sobre vivienda y la encuentra sola. Si mañana aparece
otra, entrará igual.

## Columnas del CSV

- `fecha` — fecha del periodo, en formato AAAA-MM-DD
- `anio`, `mes`, `trimestre` — el mismo periodo, desglosado
- `ambito` — España o Andalucía
- `indicador` — qué se mide exactamente en esa fila
- `valor` — el dato
- `unidad` — la unidad de medida

## Cómo leerlo

Un **índice** no son euros: es una referencia comparada con un año base. Un
índice de 111 con base 2015 = 100 significa que el precio es un 11 % superior
al de 2015. Para comparar territorios se usan las variaciones, no los niveles.

Los datos están filtrados a **España y Andalucía**. La fuente publica el resto
de territorios en la misma tabla.
