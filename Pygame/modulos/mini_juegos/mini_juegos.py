import pygame
import time
from modulos.boton import crear_boton, dibujar_lista_botones
from modulos.utilidades import lista_vacia, elegir_elemento_aleatorio_y_remover, comparar_respuestas, mostrar_pregunta, mostrar_tiempo, mostrar_estado_jugador
from modulos.tiempo import obtener_tiempo_limite
import sys


def jugar_si_o_no(pantalla, recursos_mini_juego: dict) -> bool:
    fuente = pygame.font.SysFont("Segoe UI Emoji", 20)
    reloj = pygame.time.Clock()

    ancho, alto = pantalla.get_size()  # 🔥 Obtenés dimensiones actuales

    # Ahora podés usar ancho y alto en cualquier cálculo
    centro_x = ancho // 2
    centro_y = alto // 2

    fondo = pygame.image.load("recursos\\fondo.jpg")
    fondo = pygame.transform.scale(fondo, (ancho, alto))  # Redimensiona si es necesario

    preguntas = recursos_mini_juego["preguntas"]
    estado_jugador = recursos_mini_juego["jugador"]
    config = recursos_mini_juego["configuracion"]
    juego = recursos_mini_juego["juego"]

    if lista_vacia(preguntas):
        print("No hay más preguntas disponibles.")
        return False

    tiempo_limite = obtener_tiempo_limite(config, juego)

    fuente_texto = ("Segoe UI Emoji", 20)
    boton_si = crear_boton((180, 60), (ancho//4, 360), pantalla, "white", fuente=("Arial", 30), texto="SI")
    boton_no = crear_boton((180, 60), ((ancho//4 + 200), 360), pantalla, "white", fuente=("Arial", 30), texto="NO")
    botones = [boton_si, boton_no]

    dato = elegir_elemento_aleatorio_y_remover(preguntas)
    respuesta = None
    inicio = time.time()

    while True:
        tiempo_transcurrido = time.time() - inicio
        tiempo_restante = max(0, int(tiempo_limite - tiempo_transcurrido))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_si["rectangulo"].collidepoint(evento.pos):
                    respuesta = "si"
                elif boton_no["rectangulo"].collidepoint(evento.pos):
                    respuesta = "no"

        if respuesta is not None or tiempo_restante <= 0:
            if respuesta is None:
                estado_jugador["fallos"] += 1
                return False
            elif comparar_respuestas(respuesta, dato["respuesta"]):
                estado_jugador["aciertos"] += 1
                estado_jugador["puntos"] += 100
                return True
            else:
                estado_jugador["fallos"] += 1
                estado_jugador["preguntas_falladas"].append(dato["pregunta"])
                return False

        pantalla.fill((10, 10, 40))
        pantalla.blit(fondo, (0,0))

        mostrar_tiempo(pantalla, fuente, tiempo_restante)
        mostrar_pregunta(pantalla, fuente, dato["pregunta"])
        mostrar_estado_jugador(pantalla, estado_jugador, fuente)
        
        dibujar_lista_botones(botones)

        pygame.display.flip()
        reloj.tick(60)

    
import sys, time, pygame
import sys, time, pygame

def jugar_completar_palabra(pantalla, recursos_mini_juego: dict) -> bool:
    # --- Config básica --------------------------------------------------------
    fuente        = pygame.font.SysFont("Segoe UI Emoji", 20)
    fuente_input  = pygame.font.SysFont("Consolas", 28, bold=True)
    reloj         = pygame.time.Clock()

    ancho, alto   = pantalla.get_size()
    centro_x      = ancho // 2
    centro_y      = alto // 2

    fondo = pygame.image.load("recursos\\fondo.jpg")
    fondo = pygame.transform.scale(fondo, (ancho, alto))

    preguntas      = recursos_mini_juego["preguntas"]
    estado_jugador = recursos_mini_juego["jugador"]
    config         = recursos_mini_juego["configuracion"]
    juego          = recursos_mini_juego["juego"]

    if lista_vacia(preguntas):
        print("No hay más preguntas disponibles.")
        return False

    tiempo_limite = obtener_tiempo_limite(config, juego)

    # --- Preparar datos de la ronda ------------------------------------------
    dato             = elegir_elemento_aleatorio_y_remover(preguntas)
    texto_pregunta   = dato["palabra"]       # ej.: "PYTH_N"
    texto_respuesta  = dato["respuesta"].strip()

    # --- Variables de entrada -------------------------------------------------
    entrada_actual   = ""
    respuesta_final  = None
    inicio_ronda     = time.time()
    MAX_CHARS        = 32

    # --- Bucle principal ------------------------------------------------------
    while True:
        tiempo_restante = max(0, int(tiempo_limite - (time.time() - inicio_ronda)))

        # -- Eventos ----------------------------------------------------------
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    respuesta_final = entrada_actual.strip()

                elif evento.key == pygame.K_BACKSPACE:
                    entrada_actual = entrada_actual[:-1]

                elif evento.unicode.isprintable() and len(entrada_actual) < MAX_CHARS:
                    entrada_actual += evento.unicode

        # -- Fin de ronda -----------------------------------------------------
        if respuesta_final is not None or tiempo_restante <= 0:
            if respuesta_final is None:  # sin tiempo
                estado_jugador["fallos"] += 1
                estado_jugador["preguntas_falladas"].append(texto_pregunta)
                return False

            elif comparar_respuestas(respuesta_final, texto_respuesta):
                estado_jugador["aciertos"] += 1
                estado_jugador["puntos"]   += 150
                return True
            else:
                estado_jugador["fallos"] += 1
                estado_jugador["preguntas_falladas"].append(texto_pregunta)
                return False

        # --- Dibujo ----------------------------------------------------------
        pantalla.blit(fondo, (0, 0))
        mostrar_tiempo(pantalla, fuente, tiempo_restante)
        mostrar_pregunta(pantalla, fuente, texto_pregunta)
        mostrar_estado_jugador(pantalla, estado_jugador, fuente)

        # Caja de texto
        box_w, box_h  = 500, 50
        caja_rect     = pygame.Rect(centro_x - box_w // 2, centro_y + 100, box_w, box_h)
        pygame.draw.rect(pantalla, (255, 255, 255), caja_rect, 2, border_radius=8)

        texto_render  = fuente_input.render(entrada_actual.upper(), True, (255, 255, 255))
        pantalla.blit(
            texto_render,
            (caja_rect.x + 10, caja_rect.y + (box_h - texto_render.get_height()) // 2)
        )

        pygame.display.flip()
        reloj.tick(60)