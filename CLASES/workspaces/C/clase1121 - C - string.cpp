/*

STRINGS

    char * string = "Hola como estas";

    s%

    LIBRERIA <string.h>

        char * strcat( char *dest, char *origen); -> une 2 str -> devuelve el puntero a destino
        int strcmp( char *str1, char *str2); -> compara 2 str -> devuelve 1 si el 1ro es mayor que el 2do, 0 si son iguales, -1 si el 2do es mayor al 1
        char * strcopy( char *dest, char *src) -> copia un string al destino
        size_t strlen(char *str) -> devuelve el largo del string
*/

#include <stdio.h>
#include <string.h>

int main()
{
	char* nombre   = "Pepe";
	char* apellido = "Perez";
	
	// Estos dos metodos son equivalentes.
	
	char nombre_completo_1[32];
	strcat(nombre_completo_1, apellido);
	strcat(nombre_completo_1, ", ");
	strcat(nombre_completo_1, nombre);
	
	char nombre_completo_2[32];
	sprintf(nombre_completo_2, "%s, %s", apellido, nombre);
	
	printf("El nombre completo 1 es: %s\n", nombre_completo_1);
	printf("El nombre completo 2 es: %s\n", nombre_completo_2);
	
	return 0;
}