HEADERS_CONTENEDORES = ["Nro de Contenedor", "Barrio", "latitud", "longitud", "Tipo de Contenedor", "Capacidad", "Peso Actual"]
ARCHIVO_CONTENEDORES = "/workspaces/local_env/-/FIUBA-Algoritmos-y-Programacion-I/FINAL/2024C2F2-contenedores.txt"


def leer_archivo(ruta_archivo:str) -> list:

    """
    Lee un archivo y devuelve una lista de listas, donde cada lista representa
    una fila del archivo.
    """

    data = []

    try:
        with open(ruta_archivo, 'r') as archivo:
            for fila in archivo:
                contenedor:str = fila.rstrip('\r\n')
                data.append(contenedor.split(";"))
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta_archivo}")
    except IOError:
        print(f"No se pudo leer el archivo: {ruta_archivo}")

    return data


def grabar_archivo(ruta_archivo:str, data:list):

    try:
        with open(ruta_archivo, 'w') as archivo:
            for linea in data:
                for value in linea.values():
                    archivo.write(f"{value};")
                archivo.write("\n")

    except IOError:
        print(f"No se pudo grabar el archivo: {ruta_archivo}")


def cargar_datos_automaticamente(contenedores:list):

    data:list = leer_archivo(ARCHIVO_CONTENEDORES)

    for linea in data:
        contenedor:dict = {}

        for x in range(len(linea)):
            contenedor[HEADERS_CONTENEDORES[x]] = linea[x]
        
        contenedores.append(contenedor)


def filtrar_por_valor(data:list, clave:str, valor:str) -> dict:

    for elemento in data:
        if elemento.get(clave) == valor:
            return elemento


def modificar_contenedor(contenedores:list):

    id_contenedor:str = input("Ingrese el id del contenedor que desea modificar: ")
    contenedor:dict = filtrar_por_valor(contenedores, "Nro de Contenedor", id_contenedor)

    for x in range(len(HEADERS_CONTENEDORES)-1):
        print(f"{x+1} >> {HEADERS_CONTENEDORES[x+1]}")

    inp:int = int(input("Ingrese el numero de la propiedad que desea modificar: "))
    propiedad:str = HEADERS_CONTENEDORES[inp]

    cambio:str = input(f"Ingrese el nuevo valor para la propiedad [{propiedad}]: ")

    contenedor.update({ propiedad : cambio })

    grabar_archivo(ARCHIVO_CONTENEDORES, contenedores)


def main() -> None:
    
    contenedores:list = []

    cargar_datos_automaticamente(contenedores)
    modificar_contenedor(contenedores)

main()