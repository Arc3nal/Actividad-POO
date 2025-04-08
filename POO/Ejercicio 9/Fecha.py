class Fecha:
    def __init__(self, dia=1, mes=1, anio=1900):
        """Constructor de Fecha con valores predeterminados."""
        self.dia = dia
        self.mes = mes
        self.anio = anio

    # Getters
    def get_dia(self):
        return self.dia

    def get_mes(self):
        return self.mes

    def get_anio(self):
        return self.anio

    # Setters
    def set_dia(self, dia):
        self.dia = dia

    def set_mes(self, mes):
        self.mes = mes

    def set_anio(self, anio):
        self.anio = anio

    # Método para obtener la fecha en formato largo
    def get_fecha_larga(self):
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                 "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        return f"{self.dia} de {meses[self.mes - 1]} de {self.anio}"
