# Funciones genericas / auxiliares

def elegir_elemento_aleatorio_diccionario(diccionario:dict, key:str) -> any:
    '''
    Busca dentro de un diccionario, que en su interior tiene una lista con varios elementos,
    y retorna un elemento aleatorio de esa lista.
    
    Args:
        Diccionario principal
        Clave en donde esta ubicada la lista

    Returns:
        Elemento aleatorio dentro de esa lista
    '''
    import random
    elemento_aleatorio = random.choice(diccionario[key])
    return elemento_aleatorio

def buscar_elemento_diccionario(diccionario:dict, elemento_buscar:str|int) -> any:
    '''
    Busca dentro de un diccionario si existe el elemento (clave/key) dentro de 
    un diccionario, si es asi retorna el valor de este.

    Args:
        Diccionario con las diferentes claves y valores
        Elemento/Key a encontrar
    
    Returns:
        Valor de cualquier tipo si es que la key existe
    '''
    elemento_encontrado = None
    for clave, valor in diccionario.items():
        if clave == elemento_buscar:
            elemento_encontrado = valor
            break
    return elemento_encontrado

def mostrar_elementos_lista(lista:list):
    '''
    Recorre una lista e imprime los distintos elementos que hay dentro de ella

    Args:
        Lista con elementos
    '''
    for elementos in lista:
            print(elementos)

def verificar_caracter_mayuscula(orden_caracter:int) -> bool:
    '''
    Ingresa por parametro el orden de caracter unico(Es decir, el numero que le corresponde
    al caracter en la tabla ascii) y verifica que este se encuentre dentro de el rango de
    letras mayusculas.

    Args:
        Ingresa el orden de caracter y verifica que se encuentre dentro de las mayusculas
    
    Returns:
        Retorna un booleano dependiendo de la verificacion
            True: El caracter se encuentra dentro de el rango
            False: El caracter no esta dentro de el rango
    '''
    verificacion = False
    if orden_caracter >= 65 and orden_caracter <= 90:
        verificacion = True
    return verificacion

def verificar_caracter_minuscula(orden_caracter:int) -> bool:
    '''
    Ingresa por parametro el orden de caracter unico(Es decir, el numero que le corresponde
    al caracter en la tabla ascii) y verifica que este se encuentre dentro de el rango de
    letras inusculas.

    Args:
        Ingresa el orden de caracter y verifica que se encuentre dentro de las minusculas
    
    Returns:
        Retorna un booleano dependiendo de la verificacion
            True: El caracter se encuentra dentro de el rango
            False: El caracter no esta dentro de el rango
    '''
    verificacion = False
    if orden_caracter >= 97 and orden_caracter <= 122:
        verificacion = True
    return verificacion

def verificar_caracter_numerico(orden_caracter:int) -> bool:
    '''
    Ingresa por parametro el orden de caracter unico(Es decir, el numero que le corresponde
    al caracter en la tabla ascii) y verifica que este se encuentre dentro de el rango de
    numeros.

    Args:
        Ingresa el orden de caracter y verifica que se encuentre dentro de los numeros
    
    Returns:
        Retorna un booleano dependiendo de la verificacion
            True: El caracter se encuentra dentro de el rango numerico
            False: El caracter no esta dentro de el rango numerico
    '''
    verificacion = False
    if orden_caracter >= 48 and orden_caracter <= 57:
        verificacion = True
    return verificacion

def verificar_caracter_letra(orden_caracter:int) -> bool:
    '''
    Ingresa por parametro un orden de caracter (numero que le corresponde al caracter en la tabla 
    ascii) y verifica que este se encuentre dentro de el rango de letras mayuscula y minuscula.

    Args:
        Ingreso de orden de caracter

    Returns:
    Retorna un booleano segun la verificacion
        True: El orden de caracter se encuentra dentro de el rango de minusculas o mayusculas
        False: El orden de caracter NO se encuentra dentro de ningun rango.
    '''
    verificacion = True
    if verificar_caracter_mayuscula(orden_caracter) == False and verificar_caracter_minuscula(orden_caracter) == False:
        verificacion = False
        return verificacion
    
def verificar_caracter_especial(orden_caracter:int, cadena_caracteres_especiales:str) -> bool:
    '''
    Ingresa por parametro el orden de caracter unico(Es decir, el numero que le corresponde
    al caracter en la tabla ascii) y verifica que este se encuentre dentro de una cadena de caracteres
    especifica.

    Args:
        Ingresa el orden de caracter unico
        Ingresa una cadena con los caracteres a verificar

    Returns:
        Retorna un booleano
            True: Si el caracter existe dentro la cadena de caracteres ingresada por parametro
            False: El caracter no se encuentra dentro de la cadena de caracteres
    '''
    verificacion = False
    for i in range(len(cadena_caracteres_especiales)):
        ord_caracter_especial = ord(cadena_caracteres_especiales[i])
        if orden_caracter == ord_caracter_especial:
            verificacion = True
            break
    return verificacion

def verificar_cadena(cadena:str, letras=None, numeros=None, especiales=None, cadena_especiales:str=None) -> bool:
    '''
    Igresa una cadena y, segun las funciones de verificacion que se ingresen, devuelve si la cadena completa
    esta dentro de los caracteres especificados.

    Args:
        Se tiene que ingresar por parametro funciones que verifiquen el caracter segun el requerimiento y
        devuelvan un booleano.
        - cadena: elemento a verificar
        - letras: Funcion principal que verifica que los caracteres existan dentro de el rango de letras
        - numeros: Funcion secundaria que verifica si hay numeros dentro de la cadena
        - especiales: Funcion secundaria que verifica caracteres especiales. Necesita de una cadena.
        - cadena_especiales: Cadena que va a usar la funcion de caracteres especiales. Si no hay nada, por defecto tomara el espacio, punto y coma.
    
    Returns:
        La funcion principal devuelve un booleano segun las verificaciones
        - True: Dentro de la cadena existen todos los elementos a validar (letras, numeros, etc)
        - False: Dentro de la cadena, hay elementos que NO estan dentro de la lista de validaciones
    '''
    verificacion = True
    caracter_letras = False
    caracter_numerico = False
    caracter_especial = False

    if cadena == "":
        verificacion = False
        # Si la cadena esta vacia, se saltea todas las verificaciones y devuelve un False
    else:
        for i in range(len(cadena)):
            caracter = cadena[i]
            orden_caracter = ord(caracter)

            if letras != None:
                caracter_letras = letras(orden_caracter)
            if numeros != None:
                caracter_numerico = numeros(orden_caracter)
            if especiales != None:
                if cadena_especiales == None:
                    cadena_especiales = " .,"
                caracter_especial = especiales(orden_caracter, cadena_especiales)
            
            if caracter_letras == False and caracter_numerico == False and caracter_especial == False:
                verificacion = False
                break
    return verificacion

def verificar_elemento_en_lista(lista:list, elemento_a_buscar:str) -> bool:
    '''
    Verifica que un elemento exista dentro de una lista.

    Args:
        Lista con elementos
        elemento a buscar dentro de la lista
    Returns:
        Retorna un booleano
            True: El elemento existe dentro de la lista
            False: No se ha encontrado el elemento dentro de la lista
    '''
    verificacion = False
    for elemento in lista:
        if elemento == elemento_a_buscar:
            verificacion = True
            break
    return verificacion

def verificar_dos_elementos(elemento_a, elemento_b) -> bool:
    '''
    Verifica que dos elementos sean iguales

    Args:
        Ingresan dos parametros. Se verifica que parametro A sea igual que parametro B
    
    Returns:
        Retorna un booleano dependiendo del caso.
            True: Ambos elementos son iguales
            False: Los elementos difieren entre si
    '''
    verificacion = False
    if elemento_a == elemento_b:
        verificacion = True
    return verificacion

def ingreso_y_verificacion_cadena(mensaje:str,
                                  mensaje_error:str=None,
                                  letras:any=None, 
                                  numeros:any=None, 
                                  espceiales:any=None, 
                                  cadena:str=None) -> str:
    '''
    Funcion que se encarga de ingresar un dato, validarlo segun conveniencia y devolverlo cuendo este
    se encuentre dentro de los parametros ingresados (Ejemplo: que el ingreso sean solo letras).

    Args:
        - mensaje: Esto se va a mostrar en el input a ingresar
        - mensaje_error: Si la verificacion falla, se le va a volver a pedir al usuario un ingreso
          mostrando un mensaje de error
        - verificacion_cadena: funcion que va a verificar la cadena, se le pueden ingresar funciones 
        que verifiquen determinada condicion en cada caracter (opcionales)
        - letras/numeros/especiales: funciones que devuelven un booleano, estas validan que los
          caracteres de la cadena pertenezcan a la validacion correspondiente.
        - cadena: esta se usa UNICAMENTE si se filtra por caracteres especiales, se ingresa una cadena 
          de texto con los caracteres a validar, si no se ingresa nada, por defecto estaran el espacio,
          el punto y la coma.

    Returns:
        Retorna un string con las validaciones previas
    '''
    if mensaje_error == None:
        mensaje_error = mensaje
    if letras:
        letras = verificar_caracter_letra
    if numeros:
        numeros = verificar_caracter_numerico
    if espceiales:
        espceiales = verificar_caracter_especial

    ingreso = input(mensaje)
    while verificar_cadena(ingreso, letras, numeros, espceiales, cadena) == False:
        ingreso = input(mensaje_error)
    return ingreso
