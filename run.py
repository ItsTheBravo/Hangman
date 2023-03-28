import time
import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GPSREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GPSREAD_CLIENT.open('hangman_words')

sales = SHEET.worksheet('Easy')


def get_guess():
    """
    This function takes a guess from the player
    """
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()

        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        elif guess in correct_guesses:
            print('You have already guessed that letter. Choose again.')
        else:
            return guess


def display_word():
    """
    This function displays the current state of the word being guessed
    """
    word = ""
    for letter in secret_word:
        if letter in correct_guesses:
            word += letter
        else:
            word += "_"
    print(word)


def check_win():
    """
    This function checks if the player has won the game
    """
    for letter in secret_word:
        if letter not in correct_guesses:
            return False
    return True


def play_again():
    """
    This function asks the player if they want to play again
    """
    while True:
        answer = input("Do you want to play again? (y/n) ")
        answer = answer.lower()

        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please enter y or n.")


def end_game(win):
    """
    This function ends the game and displays the result
    """
    if win:
        print("Congratulations, you won!")
    else:
        print(f"Sorry, you lost. The word was {secret_word}.")
        time.sleep(2)
    if play_again():
        start()
    else:
        print("Thanks for playing!")


def random_word():
    """
    This function uses Random to take a random word from the sheet
    """
    word = random.randint(2, 11)
    return word


def get_level():
    """
    This function takes a number from the player to pick the difficulty
    """
    while True:
        level = input('Pick a difficulty: \n1) Easy 2) Medium 3) Hard  \n')

        if len(level) != 1:
            print('Please enter a single number.')
        elif level not in '123':
            print('Please enter a one of the options.')
        else:
            return level


def start():
    """
    Method to start the game
    """
    global turns, correct_guesses, secret_word, word_num
    name = input("What is your name? \n")
    level = get_level()
    print(f'Okay, {name}, lets play hangman!')
    time.sleep(2)
    print("The game is starting!\nTime to  play Hangman!")
    time.sleep(3)
    word_num = random_word()
    secret_word = sales.cell(word_num, level).value
    print(secret_word)
    turns = 10
    correct_guesses = []
    while turns > 0:
        print(f"You have {turns} turns left.")
        display_word()
        guess = get_guess()
        if guess in secret_word:
            correct_guesses.append(guess)
            print("Correct!")
            if check_win():
                end_game(True)
                return
        else:
            print("Incorrect!")
            turns -= 1


start()
