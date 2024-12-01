def print_board(board):
    """Display the current board state."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Check for a winner or a tie."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check for a tie
    for row in board:
        if " " in row:
            return None  # Game is still ongoing

    return "Tie"


def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn.")
        try:
            row, col = map(int, input(
                "Enter row and column (0, 1, or 2 separated by space): ").split())
            if board[row][col] != " ":
                print("Cell is already occupied! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter two numbers between 0 and 2.")
            continue

        # Make a move
        board[row][col] = current_player
        print_board(board)

        # Check for winner or tie
        result = check_winner(board)
        if result:
            if result == "Tie":
                print("It's a tie!")
            else:
                print(f"Player {result} wins!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()

if __name__ == "__main__":
    tic_tac_toe()
