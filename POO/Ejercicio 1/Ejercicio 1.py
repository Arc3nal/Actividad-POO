class Complejo:
    def __init__(self, real=0, imaginario=0):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        return f"({self.real} {'+' if self.imaginario >= 0 else '-'} {abs(self.imaginario)}i)"
    
    def suma(self, otro):
        return Complejo(self.real + otro.real, self.imaginario + otro.imaginario)
    
    def resta(self, otro):
        return Complejo(self.real - otro.real, self.imaginario - otro.imaginario)
    
    def multiplicacion(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return Complejo(real, imaginario)
    
    def division(self, otro):
        if otro.real == 0 and otro.imaginario == 0:
            raise ValueError("No se puede dividir por cero")
        
        denominador = otro.real**2 + otro.imaginario**2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / denominador
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / denominador
        return Complejo(real, imaginario)

# Función para obtener un número complejo preguntando por valor, permitiendo "2i"
def obtener_complejo():
    real = float(input("Ingrese la parte real: "))
    imaginario_str = input("Ingrese la parte imaginaria (ejemplo: 2i o -3i): ")
    
    # Quitar la "i" si el usuario la ingresó
    if imaginario_str.endswith('i'):
        imaginario_str = imaginario_str[:-1]
    
    try:
        imaginario = float(imaginario_str)
    except ValueError:
        print("Error: Formato incorrecto para la parte imaginaria. Intente de nuevo.")
        return obtener_complejo()

    return Complejo(real, imaginario)

# Pedir los números complejos al usuario
print("Ingrese el primer número complejo:")
c1 = obtener_complejo()

print("Ingrese el segundo número complejo:")
c2 = obtener_complejo()

# Realizar operaciones y mostrar resultados
print("Suma:", c1.suma(c2))
print("Resta:", c1.resta(c2))
print("Multiplicación:", c1.multiplicacion(c2))
try:
    print("División:", c1.division(c2))
except ValueError as e:
    print(e)
