"""
Ejercicio 1
Suponga que usted tiene que ordenar la siguiente lista de números: [19, 1, 9, 7, 3, 10, 13, 15, 8, 12].
¿Cuál de las siguientes listas representa la lista parcialmente ordenada tras tres pasadas completas del ordenamiento burbuja?
A. [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]
B. [1, 3, 7, 9, 10, 8, 12, 13, 15, 19] <--
C. [1, 7, 3, 9, 10, 13, 8, 12, 15, 19]
D. [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]
La lista B.


Ejercicio 2:
Suponga que usted tiene que ordenar la siguiente lista de números: [15, 5, 4, 18, 12, 19, 14, 10, 8, 20]
¿Cuál de las siguientes listas representa la lista parcialmente ordenada tras tres pasadas completas del ordenamiento por inserción?
A. [4, 5, 12, 15, 14, 10, 8, 18, 19, 20]
B. [15, 5, 4, 10, 12, 8, 14, 18, 19, 20]
C. [4, 5, 15, 18, 12, 19, 14, 10, 8, 20] <--
D. [15, 5, 4, 18, 12, 19, 14, 8, 10, 20]
La lista C.



Ejercicio 3:
Suponga que usted tiene que ordenar la siguiente lista de números: [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
¿Cuál de las siguientes listas representa la lista parcialmente ordenada tras tres pasadas completas del ordenamiento por selección? 
A. [7, 11, 12, 1, 6, 14, 8, 18, 19, 20]
B. [7, 11, 12, 14, 19, 1, 6, 18, 8, 20]
C. [11, 7, 12, 14, 1, 6, 8, 18, 19, 20]
D. [11, 7, 12, 14, 8, 1, 6, 18, 19, 20] <--
La lista D



Ejercicio 4:
Dada la siguiente lista de números [14, 17, 13, 15, 19, 10, 3, 16, 9, 12]
¿Cuál respuesta corresponde al contenido de la lista después de la segunda partición de acuerdo al algoritmo de ordenamiento rápido? 
A. [9, 3, 10, 13, 12]
B. [9, 3, 10, 13, 12, 14]
C. [9, 3, 10, 13, 12, 14, 17, 16, 15, 19] 
D. [9, 3, 10, 13, 12, 14, 19, 16, 15, 17] <--
La lista D

"""
#Ejercicio 5
#Dada la siguiente implementación de inserción, modificarla para que ordene de mayor a menor

def ordenamientoPorInsercion(unaLista):
   for indice in range(1,len(unaLista)):

     valorActual = unaLista[indice]
     posicion = indice

     while posicion>0 and unaLista[posicion-1]<valorActual: #en esta linea se cambia el "sentido" de ordenacion de unaLista[posicion-1]<valorActual a unaLista[posicion-1]>valorActual
         unaLista[posicion]=unaLista[posicion-1]
         posicion = posicion-1

     unaLista[posicion]=valorActual
     
unaLista = [54,26,93,17,77,31,44,55,20]
ordenamientoPorInsercion(unaLista)
print(unaLista)
