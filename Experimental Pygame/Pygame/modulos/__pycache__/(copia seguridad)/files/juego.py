from auxiliares import *

def ingresar_usuario() -> str:
    mensaje_usuario = "Ingrese usuario: "
    mensajer_error_usuario = "Error... Ingrese usario dentro de caracteres validos: "

    usuario = ingreso_y_verificacion_cadena(mensaje_usuario, 
                                            mensajer_error_usuario, 
                                            verificar_cadena, 
                                            letras=verificar_caracter_letra)
    
    return usuario
