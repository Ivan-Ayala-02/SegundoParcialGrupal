import random
from os import system
from copy import deepcopy
from datetime import datetime
from unidecode import unidecode
import pygame
import json

def cargar_json(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def mostrar_resultado_simple(pantalla, texto, color):
    fuente = pygame.font.SysFont("Arial", 40)
    render = fuente.render(texto, True, color)
    rect = render.get_rect(center=(pantalla.get_width()//2, pantalla.get_height()//2))
    pantalla.fill((20, 20, 40))
    pantalla.blit(render, rect)
    pygame.display.flip()
    pygame.time.wait(1500)


def inicializar_ventana(ancho=960, alto=540, titulo="Mi Juego"):
    """Inicializa Pygame y crea la ventana principal del juego."""
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption(titulo)
    return ventana

def mostrar_resultado_simple(pantalla, texto, color):
    ancho, alto = pantalla.get_size()  # 🔥 Obtenés dimensiones actuales
    ancho, alto = pantalla.get_size()  # 🔥 Obtenés dimensiones actuales
    fondo = pygame.image.load("recursos\\fondo.jpg")
    fondo = pygame.transform.scale(fondo, (ancho, alto))  # Redimensiona si es necesario
    fuente = pygame.font.SysFont("Segoe UI Emoji", 20)
    render = fuente.render(texto, True, color)
    rect = render.get_rect(center=(ancho//2, alto//2))
    pantalla.fill((20, 20, 40))
    pantalla.blit(fondo, (0,0))
    pantalla.blit(render, rect)
    pygame.display.flip()

###################################################################### COMPLEMENTARIAS / GENERALES ######################################################################
#---------------------- ARREGLOS VISUALES ----------------------#
# LIMPIAR TERMINAL

#---------------------- FUNCIONES PARA TRABAJAR CON DICCIONARIOS Y LISTAS ----------------------#
# PARA OBTENER UNA LISTA CON PREGUNTAS FILTRADAS
def filtrar_por_clave(lista: list, clave: str, valor: str) -> list:
    """Filtra elementos de una lista de diccionarios por una clave y valor específico.

    Args:
        lista (list): Lista de diccionarios.
        clave (str): Clave a buscar dentro de cada diccionario.
        valor (str): Valor que debe tener la clave para que el elemento sea incluido.

    Returns:
        list: Nueva lista con los elementos filtrados (copias profundas).
    """
    resultado = []

    for elemento in lista:
        claves = obtener_lista_claves(elemento)
        if validar_elemento(claves, clave) and elemento[clave].lower() == valor.lower():
            resultado.append(deepcopy(elemento))

    return resultado

# VENDRIA A SER UN IN EN PYTHON
def validar_elemento(lista: list, elemento_a_verificar: str) -> bool:
    """Verifica si un elemento existe dentro de una lista.

    Args:
        lista (list): Lista de elementos.
        elemento_a_verificar (str): Elemento que se desea buscar.

    Returns:
        bool: True si el elemento está presente, False en caso contrario.
    """
    existe = False

    for elemento in lista:
        if elemento_a_verificar == elemento:
            existe = True
            break
    
    return existe

# OPCIONAL, PARA ARCHIVOS (PARA GENERAR CSV DE LAS LISTAS DE CADA JUEGO)
def obtener_preguntas(datos_juegos: dict, juego: str) -> list:
    """Obtiene la lista de preguntas correspondientes a un juego específico.

    Args:
        datos_juegos (dict): Diccionario con los juegos como claves y listas de preguntas como valores.
        juego (str): Nombre del juego a consultar.

    Returns:
        list: Lista de preguntas del juego.
    """
    return datos_juegos[juego]   

"""def generar_copia_de_diccionario_con_listas(diccionario_original: dict) -> dict:
    from copy import deepcopy
    return deepcopy(diccionario_original)"""

def elegir_elemento_aleatorio_y_remover(lista: list):
    """Elige un elemento aleatorio de una lista y lo elimina de la misma.

    Args:
        lista (list): Lista de elementos.

    Returns:
        any | None: Elemento elegido, o None si la lista está vacía.
    """
    if len(lista) == 0:
        return None
    elegido = random.choice(lista)
    lista.remove(elegido)

    return elegido

def obtener_lista_claves(diccionario: dict):
    lista_claves = list(diccionario.keys())

    return lista_claves

def lista_vacia(lista: list):
    if len(lista) == 0:
        vacio = True
    else:
        vacio = False

    return vacio

#---------------------- VALIDACIÓN ----------------------#
def comparar_respuestas(resp_usuario: str, resp_correcta: str) -> bool:
    """Compara ignorando tildes, mayúsculas y espacios extras."""
    r1 = unidecode(resp_usuario.strip().lower())
    r2 = unidecode(resp_correcta.strip().lower())
    return r1 == r2

def obtener_dificultad(ronda: int, dificultades: list):
    return dificultades[ronda % len(dificultades)]


def inicializar_estado_jugador(estado_inicial: dict):
    """Crea una copia independiente del estado inicial del jugador.

    Se utiliza para asegurarse de que el estado de cada jugador sea único 
    y no modifique el estado base original.

    Args:
        estado_inicial (dict): Diccionario con los valores iniciales del jugador.

    Returns:
        dict: Copia del estado inicial para ser utilizado en la partida.
    """
    return deepcopy(estado_inicial)


def inicializar_recursos_juego(configuracion: dict, preguntas: dict,
                                premios: dict, funciones_juegos: dict):
    """Prepara los recursos base necesarios para comenzar la partida.

    Crea una copia profunda de las preguntas y premios, conserva la configuración original
    y genera una lista con los juegos disponibles a jugar. Agrupa todo en un solo diccionario.

    Args:
        configuracion (dict): Configuración general del juego (rondas, dificultad, etc.).
        preguntas (dict): Preguntas organizadas por juego.
        premios (dict): Premios posibles para el jugador.
        funciones_juegos (dict): Diccionario de funciones de cada minijuego.

    Returns:
        dict: Diccionario que contiene todos los recursos del juego.
    """
    contexto = {
        "configuracion": configuracion,
        "preguntas_disponibles": deepcopy(preguntas),
        "premios_disponibles": deepcopy(premios),
        "funciones_juegos": funciones_juegos,
        "juegos_restantes": obtener_lista_claves(funciones_juegos)
    }
    
    return contexto

def construir_datos_usuario(estado_jugador, nombre, resultado):
    datos = estado_jugador.copy()
    datos["nombre"] = nombre
    datos["resultado"] = resultado

    return datos

def obtener_recursos_mini_juego(ronda, juego, preguntas, estado_jugador, configuracion):
    contexto = {
        "juego": juego,
        "ronda": ronda,
        "preguntas": preguntas,
        "jugador": estado_jugador,
        "configuracion": configuracion
    }

    return contexto

def ejecutar_minijuego(pantalla, recursos, funciones_juegos):
    juego_actual = recursos["juego"]
    return funciones_juegos[juego_actual](pantalla, recursos)


def mostrar_mensaje_final(pantalla, victoria: bool):
    if victoria:
        mostrar_resultado_simple(pantalla, f"¡Ganaste el Juego!", (255, 255, 255))
    else:
        mostrar_resultado_simple(pantalla, f"Perdiste el Juego!", (255, 255, 255))    
    pygame.time.wait(1500)
    return


def obtener_partidas_ganadas(partidas: list) -> list:
    """Filtra y devuelve todas las partidas ganadas.

    Args:
        partidas (list): Lista de diccionarios con datos de cada partida.

    Returns:
        list: Lista de partidas ganadas.
    """
    partidas_ganadas = []    
    for partida in partidas:
        if partida["resultado"] == "victoria":
            partidas_ganadas.append(partida)

    return partidas_ganadas

def normalizar_nombre_juego(nombre_juego: str):
    """Convierte el nombre de un juego a formato legible: reemplaza guiones bajos por espacios y capitaliza cada palabra.

    Args:
        nombre_juego (str): Nombre original del juego (ej. 'si_o_no').

    Returns:
        str: Nombre formateado (ej. 'Si O No').
    """
    return nombre_juego.replace('_', ' ').title()












def mostrar_pregunta(pantalla, fuente, texto):
    
    ancho, alto = pantalla.get_size()  # 🔥 Obtenés dimensiones actuales

    # Ahora podés usar ancho y alto en cualquier cálculo
    centro_x = ancho // 2
    centro_y = alto // 2

    render = fuente.render(texto, True, (255, 255, 255))
    rect = render.get_rect(center=(centro_x, centro_y))
    pantalla.blit(render, rect)

def mostrar_tiempo(pantalla, fuente, segundos):
    texto = fuente.render(f"⏱️ {segundos}s", True, (255, 255, 255))
    pantalla.blit(texto, (5, 10))
    
def mostrar_estado_jugador(pantalla, jugador, fuente):
    texto = f"❤️ {jugador['vida']}  🎟️ {jugador['fichas']}  ⭐ {jugador['puntos']}"
    render = fuente.render(texto, True, (255, 255, 255))
    pantalla.blit(render, (550, 10))

def obtener_tiempo_limite(config, juego_actual):
    """Obtiene el tiempo límite asignado a un minijuego desde la configuración general.

    Args:
        config (dict): Configuración general del juego, que incluye los tiempos por juego.
        juego_actual (str): Nombre del minijuego.

    Returns:
        int | float: Tiempo límite en segundos para ese minijuego.
    """
    return config["tiempos_limite"][juego_actual]