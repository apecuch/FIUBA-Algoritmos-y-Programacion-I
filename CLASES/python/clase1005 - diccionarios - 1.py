"""

Crear un programa que dada una tupla (alumno, padron), este nos imprima por pantalla el promedio de todas sus notas.

Las notas de cada alumno ya tienen que estar cargadas.

Tanto el nombre como el apellido estan siempre en uppercase.

"""

def promedioAlumno(listaNotas:list) -> float:

    sumaNotas:int = sum(listaNotas)
    promedio:float = sumaNotas / len(listaNotas)

    return promedio

def solicitarNombreyPadron() -> list:
    nombre:str = input("Ingrese el nombre del alumno: ").upper()
    padron:str = input("Ingrese el padron del alumno: ").upper()

    return nombre, padron

def main() -> None:

    notasAlumnos:dict = {
        ("MARTINEZ", "1234") : [10, 5, 3, 7, 9, 1],
        ("PECUCH", "40729") : [10, 7, 8, 9, 6, 5]
    }

    nombre, padron = solicitarNombreyPadron()
    promedio:float = promedioAlumno(notasAlumnos.get((nombre, padron)))

    print("El promedio del alumno", nombre, "es:", promedio)

main()

