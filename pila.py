class Pila:
    p = []
    
    def esVacia(self)->bool:
        return self.p == [] 

    def incluir(self, item)->None:
        self.p.append(item)

    def extraer(self):
        return self.p.pop() 

    def inspeccionar(self):
        if not self.esVacia():
            return self.p[-1]

    def tamano(self):
        return len(self.p)
    
    def vaciar_pila(self):
        self.p = []
    
    def imprimir_pila(self):
        for item in self.p:
            print(item)
    
    def dar_vuelta(self):
        self.p = [self.extraer() for i in range(self.tamano())]
        
"""
p = Pila()
p.incluir(4)
p.incluir(2)
p.incluir(1)
assert p.inspeccionar() == 1
assert p.p == [4, 2, 1]
assert p.extraer() == 1
assert p.inspeccionar() == 2

p = Pila()
p.incluir(4)
p.incluir(2)
p.incluir(1)
assert p.inspeccionar() == 1
print(p.p)
assert p.p == [4, 2, 1]
p.dar_vuelta()
assert p.p == [1, 2, 4]
assert p.extraer() == 4
assert p.inspeccionar() == 2
p.vaciar_pila()
assert p.estaVacia() == True
"""
#TEST 
"""
pila1 = Pila()
pila1.incluir(4)
pila1.incluir(2)
pila1.incluir(1)
assert pila1.inspeccionar() == 1
assert pila1.p == [4, 2, 1]
pila1.dar_vuelta()
assert pila1.p == [1, 2, 4]
pila1.imprimir_pila()
assert pila1.extraer() == 4
assert pila1.inspeccionar() == 2
pila1.vaciar_pila()
assert pila1.esVacia() == True
"""
"""
2. Agregar a la clase pila los siguientes métodos (usando preferentemente los métodos ya utilizados)
    a. Dar vuelta pila (al finalizar el método la misma pila tiene que estar dada vuelta)
    b. Imprimir pila (imprimir elemento a elemento, no “la lista”)
    c. Vaciar pila.

3. Usando pilas y la función split escribir una función en python que revierta una cadena de palabras
Entrada: "Mi Diario Python"
Salida: "Python Diario Mi"
"""

def revCadena(cadena:str) -> str:
    lst = cadena.split()
    pila = Pila()

    for item in lst:
        pila.incluir(item)
    
    lst1 = [pila.extraer() for i in range(pila.tamano())]

    x = " ".join(lst1)
    print(x)

revCadena("Mi diario Python")

"""
4. Usando pilas haga una función que diga si una expresión
(un string) tiene la misma cantidad de 0's que de 1's
"""

def contar0y1(palabra:str)->bool:
    pila = Pila()
    
    
    for i in palabra:
        pila.incluir(i)
    
    cero = pila.p.count("0")
    uno = pila.p.count("1")
    return cero == uno
    

assert contar0y1("ajsndakjsdn0asd1") == True
assert contar0y1("ajsndakjsdn0asd11") == False





"""
6. Usando pilas escribir una función en python para encontrar la validez de una cadena de paréntesis, '(', ')', '{', '}', '['']. 
Los paréntesis deben aparecer en el orden correcto, por ejemplo "()" y "()[]{}" son válidos, pero "[)", "({[)]" y "{{{" son inválidos.
"""