'''

EXCEPCIONES

    raise Exception("Error que creo yo")


ASSERT

    assert funcion() == "algo"   -> solo tira una exceocion si falla

'''

'''

EJERCICIO 2: Números dentro de un archivo
Se les proporcionará un archivo numeros.txt, donde cada línea contiene un número de forma aleatoria. Lo que les pedimos es leer el archivo y calcular la suma de todos esos números y mediante un assert verificar que la suma sea igual a 2.613.600


'''

# def sumaArchivos(archivo:str) -> int:
    
#     suma:int = 0
    
#     with open(archivo, "r") as archivo:
        
#         for linea in archivo:
            
#             suma += int(linea)

#     return suma


# def main() -> None:
    
#     rutaArchivo:str = "C:\\Users\\USUARIO\\Desktop\\cadenas.txt"
    
#     assert sumaArchivos(rutaArchivo) == 2613600


# main()


'''

VALIDACIONES

    if not isinstance(variable, tipo):
        raise ValueError("variable debe ser tipo")


'''