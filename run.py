import time


def start():
    """
    Method to start the game
    """
    name = input("What is your name? ")
    print(f'Hello, {name}, lets play hangman!')
    time.sleep(2)
    print("The game is starting!\nTime to  play Hangman!")
    time.sleep(3)


start()
