from datetime import datetime

def obtener_tiempo_limite(config, juego_actual):
    """Obtiene el tiempo límite asignado a un minijuego desde la configuración general.

    Args:
        config (dict): Configuración general del juego, que incluye los tiempos por juego.
        juego_actual (str): Nombre del minijuego.

    Returns:
        int | float: Tiempo límite en segundos para ese minijuego.
    """
    return config["tiempos_limite"][juego_actual]

def calcular_m_s_ms(duracion):
    """Convierte una duración de segundos a minutos, segundos y milisegundos.

    Args:
        duracion (float): Tiempo total en segundos.

    Returns:
        tuple: (minutos, segundos, milisegundos)
    """
    minutos = int(duracion // 60)
    segundos = int(duracion % 60)
    milisegundos = int((duracion - int(duracion)) * 1000)

    return minutos, segundos, milisegundos

def mostrar_duracion(duracion, tiempo_limite):
    """Muestra por consola cuánto se demoró el jugador, comparado con el tiempo límite permitido.

    Args:
        duracion (float): Tiempo real de respuesta en segundos.
        tiempo_limite (float): Tiempo máximo permitido para responder.
    """
    minutos, segundos, milisegundos = calcular_m_s_ms(duracion)

    print(f"\n⏰ ¡Se te acabó el tiempo!")
    print(f"Te demoraste {minutos} min, {segundos} seg y {milisegundos} ms (límite: {tiempo_limite} segundos).")

def formatear_fecha_actual(formato: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Devuelve la fecha y hora actual formateada como cadena.

    Args:
        formato (str, optional): Formato de la fecha, por defecto "%Y-%m-%d %H:%M:%S".

    Returns:
        str: Fecha y hora actual en el formato especificado.
    """
    return datetime.now().strftime(formato)