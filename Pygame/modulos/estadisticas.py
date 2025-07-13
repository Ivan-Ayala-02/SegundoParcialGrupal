from modulos.utilidades import validar_elemento, obtener_lista_claves
from modulos.tiempo import calcular_m_s_ms, formatear_fecha_actual
from archivos.archivo_json import *
######################################################################    MENÚS    ######################################################################
def seleccionar_perfil_estadisticas(estadisticas: dict) -> str | None:
    if len(estadisticas) == 0:
        print("⚠️ No hay perfiles registrados.")
        return None

    print("\n📋 Perfiles disponibles:")
    for nombre in estadisticas:
        print(f"- {nombre}")

    nombre = input("\n🧾 Ingresá el nombre EXACTO del perfil: ").strip()

    existe = False
    for clave in estadisticas:
        if clave == nombre:
            existe = True
            break

    if not existe:
        print("❌ Ese perfil no existe.")
        return None

    return nombre

def mostrar_porcentaje_aciertos(estadisticas: dict, usuario: str):
    partidas = estadisticas[usuario]["partidas"]

    total_aciertos = 0
    total_errores = 0

    for partida in partidas:
        total_aciertos += partida["aciertos"]
        total_errores += partida["fallos"]

    total_respuestas = total_aciertos + total_errores

    if total_respuestas == 0:
        print("⚠️ No hay respuestas registradas para este jugador.")
        return

    porcentaje = (total_aciertos * 100) / total_respuestas
    print(f"🎯 Porcentaje de aciertos: {porcentaje:.2f}%")


def obtener_partidas_ganadas(partidas: list):
    partidas_ganadas = []    
    for partida in partidas:
        if partida["resultado"] == "victoria":
            partidas_ganadas.append(partida)

    return partidas_ganadas
    
def mostrar_mejor_partida(estadisticas: dict, usuario: str):
    partidas = estadisticas[usuario]["partidas"]

    if len(partidas) == 0:
        print("⚠️ Este jugador no tiene partidas registradas.")
        return

    mejor_puntaje = -1
    mejor_partida = None

    partidas_ganadas = obtener_partidas_ganadas(partidas)
    
    if len(partidas_ganadas) == 0:
        print("¡No ha ganado ninguna partida todavía!")
    else:
        for partida in partidas_ganadas:
            if partida["puntos"] > mejor_puntaje:
                mejor_puntaje = partida["puntos"]
                mejor_partida = partida

        print("\n🏆 Mejor partida registrada:")
        print(f"- Fecha: {mejor_partida['fecha']}")
        print(f"- Resultado: {mejor_partida.get('resultado', 'desconocido')}")
        print(f"- Puntos: {mejor_partida['puntos']}")
        print(f"- Aciertos: {mejor_partida['aciertos']}")
        print(f"- Fallos: {mejor_partida['fallos']}")
        print(f"- Tiempo promedio por acierto: {mejor_partida['tiempo_promedio']} s")

def mostrar_preguntas_falladas_sin_repetir(estadisticas: dict, usuario: str):
    partidas = estadisticas[usuario]["partidas"]
    preguntas_unicas = []

    for partida in partidas:
        claves_partida = obtener_lista_claves(partida)
        if validar_elemento(claves_partida, "preguntas_falladas"):
            for pregunta in partida["preguntas_falladas"]:
                if not validar_elemento(preguntas_unicas, pregunta):
                    preguntas_unicas.append(pregunta)

    if len(preguntas_unicas) == 0:
        print("✅ No hay preguntas falladas registradas.")
        return

    print("\n📋 Preguntas falladas (únicas):")
    for pregunta in preguntas_unicas:
        print(f"- {pregunta}")

######################################################################    GUARDAR PARTIDA Y DATOS    ######################################################################
def crear_datos_partida(datos_jugador: dict):
    if datos_jugador["aciertos"] > 0:
        promedio = sum(datos_jugador["tiempo_por_aciertos"]) / datos_jugador["aciertos"]
    else:
        promedio = 0.0
    
    datos = {
        "fecha": formatear_fecha_actual(),
        "aciertos": datos_jugador["aciertos"],
        "fallos": datos_jugador["fallos"],
        "puntos": datos_jugador["puntos"],
        "tiempo_promedio": round(promedio, 2), # Use round para que sea medianamente preciso
        "preguntas_falladas": datos_jugador["preguntas_falladas"],
        "resultado": datos_jugador["resultado"]
    }
    
    return datos

def registrar_partida(usuario, datos_partida, estadisticas):
    # Recorremos las claves manualmente para ver si el usuario ya existe
    existe = False
    for clave in estadisticas:
        if clave == usuario:
            existe = True
            break

    # Si no existe, lo creamos con lista vacía de partidas
    if not existe:
        estadisticas[usuario] = {"partidas": []}

    # Agregamos la partida a la lista
    estadisticas[usuario]["partidas"].append(datos_partida)

def guardar_resultado_partida(nombre_usuario, datos_usuario):
    datos_partida = crear_datos_partida(datos_usuario)
    estadisticas = cargar_datos_json("archivos\json\estadisticas.json")
    registrar_partida(nombre_usuario, datos_partida, estadisticas)
    guardar_diccionario("archivos\json\estadisticas.json", estadisticas)

def mostrar_estadisticas(datos_usuario: dict):
    print(f"\n📊 Estadísticas de la partida del usuario {datos_usuario['nombre']}:")
    print(f"✅​ Aciertos: {datos_usuario['aciertos']}")
    print(f"❌​ Fallos: {datos_usuario['fallos']}")
    
    minutos, segundos, milisegundos = calcular_m_s_ms(datos_usuario['tiempo_juego'])
    print(f"⏱️  Duración de la partida: {minutos} min, {segundos} seg y {milisegundos} ms.")


    if datos_usuario["tiempo_por_aciertos"]:
        promedio = sum(datos_usuario["tiempo_por_aciertos"]) / len(datos_usuario["tiempo_por_aciertos"])
        minutos = int(promedio // 60)
        segundos = int(promedio % 60)
        milisegundos = int((promedio - int(promedio)) * 1000)
        print(f"⏱️  Tiempo promedio de respuesta en aciertos: {minutos} min, {segundos} seg, {milisegundos} ms")
    else:
        print("⏱️  No hubo respuestas correctas, sin promedio.")