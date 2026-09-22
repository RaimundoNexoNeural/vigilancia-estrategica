# Antigüedad de la vivienda según superficie en municipio, distritos y secciones

| | |
|---|---|
| **Qué mide** | Antigüedad de la vivienda según superficie en municipio, distritos y secciones. Conjunto publicado en el catálogo nacional de datos abiertos. |
| **Quién lo publica** | datosabiertos.aytosanlorenzo.es (vía datos.gob.es) |
| **Operación estadística** | Catálogo datos.gob.es — búsqueda «vivienda» |
| **Periodicidad** | La que fije el organismo |
| **Periodo que cubre este fichero** | la que indique el organismo en el propio fichero |
| **Ámbito territorial** | el que publique el organismo |
| **Filas** | 12 |
| **Descargado** | 22/09/2026 a las 20:13 |

## De dónde sale

```
https://datosabiertos.aytosanlorenzo.es/dataset/b22e0c23-ba84-432a-a9b4-2803d7c040ec/resource/6a5b9acc-4e51-4364-93b8-4f6832a160e3/download/antiguedad-de-la-vivienda-segun-superficie-en-municiupio-distritos-y-secciones-2021.csv
```

Esta tabla no está escrita a mano en ningún sitio: el script pregunta al
organismo qué publica sobre vivienda y la encuentra sola. Si mañana aparece
otra, entrará igual.

## Columnas del CSV

Este CSV se guarda **tal cual lo publica el organismo**, sin reordenar ni traducir, porque cada conjunto trae su propio esquema. Sus columnas son:

- `Año`
- `Superficie`
- `Total`
- `Hasta 30 m2`
- `30-45 m2`
- `46-60 m2`
- `61-75 m2`
- `76-90 m2`
- `91-105 m2`
- `106-120 m2`
- `121-150 m2`
- `151-180 m2`
- `Más de 180 m2`
- `No Consta`

## Cómo leerlo

Un **índice** no son euros: es una referencia comparada con un año base. Un
índice de 111 con base 2015 = 100 significa que el precio es un 11 % superior
al de 2015. Para comparar territorios se usan las variaciones, no los niveles.

Los datos están filtrados a **el que publique el organismo**. La fuente publica el resto
de territorios en la misma tabla.
