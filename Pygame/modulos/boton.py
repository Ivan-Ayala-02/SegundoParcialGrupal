import pygame

def crear_boton(dimensiones, posicion, ventana, color_borde,
                color_normal=(100, 100, 100), color_hover=(150, 150, 150), color_presionado=(200, 200, 200),
                imagen=None, fuente=None, texto=None):

    boton = {
        "ventana": ventana,
        "dimensiones": dimensiones,
        "posicion": posicion,
        "color_borde": color_borde,
        "presionado": False,
        "estado": "normal",
        "color_normal": color_normal,
        "color_hover": color_hover,
        "color_presionado": color_presionado,
        "imagen": None,
        "texto": texto,
        "fuente": fuente,
    }

    if imagen is not None:
        img = pygame.image.load(imagen)
        boton["imagen"] = pygame.transform.scale(img, dimensiones)
    else:
        tipo, tamanio = fuente
        fuente_pygame = pygame.font.SysFont(tipo, tamanio, True)
        boton["imagen"] = fuente_pygame.render(texto, True, "White")

    boton["rectangulo"] = pygame.Rect(posicion, dimensiones)

    return boton

def actualizar_estado_boton(boton):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()[0]

    if boton["rectangulo"].collidepoint(mouse_pos):
        if mouse_click:
            boton["estado"] = "presionado"
        else:
            boton["estado"] = "hover"
    else:
        boton["estado"] = "normal"

def dibujar_boton(boton):
    actualizar_estado_boton(boton)

    if boton["estado"] == "normal":
        color = boton["color_normal"]
    elif boton["estado"] == "hover":
        color = boton["color_hover"]
    elif boton["estado"] == "presionado":
        color = boton["color_presionado"]

    pygame.draw.rect(boton["ventana"], color, boton["rectangulo"])

    if boton["color_borde"] is not None:
        pygame.draw.rect(boton["ventana"], boton["color_borde"], boton["rectangulo"], 2)

    superficie = boton["imagen"]
    contenido_rect = superficie.get_rect(center=boton["rectangulo"].center)
    boton["ventana"].blit(superficie, contenido_rect)

def dibujar_lista_botones(lista):
    for boton in lista:
        dibujar_boton(boton)
