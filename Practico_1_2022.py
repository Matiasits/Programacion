"""
Programación 2 2022
Tecnicatura en desarrollo de software
Instituto técnico superior córdoba - Anexo villa el libertador
Prof: Matías Bordone

Práctico 1: Repaso comandos programación 1 - Programación imperativa Python
"""

# 1 Ejercicio entrada, salida y aritmética:
""" Escriba un programa que pida dos números y que escriba su media aritmética.
Se recuerda que la media aritmética de dos números es la suma de ambos números dividida por 2

---
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
def media_aritmetica(a,b):
    return ((a+b)/2)
"""

# 2 Ejercicio entrada, salida y aritmética:
""" Escriba un programa que pida la anchura y altura de un rectángulo y que escriba su área, su perímetro y la longitud de su diagonal.

CÁLCULO DE DATOS DE UN RECTÁNGULO
Escriba la anchura del rectángulo: -4
Escriba la altura del rectángulo: 3
Por favor, escriba valores mayores que cero.

---

print("CALCULO DE DATOS DE UN RECTANGULO")
a = int(input("Escriba la anchura del rectangulo: "))
b = int(input("Escriba la altura del rectangulo:"))
 
def calculo_rectangulo(a,b):
    
    perimetro = (a+b)*2
    area = a*b
    diagonal = pow(((a**2)+(b**2)),0.5)
    
    if a and b > 0:
        print(f"El perimetro es {perimetro}, el area es {area} y la longitud de la diagonal es {diagonal}")
    else:
        print("Por favor, escriba valores mayores que cero.")

calculo_rectangulo(a,b)
    
"""



# 3 Expresion Lógica o Booleana
"""Reemplace x por un valor que haga v == True, describa como comentario que tiene que pasar para que v sea true"""

v = -8 <= -7 #x tiene que ser menor o igual a -7 para que v sea True
v = 20 > 16 #x tiene que ser mayor a 16 para que v sea True
v = 0 != -33 #x tiene que ser distinto de -33 para que v sea True

# 4 Expresion Lógica o Booleana
"""Reemplace x por un valor que haga v == False, describa como comentario que tiene que pasar para que v sea true"""

v = -6 <= -7 #x tiene que ser mayor a -7 para que v sea False
v = 15 > 16 #x tiene que ser menor a 16 para que v sea False
v = -33 != -33 #x tiene que ser igual a -33 para que v sea False

# 5 Expresion Lógica o Booleana
"""asigne a x un valor para hacer v == True"""

x = 0
v = x <= 1 and x != -75 or x == 48
x = 0
x > -71 and x != 7 and x != 75
x = -100
x >= -117 and x <= -45 or x > 19

# 6 Ejercicio if
"""
Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba que son iguales.

COMPARADOR DE NÚMEROS
Escriba un número: 23
Escriba otro número: 14.5
Menor: 14.5; Mayor: 23.0
---
COMPARADOR DE NÚMEROS
Escriba un número: 23
Escriba otro número: 23
Los números son iguales

---

print("COMPARADOR DE NUMEROS")
a = int(input("Escribe un numero: "))
b = int(input("Escribe otro numero: "))


def compara_numeros(a,b):
    if a < b:
        print(f"Menor: {a}; Mayor: {b}")
    elif a > b:
        print(f"Menor: {b}; Mayor: {a}")
    else:
        print("Los numeros son iguales")

    return

compara_numeros(a,b)
"""

# 7 if (2)
""" Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 2024
Para llegar al año 2020 faltan 5 años.

COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 1997
Desde el año 1997 han pasado 22 años.

COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 2019
¡Son el mismo año!

---

print("COMPARADOR DE AÑOS")
a = int(input("¿En que año estamos?: "))
b = int(input("Escriba un año cualquiera: "))

def compare_years(a,b):
    if a < b:
        print(f"Para llegar al año 2020 faltan {b-a} años.")
    elif a > b:
        print(f"Desde el año 1997 han pasado {a-b} años.")
    else:
        print("¡Son el mismo año!")
compare_years(a,b)
"""

# 8 For 
""" Escriba un programa que imprima 10 veces "Tengo que hacer la tarea"

Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
Tengo que hacer la tarea
---
for i in range(10):
    i = "Tengo que hacer la tarea"
    print(i)
"""

# 9 For 
""" Escriba un programa que ayude a recordar una tabla de multiplicar 

¿Cual tabla quiere repasar?: 5
¡Perfecto!
1   x   5   =   5
2   x   5   =   10
3   x   5   =   15
4   x   5   =   20
5   x   5   =   25
6   x   5   =   30
7   x   5   =   35
8   x   5   =   40
9   x   5   =   45
10  x   5   =   50

---

numero = int(input("¿Cual tabla quiere repasar?: "))
tabla = 1
print("¡Perfecto!")

for i in range(10):
    print (f"{tabla} x {numero} = {tabla * numero}")
    tabla += 1
"""

# 10 For
""" Escriba un programa que ayude a recordar una tabla de multiplicar , ahora pidiendo al usuario que ingrese el valor

¿Cual tabla quiere repasar?: 5
¡Perfecto!
1   x   5: 5
Bien
2   x   5: 15
Nop
3   x   5:  15
Bien
4   x   5   =   25
Nop
5   x   5   =   25
Bien
6   x   5   =   30
Bien
7   x   5   =   35
Bien
8   x   5   =   40
Bien
9   x   5   =   45
Bien
10  x   5   =   50
Bien

---

numero = int(input("¿Cual tabla quiere repasar?: "))
tabla = 1
print("¡Perfecto!")

for i in range(10):
    resultado = int(input(f"{tabla} x {numero} = "))
    if (tabla*numero) == resultado:
        print("Bien\n")
    else:
        print("Nop\n")
    tabla += 1

"""

# 11 For (acumulador)
"""
Escriba un programa que pregunte cuantos tickets tiene, luego le pida el monto gastado con cada ticket e imprime el monto total al final

SUMA DE VALORES
¿Cuántos valores va a introducir? -1
¡Imposible!

SUMA DE VALORES
¿Cuántos valores va a introducir? 5
Escriba el ticket 1: 25
Escriba el ticket 2: 30
Escriba el ticket 3: 10.5
Escriba el ticket 4: 14
Escriba el ticket 5: 23
La suma de los números que ha escrito es 102.5

---

print("SUMA DE VALORES")
valores = int(input("¿Cuántos valores va a introducir?: "))

if valores >= 1:
    valor = 1
    suma = []
    for i in range(valores):
        ticket = float(input(f"Escriba el ticket {valor}: "))
        valor += 1
        suma.append(ticket)
    total = sum(suma)
    print(f"La suma de los números que ha escrito es {total}")

else:
    print("¡Imposible!")
"""

# 12 While
""""Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres peticiones.

CONFIRME SU CONTRASEÑA (2)
Escriba su contraseña: cantidubi dubi dubi
Tiene 3 intentos para confirmar su contraseña.
Escriba de nuevo su contraseña: cantidubi dubi da
Las contraseñas no coinciden. Inténtelo de nuevo.
Escriba de nuevo su contraseña: cantidubi dubi dubi
Contraseña confirmada. ¡Hasta la vista!

CONFIRME SU CONTRASEÑA
Escriba su contraseña: pezespada
Tiene 3 intentos para confirmar su contraseña.
Escriba de nuevo su contraseña: Pezespada
Las contraseñas no coinciden. Inténtelo de nuevo.
Escriba de nuevo su contraseña: pezEspada
Las contraseñas no coinciden. Inténtelo de nuevo.
Escriba de nuevo su contraseña: PezEspada
Lo siento, no ha confirmado la contraseña. ¡Hasta la vista!

---

print("CONFIRME SU CONTRASEÑA")
a = input("Escriba su contraseña: ")
print("Tiene 3 intentos para confirmar su contraseña.")
contador = 0

while contador < 3:
    contador += 1
    b = input("Escriba de nuevo su contraseña ")

    if contador == 3:
        print("Lo siento, no ha confirmado la contraseña. ¡Hasta la vista!.")
        break
    elif a != b:
        print("Las contraseñas no coinciden. Inténtelo de nuevo.")
    else:   
        print("Contraseña confirmada. ¡Hasta la vista!")
        break
"""

# 13 While
""" Escriba un programa para jugar a adivinar un número (el ordenador "piensa" el número y el usuario tiene que adivinarlo). El programa empieza pidiendo entre qué números está el número a adivinar, se "inventa" un número al azar y después el usuario va probando valores y el programa va diciendo si son demasiado grandes o pequeños.

Valor mínimo: 0
Valor máximo: 100
Intente adivinar un número entero entre 0 y 100.
Escriba un número: 20
¡Demasiado pequeño! Inténtelo de nuevo: 30
¡Demasiado grande! Inténtelo de nuevo: 27
¡Acertó! Le ha costado 3 intentos.

---

import random

minimo = int(input("Valor mínimo: "))
maximo = int(input("Valor máximo: "))
print(f"Intente adivinar un número entero entre {minimo} y {maximo}.")

ran = random.randint(minimo,maximo)

intentos = 0
while intentos >= 0:
    intentos += 1
    numero = int(input("Escriba un número: "))
    
    if numero < ran:
        print("¡Demasiado pequeño! Inténtelo de nuevo: ")
    elif numero > ran:
        print("¡Demasiado grande! Inténtelo de nuevo: ")
    else:
        print(f"¡Acertó! Le ha costado {intentos} intentos.")
        break
"""