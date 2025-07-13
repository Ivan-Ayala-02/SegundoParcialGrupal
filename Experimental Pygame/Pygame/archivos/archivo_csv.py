import re

def exportar_lista_diccionarios_a_csv(nombre_archivo: str, lista_diccionarios: list):
    if len(lista_diccionarios) == 0:
        print("La lista está vacía. No se generó el archivo.")
        return

    claves = list(lista_diccionarios[0].keys())

    with open(nombre_archivo, "w+", encoding="utf-8") as archivo:
        separador = ";"  # <- Este es el cambio clave

        linea_encabezados = separador.join(claves)
        archivo.write(linea_encabezados + "\n")

        for diccionario in lista_diccionarios:
            fila = []
            for clave in claves:
                valor = str(diccionario[clave])
                fila.append(valor)
            linea_datos = separador.join(fila)
            archivo.write(linea_datos + "\n")

    print(f"✅ Archivo '{nombre_archivo}' generado correctamente.")

def cargar_datos_csv(path: str) -> list:
    datos = []
    try:
        with open(path, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            if len(lineas) == 0:
                print("El archivo está vacío.")
                return datos

            claves = lineas[0].split(",")

            for linea in lineas[1:]:
                valores = linea.split(",")
                if len(valores) == len(claves):
                    fila = {}
                    for i in range(len(claves)):
                        clave = claves[i].strip()
                        valor = valores[i].strip()
                        fila[clave] = valor
                    datos.append(fila)
                else:
                    print(f"Línea con datos inválidos: {linea.strip()}")

        return datos
    except FileNotFoundError:
        print(f"No se encontró el archivo: {path}")
    except NotADirectoryError:
        print("Ingrese un directorio válido.")