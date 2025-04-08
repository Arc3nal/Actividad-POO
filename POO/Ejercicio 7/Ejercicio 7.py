class Empleado:
    def __init__(self, nif="", sueldo_base=0, pago_hora_extra=0, horas_extra=0, irpf=0, casado=False, num_hijos=0):
        """Constructor: permite proporcionar solo el NIF, los demás valores tienen un valor por defecto."""
        self.nif = nif
        self.sueldo_base = sueldo_base
        self.pago_hora_extra = pago_hora_extra
        self.horas_extra = horas_extra
        self.irpf = irpf
        self.casado = casado
        self.num_hijos = num_hijos

    # Métodos de acceso (Getters)
    def get_nif(self):
        return self.nif

    def get_sueldo_base(self):
        return self.sueldo_base

    def get_pago_hora_extra(self):
        return self.pago_hora_extra

    def get_horas_extra(self):
        return self.horas_extra

    def get_irpf(self):
        return self.irpf

    def get_casado(self):
        return self.casado

    def get_num_hijos(self):
        return self.num_hijos

    # Métodos de modificación (Setters)
    def set_nif(self, nif):
        self.nif = nif

    def set_sueldo_base(self, sueldo_base):
        self.sueldo_base = sueldo_base

    def set_pago_hora_extra(self, pago_hora_extra):
        self.pago_hora_extra = pago_hora_extra

    def set_horas_extra(self, horas_extra):
        self.horas_extra = horas_extra

    def set_irpf(self, irpf):
        self.irpf = irpf

    def set_casado(self, casado):
        self.casado = casado

    def set_num_hijos(self, num_hijos):
        self.num_hijos = num_hijos

    def complemento_horas_extra(self):
        """Calcula el complemento por horas extra realizadas."""
        return self.horas_extra * self.pago_hora_extra

    def sueldo_bruto(self):
        """Calcula y devuelve el sueldo bruto."""
        return self.sueldo_base + self.complemento_horas_extra()

    def retencion_irpf(self):
        """Calcula y devuelve la retención del IRPF con las reducciones correspondientes."""
        irpf_aplicado = self.irpf - (2 if self.casado else 0) - self.num_hijos
        if irpf_aplicado < 0:
            irpf_aplicado = 0  # Evita porcentajes negativos
        return (irpf_aplicado / 100) * self.sueldo_bruto()

    def sueldo_neto(self):
        """Calcula y devuelve el sueldo neto después de aplicar el IRPF."""
        return self.sueldo_bruto() - self.retencion_irpf()

    def println(self):
        """Muestra la información básica del empleado."""
        estado_civil = "Casado" if self.casado else "Soltero"
        print(f"\nEmpleado: {self.nif} | Estado: {estado_civil} | Hijos: {self.num_hijos}")

    def printAll(self):
        """Muestra toda la información del empleado."""
        self.println()
        print(f"Sueldo Base: {self.sueldo_base:.2f} €")
        print(f"Complemento Horas Extra: {self.complemento_horas_extra():.2f} €")
        print(f"Sueldo Bruto: {self.sueldo_bruto():.2f} €")
        print(f"Retención IRPF: {self.retencion_irpf():.2f} €")
        print(f"Sueldo Neto: {self.sueldo_neto():.2f} €\n")

    def copia(self):
        """Devuelve una copia del objeto actual."""
        return Empleado(self.nif, self.sueldo_base, self.pago_hora_extra, self.horas_extra, 
                        self.irpf, self.casado, self.num_hijos)


# Menú interactivo
def menu():
    print("\n--- MENÚ EMPLEADO ---")
    print("1. Crear nuevo empleado")
    print("2. Mostrar información básica")
    print("3. Mostrar toda la información")
    print("4. Calcular sueldo bruto")
    print("5. Calcular retención de IRPF")
    print("6. Calcular sueldo neto")
    print("7. Clonar empleado")
    print("8. Salir")
    return input("Elige una opción: ")


# Programa principal
if __name__ == "__main__":
    empleado = None  # Inicialmente no hay empleado registrado

    while True:
        opcion = menu()

        if opcion == "1":
            # Crear un nuevo empleado
            nif = input("Introduce el NIF: ")
            sueldo_base = float(input("Sueldo base (€): "))
            pago_hora_extra = float(input("Pago por hora extra (€): "))
            horas_extra = int(input("Horas extra realizadas: "))
            irpf = float(input("Tipo de IRPF (%): "))
            casado = input("¿Está casado? (s/n): ").strip().lower() == "s"
            num_hijos = int(input("Número de hijos: "))

            empleado = Empleado(nif, sueldo_base, pago_hora_extra, horas_extra, irpf, casado, num_hijos)
            print("✅ Empleado creado con éxito.")

        elif opcion == "2":
            if empleado:
                empleado.println()
            else:
                print("⚠️ No hay ningún empleado registrado.")

        elif opcion == "3":
            if empleado:
                empleado.printAll()
            else:
                print("⚠️ No hay ningún empleado registrado.")

        elif opcion == "4":
            if empleado:
                print(f"Sueldo Bruto: {empleado.sueldo_bruto():.2f} €")
            else:
                print("⚠️ No hay ningún empleado registrado.")

        elif opcion == "5":
            if empleado:
                print(f"Retención IRPF: {empleado.retencion_irpf():.2f} €")
            else:
                print("⚠️ No hay ningún empleado registrado.")

        elif opcion == "6":
            if empleado:
                print(f"Sueldo Neto: {empleado.sueldo_neto():.2f} €")
            else:
                print("⚠️ No hay ningún empleado registrado.")

        elif opcion == "7":
            if empleado:
                clon = empleado.copia()
                print("\n✅ Empleado clonado con éxito:")
                clon.printAll()
            else:
                print("⚠️ No hay ningún empleado registrado para clonar.")

        elif opcion == "8":
            print("Saliendo del programa...")
            break

        else:
            print("⚠️ Opción inválida, intenta de nuevo.")
