import random
import pygame
import sys
from modulos.boton import *



def obtener_premios(premios_disponibles_copia: dict) -> list | None:
    """Selecciona dos premios al azar de niveles distintos que aún tengan premios disponibles.

    Los premios se eliminan del conjunto disponible para evitar repetirlos más adelante.

    Args:
        premios_disponibles_copia (dict): Diccionario con niveles como claves y listas de premios como valores.

    Returns:
        list | None: Lista con dos premios distintos o None si no hay suficientes niveles con premios.
    """
    niveles = list(premios_disponibles_copia.keys())

    # Filtrar niveles con premios disponibles
    niveles_diponibles = []
    for nivel in niveles:
        if len(premios_disponibles_copia[nivel]) > 0:
            niveles_diponibles.append(nivel)

    if len(niveles_diponibles) < 2:
        return None  # No hay dos niveles distintos con premios

    premios_no_elegidos = False
    premios = []
    
    while not premios_no_elegidos: 
        nivel1 = random.choice(niveles_diponibles)
        nivel2 = random.choice(niveles_diponibles)

        while nivel1 == nivel2:
            nivel2 = random.choice(niveles_diponibles)

        premio1 = random.choice(premios_disponibles_copia[nivel1])
        premio2 = random.choice(premios_disponibles_copia[nivel2])

        premios.append(premio1)
        premios.append(premio2)

        if premio1 != premio2:
            # Eliminar premios ya entregados
            premios_disponibles_copia[nivel1].remove(premio1)
            premios_disponibles_copia[nivel2].remove(premio2)
            premios_no_elegidos = True

    return premios

def elegir_premio(pantalla, premios: list):
    fuente = pygame.font.SysFont("Arial", 24)
    clock = pygame.time.Clock()
    ancho, alto = pantalla.get_size()  # 🔥 Obtenés dimensiones actuales
    fondo = pygame.image.load("recursos\\fondo.jpg")
    fondo = pygame.transform.scale(fondo, (ancho, alto))  # Redimensiona si es necesario

    blanco_btn = crear_boton((180, 60), (ancho//4, 360), pantalla, "white", fuente=("Arial", 30), texto="BLANCO")
    negro_btn = crear_boton((180, 60), ((ancho//4 + 200), 360), pantalla, "white", fuente=("Arial", 30), texto="NEGRO")

    random.shuffle(premios)
    premio_blanco = premios[0]
    premio_negro = premios[1]

    seleccion = None

    while seleccion is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if blanco_btn["rectangulo"].collidepoint(event.pos):
                    seleccion = "blanco"
                elif negro_btn["rectangulo"].collidepoint(event.pos):
                    seleccion = "negro"

        pantalla.fill((10, 10, 40))
        texto = fuente.render("Elegí tu premio", True, (255, 255, 255))
        rect = texto.get_rect(center=(ancho//2, alto//2))

        pantalla.blit(fondo, (0,0))
        pantalla.blit(texto, rect)

        dibujar_boton(blanco_btn)
        dibujar_boton(negro_btn)

        pygame.display.flip()
        clock.tick(60)

    if seleccion == "blanco":
        return premio_blanco, premio_negro, "blanco"
    else:
        return premio_negro, premio_blanco, "negro"




def actualizar_estado_por_premio(premio, premio_dejado, vida, puntos, eleccion):
    if premio["tipo"] == "puntos":
        puntos += premio["valor"]
    elif premio["tipo"] == "vida":
        vida += premio["valor"]
    elif premio["tipo"] == "pierde_todo":
        puntos = 0

    return vida, puntos