def cargar_texto_desde_archivo(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"No se encontró el archivo: {path}")
    except NotADirectoryError:
        print("Ingrese un directorio válido.")

def mostrar_texto(pantalla, texto, fuente, color_letras, espaciado, coordenada_inicial, scroll_mouse):
    import pygame
    lineas_texto = texto.split("\n")
    pos_x, pos_y = (coordenada_inicial)
    tipo_fuente, longitud_fuente = fuente
    fuente_texto = pygame.font.SysFont(tipo_fuente, longitud_fuente)
    
    pos_y += scroll_mouse

    for linea in lineas_texto:
        texto_renderizado = fuente_texto.render(linea, True, color_letras)
        pantalla.blit(texto_renderizado, (pos_x,pos_y))
        pos_y += espaciado
