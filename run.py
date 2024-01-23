# Battleship game keys for hit, miss and available spaces to guess.
# 'X' = Battleship hit
# ' ' = for available spaces
# 'O' = for a missed shot

import os
import time
from random import randint, choice


def print_ascii():
    print("    ____        __  __  __          __    _")
    print("   / __ )____ _/ /_/ /_/ /__  _____/ /_  (_)___")
    print("  / __  / __ `/ __/ __/ / _ \\/ ___/ __ \\/ / __ |")
    print(" / /_/ / /_/ / /_/ /_/ /  __(__  ) / / / / /_/ /")
    print("/_____/\\__,_/\\__/\\__/_/\\___/____/_/ /_/_/ .___/")
    print("                                       /_/")


def intro():
    """
    An Introduction to the game of battleship with battleship
    display and game instructions.
    """
    print_ascii()
    print(
        "\nWelcome to Battleship\n"
        "Here we will test your strategic skills in a game of battleship.\n"
        "How To Play: "
        "\n- You will have 15 guesses to locate the 10 enemy ships"
        "\n- A miss will show as an O and you will use a turn."
        "\n- A hit will show as an X and a turn will not be taken."
        "\n- The aim is to locate all ships and destroy them before "
        "you run out of turns"
        "\n- Failure to locate all ships will lose the war... "
        "And the game will be over"
        "\nGood luck Commander. Go get em!\n"
    )


def clear_screen():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def start_input():
    """
    An Input to check if the user is ready to play the game.
    """
    while True:
        try:
            start_game = input(
                "Are you ready to begin? Press Y to begin your battle: \n"
            ).upper()
        except EOFError:
            print("Invalid Input. Please Enter Again\n")
            continue
        if start_game == "Y":
            break
        else:
            print("Invalid Input, Please Enter Again\n")


# Used for the user input and displaying the board with the correct user
# input for rows and columns structured in order.
letters_to_numbers = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
}

def can_place_ship(board, ship_row, ship_column, ship_size, orientation):
    """
    Checks if a ship of the given size can be placed at the specified location
    without overlapping with existing ships and fits within the board boundaries.
    """
    if orientation == "horizontal":
        if ship_column + ship_size > len(board[0]):
            return False  # If ship extends beyonds right edge of the board

        for i in range(ship_size):
            if board[ship_row][ship_column + i] == "X":
                return False
    elif orientation == "vertical":
        if ship_row + ship_size > len(board):
            return False  # If ship extends beyonds bottom edge of the board

        for i in range(ship_size):
            if board[ship_row + i][ship_column] == "X":
                return False
    return True


def place_ship(board, ship_row, ship_column, ship_size, orientation):
    """
    Place a ship of the given size at the specified location on the board.
    """
    if orientation == "horizontal":
        for i in range(ship_size):
            board[ship_row][ship_column + i] = "X"
    elif orientation == "vertical":
        for i in range(ship_size):
            board[ship_row + i][ship_column] = "X"


def create_ships(board):
    """
    Create ships of different sizes on the board.
    """
    ship_sizes = [4, 3, 3, 2, 1]  # Ship sizes for 5 ships
    orientations = ["horizontal", "vertical"]

    for ship_size in ship_sizes:
        while True:
            ship_row = randint(0, len(board) - 1)
            ship_column = randint(0, len(board[0]) - 1)
            orientation = choice(orientations)

            if can_place_ship(board, ship_row, ship_column, ship_size, orientation):
                place_ship(board, ship_row, ship_column, ship_size, orientation)
                break


def print_board(board, turns_remaining):
    """
    Creates the battleship board and converts the
    letters into numbers and prints on the board
    """
    clear_screen() # Clear the console screen
    print(f"\nYou have {turns_remaining} turns remaining\n")
    print("  A B C D E F")
    print(" +-+-+-+-+-+-+")
    row_numb = 1
    for row in board:
        print("%d|%s|" % (row_numb, "|".join(row)))
        row_numb += 1


def get_ship_location(previous_guesses):
    """
    Input information for the user to guess a ship's location.
    If the user enters an invalid row number or column letter,
    will provide an error and prompt the user to enter correct 
    value within the parameters.
    """
    while True:
        try:
            row = input("Please enter a ship row 1-6: \n")
            if not row.isdigit() or not (1 <= int(row) <= 6):
                raise ValueError("Invalid Input")
            row = int(row) - 1

            while True:
                column = input("Please enter a ship column A-F: \n").upper()
                if not column or column not in "ABCDEF":
                    print("Invalid Input. Please enter a valid column.")
                else:
                    break

            location = (row, letters_to_numbers[column])

            if location not in previous_guesses:
                previous_guesses.add(location)
                break
            else:
                print("You have already guessed that location, try guessing another location.")
        except ValueError:
            print("Invalid Input. Please enter a valid row and column.\n")

    return location


def count_ships_hit(board):
    """
    Function to check the row to see if a ship has been hit.
    If a ship has hit the mark with a hit "X"
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def run_game():
    """
    Contains all elements of the game,
    Creates the boards containing the guess and computer board,
    the ships and guessing ship locations and turns.
    """
    # Hidden Board to hold the ship's location but not seen by the user.
    HIDDEN_BOARD = [[" "] * 6 for _ in range(6)]
    # Guess Board that the user will see and use to guess the location of the
    # battle ships.
    GUESS_BOARD = [[" "] * 6 for _ in range(6)]
    create_ships(HIDDEN_BOARD)
    # Player has 15 turns to guess all 10 ship locations.
    turns = 25
    previous_guesses = set()
    while turns > 0:
        print_board(GUESS_BOARD, turns)  # Pass 'turns' as the second argument
        row, column = get_ship_location(previous_guesses)
        if GUESS_BOARD[row][column] == "O":
            print("\nYou have already guessed that location, "
                  "try guessing another location.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("\nNice Shot, you hit a battleship")
            GUESS_BOARD[row][column] = "X"
        else:
            print("\nSorry, You missed a ship")
            GUESS_BOARD[row][column] = "O"
            turns -= 1
        time.sleep(2)  # Add a short delay after hit/miss message
        if count_ships_hit(GUESS_BOARD) == 13:
            clear_screen()
            print_ascii()
            print("\nCongratulations, You have sunk all of "
                  "the battleships, Good Job!\n")
            replay_game()
            break
        if turns == 0:
            clear_screen()
            print_ascii()
            print("You have run out of guesses. GAME OVER!\n")
            replay_game()
            break


def replay_game():
    """
    A Function to check if the player would like to
    replay the game again.
    """
    while True:
        try:
            restart_game = input("Ready to play again: (Y)es/(N)o?\n").upper()
        except EOFError:
            print("Invalid Input. Please Try Again\n")
            continue
        if restart_game == "N":
            print("Thank you for playing, we hope you had a good time!")
            break
        elif restart_game == "Y":
            run_game()
        else:
            print("Invalid Input. Please Try Again\n")


def play_game():
    """
    Function to run the game after the introduction
    """
    intro()
    start_input()
    run_game()


play_game()
