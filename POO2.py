class Tarea:
    def __init__(self, nombre, dificultad, duracion):
        self.nombre = nombre
        self.dificultad = dificultad
        self.duracion = duracion

    def mostrar_info(self):
        return f"Tarea: {self.nombre}, Dificultad: {self.dificultad}, Duración: {self.duracion} min"


class Robot:
    def __init__(self, nombre, modelo, nivel_bateria=100):
        self.nombre = nombre
        self.modelo = modelo
        self.nivel_bateria = nivel_bateria
        self.estado = "Disponible"

    def ejecutar_tarea(self, tarea):
        if self.nivel_bateria >= tarea.duracion:
            self.nivel_bateria -= tarea.duracion
            self.estado = "Ocupado"
            print(f"{self.nombre} está ejecutando la tarea '{tarea.nombre}'")
        else:
            print(f"{self.nombre} no tiene suficiente batería para esta tarea.")

    def recargar(self):
        self.nivel_bateria = 100
        self.estado = "Disponible"
        print(f"{self.nombre} ha sido recargado.")

    def reportar_estado(self):
        return f"{self.nombre} - Modelo: {self.modelo} - Batería: {self.nivel_bateria}% - Estado: {self.estado}"


class TallerDeRobots:
    def __init__(self):
        self.lista_robots = []
        self.lista_tareas = [
            Tarea("Limpieza de área", 3, 20),
            Tarea("Mantenimiento de equipos", 5, 30)
        ]

    def agregar_robot(self):
        nombre = input("Ingrese el nombre del robot: ")
        modelo = input("Ingrese el modelo del robot: ")
        robot = Robot(nombre, modelo)
        self.lista_robots.append(robot)
        print(f"Robot {nombre} agregado al taller.")

    def agregar_tarea(self):
        nombre = input("Ingrese el nombre de la tarea: ")
        dificultad = int(input("Ingrese la dificultad (1-10): "))
        duracion = int(input("Ingrese la duración en minutos: "))
        tarea = Tarea(nombre, dificultad, duracion)
        self.lista_tareas.append(tarea)
        print(f"Tarea '{nombre}' agregada al taller.")

    def mostrar_tareas_disponibles(self):
        if not self.lista_tareas:
            print("No hay tareas disponibles.")
        else:
            print("\nTareas disponibles:")
            for i, tarea in enumerate(self.lista_tareas):
                print(f"{i + 1}. {tarea.mostrar_info()}")

    def asignar_tarea(self):
        if not self.lista_robots or not self.lista_tareas:
            print("No hay robots o tareas disponibles.")
            return
        
        print("\nRobots disponibles:")
        for i, robot in enumerate(self.lista_robots):
            print(f"{i + 1}. {robot.reportar_estado()}")

        robot_index = int(input("Seleccione el número del robot: ")) - 1

        self.mostrar_tareas_disponibles()
        tarea_index = int(input("Seleccione el número de la tarea: ")) - 1

        robot = self.lista_robots[robot_index]
        tarea = self.lista_tareas[tarea_index]

        robot.ejecutar_tarea(tarea)

    def mostrar_estado_robots(self):
        if not self.lista_robots:
            print("No hay robots en el taller.")
            return
        
        for robot in self.lista_robots:
            print(robot.reportar_estado())


# Interacción con el usuario
taller = TallerDeRobots()

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar Robot")
    print("2. Agregar Tarea")
    print("3. Mostrar Tareas Disponibles")
    print("4. Asignar Tarea")
    print("5. Mostrar Estado de los Robots")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        taller.agregar_robot()
    elif opcion == "2":
        taller.agregar_tarea()
    elif opcion == "3":
        taller.mostrar_tareas_disponibles()
    elif opcion == "4":
        taller.asignar_tarea()
    elif opcion == "5":
        taller.mostrar_estado_robots()
    elif opcion == "6":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
