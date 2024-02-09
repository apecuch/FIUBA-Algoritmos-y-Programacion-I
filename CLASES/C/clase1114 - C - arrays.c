/*

ARRAYS

    - no son dinamicos

    TIPO nombre[cuantos elementos];
    int vector[4] = { 1, 2, 3, 4};

    int vec[10];
    int *p_vec;
    p_vec = &vec[o]; -> mi puntero apunta la posicion 0 de mi vector

*/

#include <stdio.h>
#define N 5


int suma(int numeros[], size_t n) {
    int total = 0;
    for (size_t i = 0; i < n; i++) {
        total += numeros[i];
    }
    return total;
}


int main() {
    int numeros[N] = { 1, 3, 4, 5, 6 };
    //size_t n = sizeof(numeros) / sizeof(numeros[0]);

    int total = suma(numeros, N);

    printf("El total es: %d", total);
    
    return 0;
}