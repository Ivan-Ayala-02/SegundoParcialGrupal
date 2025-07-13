import random

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

def elegir_zapato(premios_disponibles: list):
    if premios_disponibles == None or len(premios_disponibles) != 2:
        print("Error: no hay suficientes premios disponibles.")
        return None
    
    random.shuffle(premios_disponibles)

    eleccion = input("Elegí un zapato (blanco/negro): ").strip().lower()

    if eleccion == "blanco":
        premio = premios_disponibles[0]
    else:
        premio = premios_disponibles[1]
    return premio