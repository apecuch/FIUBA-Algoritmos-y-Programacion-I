'''
FINAL ALGORITMOS I - 15/02/2024

    ALUMNO: Pecuch Agustina
    PADRON: 111560
    DNI: 40729147
'''

import csv

HEADERS_LIBROS = ["ISBN", "Título", "Autor", "Keywords", "Género literario", "Cantidad de páginas", "Valor"]
GENEROS_LITERARIOS = ["novela", "historia", "autoayuda"]
RUTA_ARCHIVO_LIBROS = "/workspaces/local_env/FINAL/libros.csv"
RUTA = "/workspaces/local_env/FINAL/"


def leer_archivo(ruta_archivo:str) -> list:
    """
    Lee un archivo y devuelve una lista de listas, donde cada lista representa
    una fila del archivo.
    """

    data = []

    try:
        with open(ruta_archivo, newline='', encoding="utf-8") as archivo:
            csv_reader = csv.reader(archivo, delimiter = ',')
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta_archivo}")
    except IOError:
        print(f"No se pudo leer el archivo: {ruta_archivo}")

    return data


def grabar_archivo(ruta_archivo:str, data:list):
    """
    Recibe una ruta y una lista.
    Se escribe un archivo por cada elemento en la lista y se guarda en la ruta proporcionada.
    """

    try:
        with open(ruta_archivo, 'w') as archivo:
            for linea in data:
                for value in linea.values():
                    if type(value) == list:
                        linea:str = "-".join(value)
                        archivo.write(f"{linea},")
                    else:
                        archivo.write(f"{value},")
                archivo.write("\n")

    except IOError:
        print(f"No se pudo grabar el archivo: {ruta_archivo}")


def cargar_datos(libros:list) -> None:
    """
    Se lee un archivo y por cada fila en el archivo se crea un diccionario.
    Cada diccionario se agrega a una lista que se recibe como parametro.
    """

    data:list = leer_archivo(RUTA_ARCHIVO_LIBROS)

    for linea in data:
        libro:dict = {}

        for x in range(len(linea)):

            if HEADERS_LIBROS[x] == "Keywords":
                libro[HEADERS_LIBROS[x]] = linea[x].split("-")
            else:    
                libro[HEADERS_LIBROS[x]] = linea[x]
        
        libros.append(libro)


def filtrar_por_valor_unico(data:list, clave:str, valor:str) -> dict:
    """
    Se filtra cada elemento de la lista, buscando donde coincida el valor indicado para la clave 
    y el valor recibidos por parametro.
    Se devuelve el objeto encontrado.
    """

    for elemento in data:
        if elemento.get(clave) == valor:
            return elemento


def filtrar_por_valor_repetido(data:list, clave:str, valor:str) -> list:
    """
    Se filtra cada elemento de la lista, buscando donde coincida el valor indicado para la clave 
    y el valor recibidos por parametro.
    Cada objeto que coincida con el criterio de busqueda se agrega a una lista que
    luego se devuelve.
    """

    data_filtrada:list = []

    for elemento in data:
        if elemento.get(clave) == valor:
            data_filtrada.append(elemento)

    return data_filtrada


def filtrar_por_keyword(libros:list, keyword:str) -> list:
    """
    Se filtra cada elemento de la lista, buscando aquellos elemento que contengan la keyword enviada
    por parametro.
    Cada objeto que coincida con el criterio de busqueda se agrega a una lista que
    luego se devuelve.
    """

    libros_filtrados:list = []

    for elemento in libros:
        for item in elemento.get("Keywords"):
            if item == keyword:
                libros_filtrados.append(elemento)

    return libros_filtrados


def eliminar_libro(libros:list) -> None:
    """
    Se solicita al usuario ingresar un ISBN para encontrar el libro correspondiente y eliminarlo.
    Al final se re-graba el archivo libros.csv para guardar los cambios.
    """

    isbn_libro:str = input("Ingrese el ISBN del libro que desea borrar: ")
    libro:dict = filtrar_por_valor_unico(libros, "ISBN", isbn_libro)

    libros.remove(libro)

    grabar_archivo(RUTA_ARCHIVO_LIBROS, libros)


def modificar_precio_libro(libros:list) -> None:
    """
    Se solicita al usuario ingresar un ISBN para encontrar el libro correspondiente y modificar su valor, el 
    cual también se le solicita al usuario.
    Al final se re-graba el archivo libros.csv para guardar los cambios.
    """

    isbn_libro:str = input("Ingrese el ISBN del libro que desea modificarle el precio: ")
    libro:dict = filtrar_por_valor_unico(libros, "ISBN", isbn_libro)

    precio_actual:str = libro.get("Valor")
    precio_nuevo:str = input(f"El precio actual es: ${precio_actual}. Ingrese el nuevo precio: ")

    libro.update({"Valor" : precio_nuevo})

    grabar_archivo(RUTA_ARCHIVO_LIBROS, libros)


def listar_libros(data:list) -> None:
    """
    Se listan los libros de una lista de una forma agradable para el usuario.
    """


    for libro in data:
        print(f">> {libro.get('Título')}")
        for x in range(len(HEADERS_LIBROS)-2):
            print(f"{HEADERS_LIBROS[x+2]} : {libro.get(HEADERS_LIBROS[x+2])}")
        print("")


def mostrar_libros_segun_keyword(libros:list) -> None:
    """
    Se le solicita al usuario ingresar una 'keyword' para proceder al filtrado de los libros que la contengan
    y mostrarselos al usuario.
    """

    keyword:str = input("Ingrese una [keyword] para comenzar el filtrado: ")
    libros_filtrados:list = filtrar_por_keyword(libros, keyword)

    print("")
    listar_libros(libros_filtrados)


def filtrar_libros_segun_genero(libros:list) -> None:
    """
    Se filtran todos los libros segun Genero Literario y se guardan en archivos correspondientes con el nombre
    del genero.
    """


    for genero in GENEROS_LITERARIOS:
        lista_libros:list = filtrar_por_valor_repetido(libros, "Género literario", genero)

        ruta_archivo:str = RUTA + genero + ".csv"
        grabar_archivo(ruta_archivo, lista_libros)


def calcular_promedio_libros(libros:list) -> float:
    """
    Se calcula el valor promedio entre todos los libros del archivo libros.csv
    """

    cantidad_libros:int = 0
    suma_valores:int = 0

    for libro in libros:
        suma_valores += int(libro.get("Valor"))
        cantidad_libros += 1

    return suma_valores // cantidad_libros


def mostrar_libros_debajo_promedio(libros:list) -> None:
    """
    Sefiltran los libros cuyo valor esten por debajo del promedio y se los muestra al usuario.
    """

    promedio:float = calcular_promedio_libros(libros)
    libros_debajo_promedio:list = []

    for libro in libros:
        if int(libro.get("Valor")) < promedio:
            libros_debajo_promedio.append(libro)

    print(f"Libros por debajo de ${promedio}:")
    print("")

    listar_libros(libros_debajo_promedio)


def mostrar_menu() -> None:
    print("")
    print("-"*10)
    print("Menu de Opciones:")
    print("")
    print("a - Eliminar un libro.")
    print("b - Modificar el precio de un libro.")
    print("c - Listar todos los títulos segun keyword.")
    print("d - Generar un archivo por cada género literario que exista.")
    print("e - Listar todos los libros cuyo valor estén por debajo del promedio de los mismos.")
    print("x - Salir.")
    print("-"*10)
    print("")


def elegir_opcion() -> str:
    mostrar_menu()
    opcion = (input("Elija una opcion: ")).lower()
    print("")

    while opcion not in ["a", "b", "c", "d", "e", "x"]:
        opcion = (input("¡OPCION INVALIDA! Elija una opcion valida: ")).lower()
        print("")

    return opcion


def main() -> None:
    libros:list = []
    cargar_datos(libros)

    opcion:str = elegir_opcion()

    while opcion != 'x':
        if opcion == "a":
            eliminar_libro(libros)
        elif opcion == "b":
            modificar_precio_libro(libros)
        elif opcion == "c":
            mostrar_libros_segun_keyword(libros)
        elif opcion == "d":
            filtrar_libros_segun_genero(libros)
        elif opcion == "e":
            mostrar_libros_debajo_promedio(libros)

        print("")
        print("+"*10)
        print("")

        opcion = elegir_opcion()


main()