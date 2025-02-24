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
    def __init__(self, nombre, tipo, ubicacion):
        super().__init__(nombre, "Criatura Mágica")
        self.tipo = tipo
        self.ubicacion = ubicacion

    def atacar(self):
        print(f"{self.nombre} lanza un ataque de {self.tipo}!")

class MundoMagico:
    def __init__(self):
        self.seres_magicos = []
        self.ubicaciones = [
            "Bosque Encantado", "Montaña de la Eternidad",
            "Lago de los Susurros", "Ciudad de Cristal", "Ruinas Perdidas"
        ]
        self.ubicacion_actual = random.choice(self.ubicaciones)
        self.criaturas_por_ubicacion = {
            "Bosque Encantado": [CriaturaMagica("Hada Brillante", "Luz", "Bosque Encantado"), CriaturaMagica("Espectro Sombrío", "Sombra", "Bosque Encantado")],
            "Montaña de la Eternidad": [CriaturaMagica("Dragón de Fuego", "Fuego", "Montaña de la Eternidad"), CriaturaMagica("Gólem de Roca", "Roca", "Montaña de la Eternidad")],
            "Lago de los Susurros": [CriaturaMagica("Sirena Guardiana", "Agua", "Lago de los Susurros"), CriaturaMagica("Kraken Dormido", "Oscuridad", "Lago de los Susurros")],
            "Ciudad de Cristal": [CriaturaMagica("Ángel Guardián", "Luz", "Ciudad de Cristal"), CriaturaMagica("Demonio de Cristal", "Oscuridad", "Ciudad de Cristal")],
            "Ruinas Perdidas": [CriaturaMagica("Fénix Ancestral", "Fuego", "Ruinas Perdidas"), CriaturaMagica("Nigromante Olvidado", "Necromancia", "Ruinas Perdidas")]
        }
    
    def agregar_ser_magico(self, ser):
        self.seres_magicos.append(ser)
        print(f"{ser.nombre} ha sido agregado al mundo mágico!")

    def ver_seres_magicos(self):
        print(f"Seres mágicos en {self.ubicacion_actual}:")
        for ser in self.seres_magicos:
            if isinstance(ser, CriaturaMagica) and ser.ubicacion == self.ubicacion_actual:
                print(f"{ser.nombre} - {ser.tipo}")
        for criatura in self.criaturas_por_ubicacion.get(self.ubicacion_actual, []):
            print(f"{criatura.nombre} - {criatura.tipo}")

    def ver_mapa(self):
        print("Ubicaciones en el mundo mágico:")
        for ubicacion in self.ubicaciones:
            print(f"- {ubicacion}")

    def cambiar_ubicacion(self, tiene_mago):
        if not tiene_mago:
            print("Debes tener un mago creado para cambiar de ubicación.")
            return
        print("Ubicaciones disponibles:")
        for i, ubicacion in enumerate(self.ubicaciones, 1):
            print(f"{i}. {ubicacion}")
        eleccion = int(input("Elige el número de la nueva ubicación: "))
        if 1 <= eleccion <= len(self.ubicaciones):
            self.ubicacion_actual = self.ubicaciones[eleccion - 1]
            print(f"Has cambiado de ubicación a {self.ubicacion_actual}!")
        else:
            print("Opción inválida.")

def menu_mundo_magico():
    mundo = MundoMagico()
    tiene_mago = False

    while True:
        print(f"\n--- Menú del Mundo Mágico (Ubicación actual: {mundo.ubicacion_actual}) ---")
        print("1. Agregar un mago")
        print("2. Agregar una criatura mágica")
        print("3. Ver seres mágicos en la ubicación actual")
        print("4. Ver mapa")
        print("5. Cambiar ubicación")
        print("6. Comenzar batalla")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Introduce el nombre del mago: ")
            nivel = int(input("Introduce el nivel del mago: "))
            mago = Mago(nombre, nivel)
            mundo.agregar_ser_magico(mago)
            tiene_mago = True

        elif opcion == "2":
            nombre = input("Introduce el nombre de la criatura mágica: ")
            tipo = input("Introduce el tipo de ataque de la criatura (por ejemplo, fuego, hielo): ")
            alineacion = input("¿Es una criatura 'Buena' o 'Mala'?: ").capitalize()

            if alineacion not in ["Buena", "Mala"]:
                print("Opción inválida, se asignará como 'Neutral'.")
                alineacion = "Neutral"

            criatura = CriaturaMagica(nombre, tipo, mundo.ubicacion_actual)
            mundo.agregar_ser_magico(criatura)
            print(f"La criatura {nombre} ({alineacion}) ha sido agregada a {mundo.ubicacion_actual}!")


        elif opcion == "3":
            mundo.ver_seres_magicos()

        elif opcion == "4":
            mundo.ver_mapa()

        elif opcion == "5":
            if not tiene_mago:
                print("Debes tener un mago para iniciar la batalla. Creemos uno primero.")
                nombre = input("Introduce el nombre del mago: ")
                nivel = int(input("Introduce el nivel del mago: "))
                mago = Mago(nombre, nivel)
                mundo.agregar_ser_magico(mago)
                tiene_mago = True
            mundo.cambiar_ubicacion(tiene_mago)

        elif opcion == "6":
            if not tiene_mago:
                print("Debes tener un mago para iniciar la batalla. Creemos uno primero.")
                nombre = input("Introduce el nombre del mago: ")
                nivel = int(input("Introduce el nivel del mago: "))
                mago = Mago(nombre, nivel)
                mundo.agregar_ser_magico(mago)
                tiene_mago = True

            criaturas_en_ubicacion = [ser for ser in mundo.seres_magicos if isinstance(ser, CriaturaMagica) and ser.ubicacion == mundo.ubicacion_actual]

            criaturas_mapa = mundo.criaturas_por_ubicacion.get(mundo.ubicacion_actual, [])


            todas_las_criaturas = criaturas_en_ubicacion + criaturas_mapa

            if not todas_las_criaturas:
                print("No hay criaturas mágicas en esta ubicación para combatir.")
            else:
                print("¡Comienza la batalla! Estas son las criaturas en esta ubicación:")
                for i, criatura in enumerate(todas_las_criaturas, 1):
                    print(f"{i}. {criatura.nombre} ({criatura.tipo})")  # Se elimina {criatura.alineacion}

                eleccion = int(input("Elige el número de la criatura a la que quieres atacar: "))

                if 1 <= eleccion <= len(todas_las_criaturas):
                    objetivo = todas_las_criaturas[eleccion - 1]
                    print(f"¡Atacas a {objetivo.nombre} con magia!")
                    objetivo.atacar()
                else:
                    print("Opción inválida.")


        elif opcion == "7":
            print("¡Hasta la próxima, mago/a!")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

menu_mundo_magico()
