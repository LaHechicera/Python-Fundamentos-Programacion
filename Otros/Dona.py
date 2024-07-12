import turtle
import math

# Configuración inicial de Turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Dona Giratoria")

# Crear la tortuga para dibujar
donut = turtle.Turtle()
donut.shape("circle")
donut.color("pink")

# Función para dibujar un círculo con un radio específico
def draw_circle(t, radius):
    t.circle(radius)

# Función para mover la tortuga a una posición sin dibujar
def move_turtle(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Dibujar la dona
move_turtle(donut, 0, -120)
draw_circle(donut, 120)

# Función para girar la dona
def rotate_donut():
    for angle in range(0, 360, 10):
        donut.right(10)
        wn.update()

# Hacer que la dona gire indefinidamente
while True:
    rotate_donut()

# Mantener abierta la ventana hasta que se cierre manualmente
wn.mainloop()