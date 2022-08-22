"""
Programación 2 2022
Tecnicatura en desarrollo de software
Instituto técnico superior córdoba - Anexo villa el libertador
Prof: Matías Bordone
Estudiantes: (Matias Roldan)
Práctico 4: Tuplas, diccionarios y conjuntos
Teórico: https://python-para-impacientes.blogspot.com/2014/01/cadenas-listas-tuplas-diccionarios-y.html
"""

# 1 Definir 3 tuplas e imprimir sus elementos.
a = "a",2
b = "b",3
c = "c",3
assert type(a) == tuple
assert type(b) == tuple
assert type(c) == tuple
print(a)
print(b)
print(c)

# 2 Definir una función que tome una lista y devuelva el mayor y el menor en una tupla (sin usar la funcion min y max)
def max_min(l:list)->tuple:
    ordena = sorted(l)
    max_y_min = (ordena[-1],ordena[0])
    return max_y_min

assert max_min([3,-1,6,22]) == (22,-1)
assert max_min([3,6,22]) == (22,3)

# 3 Hacer un programa, que tome dos listas, las convierta en conjuntos y conteste si tiene los mismos elementos.
def mismos_elementos(l1:list,l2:list)->bool:
    a = set(l1)
    b = set(l2)
    c = a.issubset(b)
    return c
assert mismos_elementos([1,2,3,4],[4,4,3,3,2,1]) == True
assert mismos_elementos([1,2,3,4],[4,4,3,3,2]) == False

# 4 Hacer un programa, que tome dos listas, las convierta en conjuntos y devuelva los elementos de l1 que no están en l2
def l1_no_l2(l1:list,l2:list)->set:
    a = set(l1)
    b = set(l2)
    c = a.difference(b)
    return c
    
assert l1_no_l2([1,2,3,4],[4,4,3,3,2,1]) == set() #conjunto vacio
assert l1_no_l2([1,2,3,4],[4,4,3,3,2]) == {1}

# 5.1 definir un diccionario que almacene los nombres de países como clave y como valor la cantidad de habitantes. Valores a guardar:
"""
Brasil 210147125
Colombia 50372424
Argentina 44938712
Perú 32131400
Venezuela 28670000
Chile 19107216
Ecuador 17300000
Bolivia  11383940
Paraguay 7152703
Uruguay 3529140
Guyana 761000
Surinam 524000
Guayana Francesa 187000
"""
d = {'Brasil':210147125, 
    'Colombia':50372424, 
    'Argentina':44938712, 
    'Peru':32131400, 
    'Venezuela':28670000, 
    'Chile':19107216, 
    'Ecuador':17300000, 
    'Bolivia':11383940, 
    'Paraguay':7152703, 
    'Uruguay':3529140, 
    'Guyana':761000, 
    'Surinam':524000, 
    'Guayana Francesa':187000}
assert d["Argentina"] == 44938712

# 5.2 Implementar una procedimiento para mostrar cada clave y valor.
# (nota) los procedimientos son como las funciones pero no devuelven un valor
def mostrar_diccionario(d:dict)->None:
    for k,v in d.items():
        k,v

# 5.3 Implementar una función que tome el diccionario, calcule la poblacion total de latinoamerica y devuelva el valor (pista, usar un for para recorrer el diccionario)
def calcular_poblacion(d:dict)->int:
    poblacion = 0
    for k in d:
        poblacion += d[k]
    return poblacion
assert calcular_poblacion(d) == 426204660

# 6
"""Escribir un programa que cree un diccionario de traducción inglés-español.
El programa debe crear un diccionario con las palabras y sus traducciones.
Después pedirá una frase en ingles y utilizará el diccionario para traducirla palabra a palabra.
Si una palabra no está en el diccionario debe dejarla sin traducir."""

def agregar_palabra(d:dict , ingles:str, esp:str)-> None:
    d[ingles]=esp
    
def traducir(d:dict, frase:str) -> str:
    concatenar = []
    desglosar = frase.split()
    
    for i in desglosar:
        valor = d.get(i)
        if i in d:
            concatenar.append(valor)
        else:
            concatenar.append(i)
    traduccion = " ".join(concatenar)
    return traduccion

dic = {}
agregar_palabra(dic,"dog","perro")
agregar_palabra(dic,"the","el")
agregar_palabra(dic,"eat","comer")
agregar_palabra(dic,"dinner","cena")
assert traducir(dic,"the dog eat the dinner late") == "el perro comer el cena late"