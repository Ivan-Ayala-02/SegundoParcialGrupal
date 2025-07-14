from modulos.utilidades import validar_elemento, obtener_lista_claves, obtener_partidas_ganadas
from modulos.tiempo import calcular_m_s_ms, formatear_fecha_actual
from archivos.archivo_json import *

######################################################################    GUARDAR PARTIDA Y DATOS    ######################################################################
def crear_datos_partida(datos_jugador: dict):
    if datos_jugador["aciertos"] > 0:
        promedio = sum(datos_jugador["tiempo_por_aciertos"]) / datos_jugador["aciertos"]
    else:
        promedio = 0.0
    
    datos = {
        "fecha": formatear_fecha_actual(),
        "aciertos": datos_jugador["aciertos"],
        "fallos": datos_jugador["fallos"],
        "puntos": datos_jugador["puntos"],
        "tiempo_promedio": round(promedio, 2), # Use round para que sea medianamente preciso
        "preguntas_falladas": datos_jugador["preguntas_falladas"],
        "resultado": datos_jugador["resultado"]
    }
    
    return datos

def registrar_partida(usuario, datos_partida, estadisticas):
    # Recorremos las claves manualmente para ver si el usuario ya existe
    existe = False
    for clave in estadisticas:
        if clave == usuario:
            existe = True
            break

    # Si no existe, lo creamos con lista vacía de partidas
    if not existe:
        estadisticas[usuario] = {"partidas": []}

    # Agregamos la partida a la lista
    estadisticas[usuario]["partidas"].append(datos_partida)

def guardar_resultado_partida(nombre_usuario, datos_usuario):
    datos_partida = crear_datos_partida(datos_usuario)
    estadisticas = cargar_datos_json("archivos\json\estadisticas.json")
    registrar_partida(nombre_usuario, datos_partida, estadisticas)
    guardar_diccionario("archivos\json\estadisticas.json", estadisticas)