# Tablero de Sudoku incompleto representado como una lista de listas
# El número 0 representa espacios vacíos que deben ser llenados
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Función para imprimir el tablero de Sudoku
def imprimir_tablero(tablero):
    for fila in range(len(tablero)):
        if fila % 3 == 0 and fila != 0:
            print("- - - - - - - - - - -")

        for columna in range(len(tablero[fila])):
            if columna % 3 == 0 and columna != 0:
                print(" | ", end="")

            if columna == 8:
                print(tablero[fila][columna])
            else:
                print(str(tablero[fila][columna]) + " ", end="")

# Función para encontrar una celda vacía en el tablero (marcada con 0)
def encontrar_vacio(tablero):
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna] == 0:
                return (fila, columna)  # Retorna una tupla (fila, columna)
    return None

# Función para verificar si un número es válido en la posición dada
def es_valido(tablero, numero, posicion):
    # Verificar fila
    for i in range(len(tablero[0])):
        if tablero[posicion[0]][i] == numero and posicion[1] != i:
            return False

    # Verificar columna
    for i in range(len(tablero)):
        if tablero[i][posicion[1]] == numero and posicion[0] != i:
            return False

    # Verificar subcuadrícula 3x3
    caja_x = posicion[1] // 3
    caja_y = posicion[0] // 3

    for i in range(caja_y * 3, caja_y * 3 + 3):
        for j in range(caja_x * 3, caja_x * 3 + 3):
            if tablero[i][j] == numero and (i, j) != posicion:
                return False

    return True

# Función para resolver el tablero usando backtracking
def resolver_sudoku(tablero):
    vacio = encontrar_vacio(tablero)
    if not vacio:
        return True  # El tablero está completo y resuelto
    else:
        fila, columna = vacio

    for numero in range(1, 10):
        if es_valido(tablero, numero, (fila, columna)):
            tablero[fila][columna] = numero  # Colocar número válido

            if resolver_sudoku(tablero):
                return True

            tablero[fila][columna] = 0  # Resetear la casilla si no es correcto

    return False

# Mostrar el tablero inicial
print("Tablero inicial:")
imprimir_tablero(tablero)
print("\nResolviendo...\n")

# Resolver el Sudoku
resolver_sudoku(tablero)

# Mostrar el tablero resuelto
print("Tablero resuelto:")
imprimir_tablero(tablero)
