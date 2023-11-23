"""
    Crear un procedimiento donde el usuario ingresara una cadena de caracteres con dos palabras intercaladas. Los caracteres pares son parte de la primera palabra y los caracteres impares son parte de la segu7nda palabra.
    Mostrar las dos palabras por separado.
"""

def separarPalabras( palabra:str ) -> None:
    palabra1:str = palabra[::2]
    palabra2:str = palabra[1::2]

    print(palabra1)
    print(palabra2)

def main() -> None:
    separarPalabras("hcohlaau")

main()