from modulos.jugador import registrar_nuevo_usuario, seleccionar_perfil 
from modulos.menus.mostrar_menu import mostrar_menu_jugar
from modulos.utilidades import pausar_y_limpiar
from modulos.juego import iniciar_juego

def menu_jugar(estadisticas: dict):
    salir = False
    
    while not salir:
        opcion = mostrar_menu_jugar()

        match opcion:
            case "1":
                pausar_y_limpiar()
                perfil = registrar_nuevo_usuario(estadisticas)
                if not perfil == None:
                    iniciar_juego(perfil)
            case "2":
                pausar_y_limpiar()
                perfil = seleccionar_perfil(estadisticas)
                if not perfil == None:
                    iniciar_juego(perfil)
            case "3":
                salir = True
            case _:
                print("❌ Opción inválida.")

###################################################################################################

import pygame
from modulos.py_game.funciones_pygame import *
from modulos.configuracion import *
from modulos.menus.mostrar_menu import *
from modulos.py_game.botones import *

def menu_juego():
    pygame.init()
    pygame.mixer.init()

    fondo = cargar_imagen("recursos/fondo.jpg")
    icono_juego = cargar_imagen("recursos/icono_menu.png")
    coordenadas_icono = [140,30]
    mostrar_imagen(fondo, LONGITUD_PANTALLA, (0,0))
    mostrar_imagen(icono_juego, LONGITUD_PANTALLA, coordenadas_icono)
    
    opciones = ["Registrar nuevo usuario", "Seleccionar perfil", "Volver al menu"]
    lista_opciones = crear_botones_opciones(opciones, LONGITUD_PANTALLA, (50,40), fuente_texto, (400,250), 10)

    animacion_menu = False
    fin_animacion = False
    bucle_menu = True
    
    while bucle_menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bucle_menu = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for boton in lista_opciones:
                    if boton["rectangulo"].collidepoint(event.pos):
                        boton["presionado"] = True

        if animacion_menu == False and fin_animacion == False:
            fin_animacion = animar_imagen(LONGITUD_PANTALLA, fondo, icono_juego, coordenadas_icono, (-50,140), 2)
        
        if fin_animacion:
            dibujar_lista_botones(lista_opciones)

        for boton in lista_opciones:
            if boton["texto"] == "Volver al menu":
                if boton["presionado"] == True:
                    bucle_menu = False
                    boton["presionado"] = False   

        pygame.display.update()

    
    
    