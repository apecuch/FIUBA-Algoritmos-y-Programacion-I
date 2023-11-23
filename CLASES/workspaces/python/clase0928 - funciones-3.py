def separarLista( lista:list, step:int ) -> list:
    nuevaLista:list = []
    for i in range(0, len(lista), step):
        nuevaLista.append(lista[i:i+step])

    return nuevaLista

def main() -> None:
    lista:list = [ "A", "B", "C", "D", "E", "F", "G"]
    n:int = 2
    print(separarLista(lista, n))

main()