# HANGMAN GAME
## Description

Hangman is a popular word guessing game where the player attempts to build a missing word by guessing one letter at a time. After a certain number of incorrect guesses, the game ends and the player loses.

You can try playing the game here https://hangmanwordgame.com/

--- 
### SETUP THE GAME CODE.

  * install git
  * `git clone https://github.com/iHatePhysics/Python_CLI_Hangman.git`
  * `python hangman` (to run code, you would be using python3) 

  
### ( Complete hangman function ):
### How To Play:
  * open `hangman.py`

  ### (LIVES)
  * A user has a set of lives to play the Game
  * Each round make a guess from the available letters
  
  ### (AVAILABLE LETTERS)
  * Availabe Letters are the letters which have not been guessed by the user.
 
  ### (INVALID INPUTS)
  * Check that whether the user's input is valid or not based on the below conditions i.e input character should be from a-z and should only contain letter.

  ### (GAME WON)
  * Check whether the word has been correctly guessed or not.

  ### (HINT)
  * Allows a user playing this game to ask for one hint, so whenever user types hint, we should display one letter which the user has not guessed and is present in the string.
  * hint can only be used once in a game
  * hint is not counted as a invalid character
  

