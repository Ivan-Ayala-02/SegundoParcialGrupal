from modulos.utilidades import validar_elemento    
from modulos.impresiones import imprimir_string_recuadro
from modulos.tiempo import mostrar_duracion
import time

###################################################################### INGRESO DE DATOS (INPUT) ######################################################################
def pedir_entrada(mensaje: str, validacion_funcion) -> str:
    respuesta = input(mensaje).strip().lower()
    while not validacion_funcion(respuesta):
        print("❌​ Entrada inválida. Intentá de nuevo. ❌​\n")
        respuesta = input(mensaje).strip().lower()
    
    return respuesta
#---------------------- INPUT (INGRESO DE DATOS) ----------------------#
def pedir_entrada_con_tiempo(mensaje, validacion_funcion, tiempo_limite):
    inicio = time.time()
    imprimir_string_recuadro(f"Tenes un límite de tiempo: {tiempo_limite} segundos.")
    print("(Escribí 'ficha' si querés cambiar la pregunta)")
    respuesta = pedir_entrada(mensaje, validacion_funcion)
    fin = time.time()

    duracion = fin - inicio

    if duracion > tiempo_limite:
        mostrar_duracion(duracion, tiempo_limite)
        respuesta = "timeout"

    return respuesta, duracion

def pedir_nombre_jugador() -> str:
    nombre_usuario = pedir_entrada("- Ingrese su nombre de usuario (sin espacios): ", es_cadena_vacia)
    confirmacion = pedir_entrada("- ¿Confirma su nombre de usuario? (si/no): ", es_si_o_no)

    while confirmacion == "no":
        print()
        nombre_usuario = pedir_entrada("- Ingrese su nombre de usuario (sin espacios): ", es_cadena_vacia)
        confirmacion = pedir_entrada("- ¿Confirma su nombre de usuario? (si/no): ", es_si_o_no)

    return nombre_usuario

# FUNCIONES CRITERIO / VALIDACIÓN #
#PARA INGRESO DE NOMBRE
def es_cadena_vacia(valor: str) -> bool:
    return not valor.strip() == ""
def es_si_o_no(valor: str) -> bool:
    return validar_elemento(["si", "no"], valor)

#PARA MINIJUEGO 
def es_si_no_o_ficha(valor: str) -> bool:
    return validar_elemento(["si", "no", "ficha"], valor)

def es_alfabetica(valor: str) -> bool:
    return valor.isalpha()

def es_numerico_o_ficha(valor: str) -> bool:
    return valor.isnumeric() or valor == "ficha"

def es_blanco_o_negro(valor: str) -> bool:
    return validar_elemento(["blanco", "negro"], valor)


