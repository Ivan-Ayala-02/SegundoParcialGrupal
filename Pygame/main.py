# Valentin Luciano Avila - Iván Ayala
# División 211 - Grupo 14 

# Segundo Parcial: Juego de Preguntas y Respuestas Multietapas
from modulos.menus.menu_principal import menu_principal
from archivos.archivo_json import cargar_datos_json

estadisticas = cargar_datos_json("archivos/json/estadisticas.json")

menu_principal(estadisticas)

