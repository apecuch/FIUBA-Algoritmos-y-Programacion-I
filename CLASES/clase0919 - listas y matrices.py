"""
    LISTAS
        - Son mutables
        - Se definen [ , , , ] -> corchetes OBLIGATORIOS
        - Puedo agregar o sacar elmentos

        CAMBIAR ELEMENTOS
            - lista[indice] = "lo nuevo que quiero poner"

        RECORRER LISTAS
            - for elemento in range(len(lista)):  -> recorre la lista por INDICE
            - for elemento in lista: -> recorre la lista por ELEMENTO -> mejorcitaaaaaaaaaa !!!!
        
        STRING A LISTAS
            "un string".split() -> separa el string por espacios y lo convierte en una lista
            "un, string".split(",") -> separa el string por comas y lo convierte en una lista   -> asi puedo elegir yo el elemento de separacion
                                                                                                -> el separador no aparece en la lista final
            " ".join(lista) -> convierte una lista en un string separado por espacios                                                                    => TODOS ELEMENTOS TIENEN QUE SER STRING
            ",".join(lista) -> convierte una lista en un string separado por comas -> asi puedo elegir yo el elemento de separacion                      => TODOS ELEMENTOS TIENEN QUE SER STRING

        LISTAS CON VARIABLES
            hola = hola
            nombre = nombre
            lista = [ hola, nombre ]

            La lista contiene COPIAS de los valores de las variables, si yo cambio algun valor en la variable pero no modifico la lista la misma sigue teniendo el valor anterior. 
            
        IN
            "un string" in lista -> devuelve true o false si en la lista hay un valor como el string

        AGREGAR ELEMENTOS
            lista.append("lo que quiero agregar") -> agrego el elemento al final
            lista.insert(posicion, "lo que quiero guardar")

        QUITAR ELEMENTOS
            lista.remove("lo que quiero quitar") -> remueve solo la PRIMER aparicion de lo que le paso  
            lista.pop() -> remueve el ultimo elemento

        OPERACIONES
            sum(lista) -> suma todos los elementos
            max(lista) -> trae el max de los elementos
            min(lista) -> trae el min de los elementos

            
    # MATRICES
        - listas de listas
        - se definen [ [], [], [] ] -> cada lista es una fila
                                    -> cada elemento de cada lista es una columna

        RECORRER LISTAS
            lista[indice][indice] -> cada [] representa un nivel

        SLICING
            lista[start:stop:step]
            matriz[star:stop:step][start:stop:step]

        FOR
            for i in range(len(matriz)):               -> itera por cada elemento de la lista
                for j in range(len(matriz[i])):        -> itera por cada elemento dentro del elemento actual de la lista
"""

"""
    EJERCICIO 1

Crear un programa que permita generar un tablero de
n x n en el cual que la diagonal se muestre con "#" mientras
que el resto de las casillas deben mostrar "*".

Pedir al usuario que ingrese una coordenada (fila y columna).
Si el casillero tiene un "*" cambiarlo a "#".

Si tiene un "#" mostrar un mensaje que diga "la diagonal es del alfil"
Si elige el mismo casillero más de una vez mostrar un mensaje que diga
"¿¿¿Pero que estas haciendo???"
"""

n = int(input("Ingrese la dimension del tablero: "))
tablero:list = []

for i in range(n):
    tablero.append([])
    for j in range(n):
        if i==j:
            tablero[i].append('#')
        else:
            tablero[i].append('*')

coordenadasIngresadas:list = []
seguirJugando:bool = True


while seguirJugando:

    for fila in tablero:
        print(fila)

    fila = int(input("Ingrese una fila: "))
    columna = int(input("Ingrese una columna: "))

    if [fila, columna] in coordenadasIngresadas:
        print("¿¿¿Pero que estas haciendo???")
        seguirJugando = False
    else:
        coordenadasIngresadas.append([fila, columna])

        if tablero[fila][columna] == "*":
            tablero[fila][columna] = "#"
        elif tablero[fila][columna] == "#":
            print("la diagonal es del alfil")
    
    respuesta:str = input("Si desea dejar de jugar ingrese -1: ")
    if respuesta == "-1":
        seguirJugando = False