"""
Programación 2 2022
Tecnicatura en desarrollo de software
Instituto técnico superior córdoba - Anexo villa el libertador
Prof: Matías Bordone
Estudiantes: Matias Roldan

Práctico 3: Listas y cadenas de caracteres
"""

# 1 Escribir una función sum() que sume todos los números de una lista.

def sum(a:list) -> int:
    elemento = 0
    for i in a:
        elemento += i
    return elemento
assert sum([1,2,3,4]) == 10
assert sum([1,2,3,4]) != 30

# 2 Escribir una función mul() que multiplique todos los números de una lista.
def mul(a:list)->int:
    elemento = 1
    for i in a:
        elemento *= i
    return elemento
assert mul([1,2,3,4]) == 24

# 3 Sin usar la funcion de lista count implementar la funcion que cuenta la cantidad de veces que aparece une elemento en una lista.
def contar(l:list,a)->int:
    veces = 0
    for i in l:
        if i == a:
            veces += 1
    return veces
assert contar([1,2,3,4],3) == 1
assert contar([1,2,3,4],3) != 2
assert contar([1,2,3,4,4],4) == 2

# 4 Definir una función longitud() que calcule la longitud de una lista o una cadena dada. (Python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio).
def longitud (a:list)->int:
    elementos = 0
    for i in a:
        elementos += 1
    return elementos
assert longitud([1,2,3,4]) == 4
assert longitud([]) == 0

# 5 Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
def superposicion(a:list,b:list)->bool:
    x = False
    for i in a:
        for j in b:
            if i == j:
                x = True
    return x
assert superposicion([1,2,3],[2,4,8]) == True #(2 se esta en las 2 listas)
assert superposicion([1,3,5],[2,4,6]) == False #(no hay elementos comunes)

# 6 Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).
def remover_dup(l:list)->list:
    lista = [] 
    for i in l:
        if i not in lista:
            lista.append(i)
    return lista
assert remover_dup([1,5,6,7,2,3,4,1,2,5]) == [1, 5, 6, 7, 2, 3, 4]

# 7 Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
def es_vocal(c:str)->bool:
    x = True
    if c not in ["a","e","i","o","u"]:
        x = False
    return x
assert es_vocal ("f") == False
assert es_vocal ("a") == True
assert es_vocal ("ala") == False
assert es_vocal ("aa") == False

# 8 Hacer una función que intercambie los caracteres indice i,j de un string, si los inices son mayores al largo del string no deberia hacer nada
def intercambiar_dos(s:str,i:int,j:int)->str:
    if j < len(s):
        a = s[j]
        b = s[i]
        a , b = a+(s[1:j]), b+(s[(j+1):])
        y = "".join([a,b])
    else:
        y = s
    return y

assert intercambiar_dos("hola mundo",0,5) == "mola hundo"
assert intercambiar_dos("hola mundo",0,20) == "hola mundo"

# 9 Hacer una función que de vuelta las palabras sin usar la función reverse.
def dar_vuelta(s:str)-> str:
    return s[::-1]
assert dar_vuelta("hola") == "aloh"

# 10 Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas)
def es_palindromo(s:str)->bool:
    x = False
    if s == s[::-1]:
        x = True
    return x
assert es_palindromo ("radar") == True
assert es_palindromo ("rada") == False

# 11 Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
def generar_n_caracteres(n:int,c:str)->str:
    a = ""
    for i in range(n):
        a += c
    return a
assert generar_n_caracteres(5, "x") == "xxxxx"
assert generar_n_caracteres(4, "x") != "xxxxx"
