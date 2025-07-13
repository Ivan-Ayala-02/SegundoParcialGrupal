from datos import *
from auxiliares import *

# ----------------------------------------------------------------------------------------------------------

# Funcion Principal

def jugar_preguntas_y_respuestas(diccionario_principal, minijuego):
    
    diccionario_datos_pregunta = elegir_elemento_aleatorio_diccionario(diccionario_principal, minijuego)
    pregunta = buscar_elemento_diccionario(diccionario_datos_pregunta, "pregunta")
    lista_opciones = buscar_elemento_diccionario(diccionario_datos_pregunta, "opciones")
    mensaje_ingreso_opcion = "Ingrese una opcion por consola: "
    respuesta = buscar_elemento_diccionario(diccionario_datos_pregunta, "respuesta")
    
    print(f"{pregunta}\n")
    mostrar_elementos_lista(lista_opciones)
    print()
    opcion_ingresada = ingreso_y_verificacion_cadena(mensaje_ingreso_opcion, letras=True, numeros=True, espceiales=True)
    verificar_respuesta = verificar_dos_elementos(opcion_ingresada, respuesta)
    if verificar_respuesta:
        print("Correcto! Avanzaste")
        estado = True
    elif verificar_respuesta == False:
        print(f"Mal!\nLa respuesta era: {respuesta}")
        estado = False
    return estado
    
def jugar_letra_cancion(diccionario_principal:dict, minijuego:str):

    diccionario_datos_letra_cancion = elegir_elemento_aleatorio_diccionario(diccionario_principal, minijuego)
    letra_cancion = buscar_elemento_diccionario(diccionario_datos_letra_cancion, "letra")
    respuesta = buscar_elemento_diccionario(diccionario_datos_letra_cancion, "respuesta")
    mensaje_ingreso = "Complete la oracion: "
    mensaje_error = "Ingrese caracteres validos: "

    print(f"{letra_cancion}\n")
    opcion_ingresada = ingreso_y_verificacion_cadena(mensaje_ingreso, mensaje_error, letras=True)     #ingresar_opcion(mensaje_ingreso, mensaje_error)
    verificar_respuesta = verificar_dos_elementos(respuesta, opcion_ingresada)
    if verificar_respuesta:
        print("Correcto! Avanzaste")
        estado = True
    elif verificar_respuesta == False:
        print(f"Mal!\nLa respuesta era: {respuesta}")
        estado = False
    return estado