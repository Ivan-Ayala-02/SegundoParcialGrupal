import random

from premios import *
from general import *
from auxiliares import *

def iniciar_juego():
    print("Bienvenido a ¡Ahora Caigo Versión Consola!")

    nombre_usuario = pedir_nombre_jugador()
    datos_usuario = {}
    estado_jugador = estado_inicial.copy()

    preguntas_disponibles = copiar_diccionario_con_listas(preguntas)
    premios_disponibles = copiar_diccionario_con_listas(premios)
    tipos_restantes = tipos_de_juegos.copy()

    vida = estado_jugador["vida"] 
    fichas = estado_jugador["fichas"] 
    puntos = estado_jugador["puntos"]
    
    rondas = 9

    tipo_actual = None

    for ronda in range(rondas):

        if (ronda) % 3 == 0:
            tipo_actual = elegir_nuevo_tipo(tipos_restantes)

        mostrar_info_ronda(ronda, tipo_actual)
        acierto = False

        while not acierto and vida != 0:
            datos = preguntas_disponibles[tipo_actual]
            resultado = funciones_juegos[tipo_actual](datos, estado_jugador)

            if resultado:
                print(f"Ganaste la ronda.")
                premios_para_elegir = obtener_premios(premios_disponibles)
                    
                # PREMIOS
                if premios_para_elegir == None:
                    print("No hay más premios para elegir.")
                else:
                    premio = elegir_zapato(premios_para_elegir)
                    vida, puntos = actualizar_estado_por_premio(premio, vida, puntos)
                    
                acierto = True
            elif fichas > 0:
                print(f"Respuesta incorrecta.")
                print(f"Tienes {fichas} ficha(s). ¿Querés usar una para pasar a otra pregunta?")
                usar = pedir_respuesta_si_o_no()  # Función tuya que valida "si" o "no"

                if usar == "si":
                    fichas -= 1
                    print(f"Usaste una ficha. Te quedan {fichas}. Pasando a otra pregunta...\n")
                else:
                    vida -= 1
                    print(f"No usaste ficha. Perdés una vida. Te quedan {vida} vida(s).\n")
            else:
                vida -= 1

        
        if vida == 0:
            print("Perdiste el Juego!")
            puntos = 0
            break
        elif ronda + 1 == rondas:
            print("¡Ganaste el Juego!")

    datos_usuario = estado_jugador.copy()
    datos_usuario["Nombre"] = nombre_usuario
    print(datos_usuario)