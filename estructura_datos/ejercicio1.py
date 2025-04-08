def mayor_menor():
    num1 = float(input("Ingrese el primer número: "))
    
    while True:
        num2 = float(input("Ingrese el segundo número (debe ser diferente al primero): "))
        if num2 != num1:
            break
        print("El segundo número debe ser diferente al primero.")
    
    if num1 > num2:
        print(f"El primer número es mayor: {num1}")
        print(f"El segundo número es menor: {num2}")
    else:
        print(f"El segundo número es mayor: {num2}")
        print(f"El primer número es menor: {num1}")

# Ejecutar la función
mayor_menor()
