# **Project 3 Battleships**

## **Milestone Project 3 for Code Institute Full Stack Software Development.**
### Author - Daniel Cave

Battleships is a fully designed back-end Python-based terminal game which has been created and running on a terminal hosted on Heroku.

The Battleship game follows the standard practice of the user guessing the location of the opponent's battleships to sink and win the game. The Python-based game is designed and used in a terminal location using the rows and columns to guess the opponent's battleship locations to then sink and win.

Live version of the game avalible on Heroku - <a href="https://p3-battleship-dc-6afed2473960.herokuapp.com/">Click Here!</a>

## Table Of Contents
- [**Project 3 Battleships**](#project-3-battleships)
  - [**Milestone Project 3 for Code Institute Full Stack Software Development.**](#milestone-project-3-for-code-institute-full-stack-software-development)
    - [Author - Daniel Cave](#author---daniel-cave)
  - [Table Of Contents](#table-of-contents)
  - [**User Experience**](#user-experience)
    - [**Target Audience**](#target-audience)
    - [**Website Goals**](#website-goals)
  - [**User Stories**](#user-stories)
  - [Design](#design)
    - [How to play:](#how-to-play)
  - [Features](#features)
    - [Welcome Message](#welcome-message)
    - [Game Board](#game-board)
    - [Future Features](#future-features)
    - [Update Features](#update-features)
  - [Technologies Used](#technologies-used)
  - [Data Model](#data-model)
  - [Testing](#testing)
    - [Game Testing](#game-testing)
    - [CI Python Linter](#ci-python-linter)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)

## **User Experience**
### **Target Audience**
The target audience of the game is fans of the classic game Battleships. The deployed program will allow the user to play the game against a randomised computer output that they can play against multiple times.

### **Website Goals**
The primary goal of the website is to operate a functional game of battleships created with Python and deployed to a working instance of the game. It is designed to allow the user to play a complete game of battleships against the computer and feel like a classic game of battleships that the user would play in a physical environment or on a game-provided server or mobile.

## **User Stories**
- ## New User Visitor Goals
1. The game is designed to allow new users to complete a game of battleship on the deployed Heroku App.
2. Give the user clear instructions on how to play the game of battleships and score to know who has won.
3. Have a fair and complete game where does not feel that the computer will always win.

- ### Returning Visitor Goals
    1. To complete a game of battleship that they either won or lost to enjoy.
    2. Test their skills in the game of battleship to better understand the game.
    3. Have an enjoyable time against the computer to feel challenged but able to beat the computer.

## Design
### How to play:

The design of the game is based on the classic game of battleships. The main aim is to guess a location on the opponent's board to try and sink all of their battleships. The game allows the user to guess and use strategic guessing to locate and destroy all of the opponent's ships.

The rules of the game are a simplistic concept. The user has a 6x6 board to guess the location of all of the ships. The user is prompted to pick a row between the values 1-6. Once the user has inputted their choice, they are then asked to input a column, ranging from A through to F. That is then entered into the game to determine if the player misses the battleship or hits the battleship. If the player misses a Circle or O is posted on the player's chosen spot and a turn is deducted from their turns. If the player guesses correctly, then the program displays an X on the spot and notifies the player of a hit and no turn is removed.

The player has 15 guesses to locate the 5 ships that are located at random on the board. Once the player has used all of their guesses the player is presented with a game-over message and the game ends. If the user successfully guesses all the locations of the battleships they are presented with a congratuarly message informing them they have won and guessed all locations correctly. The user is then prompted if they would like to restart the game or not. If they select Yes, the game will restart allowing them to keep playing. If they select no, then a prompt message appears thanking them for playing.

## Features
### Welcome Message
The first feature of the battleship program is the Welcome message that displays on the screen when the user first enters the game. The user is first greeted with the word, Battleship in the terminal that uses ASCII text to create the word out of keyboard characters. The aim of this is to intrigue the user into the game, to not only get them engaged but to make them want to play the game. Rather than just Reading the words Battleship.

![Battleship Ascii image](/assets/readme/battleship-ascii.png)

On the welcome message, the user is welcomed to the game and shown the message 'How To Play:', this is a list of instructions on how the game will be played and what information the user will need beforehand to play the game. such as the game mechanics, which explain when a user guesses a spot they will either show a miss 'O' or a hit 'X' and all empty space is for the user to guess. It informs them of the number of turns they have and if they miss they will lose a turn and if they hit they will not lose and turn. Finally the aim of the game and what happens if they do not win.

![Image of battleship welcome message](/assets/readme/welcome-message.png)

The last feature on the welcome screen is asking the user if they are ready to play the game. This I believe is crucial to the user experience, by allowing the user to read through the information and be able to decide when they are ready to play. To not be able to see the playing game without the correct instructions or knowledge. This is to not overwhelm the player or allow them to start and just guess what they are doing or waste turns, to give them the best chance of winning and enjoying the time in the game.

![Player ready questions](/assets/readme/are-you-ready.png)

### Game Board
The game boards are made up of two boards. The game is a single-player game that is against a computer. The computer generates 5 random locations across the 6x6 board that the user has to guess. The program generates 5 ships with different length value and places them. This also checks to make sure ships do not overlap and that they dont go of the board. The value of the battleship locations is listed on the 'HIDDEN_BOARD'. This board is not shown to players as it has all the locations of the battleships for the player to guess. The 'GUESS_BOARD' is what the player sees. This is the board that they use to guess the locations of the battleships.

![GUESS_BOARD](/assets/readme/battleship-board.png)

**Player Guess Choice**
The player can choose how the game events happen. The player can guess any row or column that they would like. The player can make decisions and choices on their own to play their own game of battleship. They must choose a row between 1-6 and a column between A-F.

![player choice on the board](/assets/readme/battleship-board.png)

**Player Miss**
When the user is playing the game there is either a hit or a miss. If the player, unfortunately, misses the battleship, they are prompted with a message to let them know they missed and lose a turn.

![player miss](/assets/readme/player-miss.png)

**Player Hit**
When the user is playing the game there is either a hit or a miss. If the player scores a hit on the board. they are shown a message to let them know that they have hit a battleship. 

![player hit](/assets/readme/player-hit.png)

**Player Input & Validation**
There are different options when the player's input is required. At the start of the game when they are asked if they are ready to play. Then the most common is when asked to input which row and which column. To protect the game, the user must input a row and column within the board. The game checks that the user has entered a number in the range of 1-6 and a column of A-F. If the user tries to input anything out of the range, the game replies to the user and prompts a message that they are not in the range and reminds them. They are then instructed to input the row or column again.

![Player input value](/assets/readme/incorrect-value.png)

**Multiple Guesses**
If the player guesses a location that they have already guessed. The game will inform them that they have already guessed that location with a prompt. They will not lose a guess and game will ask them to re-input the row or column.

![player guesses multiple times](/assets/readme/multiple-guess.png)

**Player Loss**
If the player is unfortunately unable to guess all the locations of the battleship the player loses the game. If the player loses the game they will be prompted with a message to inform them of the loss. Following the loss the player will be asked if they would like to restart the game to try again or not.

![player loss](/assets/readme/player-lose.png)

**Player Win**
If the player guesses the correct location of the battleships and can get all 10 ships then the player wins. If that is the case the player will be shown and congratulatory message. They will then be asked if they would like to play the game again or would like not to.

![player win](/assets/readme/player-win.png)

**Replay Game**
The last feature of the game is the ability to replay the game. Rather than completing the game and having to refresh the page to run the program again. The player is asked at the end of their game if they win or lose. Whether they would like to play the game again or if they don't.

![replay game](/assets/readme/player-win.png)

### Future Features
- Users can choose difficulty or play on larger game boards with increased battleships.
- Allow the user to have their board with the user selecting where to place their battleship and the computer guessing their location.
~~- Have set-sized battleships rather than randomised locations.~~

### Update Features
Project was update from future features. The Game now creates 5 ships in total. A 4 size ship, two 3 size ships and two 2 size ships. This allows the user to hit a shit and if they sink one of the ships, the game notifies them so they can search for the other ships.

## Technologies Used
Programming Languages
- Python

Technologies
- <a href="https://code.visualstudio.com/">VSCode</a> 
    - Visual Studio Code for primary coding
- <a href="https://www.heroku.com/">Heroku</a>
    - Heroku Cloud-Based Platform to host terminal game
- <a href="https://patorjk.com/software/taag/#p=display&f=Slant&t=Battleship">Patorjk ASCII Generator</a>
    - Terminal Art Used ASCII
- <a href="https://codebeautify.org/python-formatter-beautifier">Code Beautify</a> 
    - Code beautify to beautify the Python code for readability

## Data Model
For my data model, I decided on two separate boards one would be used to hold computer information on the location of the battleships. Then another board would be shown to the user for them to guess the location of the battleships to ultimately try to beat the game and computer.

The model follows a data function to display the information needed at specific times. The first is the intro(). This displays the Battleship Art as well as the game information and how to play. Once a player is ready the start_input() is then called to display a ready question for the player to enter and start the game. Once the player has entered the correct value, run_game() displays the board and allows the player to guess. Once a player has completed the game, replay_game() provides the last question if they would like to play again.

## Testing
### Game Testing
In creating the game, I started with an 8x8 grid. After testing and all working there were no issues and the game was working as described. The issue came in user testing. It was found that the issue was too large a grid for the user to be able to have a chance at winning the game. The 8x8 grid needed to be reduced. After testing it was found that the ideal game conditions were 15 guesses with 5 ships on a 6x6 grid.

Each input was tested for the correct number and letter for the rows and the columns. Here can see that the game provides the user with an error message that informs them they have not entered a correct value and must enter a value in the range.

![testing image](/assets/readme/incorrect-value.png)

Each line of the code has been checked and tested throughout the Python Linter test and all have passed. Within the testing phase, all print functions have been tested to make sure the user is displayed with all the correct information. Through the testing using visual studio code, I was able to see any problems within the code and be able to correct them before deploying it to Heroku.

The overall game works as intended and all functions of the game are working correctly. The user can start the game, play the game and able to restart the game at their choosing.

### CI Python Linter
This was the list of issues shown in the CI Linter.

![Python first linter test](/assets/readme/python-validator-test.png)

After looking at the errors, most were due to extra whitespace after text, or code lines being too long. To fix the white space I checked the lines listed and remove the extra white space. To fix the issue of too long characters, I moved some lines below to their line so were still connecting and made sense.

![Python Test Complete](/assets/readme/python-validator-complete.png)

The main issue I found was due to the ASCII graphic of a battleship. The issue was due to the character sequence with the characters being used. After some research, I found a fix to the code was to enter each row into a print() function. Then with the character sequence, I added either a / or \ to the code to remove the sequence issue. With def print_ascii(), I then added the code to the intro(). This solved all the issues and now the test is clear and has no errors.

![Python Test Pass](/assets/readme/python-validator-pass.png)
## Bugs
~~There is a known bug in the game that I was unable to fix and after a lot of research and trying to input the correct code I was unable to provide a fix. The issue is when the user enters a blank character in the row and column it causes an issue within the game which causes the game to stop.~~
~~This is due to the int input. I had tried to use a while true statement to only allow the correct characters to be able to be input, this then caused an issue with the input of the game and was unable to solve.~~
- Known bug was fixed and game works as expected.

## Deployment
The game was deployed to Heroku using Code Instutute's mock terminal. To deploy, the following steps were taken:

- Create a Heroku account
- Choose Python as the primary development language
- Select the 'Create New App' button
- Create a name for the application
- Must add the **Python** and **nodejs** buildpacks in the settings menu
- Link your GitHub repository with Heroku on the deployment tab
- Final step is to select either automatic deployment or 'Deploy Branch' manually and select which branch to deploy.

## Credits
- Code Institute for the deployment terminal
- Garrett Broughton for Battleship inspiration and guidence <a href="https://github.com/gbrough/battleship/blob/main/single_player.py">Click Here</a>