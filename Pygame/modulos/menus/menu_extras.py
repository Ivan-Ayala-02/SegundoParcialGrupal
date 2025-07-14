import pygame
from modulos.configuracion import *
from modulos.py_game.botones import *
from modulos.py_game.funciones_pygame import *

def menu_extras(juegos_extras:dict):

    pygame.init()
    fondo = cargar_imagen("recursos/fondo.jpg")
    icono_juego = cargar_imagen("recursos/icono_menu.png")
    coordenadas_icono = [140,30]
    lista_minijuegos = list(extras.keys())
    lista_botones_minijuegos = crear_botones_opciones(lista_minijuegos, LONGITUD_PANTALLA, (50,40), fuente_texto, (300,100), 10)

    mostrar_imagen(fondo, LONGITUD_PANTALLA, (0,0))
    mostrar_imagen(icono_juego, LONGITUD_PANTALLA, coordenadas_icono)

    volver_atras = crear_boton((50,100), (300,550), LONGITUD_PANTALLA, None, None, fuente_texto, "Volver atras")

    animacion_finalizada = False
    bandera_menu = True
    while bandera_menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bandera_menu = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if volver_atras["rectangulo"].collidepoint(event.pos):
                        volver_atras["presionado"] = True
            
        if animacion_finalizada == False:
            animacion_finalizada = animar_imagen(LONGITUD_PANTALLA, fondo, icono_juego, coordenadas_icono, (140,-300), 2)
            
        if animacion_finalizada:
            mostrar_imagen(fondo, LONGITUD_PANTALLA, (0,0))
            dibujar_lista_botones(lista_botones_minijuegos)
            dibujar_boton(volver_atras)

        if volver_atras["presionado"]:
            volver_atras["presionado"] = False
            bandera_menu = False
        
        pygame.display.update()

            
