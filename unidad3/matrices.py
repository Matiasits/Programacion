"""
Listas en Python

1 - Ejecute paso a paso el código de este link y describa a continuacion lo que hace cada linea del programa  
"""
miLista = [1024, 3, True, 6.5] #Crea una lista con los elementos 1024, 3, True, 6.5
miLista.append(False)   #Agrega el elemento False al final de la lista  
miLista.insert(2,4.5)   #Agrega el elemnto 4.5 en el indice 2
miLista.pop()   #Elimina el ultimo elemento de la lista
miLista.pop(1)  #Elimina el elemento de la lista ubicado en el indice 1
miLista.pop(2) #Elimina el elemento de la lista ubicado en el indice 2
miLista.sort()  #Ordena la lista
miLista.reverse() #Revierte la lista
miLista.count(6.5) #Cuenta las apariciones en la lista del elemento 6.5
miLista.index(4.5) #Devuelve el indice en la lista del elemento 4.5
miLista.remove(6.5) #Elimina de la lista el elemento 6.5
del miLista[0]  #Elimina de la lista el elemento ubicado en el indice 0

#2 - Ejecute el siguiente código

a=[3,3,3,3,3,3,3,3,3]
for i in range (10):
	print(a[i])

"""
¿Que pasó? 
¿en que linea esta el problema?
Busque en internet que quiere decir ese problema y explicarlo con sus palabras.
Corrija el programa para que funcione

El codigo imprime los elementos de la lista en un rango de 10 repeticiones, da error por que se queda sin elementos que imprimir.
La forma de corregirlo es utilizando el metodo len(a) para asegurarnos de que el rango de iteracion sobre la lista sea 
propiamente de la cantidad de elementos que hay en ella.
"""

#3 - Escriba una función que tome una lista y devuelva la cantidad de elementos pares que tiene. Ej: cuantosPares([2,3,4,5,1,0])=3
#Funcion
def cuantosPares(lista:list) -> int:
    contador = 0
    
    for i in lista:
        if i % 2 == 0:
            contador += 1
    return contador

assert cuantosPares([2,3,4,5,1,0]) == 3
    
#4 - Escribir una función sumaLista() y una función multiplicaLista() que sumen y multipliquen respectivamente todos los números de una lista. 
# Ej: sumaLista([1,2,3,4])=10 y multiplicaLista([1,2,3,4]) = 24.
#Funcion
def sumaLista(lista:list) -> int:
    
    pass


#5 - Escribir una función maximoEnLista() que tome una lista de números y devuelva el más grande. Ej: maximoEnLista([1,2,3,4,2,3]) = 4


#6 - Un filtro es una función que borra todos los elementos que no cumplen con una condición. 
# Escriba una función filtrarPalabrasn() que tome una lista de palabras y un entero n, y borre todas las palabras que tengan menos de n caracteres.
"""
filtrarPalabrasn(palabras:[string],n:int)->[string]: #toma una lista de palabras y devuelve una lista de palabras
filtrarPalabrasn([[“ala”],[“camino”]],4) # [“camino”]
"""
#Funcion
def filtrarPalabrasn(palabras:[str] , n:int) -> [str]:
    for i in palabras:
        if len(i) < n:
            palabras.remove(i)    
    return palabras        
"""
#Sugerencia
for p in palabras:
	if len(p) < 4:
"""

"""
7 - Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar. 
El producto escalar entre dos vectores a=(a1,a2,..,an) y b=(b1,b2,..,bn) se define así a*b=a1*b1+a2*b2+..+an*bn. 
Ej: a=(1,2) y b=(3,4) ->  a*b = 1*3 + 2*4 = 11
"""



"""
8 - Escribe una función llamada "elimina_duplicados" que tome una lista y devuelva una nueva lista con los elementos únicos de la lista original. 
No tienen por qué estar en el mismo orden. (no usen set sino recorran la lista)
"""


#Ejercicios de matrices
"""
9 - Defina una función que devuelva una matriz vacía de nxm (pueden llenarla de None o de 0’s) Ej: a = crearMatriz(2,3). print(a)
0 0 0
0 0 0
"""
"""
10 - Escriba una función que tome una matriz y devuelva la cantidad de filas (m) y Dar otra función que devuelva la cantidad de columnas (n)
Ej: mFilas(a)=2 , nColumnas(a)=3
"""

"""
11 - Programar una función enumF que tome una matriz y numere cada celda de la matriz en orden creciente de izquierda a derecha y de arriba a abajo y otra enumC que numere cada celda de la matriz en orden creciente de arriba a abajo luego izquierda a derecha.

Ej: enumF(a)  1 2 3   enumC(a)= 1 3 5
              4 5 6             2 4 6
"""


#12 - Escriba una función que cuente la cantidad de números pares que hay en una matriz.

"""  
13 - Escriba una función que sume dos matrices
https://es.wikipedia.org/wiki/Adici%C3%B3n_matricial

1 2 + 2 3 = 1+2 2+3
3 4   4 5   3+4 4+5
"""

"""
14 - 
Escriba una función que tome una matriz cuadrada (n y m son iguales) y devuelva una lista con la diagonal de esa matriz (la diagonal es cuando recorro la matriz e i==j) 
otra que sume los elementos de esa lista. diagonal() y sumaDiagonal()
https://es.wikipedia.org/wiki/Diagonal_principal
sea a = [[1,2],[3,4]
diagonal(a) = [1,4]
sumaDiagonal(a) = 5
"""

