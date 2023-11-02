"""
Dado un parrafo base, permitir al usuario el ingreso de dos palabras. Reemplazar todas las apariciones de la primer palabra, por la segunda pero invertida. 
"""

parrafo:str = "TEXTO: Voy a repetir la palabra texto muchas veces asi despues cambio la palabra texto va una vez mas texto."

print(parrafo)

palabraAReemplazar:str = input("Ingrese la palabra del texto que quiere reemplazar: ")

while palabraAReemplazar not in parrafo:
    palabraAReemplazar:str = input("La palabra ingresada no se encuentra en el texto. Ingrese una palabra que si se encuentre en el texto: ")

palabraRemplazo:str = input("Ingrese la palabra por la que quiere reemplazar: ")

parrafo = parrafo.replace(palabraAReemplazar, palabraRemplazo[-1::-1])

print("El texto queda asi:", parrafo)