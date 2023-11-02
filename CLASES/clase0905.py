"""
Ejercicio de Ciclos

Se pide hacer un programa que ingrese 8 juegos de n valores positivos cada uno.
Considerar una condición de corte para el n.

Calcular el promedio de cada juego, 
el máximo de cada juego 

y el mínimo de todos los juegos.
"""
minimo = 0

for juego in range(2):

    valor = int(input("Ingrese un valor positivo o negativo para terminar: "))

    if ( juego == 0):
        minimo = valor

    cantJuegos = 0
    valoresIngresados = 1
    suma = 0
    maximo = valor

    while valor >= 0:

        valoresIngresados += 1
        suma += valor

        if (valor > maximo):
            maximo = valor
        
        if (valor < minimo):
            minimo = valor

        valor = int(input("Ingrese un valor positivo o negativo para terminar: "))
       
    promedio = suma / valoresIngresados
    print("El promedio del juego", juego+1, "es:", promedio)
    print("El maximo del juego", juego+1, "es: ", maximo)

    print("###############################")



print("###############################")
print("El minimo de todos los juegos es: ", minimo)