from modulos.utilidades import pausar_y_limpiar, comparar_respuestas
from modulos.jugador import imprimir_estado_del_jugador
from modulos.impresiones import *
from modulos.entrada import *
from os import system

def mostrar_encabezado(ronda_actual: int, mini_juego: str, dato: dict, estado_jugador: dict, campo: str, tipo_dato: str  = "Dato"):
    nombre_juego = normalizar_nombre_juego(mini_juego)

    if mini_juego.lower() == "completar_letra":
        imprimir_encabezado_y_enunciado(ronda_actual,
                                        nombre_juego,
                                        dato[campo],
                                        dato["género"],
                                        dato["dificultad"],
                                        tipo_dato)
    else:
        imprimir_encabezado_y_enunciado(ronda_actual,
                                        nombre_juego,
                                        dato[campo],
                                        dato["categoria"],
                                        dato["dificultad"],
                                        tipo_dato)

    print()
    imprimir_estado_del_jugador(estado_jugador)
    print()

    if mini_juego.lower() == "preguntados":
        opciones = obtener_opciones_pregunta(dato, 4)
        imprimir_lista(opciones)
        print()

def pedir_respuesta_usuario(input_mensaje: str, validador, tiempo_limite=None):
    if tiempo_limite:
        return pedir_entrada_con_tiempo(input_mensaje, validador, tiempo_limite)
    else:
        print("(Escribí 'ficha' si querés cambiar la pregunta)")
        return pedir_entrada(input_mensaje, validador)

def evaluar_respuesta_en_minijuego(respuesta, respuesta_correcta, jugador, duracion, contenido_fallido):
    resultado = False  # valor por defecto

    if respuesta == "timeout":
        print("❌ Tiempo agotado.")
        jugador["fallos"] += 1
        resultado = False

    else:
        resultado = procesar_respuesta_usuario(respuesta, respuesta_correcta, jugador)

        if resultado == "cambio":
            resultado = "cambio"

        elif resultado:
            registrar_acierto(jugador, duracion)
            resultado = True

        else:
            registrar_fallo(jugador, contenido_fallido)
            resultado = False

    return resultado  # ✅ único return

def registrar_acierto(jugador: dict, duracion: float):
    jugador["aciertos"] += 1
    jugador["tiempo_por_aciertos"].append(duracion)

def registrar_fallo(jugador: dict, contenido: str):
    jugador["fallos"] += 1
    jugador["preguntas_falladas"].append(contenido)

def procesar_respuesta_usuario(respuesta_usuario, respuesta_correcta, estado_jugador):
    if respuesta_usuario == "ficha":
        if estado_jugador["fichas"] > 0:
            estado_jugador["fichas"] -= 1
            print()
            print(f"Usaste una ficha. Te queda {estado_jugador['fichas']} ficha(s).")
            resultado_respuesta = "cambio"
            pausar_y_limpiar()
        else:
            print("\n¡No te quedan más fichas! Tenés que responder esta pregunta.")
            resultado_respuesta = None
            pausar_y_limpiar()
    else:
        if comparar_respuestas(respuesta_usuario, respuesta_correcta):
            print()
            print("¡Correcto! Avanzaste.")
            resultado_respuesta =  True
        else:
            print()
            print(f"❌ Incorrecto ❌\nLa respuesta era: {respuesta_correcta}")
            resultado_respuesta = False
    
    return resultado_respuesta


def obtener_opciones_pregunta(datos_pregunta: dict, cant_opciones: int) -> list:
    """Extrae y ordena las opciones de una pregunta."""
    opciones = []
    for i in range(1, cant_opciones + 1):
        clave = f"opcion{i}"
        if clave in datos_pregunta:
            opciones.append(datos_pregunta[clave])


    return opciones

def ingresar_numero_dentro_de_rango(rango_inicio:int, rango_fin:int, salida_default:int=None, mensaje:str=None, mensaje_error:str=None) -> int:
    bandera = True

    while bandera:
        numero = input(mensaje)

        if numero == "":
            if salida_default == None:
                print(mensaje_error)
            else:
                numero = salida_default
                bandera = False
    
        elif numero.isnumeric():
            numero = int(numero)

            if numero < rango_inicio or numero > rango_fin:
                print(mensaje_error)
            else:
                bandera = False

        else:
            print(mensaje_error)

    return numero

def ingresar_longitud_tablero() -> tuple:
    system("cls")
    default_filas = 5
    maximo_filas = 20
    default_columnas = 5
    maximo_columnas = 20

    mensaje_filas = f"A) Ingrese la cantidad de filas para el tablero ( default {default_filas} - maximo {maximo_filas}): "
    mensaje_columnas = f"B) Ingrese la cantidad de columnas para el tablero ( default {default_columnas} - maximo {maximo_columnas}): "
    error_limites = "Limite exedido, ingrese dentro de un rango valido: "

    filas = ingresar_numero_dentro_de_rango(0, maximo_filas, default_filas, mensaje_filas, error_limites)
    system("cls")
    columnas = ingresar_numero_dentro_de_rango(0, maximo_columnas, default_columnas, mensaje_columnas, error_limites)
    return filas, columnas

def ingresar_cantidad_minas(filas:int, columnas:int) -> int:
    system("cls")
    default_minas = 1

    mensaje_minas = f"C) Ingrese la cantidad de minas (default {default_minas}): "
    mensaje_error_minas = "La cantidad de minas no puede ser superior al tamaño del tablero: "
    longitud_tablero = filas * columnas

    minas = ingresar_numero_dentro_de_rango(0, longitud_tablero, default_minas, mensaje_minas, mensaje_error_minas)
    return minas
