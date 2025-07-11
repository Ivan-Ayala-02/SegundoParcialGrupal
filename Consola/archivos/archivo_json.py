import json

def guardar_diccionario(path: str, diccionario: dict):
    try:
        with open(path, "w", encoding = "utf-8") as archivo_json:
            json.dump(diccionario, archivo_json, ensure_ascii = False, indent = 4)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {path}")
    except NotADirectoryError:
        print("Ingrese un directorio válido.")

def cargar_datos_json(path: str) -> dict:
    datos = {}
    try:
        with open(path, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

            if len(contenido.strip()) == 0:
                print("El archivo JSON está vacío.")
                return datos

            datos = json.load(open(path, "r", encoding="utf-8"))
            return datos
    except FileNotFoundError:
        print(f"No se encontró el archivo: {path}")
    except json.JSONDecodeError:
        print("Error: El archivo JSON no tiene un formato válido.")
        return datos
    except NotADirectoryError:
        print("Ingrese un directorio válido.")