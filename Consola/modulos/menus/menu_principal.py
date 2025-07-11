from os import system
from modulos.utilidades import pausar_y_limpiar

from modulos.menus.mostrar_menu import mostrar_reglas 
from modulos.menus.mostrar_menu import mostrar_menu_principal

from modulos.menus.menu_jugar import menu_jugar
from modulos.menus.menu_estadisticas import menu_estadisticas

from archivos.archivo_json import cargar_datos_json 
from archivos.archivo_txt import cargar_texto_desde_archivo

def main():
    en_ejecucion = True
    
    estadisticas = cargar_datos_json("archivos/json/estadisticas.json")
    reglas = cargar_texto_desde_archivo("archivos/txt/reglas.txt")
    
    while en_ejecucion:
        system("cls")    # Limpia la pantalla
        opcion = mostrar_menu_principal()

        match opcion:
            case "1":
                pausar_y_limpiar()
                menu_jugar(estadisticas)
            case "2":
                pausar_y_limpiar()
                menu_estadisticas(estadisticas)
            case "3":
                pausar_y_limpiar()
                mostrar_reglas(reglas)
                pausar_y_limpiar()
            case "4":
                print("\n¡Gracias por jugar!\n")
                en_ejecucion = False
            case _:
                print("\n❌ Opción inválida ❌")
                pausar_y_limpiar()