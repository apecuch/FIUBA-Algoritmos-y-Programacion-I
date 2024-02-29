#include <stdio.h>

int comparar(char *cadena1, char *cadena2) {

    int indice = 0;

    while (cadena1[indice] != '\0' || cadena2[indice] != '\0') {       // '\0' Caracter nulo
        if (cadena1[indice] != cadena2[indice]) {
            return 0;
        } 

        indice++;
    }

    return 1;
}

int main() {
    char* cadena1 = "hola";
    char* cadena2 = "hola";
    
    if (comparar(cadena1, cadena2)) {
        printf("Las cadenas son iguales.\n");
    } else {
        printf("Las cadenas son diferentes.\n");
    }
        
    return 0;
}