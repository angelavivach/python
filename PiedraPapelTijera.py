import random

def jugar():
    opciones = ['piedra', 'papel', 'tijera']
    
    # Input del usuario
    jugador = input("Elige piedra, papel o tijera: ").lower()
    
    # Elección aleatoria de la computadora
    computadora = random.choice(opciones)
    
    # Mostrar las elecciones
    print(f"Tú elegiste: {jugador}")
    print(f"La computadora eligió: {computadora}")
    
    # Verificar las condiciones de empate
    if jugador == computadora:
        return "¡Es un empate!"
    
    # Verificar todas las posibilidades de que el jugador gane
    if es_ganador(jugador, computadora):
        return "¡Ganaste!"
    
    # Si no es empate y el jugador no ganó, entonces la computadora ganó
    return "¡Perdiste!"

def es_ganador(jugador, computadora):
    # Retorna True si el jugador gana
    # Piedra vence tijera (piedra > tijera)
    # Tijera vence papel (tijera > papel)
    # Papel vence piedra (papel > piedra)
    if (jugador == 'piedra' and computadora == 'tijera') or \
       (jugador == 'tijera' and computadora == 'papel') or \
       (jugador == 'papel' and computadora == 'piedra'):
        return True
    return False

# Iniciar el juego
print(jugar())
