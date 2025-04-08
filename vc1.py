from turtle import *
import colorsys

def flor(x, y):
   
    global h
    penup()
    goto(x, y)
    pendown()
    for i in range(12):  
        setheading(i * 30)  
        for j in range(18):  
            c = colorsys.hsv_to_rgb(0.15, 0.9, 1)  
            color(c)
            h += 0.02  
            rt(90)
            circle(150 - j * 6, 90)
            lt(90)
            circle(150 - j * 6, 90)
            rt(180)
        circle(40, 24)  

speed(0)
bgcolor("black")
h = 0  


flor(-250, 150)  
flor(100, 120)   
flor(-100, -150)  

done()
