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
