'''

ARCHIVOS

METODO 1:

    archivo = open("nombre del archivo.extension", "modo de apertura")

        Modo de apertura:
            - r : read
            - w : write
            - r+ / w+ : ambos
            - a : escribe al final del archivo. si no existe lo crea.
            
        Leer contenido:
        
            linea = archivo.readline()
            for linea in archivo:
            
    archivo.close()     -> CUANDO TERMINO DE USARLO LO CIERRO!!!!


METODO 2:

    with open("RUTA DEL ARCHIVO", "modo de apertura") as archivo:
        for linea in archivo:
        
    RUTAS: con 2 barras invertidas // para separar carpetas
    
    -> con este metodo no hace falta cerrar el archivo, se cierra solo.
    

SALTOS DE LINEA:
    linea.rstrip('/n') -> derecha
    linea.lstrip('/n') -> izquierda
    linea.strip('/n') -> ambos lados

'''

'''

EJERCICIO 1: Leer cadenas dentro de un archivo
Se les proporcionará un archivo cadenas.txt donde cada línea contiene una cadena generada de forma aleatoria. Lo que se les pide es que lean cada línea del archivo y mostrar mediante consola el primer carácter de cada cadena.

'''

# def main() -> None:
    
#     rutaArchivo:str = "C:\\Users\\USUARIO\\Desktop\\cadenas.txt"
    
#     with open(rutaArchivo, "r") as archivo:
        
#         for linea in archivo:
            
#             print(linea[0])

# main()


'''

ESCRITURA DE ARCHIVOS

archivo.write(line)
archivo.writelines(lineas)

'''

'''

LIBRERIA OS

    os.path.isdir(directorio) -> devuelve T o F si el directorio existe o no
    os.path.isfile(nombre archivo) -> devuelve T o F si el archivo existe o no
    
    os.getcwd() -> me trae el directorio en el que estamos
    
    os.path.join(ruta, nombre) -> concatena rutas
    
    os.path.exists(ruta) -> chequea si existe un ruta completa

'''