from os import system
from modulos.utilidades import pausar_y_limpiar

from modulos.menus.mostrar_menu import mostrar_reglas 
from modulos.menus.mostrar_menu import mostrar_menu_principal
from modulos.menus.menu_jugar import menu_jugar, menu_juego
from modulos.menus.menu_estadisticas import menu_estadisticas
from modulos.menus.menu_extras import menu_extras
from modulos.menus.menu_reglas import menu_reglas

from archivos.archivo_json import cargar_datos_json 
from archivos.archivo_txt import cargar_texto_desde_archivo

'''def main():
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
                pausar_y_limpiar()
                menu_extras()
            case "5":
                print("\n¡Gracias por jugar!\n")
                en_ejecucion = False
            case _:
                print("\n❌ Opción inválida ❌")
                pausar_y_limpiar()'''

#------------------------------------------------------------------------------

from modulos.configuracion import *
from modulos.py_game.botones import *

def menu_principal(estadisticas_usuario):
    pygame.init()
    pygame.mixer.init()

    coordenadas_logo = [320,30]
    coordenadas_barassi = [-50,70]

    fondo, logo_juego, barassi = cargar_imagenes_intro()
    mostrar_imagenes_intro(fondo, LONGITUD_PANTALLA, logo_juego, coordenadas_logo, barassi, coordenadas_barassi)
    generar_nombre_e_icono_ventana("¡AHORA CAIGO!", "recursos/zapatillas.png")

    cargar_audio("recursos/musica_menu.wav")
    ajustar_volumen(0.3)

    boton_inicio = crear_boton((50,40), (150,500), LONGITUD_PANTALLA, None, None, fuente_texto, "Toque cualquier boton para empezar")

    lista_opciones = ["Jugar", "Reglas", "Estadisticas", "Extras", "Salir"]
    lista_botones = crear_botones_opciones(lista_opciones, LONGITUD_PANTALLA, (50,40), fuente_texto, (320,310), 10)

    bucle_intro =True
    musica_menu = False
    animacion_intro = False
    ingreso_menu_principal = False
    estado_animacion = False

    while bucle_intro:

        if musica_menu == False:
            pygame.mixer.music.play(-1) # Reproduce en bucle infinito
            musica_menu = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bucle_intro = False
            
            if event.type == pygame.KEYDOWN:
                if animacion_intro == False and ingreso_menu_principal == False:
                    animacion_intro = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                for boton in lista_botones:
                    if boton["rectangulo"].collidepoint(event.pos):
                        boton["presionado"] = True
        
        if boton_inicio["presionado"] == False:
            dibujar_boton(boton_inicio)
            boton_inicio["presionado"] = True

        if animacion_intro:
            estado_animacion = animar_imagen(LONGITUD_PANTALLA, fondo, logo_juego, coordenadas_logo, (140,30), 2)

        if estado_animacion:
            animacion_intro = False
            ingreso_menu_principal = True

        if ingreso_menu_principal:
            mostrar_imagen(fondo, LONGITUD_PANTALLA, (0,0))
            mostrar_imagen(logo_juego, LONGITUD_PANTALLA, (140,30))
            dibujar_lista_botones(lista_botones)

        for boton in lista_botones:
            
            if boton["texto"] == "Jugar":
                if boton["presionado"] == True:
                    boton["presionado"] = False
                    menu_juego(estadisticas_usuario)
            
            elif boton["texto"] == "Reglas":
                if boton["presionado"] == True:
                    boton["presionado"] = False
                    menu_reglas()
            
            elif boton["texto"] == "Estadisticas":
                if boton["presionado"] == True:
                    boton["presionado"] = False

            elif boton["texto"] == "Extras":
                if boton["presionado"] == True:
                    boton["presionado"] = False

            elif boton["texto"] == "Salir":
                if boton["presionado"] == True:
                    boton["presionado"] = False
                    bucle_intro = False
            
        pygame.display.update()
    
    pygame.quit()

