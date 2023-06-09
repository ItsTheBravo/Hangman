"""This python module is written entirely in python.
This is a basic hangman game and features player input,
a display of the secret word. It contains functions to
get information from a google spreadsheet, as well as being
able to take user input to add to the spreadsheet. The game
works as a hangman game should, with a menu and an introduction
to start the game as well as functions to close the program."""

import time
import random
import gspread
from google.oauth2.service_account import Credentials

# Global Variables
TURNS = None
CORRECT_GUESSES = None
SECRET_WORD = None
RANDOM_WORD_INDEX = None
ALL_GUESSES = None

# Constant Variables for credentials, needed to access the spreadsheet.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

try:
    GPSREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GPSREAD_CLIENT.open('hangman_words')
except gspread.exceptions.APIError as e:
    print(f"An error occurred while accessing the spreadsheet: "
          f"{str(e)}")

# The worksheet where the words for the game are kept and updated
word_sheet = SHEET.worksheet('words')


def get_guess():
    """
    This function takes a guess from the player
    """
    while True:
        player_guess = input('Guess a letter: \n').lower()

        if len(player_guess) != 1:
            print('Please enter a single letter.')
        elif not player_guess.isalpha():
            print('Please enter a letter.')
        elif player_guess in CORRECT_GUESSES or player_guess in ALL_GUESSES:
            print('You have already guessed that letter. Choose again.')
        else:
            ALL_GUESSES.append(player_guess)
            return player_guess


def display_word():
    """
    This function displays the current state of the word being guessed
    """
    word = [letter if letter in CORRECT_GUESSES
            else "_" for letter in SECRET_WORD]
    print(" ".join(word))


def check_win():
    """
    This function checks if the player has won the game
    """
    for letter in SECRET_WORD:
        if letter not in CORRECT_GUESSES:
            return False
    return True


def play_again():
    """
    This function asks the player if they want to play again
    """
    while True:
        answer = input("Do you want to play again? (y/n) \n")
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
        print(f"Sorry, you lost. The word was {SECRET_WORD}.")
    if play_again():
        play_game()
    else:
        print("Thanks for playing!")


def random_word():
    """
    This function uses Random to take a random word from the sheet
    """
    word = random.randint(1, len(word_sheet.get_all_values()) - 1)
    return word


def play_game():
    """
    This method is the main gameplay functions. It calls the necessary
    functions to progress through the game and closes the game when turns are 0
    """
    global TURNS, CORRECT_GUESSES, SECRET_WORD, RANDOM_WORD_INDEX, ALL_GUESSES
    while True:
        name = input("What is your name?\n")
        if name.strip() != "":
            break
        print("Please enter a valid name.")
    level = get_difficulty_level()
    print(f'Okay, {name}, lets play hangman!')
    time.sleep(2)
    print("The game is starting!\nTime to  play Hangman!")
    time.sleep(3)
    RANDOM_WORD_INDEX = random_word()
    SECRET_WORD = word_sheet.cell(RANDOM_WORD_INDEX, level).value
    remaining_turns = 10
    CORRECT_GUESSES = []
    ALL_GUESSES = []
    while remaining_turns > 0:
        print(f"You have {remaining_turns} turns left.")
        display_word()
        player_guess = get_guess()
        if player_guess in SECRET_WORD or player_guess in CORRECT_GUESSES:
            CORRECT_GUESSES.append(player_guess)
            if player_guess in SECRET_WORD:
                print("Correct!")
                if check_win():
                    end_game(True)
                    return
            else:
                print("You have already guessed that letter. Choose again.")
        else:
            print("Incorrect!")
            remaining_turns -= 1
    end_game(False)


def get_difficulty_level():
    """
    This function takes a number from the player to pick the difficulty
    """
    options = {'1': 'Easy', '2': 'Medium', '3': 'Hard'}

    while True:
        level = input('Pick a difficulty: \n1) Easy 2) Medium 3) Hard  \n')

        if len(level) != 1:
            print('Please enter a single number.')
        elif level not in options:
            print('Please enter a valid option.')
        else:
            return int(level)


def add_word():
    """
    This function allows the user to add words to the spreadsheet
    """
    level = get_difficulty_level()
    while True:
        word = input("Enter a new word: \n")
        if word.strip() == "":
            print("Please enter a word.")
        else:
            break

    try:
        last_row = len(word_sheet.get_all_values())
        word_sheet.update_cell(last_row + 1, level, word)
        print(f"{word} has been added to the {level} level!")
    except gspread.exceptions.APIError as api_error:
        print(f"An error occurred while updating the spreadsheet: "
              f"{str(api_error)}")
        return


def display_main_menu():
    """
    This menu displays the options for the player to start the game,
    edit the spreadsheet, or close the game
    """

    # The first option calls the play_game() function, which starts the game
    # The section option calls the add_word() function, which allows the user
    # to add a word to the spreadsheet
    # The third option closes the program
    options = {
        "1": play_game,
        "2": add_word,
        "3": exit_program
    }
    while True:
        print("Hello, welcome to hangman! What would you like to do?")
        option = input(
            'Please choose an option: \n1) Play game 2) Add words 3) Exit  \n')

        if option in options:
            options[option]()
        else:
            print('Please enter one of the options.')


def exit_program():
    """
    This function closes the program
    """
    confirm = input(
        "Are you sure you want to exit the program? \n \
             Press 'y' to confirm: \n")
    if confirm.lower() == "y":
        print("Exiting program...")
        exit()


display_main_menu()
