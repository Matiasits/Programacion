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
        self.p = self.p[::-1]

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

2. Agregar a la clase pila los siguientes métodos (usando preferentemente los métodos ya utilizados)
    a. Dar vuelta pila (al finalizar el método la misma pila tiene que estar dada vuelta)
    b. Imprimir pila (imprimir elemento a elemento, no “la lista”)
    c. Vaciar pila.

3. Usando pilas y la función split escribir una función en python que revierta una cadena de palabras
Entrada: "Mi Diario Python"
Salida: "Python Diario Mi"
"""

def revCadena(cadena) -> str:
    lst = cadena.split()
    p = Pila()
    
    for item in lst:
        p.incluir(item)
    p.dar_vuelta()
    p.imprimir_pila()
    vuelta = ''.join(p)
revCadena("hola mundo")