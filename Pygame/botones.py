import pygame

def crear_boton(dimensiones, posicion, ventana, color_borde, imagen = None, fuente = None, texto = None):
# Constructor
    boton = {}

    boton["ventana"] = ventana
    boton["dimensiones"] = dimensiones
    boton["posicion"] = posicion
    boton["color_borde"] = color_borde
    boton["presionado"] = False

    if imagen != None:
        img = pygame.image.load(imagen) 
        # Carga la iamgen
        boton["superficie"] = pygame.transform.scale(img, boton["dimensiones"])
        '''
        Transforma una imagen, en este caso,
        la escala segun la dimension indicada
        '''
    else:
        tipo, tamanio = fuente
        # Desempaquetado de una tupla
        # (Desempaqueto un dato complejo en dos datos mas chicos)
        fuente = pygame.font.SysFont(tipo, tamanio, True)
        #boton["superficie"] = fuente.render(texto, False, "Red", "Orange")
        boton["superficie"] = fuente.render(texto, True, "White")
        
    boton["rectangulo"] = boton["superficie"].get_rect()
    boton["rectangulo"].topleft = boton["posicion"]   

    return boton

def dibujar_boton(boton:dict):
    boton["ventana"].blit(boton["superficie"], boton["posicion"])
    if boton["color_borde"] is not None:
        pygame.draw.rect(boton["ventana"], boton["color_borde"], boton["rectangulo"], 2)

def dibujar_lista_botones(lista:list):
    for boton in lista:
        dibujar_boton(boton)