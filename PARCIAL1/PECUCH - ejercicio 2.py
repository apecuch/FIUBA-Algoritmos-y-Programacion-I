'''

PARCIAL ALGORITMOS I - 12/10/2023

    ALUMNO: Pecuch Agustina
    PADRON: 111560
    DNI: 40729147

'''

def calcularPalabras(parrafo:str) -> tuple:

    parrafo = parrafo.replace(".", "")
    parrafo = parrafo.replace(",", "")
    parrafo = parrafo.replace(";", "")
    parrafo = parrafo.replace(":", "")

    palabrasParrafo:list = parrafo.split(" ")

    cantidadPalabrasMenorLongitud:int = 0
    cantidadPalabrasMayorLongitud:int = 0

    palabraMayor:str = ""
    palabraMenor:str = ""
    largoMayorActual:int = 1
    largoMenorActual:int = len(parrafo)
    
    for palabra in palabrasParrafo:
        if len(palabra) > largoMayorActual:
             palabraMayor = palabra
             largoMayorActual = len(palabra)

        if len(palabra) < largoMenorActual:
            palabraMenor = palabra
            largoMenorActual = len(palabra)

    for palabra in palabrasParrafo:
        if len(palabra) == largoMayorActual:
            cantidadPalabrasMayorLongitud += 1
        elif len(palabra) == largoMenorActual:
            cantidadPalabrasMenorLongitud += 1

    return cantidadPalabrasMenorLongitud, cantidadPalabrasMayorLongitud

def main() -> None:

    parrafo:str = "Las personas mayores nunca son capaces de comprender las cosas por sí mismas, y es muy aburrido para los niños tener que darles una y otra vez explicaciones"
    
    palabras:tuple = calcularPalabras(parrafo)

    print(palabras)

main()