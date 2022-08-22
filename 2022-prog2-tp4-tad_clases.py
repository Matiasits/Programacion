"""
1.A  Implementar una clase llamada AlumnoMateria con las partes Constructor, operaciones y condiciones.
Constructor: nombre, nota, materia
Operaciones: imprimir datos y mostrar_estado() {libre, regular, promocional}
Condiciones: Nombre y materia tiene que ser texto, nota tiene que ser un entero (entre 0 y 10)
"""
class AlumnoMateria:
    def __init__(self, nombre, materia, nota): # Agregar parámetros
        """funcion que inicializa una variable AlumnoMateria
        tener en cuenta las condiciones del TAD (texto e int)
        """
        assert type(nombre) == str, "Esto no es un string"
        assert type(materia) == str, "Esto no es un string"
        assert type(nota) == int, f"Esto no es un entero es {type(nota)}"
        assert nota >= 0 and nota <= 10, "nota no esta entre 0 y 10"
        
        self.nombre = nombre
        self.nota = nota
        self.materia = materia
    def __str__(self)->str:
        return f"{self.nombre}, {self.materia}, {self.nota}"
    def mostrar_estado(self)->str: 
        """calcula si esta regular, promocionado, o libre"""
        nota = self.nota
        if nota<4:
            estado = "libre"
        elif nota >= 4 and nota < 7:
            estado = "regular"
        else:
            estado = "promocionado"
        return estado

# Test
alumno1 = AlumnoMateria ("Juan", "Matemáticas", 4)
assert alumno1.__str__() == "Juan, Matemáticas, 4"
assert alumno1.mostrar_estado() == "regular"

"""
1.B Implementar la clase registroAlumnoMateria() que guarde varias notas
 y diga si el alumno está regular, promocional o libre. Con las 
siguientes reglas.
    Constructor: (Nombre, Materia)
    Agregar nota: Agrega una nota al alumno en la materia (lista de notas)
    Promedio: Devuelve el promedio de notas que tiene el alumno
    Mostrar notas: imprime una por una la lista de notas
    Condiciones: Nombre y materia tiene que ser texto, nota tiene que ser un entero (entre 0 y 10)
"""
class RegistroAlumnoMateria:
    notas = []
    def __init__(self, nombre, materia): # Agregar parámetros
        """funcion que inicializa una variable registroAlumnoMateria"""
        pass
    def agregar_nota(self,nota)->None:
        pass
    def mostrar_notas(self)->None:
        pass
    def calcular_promedio(self)->float:
        pass
    def mostrar_estado(self)->str: 
        """calcula si esta regular, promocionado, o libre
        si saca menos de 4 de promedio , queda libre
        Promocion promedio de 7 y todas las notas 6 o mas.
        Sino Regular
        """
        pass
    
    def __str__(self)->str:
        pass


a = RegistroAlumnoMateria ("Juan", "Matemáticas")
a.agregar_nota(4)
a.agregar_nota(10)

assert a.mostrar_estado() == "regular"
assert a.calcular_promedio() == 7.0
assert a.__str__() == "Juan, Matemáticas, regular"


"""
2.a A la clase punto vista en la materia agregarle el método Distancia al origen ()siendo el origen el punto (0,0). Crear un programa que use este método para imprimir en pantalla la distancia entre al origen de los puntos A, B y C.
"""
A = Punto(2,3)
B = Punto(5,5)
C = Punto(1,5)

A.distancia(B)
assert A.distancia_origen() == 3.605551275463989
assert B.distancia_origen() == 7.0710678118654755
assert C.distancia_origen() == 5.0990195135927845

"""
2.b Utilizando el método de distancia al origen cree una función que tome una lista de puntos y devuelva el que se encuentra más alejado del origen.
def mas_lejos(lista:[Punto])->Punto
toma una lista de puntos y devuelve el mas alejado del origen
"""
assert mas_lejos([Punto(2,3) , Punto( 5,5 ), Punto(1,5)]) == Punto(5,5)

"""
3. Crear una clase circulo: 
constructor: punto(x, y), radio; 
operaciones:diametro,  perimetro y area.
"""
#Tomar de ejemplo la clase rectangulo
class Circulo:
    def __init__( self ): # toma un radio , centro
        pass
    def diametro ( self ):
        pass
    def perimetro ( self ):
        pass 
    def area ( self ):
        pass
    def __eq__(self,otro):
        pass
    def mover(self):
        pass
c = Circulo(0, 0, 4.5)
assert c.diametro() == 9.0
assert c.area_circulo() == 63.61725123519331
assert c.perimetro_circulo() == 28.274333882308138

# 4.a
""" Crea una clase llamada Polígono que tendrá los siguientes atributos: 
    + número de lados (un entero)
    + origen (un punto x,y en el plano)
    Tanto el numero de lados como el origen son obligatorios
    Construye los siguientes métodos para la clase:
    + Un constructor, donde los datos pueden estar vacíos.
    + Es válido. (los polígonos deben tener más de 2 lados)
    Además:
    + mover (básicamente es actualizar el atributo origen)
    + __str__ describe el polígono con sus atributos
 """

class Poligono():
    def __init__(self, lados, origen=) -> None:
        self.lados = lados
    def __str__(self) -> str:
        pass
    def es_valido(self) -> bool:
        pass
    def mover(self):
        pass


poligono = Poligono (3,(0,0))
poligono.es_valido() == True
poligono.obtener_origen() == (0,0)
poligono.mover((0,1))
poligono.obtener_origen() == (0,1)
poligono.__str__() == "Polígono, lados: 3, origen (0,1)"

poligono = Poligono (2,(0,0))
poligono.es_valido() == False

print("Fin ejercicio 5.a!")

# 4.b
"""
Extienda la clase polígono utilizando herencia para crear otra llamada Polígono regular que represente esta figura
    + deberá agregar como atributo la longitud de los lados
    + modifique el init para incluir el largo de lados
    Agregar como métodos
    + como es un poligono regular sabemos que "angulo = 360°/cantidad de lados". Implemente un método que lo calcule
    + calcular el perímetro del polígono
    + modifique el método str para indicar que es un polígono regular y la longitud de sus lados

No implementar los metodos de la clase polígono de nuevo, usar herencia de clases
"""    
class Poligono_regular():
    pass
poligono = Poligono_regular (3,(0,0),2)
poligono.obtener_origen() == (0,0)
poligono.mover((0,1))
poligono.obtener_origen() == (0,1)
poligono.angulo() == 120
poligono.perimetro = 6
poligono.__str__() == "Polígono Regular, lados: 3, origen (0,0), largo lados: 2"

poligono = Poligono (2,(0,0))
poligono.es_valido() == False

print("Fin ejercicio 5.b!")