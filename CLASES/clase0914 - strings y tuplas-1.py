"""
Ejercicio: permitir al usuario ingresar una cadena, y validar que esa cadena sea un numero entero, ya sea positivo o negativo. Utilizar únicamente lo visto hasta strings.

Ejemplos válidos: "123", "0", "-1", "-7483"

Ejemplos inválidos: "1.5", "123a", " ", "pepe", "2 + 2"
"""

cadena:str = input("Ingrese una cadena de caracteres: ")

cadena = cadena.replace("-", "")

if cadena.isnumeric() and cadena.isdigit():
    print("La cadena ingresada es un entero")
else:
    print("La cadena ingresada no es un entero")