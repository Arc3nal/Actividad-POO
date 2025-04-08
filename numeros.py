import random

class AdivinaElNumero:
    def __init__(self):
        self.numero_objetivo = random.randint(1, 30)
        self.intentos = 0
        self.juego_terminado = False

    def generar_pista(self):
        """Genera una pista adicional sobre el número secreto."""
        pistas = []
        
        # Pista sobre par o impar
        if self.numero_objetivo % 2 == 0:
            pistas.append("El número es par.")
        else:
            pistas.append("El número es impar.")

        # Pista sobre diferencia con otro número
        otro_numero = self.numero_objetivo + random.choice([-10, -5, 5, 10])
        if 1 <= otro_numero <= 30:  # Nos aseguramos de que esté en el rango válido
            pistas.append(f"Es diferente de {otro_numero}.")

        return random.choice(pistas)  # Devuelve una pista aleatoria

    def adivinar(self, intento):
        """Compara el intento con el número objetivo y da retroalimentación."""
        self.intentos += 1
        
        if intento < self.numero_objetivo:
            return f"El número es mayor. {self.generar_pista()}"
        elif intento > self.numero_objetivo:
            return f"El número es menor. {self.generar_pista()}"
        else:
            self.juego_terminado = True
            return f"¡Felicidades! Adivinaste el número en {self.intentos} intentos."

    def jugar(self):
        print("Bienvenido al juego de adivinar el número.")
        print("He elegido un número entre 1 y 30. Intenta adivinarlo.")
        
        while not self.juego_terminado:
            try:
                intento = int(input("Introduce tu intento: "))
                if intento < 1 or intento > 30:
                    print("Por favor, introduce un número entre 1 y 30.")
                    continue
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            resultado = self.adivinar(intento)
            print(resultado)

# Iniciar el juego
juego = AdivinaElNumero()
juego.jugar()
