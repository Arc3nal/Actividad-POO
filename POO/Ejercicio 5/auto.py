# Motor.py
class Motor:
    def __init__(self):
        self.encendido = False

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            print("Motor arrancado.")
        else:
            print("El motor ya está en marcha.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("Motor apagado.")
        else:
            print("El motor ya está apagado.")


# Rueda.py
class Rueda:
    def __init__(self):
        self.inflada = True

    def inflar(self):
        if not self.inflada:
            self.inflada = True
            print("Rueda inflada.")
        else:
            print("La rueda ya está inflada.")

    def desinflar(self):
        if self.inflada:
            self.inflada = False
            print("Rueda desinflada.")
        else:
            print("La rueda ya está desinflada.")


# Ventana.py
class Ventana:
    def __init__(self):
        self.abierta = False

    def abrir(self):
        if not self.abierta:
            self.abierta = True
            print("Ventana abierta.")
        else:
            print("La ventana ya está abierta.")

    def cerrar(self):
        if self.abierta:
            self.abierta = False
            print("Ventana cerrada.")
        else:
            print("La ventana ya está cerrada.")


# Puerta.py
from Ventana import Ventana

class Puerta:
    def __init__(self):
        self.ventana = Ventana()
        self.abierta = False

    def abrir(self):
        if not self.abierta:
            self.abierta = True
            print("Puerta abierta.")
        else:
            print("La puerta ya está abierta.")

    def cerrar(self):
        if self.abierta:
            self.abierta = False
            print("Puerta cerrada.")
        else:
            print("La puerta ya está cerrada.")

    def abrir_ventana(self):
        self.ventana.abrir()

    def cerrar_ventana(self):
        self.ventana.cerrar()


# Coche.py
from Motor import Motor
from Rueda import Rueda
from Puerta import Puerta

class Coche:
    def __init__(self):
        self.motor = Motor()
        self.ruedas = [Rueda() for _ in range(4)]
        self.puertas = [Puerta() for _ in range(2)]

    def arrancar(self):
        self.motor.arrancar()

    def apagar(self):
        self.motor.apagar()

    def inflar_ruedas(self):
        for i, rueda in enumerate(self.ruedas, 1):
            rueda.inflar()
            print(f"Rueda {i} inflada.")

    def desinflar_ruedas(self):
        for i, rueda in enumerate(self.ruedas, 1):
            rueda.desinflar()
            print(f"Rueda {i} desinflada.")

    def abrir_puertas(self):
        for i, puerta in enumerate(self.puertas, 1):
            puerta.abrir()
            print(f"Puerta {i} abierta.")

    def cerrar_puertas(self):
        for i, puerta in enumerate(self.puertas, 1):
            puerta.cerrar()
            print(f"Puerta {i} cerrada.")

    def abrir_ventanas(self):
        for i, puerta in enumerate(self.puertas, 1):
            puerta.abrir_ventana()
            print(f"Ventana de puerta {i} abierta.")

    def cerrar_ventanas(self):
        for i, puerta in enumerate(self.puertas, 1):
            puerta.cerrar_ventana()
            print(f"Ventana de puerta {i} cerrada.")


# main.py (interactivo)
from Coche import Coche

def menu():
    print("\n--- MENÚ DEL COCHE ---")
    print("1. Arrancar motor")
    print("2. Apagar motor")
    print("3. Inflar ruedas")
    print("4. Desinflar ruedas")
    print("5. Abrir puertas")
    print("6. Cerrar puertas")
    print("7. Abrir ventanas")
    print("8. Cerrar ventanas")
    print("9. Salir")
    return input("Elige una opción: ")

mi_coche = Coche()

while True:
    opcion = menu()

    if opcion == "1":
        mi_coche.arrancar()
    elif opcion == "2":
        mi_coche.apagar()
    elif opcion == "3":
        mi_coche.inflar_ruedas()
    elif opcion == "4":
        mi_coche.desinflar_ruedas()
    elif opcion == "5":
        mi_coche.abrir_puertas()
    elif opcion == "6":
        mi_coche.cerrar_puertas()
    elif opcion == "7":
        mi_coche.abrir_ventanas()
    elif opcion == "8":
        mi_coche.cerrar_ventanas()
    elif opcion == "9":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intenta de nuevo.")
