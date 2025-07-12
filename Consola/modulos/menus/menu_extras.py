from modulos.menus.mostrar_menu import mostrar_menu_extras

from modulos.mini_juegos.mini_juegos import minijuego_buscaminas
from modulos.configuracion import diccionario_datos_tablero

def menu_extras():
    salir = False

    while not salir:
        opcion = mostrar_menu_extras()

        match opcion:
            case "1":
                minijuego_buscaminas(5,5,1, diccionario_datos_tablero)
            
            case "2":
                salir = True
                
            case _:
                print("❌ Opción inválida.")