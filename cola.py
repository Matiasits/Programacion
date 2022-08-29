class Cola:
    elementos = []
    
    def agregar(self, item) -> None:
        self.elementos.append(item)
    
    def es_vacia(self) -> bool:
        return self.elementos == []
    
    def primero(self):
        if not self.es_vacia():
            return self.elementos[0]

    def tamanio(self) -> int:
        return len(self.elementos)
    
    def sacar(self):
        return self.elementos.pop(0)

    def __str__(self):
        return ("{}".format(self.elementos))

    def concatenar(self, cola2):
        # este metodo concatena dos colas, pone la cola 2 al final de la cola 1
        # usar metodos de cola
        # saco cada elemento de cola 2 y lo pongo en cola 1 (self)
        # al final del metodo la cola 2 debe tener los mismos elmentos que al principio
        # (es decir que no borra la cola 2)
        for i in range(cola2.tamanio()):
            self.agregar(cola2.sacar())

    def concatenar2(self, cola2):
        c2 = [self.agregar(i) for i in range(cola2.tamanio())]
        self.concatenar(c2)
    
    def imprimir_cola(self):
        for i in self.elementos():
            print(i)
    
    def vaciar_cola(self):
        self.elementos = []
    
    def dar_vuelta(self):
        self.elementos = [self.sacar() for i in range(self.tamanio())]
        
        

#Ejercicicio 3: Implementar en un archivo de python la clase cola vista en clase

p = Cola() # crea una cola (vacia)
#print(p.es_vacia()) #True
p.agregar(4) # 
p.agregar('perro')
#print(p.elementos) # [4,'perro']
#print(p.primero()) # 4
p.agregar(True) # [4,'perro',true]
#print(p.tamanio()) # 3
#print(p.es_vacia()) #False
p.agregar(8.4) # [4,'perro',true,8.4]
#print(p.sacar()) # imprime el 4 y lo saca
#print(p.sacar()) # impreme perro y lo saca
#print(p.tamanio()) # 2
#print(p.dar_vuelta())
"""
def concatenar(self,cola2): # cortar pegar
        # este metodo concatena dos colas, pone la cola 2 al final de la cola 1
        # usar metodos de cola
        # saco cada elemento de cola 2 y lo pongo en cola 1 (self)
        while not cola2.es_vacia(): #
            aux = cola2.sacar()
            self.agregar(aux)
    
    def concatenar2(self,cola2): # copiar pegar
        # este metodo concatena dos colas, pone la cola 2 al final de la cola 1
        # usar metodos de cola
        # saco cada elemento de cola 2 y lo pongo en cola 1 (self)
        # al final del metodo la cola 2 debe tener los mismos elmentos que al principio
        # (es decir que no borra la cola 2)
"""

# Ejercicio 4: 
# Agregar a la clase cola los siguientes métodos (usando preferentemente los métodos ya utilizados)
#    1. Imprimir cola
#    2. Vaciar la cola.
#    3. Dar vuelta cola


# Ejercicio 5:
# Escriba una función que reciba una Cola C1 y mueva sus elementos a una nueva Cola c2, manteniendo el orden de salida de los elementos.
# Al finalizar la Cola C1 no debe contener elementos.

def trasladar(c:Cola)->Cola:
    C2 = Cola()
    C2.vaciar_cola()

    for i in range(c.tamanio()):
            C2.agregar(c.sacar())

trasladar(p)
assert p.es_vacia == True