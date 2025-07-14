import pygame
from archivos.archivo_txt import * 
from modulos.py_game.funciones_pygame import *
from modulos.py_game.botones import *
from modulos.configuracion import ANCHO_PANTALLA, ALTO_PANTALLA, LONGITUD_PANTALLA

def menu_reglas():
    pygame.init()
    fuente_texto = ("Segoe UI Emoji", 20)

    fondo = cargar_imagen("recursos/fondo.jpg")
    icono_juego = cargar_imagen("recursos/icono_menu.png")
    coordenadas_icono = [140,30]

    color_negro = (0, 0, 0)
    color_blanco = (255, 255, 255)
    reglas = cargar_texto_desde_archivo("archivos/txt/reglas.txt") # devuelve un str

    mostrar_imagen(fondo, LONGITUD_PANTALLA, (0,0))
    mostrar_imagen(icono_juego, LONGITUD_PANTALLA, coordenadas_icono)
    boton_salir = crear_boton((50,150), (200,550), LONGITUD_PANTALLA, None, None, fuente_texto, 
                              "Toque cualquer boton para volver al menu")
    
    overlay = pygame.Surface((ANCHO_PANTALLA, ALTO_PANTALLA))
    overlay.set_alpha(120)      # | 0 = totalmente transparente | 255 = opaco |
    overlay.fill(color_negro)     # | Negro |

    desplazamiento_rueda_raton = 0
    animacion_finalizada = False
    bandera_menu = True

    while bandera_menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bandera_menu = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                bandera_menu = False

            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:             # event.y = +1: rueda arriba
                    desplazamiento_rueda_raton += 20     # Desplazar hacia abajo
                elif event.y < 0:           # event.y = -1: rueda abajo
                    desplazamiento_rueda_raton -= 20     # Desplazar hacia arriba

        if animacion_finalizada == False:
            animacion_finalizada = animar_imagen(LONGITUD_PANTALLA, fondo, icono_juego, coordenadas_icono, (140,-300), 2)

        if animacion_finalizada:
            mostrar_imagen(fondo, LONGITUD_PANTALLA, (0,0))
            LONGITUD_PANTALLA.blit(overlay, (0, 0))
            mostrar_texto(LONGITUD_PANTALLA, reglas, fuente_texto, color_blanco, 50, (50,100), desplazamiento_rueda_raton)
            dibujar_boton(boton_salir)
            
        
        pygame.display.update()

    
        