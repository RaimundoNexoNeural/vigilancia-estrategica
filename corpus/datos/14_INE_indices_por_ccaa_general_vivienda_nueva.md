# Índices por CCAA: general, vivienda nueva y de segunda mano. Trimestrales

| | |
|---|---|
| **Qué mide** | Índices por CCAA: general, vivienda nueva y de segunda mano. Trimestrales. Serie publicada dentro de la operación «Índice de Precios de la Vivienda (IPV)». |
| **Quién lo publica** | Instituto Nacional de Estadística (INE) |
| **Operación estadística** | IPV — Índice de Precios de la Vivienda (IPV) |
| **Periodicidad** | Trimestral |
| **Periodo que cubre este fichero** | 2024-06-30 a 2026-03-31 |
| **Ámbito territorial** | España y Andalucía |
| **Filas** | 192 |
| **Descargado** | 22/09/2026 a las 20:13 |

## De dónde sale

```
https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/80270?nult=8
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
