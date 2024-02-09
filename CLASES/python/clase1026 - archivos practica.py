'''

TIPOS DE ARCHIVOS

    - CSV

    import csv

    with open("CSWV", newline='', encoding="utf-8") as archivo:
        csv_reader = csv.reader(archivo, delimiter = ',')
        next(csv_reader)  ### aca evitamos leer el header
        for row in csv_reader:
            datos.append(row)

    with open("CSWV", newline='', encoding="utf-8") as archivo:
        csv_writte = csv.writter(archivo, delimiter = ',', quotechar = '"', quoting = csv.QUOTE.NONNUMERIC)   ### QUOTECHAR: me dice si lo escribe con "" o ''   QUOTING: indica que campos se escriben con el quotechar
        csv_writter.writerow(["Padron", "nombre", "apellido"]) #### escribimos el header

        for padron, nombre in alumnos.items():
        csv_writer.writerow((padron, nombre))
    

    - JSON

    import json

    # Convertir diccionario python a json

        json.dumps(diccionario, indent=3)

    # Convertir de json string a python

        json.loads(string)  ### El string tiene que estar escrito en formato json ej:   {   }
                            ### El LOADS recibe una cadena y devuelve un dict

    # Convertir json file a python

        json.load(open(archivo))   ### El LOAD recibe un archivo y devuelve un dict


    - BINARIOS

    



'''