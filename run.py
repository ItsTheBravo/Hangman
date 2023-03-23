import time

secret_word = ("secret")
turns = 10


def get_guess():
    """
    This function takes a guess from the player
    """
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()

        if len(guess) != 1:
            print('Please enter a single letter.')
        # elif guess in alreadyGuessed:
        #    print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def start():
    """
    Method to start the game
    """
    name = input("What is your name? ")
    print(f'Hello, {name}, lets play hangman!')
    time.sleep(2)
    print("The game is starting!\nTime to  play Hangman!")
    time.sleep(3)
    get_guess()


start()
