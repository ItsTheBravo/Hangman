# Hangman Game with Google Sheets Integration



This is a Python module that allows you to play a simple game of Hangman, while also interacting with a Google Sheets spreadsheet. The game works as follows: The player chooses a difficulty level (Easy, Medium, or Hard) and the program selects a random word from a list in a Google sheet based on that level. The player then tries to guess the word letter by letter, with a limited number of guesses allowed. If the player successfully guesses the word, they win the game. If they use up all their guesses without correctly guessing the word, they lose.

![Here is a live version of the project](https://hangman-jp.herokuapp.com/)

![Response](response.PNG)

The module uses the gspread library to interact with the Google sheet. The player can also add new words to the document using the program.

## Getting Started

Before you can use the module, you will need to create a Google sheet and a corresponding service account key for the application. This key should be saved in a file named "creds.json" in the same directory as the Python code. You will also need to enable the Google Sheets API for your Google account and share the document with the email address associated with the service account key.

You will also need to install the gspread library using pip.

## Gameplay

When you run the program, it will ask for your name and then display the main menu, which offers three options:

    Play the game
    Add a word to the list
    Quit

If you choose to play the game, the program will ask you to choose a difficulty level and then start the game. The program will display the current state of the word being guessed, as well as the number of turns remaining. You can then guess a letter by typing it and pressing enter. If you guess correctly, the letter will be added to the word and you will get another turn. If you guess incorrectly, you will lose a turn. You can also choose to add a new word to the list or quit the game.

At the end of the game, the program will display whether you won or lost, and ask if you want to play again.

## Features

* Random number Generation
* Player doesn't know the word, just the number of letters
* Accept User input
* Keeps track of the letters guessed, correct and incorrect
* Input validation and error checking

### Future Features
* Allow the player to Edit and Delete words
* Display a visual representation of the hangman figure
* Display all letters guessed previously

## Testing
* Passed the code through online linter, confirmed no errors.
* Tested valid inputs, tested wrong inputs such as numbers or strings longer than 1 character, or empty inputs.
* Tested on my local terminal and Heroku Terminal

## Bugs
* I had an issue where my deployed project would not run on Heroku because I was missing a gspread install, turns out I needed to install gspread with pip3 instead of just pip and it fixed it.
* I had an issue where I wasn't getting the correct words or index errors from the random numbers, I fixed this by using the length of the list for the random number instead of a magic number.

## Dependencies

The module uses the following Python libraries:

    time
    random
    gspread

## Deployment 
This project was deployed using Code Institutes mock terminal for Heroku. To deploy this:
* Fork or clone this repository.
* Create a new Heroku app.
* Set the buildbacks to Python and NodeJS in that order
* Link the Heroku App to the repository
* Click on Deploy


## Credits
* Code institute provided the deployment terminal.
* This module was written by a John-Paul McGrath.

