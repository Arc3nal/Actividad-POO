import random

class SerMagico:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def atacar(self):
        print(f"{self.nombre} ataca con magia!")

class Mago(SerMagico):
    def __init__(self, nombre, nivel):
        super().__init__(nombre, "Mago")
        self.nivel = nivel

    def lanzar_hechizo(self):
        print(f"{self.nombre} lanza un hechizo poderoso de nivel {self.nivel}!")

class CriaturaMagica(SerMagico):
    def __init__(self, nombre, tipo, alineacion):
        super().__init__(nombre, "Criatura Mágica")
        self.tipo = tipo
        self.alineacion = alineacion

    def atacar(self):
        print(f"{self.nombre} lanza un ataque de {self.tipo}!")

class Mapa:
    def __init__(self):
        self.ubicaciones = ["Bosque Encantado", "Montaña de la Eternidad", "Lago de los Susurros", "Ciudad de Cristal", "Ruinas Perdidas"]
        self.criaturas_por_ubicacion = {
            "Bosque Encantado": [CriaturaMagica("Hada Brillante", "Luz", "Buena"), CriaturaMagica("Espectro Sombrío", "Sombra", "Mala")],
            "Montaña de la Eternidad": [CriaturaMagica("Dragón de Fuego", "Fuego", "Buena"), CriaturaMagica("Gólem de Roca", "Roca", "Mala")],
            "Lago de los Susurros": [CriaturaMagica("Sirena Guardiana", "Agua", "Buena"), CriaturaMagica("Kraken Dormido", "Oscuridad", "Mala")],
            "Ciudad de Cristal": [CriaturaMagica("Ángel Guardián", "Luz", "Buena"), CriaturaMagica("Demonio de Cristal", "Oscuridad", "Mala")],
            "Ruinas Perdidas": [CriaturaMagica("Fénix Ancestral", "Fuego", "Buena"), CriaturaMagica("Nigromante Olvidado", "Necromancia", "Mala")]
        }

    def mostrar_mapa(self):
        print("\nUbicaciones en el mapa:")
        for ubicacion in self.ubicaciones:
            print(f"- {ubicacion}")

class MundoMagico:
    def __init__(self):
        self.mapa = Mapa()
        self.seres_magicos = []
        self.ubicacion_actual = random.choice(self.mapa.ubicaciones)

    def agregar_ser_magico(self, ser):
        self.seres_magicos.append(ser)
        print(f"{ser.nombre} ha sido agregado al mundo mágico!")

    def ver_seres_magicos(self):
        print("\nSeres mágicos en tu ubicación actual:")
        print(f"Ubicación actual: {self.ubicacion_actual}")
        seres_en_ubicacion = [ser for ser in self.seres_magicos if isinstance(ser, Mago)]
        criaturas_en_ubicacion = self.mapa.criaturas_por_ubicacion.get(self.ubicacion_actual, [])
        
        if not seres_en_ubicacion and not criaturas_en_ubicacion:
            print("No hay seres mágicos aquí.")
            return

        for ser in seres_en_ubicacion:
            print(f"- {ser.nombre} (Mago)")
        for criatura in criaturas_en_ubicacion:
            print(f"- {criatura.nombre} ({criatura.alineacion})")

    def cambiar_ubicacion(self):
        if not any(isinstance(ser, Mago) for ser in self.seres_magicos):
            print("\nNo puedes cambiar de ubicación sin un mago. Crea uno primero!")
            return
        
        print("\nPuedes moverte a las siguientes ubicaciones:")
        for ubicacion in self.mapa.ubicaciones:
            print(f"- {ubicacion}")
        
        nueva_ubicacion = input("Elige una nueva ubicación: ")
        if nueva_ubicacion in self.mapa.ubicaciones:
            self.ubicacion_actual = nueva_ubicacion
            print(f"Te has movido a {self.ubicacion_actual}!")
        else:
            print("Ubicación no válida.")

def menu_mundo_magico():
    mundo = MundoMagico()
    while True:
        print(f"\n--- Menú del Mundo Mágico (Ubicación: {mundo.ubicacion_actual}) ---")
        print("1. Agregar un mago")
        print("2. Agregar una criatura mágica")
        print("3. Ver seres mágicos en tu ubicación")
        print("4. Comenzar batalla")
        print("5. Ver el mapa")
        print("6. Cambiar ubicación")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Introduce el nombre del mago: ")
            nivel = int(input("Introduce el nivel del mago: "))
            mago = Mago(nombre, nivel)
            mundo.agregar_ser_magico(mago)

        elif opcion == "2":
            nombre = input("Introduce el nombre de la criatura mágica: ")
            tipo = input("Introduce el tipo de ataque de la criatura: ")
            alineacion = input("Es buena o mala?: ")
            criatura = CriaturaMagica(nombre, tipo, alineacion)
            mundo.agregar_ser_magico(criatura)

        elif opcion == "3":
            mundo.ver_seres_magicos()

        elif opcion == "4":
            if not any(isinstance(ser, Mago) for ser in mundo.seres_magicos):
                print("\nNo puedes empezar una batalla sin un mago. Crea uno primero!")
            else:
                print("\n¡Comienza la batalla entre magos y criaturas mágicas!")
                for ser in mundo.seres_magicos:
                    if isinstance(ser, Mago):
                        ser.lanzar_hechizo()
                    elif isinstance(ser, CriaturaMagica):
                        ser.atacar()

        elif opcion == "5":
            mundo.mapa.mostrar_mapa()

        elif opcion == "6":
            mundo.cambiar_ubicacion()

        elif opcion == "7":
            print("¡Hasta la próxima, mago/a!")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

menu_mundo_magico()
