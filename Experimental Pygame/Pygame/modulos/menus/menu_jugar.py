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