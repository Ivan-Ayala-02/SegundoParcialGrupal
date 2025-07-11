from modulos.utilidades import pausar_y_limpiar
from modulos.menus.mostrar_menu import mostrar_menu_estadisticas
from modulos.estadisticas import *

def menu_estadisticas(estadisticas: dict):
    usuario = seleccionar_perfil_estadisticas(estadisticas)
    if usuario == None:
        print("⚠️ No hay perfiles registrados.")
    else:
        salir = False
        while not salir:
            opcion = mostrar_menu_estadisticas()

            match opcion:
                case "1":
                    mostrar_preguntas_falladas_sin_repetir(estadisticas, "valentin")
                    pausar_y_limpiar()

                case "2":
                    mostrar_porcentaje_aciertos(estadisticas, usuario)
                    pausar_y_limpiar()

                case "3":
                    mostrar_mejor_partida(estadisticas, usuario)
                    pausar_y_limpiar()

                case "4":
                    salir = True

                case _:
                    print("❌ Opción inválida.")