def invertirParametro ( parametro:str ) -> str:
    invertido:str = parametro[::-1]
    return invertido

def main () -> None:
    parametro = input("Ingrese una frase o palabra: ")
    print(invertirParametro(parametro))

main()