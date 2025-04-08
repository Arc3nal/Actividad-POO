class Cancion:
    def __init__(self, titulo="", autor=""):
        """Constructor: permite inicializar con título y autor o dejar valores vacíos."""
        self.titulo = titulo
        self.autor = autor

    # Métodos para obtener valores (Getters)
    def dameTitulo(self):
        """Devuelve el título de la canción."""
        return self.titulo

    def dameAutor(self):
        """Devuelve el autor de la canción."""
        return self.autor

    # Métodos para establecer valores (Setters)
    def ponTitulo(self, titulo):
        """Establece el título de la canción."""
        self.titulo = titulo

    def ponAutor(self, autor):
        """Establece el autor de la canción."""
        self.autor = autor

    def mostrarInfo(self):
        """Muestra la información de la canción."""
        print(f"\n Canción: {self.titulo} |  Autor: {self.autor}")


# Menú interactivo
def menu():
    print("\n--- MENÚ CANCIÓN ---")
    print("1. Crear nueva canción")
    print("2. Mostrar información de la canción")
    print("3. Modificar título")
    print("4. Modificar autor")
    print("5. Salir")
    return input("Elige una opción: ")


# Programa principal
if __name__ == "__main__":
    cancion = None  # Inicialmente no hay canción registrada

    while True:
        opcion = menu()

        if opcion == "1":
            # Crear una nueva canción
            titulo = input("Introduce el título de la canción: ")
            autor = input("Introduce el autor de la canción: ")
            cancion = Cancion(titulo, autor)
            print(" Canción creada con éxito.")

        elif opcion == "2":
            if cancion:
                cancion.mostrarInfo()
            else:
                print(" No hay ninguna canción registrada.")

        elif opcion == "3":
            if cancion:
                nuevo_titulo = input("Nuevo título de la canción: ")
                cancion.ponTitulo(nuevo_titulo)
                print(" Título actualizado.")
            else:
                print(" No hay ninguna canción registrada.")

        elif opcion == "4":
            if cancion:
                nuevo_autor = input("Nuevo autor de la canción: ")
                cancion.ponAutor(nuevo_autor)
                print(" Autor actualizado.")
            else:
                print(" No hay ninguna canción registrada.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print(" Opción inválida, intenta de nuevo.")
