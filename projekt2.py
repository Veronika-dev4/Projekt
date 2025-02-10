"""
projekt2.py: druhý projekt do Engeto Online Python Akademie

author: Veronika Semeradova
email: semeradova.veronika@gmail.com
"""

print("Welcome to Tic Tac Toe")
print("=" * 40)
print("GAME RULES:\nEach player can place one mark (or stone)\nper turn on the 3x3 grid. The WINNER is\nwho succeeds in placing three of their\nmarks in a:\n* horizontal,\n* vertical or\n* diagonal row")
print("=" * 40)
print("Let's start the game")
print("-" * 40)

board = [" -", " -", " -",
         " -", " -", " -",
         " -", " -", " -"]

def print_board():
    print("+","-" * 3, "+","-" * 3, "+","-" * 3, "+")
    print("| " + board[0] + "  | " + board[1] + "  | " + board[2] + "  |")
    print("+","-" * 3, "+","-" * 3, "+","-" * 3, "+")
    print("| " + board[3] + "  | " + board[4] + "  | " + board[5] + "  |")
    print("+","-" * 3, "+","-" * 3, "+","-" * 3, "+")
    print("| " + board[6] + "  | " + board[7] + "  | " + board[8] + "  |")
    print("+","-" * 3, "+","-" * 3, "+","-" * 3, "+")

def take_turn(player):
    print("Player " + player, end= "")
    position = input(" | Please enter your move number: ")
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid input. Choose a position from 1-9: ")
    position = int(position) - 1
    while board[position] != " -":
        position = int(input("Position already taken. Choose a different position: ")) - 1
    board[position] = " " + str(player)
    print("=" * 40)
    print_board()
    print("=" * 40)

def check_game_over():
    if (board[0] == board[1] == board[2] != " -") or \
       (board[3] == board[4] == board[5] != " -") or \
       (board[6] == board[7] == board[8] != " -") or \
       (board[0] == board[3] == board[6] != " -") or \
       (board[1] == board[4] == board[7] != " -") or \
       (board[2] == board[5] == board[8] != " -") or \
       (board[0] == board[4] == board[8] != " -") or \
       (board[2] == board[4] == board[6] != " -"):
        return "win"
    elif " -" not in board:
        return "tie"
    else:
        return "play"
    
def play_game():
    print_board()
    current_player = "x"
    game_over = False
    while not game_over:
        take_turn(current_player)
        game_result = check_game_over()
        if game_result == "win":
            print("Congratulations, the player", current_player + " WON!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            current_player = "o" if current_player == "x" else "x"

play_game()