# ver categorias

'''for categorias in lista_juego:
    print(categorias["categoria"])'''

# ver dificultades dentro de las categorias

'''for categorias in lista_juego:
    print(categorias["categoria"])

    for dificultades in categorias["lista_dificultades"]:
        print(dificultades["dificultad"])'''

# acceder al diccionario con preguntas
from preguntas import lista_juego
from funciones_genericas import *

for diccionarios in lista_juego:
    print(f"\n---{diccionarios["categoria"]}---\n")

    for dificultades in diccionarios["lista_dificultades"]:
        mostrar_elemento_en_diccionario(dificultades, "dificultad")

        for preguntas in dificultades["lista_preguntas"]:
            mostrar_elemento_en_diccionario(preguntas, "enunciado")
            mostrar_elementos_lista(preguntas["opciones"])
        
            print()



