import random
from modulos.entrada import *
from modulos.utilidades import *

# --------------------------------------------------------------------------------------
#   AUXILIARES / Funciones generales
# --------------------------------------------------------------------------------------

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


def descubrir_bloques(posicion_fila, posicion_columna, matriz_visual, matriz_real, simbolo_visual_liberado, valor_real_liberado, valor_real_mina):
    total_filas, total_columnas = longitud_matriz(matriz_real)

    if posicion_fila < 0 or posicion_fila >= total_filas or posicion_columna < 0 or posicion_columna >= total_columnas:
        return # punto de corte, verifica limites
    
    if matriz_real[posicion_fila][posicion_columna] == valor_real_mina:
        return
    elif matriz_real[posicion_fila][posicion_columna] == valor_real_liberado:
        return
        # puntos de corte, termina si ya se descubrio antes o si hay una mina
    
    # Libera la casilla
    matriz_visual[posicion_fila][posicion_columna] = simbolo_visual_liberado
    matriz_real[posicion_fila][posicion_columna] = valor_real_liberado

    if contar_minas_alrededor(posicion_fila, posicion_columna, matriz_real, valor_real_mina) > 0:
        return # punto de corte, termina si existen minas alrededor

    # LLamada recursiva a bloques adyacentes
    for desplazamiento_fila in range(-1,2): # -1, 0, 1
        for desplazamiento_columna in range(-1,2): # -1, 0, 1
            if desplazamiento_fila != 0 or desplazamiento_columna != 0:
            # Verificacion para que no tome el bloque actual (centro)
                nueva_fila = posicion_fila + desplazamiento_fila
                nueva_columna = posicion_columna + desplazamiento_columna
                descubrir_bloques(nueva_fila, nueva_columna, matriz_visual, matriz_real, simbolo_visual_liberado, valor_real_liberado, valor_real_mina)

def verificar_elemento_matriz(matriz:list, elemento:any) -> bool:
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

# --------------------------------------------------------------------------------------
#   AUXILIARES / Imprimir en consola
# --------------------------------------------------------------------------------------

def imprimir_top(cantidad_columnas:int):
    tl = '┌'
    tm = '┬'
    tr = '┐'
    h = '─' * 3
    top = tl + h + (tm + h) * (cantidad_columnas - 1) + tr
    print(top)

def imprimir_bottom(cantidad_columnas:int):
    bl = '└'
    bm = '┴'
    br = '┘'
    h = '─' * 3
    bottom = bl + h + (bm + h) * (cantidad_columnas - 1) + br
    print(bottom)

def imprimir_mid_lineas(cantidad_columnas:int):
    h = '─' * 3
    lm = '├'
    mm = '┼'
    rm = '┤'
    mid_top_bottom = lm + h + (mm + h) * (cantidad_columnas - 1) + rm
    print(mid_top_bottom)

def guardar_mid_contenido(fila_matriz:list):
    v = '│'
    mid_contenido = v
    for i in range(len(fila_matriz)):
        mid_contenido += f" {fila_matriz[i]} {v}"
    return mid_contenido

def imprimir_mid(matriz:list, numeracion:bool=False):
    filas, columnas = longitud_matriz(matriz)
    
    # Mid
    for i in range(filas):
        mid = ""
        mid += guardar_mid_contenido(matriz[i])
        if numeracion == True:
            mid += f" {i + 1}"  
        print(mid)

        #bottom
        if i != filas - 1:
            imprimir_mid_lineas(columnas)

def imprimir_numeracion_cuadricula(cantidad_columnas:int):
    cadena_vacia = " " * 2
    medio = " " * 3
    for i in range(cantidad_columnas):
        cadena_vacia += f"{i + 1}"
        if i < cantidad_columnas - 1:
            cadena_vacia += medio
    print(cadena_vacia)

def dibujar_matriz(matriz:list, numeracion:bool=False):
    cantidad_columnas = len(matriz[0])
    if numeracion:
        imprimir_numeracion_cuadricula(cantidad_columnas)
    imprimir_top(cantidad_columnas)
    imprimir_mid(matriz, numeracion)
    imprimir_bottom(cantidad_columnas)



# --------------------------------------------------------------------------------------
#   MINIJUEGO
# --------------------------------------------------------------------------------------  

def minijuego_buscaminas(filas:int, columnas:int, cantidad_minas:int):
    bloque_visual_ocupado = "·"
    bloque_visual_liberado = " "
    caracter_real_bloque = 0
    caracter_real_liberado = 1
    caracter_real_mina = 2
    matriz_visual_minas = crear_matriz(filas, columnas, bloque_visual_ocupado)
    matriz_real_minas = crear_matriz(filas, columnas, caracter_real_bloque)
    matriz_real_minas = reemplazar_elementos_aleatorio_matriz(matriz_real_minas, caracter_real_bloque, caracter_real_mina, cantidad_minas)
    juego_activo = True
    mina_activada = False

    while juego_activo:
        tablero_disponible = verificar_elemento_matriz(matriz_real_minas, caracter_real_bloque)

        if tablero_disponible:
            dibujar_matriz(matriz_visual_minas, numeracion=True)
            ingreso_fila, ingreso_columna = ingreso_validacion_datos_buscaminas(filas, columnas) 
            ingreso_matriz = matriz_real_minas[ingreso_fila][ingreso_columna]
            pausar_y_limpiar()

            if ingreso_matriz == caracter_real_mina:
                juego_activo = False
                mina_activada = True

            else:
                descubrir_bloques(ingreso_fila, ingreso_columna, 
                                matriz_visual_minas, matriz_real_minas, 
                                bloque_visual_liberado, caracter_real_liberado, 
                                caracter_real_mina) 

        else:
            juego_activo = False    

    if mina_activada:
        print(f"Perdiste!")
        salida_juego = False

    else:
        print("Ganaste! liberaste el tablero sin tocar minas")
        salida_juego = True

    return salida_juego
         
# --------------------------------------------------------------------------------------
#   EJECUCION FUNCIONES
# --------------------------------------------------------------------------------------

minijuego_buscaminas(5,5,2)

