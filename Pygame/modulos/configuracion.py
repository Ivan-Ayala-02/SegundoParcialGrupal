from archivos.archivo_json import cargar_datos_json

configuracion_juego = cargar_datos_json("archivos/json/configuraciones.json")

ANCHO = configuracion_juego["ancho_pantalla"]
ALTO = configuracion_juego["alto_pantalla"]
LONGITUD_PANTALLA = (ANCHO, ALTO)