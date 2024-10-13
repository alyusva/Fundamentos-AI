class TicTacToe:
    def __init__(self):
        # Estado inicial del tablero (vacío)
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"  # El jugador X comienza primero

    def display_board(self):
        # Muestra el tablero actual con posiciones de 1 a 9
        for i, row in enumerate(self.board):
            print("|".join([cell if cell != "" else str(3 * i + j + 1) for j, cell in enumerate(row)]))
            if i < 2:
                print("-" * 5)

    def make_move(self, position):
        # Convierte la posición de 1-9 a coordenadas del tablero 3x3
        row, col = divmod(position - 1, 3)
        
        # Verifica si la celda está vacía antes de realizar el movimiento
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.display_board()
                print(f"¡El jugador {self.current_player} ha ganado!")
                return True
            elif self.is_draw():
                self.display_board()
                print("¡Es un empate!")
                return True
            else:
                # Cambia el turno al siguiente jugador
                self.current_player = "O" if self.current_player == "X" else "X"
                return False
        else:
            print("Movimiento inválido. La celda ya está ocupada.")
            return False

    def check_winner(self):
        # Revisa filas, columnas y diagonales
        for i in range(3):
            # Revisa filas y columnas
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
               all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        # Revisa diagonales
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def is_draw(self):
        # Verifica si hay un empate (tablero lleno sin ganador)
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

# Ejemplo de uso
game = TicTacToe()
game_over = False

while not game_over:
    game.display_board()
    try:
        move = int(input(f"Turno del jugador {game.current_player}. Introduce una posición (1-9): "))
        if move < 1 or move > 9:
            print("Posición inválida. Introduce un número entre 1 y 9.")
            continue
        game_over = game.make_move(move)
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número.")
