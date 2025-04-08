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
