import random
from datos import datos_juegos
from auxiliares import *


def jugar_si_o_no(lista_preguntas: list, estado_jugador: dict):
    if len(lista_preguntas) == 0:
        print("No hay más preguntas disponibles.")
        return False

    respuesta_de_usuario = False

    while not respuesta_de_usuario and len(lista_preguntas) > 0:
        datos_pregunta = random.choice(lista_preguntas)
        lista_preguntas.remove(datos_pregunta)

        pregunta = datos_pregunta["pregunta"]
        respuesta = datos_pregunta["respuesta"]
        categoria = datos_pregunta["categoria"]
        dificultad = datos_pregunta["dificultad"]

        print(f"\nCategoría: {categoria} | Dificultad: {dificultad}")
        print(f"Pregunta: {pregunta}")

        # Queda en no porque si no no toma el resultado.
        usar_ficha = "no"

        if estado_jugador["fichas"] > 0:
            print("¿Querés usar una ficha para cambiar esta pregunta?")
            usar_ficha = pedir_respuesta_si_o_no()

        if usar_ficha == "si":
            estado_jugador["fichas"] -= 1
            print(f"Usaste una ficha. Te quedan {estado_jugador['fichas']} fichas.")
        else:
            respuesta_usuario = pedir_respuesta_si_o_no()
            if comparar_respuestas(respuesta_usuario, respuesta):
                print("¡Correcto! Avanzaste.")
                respuesta_de_usuario = True
                resultado = True
            else:
                print(f"❌ Incorrecto ❌\nLa respuesta era: {respuesta}")
                respuesta_de_usuario = True
                resultado = False

    return resultado

def jugar_completar_oracion(lista_oraciones: list, estado_jugador: dict):
    # lista_oraciones = obtener_preguntas(datos_juegos, "completar_oracion")
    if len(lista_oraciones) == 0:
        print("No hay más oraciones disponibles para completar.")
        return False
    
    respuesta_de_usuario = False

    while not respuesta_de_usuario and len(lista_oraciones) > 0:
        datos_oracion = random.choice(lista_oraciones)
        lista_oraciones.remove(datos_oracion)

        oracion = datos_oracion["oracion"]
        respuesta = datos_oracion["respuesta"]
        categoria = datos_oracion['categoria']
        dificultad = datos_oracion['dificultad']

        print(f"\nCategoría: {categoria} | Dificultad: {dificultad}")
        print(f"Oración: {oracion}")    
        # Queda en no porque si no no toma el resultado.
        usar_ficha = "no"


        if estado_jugador["fichas"] > 0:
            print("¿Querés usar una ficha para cambiar esta pregunta?")
            usar_ficha = pedir_respuesta_si_o_no()

        if usar_ficha == "si":
            estado_jugador["fichas"] -= 1
            print(f"Usaste una ficha. Te quedan {estado_jugador['fichas']} fichas.")
        else:
            respuesta_usuario = input("Completar la oración con la palabra faltante: ").strip()
            if comparar_respuestas(respuesta_usuario, respuesta):
                print("¡Correcto! Avanzaste.")
                respuesta_de_usuario = True
                resultado = True
            else:
                print(f"❌ Incorrecto ❌\nLa respuesta era: {respuesta}")
                respuesta_de_usuario = True
                resultado = False

    return resultado

def jugar_completar_palabra(lista_palabras: list, estado_jugador: dict):
    #lista_palabras = obtener_preguntas(datos_juegos, "completar_palabra")
    if len(lista_palabras) == 0:
        print("No hay más palabras disponibles para completar.")
        return False
    
    respuesta_de_usuario = False

    while not respuesta_de_usuario and len(lista_palabras) > 0:
        # Seleccionar una palabra aleatoria
        datos_palabra = random.choice(lista_palabras)
        lista_palabras.remove(datos_palabra)
        
        palabra = datos_palabra["palabra"]
        respuesta = datos_palabra["respuesta"]
        pista = datos_palabra["pista"]
        
        print(f"\n--- Completa la palabra ---")
        print(f"Palabra: {palabra}")
        print(f"Pista: {pista}")

        # Queda en no porque si no no toma el resultado.
        usar_ficha = "no"

        if estado_jugador["fichas"] > 0:
            print("¿Querés usar una ficha para cambiar esta pregunta?")
            usar_ficha = pedir_respuesta_si_o_no()

        if usar_ficha == "si":
            estado_jugador["fichas"] -= 1
            print(f"Usaste una ficha. Te quedan {estado_jugador['fichas']} fichas.")
        else:
            respuesta_usuario = pedir_respuesta_completar_palabra()
            if comparar_respuestas(respuesta_usuario, respuesta):
                print("¡Correcto! Avanzaste.")
                respuesta_de_usuario = True
                resultado = True
            else:
                print(f"❌ Incorrecto ❌\nLa respuesta era: {respuesta}")
                respuesta_de_usuario = True
                resultado = False

    return resultado



"""def jugar_si_o_no(lista_preguntas: list):
    # Obtiene las preguntas de Si o No.
    # lista_preguntas = obtener_preguntas(datos_juegos, "si_o_no")
    # Seleccionar pregunta aleatoria
    datos_pregunta = random.choice(lista_preguntas)
    lista_preguntas.remove(datos_pregunta)

    pregunta = datos_pregunta["pregunta"]
    respuesta = datos_pregunta["respuesta"]
    categoria = datos_pregunta['categoria']
    dificultad = datos_pregunta['dificultad']

    # Mostrar pregunta.
    print(f"\nCategoría: {categoria} | Dificultad: {dificultad}")
    print(f"Pregunta: {pregunta}")

    # Respuesta del Usuario.
    respuesta_usuario = pedir_respuesta_si_o_no()
    # Validar respuesta
    if comparar_respuestas(respuesta_usuario, respuesta):
        print("¡Correcto! Avanzaste.")
        estado = True
    else:
        print(f"❌ Incorrecto ❌\nLa respuesta era: {respuesta}")
        estado = False

    return estado

def jugar_completar_oracion(lista_oraciones: list):
    # lista_oraciones = obtener_preguntas(datos_juegos, "completar_oracion")

    datos_oracion = random.choice(lista_oraciones)
    lista_oraciones.remove(datos_oracion)

    oracion = datos_oracion["oracion"]
    respuesta = datos_oracion["respuesta"]
    categoria = datos_oracion['categoria']
    dificultad = datos_oracion['dificultad']

    print(f"\nCategoría: {categoria} | Dificultad: {dificultad}")
    print(f"Oración: {oracion}")    

    respuesta_usuario = input("Completar la oración con la palabra faltante: ").strip().upper()
        
    if comparar_respuestas(respuesta_usuario, respuesta):
        print("¡Correcto! Avanzaste.")
        estado = True
    else:
        print(f"❌ Incorrecto ❌\nLa respuesta era: {respuesta}\n")
        estado = False

    return estado

def jugar_completar_palabra(lista_palabras: list):
    #lista_palabras = obtener_preguntas(datos_juegos, "completar_palabra")
    # Seleccionar una palabra aleatoria
    datos_palabra = random.choice(lista_palabras)
    lista_palabras.remove(datos_palabra)
    
    palabra = datos_palabra["palabra"]
    respuesta = datos_palabra["respuesta"]
    pista = datos_palabra["pista"]
    
    print(f"\n--- Completa la palabra ---")
    print(f"Palabra: {palabra}")
    print(f"Pista: {pista}")

    respuesta_usuario = pedir_respuesta_completar_palabra()
    
    if comparar_respuestas(respuesta_usuario, respuesta):
        print("¡Correcto! Avanzaste")
        estado = True
    else:
        print(f"❌ Incorrecto ❌\nLa respuesta era: {respuesta}")
        estado = False

    return estado
"""










"""
import random
from datos import datos_juegos
from auxiliares import *

def jugar_si_o_no(datos_juegos: dict):
    # Obtiene las preguntas de Si o No.
    lista_preguntas = obtener_preguntas(datos_juegos, "si_o_no")
    # Seleccionar pregunta aleatoria
    datos_pregunta = random.choice(lista_preguntas)

    pregunta = datos_pregunta["pregunta"]
    respuesta = datos_pregunta["respuesta"]
    categoria = datos_pregunta['categoria']
    dificultad = datos_pregunta['dificultad']

    # Mostrar pregunta.
    print(f"\nCategoría: {categoria} | Dificultad: {dificultad}")
    print(f"Pregunta: {pregunta}")

    # Respuesta del Usuario.
    respuesta_usuario = pedir_respuesta_si_o_no()
    # Validar respuesta
    if respuesta_usuario == respuesta:
        print("¡Correcto! Avanzaste.")
        estado = True
    else:
        print(f"❌ Incorrecto ❌\nLa respuesta era: {respuesta}")
        estado = False

    return estado

def jugar_completar_oracion(datos_juegos: dict):
    lista_oraciones = obtener_preguntas(datos_juegos, "completar_oracion")

    datos_oracion = random.choice(lista_oraciones)

    oracion = datos_oracion["oracion"]
    respuesta = datos_oracion["respuesta"]
    categoria = datos_oracion['categoria']
    dificultad = datos_oracion['dificultad']

    print(f"\nCategoría: {categoria} | Dificultad: {dificultad}")
    print(f"Oración: {oracion}")    

    respuesta_usuario = input("Tu respuesta: ").strip().upper()
        
    if respuesta_usuario == respuesta:
        print("¡Correcto! Avanzaste.")
        estado = True
    else:
        print(f"❌ Incorrecto ❌\nLa respuesta era: {respuesta}\n")
        estado = False

    return estado

def jugar_completar_palabra(datos_juegos: dict):
    lista_palabras = obtener_preguntas(datos_juegos, "completar_palabra")
    # Seleccionar una palabra aleatoria
    datos_palabra = random.choice(lista_palabras)
    
    palabra = datos_palabra["palabra"]
    respuesta = datos_palabra["respuesta"]
    pista = datos_palabra["pista"]
    
    print(f"\n--- Completa la palabra ---")
    print(f"Palabra: {palabra}")
    print(f"Pista: {pista}")

    respuesta_usuario = pedir_respuesta_completar_palabra()
    
    if respuesta_usuario == respuesta:
        print("¡Correcto! Avanzaste")
        estado = True
    else:
        print(f"❌ Incorrecto ❌\nLa respuesta era: {respuesta}")
        estado = False

    return estado"""

"""jugar_si_o_no,LISTO
    jugar_completar_oracion,LISTO
    jugar_completar_palabra,LISTO

    jugar_pregunta_respuesta, PENDIENTE
    jugar_letra_cancion: PENDIENTE
"""