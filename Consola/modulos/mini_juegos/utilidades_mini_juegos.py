from modulos.utilidades import pausar_y_limpiar, comparar_respuestas
from modulos.jugador import imprimir_estado_del_jugador
from modulos.impresiones import *
from modulos.entrada import *

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