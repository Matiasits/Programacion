#Juego Pong basico

"""
Iniciamos una pantalla en modo de ventana, con su titulo correspondiente, color de fondo, ancho y alto.
Con ventana.tracer se utiliza para activar o desactivar la animación de la tortuga y establecer un retraso para actualizar los dibujos.
"""

import turtle

ventana = turtle.Screen()
ventana.title("Juego Pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

#Paleta A
paleta_a = turtle.Turtle()
paleta_a.speed(0) #velocidad de la paleta
paleta_a.shape("square")
paleta_a.shapesize(stretch_wid=5, stretch_len=1)
paleta_a.color("white")
paleta_a.penup()
paleta_a.goto(-350,0)


#Paleta B
paleta_b = turtle.Turtle()
paleta_b.speed(0) #velocidad de la paleta
paleta_b.shape("square")
paleta_b.shapesize(stretch_wid=5, stretch_len=1)
paleta_b.color("white")
paleta_b.penup()
paleta_b.goto(350,0)

#Pelotita
pelota = turtle.Turtle()
pelota.speed(0) #velocidad de la pelota
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)

#funciones movimientos
def paleta_a_up(): #paleta A arriba
    y = paleta_a.ycor()
    y += 20
    paleta_a.sety(y)

def paleta_a_down(): #paleta A abajo
    y = paleta_a.ycor()
    y -= 20
    paleta_a.sety(y)

def paleta_b_up(): #paleta B abajo
    y = paleta_b.ycor()
    y += 20
    paleta_b.sety(y)

def paleta_b_down(): #paleta B abajo
    y = paleta_b.ycor()
    y -= 20
    paleta_b.sety(y)
    
    

#obtiene info de la ventana segun las teclas que se accionen
ventana.listen()

#si se presiona la letra "w" o "s", llama a las funciones
ventana.onkeypress(paleta_a_up,"w")
ventana.onkeypress(paleta_a_down,"s")

#si se presiona la letra "Up" o "Down", llama a las funciones
ventana.onkeypress(paleta_b_up,"Up")
ventana.onkeypress(paleta_b_down,"Down")

#bucle de juego principal
while True:
    ventana.update()