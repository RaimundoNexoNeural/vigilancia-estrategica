# Material de la sesión — Vigilancia Estratégica Aumentada con IA

Curso para la Agencia de Vivienda y Rehabilitación de Andalucía, coordinado por el
Instituto de Estudios Cajasol.

## Qué hay aquí

- **[Abrir el visor del corpus](index.html)** — la tabla de noticias, con buscador,
  filtros, selector de columnas y lectura en pantalla completa.
- `corpus/` — las noticias en `noticias/`, su índice en `indice.csv` (con la
  clasificación y la selección hechas en la sesión, si ya se han fundido), y las
  series de datos abiertos en `datos/`, cada una con su ficha.
- `corpus/seleccion.md` — el informe de la selección hecha en clase: qué se eligió,
  con qué criterio y por qué. Si aún no se ha seleccionado nada, no está.
- `prompts/` — las tres plantillas: extraer, clasificar y seleccionar. Son
  editables y usan periodos relativos, así que sirven igual dentro de dos semanas.
- `script/` — los scripts de descarga en Python, para quien quiera automatizarlo.
- `CLAUDE.md` y `.claude/commands/` — las instrucciones que se ejecutaron en
  pantalla durante la sesión, por si alguien quiere reproducirlas en su equipo.
- `abrir-visor.bat` — levanta el visor en local. Ver **[INSTALL.md](INSTALL.md)**.

## El visor es vuestro, no solo para este corpus

La tabla no está atada a las noticias de la sesión. El botón **«Cargar CSV»** admite
cualquier CSV: el que os devuelva vuestra herramienta de IA al ejecutar el prompt 1,
por ejemplo. Se pega y aparece la tabla completa, con sus filtros y su ordenación,
sin instalar nada y sin que nadie tenga que darle permiso.

Es decir: esto no es un archivo cerrado de la sesión, es una herramienta que podéis
seguir usando cada quincena.

## Sobre las fuentes

Cada elemento del corpus conserva su fuente, su fecha y su URL de origen. Nada está
generado: todo procede de las fuentes citadas y es verificable abriendo su enlace.
