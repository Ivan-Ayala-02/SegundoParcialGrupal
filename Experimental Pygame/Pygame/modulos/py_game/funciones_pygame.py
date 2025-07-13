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