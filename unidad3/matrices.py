from typing import *

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