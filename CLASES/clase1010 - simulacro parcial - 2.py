'''

Se nos pide crear una funcion que reciba un párrafo y realice:
    1 - Mostrar por pantalla:
        a - La cantidad de palabras que contiene
        b - La palabra mas frecuente
        c - El porcentaje de vocales presente
        d - La palabra mas corta y la palabra mas larga
    2 - Solicitar al usuario una palabra y mostrar el parrafo sin esa palabra.

'''

def porcentajesParrafo(parrafo:str) -> None:

    cantidadPalabras:int = 0
    palabraMasFrecuente:str = ""
    porcentajeDeVocales:float = 0.0
    palabraMasCorta:str = ""
    palabraMasLarga:str = ""

    palabrasParrafo:list = parrafo.split(" ")
    cantidadPalabras = len(palabrasParrafo)

    aparicionesPalabras:dict = {} # palabra : apariciones
    for palabra in palabrasParrafo:
        if palabra not in aparicionesPalabras:
            aparicionesPalabras[palabra] = 1
        else:
            aparicionesPalabras[palabra] += 1
    maximoApariciones:int = 0
    for palabra in aparicionesPalabras:
        if aparicionesPalabras[palabra] > maximoApariciones:
            palabraMasFrecuente = palabra
            maximoApariciones = aparicionesPalabras[palabra]

    cantidadVocales:int = 0
    vocales:list = ["a", "e", "i", "o", "u"]
    for letra in parrafo:
        if letra.lower() in vocales:
            cantidadVocales += 1
    porcentajeDeVocales = cantidadVocales % len(parrafo)

    print("La cantidad de palabras que contiene el parrafo es:", cantidadPalabras)
    print("La palabra mas frecuente del parrafo es:", palabraMasFrecuente)
    print("El porcentaje de vocales del parrafo es:", porcentajeDeVocales, "%")

def eliminarPalabra(parrafo:str) -> None:

    palabra:str = input("Ingrese la palabra que desea eliminar: ")
    parrafo = parrafo.replace(palabra, "")
    
    print(parrafo)

def main() -> None:

    parrafo:str = "Habia una vez una perrita llamada Mia que le gustaba dormir mucho y tambien comer como una chanchita."

    porcentajesParrafo(parrafo)
    eliminarPalabra(parrafo)       

main()