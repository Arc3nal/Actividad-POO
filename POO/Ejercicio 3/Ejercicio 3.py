class Cafetera:
    def __init__(self, capacidadMaxima=1000, cantidadActual=0):
        """
        Constructor de la clase Cafetera.
        
        :param capacidadMaxima: Capacidad máxima de la cafetera en c.c.
        :param cantidadActual: Cantidad actual de café en c.c.
        """
        self._capacidadMaxima = capacidadMaxima
        self._cantidadActual = min(cantidadActual, capacidadMaxima)
    
    # Accesores
    def get_capacidadMaxima(self):
        return self._capacidadMaxima
    
    def get_cantidadActual(self):
        return self._cantidadActual
    
    # Mutadores
    def set_capacidadMaxima(self, capacidadMaxima):
        self._capacidadMaxima = capacidadMaxima
        if self._cantidadActual > capacidadMaxima:
            self._cantidadActual = capacidadMaxima
    
    def set_cantidadActual(self, cantidadActual):
        self._cantidadActual = min(cantidadActual, self._capacidadMaxima)
    
    # Métodos de operación
    def llenarCafetera(self):
        """ Llena la cafetera hasta su capacidad máxima. """
        self._cantidadActual = self._capacidadMaxima
        print(f"Cafetera llena, cantidad actual: {self._cantidadActual} c.c.")

    def servirTaza(self, cantidad):
        """ Sirve una taza de café con la cantidad indicada. """
        if self._cantidadActual >= cantidad:
            self._cantidadActual -= cantidad
            print(f"Sirviendo taza de {cantidad} c.c., se sirvió: {cantidad} c.c.")
        else:
            print(f"Sirviendo taza de {self._cantidadActual} c.c. (No había suficiente café)")
            self._cantidadActual = 0

        print(f"Cantidad actual después de servir: {self._cantidadActual} c.c.")

    def vaciarCafetera(self):
        """ Vacía la cafetera completamente. """
        self._cantidadActual = 0
        print("Cafetera vacía. Cantidad actual: 0 c.c.")

    def agregarCafe(self, cantidad):
        """ Agrega café a la cafetera sin superar la capacidad máxima. """
        self._cantidadActual = min(self._cantidadActual + cantidad, self._capacidadMaxima)
        print(f"Cantidad actual tras agregar café: {self._cantidadActual} c.c.")

# Función para crear una cafetera con valores ingresados por el usuario
def crear_cafetera():
    capacidad = int(input("Ingrese la capacidad máxima de la cafetera (c.c.): "))
    cantidad = int(input("Ingrese la cantidad actual de café (c.c.): "))
    return Cafetera(capacidad, cantidad)

# Programa principal con menú interactivo
if __name__ == "__main__":
    cafetera = crear_cafetera()

    while True:
        print("\n--- MENÚ CAFETERA ---")
        print("1. Llenar cafetera")
        print("2. Servir taza")
        print("3. Vaciar cafetera")
        print("4. Agregar café")
        print("5. Mostrar cantidad actual")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cafetera.llenarCafetera()
        elif opcion == "2":
            cantidad = int(input("Ingrese el tamaño de la taza (c.c.): "))
            cafetera.servirTaza(cantidad)
        elif opcion == "3":
            cafetera.vaciarCafetera()
        elif opcion == "4":
            cantidad = int(input("Ingrese la cantidad de café a agregar (c.c.): "))
            cafetera.agregarCafe(cantidad)
        elif opcion == "5":
            print(f"Cantidad actual de café: {cafetera.get_cantidadActual()} c.c.")
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
