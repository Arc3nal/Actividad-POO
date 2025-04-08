class Hora:
    def __init__(self, horas=0, minutos=0, segundos=0):
        """Constructor: por defecto 00:00:00 o con valores dados."""
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self.__valida()

    def __valida(self):
        """Método privado para validar y corregir la hora si es inválida."""
        if not (0 <= self.horas < 24):
            self.horas = 0
        if not (0 <= self.minutos < 60):
            self.minutos = 0
        if not (0 <= self.segundos < 60):
            self.segundos = 0

    def leer(self):
        """Solicita al usuario la hora, los minutos y los segundos."""
        try:
            self.horas = int(input("Introduce las horas (0-23): "))
            self.minutos = int(input("Introduce los minutos (0-59): "))
            self.segundos = int(input("Introduce los segundos (0-59): "))
        except ValueError:
            print("Error: Introduce valores numéricos válidos.")
            self.horas, self.minutos, self.segundos = 0, 0, 0

        self.__valida()

    def print(self):
        """Muestra la hora en formato HH:MM:SS."""
        print(f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}")

    def aSegundos(self):
        """Devuelve los segundos transcurridos desde la medianoche."""
        return self.horas * 3600 + self.minutos * 60 + self.segundos

    def deSegundos(self, segundos):
        """Establece la hora a partir de los segundos transcurridos desde la medianoche."""
        segundos %= 86400  # Evita valores mayores a un día
        self.horas = segundos // 3600
        self.minutos = (segundos % 3600) // 60
        self.segundos = segundos % 60

    def segundosDesde(self, otra_hora):
        """Devuelve el número de segundos entre la hora actual y otra hora."""
        return abs(self.aSegundos() - otra_hora.aSegundos())

    def siguiente(self):
        """Pasa al siguiente segundo."""
        self.deSegundos(self.aSegundos() + 1)

    def anterior(self):
        """Pasa al segundo anterior."""
        self.deSegundos(self.aSegundos() - 1)

    def copia(self):
        """Devuelve un clon de la hora."""
        return Hora(self.horas, self.minutos, self.segundos)

    def igualQue(self, otra_hora):
        """Indica si la hora es la misma que la proporcionada."""
        return self.aSegundos() == otra_hora.aSegundos()

    def menorQue(self, otra_hora):
        """Indica si la hora es anterior a la proporcionada."""
        return self.aSegundos() < otra_hora.aSegundos()

    def mayorQue(self, otra_hora):
        """Indica si la hora es posterior a la proporcionada."""
        return self.aSegundos() > otra_hora.aSegundos()


# Menú interactivo
def menu():
    print("\n--- MENÚ HORA ---")
    print("1. Ingresar nueva hora")
    print("2. Mostrar hora actual")
    print("3. Convertir a segundos")
    print("4. Definir hora desde segundos")
    print("5. Avanzar un segundo")
    print("6. Retroceder un segundo")
    print("7. Comparar con otra hora")
    print("8. Salir")
    return input("Elige una opción: ")


# Programa principal
if __name__ == "__main__":
    mi_hora = Hora()  # Hora inicial por defecto

    while True:
        opcion = menu()

        if opcion == "1":
            mi_hora.leer()
        elif opcion == "2":
            print("Hora actual:", end=" ")
            mi_hora.print()
        elif opcion == "3":
            print(f"Segundos desde medianoche: {mi_hora.aSegundos()}")
        elif opcion == "4":
            segundos = int(input("Introduce el número de segundos desde medianoche: "))
            mi_hora.deSegundos(segundos)
            print("Hora actualizada:", end=" ")
            mi_hora.print()
        elif opcion == "5":
            mi_hora.siguiente()
            print("Hora tras avanzar un segundo:", end=" ")
            mi_hora.print()
        elif opcion == "6":
            mi_hora.anterior()
            print("Hora tras retroceder un segundo:", end=" ")
            mi_hora.print()
        elif opcion == "7":
            print("Introduce otra hora para comparar:")
            otra_hora = Hora()
            otra_hora.leer()
            if mi_hora.igualQue(otra_hora):
                print("Las horas son iguales.")
            elif mi_hora.menorQue(otra_hora):
                print("La hora actual es menor que la ingresada.")
            else:
                print("La hora actual es mayor que la ingresada.")
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")
