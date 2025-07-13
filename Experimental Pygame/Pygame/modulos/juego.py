import time
from modulos.utilidades import *
from modulos.configuracion import *
from modulos.estadisticas import mostrar_estadisticas, guardar_resultado_partida
from modulos.premios import *

def iniciar_juego(nombre_usuario: str):
    pausar_y_limpiar()

    estado_jugador = inicializar_estado_jugador(estado_inicial)
    recursos_juego  = inicializar_recursos_juego(configuracion_juego, preguntas,
                                            premios, funciones_juegos)

    inicio = time.time()
    datos_usuario, victoria = jugar_partida(nombre_usuario, estado_jugador, recursos_juego)

    if victoria:
        duracion = time.time() - inicio
        datos_usuario["tiempo_juego"] = duracion
        mostrar_estadisticas(datos_usuario)
    else:
        print("Perdiste el Juego!")

    guardar_resultado_partida(nombre_usuario, datos_usuario)

###########################    PARTIDA    ###########################
def jugar_partida(nombre_usuario: str, estado_jugador: dict, recursos_juego: dict):
    config = recursos_juego ["configuracion"]

    rondas = config["rondas"]
    cambio_de_juego = config["cambio_de_juego"]
    dificultades = config["dificultades"]
    
    juegos_restantes = recursos_juego ["juegos_restantes"]
    victoria = True
    juego_actual = None

    for ronda in range(rondas):
        if ronda % cambio_de_juego == 0 or juego_actual == None:
            juego_actual = elegir_elemento_aleatorio_y_remover(juegos_restantes)

        en_juego = jugar_ronda(ronda, juego_actual, dificultades, estado_jugador, recursos_juego)

        if not en_juego:
            estado_jugador["puntos"] = 0
            victoria = False
            break

    if victoria:
        resultado = "victoria"
    else:
        resultado = "derrota"

    datos_usuario = construir_datos_usuario(estado_jugador, nombre_usuario, resultado)

    resultado_partida = (datos_usuario, victoria)

    return resultado_partida

###########################    RONDA    ###########################
def jugar_ronda(ronda, juego_actual, dificultades, estado_jugador, recursos_juego):
    dificultad = obtener_dificultad(ronda, dificultades)
    preguntas = obtener_preguntas(recursos_juego["preguntas_disponibles"], juego_actual)
    preguntas_por_dificultad = filtrar_por_clave(preguntas, "dificultad", dificultad)

    contexto_juego = construir_contexto_mini_juego(ronda, juego_actual,
                                                preguntas_por_dificultad,
                                                estado_jugador,
                                                recursos_juego["configuracion"])

    resultado_ronda = False
    acierto = False

    while not acierto and estado_jugador["vida"] > 0:
        resultado = ejecutar_minijuego(contexto_juego, recursos_juego["funciones_juegos"])

        if resultado:
            manejar_ronda_ganada(estado_jugador, recursos_juego["premios_disponibles"])
            resultado_ronda = True
            acierto = True
        else:
            manejar_ronda_perdida(estado_jugador)
            resultado_ronda = False  # solo cuando realmente fallás

        pausar_y_limpiar()

    return resultado_ronda

def manejar_ronda_ganada(jugador, premios_disponibles):
    print("Ganaste la ronda.")
    pausar_y_limpiar()
    premios = obtener_premios(premios_disponibles)

    if premios is None:
        print("No hay más premios para elegir.")
        return

    premio, premio_dejado, eleccion = elegir_premio(premios)
    jugador["vida"], jugador["puntos"] = actualizar_estado_por_premio(
        premio, premio_dejado, jugador["vida"], jugador["puntos"], eleccion
    )


def manejar_ronda_perdida(jugador):
    if jugador["fichas"] > 0:
        jugador["fichas"] -= 1
        print(f"❤️ Se usó una ficha como vida. Te quedan {jugador['fichas']} ficha(s).")
    else:
        jugador["vida"] -= 1