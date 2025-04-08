import Persona
import Fecha

class Libro:
    def __init__(self, titulo="", autor=None, isbn="", paginas=0, edicion="", editorial="", ciudad="", pais="", fecha_edicion=None):
        """Constructor de Libro con valores predeterminados."""
        self.titulo = titulo
        self.autor = autor if autor is not None else Persona()
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.ciudad = ciudad
        self.pais = pais
        self.fecha_edicion = fecha_edicion if fecha_edicion is not None else Fecha()

    # Getters
    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_isbn(self):
        return self.isbn

    def get_paginas(self):
        return self.paginas

    def get_edicion(self):
        return self.edicion

    def get_editorial(self):
        return self.editorial

    def get_ciudad(self):
        return self.ciudad

    def get_pais(self):
        return self.pais

    def get_fecha_edicion(self):
        return self.fecha_edicion

    # Setters
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_paginas(self, paginas):
        self.paginas = paginas

    def set_edicion(self, edicion):
        self.edicion = edicion

    def set_editorial(self, editorial):
        self.editorial = editorial

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad

    def set_pais(self, pais):
        self.pais = pais

    def set_fecha_edicion(self, fecha_edicion):
        self.fecha_edicion = fecha_edicion

    def leer_info(self):
        """Solicita al usuario la información del libro."""
        self.titulo = input("Ingrese el título del libro: ")
        nombre_autor = input("Ingrese el nombre del autor: ")
        apellido_autor = input("Ingrese el apellido del autor: ")
        self.autor = Persona(nombre_autor, apellido_autor)
        self.isbn = input("Ingrese el ISBN: ")
        self.paginas = int(input("Ingrese el número de páginas: "))
        self.edicion = input("Ingrese la edición: ")
        self.editorial = input("Ingrese la editorial: ")
        self.ciudad = input("Ingrese la ciudad: ")
        self.pais = input("Ingrese el país: ")
        dia = int(input("Ingrese el día de la fecha de edición: "))
        mes = int(input("Ingrese el mes de la fecha de edición (1-12): "))
        anio = int(input("Ingrese el año de la fecha de edición: "))
        self.fecha_edicion = Fecha(dia, mes, anio)

    def mostrar_info(self):
        """Muestra la información del libro en el formato indicado."""
        print(f"Título: {self.titulo} {self.edicion}")
        print(f"Autor: {self.autor.get_nombre_completo()} ISBN: {self.isbn}")
        print(f"{self.editorial}, {self.ciudad} ({self.pais}), {self.fecha_edicion.get_fecha_larga()}")
        print(f"{self.paginas} páginas")


# Ejemplo de uso
if __name__ == "__main__":
    autor1 = Persona.Persona("Y. Daniel", "Liang")
    fecha1 = Fecha.Fecha(16, 11, 2001)
    libro1 = Libro("Introduction to Java Programming", autor1, "0-13-031997-X", 784, "3a edición",
                   "Prentice-Hall", "New Jersey", "USA", fecha1)

    libro1.mostrar_info()
