from mini_juegos import jugar_si_o_no, jugar_completar_oracion, jugar_completar_palabra
from datos import datos_juegos

estado_inicial = {
    "vida": 1,
    "fichas": 2,
    "puntos": 0
}

funciones_juegos = {
    "si_o_no": jugar_si_o_no,
    "completar_oracion": jugar_completar_oracion,
    "completar_palabra": jugar_completar_palabra,
}    

premios = {
    "1": [{"tipo": "puntos", "valor": 1000000}],
    "2": [{"tipo": "puntos", "valor": 800000}, {"tipo": "puntos", "valor": 800000}],
    "3": [{"tipo": "puntos", "valor": 400000}, {"tipo": "puntos", "valor": 400000}],
    "4": [{"tipo": "puntos", "valor": 300000}, {"tipo": "puntos", "valor": 300000}, {"tipo": "puntos", "valor": 300000}],
    "5": [{"tipo": "puntos", "valor": 100000}, {"tipo": "puntos", "valor": 100000}, {"tipo": "puntos", "valor": 100000}, {"tipo": "puntos", "valor": 100000}],
    "6": [{"tipo": "puntos", "valor": 50000}, {"tipo": "puntos", "valor": 50000}],
    "7": [{"tipo": "vida", "valor": 1}],
    "8": [{"tipo": "pierde_todo", "valor": 0}]
}

tipos_de_juegos = list(funciones_juegos.keys())

preguntas = {
    "si_o_no": datos_juegos["si_o_no"].copy(),
    "completar_oracion": datos_juegos["completar_oracion"].copy(),
    "completar_palabra": datos_juegos["completar_palabra"].copy()
}

premios_disponibles = {
"1": premios["1"].copy(),
"2": premios["2"].copy(),
"3": premios["3"].copy(),
"4": premios["4"].copy(),
"5": premios["5"].copy(),
"6": premios["6"].copy(),
"7": premios["7"].copy(),
"8": premios["8"].copy()
}
