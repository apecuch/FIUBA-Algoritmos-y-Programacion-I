/*

MATRIZ

    int matriz[filas][columnas] = { {}, {} };


*/

#include <stdio.h>
#define FILAS 2
#define COLUMNAS 2

void suma(int matrizA[FILAS][COLUMNAS], int matrizB[FILAS][COLUMNAS]) {

    int matrizC[FILAS][COLUMNAS] = {{}};

    for (size_t i = 0; i < 2; i++) {

        for (size_t j = 0; j < 2; j++) {

            matrizC[i][j] = matrizA[i][j] + matrizB[i][j];
        }

    }

}

int main() {

    int matrizA[FILAS][COLUMNAS] = { {1, 2}, {3, 4} };
    int matrizB[FILAS][COLUMNAS] = { {5, 6}, {7, 8} };

    suma(matrizA, matrizB);

    return 0;
}