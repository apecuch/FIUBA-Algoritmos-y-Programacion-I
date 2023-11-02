"""
    # STRINGS

    - CONCATENAR
        Con un ' + '
    - CASTING (castea)
        str(numero) -> str(2)
    - MULTIPLICAR
        " " * 4 -> lo imprime 4 veces
    - CONTAR
        " ".count("lo que quiero contar") -> cuantas veces aparece algo en el string
        len("frase") -> cuenta la cantidad de caracteres
    - CONVERTIR EN MAYUSCULAS y MINISCULAS
        " ".upper()
        " ".lower()
        " ".capitalize() -> convierte la primera letra en mayuscula
    - VALIDAR
        " ".isalnum() -> chequea no haya simbolos raros solo letras y num
        " ".isalpha() -> chequea que solo haya letras
        " ".isnumeric() -> chequea que solo haya numeros
        " ".startswith(" ") -> chequea que empiece con lo que le paso
        " ".endswith(" ") -> chequea que termine con lo que le paso
        " ".isspace() -> chequea que solo haya espacios
    - BUSCAR UN STRING DENTRO DE OTRO
        " ".find(" ") -> devuelve la posicion donde empieza el string que busco
    - REEMPLAZAR
        " ".replace("lo que quiero remplazar", "con lo que quiero remplazar") -> remplaza lo que le paso por lo que quiero
                                                                              -> los cambios no se guardan solo, hay que reasignar la variable
    - SLICING
        " "[0:11:1] [start:stop:step]-> va desde el 0 hasta el 11 de a 1 (el 11 no lo toma en cuenta)
        " "[-1:0:-1] -> va desde el ultimo caracter hasta el primero de atras para adelante
        " "[0::1] -> si no indico nada en el medio recorre todo el string
    - INMUTABILIDAD -> no se puede asignar items a un string ya definido. NO SE PUEDEN MODIFICAR

        
"""

# Ejercicio 1


texto:str = "Hola como estas"

for palabra in texto.split():
    print(texto)
    palabraAReemplazar = input("Ingrese la palabra que quiere reemplazar: ")

    while palabraAReemplazar not in texto:
        palabraAReemplazar = input("La palabra", palabraAReemplazar, "no se encuentra en el texto. Ingrese una palabra que si se encuentre en el texto: ")

    palabraReemplazo = input("Ingrese la palabra por la que quiere reemplazar: ")
    texto = texto.replace(palabraAReemplazar, palabraReemplazo)

    
# Ejercicio 2

texto = "avFfe2rtlty3cvchg3yutui1olcpi3bv4qwnef2zxsza,zc&cvdjy4uimkm3lindg1qcnxa&wesxatqhrjr3xcnumgaqs"

textoDesencriptado = texto[2::3]

textoDesencriptado = textoDesencriptado.replace("1", "a")
textoDesencriptado = textoDesencriptado.replace("2", "e")
textoDesencriptado = textoDesencriptado.replace("3", "i")
textoDesencriptado = textoDesencriptado.replace("4", "o")
textoDesencriptado = textoDesencriptado.replace("5", "u")
textoDesencriptado = textoDesencriptado.replace("&", " ")

print(textoDesencriptado)


"""

    # TUPLAS

        - son inmutables
        - ( , , ,)
        - cada elemento de la tupla puede ser de un tipo de dato distinto

        ANALIZAR ELEMENTOS DE UNA TUPLA
            fecha[0] -> si tuviera una tupla en esa posicion -> tupla[0][1]
            - se banca slicing -> fecha[0:2]

        INDEX
            tupla.index(" ") -> devuelve la posicion del elemento que le paso

        LEN
            len(tupla) -> devuelve la cantidad de elementos que tiene la tupla

        # TUPLAS DE VARIABLES

            tupla = (dia, mes, año) -> dia mes y año son variables con sus valores

            dia, mes, año = tupla -> toma los valores que tiene la tupla y los asigna a las variabñes siguiendo el orden

"""