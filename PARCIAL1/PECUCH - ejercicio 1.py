'''

PARCIAL ALGORITMOS I - 12/10/2023

    ALUMNO: Pecuch Agustina
    PADRON: 111560
    DNI: 40729147

'''
def cargarVenta(ventas:dict, paquetesTuristicos:dict) -> None:

    idVenta:int = list(ventas)[-1] +1

    dni:int = int(input("Ingrese el numero de DNI del cliente: "))
    nombreCompleto:str = input("Ingrese el nombre completo del cliente: ")
    destinoTuristico:str = (input("Ingrese el destino turistico deseado: ")).lower()
    paquete:int = elegirPaqueteTuristico(paquetesTuristicos, destinoTuristico)
    cantidadPasajeros:int = int(input("Ingrese la cantidad de pasajeros: "))
    valor:float = paquetesTuristicos[paquete].get("valor") * cantidadPasajeros

    venta:dict = {
        "DNI" : dni,
        "nombreCompleto" : nombreCompleto,
        "destinoTuristico" : destinoTuristico,
        "paqueteTuristico" : paquete,
        "cantidadPasajeros" : cantidadPasajeros,
        "valor" : valor
    }

    ventas[idVenta] = venta

def cargarPaqueteTuristico(paquetesTuristicos:dict) -> None:

    idPaquete:int = list(paquetesTuristicos)[-1] +1

    nombrePaquete:str = input("Ingrese el nombre del paquete: ")
    destino:str = (input("Ingrese el destino: ")).lower()
    cantidadDias:int = int(input("Ingrese la cantidad de dias: "))
    valor:float = float(input("Ingrese el valor del paquete: "))

    paquete:dict = {
        "nombrePaquete" : nombrePaquete,
        "destino" : destino,
        "cantidadDias" : cantidadDias,
        "valor": valor
    }

    paquetesTuristicos[idPaquete] = paquete

def elegirPaqueteTuristico(paquetesTuristicos:dict, destino:str) -> int:

    mostrarPaquetesTuristicos(paquetesTuristicos, destino)
    destino:int = int(input("Ingrese el numero de paquete que desea adquirir: "))

    return destino

def listarVentasPorDestino(ventas:dict) -> None:

    destino:str = (input("Ingrese el destino para el que desea buscar las ventas realizadas hasta el momento: ")).lower()
    numeroVenta:int = 1
    
    for venta in ventas:
        
        if ventas[venta].get("destinoTuristico") == destino:
            print(numeroVenta, ":")
            print("DNI CLIENTE:", ventas[venta].get("DNI"))
            print("NOMBRE COMPLETO:", ventas[venta].get("nombreCompleto"))
            print("PAQUETE TURISTICO SELECCIONADO:", ventas[venta].get("paqueteTuristico"))
            print("CANTIDAD PASAJEROS:", ventas[venta].get("cantidadPasajeros"))
            print("VALOR: $", ventas[venta].get("valor"))
            print("-")

            numeroVenta += 1

def listarPaqueteMasvendido(ventas:dict, paquetesTuristicos:dict) -> None:

    listaPaquete:list = list(paquetesTuristicos.keys())
    paquetesPorVentas:dict = {} # idpaquete : ventas
    cantidadVentas:int = 0
    paqueteMasVendido:int = 0
    clientes:list = []

    for venta in ventas:
        for paquete in listaPaquete:
            if ventas[venta].get("paqueteTuristico") == paquete:
                if paquete not in list(paquetesPorVentas.keys()):
                    paquetesPorVentas[paquete] = 1
                else:
                    paquetesPorVentas[paquete] += 1

    for paquete in paquetesPorVentas:
        if paquetesPorVentas[paquete] > cantidadVentas:
            paqueteMasVendido = paquete
            cantidadVentas = paquetesPorVentas[paquete]

    for venta in ventas:
        if ventas[venta].get("paqueteTuristico") == paquete:
            clientes.append(ventas[venta].get("nombreCompleto"))

    print("El paquete mas vendido fue:", paquetesTuristicos[paqueteMasVendido].get("nombrePaquete"))
    print("Se adquirio un total de", cantidadVentas, "veces por los siguientes compradores:", clientes)

def listarPasajeroConMasReservas(ventas:dict) -> None:

    clientesPorPedidos:dict = {} # dniCliente : cantidadVentas
    cantidadReservas:int = 0
    clienteConMasVentas:int = 0
    nombrecliente:str = ""

    for venta in ventas:
        if ventas[venta].get("DNI") not in list(clientesPorPedidos.keys()):
            clientesPorPedidos[ventas[venta].get("DNI")] = 1
        else:
            clientesPorPedidos[ventas[venta].get("DNI")] += 1

    for cliente in clientesPorPedidos:
        if clientesPorPedidos[cliente] > cantidadReservas:
            clienteConMasVentas = cliente
            cantidadReservas = clientesPorPedidos[cliente]

    for venta in ventas:
        if ventas[venta].get("DNI") == clienteConMasVentas:
            nombrecliente = ventas[venta].get("nombreCompleto")

    print("El cliente que mas ventas realizo fue:")
    print("- DNI:", clienteConMasVentas)
    print("- NOMBRE COMPLETO:", nombrecliente)
    print("- CANTIDAD DE RESERVAS:", cantidadReservas)

def listarVentasMayoresAlPromedio(ventas:dict) -> None:
     
    valorTotalVentas:float = 0.0
    cantidadTotalVentas:int = len(ventas)
    ventasMayoresAlPromedio:list = []

    for venta in ventas:
        valorTotalVentas += ventas[venta].get("valor")

    promedioValor:float = valorTotalVentas // cantidadTotalVentas

    for venta in ventas:
        if ventas[venta].get("valor") > promedioValor:
            ventasMayoresAlPromedio.append(venta)

    print("Ventas con valores mayores al promedio:", ventasMayoresAlPromedio)

def mostrarPaquetesTuristicos(paquetesTuristicos:dict, destino:str) -> None:
    print("")
    print("- PAQUETES TURISTICOS DISPONIBLES - destino:", destino)

    for paquete in paquetesTuristicos:

        if paquetesTuristicos[paquete].get("destino") == destino:

            print("-"*10)
            print("ID PAQUETE:", paquete)
            print("NOMBRE:", (paquetesTuristicos[paquete].get('nombrePaquete')))
            print("CANTIDAD DE DIAS:", (paquetesTuristicos[paquete].get('cantidadDias')))
            print("VALOR POR PERSONA:", (paquetesTuristicos[paquete].get('valor')))
            print("")

def mostrarMenu() -> None:
    print("")
    print("-"*10)
    print("Menu de Opciones:")
    print("")
    print("a - Cargar una nueva venta.")
    print("b - Cargar un nuevo paquete.")
    print("c - Listar ventas por destino.")
    print("d - Mostrar paquete mas vendido.")
    print("e - Mostrar cliente con mayor cantidad de reservas.")
    print("f - Listar ventas mayores al promedio.")
    print("x - Salir.")
    print("-"*10)
    print("")

def elegirOpcion() -> str:
    mostrarMenu()
    opcion = (input("Elija una opcion: ")).lower()
    print("")

    while opcion not in ["a", "b", "c", "d", "e", "f", "x"]:
        opcion = (input("¡OPCION INVALIDA! Elija una opcion valida: ")).lower()
        print("")

    return opcion


def main() -> None:
    
    # Defino una ventas inicial -> ventas = { dni : { nombreCompleto : "" , destinoTuristico : "" , paqueteTuristico : [] , cantidadPasajeros : int, valor : float   } }
    ventas:dict = { 
        1 : {
            "DNI" : 40729147,
            "nombreCompleto" : "Agustina Pecuch",
            "destinoTuristico" : "francia",
            "paqueteTuristico" : 1,
            "cantidadPasajeros" : 1,
            "valor" : 100.00
        },
        2 : {
            "DNI" : 123456,
            "nombreCompleto" : "Susana Panarotti",
            "destinoTuristico" : "brasil",
            "paqueteTuristico" : 2,
            "cantidadPasajeros" : 2,
            "valor" : 200.00
        },
        3 : {
            "DNI" : 40729147,
            "nombreCompleto" : "Agustina Pecuch",
            "destinoTuristico" : "brasil",
            "paqueteTuristico" : 2,
            "cantidadPasajeros" : 3,
            "valor" : 300.00
        }
    }             

    # Defino algunos paquetes turisticos iniciales ->  paquetesTuristicos = { 1 : { nombrePaquete: "" , destino: "", cantidadDeDias: 1, valor : 10.0 } }
    paquetesTuristicos:dict = {
        1 : {
            "nombrePaquete" : "Francia Romantico",
            "destino" : "francia",
            "cantidadDias" : 20,
            "valor": 100.00
        },
        2 : {
            "nombrePaquete" : "Brasil Magico",
            "destino" : "brasil",
            "cantidadDias" : 10,
            "valor": 50.00
        }
    }

    opcion:str = elegirOpcion()

    while opcion != 'x':
        if opcion == "a":
            print(" >> Eligió la opcion: A")
            print("")
            cargarVenta(ventas, paquetesTuristicos)
        elif opcion == "b":
            print(" >> Eligió la opcion: B")
            print("")
            cargarPaqueteTuristico(paquetesTuristicos)
        elif opcion == "c":
            print(" >> Eligió la opcion: C")
            print("")
            listarVentasPorDestino(ventas)
        elif opcion == "d":
            print(" >> Eligió la opcion: D")
            print("")
            listarPaqueteMasvendido(ventas, paquetesTuristicos)
        elif opcion == "e":
            print(" >> Eligió la opcion: E")
            print("")
            listarPasajeroConMasReservas(ventas)
        elif opcion == "f":
            print(" >> Eligió la opcion: F")
            print("")
            listarVentasMayoresAlPromedio(ventas)

        print("")
        print("+"*10)
        print("")

        opcion = elegirOpcion()

main()