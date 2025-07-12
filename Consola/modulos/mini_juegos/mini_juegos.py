#from modulos.utilidades import elegir_elemento_aleatorio_y_remover, lista_vacia
from modulos.utilidades import *
from modulos.mini_juegos.utilidades_mini_juegos import *
from modulos.tiempo import obtener_tiempo_limite
from modulos.entrada import es_cadena_vacia

def jugar_si_o_no(recursos_mini_juego: dict) -> bool:
    preguntas = recursos_mini_juego["preguntas"]
    jugador = recursos_mini_juego["jugador"]
    ronda = recursos_mini_juego["ronda"]
    config = recursos_mini_juego["configuracion"]
    juego = recursos_mini_juego["juego"]

    if lista_vacia(preguntas):
        print("No hay más preguntas disponibles.")
        return False

    tiempo_limite = obtener_tiempo_limite(config, juego)

    se_respondio = False
    resultado_final = False  # Valor predeterminado

    while not se_respondio:
        dato = elegir_elemento_aleatorio_y_remover(preguntas)

        mostrar_encabezado(ronda, juego, dato, jugador, "pregunta", "Pregunta")

        respuesta, duracion = pedir_respuesta_usuario(
            "Escriba la respuesta (si/no): ", es_si_no_o_ficha, tiempo_limite
        )

        resultado = evaluar_respuesta_en_minijuego(
            respuesta, dato["respuesta"], jugador, duracion, dato["pregunta"]
        )

        if resultado != "cambio":
            resultado_final = resultado
            se_respondio = True

    return resultado_final

def jugar_completar_oracion(recursos_mini_juego: dict) -> bool:
    oraciones = recursos_mini_juego["preguntas"]
    jugador = recursos_mini_juego["jugador"]
    ronda = recursos_mini_juego["ronda"]
    config = recursos_mini_juego["configuracion"]
    juego = recursos_mini_juego["juego"]

    if lista_vacia(oraciones):
        print("No hay más oraciones disponibles para completar.")
        return False

    tiempo_limite = obtener_tiempo_limite(config, juego)

    se_respondio = False
    resultado_final = False  # valor por defecto

    while not se_respondio:
        dato = elegir_elemento_aleatorio_y_remover(oraciones)

        mostrar_encabezado(ronda, juego, dato, jugador, "oracion", "Oracion")

        respuesta, duracion = pedir_respuesta_usuario(
            "Completa la oración: ", es_cadena_vacia, tiempo_limite
        )

        resultado = evaluar_respuesta_en_minijuego(
            respuesta, dato["respuesta"], jugador, duracion, dato["oracion"]
        )

        if resultado != "cambio":
            resultado_final = resultado
            se_respondio = True
        # si fue "cambio", no pasa nada, se repite el while

    return resultado_final


def jugar_completar_palabra(recursos_mini_juego: dict) -> bool:
    palabras = recursos_mini_juego["preguntas"]
    jugador = recursos_mini_juego["jugador"]
    ronda = recursos_mini_juego["ronda"]
    config = recursos_mini_juego["configuracion"]
    juego = recursos_mini_juego["juego"]

    if lista_vacia(palabras):
        print("No hay más palábras disponibles para completar.")
        return False

    tiempo_limite = obtener_tiempo_limite(config, juego)

    se_respondio = False
    resultado_final = False  # valor por defecto

    while not se_respondio:
        dato = elegir_elemento_aleatorio_y_remover(palabras)

        mostrar_encabezado(ronda, juego, dato, jugador, "pista", dato["palabra"])

        respuesta, duracion = pedir_respuesta_usuario(
            "Completa la palábra: ", es_alfabetica, tiempo_limite
        )

        resultado = evaluar_respuesta_en_minijuego(
            respuesta, dato["respuesta"], jugador, duracion, dato["palabra"]
        )

        if resultado != "cambio":
            resultado_final = resultado
            se_respondio = True
        # si fue "cambio", no pasa nada, se repite el while

    return resultado_final

def jugar_preguntados(recursos_mini_juego: dict) -> bool:
    preguntas = recursos_mini_juego["preguntas"]
    jugador = recursos_mini_juego["jugador"]
    ronda = recursos_mini_juego["ronda"]
    config = recursos_mini_juego["configuracion"]
    juego = recursos_mini_juego["juego"]

    if lista_vacia(preguntas):
        print("No hay más preguntas disponibles.")
        return False

    tiempo_limite = obtener_tiempo_limite(config, juego)

    se_respondio = False
    resultado_final = False

    while not se_respondio and preguntas:
        dato = elegir_elemento_aleatorio_y_remover(preguntas)

        mostrar_encabezado(ronda, juego, dato, jugador,"pregunta", "Pregunta")

        respuesta, duracion = pedir_respuesta_usuario(
            "Elegir una de las opciones: ", es_numerico_o_ficha, tiempo_limite
        )

        resultado = evaluar_respuesta_en_minijuego(
            respuesta, dato["respuesta"], jugador, duracion, dato["pregunta"]
        )

        if resultado != "cambio":
            resultado_final = resultado
            se_respondio = True

    return resultado_final

def minijuego_buscaminas(filas:int, columnas:int, cantidad_minas:int, datos_tablero:dict):
    system("cls")
    bloque_visual_ocupado = datos_tablero["bloque_visual_ocupado"]
    bloque_visual_mina = datos_tablero["bloque_visual_mina"]
    caracter_real_bloque = datos_tablero["caracter_real_bloque"]
    caracter_real_mina = datos_tablero["caracter_real_mina"]
    
    matriz_visual_minas = crear_matriz(filas, columnas, bloque_visual_ocupado)
    matriz_real_minas = crear_matriz(filas, columnas, caracter_real_bloque)
    matriz_real_minas = reemplazar_elementos_aleatorio_matriz(matriz_real_minas, caracter_real_bloque, 
                                                              caracter_real_mina, cantidad_minas)
    juego_activo = True
    mina_activada = False

    while juego_activo:
        tablero_disponible = contador_elemento_matriz(matriz_real_minas, caracter_real_bloque)

        if tablero_disponible:
            dibujar_matriz(matriz_visual_minas, numeracion=True)
            ingreso_fila, ingreso_columna = ingreso_validacion_datos_buscaminas(filas, columnas) 
            ingreso_matriz = matriz_real_minas[ingreso_fila][ingreso_columna]

            if ingreso_matriz == caracter_real_mina:
                reemplazar_elemento_entre_matrices(matriz_real_minas, matriz_visual_minas,
                                                   caracter_real_mina, bloque_visual_mina)
                juego_activo = False
                mina_activada = True
            else:
                descubrir_bloques(ingreso_fila, ingreso_columna, matriz_visual_minas,
                                  matriz_real_minas, datos_tablero) 
            
            pausar_y_limpiar()

        else:
            juego_activo = False    

    if mina_activada:
        mensaje_resultado = f"Perdiste! Mina pisada en {ingreso_fila+1, ingreso_columna+1}"
        salida_juego = False
    else:
        mensaje_resultado ="Ganaste! liberaste el tablero sin tocar minas"
        salida_juego = True

    dibujar_matriz(matriz_visual_minas, True)
    print(mensaje_resultado)

    pausar_y_limpiar()
    return salida_juego