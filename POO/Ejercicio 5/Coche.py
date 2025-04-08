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
