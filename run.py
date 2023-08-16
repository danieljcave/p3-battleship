# Battleship game keys for hit, miss and available spaces to guess.
# 'X' = Battleship hit
# ' ' = for available spaces
# 'O' = for a missed shot

from random import randint

# Used for the user input and displaying the board with the correct user 
# input for rows and columns structured in order.
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    }
   
def print_board(board):
    """
    Creates the battleship board and converts the 
    letters into numbers and prints on the board
    """
    print('  A B C D E F')
    print(' +-+-+-+-+-+-+')
    row_numb = 1
    for row in board:
        print("%d|%s|" % (row_numb, "|".join(row)))
        row_numb += 1

def create_ships(board):
    """
    Create a ship's location in a range of 10 ships total.
    Uses randint to randomise the ship's location,
    6 rows and columns
    """
    for ship in range(10):
        ship_row, ship_column = randint(0,5), randint(0,5)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,5), randint(0,5)
        board[ship_row][ship_column] = 'X'

def get_ship_location():
    """
    Input information for the user to guess a ship's location.
    If the user enters an invalid row number or column letter,
    will provide an error and prompt the user to enter the
    parameters.
    """
    row = input('Please enter a ship row 1-6: ')
    while row not in '123456':
        print('Please enter a valid row between 1-6')
        row = input('Please enter a ship row 1-6: ')
    column  = input('Please enter a ship column A-F: ').upper()
    while column not in 'ABCDEF':
        print('Please enter a valid column between letters A-F')
        column = input('Please enter a ship column A-F: ').upper()
    return int(row) - 1, letters_to_numbers[column]

def count_ships_hit(board):
    """
    Function to check the row to see if a ship has been hit.
    If a ship has hit the mark with a hit "X"
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

def intro():
    """
    An Introduction to the game of battleship with battleship
    display and game instructions.
    """
    print('''
    ____        __  __  __          __    _     
   / __ )____ _/ /_/ /_/ /__  _____/ /_  (_)___ 
  / __  / __ `/ __/ __/ / _ \/ ___/ __ \/ / __ |
 / /_/ / /_/ / /_/ /_/ /  __(__  ) / / / / /_/ /
/_____/\__,_/\__/\__/_/\___/____/_/ /_/_/ .___/ 
                                       /_/
'''
'\nWelcome to Battleship\n'
'Here we will test your strategic skills in a game of battleship.\n'
'How To Play: '
'\n- You will have 15 guesses to locate the 10 enemy ships'
'\n- A miss will show as an O and you will use a turn.'
'\n- A hit will show as an X and a turn will not be taken.'
'\n- The aim is to locate all ships and destroy them before you run out of turns'
'\n- Failure to locate all ships will lose the war... And the game will be over'
'\nGood luck Commander. Go get em!')

def start_input():
    """
    An Input to check if the user is ready to play the game.
    """
    while True:
        try:
            start_game = input("\nAre you ready to begin? Press Y to begin your battle: \n").upper()
        except EOFError:
            print("Invalid Input. Please Enter Again")
            continue
        if start_game == "Y":
            break
        else:
            print('Invalid Input, Please Enter Again')

def run_game():
    """
    Contains all elements of the game,
    Creates the boards containing the guess and computer board,
    the ships and guessing ship locations and turns.
    """
    # Hidden Board to hold the ship's location but not seen by the user.
    HIDDEN_BOARD = [[' '] * 6 for x in range(6)]
    # Guess Board that the user will see and use to guess the location of the 
    # battle ships.
    GUESS_BOARD = [[' '] * 6 for x in range(6)]
    create_ships(HIDDEN_BOARD)
    #Player has 15 turns to guess all 10 ship locations.
    turns = 15
    while turns > 0:
        print_board(HIDDEN_BOARD)
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == 'O':
            print('\nYou have already guessed that location, try guess again.')
        elif HIDDEN_BOARD[row][column] == 'X':
            print('\nNice Shot, you hit a battleship')
            GUESS_BOARD[row][column] = 'X'
        else:
            print('\nSorry, You missed a ship')
            GUESS_BOARD[row][column] = 'O'
            turns -= 1
        if count_ships_hit(GUESS_BOARD) == 10:
            print('\nCongratulations, You have sunk all of the battleships, Good Job!\n')
            break
        print('You have ' + str(turns) + ' turns remaining\n')
        if turns == 0:
            print('You have ran out of guesses. GAME OVER!\n')
            break

def replay_game():
    """
    A Function to check if the player would like to
    replay the game again.
    """
    while True:
        try:
            restart_game = input("Are you ready to play again: (Y)es / (N)o?\n").upper()
        except EOFError:
            print("Invalid Input. Please Try Again")
            continue
        if restart_game == "N":
            print("Thank you for playing, we hope you had a good time!")
            break
        elif restart_game == "Y":
            run_game() 
        else:
            print("\nAre you ready to play again: (Y)es / (N)o?\n").upper()

def play_game():
    """
    Function to run the game after the introduction
    """
    intro()
    start_input()
    run_game()
    replay_game()

play_game()