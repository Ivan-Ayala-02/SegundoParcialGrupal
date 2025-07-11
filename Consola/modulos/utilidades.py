import random
from os import system
from copy import deepcopy
from datetime import datetime
from unidecode import unidecode
###################################################################### COMPLEMENTARIAS / GENERALES ######################################################################
#---------------------- ARREGLOS VISUALES ----------------------#
# LIMPIAR TERMINAL
def pausar_y_limpiar():
    print()
    system("pause")
    system("cls")

#---------------------- FUNCIONES PARA TRABAJAR CON DICCIONARIOS Y LISTAS ----------------------#
# PARA OBTENER UNA LISTA CON PREGUNTAS FILTRADAS
def filtrar_por_clave(lista: list, clave: str, valor: str) -> list:
    resultado = []

    for elemento in lista:
        claves = obtener_lista_claves(elemento)
        if validar_elemento(claves, clave) and elemento[clave].lower() == valor.lower():
            resultado.append(deepcopy(elemento))

    return resultado

# VENDRIA A SER UN IN EN PYTHON
def validar_elemento(lista: list, elemento_a_verificar: str) -> bool:
    """Valida si un elemento se encuentra dentro de una lista (vector).
    """
    existe = False

    for elemento in lista:
        if elemento_a_verificar == elemento:
            existe = True
            break
    
    return existe

# OPCIONAL, PARA ARCHIVOS (PARA GENERAR CSV DE LAS LISTAS DE CADA JUEGO)
def obtener_preguntas(datos_juegos: dict, juego: str):
    return datos_juegos[juego]   

def generar_copia_de_diccionario_con_listas(diccionario_original: dict) -> dict:
    from copy import deepcopy
    return deepcopy(diccionario_original)

def elegir_elemento_aleatorio_y_remover(lista: list):
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
    return deepcopy(estado_inicial)


def inicializar_recursos_juego(configuracion: dict, preguntas: dict,
                                premios: dict, funciones_juegos: dict):
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


def construir_contexto_mini_juego(ronda, juego, preguntas, estado_jugador, configuracion):
    contexto = {
        "juego": juego,
        "ronda": ronda,
        "preguntas": preguntas,
        "jugador": estado_jugador,
        "configuracion": configuracion
    }

    return contexto

def ejecutar_minijuego(contexto, funciones_juegos):
    juego_actual = contexto["juego"]
    return funciones_juegos[juego_actual](contexto)