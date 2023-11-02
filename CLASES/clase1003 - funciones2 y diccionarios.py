"""

# PARAMETROS POR DEFECTO
    Forma de indicar que valor debe ser pasado a una funcion en caso de que no se pasen cuando se llama a la funcion

    def saludar(saludo:str = "mundo"):

# MODULOS
    Es la forma de dividir el programa en partes independientes
    Se usa para funciones completamente independientes
    - Cada archivo .py es un modulo

    Para implementar modulos:

        import nombreDelArchivo             -> al principio del archivo que va a tener el main

        from nombreDelArchivo import nombreFuncion         -> aca me ahorro dsps tener que poner el nombre del archivo cuando llamo a la funcion

    Para llamar a las funciones de otro modulo:

        nombreArchivo.nombreFuncion()

        
    + MODULOS ESTANDAR

        - modulos tipicos ya emplementados
        - math, random, os

# PAQUETES
    Son carpetas que contienen modulos.
    Para acceder a cada una se hace con el " . " como en el caso de los modulos

    import nombrePaquete.nombreSubPaquete

    from nombrePaquete import nombreSubPaquete
    

    

# DICCIONARIOS !!!

    - coleccion no ordenada de valores que son accedidos a traves de una clave
    - claves son unicas             -> si declaro 2 claves iguales se pisan

    nombreVariable : dict = { clave1:valor, clave2:valor2, clave3:valor3 }

    + Insertar valores

        materias[lunes] = [valor]

    + Operador IN

        Para chequear si una clave esta en el diccionario

            clave in diccionario:

    + Operador FOR

        Para iterar por claves

            for clave in diccionario:
            
        Para iterar por item dentro de clave

            for dia, codigos in materias.items():
            
    + REFERENCIAS

        diccionario.keys()
        diccionario.values()
        diccionario.items() -> clave y valor
        diccionario.get(clave, []) -> devuelve el valor de la clave dada y si no la encuentra devuelve lo que sigue despues de la " , "

    + ELIMINAR

        Remove an item by key and return its value: pop()
        Remove an item and return its key and value: popitem()
        Remove an item by key: del

"""