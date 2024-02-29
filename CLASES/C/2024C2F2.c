#include <stdio.h>
#define N 5

int suma(int numeros[], size_t n) {
    int total = 0;
    for (size_t i = 0; i < n; i++) {
        total += numeros[i];
    }
    return total;
}

float promedio(int numeros[], size_t n) {
    int suma_numeros = suma(numeros, n);

    return (float) suma_numeros / (float) n;
}

int hallar_max(int numeros[], int n) {
    int max = numeros[0];

    for(size_t i = 0; i < n; i++) {

        if(numeros[i] > max) {
            max= numeros[i];
        } 
    }

    return max;
}

int main() {

    int numeros[N];
    int numero = 0;
    int i = 0;

    for (size_t i = 0; i < N; i++) {
        printf("Ingrese un numero: \n >> ");
        scanf("%d", &numero);
        numeros[i] = numero;
    }

    float valor_promedio = promedio(numeros, N);
    int max = hallar_max(numeros, N);

    return 0;
}