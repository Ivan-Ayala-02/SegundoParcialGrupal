import pygame

def crear_ventana(ancho:int, alto:int) -> tuple:
    VENTANA = pygame.display.set_mode((ancho,alto))
    return VENTANA

def generar_nombre_e_icono_ventana(texto_ventana:str, path_icono:str):
    pygame.display.set_caption(texto_ventana)
    icono_ventana = cargar_imagen(path_icono)
    pygame.display.set_icon(icono_ventana)

def cargar_imagen(path_imagen:str):
    imagen = pygame.image.load(path_imagen)
    return imagen

def mostrar_imagen(imagen, ventana, coordenadas):
    ventana.blit(imagen, coordenadas)

def mover_imagen(coordenadas_base:list, coordenadas_final:list, velocidad=1) -> bool:
    
    for i in range(2):
        if coordenadas_base[i] < coordenadas_final[i]:
            coordenadas_base[i] += velocidad
            if coordenadas_base[i] > coordenadas_final[i]:
                coordenadas_base[i] = coordenadas_final[i]
        elif coordenadas_base[i] > coordenadas_final[i]:
            coordenadas_base[i] -= velocidad
            if coordenadas_base[i] < coordenadas_final[i]:
                coordenadas_base[i] = coordenadas_final[i]

    if (coordenadas_base[0] == coordenadas_final[0]) and (coordenadas_base[1] == coordenadas_final[1]):
        estado_animacion = True
    else:
        estado_animacion = False
    return estado_animacion

def cargar_audio(path_audio:str):
    pygame.mixer.music.load(path_audio)

def ajustar_volumen(volumen:int):
    pygame.mixer.music.set_volume(volumen)

def mostrar_imagenes_intro(fondo, pantalla, logo, coord_logo, barassi, coord_barassi):
    mostrar_imagen(fondo, pantalla, (0,0))
    mostrar_imagen(logo, pantalla, coord_logo)
    mostrar_imagen(barassi, pantalla, coord_barassi)

def animar_imagen(PANTALLA, fondo, logo_juego, coordenadas_logo, coordenadas_destino, velocidad):

    animacion_finalizada = mover_imagen(coordenadas_logo, coordenadas_destino, velocidad)
    mostrar_imagen(fondo, PANTALLA, (0,0))
    mostrar_imagen(logo_juego, PANTALLA, coordenadas_logo)

    if animacion_finalizada:
        return True
    else:
        return False
    
def cargar_imagenes_intro():
    fondo = cargar_imagen("recursos/fondo.jpg")
    logo_juego = cargar_imagen("recursos/icono_menu.png")
    barassi = cargar_imagen("recursos/barassi_menu.png")
    return fondo, logo_juego, barassi

def crear_input(ventana, fuente, color_activo, color_inactivo, posicion, dimensiones):
    input = {}
    input["ventana"] = ventana 
    input["fuente"] = pygame.font.SysFont(fuente[0], fuente[1])
    input["color_activo"] = color_activo
    input["color_inactivo"] = color_inactivo
    input["texto"] = ""
    input["activo"] = False
    x, y = posicion
    input["posicion"] = posicion
    w, h = dimensiones
    input["dimensiones"] = dimensiones
    input["rectangulo"] = pygame.Rect(x+5, y+7, w, h)
    # Rect = Rectangulo coneptual
    input["color_actual"] = input["color_inactivo"]

    return input

def dibujar_input(input_box):
    texto = input_box["fuente"].render(input_box["texto"], False, input_box["color_actual"])
    x = input_box["rectangulo"].x
    y = input_box["rectangulo"].y
    input_box["ventana"].blit(texto, (x, y))
    pygame.draw.rect(input_box["ventana"], input_box["color_actual"], input_box["rectangulo"], 1)


def escribir(input_box, evento):
    if evento.key == pygame.K_ESCAPE:
        input_box["texto"] = ""
    elif evento.key == pygame.K_BACKSPACE:
        input_box["texto"] = input_box["texto"][:-1]
    else:
        input_box["texto"] += evento.unicode
