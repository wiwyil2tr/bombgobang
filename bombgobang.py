# Bomb Gobang
import random
import time

# Define the board size
board_size = int(input("Enter the board size: (example:15) "))

# Create an empty board
board = [[" " for _ in range(board_size)] for _ in range(board_size)]

# Get the number of bombs and the time limit from the player
print("Welcome to Bomb Gobang!")
print("Game Rules: There are a total of a number of bombs in the game. Both players must dismantle them all within a number of minutes, otherwise the bomb will explode, and both players will lose. At the beginning, the player should input the bombs number and the time limit. A bomb will be dismantled every time a five-in-a-row is formed. The winner is the one who dismantles the most bombs. ")
print("The goal is to dismantle as many bombs as possible by forming five-in-a-row.")
print("The bombs are hidden and will be revealed when dismantled.")
bomb_num = int(input("Enter the number of bombs: "))
time_limit = int(input("Enter the time limit in minutes: "))
print("You have", time_limit, "minutes to dismantle all", bomb_num, "bombs.")
print("Good luck!")

# Define a global variable to store the remaining bombs
global remaining_bombs
remaining_bombs = bomb_num

# Define the symbols for the players
symbols = ["X", "O"]

# Define the scores for the players
scores = [0, 0]

# Define a function to print the board
def print_board():
    # Print the column numbers
    print("  ", end="")
    for i in range(board_size):
        print(f"{i:2d}", end=" ")
    print()

    # Print the row numbers and the board cells
    for i in range(board_size):
        print(f"{i:2d} ", end="")
        for j in range(board_size):
            print(f"{board[i][j]} ", end=" ")
        print()

    # Print the scores and the remaining bombs
    print(f"Score: X - {scores[0]}, O - {scores[1]}")
    print(f"Bombs left: {remaining_bombs}")

# Define a function to check if a move is valid
def is_valid_move(x, y):
    # Check if the coordinates are within the board range
    if x < 0 or x >= board_size or y < 0 or y >= board_size:
        return False

    # Check if the cell is empty
    if board[x][y] != " ":
        return False

    # The move is valid
    return True

# Define a function to check if a player has formed a five-in-a-row
def has_five_in_a_row(symbol):
    # Check horizontal lines
    for i in range(board_size):
        count = 0
        for j in range(board_size):
            if board[i][j] == symbol:
                count += 1
            else:
                count = 0
            if count == 5:
                return True

    # Check vertical lines
    for j in range(board_size):
        count = 0
        for i in range(board_size):
            if board[i][j] == symbol:
                count += 1
            else:
                count = 0
            if count == 5:
                return True

    # Check diagonal lines (top-left to bottom-right)
    for k in range(2 * board_size - 1):
        count = 0
        if k < board_size:
            i = k
            j = 0
        else:
            i = board_size - 1
            j = k - board_size + 1
        while i >= 0 and j < board_size:
            if board[i][j] == symbol:
                count += 1
            else:
                count = 0
            if count == 5:
                return True
            i -= 1
            j += 1

    # Check diagonal lines (bottom-left to top-right)
    for k in range(2 * board_size - 1):
        count = 0
        if k < board_size:
            i = board_size - k - 1
            j = 0
        else:
            i = 0
            j = k - board_size + 1
        while i < board_size and j < board_size:
            if board[i][j] == symbol:
                count += 1
            else:
                count = 0
            if count == 5:
                return True
            i += 1
            j += 1

    # No five-in-a-row found
    return False

# Define a function to check if a player has dismantled a bomb
def has_dismantled_bomb():
    # Declare the global variable for remaining bombs
    global remaining_bombs

    # Check if there are any remaining bombs
    if remaining_bombs == 0:
        return False

    # Decrease the remaining bombs by one
    remaining_bombs -= 1

    # The bomb is dismantled
    return True

# Define a function to check if the game is over (either time is up or all bombs are dismantled)
def is_game_over():
    # Check if the time is up
    if time.time() - start_time > time_limit * 60:
        return True

    # Check if all bombs are dismantled
    if remaining_bombs == 0:
        return True

    # The game is not over
    return False

# Define a function to declare the winner (or a tie)
def declare_winner():
    
    # Print the final board
    print_board()

    # Compare the scores
    if remaining_bombs != 0:
        print("Time Up! Bomb Exploded! You All Lost!")
    elif scores[0] > scores[1]:
        print("X Wins! Congratulations!")
    elif scores[0] < scores[1]:
        print("O Wins! Congratulations!")
    else:
        print("It's a tie!")

# Define a function to display the remaining time
def display_time():
    # Calculate the elapsed time in seconds
    elapsed_time = time.time() - start_time

    # Calculate the remaining time in minutes and seconds
    remaining_time = time_limit * 60 - elapsed_time
    minutes = int(remaining_time // 60)
    seconds = int(remaining_time % 60)

    # Print the remaining time
    print(f"Time left: {minutes}:{seconds:02d}")

# Start the game
# Record the start time
start_time = time.time()

# Set the current player index
current_player = 0

# Loop until the game is over
while not is_game_over():
    # Print the board
    print_board()

    # Display the remaining time
    display_time()

    # Get the current player symbol
    symbol = symbols[current_player]

    # Get the move from the current player
    print(symbol, "'s turn. Enter your move (row column):")
    x, y = map(int, input().split())

    # Validate the move
    while not is_valid_move(x, y):
        print("Invalid move. Try again.")
        x, y = map(int, input().split())

    # Make the move
    board[x][y] = symbol

    # Check if the current player has formed a five-in-a-row
    if has_five_in_a_row(symbol):
        print(symbol, "has formed a five-in-a-row!")

        # Dismantle a random bomb and update the score
        if has_dismantled_bomb():
            print(symbol, "has dismantled a bomb!")
            scores[current_player] += 1

        else:
            print("No more bombs left!")

    # Switch to the next player
    current_player = 1 - current_player

# Declare the winner (or a tie)
declare_winner()
