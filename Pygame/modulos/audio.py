import pygame

def ajustar_volumen(volumen:int):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(volumen)