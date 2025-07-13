import random

def buscar_elemento_en_diccionario(elemento_a_buscar:str|int, diccionario:dict) -> any:
    retorno_elemento = None

    for elemento in diccionario:
        if elemento == elemento_a_buscar:
            retorno_elemento = elemento

    return retorno_elemento

def mostrar_elemento_en_diccionario(diccionario:dict, elemento:str|int):
    print(diccionario[elemento])

def mostrar_elementos_lista(lista:list):
    for elemeneto in lista:
        print(elemeneto)

def generar_numero_aleatorio(rango_inicio:int = 0, rango_final:int = None) -> int|None:
    numero = None
    if rango_final != None:
        numero = random.randint(rango_inicio, rango_final)
    return numero

def buscar_elemento_en_lista(elemento, lista):
    cantidad_elementos = len(lista)
    for i in range(cantidad_elementos):
        pass