# Funciones para las operaciones básicas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# Función principal de la calculadora
def calculadora():
    print("Bienvenido a la calculadora")

    while True:
        print("\nSelecciona la operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        # Pedir al usuario la operación a realizar
        eleccion = input("Elige una opción (1/2/3/4/5): ")

        if eleccion == '5':
            print("Saliendo...")
            break

        if eleccion not in ['1', '2', '3', '4']:
            print("Opción inválida. Inténtalo de nuevo.")
            continue

        # Pedir los números al usuario
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Por favor ingresa un número válido.")
            continue

        # Realizar la operación seleccionada
        if eleccion == '1':
            print(f"El resultado de {num1} + {num2} es: {sumar(num1, num2)}")
        elif eleccion == '2':
            print(f"El resultado de {num1} - {num2} es: {restar(num1, num2)}")
        elif eleccion == '3':
            print(f"El resultado de {num1} * {num2} es: {multiplicar(num1, num2)}")
        elif eleccion == '4':
            resultado = dividir(num1, num2)
            print(f"El resultado de {num1} / {num2} es: {resultado}")

# Ejecutar la calculadora en consola
calculadora()

