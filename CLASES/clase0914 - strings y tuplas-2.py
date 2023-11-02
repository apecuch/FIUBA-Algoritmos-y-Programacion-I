"""
Ejercicio: permitir al usuario ingresar N fechas (ejemplo de formato: 2023-09-14) y luego mostrar por pantalla la fecha más antigua y la fecha más reciente con el siguiente formato:

FECHA MAS ANTIGUA: [DIA] / [MES] / [AÑO]
FECHA MAS RECIENTE: [DIA] / [MES] / [AÑO]
"""

condicionCorte:str = "*"
tuplaDeFechas:tuple = ()

fecha:str = input("Ingrese una fecha con el formato aaaa-mm-dd o * para finalizar: ")
fechaMayor = fecha
fechaMenor = fecha

while fecha != condicionCorte:

    tuplaDeFechas += (fecha,)
    fecha = input("Ingrese una fecha con el formato aaaa-mm-dd o * para finalizar: ")

for fecha in tuplaDeFechas:
    if fecha > fechaMayor:
        fechaMayor = fecha
    if fecha < fechaMenor:
        fechaMenor = fecha

print("La fecha mas reciente es:", fechaMayor[8:10], "/", fechaMayor[5:7], "/", fechaMayor[0:4])
print("La fecha mas antigua es:", fechaMenor[8:10], "/", fechaMenor[5:7], "/", fechaMenor[0:4])
