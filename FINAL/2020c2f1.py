import re
import csv

ARCHIVO_ALUMNOS = "/workspaces/local_env/-/FIUBA-Algoritmos-y-Programacion-I/FINAL/2020C2F1-alumnos.csv"
ARCHIVO_MATERIAS = "/workspaces/local_env/-/FIUBA-Algoritmos-y-Programacion-I/FINAL/2020C2F1-materias.csv"

HEADERS_ALUMNOS = ["Padrón", "Nombre", "Apellido", "Carrera", "Año de Ingreso"]
HEADERS_HISTORIA_ACADEMICA = ["Padrón", "Materias"]
HEADERS_MATERIA = ["Materia", "Nota"]


def leer_archivo(archivo:str) -> list:
    data = []

    try:
        with open(archivo, newline='', encoding="utf-8") as archivo:
            csv_reader = csv.reader(archivo, delimiter = ',')
            next(csv_reader)
            for row in csv_reader:
                data.append(row)
    except IOError:
        print("\nNo se pudo leer el archivo: ", archivo)

    return data


def filtrar_valores_unicos(data:list, key:str):
    data_filtrada:list = []
    valores_unicos:dict = {}

    for x in data:
        valor_por_clave = x[key]
        valores_unicos[valor_por_clave] = x

    data_filtrada = list(valores_unicos.keys())

    return data_filtrada


def filtrar_valores_por_clave(data:list, key:str, valor:str):
    
    data_filtrada:list = []

    for x in data:
        if x.get(key) == valor:
            data_filtrada.append(x)

    return data_filtrada


def formatear_informacion_alumno(data:list):

    alumno:dict = {}

    for x in range(len(HEADERS_ALUMNOS)):
        alumno[HEADERS_ALUMNOS[x]] = data[x] 

    return alumno


def formatear_informacion_materias(data:list):
   
    materias:list = []
    historia_academica:dict = {}

    contador:int = len(data) // 2

    historia_academica[HEADERS_HISTORIA_ACADEMICA[0]] = data[0]
    data.pop(0)

    for x in range(contador):
        materia:dict = {}
        materia[HEADERS_MATERIA[0]] = data[x*2]
        materia[HEADERS_MATERIA[1]] = data[x*2 + 1]

        materias.append(materia)

    historia_academica[HEADERS_HISTORIA_ACADEMICA[1]] = materias
        

    return historia_academica


def procesar_informacion():
    
    alumnos:list = []
    historias_academicas:list = []
    data_alumnos:list = leer_archivo(ARCHIVO_ALUMNOS)
    data_materias:list = leer_archivo(ARCHIVO_MATERIAS)

    for x in range(len(data_alumnos)):
        alumnos.append(formatear_informacion_alumno(data_alumnos[x]))

    for x in range(len(data_materias)):
        historias_academicas.append(formatear_informacion_materias(data_materias[x]))

    return alumnos, historias_academicas


def determinar_antiguedad_promedio(alumnos:list):

    materias:list = filtrar_valores_unicos(alumnos, 'Carrera')
    antiguedad:list = []

    año:int = int(input("Ingrese año actual: "))

    for materia in materias:
        años:int = 0
        cant_alumnos:int = 0

        for alumno in alumnos:
            if alumno.get('Carrera') == materia:
                años += int(alumno.get('Año de Ingreso'))
                cant_alumnos += 1

        antiguedad.append(round(año - años/cant_alumnos))

    for x in range(len(materias)):
        print("La carrera", materias[x], "tiene antiguedad promedio:", antiguedad[x], "años, al año", año)


def determinar_mejor_alumno(historias_academicas:list, alumnos:list):

    mejor_promedio:int = 0
    padron_mejor_alumno:str = ''
    mejor_alumno:dict = {}

    for padron in historias_academicas:

        notas:int = 0
        cant_materias:int = 0
        promedio:int = 0

        for materia in padron.get('Materias'):

            notas += int(materia.get('Nota'))
            cant_materias += 1

        promedio = notas / cant_materias

        if promedio > mejor_promedio:
            padron_mejor_alumno = padron.get('Padrón')
            mejor_promedio = promedio

    for alumno in alumnos:
        if alumno.get('Padrón') == padron_mejor_alumno:
            mejor_alumno = alumno

    print("Mejor alumno activo es", mejor_alumno.get('Nombre'), mejor_alumno.get('Apellido'), "con un promedio de", mejor_promedio)


def determinar_materias_aprobadas_por_carrera(alumnos:list, historias_academicas:list):

    inp_carrera:str = input("Ingrese una carrera: ")
    alumnos_por_carrera:list = filtrar_valores_por_clave(alumnos, 'Carrera', inp_carrera)
    padrones:list = []
    cant_materias_aprobadas:int = 0

    for alumno in alumnos_por_carrera:
        padrones.append(alumno.get('Padrón'))

    for historia in historias_academicas:
        if historia.get('Padrón') in padrones:
            for materia in historia.get('Materias'):
                if int(materia.get('Nota')) >= 4:
                    cant_materias_aprobadas += 1
        
    promedio:int = cant_materias_aprobadas / len(alumnos_por_carrera)

    print("El promedio de materias aprobadas de la carrera", inp_carrera, "con una cantidad de alumnos de", len(alumnos_por_carrera), "es de", promedio)


def get_departamentos(historias_academicas:list) -> list:

    departamentos:list = []

    for historia in historias_academicas:
        for materia in historia.get('Materias'):
            departamento:str = materia.get('Materia').split(".")[0]

            if departamento not in departamentos:
                departamentos.append(departamento)

    return departamentos


def determinar_mejor_departamenmto(historias_academicas:list):

    departamentos:list = get_departamentos(historias_academicas)
    mejor_departamento:str = ""
    mejor_promedio:int = 0

    for departamento in departamentos:

        cant_materias:int = 0
        cant_materias_aprobadas:int = 0

        for historia in historias_academicas:
            for materia in historia.get('Materias'):
                if materia.get('Materia').startswith(departamento):
                    if int(materia.get('Nota')) >= 4:
                        cant_materias_aprobadas += 1
                    cant_materias += 1
        
        promedio:int = cant_materias_aprobadas / cant_materias

        if promedio > mejor_promedio:
            mejor_departamento = departamento
            mejor_promedio = promedio

    print("El '{0}', es el departamento con mayor cantidad de materias aprobadas por alumnos, con una cantidad de {1} materias aprobadas")


def mostrar_menu() -> None:

    print("")
    print("-"*10)
    print("Menu de Opciones:")
    print("")
    print("a - Cargar un nuevo alumno.")
    print("b - Determinar la antigüedad promedio por carrera de los alumnos activos.")
    print("c - Indicar cual es el mejor alumno activo de la facultad (en base a su promedio).")
    print("d - Determinar el promedio de materias aprobadas de los alumnos de una carrera.")
    print("e - Indicar cual es el departamento con mayor cantidad de materias aprobadas por alumnos.")
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
    opcin:str = ""
    alumnos:list = []
    historias_academicas:list = []

    """
    alumnos = [{
                'Padron' : '',
                'Nombre' : '',
                'Apellido' : '',
                'Carrera' : '',
                'Año de Ingreso' : ''
              }]

    historias_academicas = [{
                            'Padron' : '',
                            'Materias' : [{
                                           'Materia' : '',
                                           'Nota' : '' 
                            }]
    }]
    """


    alumnos, historias_academicas = procesar_informacion()
    determinar_antiguedad_promedio(alumnos)
    determinar_mejor_alumno(historias_academicas, alumnos)
    determinar_materias_aprobadas_por_carrera(alumnos, historias_academicas)
    determinar_mejor_departamenmto(historias_academicas)

main()