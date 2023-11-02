"""
Desarrollar un programa, a partir del cual el usuario ingresa una oración y le muestre
    por consola cuál es el carácter que más se repite
    
    Condiciones: No se debe tener en consideración el espacio en blanco. 
    La oración a ingresar no debe estar vacía
"""

oracion = input("Ingrese una oracion: ")

letraRepetida = ""
cantidadRepetida = 0

if oracion != "":

    for letra in oracion:

        repeticiones = 0
        
        if letra != "":

            for comparacion in oracion:

                if (letra == comparacion):
                    repeticiones += 1

                if repeticiones > cantidadRepetida:
                    letraRepetida = letra
                    cantidadRepetida = repeticiones

            print("La letra", letra, "se repite", repeticiones, "veces")
        
    print("La letra que mas se repite es:", letraRepetida, "con", cantidadRepetida, "repeticiones")
    
else:    
    print("Usted no ingreso una oracion")