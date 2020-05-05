# Tic tac toe board game
# The user enters the positions at which he wants the move to be made
# Digant Kumar

# Defining the board positions
board = {'top-left':" ", "top-middle": " ", "top-right":" ",
         'middle-left':" ", "middle-middle": " ", "middle-right":" ",
         'bottom-left':" ", "bottom-middle": " ", "bottom-right":" "}

# Pretty printing the board
def board_printing(board):
    print(board['top-left'] + "|" + board['top-middle'] + "|" + board['top-right'])
    print("_ _ _")
    print(board['middle-left'] + "|" + board['middle-middle'] + "|" + board['middle-right'])
    print("_ _ _ ")
    print(board['bottom-left'] + "|" + board['bottom-middle'] + "|" + board['bottom-right'])
    return ""

# Since the first move in tic tac toe is X
move = "X"
move_count = 0
for i in range(9):
    print(board_printing(board))
    turn = input("Where do you wanna move: ")
    while turn not in board:   # If the user enters a position which does not exist, this loop will keep on asking the user to enter the correct position
        print("The given position does not exit, please enter a position ")
        print()
        turn = input("Where do you wanna move: ")

    if board[turn] == " ":
        board[turn] = move
        move_count += 1
    else:
        print("Position has already been filled")       # Not allowing the previously filled position to be replaced
        continue
    if move == "X":
        move = "O"
    else:
        move = "X"

    # Matching all the possible tic tac toe patterns from diagonals, to across the side and from top to bottom etc.
    if board["top-left"] == board["top-middle"] == board["top-right"] != " " or board["middle-left"] == board["middle-middle"] == board["middle-right"] != " " or \
            board["bottom-left"] == board["bottom-middle"] == board["bottom-right"] != " " or board["top-left"] == board["middle-middle"] == board["bottom-right"] != " " or \
            board["top-right"] == board["middle-middle"] == board["bottom-left"] != " " or board["top-left"] == board["middle-left"] == board["bottom-left"] != " " or \
            board["top-middle"] == board["middle-middle"] == board["bottom-middle"] != " " or board["top-right"] == board["middle-right"] == board["bottom-right"] != " ":
            board_printing(board)
            print()
            print("Game over")
            break

    if move_count == 9:      # As the tic tac toe board can only have 9 moves, if all the moves are used, it is declared a tie
        print()
        print("Game over! The result was a tie")
        break

board_printing(board)