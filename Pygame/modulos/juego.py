import sys
import time
import pygame
from modulos.premios import *
from modulos.utilidades import *
from modulos.configuracion import *
from modulos.mini_juegos.mini_juegos import jugar_si_o_no
from archivos.archivo_csv import cargar_datos_csv
from modulos.estadisticas import guardar_resultado_partida


def iniciar_juego(pantalla, nombre_usuario: str):
    estado_jugador = inicializar_estado_jugador(estado_inicial)
    recursos_juego = inicializar_recursos_juego(configuracion_juego, preguntas,
                                                 premios, funciones_juegos)

    inicio = time.time()
    datos_usuario, victoria = jugar_partida(pantalla, nombre_usuario, estado_jugador, recursos_juego)
    duracion = time.time() - inicio
    datos_usuario["tiempo_juego"] = duracion

    # Parte donde va pygame
    mostrar_mensaje_final(pantalla, victoria)
    guardar_resultado_partida(nombre_usuario, datos_usuario)

###########################   MANEJO DE PARTIDA    ###########################
def jugar_partida(pantalla, nombre_usuario: str, estado_jugador: dict, recursos_juego: dict):
    config = recursos_juego ["configuracion"]

    rondas = config["rondas"]
    cambio_de_juego = config["cambio_de_juego"]
    dificultades = config["dificultades"]
    juegos_restantes = recursos_juego ["juegos_restantes"]
    
    juego_actual = None
    victoria = True

    for ronda in range(rondas):
        if ronda % cambio_de_juego == 0 or juego_actual == None:
            juego_actual = elegir_elemento_aleatorio_y_remover(juegos_restantes)
        # PARTE EN LA QUE IRIA PYGAME
        en_juego = jugar_ronda(pantalla, ronda, juego_actual, dificultades, estado_jugador, recursos_juego)
        print(en_juego)
        ##############################################
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
    print(resultado_partida)
    return resultado_partida

###########################   MANEJO DE RONDA    ###########################
def jugar_ronda(pantalla, ronda, juego_actual, dificultades, estado_jugador, recursos_juego):
    dificultad = obtener_dificultad(ronda, dificultades)
    preguntas = obtener_preguntas(recursos_juego["preguntas_disponibles"], juego_actual)
    preguntas_por_dificultad = filtrar_por_clave(preguntas, "dificultad", dificultad)

    recursos_mini_juego = obtener_recursos_mini_juego(ronda, juego_actual,
                                                preguntas_por_dificultad,
                                                estado_jugador,
                                                recursos_juego["configuracion"])

    resultado_ronda = False
    acierto = False

    while not acierto and estado_jugador["vida"] > 0:
        resultado = ejecutar_minijuego(pantalla, recursos_mini_juego, recursos_juego["funciones_juegos"])
        print(resultado)
        if resultado:
            # MANEJO DE RONDA GANADA CON PYGAME(MOSTRAR QUE SE ACERTO LA PREGUNTA Y LUEGO ELEGIR PREMIO)
            manejar_ronda_ganada(pantalla, estado_jugador, recursos_juego["premios_disponibles"])
            resultado_ronda = True
            acierto = True
        else:
            manejar_ronda_perdida(pantalla, estado_jugador)
            resultado_ronda = False  # solo cuando realmente fallás

    return resultado_ronda

def esperar_cierre_o_tecla():
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                esperando = False  # continúa con el juego


# ---------------------- MANEJO DE RESULTADOS DE RONDA ----------------------
def manejar_ronda_ganada(pantalla, jugador: dict, premios_disponibles: dict):
    fuente = pygame.font.SysFont("Arial", 28)

    # Paso 1: Mensaje de victoria
    mostrar_resultado_simple(pantalla, "¡Ganaste la ronda!", (0, 200, 0))
    pygame.time.wait(1500)

    # Paso 2: Obtener premios
    premios = obtener_premios(premios_disponibles)
    if premios is None:
        mostrar_resultado_simple(pantalla, "No hay más premios disponibles 🎁", (200, 200, 0))
        pygame.time.wait(1500)
        return

    # Paso 3: Elegir entre blanco y negro
    premio, premio_dejado, eleccion = elegir_premio(pantalla, premios)

    # Paso 4: Aplicar efectos del premio
    jugador["vida"], jugador["puntos"] = actualizar_estado_por_premio(
        premio, premio_dejado, jugador["vida"], jugador["puntos"], eleccion
    )

    if premio["tipo"] == "puntos":
        mostrar_resultado_simple(pantalla, f"Obtuvo {premio['valor']} puntos.", (255, 255, 255))
    elif premio["tipo"] == "vida":
        mostrar_resultado_simple(pantalla, f"¡Gano una vida!", (255, 255, 255))
    else:
        mostrar_resultado_simple(pantalla, f"Perdio todo!", (255, 255, 255))

    pygame.time.wait(1000)
    return

def manejar_ronda_perdida(pantalla, jugador: dict):
    """Procesa las consecuencias de una ronda perdida en Pygame.

    Si el jugador tiene fichas, usa una. Si no, pierde una vida.
    Muestra un mensaje gráfico según lo que se haya usado.

    Args:
        pantalla: Surface de Pygame donde se muestra el mensaje.
        jugador (dict): Estado actual del jugador.
    """
    if jugador["fichas"] > 0:
        jugador["fichas"] -= 1
        mensaje = f"❤️ Se usó una ficha como vida. Te quedan {jugador['fichas']} ficha(s)"
        mostrar_resultado_simple(pantalla, mensaje, (255, 165, 0))  # naranja
    else:
        jugador["vida"] -= 1
        mensaje = f"💀 Perdiste una vida. Vidas restantes: {jugador['vida']}"
        mostrar_resultado_simple(pantalla, mensaje, (255, 0, 0))  # rojo

    pygame.time.wait(1000)
    return