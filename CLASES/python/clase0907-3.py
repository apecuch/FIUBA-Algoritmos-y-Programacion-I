"""
3- Un número se considera abundante si la suma
de todos sus divisores (Exceptuando así mismo)
es mayor a el mismo.
​
Ejemplo:
10 -> Sus divisores son 5 + 2 + 1 = 8, 10 no es un número abundante.
12 -> Sus divisores son 6 + 4 + 3 + 2 + 1 = 16, 12 es un número abundante
​
Se pide realizar un programa que dado
un número N, calcule todos los números
abundantes en el intervalo [1, N]
​
"""

n = int(input("Ingrese un numero: "))

for num in range(1, n+1):

    sumaDivisores: int = 0

    for m in range(1, num//2 + 1):

        if num % m == 0:
            sumaDivisores += m
        
    if sumaDivisores > num:
        print( num, "es abundante")
