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

    def concatenar(self, cola2):
        # este metodo concatena dos colas, pone la cola 2 al final de la cola 1
        # usar metodos de cola
        # saco cada elemento de cola 2 y lo pongo en cola 1 (self)
        # al final del metodo la cola 2 debe tener los mismos elmentos que al principio
        # (es decir que no borra la cola 2)
        for i in range(cola2.tamanio()):
            self.agregar(cola2.sacar())

  #  def concatenar2(self, cola2):
  #      c2 = [self.agregar(i) for i in range(cola2.tamanio())]
   #     self.concatenar(c2)


    
        


cola1 = Cola()
cola1.agregar(10)
assert cola1.tamanio() == 1
cola1.agregar(9)
assert cola1.tamanio() == 2
assert cola1.primero() == 10
assert cola1.sacar() == 10
assert cola1.tamanio() == 1

cola1.agregar(8)
cola1.agregar(7)

cola2 = Cola()
cola2.agregar(6)
cola2.agregar(5)
cola2.agregar(4)

print(cola1.elementos)
print(cola2.elementos)
cola1.concatenar(cola2)



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