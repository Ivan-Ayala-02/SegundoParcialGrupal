import random

niveles_premios_prueba = {
    "1": [{"tipo": "puntos", "valor": 1000000}],
    "2": [{"tipo": "puntos", "valor": 800000}, {"tipo": "puntos", "valor": 800000}],
    "3": [{"tipo": "puntos", "valor": 400000}, {"tipo": "puntos", "valor": 400000}],
    "4": [{"tipo": "puntos", "valor": 300000}, {"tipo": "puntos", "valor": 300000}, {"tipo": "puntos", "valor": 300000}],
    "5": [{"tipo": "puntos", "valor": 100000}, {"tipo": "puntos", "valor": 100000}, {"tipo": "puntos", "valor": 100000}, {"tipo": "puntos", "valor": 100000}],
    "6": [{"tipo": "puntos", "valor": 50000}, {"tipo": "puntos", "valor": 50000}],
    "7": [{"tipo": "vida", "valor": 1}],
    "8": [{"tipo": "pierde_todo", "valor": 0}]
}



premios_disponibles_copia = {
    "1": niveles_premios_prueba["1"].copy(),
    "2": niveles_premios_prueba["2"].copy(),
    "3": niveles_premios_prueba["3"].copy(),
    "4": niveles_premios_prueba["4"].copy(),
    "5": niveles_premios_prueba["5"].copy(),
    "6": niveles_premios_prueba["6"].copy(),
    "7": niveles_premios_prueba["7"].copy(),
    "8": niveles_premios_prueba["8"].copy()
}

def obtener_premios_de_dict(premios_disponibles_copia: dict):
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


"""if premio["tipo"] == "puntos":
        print(f"Obtuviste {premio['valor']} puntos.")
    elif premio["tipo"] == "vida":
        print("¡Ganaste una vida extra!")
    elif premio["tipo"] == "pierde_todo":
        print("⚠️ Perdiste todos tus puntos ⚠️")
"""

niveles = list(premios_disponibles_copia.keys())
puntos = 100000
vida = 1
for i in range(9):
    for nivel in niveles:
        print(f'{premios_disponibles_copia[nivel]}')

    print()
    premios_para_elegir = obtener_premios_de_dict(premios_disponibles_copia)
    if premios_para_elegir is None:
        print("No hay más premios para elegir.")
    else:
        premio = elegir_zapato(premios_para_elegir)