import random
from modulos.entrada import pedir_entrada, es_blanco_o_negro

###################################################################### PREMIOS ######################################################################
def obtener_premios(premios_disponibles_copia: dict):
    niveles = list(premios_disponibles_copia.keys())

    # Filtrar niveles con premios disponibles
    niveles_diponibles = []
    for nivel in niveles:
        if len(premios_disponibles_copia[nivel]) > 0:
            niveles_diponibles.append(nivel)

    if len(niveles_diponibles) < 2:
        return None  # No hay dos niveles distintos con premios

    premios_no_elegidos = False
    premios = []
    
    while not premios_no_elegidos: 
        nivel1 = random.choice(niveles_diponibles)
        nivel2 = random.choice(niveles_diponibles)

        while nivel1 == nivel2:
            nivel2 = random.choice(niveles_diponibles)

        premio1 = random.choice(premios_disponibles_copia[nivel1])
        premio2 = random.choice(premios_disponibles_copia[nivel2])

        premios.append(premio1)
        premios.append(premio2)

        if premio1 != premio2:
            # Eliminar premios ya entregados
            premios_disponibles_copia[nivel1].remove(premio1)
            premios_disponibles_copia[nivel2].remove(premio2)
            premios_no_elegidos = True

    return premios

def elegir_premio(premios_disponibles: list):
    if premios_disponibles == None or len(premios_disponibles) != 2:
        print("Error: no hay suficientes premios disponibles.")
        return None
    
    random.shuffle(premios_disponibles)

    eleccion = pedir_entrada("Elegí un color ⚪ ⚫​ (blanco/negro): ", es_blanco_o_negro)

    if eleccion == "blanco":
        premio_elegido = premios_disponibles[0]
        premio_no_elegido = premios_disponibles[1]
    else:
        premio_elegido = premios_disponibles[1]
        premio_no_elegido = premios_disponibles[0]

    return premio_elegido, premio_no_elegido, eleccion

def actualizar_estado_por_premio(premio, premio_dejado, vida, puntos, eleccion):
    if premio["tipo"] == "puntos":
        puntos += premio["valor"]
        linea_1 = f"Obtuviste {premio['valor']} puntos."
    elif premio["tipo"] == "vida":
        vida += premio["valor"]
        linea_1 = f"¡Ganaste una vida extra! Tienes {vida} vidas."
    elif premio["tipo"] == "pierde_todo":
        puntos = 0
        linea_1 = "¡Perdiste todos tus puntos!"

    if premio_dejado["tipo"] == "puntos":
        print()
        linea_2 = f"Premio no elegido: {premio_dejado['valor']} puntos."
    elif premio_dejado["tipo"] == "vida":
        print()
        linea_2 = f"Premio no elegido: {premio_dejado['valor']} vida."
    elif premio_dejado["tipo"] == "pierde_todo":
        print()
        linea_2 = f"Premio no elegido: {premio_dejado['tipo']}"

    if eleccion == "blanco":     
        print(f'⚪  {linea_1} | ⚫  ​{linea_2}')
    else:
        print(f'⚫  {linea_1} | ⚪  ​{linea_2}')

    return vida, puntos