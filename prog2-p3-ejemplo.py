# 1 Pilas
class Pila:
    def __init__(self):
        self.items = []
    
    def esVacia(self)->bool:
        """pregunta si no hay niongun dato en la pila"""
        #return len(self.items) == 0
        return self.items == []

    def incluir(self, item)->None:
        """agrega un elemento a mi pila"""
        self.items.append(item)

    def extraer(self):
        """extrae un elemento de la pila, en este caso el último de la lista"""
        return self.items.pop() # me devuelve el ultimo elemento y lo borra

    def inspeccionar(self):
        """Ver cual es el tope de la pila"""
        return self.items[-1]

    def tamano(self):
        """me dice al cantidad de elementos que tenemos en la pila"""
        return len(self.items())
    
    def __eq__(self,otra_pila)->bool:
        """Definimos cuando dos pilas son iguales"""
        return (self.items == otra_pila.items)
    
    def __str__(self):
        return str(self.items)

"""
Agregue 2 métodos:
a) remover: pila x tipo_item -> pila: elimina todas las ocurrencias de un item en la pila
b) montar: pila x pila  →  pila,  para  poner  la  segunda  pila  encima  de  la  primera
(respetando el orden de los elementos).
"""

p = Pila()
p.incluir(1)
p.incluir(3)
p.incluir(5)
p.incluir(1)
p.incluir(5)
p.incluir(6)
p.remover(5)

assert p.extraer() == 6
assert p.extraer() == 1
assert p.extraer() == 3
assert p.extraer() == 1

print("Fin ejercicio 1.a!")

p1 = Pila()
p1.incluir(1)
p1.incluir(3)
p1.incluir(5)

p2 = Pila()
p2.incluir(1)
p2.incluir(5)
p2.incluir(6)

p1.montar(p2)
assert p1.__str__() == "[1, 3, 5, 1, 5, 6]"

print("Fin ejercicio 1.b!")

# 3 Colas
class Cola:
    """La cola es una coleccion de datos lineales, FIFO (First in First out)"""
    def __init__(self):
      self.elementos = []
      
    def incluir(self, item):
        self.elementos.append(item)

    def es_vacia(self)->bool:
        return self.elementos == []

    def primero(self): # fijarse que no este vacia
        if not self.es_vacia():
            return self.elementos[0]

    def tamanio(self):
        return len(self.elementos)

    def sacar(self):
        if not self.es_vacia():
            return self.elementos.pop(0)
        
    def __str__(self):
        return ("{}".format(self.elementos))
    
"""
Agregue 1 funcion:
+ mezclar_impares: toma los elementos pares de las dos listas y los
mezcla alternativamente (no tienen que
ser necesariamente de la misma longitud)
"""

c = Cola()
c.incluir(1)
c.incluir(3)
c.incluir(1)
c.incluir(5)

c2 = Cola()
c2.incluir(1)
c2.incluir(5)
c2.incluir(6)
c3 = mezclar_impares(c,c2)
assert c1.__str__() == "[1,3,1,5]"
assert c2.__str__() == "[1,5,6]"
assert c.__str__() == "[1, 1, 3, 5, 1, 5]"

print("Fin ejercicio 2!")

# 3 Matrices
# dada las funciónes
from typing import List,Tuple
Matrix = List[List[int]]

def filas(A:Matrix)->int: #devuelve la cantidad de filas (o m) de la matriz
    return len(A)

def columnas(A:Matrix)->int: #devuelve la cantidad de columnas (o n) de una matriz
    return len(A[0])

def dimension(A:Matrix)->Tuple[int,int]: # Devuelve una tupla (un par) con el valor (filas,columnas)
    return (filas(A),columnas(A))

"""
Las matrices simétricas son matrices donde para todo elemento de la matriz a[i][j] == a [j][i],
fíjense que esto funciona si la matriz es cuadrada, filas(M) = columna(M)
Escriba una función que tome una matriz cuadrada (n y m son iguales) y
devuelva si es simétrica o no.
"""
M1 = [[1,3,5],
      [4,3,5],
      [2,1,2]] # 3 filas x 3 columnas

M2 = [[1,2,3],
      [2,3,5],
      [3,5,2]] # 3 filas x 3 columnas

def matriz_simetrica(M:Matrix)->bool:
    pass
assert matriz_simetrica(M1) == False
assert matriz_simetrica(M2) == True

print("Fin ejercicio 3!")