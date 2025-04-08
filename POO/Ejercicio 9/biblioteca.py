class Fecha:
    def __init__(self, dia=1, mes=1, anio=1900):
        self.dia = dia
        self.mes = mes
        self.anio = anio
    
    def get_fecha_larga(self):
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                 "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        return f"{self.dia} de {meses[self.mes - 1]} de {self.anio}"

class Persona:
    def __init__(self, nombre="", apellido=""):
        self.nombre = nombre
        self.apellido = apellido
    
    def get_nombre_completo(self):
        return f"{self.apellido}, {self.nombre}"

class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, ciudad, pais, fecha_edicion):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.ciudad = ciudad
        self.pais = pais
        self.fecha_edicion = fecha_edicion
    
    def mostrar_info(self):
        print(f"Título: {self.titulo} {self.edicion}")
        print(f"Autor: {self.autor.get_nombre_completo()} ISBN: {self.isbn}")
        print(f"{self.editorial}, {self.ciudad} ({self.pais}), {self.fecha_edicion.get_fecha_larga()}")
        print(f"{self.paginas} páginas\n")

# Libro preexistente
libros = [
    Libro("Introduction to Java Programming", Persona("Y. Daniel", "Liang"), "0-13-031997-X", 784, "3a edición",
          "Prentice-Hall", "New Jersey", "USA", Fecha(16, 11, 2001))
]

def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    nombre_autor = input("Ingrese el nombre del autor: ")
    apellido_autor = input("Ingrese el apellido del autor: ")
    isbn = input("Ingrese el ISBN: ")
    paginas = int(input("Ingrese el número de páginas: "))
    edicion = input("Ingrese la edición: ")
    editorial = input("Ingrese la editorial: ")
    ciudad = input("Ingrese la ciudad: ")
    pais = input("Ingrese el país: ")
    dia = int(input("Ingrese el día de la fecha de edición: "))
    mes = int(input("Ingrese el mes de la fecha de edición (1-12): "))
    anio = int(input("Ingrese el año de la fecha de edición: "))
    
    nuevo_libro = Libro(titulo, Persona(nombre_autor, apellido_autor), isbn, paginas, edicion,
                        editorial, ciudad, pais, Fecha(dia, mes, anio))
    libros.append(nuevo_libro)
    print("\nLibro agregado con éxito!\n")

def mostrar_libros():
    if not libros:
        print("No hay libros registrados.\n")
    else:
        for libro in libros:
            libro.mostrar_info()

def menu():
    while True:
        print("---  MENÚ LIBRERÍA ---")
        print("1️  Ingresar datos de un libro")
        print("2️  Mostrar información de los libros")
        print("3️  Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            mostrar_libros()
        elif opcion == "3":
            print("Saliendo del programa...\n")
            break
        else:
            print("Opción no válida, intenta nuevamente.\n")

# Ejecutar menú
menu()
