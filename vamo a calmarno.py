import turtle
import random

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("¡Carrera de tortugas!")
ventana.bgcolor("lightblue")
ventana.setup(width=1000, height=600)

# Pista de carreras
pista = turtle.Turtle()
pista.color("gray")
pista.width(20)
pista.penup()
pista.goto(-400, 250)
pista.pendown()
pista.goto(400, 250)
pista.penup()

# Dibujar líneas discontinuas en la pista
pista.color("white")
pista.width(5)
for i in range(-200, 300, 100):
    pista.penup()
    pista.goto(-400, i)
    pista.pendown()
    pista.goto(400, i)

# Crear tortugas
tortugas = []
colores = ["red", "orange", "blue", "green", "purple"]
for i, color in enumerate(colores):
    tortuga = turtle.Turtle()
    tortuga.shape("turtle")
    tortuga.color(color)
    tortuga.penup()
    tortuga.goto(-380, 220 - i * 100)
    tortugas.append(tortuga)

# Función para mover las tortugas aleatoriamente con distancias ajustadas
def mover_tortuga(tortuga):
    distancia = random.randint(5, 15)
    tortuga.forward(distancia)

# Carrera de tortugas
for _ in range(100):
    for tortuga in tortugas:
        mover_tortuga(tortuga)

# Mostrar resultado en la consola
ganador = max(tortugas, key=lambda t: t.xcor())
mensaje = "¡" + ganador.color()[0].capitalize() + " gana!"
print(mensaje)

# Mostrar mensaje en la ventana
resultado = turtle.Turtle()
resultado.color("black")
resultado.penup()
resultado.goto(0, -280)
resultado.write(mensaje, align="center", font=("Arial", 30, "bold"))

ventana.mainloop()
