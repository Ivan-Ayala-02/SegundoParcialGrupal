from modulos.menus.mostrar_menu import mostrar_menu_extras
from modulos.mini_juegos.mini_juegos import minijuego_buscaminas
from modulos.configuracion import diccionario_datos_tablero
from modulos.mini_juegos.utilidades_mini_juegos import ingresar_longitud_tablero, ingresar_cantidad_minas

def menu_extras():
    salir = False

    while not salir:
        opcion = mostrar_menu_extras()

        match opcion:
            case "1":
                filas, columnas = ingresar_longitud_tablero()
                minas = ingresar_cantidad_minas(filas, columnas)
                minijuego_buscaminas(filas, columnas, minas, diccionario_datos_tablero)
            
            case "2":
                salir = True
                
            case _:
                print("❌ Opción inválida.")