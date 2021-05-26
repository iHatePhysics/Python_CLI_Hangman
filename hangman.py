import random
import string
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* constant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True
# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = (set(list(string.ascii_lowercase))).difference(set(letters_guessed))
    return " ".join(sorted(letters_left))

def hint(secret_word,letters_guessed):
    '''
    Secret_word : secret word
    returns a letter that already exists in the Secret word
    '''
    n = ''.join(set(secret_word).difference(set(letters_guessed)))
    return random.choice(n)

def ifValid(input_character):
    if len(input_character)==1 and input_character in string.ascii_lowercase or input_character=='hint':
        return True
    else:
        return False
    
    # condition : 
    #   * input length == 1
    #   * must be character from a-z
    # return :
    #   true or false

def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(str(len(secret_word))), end='\n\n')
    
    lives = 8
    hints = 1
    letters_guessed = []
    while (lives > 0):
        
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters), end='\n')

        guess = input("Please guess a letter: ")
        
        if ifValid(guess)==True:
            if guess == "hint":
                if hints != 0:
                    hints-=1
                    letter = hint(secret_word,letters_guessed)
                    letters_guessed.append(letter)
                    print("Guess: {}".format(get_guessed_word(secret_word, letters_guessed)), end='\n')
                    print(f"{hints} Hints Left!\n")
                    continue
                else:
                    print("!!You have 0 hints left!!")
                    print("Guess: {}".format(get_guessed_word(secret_word, letters_guessed)), end='\n')
                    continue
            else:
                letter = guess.lower()

            if letter in secret_word:
                letters_guessed.append(letter)
                print("Good guess: {} ".format(get_guessed_word(secret_word, letters_guessed)), end='\n')
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print(" \n* * Congratulations, you won! * * ", end='\n\n')
                    break
            else:
                print("Oops! That letter is not in my word: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                letters_guessed.append(letter)
                print(IMAGES[8-lives])
                if lives == 1:
                    print("You Lost!")
                    print("\nThe Secret word was:",secret_word)
                lives -= 1
        else:
            print("Invalid Input!\nValid inputs:\tLetters:'a-z' or 'hint' for a hint!")
            continue

# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
