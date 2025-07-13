from juego import iniciar_juego

def mostrar_menu():
    print("==== ¡AHORA CAIGO! ====")
    print("1. Jugar")
    print("2. Salir")
    opcion = input("Elegí una opción: ")
    return opcion

def main():
    salir = False
    while not salir:
        opcion = mostrar_menu()
        if opcion == "1":
            iniciar_juego()
        elif opcion == "2":
            print("¡Hasta luego!")
            salir = True
        else:
            print("Opción inválida.")