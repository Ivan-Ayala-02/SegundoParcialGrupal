import pygame
from modulos.botones import *
from modulos.audio import *

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

pygame.init()

# Establezco el tamaño de la pantalla ---------------------------------------------------

PANTALLA = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
fondo_juego = pygame.image.load("pygame/recursos/fondo.jpg")
logo_juego = pygame.image.load("pygame/recursos/icono_menu.png")
barassi = pygame.image.load("pygame/recursos/barassi_menu.png")
pos_logo_juego = [320,30]
pos_barassi = [-50,70]
PANTALLA.blit(fondo_juego, (0,0))
PANTALLA.blit(logo_juego, pos_logo_juego)
PANTALLA.blit(barassi, pos_barassi)

# Genero el icono nombre de ventana -----------------------------------------------------

pygame.display.set_caption("¡AHORA CAIGO!")
icono_ventana = pygame.image.load("pygame/recursos/zapatillas.png")
pygame.display.set_icon(icono_ventana)

# Inicio el mixer para la cancion del menu ----------------------------------------------

pygame.mixer.init()
pygame.mixer.music.load("pygame/recursos/musica_menu.wav")
ajustar_volumen(0.1)

# establezco los botones del MENU INICIO ------------------------------------------------

fuente_texto = ("arial", 20)

boton_salir = crear_boton(dimensiones=(30,30), 
                          posicion=(760,10), 
                          ventana=PANTALLA, 
                          imagen="pygame/recursos/exit.png",
                          color_borde=None)

boton_menu_principal = crear_boton(dimensiones=(50,150),
                         posicion=(450,400),
                         ventana=PANTALLA,
                         fuente=(fuente_texto),
                         texto="Presione enter para continuar",
                         color_borde=None)
                         
lista_botones = [boton_salir, boton_menu_principal]

# Inicio el bucle principal -------------------------------------------------------------

bandera_juego = True 
musica_reproducida = False
animacion_en_progreso = False

'''def verificar_accion(tipo_evento, comparador, accion):
    if tipo_evento == comparador:
        accion

def presionar_boton(boton:dict, evento):'''

while bandera_juego:

    if not musica_reproducida:
        pygame.mixer.music.play(-1) # Reproduce en bucle infinito
        musica_reproducida = True

    for evento in pygame.event.get():
        #print(evento)    
        if evento.type == pygame.QUIT:
            bandera_juego = False

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                animacion_en_progreso = True
                lista_botones.remove(boton_menu_principal)
    
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_salir["rectangulo"].collidepoint(evento.pos):
                boton_salir["presionado"] = True

    dibujar_lista_botones(lista_botones)

    if boton_salir["presionado"] == True:
        bandera_juego = False
    
    if animacion_en_progreso:
    # Mover logo_juego hacia el centro (400, 300)
        if pos_logo_juego[0] < 140:
            pos_logo_juego[0] += 2
        elif pos_logo_juego[0] > 140:
            pos_logo_juego[0] -= 2
    
        if pos_barassi[0] > -barassi.get_width():
            pos_barassi[0] -= 4
    
        PANTALLA.blit(fondo_juego, (0,0))  # Redibuja el fondo
        PANTALLA.blit(logo_juego, pos_logo_juego)
        PANTALLA.blit(barassi, pos_barassi)

        if pos_logo_juego == [140, 30] and pos_barassi[0] <= -barassi.get_width():
            animacion_en_progreso = False
        
        print(animacion_en_progreso)

    pygame.display.update()

pygame.quit()
