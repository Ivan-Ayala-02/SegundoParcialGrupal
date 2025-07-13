# Valentin Luciano Avila - Iván Ayala
# División 211 - Grupo 14 

# Segundo Parcial: Juego de Preguntas y Respuestas Multietapas
from modulos.menus.menu_principal import main
from modulos.py_game.funciones_pygame import *
from modulos.configuracion import *
from modulos.menus.mostrar_menu import *
from modulos.py_game.botones import *

import pygame

pygame.init()

def intro():
    coordenadas_logo = [320,30]
    coordenadas_barassi = [-50,70]

    fondo, logo_juego, barassi = cargar_imagenes_intro()
    mostrar_imagenes_intro(fondo, LONGITUD_PANTALLA, logo_juego, coordenadas_logo, barassi, coordenadas_barassi)

    cargar_audio("recursos/musica_menu.wav")
    ajustar_volumen(0.3)

    lista_opciones = ["Jugar", "Reglas", "Estadisticas", "Extras", "Salir"]
    lista_botones = crear_botones_opciones(lista_opciones, LONGITUD_PANTALLA, (50,40), fuente_texto, (320,310), 10)

    bucle_intro =True
    musica_menu = False
    animacion_intro = False
    ingreso_menu_principal = False
    estado_animacion = False

    while bucle_intro:

        if musica_menu == False:
            pygame.mixer.music.play(-1) # Reproduce en bucle infinito
            musica_menu = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bucle_intro = False
            
            if event.type == pygame.KEYDOWN:
                if animacion_intro == False and ingreso_menu_principal == False:
                    animacion_intro = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                for boton in lista_botones:
                    if boton["rectangulo"].collidepoint(event.pos):
                        boton["presionado"] = True
        
        if animacion_intro:
            estado_animacion = animar_intro(LONGITUD_PANTALLA, fondo, logo_juego, coordenadas_logo)

        if estado_animacion:
            animacion_intro = False
            ingreso_menu_principal = True

        if ingreso_menu_principal:
            dibujar_lista_botones(lista_botones)

        for boton in lista_botones:
            if boton["texto"] == "Salir":
                if boton["presionado"] == True:
                    bucle_intro = False

        pygame.display.update()
    
    pygame.quit()
    
#main()
intro()
