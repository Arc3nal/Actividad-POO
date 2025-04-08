class Cuenta:
    def __init__(self, numero_cuenta: int, dni_cliente: int, saldo: float = 0.0, interes_anual: float = 0.0):
        """
        Constructor de la clase Cuenta.

        :param numero_cuenta: Número de cuenta (entero largo).
        :param dni_cliente: DNI del cliente (entero largo).
        :param saldo: Saldo actual de la cuenta (float).
        :param interes_anual: Interés anual en porcentaje (float).
        """
        self.numero_cuenta = numero_cuenta
        self.dni_cliente = dni_cliente
        self.saldo = saldo
        self.interes_anual = interes_anual

    # Métodos accesores (getters)
    def get_numero_cuenta(self):
        return self.numero_cuenta

    def get_dni_cliente(self):
        return self.dni_cliente

    def get_saldo(self):
        return self.saldo

    def get_interes_anual(self):
        return self.interes_anual

    # Métodos mutadores (setters)
    def set_interes_anual(self, interes_anual: float):
        self.interes_anual = interes_anual

    # Métodos de operaciones bancarias
    def depositar(self, cantidad: float):
        """ Deposita una cantidad en la cuenta. """
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad:.2f}€. Saldo actual: {self.saldo:.2f}€")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad: float):
        """ Retira una cantidad de la cuenta, si hay saldo suficiente. """
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad:.2f}€. Saldo actual: {self.saldo:.2f}€")
        elif cantidad > self.saldo:
            print(f"Fondos insuficientes. Saldo actual: {self.saldo:.2f}€")
        else:
            print("La cantidad a retirar debe ser mayor que 0.")

    def calcular_interes(self):
        """ Calcula y aplica el interés anual sobre el saldo. """
        interes_ganado = (self.saldo * self.interes_anual) / 100
        self.saldo += interes_ganado
        print(f"Interés aplicado: {interes_ganado:.2f}€. Saldo actual: {self.saldo:.2f}€")

    def mostrar_info(self):
        """ Muestra la información de la cuenta bancaria. """
        print(f"\nNúmero de Cuenta: {self.numero_cuenta}")
        print(f"DNI Cliente: {self.dni_cliente}")
        print(f"Saldo Actual: {self.saldo:.2f}€")
        print(f"Interés Anual: {self.interes_anual:.2f}%\n")


# Función para crear una cuenta pidiendo datos al usuario
def crear_cuenta():
    print("Ingrese los datos de la cuenta bancaria:")
    numero_cuenta = int(input("Número de cuenta: "))
    dni_cliente = int(input("DNI del cliente: "))
    saldo = float(input("Saldo inicial: "))
    interes_anual = float(input("Interés anual (%): "))

    return Cuenta(numero_cuenta, dni_cliente, saldo, interes_anual)


# Programa Principal
if __name__ == "__main__":
    cuenta = crear_cuenta()

    cuenta.mostrar_info()

    # Opciones para el usuario
    while True:
        print("\nSeleccione una opción:")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Calcular interés")
        print("4. Mostrar información")
        print("5. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == "3":
            cuenta.calcular_interes()
        elif opcion == "4":
            cuenta.mostrar_info()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
