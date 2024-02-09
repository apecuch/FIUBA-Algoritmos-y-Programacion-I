/*

PUNTEROS

    Un puntero es una variable que contiene como valor la direccion de memoria de otra variable
    
    TIPO * nombre_variable;
       -> ej: int *ptr   -> puntero a un entero
       -> ptr = &numero  -> el operador de direccion & devuelve la direccion de memoria del operando
       -> *ptr           -> el operador * devuelve el contenido de la variable
    
    

STRUCTS

    Coleccion de una o mas variables, que pueden ser de tipos diferentes, agrupados bajo un solo nombre

    typedef struct {
        int capacidad;
        char destino[30];
    }avion_t;   -> avion_t es el nombre

    - inicializacion:

    avion_t boeing = { 200, "Cordoba" }; -> asi si lo paso en orden
    avion_t airbus = { .capacidad = 200, .destino = "Cordoba" }; -> si no es en orden

    - asignacion:

    boing.capacidad += 20

    - punteros:

    (*ptr_avion).capacidad = 30;
    ptr_avion->capacidad = 30; 


*/

#include <stdio.h>
#include <stdbool.h>
#include <string.h>

/*
Equivalente a:

struct avion {
	int  capacidad;
	char destino[30];
	char empresa[30];
	int  asientos_ocupados;
	bool es_internacional;
};

typedef struct avion avion_t;
*/

typedef struct {
	int  capacidad;
	char destino[30];
	char empresa[30];
	int  asientos_ocupados;
	bool es_internacional;
} avion_t;

typedef struct {
	avion_t* avion_guardado;
} aeropuerto_t;

void vender_asientos(avion_t* avion)
{
	// (*avion).asientos_ocupados += 50;
	avion->asientos_ocupados += 50;
}

void vender_en_aeropuerto(aeropuerto_t* aeropuerto)
{
	// (*((*aeropuerto).avion_guardado)).asientos_ocupados += 50;
	aeropuerto->avion_guardado->asientos_ocupados += 50;
	
	/*
	Cabe destacar que esta funcion es codigo reutilizado, es igual a:
	vender_asientos(aeropuerto->avion_guardado);
	*/
}

int main()
{
	/*
	Equivalente a:
	
	avion_ejemplo.capacidad = 50;
	strcpy(avion_ejemplo.destino, "ABCDE");
	strcpy(avion_ejemplo.empresa, "FGHIJ");
	avion_ejemplo.asientos_ocupados = 30;
	avion_ejemplo.es_internacional = false;
	
	o tambien a (NO USAR ESTO):
	
	avion_t avion_prueba = {200, "AAA", "BBB", 0, false};
	*/
	avion_t avion_prueba = {
		.capacidad = 200,
		.destino = "AAA",
		.empresa = "BBB",
		.asientos_ocupados = 0,
		.es_internacional = false
	};
	
	aeropuerto_t aeropuerto_prueba = {
		.avion_guardado = &avion_prueba
	};
	
	vender_asientos(&avion_prueba);           //Esto vende 50.
	vender_en_aeropuerto(&aeropuerto_prueba); //Y esto otros 50.
	
	//No existe el print lindo para structs, hay que hacerlo manualmente.
	printf("Capacidad: %d\n", avion_prueba.capacidad);
	printf("Destino: %s\n", avion_prueba.destino);
	printf("Empresa: %s\n", avion_prueba.empresa);
	printf("Asientos Ocupados: %d\n", avion_prueba.asientos_ocupados);
	printf("Es Internacional? %d\n", avion_prueba.es_internacional);
	
	return 0;
}