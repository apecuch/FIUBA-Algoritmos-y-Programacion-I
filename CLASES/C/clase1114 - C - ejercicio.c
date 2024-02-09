#include <stdio.h>
#define CORTE -1


int suma(int numeros[], size_t n) {
    int total = 0;
    for (size_t i = 0; i < n; i++) {
        total += numeros[i];
    }
    return total;
}


float promedio(int numeros[], size_t n) {
    int suma_edades = suma(numeros, n);

    // Casteo los valores a float
    return (float) suma_edades / (float) n;
}


int main() {
    int edades[7];
    int edad = 0;
    int i = 0;

    while (edad != CORTE && i < 7) {
        printf("Ingrese una edad o -1 para salir: \n >> ");
        scanf("%d", &edad);
        if (edad != CORTE) {
            edades[i] = edad;
            i++;
        }
    }

    float edad_promedio = promedio(edades, (size_t) i);

    printf("La edad promedio es: %.2f\n", edad_promedio);
    
    return 0;
}