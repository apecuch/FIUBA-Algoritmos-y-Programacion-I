'''

EJERCICIO 1

Una importante empresa de catering para eventos quiere controlar su produccion.
Para esto nos pide crear un programa que permita ingresar la siguiente informacion:
    Id_Plato
    Nombre
    Valor

Por otro lado nos piden cargar los pedidos que van llegando de cada cliente, para esto nos piden cargar:
    Id_Pedido
    CUIT Cliente
    y todos los platos que haya pedido ese cliente, al menos debe pedir 1 plato

Se solicita:
    a. Agregar, Modificar, Eliminar un plato
    b. Agregar un pedido. Se debera listar los platos disponibles
    c. Listar un pedido por nro de CUIT
    d. Mostrar el pedido completo de mayor valor
    e. Mostrar el cliente que mas pedidos realizo hasta el momento, indicando el importe total gastado.
    f. Indicar el plato mas solicitado y la cantidad de veces que se pidio.

Se debe vigilar que al momento de crear un pedido, exista al menos un plato para ser agregado.


'''

def ingresarPlatoNuevo(platos:dict) -> None:

    nombre:str = input("Ingrese el nombre del plato nuevo: ")
    precio:float = float(input("Ingrese el valor del plato: "))

    id_plato:int = list(platos)[-1] +1

    plato:dict = {
        "nombre" : nombre,
        "valor" : precio
    }

    platos[id_plato] = plato

def modificarPlato(platos:dict) -> None:

    mostrarPlatos(platos)
    id_plato:int = int(input("Ingrese el ID del plato que desea modificar: "))
    nombre:str = platos[id_plato].get('nombre')
    valor:float = platos[id_plato].get('valor')
    opcion:str = (input("Ingrese 'NOMBRE' para modificar el nombre del plato. Ingrese 'VALOR' para modificar el valor del plato: ")).lower()

    if opcion == "nombre":
        nombre = input("Ingrese el nuevo nombre: ")
    elif opcion == "valor":
        valor = input("Ingrese el nuevo valor: ")
    
    platos[id_plato] = {
        "nombre" : nombre,
        "valor" : valor
    }

def eliminarPlato(platos:dict) -> None:

    mostrarPlatos(platos)
    id_plato:int = int(input("Ingrese el ID del plato que desea eliminar: "))

    platos.pop(id_plato)

def cargarPedidos(pedidos:dict, platosDisponibles:dict) -> None:

    corte:bool = True

    id_pedido:int = list(pedidos)[-1] +1
    cuit:str = input("Ingrese CUIT del cliente: ")
    print("")
    platos:list = []

    mostrarPlatos(platosDisponibles)  

    while corte:

        opcion:int = int(input("Ingrese el ID del plato que desea pedir o 0 para dejar de agregar platos: "))
        
        if opcion == 0:
            if len(platos) == 0:
                print("No se puede crear un pedido sin ningun plato!")
            else:
                corte = False
        elif opcion not in list(platosDisponibles.keys()):
            opcion:int = int(input("¡OPCION INVALIDA!. Ingrese un ID VALIDO del plato que desea pedir o 0 para dejar de agregar platos: "))
        
        if opcion in list(platosDisponibles.keys()):
            platos.append(opcion)
    
    pedidos[id_pedido] = {
        "cuit" : cuit,
        "platos" : platos
    }   

def listarPedido(pedidos:dict, platos:dict) -> None:

    cuit:str = input("Ingrese el numero de CUIT con el que se registro el pedido: ")

    for i in pedidos:
        if pedidos[i].get("cuit") == cuit:
            mostrarPedido(pedidos, platos, i)

def listarPedidoMayorValor(pedidos:dict, platos:dict) -> None:

    pedidoMayor:dict = {}
    mayor:float = 0

    for pedido in pedidos:
        sumaValores:float = 0
        for plato in pedidos[pedido].get("platos"):
            sumaValores += platos[plato].get("valor")

        if sumaValores > mayor:
            pedidoMayor = pedido
            mayor = sumaValores

    mostrarPedido(pedidos, platos, pedidoMayor)
    print("VALOR TOTAL: $", mayor)

def listarClienteConMasPedidos(pedidos:dict, platos:dict) -> None:

    listaUsuarios:list = []
    mayorCantidadPedidos:int = 0
    usuarioConMasPedidos:str = ""
    platosDelUsuario:list = []
    total:float = 0.0

    for pedido in pedidos:
        cuitCliente:str = pedidos[pedido].get("cuit")
        if cuitCliente not in listaUsuarios:
            listaUsuarios.append(cuitCliente)

    for usuario in listaUsuarios:
        cantidadPedidos:int = 0
        for pedido in pedidos:
            if pedidos[pedido].get("cuit") == usuario:
                cantidadPedidos += 1
        
        if cantidadPedidos > mayorCantidadPedidos:
            usuarioConMasPedidos = usuario
            mayorCantidadPedidos = cantidadPedidos

    for pedido in pedidos:
        if pedidos[pedido].get("cuit") == usuarioConMasPedidos:
            for plato in pedidos[pedido].get("platos"):
                platosDelUsuario.append(plato)

    for plato in platosDelUsuario:
        total += platos[plato].get("valor")

    print("El cliente con mayor cantidad de pedidos es:", usuarioConMasPedidos)
    print("- Gasto un total de:", total)

def listarPlatoMasSolicitado(pedidos:dict, platos:dict) -> None:

    platosPorCantidades:dict = {}
    platoMasSolicitado:int = 0

    for pedido in pedidos:
        for plato in list(pedidos[pedido].get("platos")):
            
            if plato not in platosPorCantidades:
                platosPorCantidades[plato] = 1
            else:
                platosPorCantidades[plato] += 1

    maximoSolicitudes:int = 0

    for plato in platosPorCantidades:
        if platosPorCantidades[plato] > maximoSolicitudes:
            platoMasSolicitado = plato
            maximoSolicitudes = platosPorCantidades[plato]
    
    print("El plato mas solicitado fue:", platos[platoMasSolicitado].get("nombre"), "pedido un total de:", platosPorCantidades[platoMasSolicitado], "veces.")

def mostrarPlatos(platos:dict) -> None:

    print("- PLATOS DISPONIBLES -")
    for plato in platos:
        print("-"*10)
        print("ID:", plato)
        print("NOMBRE:", (platos[plato].get('nombre')))
        print("VALOR:", (platos[plato].get('valor')))
        print("")

def mostrarPedido(pedidos:dict, platos:dict, idPedido:int) -> None:

    print("ID:", idPedido)
    print("CUIT:", pedidos[idPedido].get("cuit"))
    print("PLATOS:")
    for plato in pedidos[idPedido].get("platos"):
        print("-", platos[plato].get("nombre"))

def mostrarMenu() -> None:
    print("")
    print("-"*10)
    print("Menu de Opciones:")
    print("")
    print("a - Ingresar un plato nuevo.")
    print("b - Modificar un plato.")
    print("c - Eliminar un plato.")
    print("d - Cargar un pedido.")
    print("e - Listar un pedido por nro CUIT.")
    print("f - Listar pedido de mayor valor.")
    print("g - Listar cliente con mas pedidos.")
    print("h - Listar plato mas solicitado.")
    print("x - Salir.")
    print("-"*10)
    print("")

def elegirOpcion() -> str:
    mostrarMenu()
    opcion = (input("Elija una opcion: ")).lower()
    print("")

    while opcion not in ["a", "b", "c", "d", "e", "f", "g", "h", "x"]:
        opcion = (input("¡OPCION INVALIDA! Elija una opcion valida: ")).lower()
        print("")

    return opcion

def main() -> None:
    # Defino algunos platos iniciales -> { 1 : { "nombre" : "", "valor" : ""}}
    platos:dict = { 
        1 : {
            "nombre" : "Milanesa con pure",
            "valor" : 100.00
        },
        2 : {
            "nombre" : "Fideos con crema",
            "valor" : 80.00
        }           
    }
    # Defino un pedido inicial -> { idPedido : { "cuit" : "", "platos" : [ idplatos ] } }
    pedidos:dict = {
        1 : {
            "cuit" : "2740729147-1",
            "platos" : [ 1, 2 ]
        },
        2 : {
            "cuit" : "1234567-8",
            "platos" : [ 1 ]
        },
        3 : {
            "cuit" : "1234567-8",
            "platos" : [ 1 ]
        }
    } 

    opcion:str = elegirOpcion()

    while opcion != 'x':
        if opcion == "a":
            print(" >> Eligió la opcion: A")
            print("")
            ingresarPlatoNuevo(platos)
        elif opcion == "b":
            print(" >> Eligió la opcion: B")
            print("")
            modificarPlato(platos)
        elif opcion == "c":
            print(" >> Eligió la opcion: C")
            print("")
            eliminarPlato(platos)
        elif opcion == "d":
            print(" >> Eligió la opcion: D")
            print("")
            cargarPedidos(pedidos, platos)
        elif opcion == "e":
            print(" >> Eligió la opcion: E")
            print("")
            listarPedido(pedidos, platos)
        elif opcion == "f":
            print(" >> Eligió la opcion: F")
            print("")
            listarPedidoMayorValor(pedidos, platos)
        elif opcion == "g":
            print(" >> Eligió la opcion: G")
            print("")
            listarClienteConMasPedidos(pedidos, platos)
        elif opcion == "h":
            print(" >> Eligió la opcion: H")
            print("")
            listarPlatoMasSolicitado(pedidos, platos)

        opcion = elegirOpcion()

main()