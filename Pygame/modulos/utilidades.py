import random
from os import system
from copy import deepcopy
from datetime import datetime
from unidecode import unidecode
###################################################################### COMPLEMENTARIAS / GENERALES ######################################################################
#---------------------- ARREGLOS VISUALES ----------------------#
# LIMPIAR TERMINAL
def pausar_y_limpiar():
    print()
    system("pause")
    system("cls")

#---------------------- FUNCIONES PARA TRABAJAR CON DICCIONARIOS Y LISTAS ----------------------#
# PARA OBTENER UNA LISTA CON PREGUNTAS FILTRADAS
def filtrar_por_clave(lista: list, clave: str, valor: str) -> list:
    resultado = []

    for elemento in lista:
        claves = obtener_lista_claves(elemento)
        if validar_elemento(claves, clave) and elemento[clave].lower() == valor.lower():
            resultado.append(deepcopy(elemento))

    return resultado

# VENDRIA A SER UN IN EN PYTHON
def validar_elemento(lista: list, elemento_a_verificar: str) -> bool:
    """Valida si un elemento se encuentra dentro de una lista (vector).
    """
    existe = False

    for elemento in lista:
        if elemento_a_verificar == elemento:
            existe = True
            break
    
    return existe

# OPCIONAL, PARA ARCHIVOS (PARA GENERAR CSV DE LAS LISTAS DE CADA JUEGO)
def obtener_preguntas(datos_juegos: dict, juego: str):
    return datos_juegos[juego]   

def generar_copia_de_diccionario_con_listas(diccionario_original: dict) -> dict:
    from copy import deepcopy
    return deepcopy(diccionario_original)

def elegir_elemento_aleatorio_y_remover(lista: list):
    if len(lista) == 0:
        return None
    elegido = random.choice(lista)
    lista.remove(elegido)

    return elegido

def obtener_lista_claves(diccionario: dict):
    lista_claves = list(diccionario.keys())

    return lista_claves

def lista_vacia(lista: list):
    if len(lista) == 0:
        vacio = True
    else:
        vacio = False

    return vacio

#---------------------- VALIDACIÓN ----------------------#
def comparar_respuestas(resp_usuario: str, resp_correcta: str) -> bool:
    """Compara ignorando tildes, mayúsculas y espacios extras."""
    r1 = unidecode(resp_usuario.strip().lower())
    r2 = unidecode(resp_correcta.strip().lower())
    return r1 == r2

def obtener_dificultad(ronda: int, dificultades: list):
    return dificultades[ronda % len(dificultades)]




def inicializar_estado_jugador(estado_inicial: dict):
    return deepcopy(estado_inicial)


def inicializar_recursos_juego(configuracion: dict, preguntas: dict,
                                premios: dict, funciones_juegos: dict):
    contexto = {
        "configuracion": configuracion,
        "preguntas_disponibles": deepcopy(preguntas),
        "premios_disponibles": deepcopy(premios),
        "funciones_juegos": funciones_juegos,
        "juegos_restantes": obtener_lista_claves(funciones_juegos)
    }
    
    return contexto


def construir_datos_usuario(estado_jugador, nombre, resultado):
    datos = estado_jugador.copy()
    datos["nombre"] = nombre
    datos["resultado"] = resultado

    return datos


def construir_contexto_mini_juego(ronda, juego, preguntas, estado_jugador, configuracion):
    contexto = {
        "juego": juego,
        "ronda": ronda,
        "preguntas": preguntas,
        "jugador": estado_jugador,
        "configuracion": configuracion
    }

    return contexto

def ejecutar_minijuego(contexto, funciones_juegos):
    juego_actual = contexto["juego"]
    return funciones_juegos[juego_actual](contexto)


#---------------------- BUSCAMINAS ----------------------#


def es_numerico(valor:str): # <---- Agregar al auxiliar
    return valor.isnumeric()

def crear_matriz(filas:int=3, columnas:int=3, contenido:str|int=" "):
    matriz = []

    for _ in range(filas):  
        fila_actual = []

        for _ in range(columnas):  
            fila_actual.append(contenido) 

        matriz.append(fila_actual)
    return matriz

def longitud_matriz(matriz:list):
    return len(matriz), len(matriz[0])

def reemplazar_elementos_aleatorio_matriz(matriz:list, elemento:any, reemplazo:any, cantidad:int) -> list:
    contador = 0
    while contador < cantidad:
        i = random.randint(0, len(matriz) -1)
        j = random.randint(0, len(matriz[0]) - 1)
    
        if matriz[i][j] == elemento:
            cambiar_elemento_matriz(matriz, i, j, reemplazo)
            contador += 1
    return matriz

def ingreso_validacion_datos_buscaminas(filas, columnas):
    from modulos.entrada import pedir_entrada
    
    mensaje_error = "❌​ Entrada inválida. Intentá de nuevo. ❌​"

    ingreso_fila = pedir_entrada(f"Ingrese una fila (1-{filas}): ", es_numerico)
    while int(ingreso_fila) < 1 or int(ingreso_fila) > filas:
        ingreso_fila = pedir_entrada(f"{mensaje_error}: ", es_numerico)

    ingreso_columna = pedir_entrada(f"Ingrese una columna (1-{columnas}): ", es_numerico)
    while int(ingreso_columna) < 1 or int(ingreso_columna) > columnas:
        ingreso_columna = pedir_entrada(f"{mensaje_error}: ", es_numerico)
    
    return int(ingreso_fila)-1, int(ingreso_columna)-1

def cambiar_elemento_matriz(matriz:list, fila_i:int, columna_j:int, nuevo_elemento:any) -> list:
    matriz[fila_i][columna_j] = nuevo_elemento

def contar_minas_alrededor(posicion_fila, posicion_columna, matriz_real_minas, valor_real_mina) -> int:
    cantidad_minas = 0
    total_filas, total_columnas = longitud_matriz(matriz_real_minas)

    for desplazamiento_fila in range(-1,2): # -1, 0, 1
        for desplazamiento_columna in range(-1,2): # -1, 0, 1
            casilla_fila_vecina = posicion_fila + desplazamiento_fila
            casilla_columna_vecina = posicion_columna + desplazamiento_columna

            if (0 <= casilla_fila_vecina < total_filas) and (0 <= casilla_columna_vecina < total_columnas):
                if matriz_real_minas[casilla_fila_vecina][casilla_columna_vecina] == valor_real_mina:
                    cantidad_minas += 1
    return cantidad_minas


def descubrir_bloques(posicion_fila:int, posicion_columna:int, matriz_visual:list, matriz_real:list, datos_tablero:dict):
    
    simbolo_visual_liberado = datos_tablero["bloque_visual_liberado"]
    valor_real_liberado = datos_tablero["caracter_real_liberado"]
    valor_real_mina = datos_tablero["caracter_real_mina"]

    total_filas, total_columnas = longitud_matriz(matriz_real)

    if posicion_fila < 0 or posicion_fila >= total_filas or posicion_columna < 0 or posicion_columna >= total_columnas:
        return # punto de corte, verifica limites
    
    if matriz_real[posicion_fila][posicion_columna] == valor_real_mina:
        return
    elif matriz_real[posicion_fila][posicion_columna] == valor_real_liberado:
        return
        # puntos de corte, termina si ya se descubrio antes o si hay una mina
    
    # Libera la casilla
    cambiar_elemento_matriz(matriz_visual, posicion_fila, posicion_columna, simbolo_visual_liberado)
    cambiar_elemento_matriz(matriz_real, posicion_fila, posicion_columna, valor_real_liberado)

    #Cuenta la cantidad de minas que hay alrededor de la casilla
    cantidad_minas = contar_minas_alrededor(posicion_fila, posicion_columna, matriz_real, valor_real_mina)

    if cantidad_minas > 0:
        matriz_visual[posicion_fila][posicion_columna] = cantidad_minas
        return # punto de corte, termina si existen minas alrededor

    # LLamada recursiva a bloques adyacentes
    for desplazamiento_fila in range(-1,2): # -1, 0, 1

        for desplazamiento_columna in range(-1,2): # -1, 0, 1

            if desplazamiento_fila != 0 or desplazamiento_columna != 0:
            # Verificacion para que no tome el bloque actual (centro)
                nueva_fila = posicion_fila + desplazamiento_fila
                nueva_columna = posicion_columna + desplazamiento_columna
                descubrir_bloques(nueva_fila, nueva_columna, matriz_visual,
                                   matriz_real, datos_tablero)

def reemplazar_elemento_entre_matrices(matriz_a:list, matriz_b:list, elemento_a:any, reemplazo_b:any):
    filas, columnas = longitud_matriz(matriz_a)
    for i in range(filas):
        for j in range(columnas):
            if matriz_a[i][j] == elemento_a:
                matriz_b[i][j] = reemplazo_b

def contador_elemento_matriz(matriz:list, elemento:any) -> bool:
    filas, columnas = longitud_matriz(matriz)
    contador = 0
    verificador = False
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == elemento:
                contador += 1
    if contador > 0:
        verificador = True
    return verificador
