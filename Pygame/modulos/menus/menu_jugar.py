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

def menu_juego(estadisticas_usuario):
    pygame.init()

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
            mostrar_imagen(fondo, LONGITUD_PANTALLA, (0,0))
            mostrar_imagen(icono_juego, LONGITUD_PANTALLA, (-50,140))
            dibujar_lista_botones(lista_opciones)

        for boton in lista_opciones:

            if boton["texto"] == "Registrar nuevo usuario":
                if boton["presionado"] == True:
                    usuario = crear_perfil_usuario(estadisticas_usuario)
                    boton["presionado"] = False 

            elif boton["texto"] == "Seleccionar perfil":
                if boton["presionado"] == True:
                    usuario = seleccionar_perfil_usuario(estadisticas_usuario)
                    boton["presionado"] = False 

            elif boton["texto"] == "Volver al menu":
                if boton["presionado"] == True:
                    bucle_menu = False
                    boton["presionado"] = False   

        pygame.display.update()


def crear_perfil_usuario(estadisticas:dict):

    pygame.init()
    color_blanco = (255,255,255)
    color_rojo = (100,0,0)
    fondo = cargar_imagen("recursos/fondo.jpg")
    fuente_mensaje = pygame.font.Font(None, 30)
    pos_mensaje = (220,50)
    mensaje_seleccion = fuente_mensaje.render("Ingrese nombre de nuevo usuario", True, color_blanco)
    mensaje_error = fuente_mensaje.render("Usuario existente", True, color_rojo)
    mostrar_imagen(fondo, LONGITUD_PANTALLA, (0,0))

    volver_atras = crear_boton((50,100), (300,550), LONGITUD_PANTALLA, None, None, fuente_texto, "Volver atras")
    input_usuario = crear_input(LONGITUD_PANTALLA, fuente_texto, color_blanco, color_blanco, (280,300), (200,32))

    error = False
    bucle_menu = True

    while bucle_menu:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                bucle_menu = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if volver_atras["rectangulo"].collidepoint(event.pos):
                        volver_atras["presionado"] = True

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    # Verificamos si existe el usuario cuando toca enter
                    nombre_usuario = input_usuario["texto"].strip()

                    existe = False
                    for clave in estadisticas:
                        if clave == nombre_usuario:
                            existe = True
                            break
                    
                    if existe:
                        error = True
                        input_usuario["texto"] = ""
                        print(input_usuario)

                    else:
                        bucle_menu = False
                        return nombre_usuario

                escribir(input_usuario, event)


        mostrar_imagen(fondo, LONGITUD_PANTALLA, (0,0))  
        LONGITUD_PANTALLA.blit(mensaje_seleccion, pos_mensaje)
        dibujar_input(input_usuario)
        dibujar_boton(volver_atras)
        
        if error:
            LONGITUD_PANTALLA.blit(mensaje_error, (300,280))

        if volver_atras["presionado"]:
            volver_atras["presionado"] = False
            bucle_menu = False

        pygame.display.update()


def seleccionar_perfil_usuario(estadisticas:dict):
    pygame.init()
    color_blanco = (255,255,255)
    fondo = cargar_imagen("recursos/fondo.jpg")
    mostrar_imagen(fondo, LONGITUD_PANTALLA, (0,0))
    fuente_mensaje = pygame.font.Font(None, 30)
    pos_mensaje = (280,50)
    mensaje_seleccion = fuente_mensaje.render("Seleccione usuario", True, color_blanco)
    mensaje_error = fuente_mensaje.render("No existen usuarios", True, color_blanco)

    volver_atras = crear_boton((50,100), (300,550), LONGITUD_PANTALLA, None, None, fuente_texto, "Volver atras")

    bucle_menu = True

    while bucle_menu:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    bucle_menu = False
                    pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if volver_atras["rectangulo"].collidepoint(event.pos):
                        volver_atras["presionado"] = True

        if len(estadisticas) == 0:
            mostrar_imagen(fondo, LONGITUD_PANTALLA, (0,0))  
            LONGITUD_PANTALLA.blit(mensaje_error, pos_mensaje)

        else:
            mostrar_imagen(fondo, LONGITUD_PANTALLA, (0,0))
            LONGITUD_PANTALLA.blit(mensaje_seleccion, pos_mensaje)

            lista_usuarios = []
            for clave in estadisticas:
                lista_usuarios.append(clave)
                lista_botones = crear_botones_opciones(lista_usuarios, LONGITUD_PANTALLA, (50,40), fuente_texto, (320,100), 10)

            dibujar_lista_botones(lista_botones)

        dibujar_boton(volver_atras)
        if volver_atras["presionado"]:
            volver_atras["presionado"] = False
            bucle_menu = False

        pygame.display.update()