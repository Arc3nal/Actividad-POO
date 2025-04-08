from tkinter import *
from math import *

# Configuración de la ventana
ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x600")
ventana.configure(background="skyblue4")

# Variable global para la entrada de texto
operador = ""
input_text = StringVar()
input_text.set("0")  # Valor inicial en pantalla

def btnClik(num):
    global operador
    operador += str(num)
    input_text.set(operador)

def resultado():
    global operador
    try:
        opera = str(eval(operador))
        input_text.set(opera)
        operador = opera
    except:
        input_text.set("ERROR")
        operador = ""

def clear():
    global operador
    operador = ""
    input_text.set("0")

# Configuración de botones
ancho_boton = 11
Alto_boton = 3
color_boton = "gray77"

def crear_boton(texto, x, y, cmd=None):
    """Crea un botón y lo posiciona en la ventana."""
    return Button(ventana, text=texto, width=ancho_boton, height=Alto_boton, bg=color_boton, 
                  command=cmd if cmd else lambda: btnClik(texto)).place(x=x, y=y)

# Creación de botones
crear_boton("0", 17, 180)
crear_boton("1", 107, 180)
crear_boton("2", 197, 180)
crear_boton("3", 287, 180)
crear_boton("4", 17, 240)
crear_boton("5", 107, 240)
crear_boton("6", 197, 240)
crear_boton("7", 287, 240)
crear_boton("8", 17, 300)
crear_boton("9", 107, 300)
crear_boton("π", 197, 300, lambda: btnClik(pi))  # π como número
crear_boton(",", 287, 300)
crear_boton("+", 17, 360)
crear_boton("-", 107, 360)
crear_boton("*", 197, 360)
crear_boton("/", 287, 360)
crear_boton("√", 17, 420, lambda: btnClik("sqrt("))
crear_boton("EXP", 197, 420, lambda: btnClik("**"))
crear_boton("(", 17, 480)
crear_boton(")", 107, 480)
crear_boton("%", 197, 480, lambda: btnClik("/100"))
crear_boton("In", 287, 480, lambda: btnClik("log("))

# Botones con comandos especiales
Button(ventana, text="C", width=ancho_boton, height=Alto_boton, bg=color_boton, command=clear).place(x=107, y=420)
Button(ventana, text="=", width=ancho_boton, height=Alto_boton, bg=color_boton, command=resultado).place(x=287, y=420)

# Campo de salida (pantalla de la calculadora)
salida = Entry(ventana, font=("arial", 20, "bold"), width=22, bg="powder blue", 
               justify="right", textvariable=input_text)
salida.place(x=10, y=60)

ventana.mainloop()
