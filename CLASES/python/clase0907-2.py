""""
  Un docente de FIUBA recibe un listado con muchos alumnos, a priori no conoce la cantidad que hay, dado que son realmente muchos y le llevaría mucho tiempo contar las filas.
Se pide crear un programa que permita la nota final de los alumnos.
Al finalizar la carga total de alumnos el programa deberá mostrar por pantalla la cantidad de alumnos desaprobados, aprobados, el promedio de notas

"""

cantidadAlumnos = 0
condicionAprobados = 4
canidadAlumnosAprobados = 0
cantidadAlumnosDesaprobados = 0
sumaNotas = 0

condicionFinPrograma = -1

nota = int(input("Ingrese la nota del alumno o -1 para terminar: "))

while nota != condicionFinPrograma:

    if (nota >= condicionAprobados):
        canidadAlumnosAprobados += 1
    elif (nota <= condicionAprobados):
        cantidadAlumnosDesaprobados += 1

    cantidadAlumnos += 1
    sumaNotas += nota

    nota = int(input("Ingrese la nota del alumno o -1 para terminar: "))

if (cantidadAlumnos > 0):
    promedio = sumaNotas / cantidadAlumnos
    print("Cantidad de alumnos aprobados: ", canidadAlumnosAprobados)
    print("Cantidad de alumnos desaprobados: ", cantidadAlumnosDesaprobados)
    print("Promedio de notas: ", promedio)
else:
    print("No ingreso ninguna nota.")
