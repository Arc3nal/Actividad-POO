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
