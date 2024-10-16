import random

def get_random_word():
    # Lista de palabras para el juego
    words = ["python", "diccionario", "modulo", "cadena", "programacion", "ahorcado", "computadora"]
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    # Función para mostrar el estado actual de la palabra (letras adivinadas y guiones bajos)
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word_to_guess = get_random_word()  # Seleccionar palabra aleatoria
    guessed_letters = []  # Lista para almacenar las letras que ya han sido adivinadas
    incorrect_guesses = []  # Lista para las letras incorrectas
    attempts = 6  # Intentos máximos
    
    print("¡Bienvenido al juego de Ahorcado!")
    
    # Ciclo principal del juego
    while attempts > 0:
        print("\nPalabra actual: ", display_word(word_to_guess, guessed_letters))
        print(f"Letras incorrectas: {', '.join(incorrect_guesses)}")
        print(f"Intentos restantes: {attempts}")
        
        guess = input("Adivina una letra: ").lower()
        
        # Validación de la entrada
        if len(guess) != 1 or not guess.isalpha():
            print("Por favor, ingresa una sola letra válida.")
            continue
        
        # Verificar si la letra ya fue adivinada
        if guess in guessed_letters or guess in incorrect_guesses:
            print("Ya has adivinado esa letra. Intenta otra.")
            continue
        
        # Verificar si la letra está en la palabra
        if guess in word_to_guess:
            print(f"¡Correcto! La letra '{guess}' está en la palabra.")
            guessed_letters.append(guess)
        else:
            print(f"Lo siento, la letra '{guess}' no está en la palabra.")
            incorrect_guesses.append(guess)
            attempts -= 1
        
        # Verificar si se ha adivinado toda la palabra
        if set(guessed_letters) == set(word_to_guess):
            print(f"¡Felicidades! Has adivinado la palabra: {word_to_guess}")
            break
    else:
        print(f"Te has quedado sin intentos. La palabra era: {word_to_guess}")

# Ejecutar el juego
hangman()
