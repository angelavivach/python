import random
import string

def generar_contrasena(longitud):
    # Definir los caracteres posibles para la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Usamos un bucle for para generar una contraseña de la longitud especificada
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def generar_contrasenas(numero_contrasenas, longitud_contrasena):
    # Generar una lista de contraseñas
    contrasenas = [generar_contrasena(longitud_contrasena) for _ in range(numero_contrasenas)]
    return contrasenas

def main():
    print("Generador de contraseñas aleatorias")
    
    # Solicitar al usuario el número de contraseñas y su longitud
    while True:
        try:
            numero_contrasenas = int(input("¿Cuántas contraseñas te gustaría generar? "))
            longitud_contrasena = int(input("¿Cuál debe ser la longitud de cada contraseña? "))
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    # Generar las contraseñas
    contrasenas = generar_contrasenas(numero_contrasenas, longitud_contrasena)
    
    # Mostrar las contraseñas generadas
    print("\nContraseñas generadas:")
    for i, contrasena in enumerate(contrasenas, 1):
        print(f"{i}. {contrasena}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
