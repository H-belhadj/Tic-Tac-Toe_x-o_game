# Tic-Tac-Toe Game

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print("-------------")
    for i in range(3):
        print("|", board[i*3], "|", board[i*3 + 1], "|", board[i*3 + 2], "|")
        print("-------------")

# Function to check for a win
def check_win():
    # Check rows
    for i in range(3):
        if board[i*3] == board[i*3 + 1] == board[i*3 + 2] != " ":
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    return False

# Function to play the game
def play_game():
    player1 = "X"
    player2 = "O"
    current_player = player1
    while True:
        print_board()
        move = input("Player " + current_player + ", enter your move (1-9): ")
        move = int(move) - 1

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move. Try again.")
            continue

        board[move] = current_player

        if check_win():
            print_board()
            print("Player", current_player, "wins!")
            break

        if " " not in board:
            print_board()
            print("It's a draw!")
            break

        current_player = player2 if current_player == player1 else player1

# Start the game
play_game()
