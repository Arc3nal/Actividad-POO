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
