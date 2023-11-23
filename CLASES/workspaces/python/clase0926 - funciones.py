"""
    # FUNCIONES
        - Bloque de codigo organizado y reutilizable

        SYNTAXIS

            def nombre_funcion (parametro1: param_type) -> return_type:
                # codigo
                return resultado

            - los parametros se separan con coma ","

        EJEMPLOS

            def suma ( num1:int, num2:int ) -> int:
                resultado:int = num1 + num2
                return resultado

        FUNCION MAIN()

            - obligatoria
            - no lleva parametro

            def main () -> None:
                SOLO VARIABLES Y LLAMADOS A FUNCIONES
            
            main()

        PROCEDIMIENTOS

            - funciones que no retornan ningun valor
            - como el main() el type del return es None

    # PASAJE DE PARAMETROS

        POR VALOR
            - la funcion recibe solo una copia del valor que tiene la variable

        POR REFERENCIA
            - la funcion recibe la posicion de memoria donde esta guardada la variable -> permite que la funcion modifique el valor de la variable
                                                                                       -> tiene que se runa variable de tipo mutable (list)
            - para copiar el contenido y no usar la referencia puedo usar el metodo .copy()
                                                                                       
    # VARIABLES LOCALES
        - se crean dentro de la funcion y se usan solamente ahi

"""