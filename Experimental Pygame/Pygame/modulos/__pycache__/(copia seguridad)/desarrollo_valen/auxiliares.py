import random
from unidecode import unidecode

def pedir_respuesta_si_o_no() -> str:
    
    respuesta = input("Respuesta (si/no): ").strip().lower()

    while respuesta != "si" and respuesta != "no":
        print("❌​ ERROR: Debe ingresar si o no. ❌​\n")
        respuesta = input("Respuesta (si/no): ").strip().lower()

    return respuesta

def pedir_respuesta_completar_palabra() -> str:
    
    respuesta = input("Tu respuesta: ").strip().lower()

    while not respuesta.isalpha():
        print("❌​ ERROR: Debe ingresar una palabra. ❌​\n")
        respuesta = input("Tu respuesta: ").strip().lower()

    return respuesta

def pedir_nombre_jugador() -> str:
    nombre_usuario = input("- Ingrese su nombre de usuario(sin espacios): ​").strip()
    print("- ¿Confirma su nombre de usuario?", end="")
    confirmacion = pedir_respuesta_si_o_no()

    while confirmacion == "no":
        nombre_usuario = input("- Ingrese su nombre de usuario(sin espacios): ​").strip()
        print("- ¿Confirma su nombre de usuario?", end="")
        confirmacion = pedir_respuesta_si_o_no()

    return nombre_usuario

def validar_elemento(lista: list, elemento_a_verificar: str) -> bool:
    """Valida si un elemento se encuentra dentro de una lista (vector).
    """
    existe = False

    for elemento in lista:
        if elemento_a_verificar == elemento:
            existe = True
            break
    
    return existe

def obtener_preguntas(datos_juegos: dict, juego: str):
    return datos_juegos[juego]   


def copiar_diccionario_con_listas(diccionario_original: dict) -> dict:
    copia = {}
    for clave in diccionario_original.keys():
        copia[clave] = diccionario_original[clave].copy()
    return copia

def mostrar_info_ronda(ronda: int, tipo_actual: str):
    print(f"\n===== Ronda {ronda + 1} =====")
    print(f"Tipo de juego: {tipo_actual.replace('_', ' ').title()}")

def elegir_nuevo_tipo(tipos_restantes):
    tipo = random.choice(tipos_restantes)
    tipos_restantes.remove(tipo)
    return tipo


def actualizar_estado_por_premio(premio, vida, puntos):
    if premio["tipo"] == "puntos":
        puntos += premio["valor"]
        print(f"Obtuviste {premio['valor']} puntos.")
    elif premio["tipo"] == "vida":
        vida += premio["valor"]
        print(f"¡Ganaste una vida extra! Tienes {vida} vidas.")
    elif premio["tipo"] == "pierde_todo":
        puntos = 0
        print("⚠️ Perdiste todos tus puntos ⚠️")

    return vida, puntos

def comparar_respuestas(resp_usuario: str, resp_correcta: str) -> bool:
    """Compara ignorando tildes, mayúsculas y espacios extras."""
    r1 = unidecode(resp_usuario.strip().lower())
    r2 = unidecode(resp_correcta.strip().lower())
    return r1 == r2
