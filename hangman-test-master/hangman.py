import string
from typing import Counter
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''
def hint(val, hint_count, letters_guessed):
    if val.lower() != "hint":
        return hint_count
    if hint_count == 0:
        print("Hints limit exceeded!!!")
        return 0
    else:
        hint_count = hint_count - 1
        words_remaining = [item for item in list(secret_word) if item not in list(letters_guessed)]
        letters_guessed += words_remaining[0]
        print(get_guessed_word(secret_word, letters_guessed))
    return hint_count
    

def ifValid(c):
    if len(c) == 1:
        if c.isalpha() and c.islower():
            return True
    return False


def display_images(cnt):
    print(IMAGES[len(IMAGES) - cnt - 1])


def is_word_guessed(secret_word, letters_guessed):
    
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)j
    '''
    guessed_word = get_guessed_word(secret_word, letters_guessed)

    if guessed_word == secret_word:
        return True
    return False

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
    letters_left = string.ascii_lowercase
    letters_left = [item for item in list(letters_left) if item not in list(letters_guessed)]
    return letters_left


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
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    letters_guessed = []
    remaining_lives = 8
    hint_count = 1
    while remaining_lives != 0:
        # print(remaining_lives)

        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))

        guess = input("Please guess a letter: ")

        hint_count = hint(guess, hint_count, letters_guessed)
        if hint_count == 0 and guess == "hint":
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
            continue
        


        if not ifValid(guess):
            print("Invalid")
            continue
        letter = guess.lower()

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            display_images(remaining_lives)
            remaining_lives = remaining_lives - 1
            print("Remaining lives: " + str(remaining_lives))
            letters_guessed.append(letter)
            print("")
    if remaining_lives == 0:
        print("Game Over")
        print("WORD was "+ secret_word)


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
