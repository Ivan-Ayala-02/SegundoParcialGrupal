import re
from colorama import Fore, Style

###################################################################### IMPRIMIR ######################################################################
#---------------------- FUNCIONES PARA USAR EN IMPRESIONES ----------------------#
# COLORES Y ELIMINACIÓN DE CARACTERES ANSI
def strip_ansi(texto):
    """Elimina los códigos de color ANSI para calcular longitud visible."""
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', texto)

def dificultad_a_color(dificultad: str) -> str:
    dificultad = dificultad.lower()
    color = ""
    texto = dificultad.capitalize()

    if dificultad == "fácil":
        color = Fore.GREEN
        texto = "Fácil"
    elif dificultad == "media":
        color = Fore.YELLOW
        texto = "Media"
    elif dificultad == "difícil":
        color = Fore.RED
        texto = "Difícil"

    return f"{color}{texto}{Style.RESET_ALL}"

def obtener_longitud_maxima_cadenas(linea_1: str, linea_2: str):
    long_linea_1 = len(strip_ansi(linea_1))
    long_linea_2 = len(strip_ansi(linea_2))
    longitud_maxima = max(long_linea_1, long_linea_2)

    return longitud_maxima

def obtener_ancho_referencia(texto: str, categoria: str,
                            dificultad: str, tipo_dato: str,
                            espacios_por_lado: int = 4):
    linea_1 = f"Categoría: {categoria} | Dificultad: {dificultad}"
    linea_2 = f"{tipo_dato}: {texto}"

    linea_mas_larga = obtener_longitud_maxima_cadenas(linea_1, linea_2)
    ancho_referencia =  linea_mas_larga + (espacios_por_lado * 2)

    return ancho_referencia

def normalizar_nombre_juego(nombre_juego: str):
    return nombre_juego.replace('_', ' ').title()

#----------------------  IMPRESIONES ----------------------#
def imprimir_string_recuadro(texto: str, espacios_por_lado: int = 4, margen_izquierdo: int = 0):
    ancho = len(texto) + (espacios_por_lado * 2)

    print(" " * margen_izquierdo + "╔" + "═" * ancho + "╗")
    print(" " * margen_izquierdo + "║" + texto.center(ancho) + "║")
    print(" " * margen_izquierdo + "╚" + "═" * ancho + "╝")

def imprimir_info_ronda(ronda: int, juego_actual: str, ancho_referencia: int, espacios_por_lado: int = 4):
    texto = f"Ronda {ronda + 1} | Juego actual: {juego_actual}"
    ancho = len(texto) + (espacios_por_lado * 2)
    margen_izquierdo = (ancho_referencia - ancho) // 2
    imprimir_string_recuadro(texto, espacios_por_lado, margen_izquierdo)

def imprimir_strings_recuadro_dividido(linea_1: str, linea_2: str):
    ancho = len(strip_ansi(linea_1))

    print("╔" + "═" * ancho + "╗")
    print("║" + linea_1 + "║")
    print("╟" + "─" * ancho + "╢")
    print("║" + linea_2 + "║")
    print("╚" + "═" * ancho + "╝")

def imprimir_enunciado(texto: str, categoria: str, dificultad: str, tipo_dato: str, espacios_por_lado: int = 4):
    dificultad_con_color = dificultad_a_color(dificultad)
    dificultad_sin_color = strip_ansi(dificultad_con_color)

    linea_1_base = f"Categoría: {categoria} | Dificultad: {dificultad_sin_color}"
    linea_2_base = f"{tipo_dato}: {texto}"

    linea_mas_larga = obtener_longitud_maxima_cadenas(linea_1_base, linea_2_base)
    ancho = linea_mas_larga + (espacios_por_lado * 2)

    # Centrado antes de aplicar color
    linea_1_centrada = linea_1_base.center(ancho)
    linea_2_centrada = linea_2_base.center(ancho)

    # Insertar color después del centrado
    linea_1_coloreada = linea_1_centrada.replace(dificultad_sin_color, dificultad_con_color)

    imprimir_strings_recuadro_dividido(linea_1_coloreada, linea_2_centrada)

def imprimir_encabezado_y_enunciado(ronda: int, juego_actual: str, dato: str,
                                    categoria: str, dificultad: str,
                                    tipo_dato: str):
    # calcular ancho del enunciado
    ancho_referencia = obtener_ancho_referencia(dato, categoria, dificultad, tipo_dato)

    imprimir_info_ronda(ronda, juego_actual, ancho_referencia)
    imprimir_enunciado(dato, categoria, dificultad, tipo_dato)

def imprimir_lista(lista:list): ####### <-------- Nuevo
    for elemento in lista: 
    # Imprime elemento por elemento dentro de la lista
        print(f'{elemento}')
