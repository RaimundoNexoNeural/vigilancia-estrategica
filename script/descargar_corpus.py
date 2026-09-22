#!/usr/bin/env python3
"""
================================================================================
descargar_corpus.py — Corpus de noticias para la sesion de vigilancia
================================================================================

DESCRIPCION
    Reune noticias recientes del ambito de AVRA (vivienda, suelo, alquiler,
    rehabilitacion, construccion, normativa) y deja una ficha legible por cada
    una, con su cuerpo real, no con el reclamo del RSS.

    Funciona en cinco pasos:
      1. Determina de que fuentes tirar (ver el parametro --fuentes).
      2. Descarga cada feed y se queda con lo publicado dentro de la ventana.
      3. A las fuentes generalistas y oficiales les aplica un filtro tematico.
      4. Entra en la URL de cada noticia y le extrae el cuerpo del articulo.
      5. Escribe las fichas, el indice y el fichero de ayuda.

PARAMETROS
    --fuentes RUTA|LISTA   Opcional. Acota de donde se descarga.
                             - ruta a un CSV de fuentes: usa solo ese fichero
                             - lista separada por comas: usa solo las fuentes de
                               la lista predefinida cuyo nombre o dominio
                               coincida (p. ej. "BOE,Construible")
                           Si NO se indica, se usa la lista predefinida
                           (fuentes.csv) Y ADEMAS se buscan fuentes nuevas en
                           internet, en dos pasos: se pregunta a Google News
                           que medios estan cubriendo los temas de vigilancia,
                           y de esos medios (mas los ya conocidos) se sondean
                           las rutas de feed habituales. Los feeds que
                           respondan se anaden como fuentes nuevas.
                           Google News se usa solo para DESCUBRIR medios,
                           nunca como fuente de noticias: sus enlaces van a un
                           redirector del que no se puede extraer el articulo.
    --dias N               Opcional, 14 por defecto. Ventana hacia atras, en
                           dias. Siempre relativa: el mismo comando sirve
                           dentro de dos semanas.
    --hilos N              Opcional, 8 por defecto. Descargas simultaneas.
    --medios N             Opcional, 20 por defecto. Cuantos de los medios que
                           detecta Google News se sondean buscando su feed.
    --descubiertas N       Opcional, 12 por defecto. Cuantas fuentes nuevas se
                           aceptan como maximo en una ejecucion.
    --limpiar              Opcional. Si se indica, vacia noticias/ y deja solo
                           lo descargado en esta ejecucion. Si NO se indica,
                           ACUMULA: conserva lo que hubiera y anade lo nuevo,
                           sin sobrescribir, saltandose las URL repetidas.
    --corpus-completo      Opcional. Genera ademas corpus-completo.txt, con
                           todas las noticias en un solo fichero de texto.
    --salida RUTA          Opcional. Carpeta de corpus. Por defecto ../corpus.

ENTRADAS
    script/fuentes.csv     Lista predefinida de fuentes: nombre, url, tipo,
                           tope. Si no existe, se crea con una de partida.
                           El tipo decide el trato de cada fuente:
                             especializada - no se filtra por tema
                             generalista   - se filtra por tema
                             oficial       - se filtra por tema
                             suscripcion   - no se filtra (medio de pago)
    corpus/indice.csv      Solo al acumular: se lee para no repetir noticias.
    Internet               Los feeds y la pagina de cada articulo.

SALIDAS  (dentro de la carpeta de corpus)
    noticias/*.md          Una ficha por noticia: metadatos, titular,
                           entradilla y cuerpo. UTF-8 con BOM.
    indice.csv             La tabla del corpus, con BOM para Excel. Es la
                           fuente de verdad de las columnas del visor.
    LEEME.txt              Que es el corpus, cuando se descargo, con que
                           criterio y en que modo.
    corpus-completo.txt    Solo con --corpus-completo.

TEXTO QUE SE GUARDA
    El articulo COMPLETO siempre que la pagina lo exponga, de todas las
    fuentes, incluidas las de suscripcion. Solo queda incompleto cuando un
    muro de pago corta la pagina o cuando la web no publica el texto en HTML.
    El enlace al original se conserva siempre.

DEPENDENCIAS
    Ninguna. Solo biblioteca estandar de Python 3.

EJEMPLOS
    python descargar_corpus.py
    python descargar_corpus.py --dias 7 --limpiar
    python descargar_corpus.py --fuentes fuentes.csv
    python descargar_corpus.py --fuentes "BOE,Construible" --corpus-completo
================================================================================
"""

import argparse
import csv
import gzip
import html
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import zlib
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from xml.etree import ElementTree as ET

# --------------------------------------------------------------- configuracion

AGENTE = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
          "(KHTML, like Gecko) Chrome/129.0 Safari/537.36")
ESPERA_FEED = 25
ESPERA_ARTICULO = 20
TOPE_POR_DEFECTO = 20

# Se conserva el articulo completo. El tope solo existe para que una pagina
# con cientos de parrafos (un sumario, un boletin entero) no desborde el corpus.
PARRAFOS_MAXIMO = 120

# Lista de partida. Solo se usa para crear fuentes.csv la primera vez: a partir
# de ahi manda el fichero, que se edita sin tocar codigo.
FUENTES_POR_DEFECTO = [
    ("Brains Real Estate News", "https://brainsre.news/feed/", "especializada", 20),
    ("Democrata", "https://democrata.es/feed/", "generalista", 20),
    ("Construible", "https://www.construible.es/feed", "especializada", 20),
    ("Innovando en la construccion",
     "https://www.innovandoenlaconstruccion.com/feed/", "especializada", 20),
    ("OVACEN", "https://ovacen.com/feed/", "especializada", 20),
    ("Fotocasa Research", "https://www.fotocasa.es/blog/feed/", "especializada", 14),
    ("Europa Press - Economia",
     "https://www.europapress.es/rss/rss.aspx?ch=00072", "generalista", 20),
    ("20minutos - Vivienda", "https://www.20minutos.es/rss/vivienda/",
     "especializada", 20),
    ("Expansion - Inmobiliario",
     "https://www.expansion.com/rss/empresas/inmobiliario.xml", "suscripcion", 20),
    ("Inmodiario", "https://www.inmodiario.com/feed", "especializada", 20),
    ("El Periodico de la Energia", "https://www.elperiodicodelaenergia.com/feed/",
     "especializada", 8),
    ("Comision Europea - Sala de prensa",
     "https://ec.europa.eu/commission/presscorner/api/rss?language=es",
     "oficial", 20),
    ("BOE - Sumario del dia", "https://www.boe.es/rss/boe.php", "oficial", 20),
]

CABECERAS_FUENTES = ["nombre", "url", "tipo", "tope"]

# El tipo solo decide si la fuente se filtra por tema antes de entrar. El texto
# se guarda completo en todos los casos.
TIPOS_FILTRADOS = {"generalista", "oficial"}

# Temas con los que se busca cuando hay que descubrir fuentes nuevas.
TEMAS_BUSQUEDA = [
    "vivienda protegida Andalucía", "alquiler vivienda España",
    "rehabilitación energética edificios", "suelo urbanizable planeamiento",
    "construcción industrializada", "plan estatal de vivienda",
]
GOOGLE_NEWS = ("https://news.google.com/rss/search?q={consulta}"
               "+when:{dias}d&hl=es&gl=ES&ceid=ES:es")
RUTAS_FEED = ["/feed/", "/rss", "/rss.xml", "/feed", "/index.xml"]
# Cuantos medios de los mas repetidos se sondean, y cuantas fuentes nuevas se
# aceptan como maximo.
MEDIOS_A_SONDEAR = 20
TOPE_DESCUBIERTAS = 12

CLAVES_TEMATICAS = [
    "vivienda", "urbanis", "rehabilitac", "alquiler", "arrendamiento", "suelo",
    "edificac", "construcc", "energetic", "energia", "hipotec", "urbana",
    "alojamiento", "habitacional", "inmobiliar",
]

CLAVES_NUCLEO = [
    "vivienda", "viviendas", "alquiler", "arrendamiento", "hipotec",
    "rehabilitac", "vpo", "vivienda protegida", "urbanis", "suelo",
    "edificac", "infravivienda", "desahucio", "parque publico",
]
CLAVES_PERIFERIA = [
    "construcc", "obra", "energetic", "eficiencia energetica", "inmobiliar",
    "urbana", "alojamiento", "habitacional", "catastro", "arquitect",
    "industrializad", "pobreza energetica", "comunidad energetica",
]

MARCAS_MURO = [
    "suscribete", "suscribase", "hazte suscriptor", "contenido exclusivo",
    "para seguir leyendo", "registrate para", "solo para suscriptores",
    "inicia sesion para", "articulo para suscriptores",
]

COLETILLAS = [
    r"Art[ií]culo publicado originalmente en [^.]{0,160}",
    r"The post .{0,120}? appeared first on .{0,60}",
    r"La entrada .{0,120}? se public[oó] primero en .{0,60}",
    r"La entrada .{0,120}? aparece prime\w*",
    r"Noticias Inmobiliarias y de Vivienda",
    r'">',
    r"Leer\s*$",
    r"\.\.\.\s*$",
]

BASURA = [
    "acepto", "cookies", "politica de privacidad", "newsletter",
    "sigue leyendo", "leer mas", "compartir en", "suscribete",
    "todos los derechos reservados", "publicidad",
]

CABECERAS_INDICE = ["id", "archivo", "titular", "fuente", "fecha", "url",
                    "cuerpo_completo", "motivo_cuerpo", "palabras_cuerpo",
                    "relevancia_prefiltro", "motivo_prefiltro"]


# ------------------------------------------------------------------- utilidades

def descargar(url, espera):
    """Devuelve (bytes, cabecera Content-Type), descomprimiendo si hace falta."""
    peticion = urllib.request.Request(url, headers={
        "User-Agent": AGENTE,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.9",
        "Accept-Encoding": "gzip, deflate",
    })
    with urllib.request.urlopen(peticion, timeout=espera) as respuesta:
        bruto = respuesta.read()
        codificacion = (respuesta.headers.get("Content-Encoding") or "").lower()
        if codificacion == "gzip":
            bruto = gzip.decompress(bruto)
        elif codificacion == "deflate":
            bruto = zlib.decompress(bruto, -zlib.MAX_WBITS)
        return bruto, respuesta.headers.get("Content-Type", "")


def decodificar(bruto, cabecera):
    """Pasa bytes a texto respetando el juego de caracteres que declare la web."""
    juego = None
    coincidencia = re.search(r"charset=([\w\-]+)", cabecera or "", re.I)
    if coincidencia:
        juego = coincidencia.group(1)
    if not juego:
        coincidencia = re.search(rb'charset=["\']?([\w\-]+)', bruto[:4000], re.I)
        if coincidencia:
            juego = coincidencia.group(1).decode("ascii", "ignore")
    for candidato in (juego, "utf-8", "cp1252", "latin-1"):
        if not candidato:
            continue
        try:
            return bruto.decode(candidato)
        except (UnicodeDecodeError, LookupError):
            continue
    return bruto.decode("utf-8", "replace")


def sin_etiquetas(texto):
    """Quita el HTML y deja texto plano."""
    if not texto:
        return ""
    texto = re.sub(r"(?is)<(script|style).*?</\1>", " ", texto)
    texto = re.sub(r"<[^>]+>", " ", texto)
    texto = html.unescape(texto)
    return re.sub(r"\s+", " ", texto).strip()


def sin_acentos(texto):
    """Minusculas y sin tildes, para comparar sin sorpresas."""
    texto = unicodedata.normalize("NFKD", (texto or "").lower())
    return texto.encode("ascii", "ignore").decode()


def limpiar_entradilla(texto):
    """Quita del resumen del feed las coletillas de autopromocion."""
    if not texto:
        return ""
    for _ in range(3):
        anterior = texto
        for patron in COLETILLAS:
            texto = re.sub(patron, " ", texto, flags=re.I)
        texto = re.sub(r"\s+", " ", texto).strip(" -|·–—\"")
        if texto == anterior:
            break
    mitad = len(texto) // 2
    if mitad > 40 and texto[:mitad].strip() == texto[mitad:].strip():
        texto = texto[:mitad].strip()
    if len(texto) < 45 or not re.search(r"[.:;]|\d", texto):
        return ""
    return texto


# ---------------------------------------------------------------------- fuentes

def cargar_fuentes_csv(ruta, crear_si_falta=False):
    """Lee un CSV de fuentes. Si se pide, lo crea con la lista de partida."""
    if not os.path.isfile(ruta):
        if not crear_si_falta:
            raise FileNotFoundError(ruta)
        with open(ruta, "w", encoding="utf-8-sig", newline="") as f:
            escritor = csv.writer(f)
            escritor.writerow(CABECERAS_FUENTES)
            escritor.writerows(FUENTES_POR_DEFECTO)
        print(f"  Creado {os.path.basename(ruta)} con "
              f"{len(FUENTES_POR_DEFECTO)} fuentes de partida.")

    fuentes = []
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        for fila in csv.DictReader(f):
            nombre = (fila.get("nombre") or "").strip()
            url = (fila.get("url") or "").strip()
            if not nombre or not url or url.startswith("#"):
                continue
            try:
                tope = int((fila.get("tope") or "").strip() or TOPE_POR_DEFECTO)
            except ValueError:
                tope = TOPE_POR_DEFECTO
            fuentes.append({
                "nombre": nombre,
                "url": url,
                "tipo": (fila.get("tipo") or "especializada").strip().lower(),
                "tope": tope,
                "origen": "lista",
            })
    return fuentes


def acotar(fuentes, seleccion):
    """Deja solo las fuentes cuyo nombre o dominio case con la lista pedida."""
    pedidas = [sin_acentos(p.strip()) for p in seleccion.split(",") if p.strip()]
    return [f for f in fuentes
            if any(p in sin_acentos(f["nombre"] + " " + f["url"]) for p in pedidas)]


def feed_valido(url):
    """Comprueba que la URL devuelve algo que parece un feed con entradas."""
    try:
        bruto, _ = descargar(url, ESPERA_FEED)
        return len(parsear_feed(bruto)) > 0
    except Exception:                                           # noqa: BLE001
        return False


def medios_en_google_news(dias):
    """
    Pregunta a Google News que medios estan cubriendo los temas de vigilancia.

    Solo se recoge el DOMINIO de cada medio, que es lo aprovechable: los
    enlaces de Google News van a un redirector en JavaScript del que no se
    puede extraer el articulo, asi que no sirven como fuente de noticias.
    Devuelve los dominios ordenados por cuantas veces aparecen.
    """
    frecuencia = {}
    for tema in TEMAS_BUSQUEDA:
        url = GOOGLE_NEWS.format(consulta=urllib.parse.quote_plus(tema), dias=dias)
        try:
            bruto, _ = descargar(url, ESPERA_FEED)
            raiz = ET.fromstring(bruto.lstrip())
        except Exception:                                       # noqa: BLE001
            continue
        for elemento in raiz.iter():
            if elemento.tag.split("}")[-1] != "item":
                continue
            for hijo in elemento:
                if hijo.tag.split("}")[-1] == "source":
                    dominio = (hijo.attrib.get("url") or "").rstrip("/")
                    if dominio.startswith("http"):
                        frecuencia[dominio] = frecuencia.get(dominio, 0) + 1
    return [d for d, _ in sorted(frecuencia.items(), key=lambda kv: -kv[1])]


def descubrir_fuentes(conocidas, dias, hilos, medios=None, tope=None):
    """
    Busca fuentes que no esten en la lista predefinida.

    Primero averigua que medios estan publicando sobre los temas de vigilancia
    (ver medios_en_google_news). Despues sondea, en esos medios y en los ya
    conocidos, las rutas de feed habituales, y se queda con las que devuelven
    un feed con entradas. Asi las noticias llegan del propio medio, con su URL
    real y su cuerpo recuperable.

    Devuelve una lista de fuentes con origen "descubierta".
    """
    usadas = {f["url"].rstrip("/") for f in conocidas}

    dominios = []
    for fuente in conocidas:
        partes = urllib.parse.urlsplit(fuente["url"])
        if partes.scheme and partes.netloc:
            raiz = f"{partes.scheme}://{partes.netloc}"
            if raiz not in dominios:
                dominios.append(raiz)

    medios = medios or MEDIOS_A_SONDEAR
    tope = tope or TOPE_DESCUBIERTAS
    encontrados = medios_en_google_news(dias)
    print(f"    {len(encontrados)} medios detectados cubriendo estos temas; "
          f"se sondean {min(medios, len(encontrados))}")
    nuevos = [d for d in encontrados[:medios] if d not in dominios]

    # Los medios que no estaban en la lista van primero: las plazas de
    # descubrimiento valen mas gastadas en un medio nuevo que en otro canal
    # de uno que ya se esta leyendo.
    candidatas = [(d, d + ruta) for d in nuevos + dominios for ruta in RUTAS_FEED
                  if (d + ruta).rstrip("/") not in usadas]

    with ThreadPoolExecutor(max_workers=hilos) as ejecutor:
        validas = list(ejecutor.map(lambda par: (par, feed_valido(par[1])),
                                    candidatas))

    nuevas, vistos = [], set()
    for (raiz, url), vale in validas:
        if not vale or raiz in vistos or len(nuevas) >= tope:
            continue
        vistos.add(raiz)
        dominio = urllib.parse.urlsplit(raiz).netloc.replace("www.", "")
        nuevas.append({
            "nombre": f"{dominio} (descubierta)",
            "url": url,
            # generalista: se filtra por tema, porque muchos de estos medios
            # publican de todo y aqui solo interesa el ambito de la Agencia.
            "tipo": "generalista",
            "tope": 8,
            "origen": "descubierta",
        })
    return nuevas


# ------------------------------------------------------------------- extraccion

def extraer_parrafos(pagina):
    """Saca del HTML de un articulo los parrafos con sentido."""
    cuerpo = pagina
    for etiqueta in ("script", "style", "nav", "header", "footer", "aside",
                     "form", "figure", "noscript", "iframe"):
        cuerpo = re.sub(rf"(?is)<{etiqueta}\b.*?</{etiqueta}>", " ", cuerpo)

    for contenedor in ("article", "main"):
        trozos = re.findall(rf"(?is)<{contenedor}\b[^>]*>(.*?)</{contenedor}>", cuerpo)
        if trozos:
            cuerpo = max(trozos, key=len)
            break

    parrafos = []
    for bruto in re.findall(r"(?is)<p\b[^>]*>(.*?)</p>", cuerpo):
        texto = sin_etiquetas(bruto)
        if len(texto) < 60:
            continue
        plano = sin_acentos(texto)
        if any(marca in plano for marca in BASURA) and len(texto) < 160:
            continue
        if texto not in parrafos:
            parrafos.append(texto)
    return parrafos


def obtener_cuerpo(entrada):
    """
    Descarga el articulo y devuelve (parrafos, estado, nota).

    Estado:
      si       el texto que publica la pagina, completo
      parcial  un muro de pago lo ha cortado, o apenas hay texto
      no       no se ha podido abrir, o la web no lo publica en HTML
    """
    try:
        bruto, cabecera = descargar(entrada["url"], ESPERA_ARTICULO)
    except urllib.error.HTTPError as error:
        return [], "no", f"La fuente respondió {error.code} al pedir el artículo."
    except Exception as error:                                  # noqa: BLE001
        return [], "no", f"No se ha podido abrir el artículo ({type(error).__name__})."

    parrafos = extraer_parrafos(decodificar(bruto, cabecera))
    if not parrafos:
        return [], "no", "La página no expone el texto del artículo en HTML plano."

    recorte = parrafos[:PARRAFOS_MAXIMO]
    nota = ""
    if len(parrafos) > PARRAFOS_MAXIMO:
        nota = (f"Página muy larga: se guardan los {PARRAFOS_MAXIMO} primeros "
                f"párrafos de {len(parrafos)}.")

    plano = sin_acentos(" ".join(recorte[:6]))
    if any(marca in plano for marca in MARCAS_MURO):
        return recorte, "parcial", (
            "Un muro de pago corta el artículo: solo está lo que la web deja "
            "leer. El texto completo está en el enlace.")

    if sum(len(p) for p in recorte) < 300:
        return recorte, "parcial", nota or "El texto publicado es muy breve."

    return recorte, "si", nota


def clasificar_prefiltro(titular, cuerpo):
    """Pre-filtro tematico. No descarta nada: solo etiqueta."""
    plano = sin_acentos(titular + " " + cuerpo)
    nucleo = sum(1 for clave in CLAVES_NUCLEO if clave in plano)
    periferia = sum(1 for clave in CLAVES_PERIFERIA if clave in plano)
    en_titular = any(clave in sin_acentos(titular) for clave in CLAVES_NUCLEO)

    if en_titular or nucleo >= 2:
        return "alta", "El ámbito de la Agencia aparece en el titular o de forma repetida."
    if nucleo == 1 or periferia >= 2:
        return "dudosa", "Toca el ámbito de refilón: hay que leerla para decidir."
    return "fuera", "No aparece el ámbito de la Agencia; candidata a descarte."


# ------------------------------------------------------------------------ feeds

def leer_fecha(texto):
    """Normaliza las muchas formas de fecha que traen los feeds."""
    if not texto:
        return None
    try:
        fecha = parsedate_to_datetime(texto)
    except (TypeError, ValueError):
        try:
            fecha = datetime.fromisoformat(texto.replace("Z", "+00:00"))
        except ValueError:
            return None
    if fecha.tzinfo is None:
        fecha = fecha.replace(tzinfo=timezone.utc)
    return fecha


def etiqueta_de(elemento, *nombres):
    """Texto del primer hijo que coincida, ignorando el espacio de nombres."""
    for hijo in elemento:
        nombre = hijo.tag.split("}")[-1]
        if nombre in nombres:
            if nombre == "link" and not (hijo.text or "").strip():
                return hijo.attrib.get("href", "")
            return (hijo.text or "").strip()
    return ""


def parsear_feed(contenido):
    """Convierte el XML de un feed (RSS o Atom) en una lista de entradas."""
    if contenido.startswith(b"\xef\xbb\xbf"):
        contenido = contenido[3:]
    raiz = ET.fromstring(contenido.lstrip())
    entradas = []
    for elemento in raiz.iter():
        if elemento.tag.split("}")[-1] in ("item", "entry"):
            entradas.append({
                "titular": sin_etiquetas(etiqueta_de(elemento, "title")),
                "url": etiqueta_de(elemento, "link", "id"),
                "fecha": leer_fecha(etiqueta_de(elemento, "pubDate", "published",
                                                "updated", "date")),
                "entradilla": limpiar_entradilla(
                    sin_etiquetas(etiqueta_de(elemento, "description",
                                              "summary", "content"))),
            })
    return entradas


# ----------------------------------------------------------------------- salida

def nombre_archivo(fecha, titular, indice):
    """Nombre de fichero estable: fecha, numero de orden y titular."""
    base = re.sub(r"[^a-z0-9]+", "-", sin_acentos(titular)).strip("-")[:60]
    dia = fecha.strftime("%Y%m%d") if fecha else "sinfecha"
    return f"{dia}_{indice:03d}_{base or 'noticia'}.md"


def escribir_noticia(ruta, ficha, parrafos):
    """Escribe la ficha Markdown de una noticia."""
    lineas = [
        "---",
        f"titular: {ficha['titular']}",
        f"fuente: {ficha['fuente']}",
        f"fecha: {ficha['fecha']}",
        f"url: {ficha['url']}",
        f"cuerpo_completo: {ficha['cuerpo_completo']}",
        f"relevancia_prefiltro: {ficha['relevancia_prefiltro']}",
        "---",
        "",
        f"# {ficha['titular']}",
        "",
        f"**{ficha['fuente']}** · {ficha['fecha']} · [ver original]({ficha['url']})",
        "",
    ]
    if ficha["entradilla"]:
        lineas += [f"> {ficha['entradilla']}", ""]
    if parrafos:
        for parrafo in parrafos:
            lineas += [parrafo, ""]
    else:
        lineas += ["*(No se ha podido recuperar el texto del artículo. "
                   "El enlace de arriba lleva al original.)*", ""]
    if ficha["nota_cuerpo"]:
        lineas += ["---", "", f"*{ficha['nota_cuerpo']}*", ""]
    # utf-8-sig: con BOM, para que el navegador no adivine el juego de caracteres.
    with open(ruta, "w", encoding="utf-8-sig") as f:
        f.write("\n".join(lineas))


def leer_indice(ruta):
    """Devuelve las filas del indice anterior, para poder acumular."""
    if not os.path.isfile(ruta):
        return []
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        return [fila for fila in csv.DictReader(f) if fila.get("url")]


def elegir_fuentes(argumentos, aqui):
    """Resuelve el parametro --fuentes a una lista de fuentes."""
    ruta_lista = os.path.join(aqui, "fuentes.csv")

    if argumentos.fuentes and os.path.isfile(argumentos.fuentes):
        fuentes = cargar_fuentes_csv(argumentos.fuentes)
        print(f"  Fuentes: {len(fuentes)}, acotadas a "
              f"{os.path.basename(argumentos.fuentes)}")
        return fuentes

    if argumentos.fuentes:
        fuentes = acotar(cargar_fuentes_csv(ruta_lista, crear_si_falta=True),
                         argumentos.fuentes)
        print(f"  Fuentes: {len(fuentes)}, acotadas a «{argumentos.fuentes}»")
        return fuentes

    fuentes = cargar_fuentes_csv(ruta_lista, crear_si_falta=True)
    print(f"  Fuentes: {len(fuentes)} en fuentes.csv. Buscando además fuentes "
          f"nuevas en internet…")
    descubiertas = descubrir_fuentes(fuentes, argumentos.dias, argumentos.hilos,
                                     argumentos.medios, argumentos.descubiertas)
    print(f"  {len(descubiertas)} fuente(s) descubierta(s); "
          f"{len(fuentes) + len(descubiertas)} en total")
    return fuentes + descubiertas


# ------------------------------------------------------------------------- main

def main():
    analizador = argparse.ArgumentParser(
        description="Descarga un corpus de noticias de vigilancia con su cuerpo.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    analizador.add_argument("--fuentes", default=None, metavar="RUTA|LISTA",
                            help="CSV de fuentes, o lista de nombres separados por "
                                 "comas. Sin este parámetro se usa la lista "
                                 "predefinida y además se buscan fuentes nuevas.")
    analizador.add_argument("--dias", type=int, default=14, metavar="N",
                            help="ventana hacia atrás en días (por defecto 14)")
    analizador.add_argument("--hilos", type=int, default=8, metavar="N",
                            help="descargas simultáneas (por defecto 8)")
    analizador.add_argument("--medios", type=int, default=None, metavar="N",
                            help="medios detectados que se sondean (por defecto 20)")
    analizador.add_argument("--descubiertas", type=int, default=None, metavar="N",
                            help="máximo de fuentes nuevas aceptadas (por defecto 12)")
    analizador.add_argument("--limpiar", action="store_true",
                            help="vacía noticias/ antes de escribir; "
                                 "sin este parámetro, acumula")
    analizador.add_argument("--corpus-completo", action="store_true",
                            dest="corpus_completo",
                            help="genera además corpus-completo.txt")
    analizador.add_argument("--salida", default=None, metavar="RUTA",
                            help="carpeta de corpus (por defecto ../corpus)")
    argumentos = analizador.parse_args()

    aqui = os.path.dirname(os.path.abspath(__file__))
    corpus = argumentos.salida or os.path.join(os.path.dirname(aqui), "corpus")
    carpeta_noticias = os.path.join(corpus, "noticias")
    os.makedirs(carpeta_noticias, exist_ok=True)
    ruta_indice = os.path.join(corpus, "indice.csv")

    arranque = time.time()

    # 1. de donde se descarga
    fuentes = elegir_fuentes(argumentos, aqui)
    if not fuentes:
        print("  Ninguna fuente casa con ese filtro. Nada que hacer.")
        return 1

    # 2. limpiar o acumular
    previas = []
    if argumentos.limpiar:
        for nombre in os.listdir(carpeta_noticias):
            os.remove(os.path.join(carpeta_noticias, nombre))
        # Tambien el corpus en un solo fichero: si no, se queda con el
        # contenido de la tanda anterior y enganaria.
        anterior_completo = os.path.join(corpus, "corpus-completo.txt")
        if os.path.isfile(anterior_completo):
            os.remove(anterior_completo)
        print("  --limpiar: noticias/ vaciada")
    else:
        previas = leer_indice(ruta_indice)
        if previas:
            print(f"  Acumulando sobre {len(previas)} noticias ya descargadas")

    urls_previas = {fila["url"] for fila in previas}
    siguiente_id = max([int(f.get("id") or 0) for f in previas] or [0]) + 1

    # 3. feeds
    print("\n  Feeds:")
    recogidas, fallos = [], []
    corte = datetime.now(timezone.utc) - timedelta(days=argumentos.dias)
    for fuente in fuentes:
        nombre, url = fuente["nombre"], fuente["url"]
        try:
            bruto, _ = descargar(url, ESPERA_FEED)
            entradas = parsear_feed(bruto)
        except Exception as error:                              # noqa: BLE001
            fallos.append((nombre, str(error)[:120]))
            print(f"    FALLA  {nombre}: {str(error)[:120]}")
            continue

        aceptadas = 0
        for entrada in entradas:
            if aceptadas >= fuente["tope"]:
                break
            if entrada["fecha"] and entrada["fecha"] < corte:
                continue
            if not entrada["titular"] or not entrada["url"]:
                continue
            if entrada["url"] in urls_previas:
                continue
            if fuente["tipo"] in TIPOS_FILTRADOS:
                plano = sin_acentos(entrada["titular"] + " " + entrada["entradilla"])
                if not any(clave in plano for clave in CLAVES_TEMATICAS):
                    continue
            entrada["fuente"] = nombre
            entrada["tipo"] = fuente["tipo"]
            recogidas.append(entrada)
            urls_previas.add(entrada["url"])
            aceptadas += 1
        marca = "  (descubierta)" if fuente.get("origen") == "descubierta" else ""
        print(f"    {aceptadas:>4} de {len(entradas):>4}  {nombre}{marca}")

    if not recogidas:
        print("\n  No hay noticias nuevas en la ventana pedida.")
        return 0

    recogidas.sort(key=lambda e: e["fecha"] or datetime.min.replace(tzinfo=timezone.utc),
                   reverse=True)

    # 4. cuerpo de cada articulo
    print(f"\n  Entrando en {len(recogidas)} artículos con {argumentos.hilos} hilos…")
    inicio = time.time()
    with ThreadPoolExecutor(max_workers=argumentos.hilos) as ejecutor:
        resultados = list(ejecutor.map(obtener_cuerpo, recogidas))
    print(f"  Cuerpos descargados en {time.time() - inicio:.1f} s")

    # 5. fichas e indice
    filas = list(previas)
    nuevas = []
    for desplazamiento, (entrada, (parrafos, estado, nota)) in enumerate(
            zip(recogidas, resultados)):
        identificador = siguiente_id + desplazamiento
        fecha = entrada["fecha"].strftime("%Y-%m-%d %H:%M") if entrada["fecha"] else ""
        cuerpo = " ".join(parrafos)
        relevancia, motivo = clasificar_prefiltro(entrada["titular"], cuerpo)
        archivo = nombre_archivo(entrada["fecha"], entrada["titular"], identificador)

        escribir_noticia(os.path.join(carpeta_noticias, archivo), {
            "titular": entrada["titular"], "fuente": entrada["fuente"],
            "fecha": fecha, "url": entrada["url"],
            "entradilla": entrada["entradilla"][:400],
            "cuerpo_completo": estado, "relevancia_prefiltro": relevancia,
            "nota_cuerpo": nota,
        }, parrafos)

        fila = {
            "id": identificador, "archivo": f"noticias/{archivo}",
            "titular": entrada["titular"], "fuente": entrada["fuente"],
            "fecha": fecha, "url": entrada["url"],
            "cuerpo_completo": estado, "motivo_cuerpo": nota,
            "palabras_cuerpo": len(cuerpo.split()),
            "relevancia_prefiltro": relevancia, "motivo_prefiltro": motivo,
        }
        filas.append(fila)
        nuevas.append((fila, cuerpo, entrada["entradilla"]))

    with open(ruta_indice, "w", encoding="utf-8-sig", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=CABECERAS_INDICE,
                                  extrasaction="ignore")
        escritor.writeheader()
        escritor.writerows(filas)

    if argumentos.corpus_completo:
        ruta_completo = os.path.join(corpus, "corpus-completo.txt")
        textos = []
        for fila, cuerpo, entradilla in nuevas:
            textos += [
                f"[{fila['id']}] {fila['titular']}",
                f"    Fuente: {fila['fuente']} | Fecha: {fila['fecha']} | "
                f"Cuerpo: {fila['cuerpo_completo']} | "
                f"Pre-filtro: {fila['relevancia_prefiltro']}",
                f"    URL: {fila['url']}",
                "    " + (cuerpo or entradilla),
                "",
            ]
        nuevo_fichero = argumentos.limpiar or not os.path.isfile(ruta_completo)
        with open(ruta_completo, "w" if nuevo_fichero else "a",
                  encoding="utf-8-sig") as f:
            if nuevo_fichero:
                f.write(f"CORPUS DE VIGILANCIA\nGenerado el "
                        f"{datetime.now():%d/%m/%Y a las %H:%M}\n" + "=" * 70 + "\n\n")
            f.write("\n".join(textos))
        print(f"  corpus-completo.txt: {len(nuevas)} noticias añadidas")

    with open(os.path.join(corpus, "LEEME.txt"), "w", encoding="utf-8-sig") as f:
        f.write(
            "Corpus de la sesion 4 - Vigilancia Estrategica Aumentada con IA\n"
            f"Ultima descarga: {datetime.now():%d/%m/%Y a las %H:%M}\n"
            f"Ventana: ultimos {argumentos.dias} dias\n"
            f"Modo: {'limpiado' if argumentos.limpiar else 'acumulado'}\n\n"
            f"{len(filas)} noticias en noticias/, en Markdown y legibles por si\n"
            "solas. El indice esta en indice.csv. Los datos abiertos, en datos/.\n\n"
            "Cada ficha indica si se ha podido recuperar el cuerpo del articulo\n"
            "(cuerpo_completo: si / parcial / no) y un pre-filtro tematico\n"
            "(relevancia_prefiltro: alta / dudosa / fuera). No se ha borrado nada:\n"
            "lo que no viene al caso esta marcado, no eliminado.\n\n"
            "De la prensa se conserva un extracto y el enlace al original, nunca\n"
            "el articulo completo. Nada esta generado: todo es verificable en su URL.\n")

    resumen, prefiltro = {}, {}
    for fila in filas:
        resumen[fila["cuerpo_completo"]] = resumen.get(fila["cuerpo_completo"], 0) + 1
        prefiltro[fila["relevancia_prefiltro"]] = \
            prefiltro.get(fila["relevancia_prefiltro"], 0) + 1
    palabras = sum(int(f["palabras_cuerpo"]) for f in filas)

    print(f"\n  {len(nuevas)} noticias nuevas · {len(filas)} en el corpus")
    print("  Cuerpo recuperado: " +
          ", ".join(f"{k}={v}" for k, v in sorted(resumen.items())))
    print("  Pre-filtro: " +
          ", ".join(f"{k}={v}" for k, v in sorted(prefiltro.items())))
    print(f"  Palabras de cuerpo: {palabras}")
    print(f"  TIEMPO TOTAL: {time.time() - arranque:.1f} s")
    if fallos:
        print(f"\n  {len(fallos)} fuente(s) con problemas:")
        for nombre, error in fallos:
            print(f"    - {nombre}: {error}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
