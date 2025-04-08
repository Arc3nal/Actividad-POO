from datetime import date, timedelta

class Fecha:
    def __init__(self, dia=1, mes=1, anio=1900):
        self._dia = dia
        self._mes = mes
        self._anio = anio
        self._valida()
    
    def _valida(self):
        if not (1900 <= self._anio <= 2050):
            self._anio = 1900
        if not (1 <= self._mes <= 12):
            self._mes = 1
        if not (1 <= self._dia <= self.diasMes(self._mes)):
            self._dia = 1
    
    def leer(self, titulo=""):
        if titulo:
            print(titulo)
        self._dia = int(input("Día (1-31): "))
        self._mes = int(input("Mes (1-12): "))
        self._anio = int(input("Año (1900-2050): "))
        self._valida()
    
    def bisiesto(self):
        return (self._anio % 4 == 0 and self._anio % 100 != 0) or (self._anio % 400 == 0)
    
    def diasMes(self, mes):
        dias_por_mes = [31, 29 if self.bisiesto() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return dias_por_mes[mes - 1]
    
    def corta(self):
        return f"{self._dia:02d}-{self._mes:02d}-{self._anio}"
    
    def diasTranscurridos(self):
        fecha_actual = date(self._anio, self._mes, self._dia)
        fecha_base = date(1900, 1, 1)
        return (fecha_actual - fecha_base).days
    
    def diaSemana(self):
        return (self.diasTranscurridos() % 7)
    
    def larga(self):
        dias_semana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        return f"{dias_semana[self.diaSemana()]} {self._dia} de {meses[self._mes - 1]} de {self._anio}"
    
    def fechaTras(self, dias):
        nueva_fecha = date(1900, 1, 1) + timedelta(days=dias)
        self._dia, self._mes, self._anio = nueva_fecha.day, nueva_fecha.month, nueva_fecha.year
    
    def diasEntre(self, otra):
        fecha1 = date(self._anio, self._mes, self._dia)
        fecha2 = date(otra._anio, otra._mes, otra._dia)
        return abs((fecha1 - fecha2).days)
    
    def siguiente(self):
        self.fechaTras(self.diasTranscurridos() + 1)
    
    def anterior(self):
        self.fechaTras(self.diasTranscurridos() - 1)
    
    def copia(self):
        return Fecha(self._dia, self._mes, self._anio)
    
    def igualQue(self, otra):
        return self._dia == otra._dia and self._mes == otra._mes and self._anio == otra._anio
    
    def menorQue(self, otra):
        return date(self._anio, self._mes, self._dia) < date(otra._anio, otra._mes, otra._anio)
    
    def mayorQue(self, otra):
        return date(self._anio, self._mes, self._dia) > date(otra._anio, otra._mes, otra._anio)

# Creación de Fecha 1 y Fecha 2 con mensajes
fecha1 = Fecha()
fecha1.leer("Fecha 1:")

fecha2 = Fecha()
fecha2.leer("Fecha 2:")

print("\nInformación de Fecha 1:")
print("Fecha corta:", fecha1.corta())
print("Fecha larga:", fecha1.larga())
print("Día de la semana:", fecha1.diaSemana())
print("Días transcurridos desde 1-1-1900:", fecha1.diasTranscurridos())
print("Es bisiesto:", fecha1.bisiesto())

print("\nInformación de Fecha 2:")
print("Fecha corta:", fecha2.corta())
print("Fecha larga:", fecha2.larga())
print("Día de la semana:", fecha2.diaSemana())
print("Días transcurridos desde 1-1-1900:", fecha2.diasTranscurridos())
print("Es bisiesto:", fecha2.bisiesto())

print("\nDías entre Fecha 1 y Fecha 2:", fecha1.diasEntre(fecha2))
