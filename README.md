# Connect-4

### 1. Introduction
The task was to implement a game  Connect 4 with python. It is played through terminal. There are two players who play round by round until one of the players won or the game board is filled - nobody wins. The purpose of the game is to match 4 or more player tokens horizontally, vertically or diagonally.

### 2. Methods
The configuration file configs.txt is provided to configure the game. Game field width, height and player token symbols are declared in this file. The game board configuration was implemented in exercise 5. The board representation has separators to separate the fields which will be filled with player token symbols. Depending on the proportions of a symbol the walls of the cell are drawn using separator symbols “-” and “|”. The game board is drawn in a method createGameField().
Validity of the symbols is checked using a method checkValid(). The symbol is valid if it has correct proportions (a x a). Length and height are equal.
In exercise 6 the game was implemented. gameTurn method implements how each turn works. 

First it is checked whether a correct column (if it exists and if it is full) was provided by the player, if not the gameTurn function is called recursively and player is asked to enter a different column.
During a turn the player token is placed on the board, as well as in game tracking board which stores the number of player in the plater tracking table matching cell.
After each turn it is checked whether the game continues. That is whether there is a winner or the board is full and there is no winner.

### 3. Play the game
To play the game you have to write your wanted configurations into configuration file configs.txt (or use the provided one).
Run the python script to start the game:
python3 ex6.py
The game starts. Player 1 and 2 one by one are asked to enter the column. The column must be of correct data type - int.
Round by round game is played until a winner is declared or the board is full.
