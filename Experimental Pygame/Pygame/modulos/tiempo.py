######################################################################    TIEMPO    ######################################################################
from datetime import datetime

def obtener_tiempo_limite(config, juego_acutal):
    return config["tiempos_limite"][juego_acutal]

def calcular_m_s_ms(duracion):
    minutos = int(duracion // 60)
    segundos = int(duracion % 60)
    milisegundos = int((duracion - int(duracion)) * 1000)

    return minutos, segundos, milisegundos

def mostrar_duracion(duracion, tiempo_limite):
    minutos, segundos, milisegundos = calcular_m_s_ms(duracion)

    print(f"\n⏰ ¡Se te acabó el tiempo!")
    print(f"Te demoraste {minutos} min, {segundos} seg y {milisegundos} ms (límite: {tiempo_limite} segundos).")


def formatear_fecha_actual(formato: str = "%Y-%m-%d %H:%M:%S") -> str:
    return datetime.now().strftime(formato)