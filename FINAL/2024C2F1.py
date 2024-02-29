import sys

ARCHIVO_SENSORES = "/workspaces/local_env/-/FIUBA-Algoritmos-y-Programacion-I/FINAL/2024C2F1.txt"
ARCHIVO_INFORMES = "/workspaces/local_env/-/FIUBA-Algoritmos-y-Programacion-I/FINAL/informe.txt"
HEADERS_SENSORES = ["id_sensor", "lat", "long", "tipo_sensor", "valor_estandar", "desviación", "valor_actual", "activo"]
HEADERS_ENTEROS = ["valor_estandar", "desviación", "valor_actual"]


def leer_archivo(ruta_archivo:str) -> list:

    """
    Lee un archivo y devuelve una lista de listas, donde cada lista representa
    una fila del archivo.
    """

    data = []

    try:
        with open(ruta_archivo, 'r') as archivo:
            for fila in archivo:
                sensor:str = fila.rstrip('\r\n')
                data.append(sensor.split(";"))
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta_archivo}")
    except IOError:
        print(f"No se pudo leer el archivo: {ruta_archivo}")

    return data


def validar_input_entero(data:str) -> int:

    """
    Valida que la entrada sea un número entero y lo devuelve.
    """

    valor:int = 0

    try:
        valor = int(data)
    except ValueError:
        print("Error: ¡Debe ser un numero!")
        sys.exit(1)

    return valor


def validar_input_booleano(data:str) -> bool:

    """
    Valida que la entrada sea un valor booleano ("True" o "False") y lo devuelve.
    """

    try:
        if data.lower() == "true":
            return True
        elif data.lower() == "false":
            return False
        else:
            raise ValueError("Error: ¡Debe ser True o False!")
    except ValueError as e:
        print(e)


def cargar_datos_automaticamente(sensores:list):

    data:list = leer_archivo(ARCHIVO_SENSORES)

    for linea in data:

        sensor:dict = {}

        for x in range(len(linea)):
            if HEADERS_SENSORES[x] in HEADERS_ENTEROS:
                sensor[HEADERS_SENSORES[x]] = validar_input_entero(linea[x])
            elif HEADERS_SENSORES[x] == "activo":
                sensor[HEADERS_SENSORES[x]] = validar_input_booleano(linea[x])
            else:
                sensor[HEADERS_SENSORES[x]] = linea[x]
        
        sensores.append(sensor)


def obtener_numero_id(sensores:list) -> str:

    id_sensor:int = int(sensores[-1]["id_sensor"]) + 1

    return str(id_sensor)


def cargar_datos_manualmente(sensores:list):

    sensor:dict = {}
    sensor["id_sensor"] = obtener_numero_id(sensores)

    for x in range(len(HEADERS_SENSORES)-1):

        print(f"Ingrese el valor para: [{HEADERS_SENSORES[x+1]}]")
        inp:str = input(">>> ")

        if HEADERS_SENSORES[x+1] in HEADERS_ENTEROS:
            sensor[HEADERS_SENSORES[x+1]] = validar_input_entero(inp)
        elif HEADERS_SENSORES[x+1] == "activo":
            sensor[HEADERS_SENSORES[x+1]] = validar_input_booleano(inp)
        else:
            sensor[HEADERS_SENSORES[x+1]] = inp

    sensores.append(sensor)


def filtrar_por_valor(data:list, clave:str, valor:str) -> dict:

    for elemento in data:
        if elemento.get(clave) == valor:
            return elemento


def modificar_sensor(sensores:list):

    id_sensor:str = input("Ingrese el id del sensor que desea modificar: ")
    sensor:dict = filtrar_por_valor(sensores, "id_sensor", id_sensor)

    estado_sensor:str = ""

    if sensor.get("activo"):
        estado_sensor = "ACTIVO"
        sensor.update({"activo" : False})
    else:
        estado_sensor = "INACTIVO"
        sensor.update({"activo" : True})

    print(f"El sensor {id_sensor} se encontraba {estado_sensor}. Se ha cambiado el estado del mismo.")


def mostrar_alertas_globales(sensores:list):

    sensores_por_encima:list = []
    sensores_por_debajo:list = []

    for sensor in sensores:

        if sensor.get("valor_actual") > (sensor.get("valor_estandar") + sensor.get("desviación")):
            sensores_por_encima.append(sensor.get("id_sensor"))
        elif sensor.get("valor_actual") < (sensor.get("valor_estandar") - sensor.get("desviación")):
            sensores_por_debajo.append(sensor.get("id_sensor"))

    print(f"Los sensores que superan el valor estándar + desviación: {sensores_por_encima}")
    print(f"Los sensores que estan por debajo del valor estándar - desviación: {sensores_por_debajo}")


def grabar_archivo(ruta_archivo:str, alertas:dict):

    try:
        with open(ruta_archivo, 'w') as archivo:
            for alerta, sensores in alertas.items():
                archivo.write(f"{alerta}:\n")
                for sensor in sensores:
                    archivo.write(f"- {sensor}\n")

    except IOError:
        print(f"No se pudo grabar el archivo: {ruta_archivo}")


def clasificar_alertas(sensores:list):

    alertas:dict = {}

    alertas_amarillas:list = []
    alertas_naranjas:list = []
    alertas_rojas:list = []

    for sensor in sensores:

        valor_conjunto:int = sensor.get("valor_estandar") + sensor.get("desviación")

        if sensor.get("valor_actual") < (valor_conjunto * 0.1):
            alertas_amarillas.append(sensor)
        elif sensor.get("valor_actual") > (valor_conjunto * 0.1) and sensor.get("valor_actual") < (valor_conjunto * 0.2):
            alertas_naranjas.append(sensor)
        elif sensor.get("valor_actual") > (valor_conjunto * 0.2):
            alertas_rojas.append(sensor)

    alertas["ALERTAS AMARILLAS"] = alertas_amarillas
    alertas["ALERTAS NARANJAS"] = alertas_naranjas
    alertas["ALERTAS ROJAS"] = alertas_rojas

    grabar_archivo(ARCHIVO_INFORMES, alertas)


def mostrar_menu() -> None:

    print("")
    print("-"*10)
    print("Menu de Opciones:")
    print("")
    print("a - Carga automática del archivo de sensores.")
    print("b - Carga manual de datos.")
    print("c - Activar o desactivar un sensor.")
    print("d - Listado de alertas globales.")
    print("e - Grabar alertas según su severidad.")
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


def main():

    sensores:list = []

    opcion:str = elegir_opcion()

    while opcion != 'x':
        if opcion == "a":
            cargar_datos_automaticamente(sensores)
        elif opcion == "b":
            cargar_datos_manualmente(sensores)
        elif opcion == "c":
            modificar_sensor(sensores)
        elif opcion == "d":
            mostrar_alertas_globales(sensores)
        elif opcion == "e":
            clasificar_alertas(sensores)

        print("")
        print("+"*10)
        print("")

        opcion = elegir_opcion()


main()