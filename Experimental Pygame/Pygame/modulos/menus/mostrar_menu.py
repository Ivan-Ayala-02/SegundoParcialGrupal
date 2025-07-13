from modulos.impresiones import imprimir_string_recuadro
from modulos.py_game.funciones_pygame import *

def mostrar_menu_principal():
    print()
    imprimir_string_recuadro("MENÚ: PRINCIPAL", 3)
    print()
    print("1) Jugar")
    print("2) Estadísticas")
    print("3) Reglas del Juego")
    print("4) Extras")
    print("5) Salir")
    print()
    opcion = input("Elegí una opción: ").strip()

    return opcion

def mostrar_menu_jugar():
    print()
    imprimir_string_recuadro("MENÚ: JUGAR", 3)
    print()
    print("1) Registrar un nuevo usuario e iniciar partida")
    print("2) Seleccionar perfil existente")
    print("3) Volver al menú principal")
    print()
    opcion = input("Elegí una opción: ").strip()
    
    return opcion

def mostrar_menu_estadisticas():
    print()
    imprimir_string_recuadro("MENÚ DE ESTADÍSTICAS", 3)
    print()
    print("1) Ver pregunta más fallada")
    print("2) Ver porcentaje de aciertos")
    print("3) Ver mejor partida")
    print("4) Volver al menú principal")
    print()
    opcion = input("Elegí una opción: ").strip()

    return opcion

def mostrar_menu_extras():
    print()
    imprimir_string_recuadro("MENÚ DE EXTRAS", 3)
    print()
    print("1) Jugar buscaminas")
    print("2) Volver al menú principal")
    print()
    opcion = input("Elegí una opción: ").strip()

    return opcion

def mostrar_reglas(texto: str):
    print(texto)

#---------------------------------------------------------------------------------------------------

def cargar_imagenes_intro():
    fondo = cargar_imagen("recursos/fondo.jpg")
    logo_juego = cargar_imagen("recursos/icono_menu.png")
    barassi = cargar_imagen("recursos/barassi_menu.png")
    return fondo, logo_juego, barassi

def mostrar_imagenes_intro(fondo, pantalla, logo, coord_logo, barassi, coord_barassi):
    mostrar_imagen(fondo, pantalla, (0,0))
    mostrar_imagen(logo, pantalla, coord_logo)
    mostrar_imagen(barassi, pantalla, coord_barassi)

def animar_intro(PANTALLA, fondo, logo_juego, coordenadas_logo):

    animacion_finalizada = mover_imagen(coordenadas_logo, (140,30), 2)
    mostrar_imagen(fondo, PANTALLA, (0,0))
    mostrar_imagen(logo_juego, PANTALLA, coordenadas_logo)

    if animacion_finalizada:
        return True
    else:
        return False