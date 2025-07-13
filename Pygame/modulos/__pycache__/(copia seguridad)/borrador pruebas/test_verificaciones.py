from files.auxiliares import *

def verifica_cadena(cadena:str, caracteres_especiales:str=None) -> bool:
    verificacion = True

    for i in range(len(cadena)):
        caracter = cadena[i]
        orden_caracter = ord(caracter)
        
        caracteres_letras = verificar_caracter_letra(orden_caracter)
        caracteres_numericos = verificar_caracter_numerico(orden_caracter)
        if caracteres_especiales == None:
            cadena_caracteres_especiales = "., "
        caracteres_especiales = verifica_caracter_especial(orden_caracter, cadena_caracteres_especiales) 

        if caracteres_letras == False and caracteres_numericos == False and caracteres_especiales == False:
            verificacion = False
            break
        
    return verificacion