'''

Trabajo Práctico 1 - Pirámide de Palitos

[75.40] Algoritmos y Programación I

    Alumno:	            Pecuch Agustina
    Padrón:	            111560
    DNI:	            40720147
    Email:	            apecuch@fi.uba.ar
    Fecha de Entrega:	24 de Octubre de 2023

'''

import random # Utilizado para la eleccion de palitos de la máquina.
from os import system, name # Utilizado para limpiar la consola.
from time import sleep # Utilizado para detener el juego y que no se borre tan rapido la consola.
from math import sqrt, ceil # Utilizado para calcular el promedio de los palitos
from colorama import init, Fore, Style # Utilizado con proposito decorativo.


# Inicializo colorama
init(autoreset=True)

# Constantes JUGADOR
NOMBRE_JUGADOR = 0
TURNOS = 1
PALITOS_SACADOS = 2

# Constantes TABLERO
PALITO_BASE = ["|", False, 0]
PALITO = 0
ES_ROJO = 1
BLOQUEADO = 2


def clear() -> None:

    '''
    Esta función limpia la consola.
    '''
    # windows
    if name == 'nt':
        _ = system('cls')

   # linux y mac
    else:
        _ = system('clear')


def iniciarJuego() -> None:

    '''
    Esta función simplemente imprime un titulo con color al inicio del juego.
    '''
   
    titulo:str = "ʕ•́ᴥ•̀ʔ ¡Bienvenidos al juego de los palitos chinos!"
    tituloColor:str = f"{Fore.MAGENTA}{Style.BRIGHT}{titulo}{Style.RESET_ALL}"
    guion:str = "-"*65

    print("")
    print(f"{Fore.CYAN}{Style.BRIGHT}{guion}{Style.RESET_ALL}")
    print("     " + tituloColor + "     ")
    print(f"{Fore.CYAN}{Style.BRIGHT}{guion}{Style.RESET_ALL}")
    print("")


def finalizarJuego(jugador:list) -> None:

    '''
    Esta función simplemente imprime el jugador perdedor.
    '''

    guion:str = "-"*60
    print(f"{Fore.CYAN}{Style.BRIGHT}{guion}{Style.RESET_ALL}")

    titulo:str = "ʕ•́ᴥ•̀ʔ El jugador que PERDIO porque quito el ultimo palito es ..."
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{titulo}{Style.RESET_ALL}")
    print("")
    print(f"     {Fore.CYAN}{Style.BRIGHT}¡{jugador[NOMBRE_JUGADOR]}!{Style.RESET_ALL}")
    print("")

    texto:str = "Quito un total de " + str(jugador[PALITOS_SACADOS]) + " palitos."
    print(f"{Fore.CYAN}{Style.BRIGHT}{texto}{Style.RESET_ALL}")

    print(f"{Fore.CYAN}{Style.BRIGHT}{guion}{Style.RESET_ALL}")


def elegirJugadores() -> list:

    '''
    Esta función inicializa la lista de jugadores. Dependiendo de la cantidad de jugadores que se ingrese se crearan:
        - Un jugador real con el nombre del jugador.
        - El resto de jugadores seran maquinas con el nombre "Maquina(nro)".
    A cada jugador tambien se le asigna dos valores int para indicar la cantidad de turnos que debe perder y la cantidad de palitos que lleva sacados.
    Al comienzo del juego a todos los jugadores se les asigna "0"
    '''

    jugador:list = []
    jugadores: list = []

    cantidadJugadores = int(input("Ingrese la cantidad de jugadores: "))
    # Valido que no ingrese un numero menor a 2.
    if cantidadJugadores < 2:
        cantidadJugadores = int(input("No podes jugar solo! Elegi nuevamente la cantidad de jugadores: "))

    nombreJugador = input("Ingrese su nombre: ")

    jugador = [nombreJugador, 0, 0]
    jugadores.append(jugador)

    for i in range(cantidadJugadores-1):
        nombreMaquina = "Maquina" + str(i+1)
        jugador = [nombreMaquina, 0, 0]
        jugadores.append(jugador)

    return cantidadJugadores, nombreJugador, jugadores


def calcularCantidadPalitosMinima(cantidadJugadores:int) -> int:
    
    '''
    Esta función calcula la cantidad de palitos MINIMA para inicializar el tablero, basada en la cantidad de jugadores.
    '''
    
    cantidadPalitosMinima = ((cantidadJugadores + 2) * (cantidadJugadores + 3)) // 2

    return cantidadPalitosMinima


def calcularCantidadPalitos(cantidadJugadores:int) -> int:

    '''
    Esta funcion consulta al usuario con cuantos palitos desea jugar y chequea que no sea menor a la cantidad mínima requerida.
    '''
    
    cantidadPalitos:int = 0
    cantidadPalitosMinima:int = 0
    cantidadFilas:int = 0
    cantidadFinalPalitos:int = 0
    
    cantidadPalitos = int(input("¿Con cuantos palitos queres jugar?: "))

    cantidadPalitosMinima = calcularCantidadPalitosMinima(cantidadJugadores)
    
    if cantidadPalitos < cantidadPalitosMinima:
        cantidadPalitos = cantidadPalitosMinima
        
    cantidadFilas = ceil((sqrt((2*cantidadPalitos) + 1/4)) - 1/2)
    
    for fila in range(cantidadFilas):
        cantidadFinalPalitos += fila+1
        
    print("    >> Se va a armar un tablero de", cantidadFilas, "filas y", cantidadFinalPalitos, "palitos.")
    
    return cantidadFinalPalitos


def armarTablero(cantidadPalitos:int) -> list:

    '''
    Esta función arma el tablero inicial dependiendo de la cantidad de palitos. Al inicio el tablero esta COMPLETO.
    El tablero esta conformado por una lista de listas
        - Cada FILA es una lista.
        - Dentro de cada fila hay una lista por PALITO, compuesta por:
            - str: "|"
            - bool: T si el palito es rojo. F si el palito NO es rojo.
            - int: indica la cantidad de turnos bloqueados para el palito.
                - ej: [ [ "|", True, 0 ] , [ "|", False, 3 ] ]
    '''

    tablero:list = []
   
    # Calculo cuantas filas va a tener mi tablero.
    cantidadFilas:int = ceil((sqrt((2*cantidadPalitos) + 1/4)) - 1/2)
   
    for i in range(1, cantidadFilas + 1):
        
        fila:list = []

        for j in range(i):
            fila.append(["|", False, 0])

        tablero.append(fila)
   
    tablero = colocarPalitosRojos(tablero, cantidadPalitos)
   
    return tablero


def colocarPalitosRojos(tablero:list, cantidadPalitos:int) -> list:
   
    '''
    Esta función toma el 30% de la cantidad de palitos y se los asigna como "palitos rojos".
    El segundo elemento de cada lista correspondiente a cada palito es asignado como: True.
    - La eleccion de que palito sera asignado como rojo se realiza de forma random.
    '''

    porcentajePalitosRojos:int = ceil((0.30 * cantidadPalitos))
   
    for i in range(porcentajePalitosRojos):
        fila:int = int(random.randint(0,(len(tablero))-1))
        columna:int = int(random.randint(0,(len(tablero[fila]))-1))
       
        tablero[fila][columna][ES_ROJO] = True
   
    return tablero


def mostrarTablero(tablero:list) -> None:

    '''
    Esta función imprime en pantalla el tablero de una forma mas amigable para el usuario.
        - A la izquierda se imprime el numero de fila
        - Abajo se imprime la posicion.
    '''

    espacioMaximo = max(len(x) for x in tablero) # Busco el largo maximo de las filas.
    contadorFila:int = 1
    contadorColumna:int = 1
   
    for fila in tablero:
        cantidad = len(fila)
        diferencia = espacioMaximo - cantidad    # Hago la diferencia entre la base y la fila actual.
       
        print(str(contadorFila) + "\t", end="")  
        print(" " * diferencia, end="")          # Imprimo un espacio en blanco por la diferencia entre la base y la fila actual.
       
        for data in fila:
            print(data[PALITO] + " ", end="")
       
        print()
        contadorFila += 1
       
    print("")
    print("\t", end="")

    for columna in range(len(tablero)):
        print(str((contadorColumna)) + " ", end="")
        contadorColumna += 1


def mostrarTableroInicial(tablero:list) -> None:

    '''
    Esta función imprime en pantalla el tablero de una forma mas amigable para el usuario y mostrando los palitos que son rojos.
    '''

    espacioMaximo = max(len(x) for x in tablero) # Busco el largo maximo de las filas.
    contadorFila:int = 1
    contadorColumna:int = 1
   
    for fila in tablero:
        cantidad = len(fila)
        diferencia = espacioMaximo - cantidad    # Hago la diferencia entre la base y la fila actual.
       
        print(str(contadorFila) + "\t", end="")  
        print(" " * diferencia, end="")          # Imprimo un espacio en blanco por la diferencia entre la base y la fila actual.
       
        for data in fila:
            
            if data[ES_ROJO]:
                print(f"{Fore.RED}{Style.BRIGHT}{data[PALITO]}{Style.RESET_ALL} ", end="")
            else:
                print(data[PALITO] + " ", end="")
       
        print()
        contadorFila += 1
       
    print("")
    print("\t", end="")

    for columna in range(len(tablero)):
        print(str((contadorColumna)) + " ", end="")
        contadorColumna += 1


def acomodarTablero(tablero:list) -> list:

    '''
    Esta función reacomoda el tablero para evitar que haya espacios vacios en el medio de una fila.
    El lugar vacío se ocupa con el primer palito de la fila superior.
    '''
   
    tableroAlReves:list = tablero[::-1]     # Recorro el tablero de abajo para arriba.
    contador:int = len(tablero)
   
    for fila in tableroAlReves:

        while (len(fila) < contador) and contador > 1:

            if len(tablero[contador - 2]) > 0:
                item:list = tablero[(contador - 2)][0]
                del tablero[contador - 2][0]
                tablero[contador - 1].append(item)
            # Si la fila superior esta vacio, paso a la de arriba.
            elif contador - 3 >= 0 and len(tablero[contador - 3]) > 0:
                item:list = tablero[(contador - 3)][0]
                del tablero[contador - 3][0]
                tablero[contador - 1].append(item)
            # Si esa también esta vacia lo dejo como esta.
            else:
                contador -= 1                    

        contador -= 1          
           
    return tablero


def inicializarTurno(jugador:str, tablero:list) -> None:

    '''
    Esta función inicializa el turno para cada jugador.
    Se imprime en pantalla a quien corresponde el turno y el tablero al inicio.
    '''

    turno:str = "   = Turno de " + jugador[NOMBRE_JUGADOR] + " ="
    turnoColor:str = f"{Fore.BLUE}{Style.BRIGHT}{turno}{Style.RESET_ALL}"

    print(turnoColor)
    print("")

    print("+ Tablero al inicio del turno:")
    print("")
    mostrarTableroInicial(tablero)
    print("")


def quitarPalitosJugador(tablero:list, cantidadPalitos:int) -> list:

    '''
    Esta función retira los palitos indicados por el jugador.
    '''
   
    palitosRojos:int = 0

    cantidadPalitosAQuitar:int = int(input("Ingrese cuantos palitos desea retirar en esta ronda: "))
    print("- El jugador decidio quitar", cantidadPalitosAQuitar, "palitos." )
    
    cantidadPalitosSacados:int = 0
   
    for i in range(cantidadPalitosAQuitar):
       
        if cantidadPalitos > 0:
            print("")
            coordenada:str = input("Ingrese la coordenada (fila posicion) del palito que desea retirar: [ EJ: si deseo retirar de la fila 3 el palito en la posicion 2, ingreso: 3 2 ]: ")
            fila, columna = int(coordenada[::][0]), int(coordenada[::][2])

            # Chequeo que haya un palito en la posicion ingresada
            while fila-1 > (len(tablero)-1) or columna-1 > (len(tablero[fila-1])-1):
                texto:str = "¡LA POSICION INGRESADA NO ES VALIDA!"
                print(f"{Fore.RED}{Style.BRIGHT}{texto}{Style.RESET_ALL}")

                coordenada:str = input("Ingrese la coordenada (fila posicion) del palito que desea retirar: [ EJ: si deseo retirar de la fila 3 el palito en la posicion 2, ingreso: 3 2 ]: ")
                fila, columna = int(coordenada[::][0]), int(coordenada[::][2])

            palito = tablero[fila-1][columna-1]
           
            # Chequeo que el palito no este bloqueado.
            if palito[BLOQUEADO] > 0:
                texto = "¡PALITO BLOQUEADO! No se puede retirar en este turno."
                print(f"{Fore.RED}{texto}{Style.RESET_ALL}")
            
            else:
                del tablero[fila-1][columna-1]
                tablero = acomodarTablero(tablero)
                
                cantidadPalitos -= 1
                cantidadPalitosSacados += 1
           
            print("")
            texto = ">>> Tablero al momento:"
            print(f"{Fore.CYAN}{texto}{Style.RESET_ALL}")
            print("")
            mostrarTablero(tablero)
            print("")
          
            # Si saco un palito rojo en alguna de las jugadas lo agrego a la lista de palitos rojos.
            if palito[ES_ROJO]:
                palitosRojos += 1
   
    return tablero, cantidadPalitos, cantidadPalitosSacados, palitosRojos


def quitarPalitosMaquina(tablero:list, cantidadPalitos:int) -> list:
   
    '''
    Esta función retira los palitos indicados por la maquina.
    '''

    palitosRojos:int = 0
   
    print("")
    print("Ingrese cuantos palitos desea retirar en esta ronda: ")
    cantidadPalitosAQuitar:int = random.randint(1, cantidadPalitos)
    print("- El jugador decidio quitar", cantidadPalitosAQuitar, "palitos." )
    
    cantidadPalitosSacados:int = 0

    for i in range(cantidadPalitosAQuitar):

        if cantidadPalitos > 0:
            print("")
            print("Ingrese la coordenada (fila columna) del palito que desea retirar: ")
            fila:int = int(random.randint(0,(len(tablero))-1))
           
            while len(tablero[fila]) == 0:
                fila:int = int(random.randint(0,(len(tablero))-1))
           
            columna:int = int(random.randint(0,(len(tablero[fila]))-1))

            print("- El jugador decidio quitar el palito en la posicion: ", fila+1, columna+1)
           
            palito = tablero[fila][columna]
           
            if palito[BLOQUEADO] > 0:
                texto = "¡PALITO BLOQUEADO! No se puede retirar en este turno."
                print(f"{Fore.RED}{texto}{Style.RESET_ALL}")

            else:
                del tablero[fila][columna]
                tablero = acomodarTablero(tablero)
                
                cantidadPalitos -= 1
                cantidadPalitosSacados += 1

            print("")
            texto = ">>> Tablero al momento:"
            print(f"{Fore.CYAN}{texto}{Style.RESET_ALL}")
            print("")
            mostrarTablero(tablero)
            print("")
                      
            if palito[ES_ROJO]:
                palitosRojos += 1
                
            sleep(2)

    return tablero, cantidadPalitos, cantidadPalitosSacados, palitosRojos


def evaluarEventos(tablero:list, cantidadPalitos:int, 
                   jugador:list, cantidadInicialPalitos:int) -> list:
   
    '''
    Esta función se utiliza cuando un jugador retiro algun palito rojo.
    Se elige un numero random del 1 al 6. Cada numero inicializa un evento distinto.
    '''
    
    print("")
    texto:str = "¡SACASTE ALGUN PALITO ROJO!"
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Style.RESET_ALL}")
    
    print("Tirando dado...")
    sleep(2)

    dado:int = int(random.randint(1,6))
    
    print("Salio el numero:", dado)
    print("")
   
    if dado == 1:
        jugador = eventoUno(jugador)

    elif dado == 2:
        tablero, cantidadPalitos = eventoDos(tablero, cantidadInicialPalitos, cantidadPalitos)

    elif dado == 3:
        tablero = eventoTres(tablero, cantidadPalitos)

    elif dado == 4:
        tablero, cantidadPalitos = eventoCuatro(tablero, jugador, cantidadPalitos)
       
    elif dado == 5:
        tablero = eventoCinco(tablero, cantidadInicialPalitos)
        cantidadPalitos = cantidadInicialPalitos
       
    elif dado == 6:
        texto:str = "Esta vez tuviste suerte, no ocurre ningun evento ( ͡~ ͜ʖ ͡°) "
        print(f"{Fore.GREEN}{texto}{Style.RESET_ALL}")

    return tablero, cantidadPalitos


def eventoUno(jugador:list) -> list:

    '''
    Esta función corresponde al Evento 1:
        - El jugador pierde su próximo turno.
    '''

    print("")
    texto:str = " # SE ACTIVA EL EVENTO 1 #"
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}{texto}{Style.RESET_ALL}")

    texto = "¡UPS! Perdes tu proximo turno (ง︡'-'︠)ง"
    print(f"{Fore.LIGHTMAGENTA_EX}{texto}{Style.RESET_ALL}")
   
    jugador[TURNOS] += 1
   
    return


def eventoDos(tablero:list, cantidadInicialPalitos:int, cantidadPalitos:int) -> list:

    '''
    Esta función corresponde al Evento 2:
        - Se agregan entre 1 y M palitos, en caso de no poder agregarse a totalidad, se agrega el máximo que se pueda
                (no superar cantidad inicial de palitos).
    '''
   
    cantidadPalitosAgregar:int = int(random.randint(1,cantidadInicialPalitos-cantidadPalitos))
   
    print("")
    texto:str = " # SE ACTIVA EL EVENTO 2 #"
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}{texto}{Style.RESET_ALL}")

    texto = "Se van a agregar al tablero " + str(cantidadPalitosAgregar) + " palitos."
    print(f"{Fore.LIGHTMAGENTA_EX}{texto}{Style.RESET_ALL}")

    tableroAlReves:list = tablero[::-1]     # Recorro el tablero de abajo para arriba.
    contador:int = len(tablero) 
    
    cantidadPalitos += cantidadPalitosAgregar
    
    while cantidadPalitosAgregar > 0:
    
        for fila in tableroAlReves:
            
            while len(fila) < contador and cantidadPalitosAgregar > 0:
                tablero[contador-1].append(PALITO_BASE)
                cantidadPalitosAgregar -= 1
                
            contador -= 1        
   
    return tablero, cantidadPalitos


def eventoTres(tablero:list, cantidadPalitos:int) -> list:

    '''
    Esta función corresponde al Evento 3:
        - Se bloquean/congelan el 20% de los palitos (en el caso que el valor sea < 1 entonces se toma 1 palito) , durante 3 turnos los jugadores no podrán retirarlos.
    '''
   
    porcentajePalitosBloqueados:int = ceil((0.20 * cantidadPalitos))
   
    print("")
    texto:str = " # SE ACTIVA EL EVENTO 3 #"
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}{texto}{Style.RESET_ALL}")

    texto = "Se van a bloquear por 3 turnos " + str(porcentajePalitosBloqueados) + " palitos."
    print(f"{Fore.LIGHTMAGENTA_EX}{texto}{Style.RESET_ALL}")

    for i in range(porcentajePalitosBloqueados):
        fila:int = int(random.randint(0,(len(tablero))-1))

        while len(tablero[fila]) == 0:
            fila:int = int(random.randint(0,(len(tablero))-1))

        columna:int = int(random.randint(0,(len(tablero[fila]))-1))
       
        tablero[fila][columna][BLOQUEADO] = 3
   
    return tablero


def eventoCuatro(tablero:list, jugador:str, cantidadPalitos:int) -> list:

    '''
    Esta función corresponde al Evento 4:
        - Bomba: el jugador debe retirar una fila completa a su elección.
    '''
   
    fila:int = 0

    print("")
    texto:str = " # SE ACTIVA EL EVENTO 4 #"
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}{texto}{Style.RESET_ALL}")

    texto = "Vas a tener que eliminar una fila entera ᕙ(`▿´)ᕗ"
    print(f"{Fore.LIGHTMAGENTA_EX}{texto}{Style.RESET_ALL}")
   
    print("")
    print(">> Tablero al momento:")
    print("")
    mostrarTablero(tablero)
    print("")
   
    if jugador[NOMBRE_JUGADOR].startswith("Maquina"):
        print("")
        print("Indique que fila desea retirar por completo: ")
        fila = int(random.randint(1,(len(tablero))))
        
        print("    >> El jugador decidio retirar la fila", fila)
        
        while fila-1 > (len(tablero)-1) or len(tablero[fila-1]) < 1:
            texto:str = "¡LA FILA INGRESADA NO ES VALIDA!"
            print(f"{Fore.RED}{Style.BRIGHT}{texto}{Style.RESET_ALL}")
            
            print("")
            print("Indique que fila desea retirar por completo: ")
            fila = int(random.randint(1,(len(tablero))))
            print("    >> El jugador decidio retirar la fila", fila)
       
        for i in range(len(tablero[fila-1])-1):
            del tablero[fila-1][i-1]
            
            cantidadPalitos -= 1

    else:
        print("")
        fila = int(input("Indique que fila desea retirar por completo: "))
        
        while fila-1 > (len(tablero)-1) or len(tablero[fila-1]) < 1:
            texto:str = "¡LA FILA INGRESADA NO ES VALIDA!"
            print(f"{Fore.RED}{Style.BRIGHT}{texto}{Style.RESET_ALL}")
            
            print("")
            fila = int(input("Indique que fila desea retirar por completo: "))
              
        for i in range(len(tablero[fila-1])-1):
            del tablero[fila-1][i-1]
            
            cantidadPalitos -= 1
        
        
    return tablero, cantidadPalitos


def eventoCinco(tablero:list, cantidadInicialPalitos:int) -> list:

    '''
    Esta función corresponde al Evento 5:
        - Nueva pirámide: se genera una nueva pirámide, del mismo tamaño que la original.
    '''

    print("")
    texto:str = " # SE ACTIVA EL EVENTO 5 #"
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}{texto}{Style.RESET_ALL}")

    texto = "Se crea un tablero nuevo (̶◉͛‿◉̶)"
    print(f"{Fore.LIGHTMAGENTA_EX}{texto}{Style.RESET_ALL}")

    tablero = armarTablero(cantidadInicialPalitos)
   
    return tablero


def main() -> None:

    iniciarJuego()

    # Inicializo mis variables.
    cantidadJugadores:int = 0
    nombreJugador:str = ""
    jugadores:list = []

    cantidadPalitosSacados:int = 0
    palitosRojos:int = 0
    texto:str = ""
   
    cantidadJugadores, nombreJugador, jugadores = elegirJugadores()

    cantidadInicialPalitos:int = calcularCantidadPalitos(cantidadJugadores)

    tablero:list = armarTablero(cantidadInicialPalitos)
       
    cantidadPalitos:int = cantidadInicialPalitos
       
    print("")
       
    while cantidadPalitos > 0:

        for jugador in jugadores:

            if jugador[NOMBRE_JUGADOR] == nombreJugador and cantidadPalitos > 0:

                inicializarTurno(jugador, tablero)
                print("")

                if jugador[TURNOS] > 0:
                    texto = "Como perdiste un turno, esta vez no podes jugar (ɔ◔‿◔)ɔ ♥"
                    print(f"{Fore.RED}{texto}{Style.RESET_ALL}")
                   
                    jugador[TURNOS] -= 1
               
                else:
                    turnoActual = jugador

                    tablero, cantidadPalitos, cantidadPalitosSacados, palitosRojos = quitarPalitosJugador(tablero, cantidadPalitos)
                   
                    if palitosRojos > 0:
                        tablero, cantidadPalitos = evaluarEventos(tablero, cantidadPalitos, jugador, cantidadInicialPalitos)
               
                    jugador[PALITOS_SACADOS] += cantidadPalitosSacados # Le voy agregando en cada turno cuantos palitos va sacando

                print("")
                texto = "  = Fin del turno de " + jugador[NOMBRE_JUGADOR] + " =  "
                print(f"{Fore.BLUE}{Style.BRIGHT}{texto}{Style.RESET_ALL}")

                sleep(10)
                clear()
               
            elif jugador[NOMBRE_JUGADOR] != nombreJugador and cantidadPalitos > 0:

                inicializarTurno(jugador, tablero)
                print("")

                if jugador[TURNOS] > 0:
                    texto:str = "Como perdiste un turno, esta vez no podes jugar (ɔ◔‿◔)ɔ ♥"
                    print(f"{Fore.RED}{texto}{Style.RESET_ALL}")
                   
                    jugador[TURNOS] -= 1

                else:
                    turnoActual = jugador

                    tablero, cantidadPalitos, cantidadPalitosSacados, palitosRojos = quitarPalitosMaquina(tablero, cantidadPalitos)
                   
                    if palitosRojos > 0:
                        tablero, cantidadPalitos = evaluarEventos(tablero, cantidadPalitos, jugador, cantidadInicialPalitos)
               
                    jugador[PALITOS_SACADOS] += cantidadPalitosSacados

                print("")
                texto = "  = Fin del turno de " + jugador[NOMBRE_JUGADOR] + " =  "
                print(f"{Fore.BLUE}{Style.BRIGHT}{texto}{Style.RESET_ALL}")

                sleep(10)
                clear()

            for fila in tablero:
                for palito in fila:
                    if palito[BLOQUEADO] > 0:
                        palito[BLOQUEADO] -= 1

    finalizarJuego(turnoActual)


main()
