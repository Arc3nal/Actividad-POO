from turtle import *
import colorsys

h = 0  # Variable global para el matiz

def flor(x, y, size):
    global h
    penup()
    goto(x, y)
    pendown()
    for i in range(12):
        setheading(i * 30)
        for j in range(18):
            c = colorsys.hsv_to_rgb(h, 0.9, 1)  # Color dinámico
            color(c)
            h += 0.005  # Incremento suave para que el degradado sea más fluido
            rt(90)
            circle(size - j * 5, 90)
            lt(90)
            circle(size - j * 5, 90)
            rt(180)
        circle(size * 0.3, 24)

speed(0)
bgcolor("black")
hideturtle()
tracer(0, 0)  # Dibuja todo de golpe al final para más velocidad

# Dibujamos las flores más separadas y con tamaños variados
flor(-250, 150, 160)
flor(200, 120, 140)
flor(-100, -150, 150)

update()  # Renderiza todo de una vez
done()

