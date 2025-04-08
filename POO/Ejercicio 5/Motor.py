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
