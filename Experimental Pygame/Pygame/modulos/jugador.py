# MOSTRAR DATOS (VIDA Y PUNTOS) DEL JUGADOR CON EMOJIS 
def representar_dato_con_emojis(dato: str, cantidad: int):
    if dato == "vida":
        texto = f'💖 ' * cantidad
    elif dato == "fichas":
        texto = f'🎟️ ' * cantidad
    else:
        texto = "No hay representación con emojis"

    return texto

def imprimir_estado_del_jugador(estado_jugador: dict): 
    vida = estado_jugador["vida"]
    fichas = estado_jugador["fichas"]
    puntos = estado_jugador["puntos"]

    vida_emojis = representar_dato_con_emojis("vida", vida)
    fichas_emojis = representar_dato_con_emojis("fichas", fichas)

    print(f"Vida: {vida_emojis:<15} | Fichas: {fichas_emojis:<15} | Puntos: {puntos}")


def registrar_nuevo_usuario(estadisticas: dict) -> str | None:
    print()
    nombre = input("📝 Ingresá el nombre del nuevo usuario: ").strip()

    # Verificamos si ya existe el perfil
    existe = False
    for clave in estadisticas:
        if clave == nombre:
            existe = True
            break

    if existe:
        print(f"⚠️  El perfil '{nombre}' ya existe. Elegí la opción 2 para seleccionarlo ⚠️")
        return None

    # Si no existe, se crea
    estadisticas[nombre] = {"partidas": []}
    print(f"✅  Usuario '{nombre}' registrado correctamente ✅")
    return nombre


def seleccionar_perfil(estadisticas: dict) -> str | None:
    if len(estadisticas) == 0:
        print("⚠️  No hay perfiles registrados aún ⚠️")
        return None

    print("\n👤 Perfiles disponibles:")
    for clave in estadisticas:
        print(f"| {clave}", end="")

    nombre = input("\n- Ingresá el nombre EXACTO del perfil que querés usar: ").strip()

    existe = False
    for clave in estadisticas:
        if clave == nombre:
            existe = True
            break

    if not existe:
        print(f"❌ El perfil '{nombre}' no existe. Usá la opción 1 para registrarlo ❌")
        return None

    print(f"✅ Perfil '{nombre}' seleccionado correctamente ✅")
    return nombre