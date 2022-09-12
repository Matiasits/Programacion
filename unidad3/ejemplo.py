"""
from typing import *
Matrix = List[List[int]]

def filas(a):
    return len(a)

def columnas(a):
    return len(a[0])

def dimension(a):
    return (filas(a),columnas(a))

def contarRepes(m,valor):
    contador = 0 
    dim = dimension(m)
    
    for i in range(dim[0]):
        for j in range(dim[1]):
            if m[i][j] == valor:
                contador = contador + 1
    return contador

c = [[1,3,5],[4,3,5],[2,1,2]]

assert contarRepes(c,1) == 2

def multiplicacion_escalar(M:Matrix, a:int) -> Matrix:
    dim = dimension(M)
    
    for i in range(dim[0]):
        for j in range(dim[1]):
            M[i][j] = M[i][j] * a

"""
from pila import Pila

def balanceada_general(experesion):
    p = Pila()
    p.vaciar_pila()
    balance = True
    indice = 0
    
    while indice < len(experesion) and balanceados:
        simbolo = experesion[indice]
        if simbolo in "([{":
            p.incluir(simbolo)
        else:
            if p.esVacia():
                balanceados = False
            else:
                tope = p.extraer()
                if not parejas(tope,simbolo):
                       balanceados = False
        indice = indice + 1
    if balanceados and p.esVacia():
        return True
    else:
        return False

def parejas(simboloApertura, simboloCierre):
    aperturas = "([{"
    cierres = ")]}"
    return aperturas.index(simboloApertura) == cierres.index(simboloCierre)


print(balanceada_general('{({[][]})()}'))
print(balanceada_general('[{()]'))
