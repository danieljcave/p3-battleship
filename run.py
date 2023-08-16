# Battleship game keys for hit, miss and available spaces to guess.
# 'X' = Battleship hit
# ' ' = for avalible spaces
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
    'G': 6,
    'H': 7
    }
   
def print_board(board):
    print('  A B C D E F G H')
    print(' +-+-+-+-+-+-+-+-+')
    row_numb = 1
    for row in board:
        print("%d|%s|" % (row_numb, "|".join(row)))
        row_numb += 1

def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'X'

def get_ship_location():
    row = input('Please enter a ship row 1-8: ')
    while row not in '12345678':
        print('Please enter a valid row between 1-8')
        row = input('Please enter a ship row 1-8: ')
    column  = input('Please enter a ship column A-H: ').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column between letters A-H')
        column = input('Please enter a ship column A-H: ').upper()
    return int(row) - 1, letters_to_numbers[column]

def count_ships_hit(board):
    """
    Function to check the row to see if a ship has been hit.
    If a ship has been hit mark with a hit "X"
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

def intro():
    """
    An Introduction into the game of battleship with battleship
    display and game instructions.
    """
    print('''
    ____        __  __  __          __    _     
   / __ )____ _/ /_/ /_/ /__  _____/ /_  (_)___ 
  / __  / __ `/ __/ __/ / _ \/ ___/ __ \/ / __ |
 / /_/ / /_/ / /_/ /_/ /  __(__  ) / / / / /_/ /
/_____/\__,_/\__/\__/_/\___/____/_/ /_/_/ .___/ 
                                       /_/
\nWelcome to Battleship. Here we will test your strategic 
skills in a game of battleship.\n
How To Play:
          ''')
    
def start_input():
    """
    A Input to check if the user is ready to play the game.
    """
    while True:
        try:
            start_game = input("Are you ready to begin? Press Y to begin your battle: \n").upper()
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
    # Hidden Board to hold the ships location but not seen by the user.
    HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
    # Guess Board that the user will see and use to guess the location of the 
    # battle ships.
    GUESS_BOARD = [[' '] * 8 for x in range(8)]
    create_ships(HIDDEN_BOARD)
    #Player has 10 turns to guess all 5 ship locations.
    turns = 10
    while turns > 0:
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == 'O':
            print('\nYou have already guessed that location, try guess again.')
        elif HIDDEN_BOARD[row][column] == 'X':
            print('\nNice Shot, you hit a battleship')
            GUESS_BOARD[row][column] = 'X'
            turns -= 1
        else:
            print('\nSorry, You missed a ship')
            GUESS_BOARD[row][column] = 'O'
            turns -= 1
        if count_ships_hit(GUESS_BOARD) == 5:
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
            print("Invalid Input. PLease Try Again")
            continue
        if restart_game == "N":
            print("Thank you for playing, we hope you had a good time!")
            break
        elif restart_game == "Y":
            run_game() 
        else:
            print("Are you ready to play again: (Y)es / (N)o?\n").upper()

def play_game():
    """
    Function to run the game after the introduction
    """
    intro()
    start_input()
    run_game()
    replay_game()

play_game()