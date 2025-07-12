import pygame
from botones import *

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

pygame.init()

# Establezco el tamaño de la pantalla ---------------------------------------------------

PANTALLA = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
fondo_juego = pygame.image.load("pygame/recursos/fondo.jpg")
logo_juego = pygame.image.load("pygame/recursos/icono_menu.png")
barassi = pygame.image.load("pygame/recursos/barassi_menu.png")
PANTALLA.blit(fondo_juego, (0,0))
PANTALLA.blit(logo_juego, (320,30))
PANTALLA.blit(barassi, (-50,70))

# Genero el icono nombre de ventana -----------------------------------------------------

pygame.display.set_caption("¡AHORA CAIGO!")
icono_ventana = pygame.image.load("pygame/recursos/zapatillas.png")
pygame.display.set_icon(icono_ventana)

# Inicio el mixer para la cancion del menu ----------------------------------------------

pygame.mixer.init()
pygame.mixer.music.load("pygame/recursos/musica_menu.wav")
pygame.mixer.music.set_volume(0.1) # Volumen del juego

# establezco los botones del MENU INICIO ------------------------------------------------

fuente_texto = ("arial", 20)

boton_salir = crear_boton(dimensiones=(30,30), 
                          posicion=(760,10), 
                          ventana=PANTALLA, 
                          imagen="pygame/recursos/exit.png",
                          color_borde=None)

boton_menu_principal = crear_boton(dimensiones=(50,150),
                         posicion=(400,400),
                         ventana=PANTALLA,
                         fuente=(fuente_texto),
                         texto="Ingrese cualquier boton para continuar",
                         color_borde=None)
                         
lista_botones = [boton_salir, boton_menu_principal]

# Inicio el bucle principal -------------------------------------------------------------

bandera_juego = True 
musica_reproducida = False

while bandera_juego:

    if not musica_reproducida:
        pygame.mixer.music.play(-1) # Reproduce en bucle infinito
        musica_reproducida = True

    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            bandera_juego = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_salir["rectangulo"].collidepoint(evento.pos):
                boton_salir["presionado"] = True

    dibujar_lista_botones(lista_botones)

    if boton_salir["presionado"] == True:
        bandera_juego = False

    pygame.display.update()

pygame.quit()
