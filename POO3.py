class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_info(self):
        return f"Mascota: {self.nombre}, Especie: {self.especie}, Edad: {self.edad} años"


class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad}"


class TiendaMascotas:
    def __init__(self):
        self.mascotas = [
            Mascota("Luna", "Perro", 2),
            Mascota("Milo", "Gato", 1)
        ]
        self.productos = [
            Producto("Croquetas", 20, 10),
            Producto("Juguete", 15, 5)
        ]

    def mostrar_mascotas(self):
        if not self.mascotas:
            print("No hay mascotas disponibles para adopción.")
        else:
            print("\nMascotas disponibles:")
            for i, mascota in enumerate(self.mascotas):
                print(f"{i + 1}. {mascota.mostrar_info()}")

    def adoptar_mascota(self):
        self.mostrar_mascotas()
        if self.mascotas:
            try:
                indice = int(input("Seleccione el número de la mascota que desea adoptar: ")) - 1
                if 0 <= indice < len(self.mascotas):
                    mascota_adoptada = self.mascotas.pop(indice)
                    print(f"Felicidades, ha adoptado a {mascota_adoptada.nombre}!")
                else:
                    print("Selección no válida.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos disponibles.")
        else:
            print("\nProductos disponibles:")
            for i, producto in enumerate(self.productos):
                print(f"{i + 1}. {producto.mostrar_info()}")

    def comprar_producto(self):
        self.mostrar_productos()
        if self.productos:
            try:
                indice = int(input("Seleccione el número del producto que desea comprar: ")) - 1
                if 0 <= indice < len(self.productos):
                    producto = self.productos[indice]
                    cantidad = int(input(f"¿Cuántos '{producto.nombre}' desea comprar? "))
                    if cantidad > 0 and cantidad <= producto.cantidad:
                        producto.cantidad -= cantidad
                        print(f"Has comprado {cantidad} {producto.nombre}(s).")
                    else:
                        print("Cantidad no válida o insuficiente en stock.")
                else:
                    print("Selección no válida.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def agregar_mascota(self):
        nombre = input("Ingrese el nombre de la nueva mascota: ")
        especie = input("Ingrese la especie de la mascota: ")
        try:
            edad = int(input("Ingrese la edad de la mascota: "))
            nueva_mascota = Mascota(nombre, especie, edad)
            self.mascotas.append(nueva_mascota)
            print(f"Mascota '{nombre}' agregada a la tienda.")
        except ValueError:
            print("Por favor, ingrese una edad válida.")

    def agregar_producto(self):
        nombre = input("Ingrese el nombre del nuevo producto: ")
        try:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad en stock: "))
            nuevo_producto = Producto(nombre, precio, cantidad)
            self.productos.append(nuevo_producto)
            print(f"Producto '{nombre}' agregado a la tienda.")
        except ValueError:
            print("Por favor, ingrese valores válidos para precio y cantidad.")


tiendas = TiendaMascotas()

while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar Mascotas Disponibles")
    print("2. Adoptar Mascota")
    print("3. Mostrar Productos Disponibles")
    print("4. Comprar Producto")
    print("5. Agregar Nueva Mascota")
    print("6. Agregar Nuevo Producto")
    print("7. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        tiendas.mostrar_mascotas()
    elif opcion == "2":
        tiendas.adoptar_mascota()
    elif opcion == "3":
        tiendas.mostrar_productos()
    elif opcion == "4":
        tiendas.comprar_producto()
    elif opcion == "5":
        tiendas.agregar_mascota()
    elif opcion == "6":
        tiendas.agregar_producto()
    elif opcion == "7":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
