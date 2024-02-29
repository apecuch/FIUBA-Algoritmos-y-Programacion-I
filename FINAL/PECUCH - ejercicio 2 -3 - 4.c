/*
FINAL ALGORITMOS I - 15/02/2024

    ALUMNO: Pecuch Agustina
    PADRON: 111560
    DNI: 40729147
*/

#include <stdio.h>
#include <ctype.h>

#define LARGO_CADENA 100

int contar_palabras(char *cadena) {
    int palabras = 0;

    for (size_t i = 0; i < LARGO_CADENA; i++) {
        if (isspace(cadena[i])) {
            palabras++;
        }
    }
    
    return palabras;
}

void encontrar_palabra_larga(char *cadena) {
    int cantidad_caracteres_mayor = 0;
    int cantidad_caracteres_actual = 0;

    char* palabra_mayor;
    char* palabra_actual;

    for (size_t i = 0; i < LARGO_CADENA; i++) {
        if (!isspace(cadena[i])) {
            cantidad_caracteres_actual++;
            palabra_actual += cadena[i];
        } else {
            if (palabra_actual > palabra_mayor) {
                palabra_mayor = palabra_actual;
            }
        }
    }

    printf("La palabra mas larga es: %s\n", palabra_mayor);
}


int main() {
    char cadena[LARGO_CADENA] = "Sabiendo que existen grupos de lenguajes interpretados y compilados";

    encontrar_palabra_larga(cadena);

    int cantidad_palabras = contar_palabras(cadena);
       
    return 0;
}

/*

PUNTO 2:
- Lenguajes interpretados: el código se traduce línea por línea a medida que se ejecuta el programa, es decir, en tiempo real.
- Lenguajes compilados: Estos lenguajes se traducen completamente a código de máquina antes de que el programa se ejecute mediante un compilador. Una vez compilado, el programa resultante se puede ejecutar sin necesidad de volver a traducirlo.
Python es interpretado y C es compilado.

PUNTO 3:
Cuando hablamos de pasar parámetros por referencia o por valor, nos referimos a la forma en que se pasa la información a una función.
Esto influye en si los cambios realizados en los parámetros dentro de la función afectarán o no a los valores originales fuera de la función.
- Paso por valor: Significa que se pasa una copia del valor original del argumento a la función. Cualquier modificación realizada dentro de la función no afectará al valor original fuera de ella.
- Paso por referencia: Significa que se pasa la dirección de memoria del valor original del argumento a la función. Cualquier modificación realizada dentro de la función afectará a esos valores fuera de la función también.


void suma_por_valor(int x) {
    x = x + 1;
}

void suma_por_referencia(int *x) {
    (*x) = (*x) + 1;
}

int main() {
    int numero = 5;

    incrementarPorValor(numero);

    incrementarPorReferencia(&numero);

    return 0;
}


*/