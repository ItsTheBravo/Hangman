import time

secret_word = ("secret")
turns = 10
correct_guesses = []


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


def start():
    """
    Method to start the game
    """
    global turns, correct_guesses
    name = input("What is your name? ")
    print(f'Hello, {name}, lets play hangman!')
    time.sleep(2)
    print("The game is starting!\nTime to  play Hangman!")
    time.sleep(3)
    while turns > 0:
        print(f"You have {turns} turns left.")
        display_word()
        guess = get_guess()
        if guess in secret_word:
            correct_guesses.append(guess)
            print("Correct!")
        else:
            print("Incorrect!")
            turns -= 1


start()
