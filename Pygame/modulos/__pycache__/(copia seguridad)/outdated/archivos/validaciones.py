def validar_caracter_dentro_rango(numero:int, rango_minimo:int, rango_maximo:int) -> bool:
    numero_validado = False
    if numero >= rango_minimo and numero <= rango_maximo:
        numero_validado = True
    return numero_validado

def validar_tipo_input(input_ingresado:int|str, tipo_validacion:str) -> int|str|None:
    cantidad_caracteres = len(input_ingresado)
    cadena_convertida = ""

    if tipo_validacion == "cadena":
        # rango caracteres mayusculas: 65-90
        # rango caracteres mayusculas: 97-122

        for i in range(cantidad_caracteres):
            caracter = input_ingresado[i]
            orden_caracter = ord(caracter) # ord: devuelve numero de caracter ascii
            caracter_mayuscula = validar_caracter_dentro_rango(orden_caracter, 65, 90)
            caracter_minuscula = validar_caracter_dentro_rango(orden_caracter, 97, 122)

            if caracter_mayuscula == True or caracter_minuscula == True:
                cadena_convertida += caracter
    
    return cadena_convertida
            