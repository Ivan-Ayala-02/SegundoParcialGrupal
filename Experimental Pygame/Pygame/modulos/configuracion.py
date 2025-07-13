from copy import deepcopy
from modulos.mini_juegos.mini_juegos import *
from modulos.py_game.funciones_pygame import *
from archivos.archivo_json import cargar_datos_json
from archivos.archivo_csv import cargar_datos_csv

configuracion_juego = cargar_datos_json("archivos\json\configuracion.json")

rondas = configuracion_juego["rondas"]
estado_inicial = configuracion_juego["estado_inicial"]
tiempos = configuracion_juego["tiempos_limite"]
modo = configuracion_juego["accesibilidad"]
dificultades = configuracion_juego["dificultades"]

funciones_juegos = {
    "si_o_no": jugar_si_o_no,
    "completar_oracion": jugar_completar_oracion,
    "completar_palabra": jugar_completar_palabra,
    "preguntados": jugar_preguntados
}    

preguntas = {
    "si_o_no": cargar_datos_csv("archivos\csv\si_o_no.csv"),
    "completar_oracion": cargar_datos_csv("archivos\csv\completar_oracion.csv"),
    "completar_palabra": cargar_datos_csv("archivos\csv\completar_palabra.csv"),
    "preguntados": cargar_datos_csv("archivos\csv\preguntados.csv")
}

premios = cargar_datos_json("archivos\json\premios.json")

premios_disponibles = deepcopy(premios)

estadisticas_jugadores = []

diccionario_datos_tablero = {
    "bloque_visual_ocupado" : ".",
    "bloque_visual_liberado" : " ",
    "bloque_visual_mina" : "x",
    "caracter_real_bloque" : 0,
    "caracter_real_liberado" : 1,
    "caracter_real_mina" : 2
    }

#-------------------------------------------------------------------------------------------------------

ANCHO_PANTALLA = configuracion_juego["ancho_pantalla"]
ALTO_PANTALLA = configuracion_juego["alto_pantalla"]
LONGITUD_PANTALLA = crear_ventana(ANCHO_PANTALLA, ALTO_PANTALLA)

def crear_ventana(ancho:int, alto:int) -> tuple:
    VENTANA = pygame.display.set_mode((ancho,alto))
    return VENTANA

generar_nombre_e_icono_ventana("¡AHORA CAIGO!", "recursos/zapatillas.png")
fuente_texto = ("Arial", 30)
