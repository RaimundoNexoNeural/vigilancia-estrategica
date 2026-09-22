#!/usr/bin/env python3
"""
================================================================================
descargar_datos.py — Datos abiertos sobre vivienda, suelo y construccion
================================================================================

DESCRIPCION
    Reune series de datos abiertos del ambito de AVRA y las deja en CSV plano,
    legible, con una ficha al lado que explica que mide cada una.

    NO lleva ninguna tabla escrita a mano: las descubre preguntando a cada
    proveedor que publica sobre vivienda. Si mañana aparece una tabla nueva,
    entra sola; si desaparece una, el script lo dice en vez de fallar callando.

    Proveedores implementados:
      INE           pregunta que operaciones estadisticas hay, se queda con las
                    del ambito (vivienda, suelo, construccion, hipotecas,
                    alquiler, transmisiones, indicadores urbanos, renta de los
                    hogares, precios de materiales) y de cada una toma las
                    tablas con desglose por comunidad autonoma, comprobando que
                    traen serie de Andalucia.
      Eurostat      conjuntos europeos: precio de vivienda trimestral y anual,
                    sobrecarga del coste de la vivienda, hacinamiento y
                    produccion en la construccion, filtrados a Espana y UE-27.
      datos.gob.es  catalogo nacional de datos abiertos: conjuntos sobre
                    vivienda, suelo, alquiler y rehabilitacion que ofrezcan un
                    CSV de descarga directa. Se guardan tal cual los publica
                    cada organismo, porque cada uno trae su propio esquema.

PARAMETROS
    --fuentes LISTA   Opcional. Acota a los proveedores indicados, separados
                      por comas (p. ej. "INE" o "INE,datos.gob.es"). Si NO se
                      indica, se consultan todos: INE, Eurostat y datos.gob.es.
    --max N           Opcional. Tope de tablas por proveedor. Si NO se indica,
                      se descarga TODO lo que encuentre relacionado con
                      vivienda, suelo y construccion: medido el 22/09/2026, son
                      13 conjuntos en unos 17 segundos. Con --max se acota.
    --hilos N         Opcional, 6 por defecto. Sondeos simultaneos.
    --limpiar         Opcional. Si se indica, vacia datos/ antes de escribir.
                      Si NO se indica, ACUMULA: conserva los conjuntos que
                      hubiera y anade los nuevos, sin sobrescribir.
    --salida RUTA     Opcional. Carpeta de corpus. Por defecto ../corpus.

ENTRADAS
    Internet          API del INE (servicios.ine.es/wstempus) y de Eurostat.
    datos/catalogo.json  Solo para comparar con la ejecucion anterior y avisar
                      de altas y bajas. No condiciona lo que se descarga.

SALIDAS  (dentro de corpus/datos, salvo el indice)
    NN_*.csv          Un CSV plano por conjunto: fechas reales, etiquetas
                      reales, unidad y ambito. Con BOM, para Excel.
    NN_*.md           La ficha de ese conjunto: que mide, quien lo publica,
                      periodo, unidad, ambito y URL exacta de descarga.
    catalogo.json     Que se encontro en esta ejecucion.
    corpus/datos.js   Indice de conjuntos que lee el visor.

DEPENDENCIAS
    Ninguna. Solo biblioteca estandar de Python 3.

EJEMPLOS
    python descargar_datos.py
    python descargar_datos.py --max 8 --limpiar
    python descargar_datos.py --fuentes INE --max 4
================================================================================
"""

import argparse
import csv
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

# --------------------------------------------------------------- configuracion

AGENTE = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
ESPERA = 60

INE = "https://servicios.ine.es/wstempus/js/ES/"
EUROSTAT_API = ("https://ec.europa.eu/eurostat/api/dissemination/statistics/"
                "1.0/data/")

# Lo unico que hay que tocar para ampliar el alcance tematico.
TEMAS = [
    "vivienda", "hipotec", "alquiler", "transmision de derechos",
    "ejecuciones hipotecarias", "construccion", "edificacion", "suelo",
    "materiales y energia",
]
# Quedan fuera a proposito las operaciones que solo publican series
# municipales o por distrito (Indicadores Urbanos, Atlas de renta de los
# hogares): este script trabaja el marco Espana / Andalucia, y sus series no
# traen ninguno de los dos.

# Pistas de desglose territorial en el nombre de la tabla. Se confirma despues
# abriendo la tabla y comprobando que existe serie de Andalucia.
PISTAS_CCAA = ["comunidad", "ccaa", "autonom"]

# Tablas que no son datos de coyuntura.
DESCARTAR = ["ponderacion", "indice de precios al consumo", "rustica"]

# Si el nombre de las tablas no dice si hay desglose territorial, se sondean
# estas tantas de las mas recientes para averiguarlo.
SONDEO_SIN_PISTAS = 6

# Cuantas tablas se llegan a abrir por operacion para comprobar si traen
# Andalucia. Hay operaciones con cientos de tablas (el atlas de renta tiene
# 540) y sondearlas todas no aporta nada.
MAX_SONDEOS_POR_OPERACION = 12

# Cuantos periodos se piden segun la periodicidad que declare el proveedor.
PERIODOS = {"Mensual": 12, "Trimestral": 8, "Semestral": 6, "Anual": 8}
PERIODOS_POR_DEFECTO = 8

# Conjuntos de Eurostat. Anadir uno es anadir una entrada.
CONJUNTOS_EUROSTAT = [
    {
        "codigo": "prc_hpi_q",
        "archivo": "Eurostat_precio_vivienda_trimestral",
        "titulo": "Índice de precios de la vivienda, trimestral: España y la UE",
        "mide": "Índice de precios de la vivienda y su variación, para España y "
                "para el conjunto de la UE-27, en serie trimestral.",
        "periodicidad": "Trimestral",
        "parametros": "geo=ES&geo=EU27_2020&lastTimePeriod=8",
    },
    {
        "codigo": "prc_hpi_a",
        "archivo": "Eurostat_precio_vivienda_anual",
        "titulo": "Índice de precios de la vivienda, anual: España y la UE",
        "mide": "La misma serie de precios de vivienda en medias anuales, que es "
                "la que sirve para comparar años completos.",
        "periodicidad": "Anual",
        "parametros": "geo=ES&geo=EU27_2020&lastTimePeriod=8",
    },
    {
        "codigo": "ilc_lvho07a",
        "archivo": "Eurostat_sobrecarga_coste_vivienda",
        "titulo": "Tasa de sobrecarga del coste de la vivienda: España y la UE",
        "mide": "Porcentaje de población que dedica más del 40 % de su renta "
                "disponible a la vivienda. Es el indicador europeo de "
                "esfuerzo residencial.",
        "periodicidad": "Anual",
        "parametros": "geo=ES&geo=EU27_2020&lastTimePeriod=6",
    },
    {
        "codigo": "ilc_lvho05a",
        "archivo": "Eurostat_hacinamiento",
        "titulo": "Tasa de hacinamiento en la vivienda: España y la UE",
        "mide": "Porcentaje de población que vive en un hogar sin habitaciones "
                "suficientes para su tamaño y composición.",
        "periodicidad": "Anual",
        "parametros": "geo=ES&geo=EU27_2020&lastTimePeriod=6",
    },
    {
        "codigo": "sts_copr_q",
        "archivo": "Eurostat_produccion_construccion",
        "titulo": "Producción en la construcción, trimestral: España y la UE",
        "mide": "Índice de producción del sector de la construcción, que mide "
                "la actividad constructora real.",
        "periodicidad": "Trimestral",
        "parametros": "geo=ES&geo=EU27_2020&lastTimePeriod=8",
    },
]

# ------------------------------------------------------- proveedor datos.gob.es
# Catalogo nacional de datos abiertos. Se piden los conjuntos cuyo titulo case
# con estos terminos y que ofrezcan un CSV de descarga directa.
DATOS_GOB = "https://datos.gob.es/apidata/catalog/dataset/title/{termino}?_pageSize=25&_page=0"
TERMINOS_DATOS_GOB = ["vivienda", "suelo urbano", "alquiler", "rehabilitacion",
                      "vivienda protegida", "urbanismo"]
# El catalogo busca por titulo, asi que "vivienda" trae tambien cosas del
# equipamiento del hogar. Se exige una palabra del ambito y se descartan estas.
EXIGIDOS_DATOS_GOB = ["vivienda", "viviendas", "suelo", "urbanis", "alquiler",
                      "rehabilitac", "edificac", "construcc", "vpo", "urbana"]
DESCARTAR_DATOS_GOB = ["internet", "tic", "television", "telefon", "ordenador",
                       "equipamiento", "hidrante", "movil", "banda ancha",
                       "informatic"]
TOPE_DATOS_GOB = 8
MAX_BYTES_CSV = 6 * 1024 * 1024

MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

# Eurostat solo sirve las etiquetas en ingles, asi que se traducen aqui.
TERRITORIOS = {"ES": "España", "EU27_2020": "Unión Europea (27)"}
INDICADORES = {
    "I15_Q": "Índice de precios de la vivienda",
    "I25_Q": "Índice de precios de la vivienda",
    "RCH_A": "Variación anual del precio de la vivienda",
    "RCH_Q": "Variación trimestral del precio de la vivienda",
}
UNIDADES_EUROSTAT = {
    "I15_Q": "Índice (base 2015 = 100)", "I25_Q": "Índice (base 2025 = 100)",
    "RCH_A": "Porcentaje", "RCH_Q": "Porcentaje",
}

PROVEEDORES = ["INE", "Eurostat", "datos.gob.es"]


# ------------------------------------------------------------------- utilidades

def descargar(url):
    """Descarga una URL y devuelve sus bytes."""
    peticion = urllib.request.Request(url, headers={"User-Agent": AGENTE})
    with urllib.request.urlopen(peticion, timeout=ESPERA) as respuesta:
        return respuesta.read()


def json_de(url):
    """Descarga una URL y la interpreta como JSON."""
    return json.loads(descargar(url))


def sin_acentos(texto):
    """Minusculas y sin tildes, para comparar sin sorpresas."""
    texto = unicodedata.normalize("NFKD", (texto or "").lower())
    return texto.encode("ascii", "ignore").decode()


def nombre_seguro(texto):
    """Convierte un titulo en un nombre de fichero corto y sin acentos."""
    base = re.sub(r"[^a-z0-9]+", "_", sin_acentos(texto)).strip("_")
    return base[:40].rstrip("_") or "conjunto"


def escribir_csv(ruta, cabeceras, filas):
    """Escribe un CSV con BOM, para que Excel respete los acentos."""
    # utf-8-sig: con BOM, para que Excel lo abra con los acentos bien.
    with open(ruta, "w", encoding="utf-8-sig", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=cabeceras)
        escritor.writeheader()
        escritor.writerows(filas)


def escribir_ficha(ruta, datos):
    """Escribe la ficha .md que acompana a cada CSV."""
    texto = f"""# {datos['titulo']}

| | |
|---|---|
| **Qué mide** | {datos['mide']} |
| **Quién lo publica** | {datos['organismo']} |
| **Operación estadística** | {datos['operacion']} |
| **Periodicidad** | {datos['periodicidad']} |
| **Periodo que cubre este fichero** | {datos['cobertura']} |
| **Ámbito territorial** | {datos['ambitos']} |
| **Filas** | {datos['filas']} |
| **Descargado** | {datetime.now():%d/%m/%Y a las %H:%M} |

## De dónde sale

```
{datos['url']}
```

Esta tabla no está escrita a mano en ningún sitio: el script pregunta al
organismo qué publica sobre vivienda y la encuentra sola. Si mañana aparece
otra, entrará igual.

## Columnas del CSV

{datos['columnas']}

## Cómo leerlo

Un **índice** no son euros: es una referencia comparada con un año base. Un
índice de 111 con base 2015 = 100 significa que el precio es un 11 % superior
al de 2015. Para comparar territorios se usan las variaciones, no los niveles.

Los datos están filtrados a **{datos['ambitos']}**. La fuente publica el resto
de territorios en la misma tabla.
"""
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(texto)


# -------------------------------------------------------------- descubrir: INE

def operaciones_de_interes():
    """Operaciones estadisticas del INE que tratan de los temas de TEMAS."""
    operaciones = json_de(INE + "OPERACIONES_DISPONIBLES")
    elegidas = []
    for operacion in operaciones:
        if any(tema in sin_acentos(operacion.get("Nombre", "")) for tema in TEMAS):
            if operacion.get("Codigo"):
                elegidas.append({"codigo": operacion["Codigo"],
                                 "nombre": (operacion.get("Nombre") or "").strip()})
    return elegidas


def ambito_de_la_tabla(tabla):
    """
    Abre la tabla y dice con que ambito sirve, o None si no sirve.

    Devuelve "Andalucia" si trae serie de la comunidad, que es lo preferido;
    "Espana" si no la trae pero si series nacionales, o si la propia tabla se
    declara nacional (los indices de produccion en la construccion o de precios
    de materiales no tienen desglose territorial y aun asi interesan).

    Algunas tablas responden con un mensaje de error en vez de con la lista de
    series, asi que se comprueba la forma antes de mirar dentro.
    """
    try:
        series = json_de(INE + f"DATOS_TABLA/{tabla['Id']}?nult=1")
    except Exception:                                           # noqa: BLE001
        return None
    if not isinstance(series, list) or not series:
        return None
    nombres = [s.get("Nombre") or "" for s in series if isinstance(s, dict)]
    if any("Andaluc" in n for n in nombres):
        return "Andalucía"
    if any(("Nacional" in n or "España" in n) for n in nombres):
        return "España"
    nombre_tabla = sin_acentos(tabla.get("Nombre", ""))
    if "nacional" in nombre_tabla or "espana" in nombre_tabla:
        return "España"
    return None


def descubrir_ine(maximo, hilos):
    """Catalogo de tablas del INE con desglose de Andalucia."""
    periodicidades = {p["Id"]: p.get("Nombre", "")
                      for p in json_de(INE + "PERIODICIDADES")}
    catalogo = []

    for operacion in operaciones_de_interes():
        try:
            tablas = json_de(INE + "TABLAS_OPERACION/" + operacion["codigo"])
        except Exception as error:                              # noqa: BLE001
            print(f"    aviso: {operacion['codigo']} no responde ({error})")
            continue

        utiles = [t for t in tablas
                  if not any(mal in sin_acentos(t.get("Nombre", ""))
                             for mal in DESCARTAR)]
        utiles.sort(key=lambda t: t.get("Ultima_Modificacion") or 0, reverse=True)

        con_pistas = [t for t in utiles
                      if any(p in sin_acentos(t.get("Nombre", ""))
                             for p in PISTAS_CCAA)]
        # Hay operaciones que no anuncian el desglose territorial en el nombre
        # (las de transmisiones de propiedad, por ejemplo). Si el nombre no da
        # pistas, se sondean las mas recientes. Descubrir, no adivinar.
        candidatas = con_pistas if con_pistas else utiles[:SONDEO_SIN_PISTAS]
        candidatas = candidatas[:maximo * 3 if maximo else MAX_SONDEOS_POR_OPERACION]

        with ThreadPoolExecutor(max_workers=hilos) as ejecutor:
            confirmadas = list(ejecutor.map(
                lambda t: (t, ambito_de_la_tabla(t)), candidatas))

        elegidas, vistos = 0, []
        for tabla, ambito in confirmadas:
            if not ambito or (maximo and elegidas >= maximo):
                continue
            # Dos tablas de la misma operacion que empiezan igual suelen ser la
            # misma serie en otra periodicidad: basta con una.
            raiz = sin_acentos(tabla.get("Nombre", ""))[:45]
            if raiz in vistos:
                continue
            vistos.append(raiz)
            catalogo.append({
                "proveedor": "INE",
                "id": tabla["Id"],
                "titulo": (tabla.get("Nombre") or "").strip(),
                "operacion_codigo": operacion["codigo"],
                "operacion": operacion["nombre"],
                "periodicidad": periodicidades.get(tabla.get("FK_Periodicidad"))
                                or "No declarada",
                "ambito": ambito,
                "ultima_modificacion": tabla.get("Ultima_Modificacion"),
            })
            elegidas += 1
        if elegidas:
            print(f"    {elegidas} tabla(s) en {operacion['codigo']} — "
                  f"{operacion['nombre'][:56]}")

    catalogo.sort(key=lambda c: (c["operacion_codigo"], c["id"]))
    return catalogo


def descubrir_eurostat(maximo):
    """Catalogo de conjuntos de Eurostat."""
    conjuntos = CONJUNTOS_EUROSTAT[:maximo] if maximo else CONJUNTOS_EUROSTAT
    catalogo = []
    for conjunto in conjuntos:
        entrada = dict(conjunto)
        entrada.update({"proveedor": "Eurostat", "id": conjunto["codigo"]})
        catalogo.append(entrada)
    if catalogo:
        print(f"    {len(catalogo)} conjunto(s) en Eurostat")
    return catalogo


def descubrir_datos_gob(maximo):
    """
    Catalogo nacional datos.gob.es: conjuntos sobre vivienda y suelo que
    ofrezcan un CSV de descarga directa.

    A diferencia del INE, aqui cada conjunto trae su propio esquema, asi que el
    CSV se guarda tal cual lo publica el organismo y la ficha lo advierte.
    """
    catalogo, vistos = [], set()
    tope = maximo or TOPE_DATOS_GOB
    for termino in TERMINOS_DATOS_GOB:
        if len(catalogo) >= tope:
            break
        url = DATOS_GOB.format(termino=urllib.parse.quote(termino))
        try:
            respuesta = json_de(url)
        except Exception as error:                              # noqa: BLE001
            print("    aviso: datos.gob.es no responde (%s)" % str(error)[:60])
            break
        for elemento in respuesta.get("result", {}).get("items", []):
            if len(catalogo) >= tope:
                break
            titulo = elemento.get("title")
            if isinstance(titulo, list):
                titulo = (titulo[0].get("_value") if isinstance(titulo[0], dict)
                          else titulo[0])
            elif isinstance(titulo, dict):
                titulo = titulo.get("_value")
            titulo = (titulo or "").strip()
            if not titulo or titulo in vistos:
                continue
            plano = sin_acentos(titulo)
            if not any(clave in plano for clave in EXIGIDOS_DATOS_GOB):
                continue
            if any(mal in plano for mal in DESCARTAR_DATOS_GOB):
                continue

            distribuciones = elemento.get("distribution") or []
            if isinstance(distribuciones, dict):
                distribuciones = [distribuciones]
            enlace = None
            for dist in distribuciones:
                if not isinstance(dist, dict):
                    continue
                acceso = str(dist.get("accessURL") or "")
                if ("CSV" in str(dist.get("format", "")).upper()
                        and acceso.lower().endswith(".csv")):
                    enlace = acceso
                    break
            if not enlace:
                continue

            # El identificador de organismo que da el catalogo es una URI que
            # no resuelve a un nombre, asi que se usa el dominio desde el que
            # se descarga el fichero, que si dice quien lo publica.
            dominio = urllib.parse.urlsplit(enlace).netloc.replace("www.", "")
            organismo = f"{dominio} (vía datos.gob.es)"
            vistos.add(titulo)
            catalogo.append({
                "proveedor": "datos.gob.es",
                "id": enlace,
                "titulo": titulo,
                "operacion": "Catálogo datos.gob.es — búsqueda «%s»" % termino,
                "organismo": str(organismo or "Administración publicadora"),
                "periodicidad": "La que fije el organismo",
                "url": enlace,
            })
    if catalogo:
        print("    %d conjunto(s) en datos.gob.es" % len(catalogo))
    return catalogo


def procesar_datos_gob(entrada, carpeta, indice):
    """Guarda el CSV tal cual lo publica el organismo, con su ficha al lado."""
    bruto = descargar(entrada["url"])
    if len(bruto) > MAX_BYTES_CSV:
        raise ValueError("el CSV pesa %d KB, por encima del tope"
                         % (len(bruto) // 1024))
    texto = None
    for juego in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            texto = bruto.decode(juego)
            break
        except UnicodeDecodeError:
            continue
    if texto is None:
        raise ValueError("no se ha podido leer el CSV en ninguna codificación")

    lineas = [l for l in texto.splitlines() if l.strip()]
    if len(lineas) < 2:
        raise ValueError("el CSV no trae filas")

    base = "%02d_datosgob_%s" % (indice, nombre_seguro(entrada["titulo"]))
    with open(os.path.join(carpeta, base + ".csv"), "w",
              encoding="utf-8-sig", newline="") as f:
        f.write("\n".join(lineas))

    separador = ";" if lineas[0].count(";") > lineas[0].count(",") else ","
    columnas = [c.strip() for c in lineas[0].split(separador)]
    detalle = ("Este CSV se guarda **tal cual lo publica el organismo**, sin "
               "reordenar ni traducir, porque cada conjunto trae su propio "
               "esquema. Sus columnas son:\n\n- `"
               + "`\n- `".join(columnas[:20]) + "`")
    escribir_ficha(os.path.join(carpeta, base + ".md"), {
        "titulo": entrada["titulo"],
        "mide": entrada["titulo"] + ". Conjunto publicado en el catálogo "
                "nacional de datos abiertos.",
        "organismo": entrada["organismo"],
        "operacion": entrada["operacion"],
        "periodicidad": entrada["periodicidad"],
        "cobertura": "la que indique el organismo en el propio fichero",
        "ambitos": "el que publique el organismo",
        "filas": len(lineas) - 1,
        "url": entrada["url"],
        "columnas": detalle,
    })
    return {"archivo": "datos/%s.csv" % base, "ficha": "datos/%s.md" % base,
            "titulo": entrada["titulo"], "organismo": entrada["organismo"],
            "periodicidad": entrada["periodicidad"], "filas": len(lineas) - 1}


def comparar(nuevo, anterior, proveedores):
    """
    Altas y bajas respecto al catalogo de la ejecucion anterior.

    Solo se comparan los proveedores consultados en esta ejecucion: si se ha
    acotado con --fuentes, lo de los demas no ha desaparecido, simplemente no
    se ha mirado.
    """
    previo = [c for c in anterior if c.get("proveedor") in proveedores]
    ids_nuevo = {str(c["id"]) for c in nuevo}
    ids_previo = {str(c["id"]) for c in previo}
    return ([c for c in nuevo if str(c["id"]) not in ids_previo],
            [c for c in previo if str(c["id"]) not in ids_nuevo])


# -------------------------------------------------------------------- procesar

def ambito_de(nombre):
    """Dice si una serie del INE es de Espana, de Andalucia o de otro sitio."""
    if "Andaluc" in nombre:
        return "Andalucía"
    if "Nacional" in nombre or "Total Nacional" in nombre or "España" in nombre:
        return "España"
    return None


def procesar_ine(entrada, unidades, carpeta, indice):
    """Descarga una tabla del INE y la deja en CSV plano con su ficha."""
    periodos = PERIODOS.get(entrada["periodicidad"], PERIODOS_POR_DEFECTO)
    url = INE + f"DATOS_TABLA/{entrada['id']}?nult={periodos}"
    series = json_de(url)
    if not isinstance(series, list):
        raise ValueError("la tabla no devuelve series, sino: %s"
                         % str(series)[:70])

    # Una tabla nacional sin desglose territorial no nombra a Espana en cada
    # serie: en ese caso todas las series son del ambito que se detecto al
    # descubrirla.
    sin_territorio = not any(
        ambito_de(s.get("Nombre", "")) for s in series if isinstance(s, dict))

    filas = []
    for serie in series:
        ambito = ambito_de(serie.get("Nombre", ""))
        if ambito is None and sin_territorio:
            ambito = entrada.get("ambito", "España")
        if ambito is None:
            continue
        tramos = [t.strip() for t in serie["Nombre"].split(".") if t.strip()]
        tramos = [t for t in tramos if "Andaluc" not in t and t != "Nacional"]
        indicador = ". ".join(tramos)
        unidad = unidades.get(serie.get("FK_Unidad"), "")
        for dato in serie.get("Data", []):
            if dato.get("Valor") is None:
                continue
            fecha = datetime.fromtimestamp(dato["Fecha"] / 1000, tz=timezone.utc)
            filas.append({
                "fecha": fecha.strftime("%Y-%m-%d"),
                "anio": fecha.year,
                "mes": MESES[fecha.month - 1],
                "trimestre": f"T{(fecha.month - 1) // 3 + 1}",
                "ambito": ambito,
                "indicador": indicador,
                "valor": dato["Valor"],
                "unidad": unidad,
            })

    if not filas:
        raise ValueError("la tabla no devuelve datos de España ni de Andalucía")

    filas.sort(key=lambda f: (f["fecha"], f["ambito"], f["indicador"]), reverse=True)
    base = f"{indice:02d}_INE_{nombre_seguro(entrada['titulo'])}"
    escribir_csv(os.path.join(carpeta, base + ".csv"),
                 ["fecha", "anio", "mes", "trimestre", "ambito", "indicador",
                  "valor", "unidad"], filas)

    fechas = sorted({f["fecha"] for f in filas})
    escribir_ficha(os.path.join(carpeta, base + ".md"), {
        "titulo": entrada["titulo"],
        "mide": f"{entrada['titulo']}. Serie publicada dentro de la operación "
                f"«{entrada['operacion']}».",
        "organismo": "Instituto Nacional de Estadística (INE)",
        "operacion": f"{entrada['operacion_codigo']} — {entrada['operacion']}",
        "periodicidad": entrada["periodicidad"],
        "cobertura": f"{fechas[0]} a {fechas[-1]}",
        "ambitos": ("España y Andalucía" if entrada.get("ambito") == "Andalucía"
                    else "España"),
        "filas": len(filas),
        "url": url,
        "columnas": ("- `fecha` — fecha del periodo, en formato AAAA-MM-DD\n"
                     "- `anio`, `mes`, `trimestre` — el mismo periodo, desglosado\n"
                     "- `ambito` — España o Andalucía\n"
                     "- `indicador` — qué se mide exactamente en esa fila\n"
                     "- `valor` — el dato\n"
                     "- `unidad` — la unidad de medida"),
    })
    return {"archivo": f"datos/{base}.csv", "ficha": f"datos/{base}.md",
            "titulo": entrada["titulo"],
            "organismo": "Instituto Nacional de Estadística (INE)",
            "periodicidad": entrada["periodicidad"], "filas": len(filas)}


def procesar_eurostat(conjunto, carpeta, indice):
    """Descarga un conjunto de Eurostat, decodificando su formato JSON-stat."""
    url = f"{EUROSTAT_API}{conjunto['codigo']}?format=JSON&{conjunto['parametros']}"
    datos = json_de(url)

    dimensiones = datos["dimension"]
    orden = datos.get("id") or list(dimensiones.keys())
    tamanos = datos.get("size") or [len(dimensiones[d]["category"]["index"])
                                    for d in orden]
    tablas = []
    for nombre in orden:
        categoria = dimensiones[nombre]["category"]
        indices = categoria["index"]
        etiquetas = categoria.get("label", {})
        if isinstance(indices, dict):
            pares = sorted(indices.items(), key=lambda kv: kv[1])
        else:
            pares = [(c, i) for i, c in enumerate(indices)]
        tablas.append([(codigo, etiquetas.get(codigo, codigo)) for codigo, _ in pares])

    def descomponer(plano):
        posiciones = []
        for tamano in reversed(tamanos):
            posiciones.append(plano % tamano)
            plano //= tamano
        return list(reversed(posiciones))

    filas = []
    for clave, valor in datos["value"].items():
        if valor is None:
            continue
        posiciones = descomponer(int(clave))
        fila = {}
        for i, nombre in enumerate(orden):
            fila[nombre] = tablas[i][posiciones[i]]
        geo_codigo, geo_etiqueta = fila.get("geo", ("", ""))
        if geo_codigo not in TERRITORIOS:
            continue
        periodo = fila.get("time", ("", ""))[0]
        anio, _, trimestre = periodo.partition("-")
        unidad_codigo, unidad_etiqueta = fila.get("unit", ("", ""))
        # El indicador recoge todas las dimensiones salvo territorio y tiempo:
        # hay conjuntos con edad, sexo o nivel de renta, y sin eso las filas
        # quedarian indistinguibles entre si.
        detalle = [etiqueta for clave, (codigo, etiqueta) in fila.items()
                   if clave not in ("geo", "time", "freq") and etiqueta]
        filas.append({
            "periodo": periodo, "anio": anio, "trimestre": trimestre or "",
            "ambito": TERRITORIOS.get(geo_codigo, geo_etiqueta),
            "indicador": INDICADORES.get(unidad_codigo) or ". ".join(detalle),
            "valor": valor,
            "unidad": UNIDADES_EUROSTAT.get(unidad_codigo, unidad_etiqueta),
        })

    if not filas:
        raise ValueError("el conjunto no devuelve datos para España ni la UE")

    filas.sort(key=lambda f: (f["periodo"], f["ambito"]), reverse=True)
    base = f"{indice:02d}_{conjunto['archivo']}"
    escribir_csv(os.path.join(carpeta, base + ".csv"),
                 ["periodo", "anio", "trimestre", "ambito", "indicador",
                  "valor", "unidad"], filas)

    periodos = sorted({f["periodo"] for f in filas})
    escribir_ficha(os.path.join(carpeta, base + ".md"), {
        "titulo": conjunto["titulo"], "mide": conjunto["mide"],
        "organismo": "Eurostat (Oficina Estadística de la Unión Europea)",
        "operacion": f"{conjunto['codigo']} — conjunto de datos de Eurostat",
        "periodicidad": conjunto["periodicidad"],
        "cobertura": f"{periodos[0]} a {periodos[-1]}",
        "ambitos": "España y Unión Europea (27)",
        "filas": len(filas), "url": url,
        "columnas": ("- `periodo` — trimestre en formato AAAA-Qn\n"
                     "- `anio`, `trimestre` — el mismo periodo, desglosado\n"
                     "- `ambito` — España o Unión Europea (27)\n"
                     "- `indicador` / `unidad` — qué mide la fila y en qué unidad\n"
                     "- `valor` — el dato"),
    })
    return {"archivo": f"datos/{base}.csv", "ficha": f"datos/{base}.md",
            "titulo": conjunto["titulo"], "organismo": "Eurostat",
            "periodicidad": conjunto["periodicidad"], "filas": len(filas)}


# ------------------------------------------------------------------------- main

def leer_json(ruta, por_defecto):
    """Lee un JSON del disco; si no existe o esta roto, devuelve el valor dado."""
    if not os.path.isfile(ruta):
        return por_defecto
    try:
        with open(ruta, encoding="utf-8") as f:
            return json.load(f)
    except Exception:                                           # noqa: BLE001
        return por_defecto


def indice_existente(carpeta_corpus):
    """Conjuntos ya presentes, para poder acumular sin sobrescribir."""
    ruta = os.path.join(carpeta_corpus, "datos.js")
    if not os.path.isfile(ruta):
        return []
    try:
        with open(ruta, encoding="utf-8") as f:
            texto = f.read()
        texto = texto[texto.index("=") + 1:].rstrip().rstrip(";")
        return json.loads(texto)
    except Exception:                                           # noqa: BLE001
        return []


def main():
    analizador = argparse.ArgumentParser(
        description="Descarga datos abiertos sobre vivienda, suelo y construcción.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    analizador.add_argument("--fuentes", default=None, metavar="LISTA",
                            help="proveedores separados por comas (INE, Eurostat). "
                                 "Sin este parámetro se consultan todos.")
    analizador.add_argument("--max", type=int, default=None, metavar="N",
                            dest="maximo",
                            help="tope de tablas por proveedor. Sin este parámetro "
                                 "se descarga todo lo que encuentre.")
    analizador.add_argument("--hilos", type=int, default=6, metavar="N",
                            help="sondeos simultáneos (por defecto 6)")
    analizador.add_argument("--limpiar", action="store_true",
                            help="vacía datos/ antes de escribir; "
                                 "sin este parámetro, acumula")
    analizador.add_argument("--salida", default=None, metavar="RUTA",
                            help="carpeta de corpus (por defecto ../corpus)")
    argumentos = analizador.parse_args()

    aqui = os.path.dirname(os.path.abspath(__file__))
    corpus = argumentos.salida or os.path.join(os.path.dirname(aqui), "corpus")
    carpeta = os.path.join(corpus, "datos")
    os.makedirs(carpeta, exist_ok=True)
    ruta_catalogo = os.path.join(carpeta, "catalogo.json")

    arranque = time.time()

    # 1. que proveedores se consultan
    if argumentos.fuentes:
        pedidos = [sin_acentos(p.strip()) for p in argumentos.fuentes.split(",")
                   if p.strip()]
        proveedores = [p for p in PROVEEDORES if sin_acentos(p) in pedidos]
        if not proveedores:
            print(f"  Ningún proveedor casa con «{argumentos.fuentes}». "
                  f"Disponibles: {', '.join(PROVEEDORES)}")
            return 1
        print(f"  Proveedores: {', '.join(proveedores)} (acotado)")
    else:
        proveedores = list(PROVEEDORES)
        print(f"  Proveedores: {', '.join(proveedores)} (todos)")
    if not argumentos.maximo:
        print("  Sin --max: se descargará todo lo que se encuentre.")

    # 2. descubrir
    anterior = leer_json(ruta_catalogo, [])
    print("\n  Descubriendo qué publican sobre vivienda…")
    catalogo = []
    if "INE" in proveedores:
        catalogo += descubrir_ine(argumentos.maximo, argumentos.hilos)
    if "Eurostat" in proveedores:
        catalogo += descubrir_eurostat(argumentos.maximo)
    if "datos.gob.es" in proveedores:
        catalogo += descubrir_datos_gob(argumentos.maximo)

    if not catalogo:
        print("  No se ha encontrado ningún conjunto.")
        return 1

    altas, bajas = comparar(catalogo, anterior, proveedores)
    if anterior:
        if altas:
            print("    NUEVOS desde la última vez: " +
                  ", ".join(f"{a['id']} ({a['titulo'][:38]})" for a in altas))
        if bajas:
            print("    YA NO APARECEN: " +
                  ", ".join(f"{b['id']} ({b['titulo'][:38]})" for b in bajas))
        if not altas and not bajas:
            print("    sin cambios respecto a la última ejecución")

    # 3. limpiar o acumular
    previos = []
    if argumentos.limpiar:
        for nombre in os.listdir(carpeta):
            if nombre.endswith((".csv", ".md")):
                os.remove(os.path.join(carpeta, nombre))
        print("\n  --limpiar: datos/ vaciada")
    else:
        previos = indice_existente(corpus)
        if previos:
            print(f"\n  Acumulando sobre {len(previos)} conjuntos ya descargados")

    titulos_previos = {c.get("titulo") for c in previos}
    siguiente = len(previos) + 1

    try:
        unidades = {u["Id"]: (u.get("Nombre") or "")
                    for u in json_de(INE + "UNIDADES")}
    except Exception as error:                                  # noqa: BLE001
        print(f"  aviso: catálogo de unidades no disponible ({error})")
        unidades = {}

    # 4. descargar
    print("\n  Descargando:")
    fichas, problemas, saltados = list(previos), [], 0
    for entrada in catalogo:
        if entrada["titulo"] in titulos_previos:
            saltados += 1
            continue
        try:
            if entrada["proveedor"] == "INE":
                ficha = procesar_ine(entrada, unidades, carpeta, siguiente)
            elif entrada["proveedor"] == "datos.gob.es":
                ficha = procesar_datos_gob(entrada, carpeta, siguiente)
            else:
                ficha = procesar_eurostat(entrada, carpeta, siguiente)
            fichas.append(ficha)
            print(f"    OK     {ficha['archivo'][6:]} — {ficha['filas']} filas")
            siguiente += 1
        except Exception as error:                              # noqa: BLE001
            detalle = str(error)
            if "CERTIFICATE_VERIFY_FAILED" in detalle:
                detalle = "el portal que lo publica tiene un certificado no válido"
            problemas.append((entrada["titulo"][:48], detalle[:110]))
            print(f"    FALLA  {entrada['titulo'][:48]}: {detalle[:110]}")

    if saltados:
        print(f"    {saltados} conjunto(s) ya estaban descargados y se conservan")

    # Se conserva en el catalogo lo de los proveedores que no se han mirado,
    # para no perder memoria de ellos al acotar con --fuentes.
    intactos = [c for c in anterior if c.get("proveedor") not in proveedores]
    with open(ruta_catalogo, "w", encoding="utf-8") as f:
        json.dump(intactos + catalogo, f, ensure_ascii=False, indent=1)

    with open(os.path.join(corpus, "datos.js"), "w", encoding="utf-8") as f:
        f.write("window.DATOS = ")
        json.dump([{k: v for k, v in c.items() if k != "filas"} for c in fichas],
                  f, ensure_ascii=False, indent=1)
        f.write(";\n")

    print(f"\n  {len(fichas)} conjuntos en {carpeta}")
    print(f"  Modo: {'limpiado' if argumentos.limpiar else 'acumulado'}")
    print(f"  TIEMPO: {time.time() - arranque:.1f} s")
    if problemas:
        print(f"\n  {len(problemas)} con problemas:")
        for nombre, error in problemas:
            print(f"    - {nombre}: {error}")
    return 0 if fichas else 1


if __name__ == "__main__":
    sys.exit(main())
