def cargar_texto_desde_archivo(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"No se encontró el archivo: {path}")
    except NotADirectoryError:
        print("Ingrese un directorio válido.")