# Transacciones de suelo urbano

| | |
|---|---|
| **Qué mide** | Transacciones de suelo urbano. Conjunto publicado en el catálogo nacional de datos abiertos. |
| **Quién lo publica** | datos.comunidad.madrid (vía datos.gob.es) |
| **Operación estadística** | Catálogo datos.gob.es — búsqueda «suelo urbano» |
| **Periodicidad** | La que fije el organismo |
| **Periodo que cubre este fichero** | la que indique el organismo en el propio fichero |
| **Ámbito territorial** | el que publique el organismo |
| **Filas** | 198 |
| **Descargado** | 22/09/2026 a las 20:13 |

## De dónde sale

```
https://datos.comunidad.madrid/dataset/2a1d060e-06f0-4661-bcbc-ff9f654e4f0e/resource/86123e17-a301-4131-9b2e-24f75c32cd90/download/transacciones-de-suelo-urbano.csv
```

Esta tabla no está escrita a mano en ningún sitio: el script pregunta al
organismo qué publica sobre vivienda y la encuentra sola. Si mañana aparece
otra, entrará igual.

## Columnas del CSV

Este CSV se guarda **tal cual lo publica el organismo**, sin reordenar ni traducir, porque cada conjunto trae su propio esquema. Sus columnas son:

- `Año`
- `Concepto`
- `Tipo territorio`
- `Código territorio`
- `Territorio`
- `Valor`
- `Unidad`
- `Estado dato`

## Cómo leerlo

Un **índice** no son euros: es una referencia comparada con un año base. Un
índice de 111 con base 2015 = 100 significa que el precio es un 11 % superior
al de 2015. Para comparar territorios se usan las variaciones, no los niveles.

Los datos están filtrados a **el que publique el organismo**. La fuente publica el resto
de territorios en la misma tabla.
