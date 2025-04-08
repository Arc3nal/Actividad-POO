class Persona:
    def __init__(self, nombre="", apellido=""):
        """Constructor de Persona con nombre y apellido opcionales."""
        self.nombre = nombre
        self.apellido = apellido

    # Getters
    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    # Método para obtener el nombre completo
    def get_nombre_completo(self):
        return f"{self.apellido}, {self.nombre}"
