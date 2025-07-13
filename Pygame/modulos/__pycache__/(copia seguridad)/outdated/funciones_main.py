from archivos.preguntas import lista_juego
from archivos.funciones_genericas import *
from archivos.validaciones import *

def ingresar_opcion(tipo_opcion:str) -> str|int:
    
    opcion = input("Ingrese la opcion a elegir: ")
    
    if tipo_opcion == "cadena" or tipo_opcion == "numerica":
        opcion = validar_tipo_input(opcion, tipo_opcion)
    else:
        opcion = ""

    while opcion == "":
        opcion = input("[ERROR] Ingrese la opcion a elegir: ")
        if tipo_opcion == "cadena" or tipo_opcion == "numerica":
            opcion = validar_tipo_input(opcion, tipo_opcion)
        else:
            opcion = ""

    return opcion

def elegir_categoria(ingreso:str, lista_principal:list = None):

    if ingreso == "manual":
        categoria = ingresar_opcion("cadena")

        for diccionario_categorias in lista_principal:
            categoria_elegida = buscar_elemento_en_diccionario(categoria, diccionario_categorias)
            if categoria_elegida != None:
                categoria_elegida = buscar_elemento_en_diccionario(categoria, diccionario_categorias)

    elif ingreso == "aleatoria":
        cantidad_categorias = len(lista_juego)
        categoria_aleatoria = generar_numero_aleatorio(0, cantidad_categorias)
        categoria_elegida = ""

        for i in range(cantidad_categorias):
            
            if lista_juego[i]["categoria"] == lista_juego[categoria_aleatoria]["categoria"]:
                categoria_elegida = lista_juego[i]["categoria"]
                break
    
    return categoria_elegida