from lzma import MODE_NORMAL


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
        for i in range(cola2.tamanio()):
            self.agregar(cola2.sacar())
    
    def imprimir_cola(self):
        for i in self.elementos():
            print(i)
    
    def vaciar_cola(self):
        self.elementos = []
    
    def dar_vuelta(self):
        self.elementos = [self.sacar() for i in range(self.tamanio())]
        
    #Ejercicio 6
    """ Escriba un metodo de Cola que dada una cola C1 reciba una cola C2  de 
    números enteros y devuelva una nueva Cola con los elementos concatenados en el 
    orden C1 y C2. Es de destacar que las Colas recibidas no deben sufrir ningún 
    tipo de cambio o alteración.(en principio utilizar los métodos de cola para la 
    tarea)"""
    def concatenar_orden(self,cola2):
        
        for i in range(cola2.tamanio()):
            elemento = cola2.sacar()
            self.agregar(elemento)
            cola2.agregar(elemento)

        """Escriba una rutina que reciba dos Colas C1 y C2 de números enteros y 
        proceda a intercambiar sus elementos, manteniendo el orden de salida de los mismos.
        Al finalizar la rutina, la Cola C1 tendrá los elementos de la 
        Cola C2 y ésta a su vez tendrá los elementos de la Cola C1."""

    def intercambiar(self,c2):
        if c2.tamanio() > self.tamanio():
            mayor, menor = c2.tamanio(), self.tamanio() 
        else:
            mayor, menor = self.tamanio(), c2.tamanio()
        
        for i in range(mayor):
            c2.agregar(self.sacar())
            self.agregar(c2.sacar())
        for i in range(mayor-menor):
            c2.agregar(self.sacar())
            self.agregar(c2.sacar())
        


#c1.intercambiar(c2) 
# c1 = [1,4,8] y c2 = [4,2,7]
# c2 == [1,4,8] y c1 == [4,2,7]

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

c2 = Cola()
print(c2.es_vacia())
c2.vaciar_cola()

c2.agregar(1)
c2.agregar(2)
c2.agregar(3)
c2.agregar(4)
c2.agregar(5)

print(f"cola inicial {p.elementos}")
print(f"cola aniadida {c2.elementos}\n")

p.intercambiar(c2)
print(f"cola inicial {p.elementos}")
print(f"cola aniadida {c2.elementos}")
#print(p.sacar()) # imprime el 4 y lo saca
#print(p.sacar()) # impreme perro y lo saca
#print(p.tamanio()) # 2
#print(p.dar_vuelta())

# Ejercicio 4: 
# Agregar a la clase cola los siguientes métodos (usando preferentemente los métodos ya utilizados)
#    1. Imprimir cola
#    2. Vaciar la cola.
#    3. Dar vuelta cola


# Ejercicio 5:
# Escriba una función que reciba una Cola C1 y mueva sus elementos a una nueva Cola c2, 
# manteniendo el orden de salida de los elementos.
# Al finalizar la Cola C1 no debe contener elementos.

def trasladar(c1:Cola)->Cola:
    c2 = Cola()
    c2.vaciar_cola()
    
    for i in range(c1.tamanio()):
            c2.agregar(c1.sacar())

c1 = Cola()

trasladar(c1)
assert c1.es_vacia() == True

