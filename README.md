# Hangman Game with Google Sheets Integration

## Table of Contents

- Overview
- User Goals
- Live Demo
- Getting Started
- Gameplay
- Features
- Future Features
- Testing
- Bugs
- Dependencies
- Deployment
- Credits

## Overview
This is a Python module that allows you to play a simple game of Hangman, while also interacting with a Google Sheets spreadsheet. The game works as follows: The player chooses a difficulty level (Easy, Medium, or Hard) and the program selects a random word from a list in a Google sheet based on that level. The player then tries to guess the word letter by letter, with a limited number of guesses allowed. If the player successfully guesses the word, they win the game. If they use up all their guesses without correctly guessing the word, they lose.

![Here is a live version of the project](https://hangman-jp.herokuapp.com/)

![Response](response.PNG)

The module uses the gspread library to interact with the Google sheet. The player can also add new words to the document using the program.


## User Goals

The Hangman game aims to provide an entertaining and interactive word-guessing experience for players. The following are the main user goals:

- **Entertainment**: Users expect to have an enjoyable and engaging gaming experience while playing Hangman. The game offers a classic word-guessing gameplay that keeps players entertained and immersed.

- **Challenge**: Players seek a game that tests their vocabulary and deduction skills. Hangman presents them with hidden words to guess, challenging their ability to decipher the correct letters and solve the puzzle.

- **Convenience**: Users appreciate the convenience of interacting with the game through player input. Hangman allows players to input their guesses and navigate the game using the menu and introductory prompts.

- **Learning**: Many players enjoy games that enhance their knowledge or vocabulary. Hangman introduces players to various words from different categories, contributing to their learning experience while having fun.

## Achieving User Goals

The Hangman game achieves these user goals and more through the following features and design elements:

- **Interactive Gameplay**: Hangman offers a basic yet engaging word-guessing gameplay experience. Players are prompted to enter their guesses, and the game displays the current state of the word being guessed, providing an interactive and dynamic gameplay environment.

- **Word Display**: The game provides a display of the secret word, showing the correct letters guessed by the player. This feature allows players to track their progress and make more informed guesses as they uncover the hidden word.

- **Word Source**: Hangman incorporates a functionality to retrieve words from a Google Spreadsheet. By accessing the spreadsheet, the game ensures a diverse and constantly updated set of words, offering players a wide range of options and challenges.

- **Player Input and Spreadsheet Interaction**: The game allows players to input new words to be added to the Google Spreadsheet. This feature promotes player engagement and contribution to the game's word repository, fostering a sense of ownership and customization.

- **Difficulty Levels**: Hangman offers different difficulty levels, including easy, medium, and hard. Players can choose the level that suits their skill and preference, allowing them to adjust the game's challenge and cater to different playing styles.

- **Menu and Navigation**: The game features a menu that allows players to start the game, add new words, or exit the program. This menu-based navigation provides a straightforward and convenient way for players to interact with the game and access different functionalities.

By addressing these user goals and incorporating the mentioned features, the Hangman game aims to deliver an entertaining, challenging, and educational gaming experience.


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

## Random Number Generation
The Hangman game utilizes a random number generation feature to select a word for the player to guess. This ensures that each gameplay session is unique and unpredictable. By generating a random number within a defined range, the game selects a word from its word bank or dictionary without any predetermined pattern or bias. This randomness adds excitement and variety to the game, preventing repetition and keeping players engaged.

## Player Doesn't Know the Word, Just the Number of Letters
In Hangman, the player is not provided with the actual word they need to guess. Instead, they are shown the number of letters in the word and blank spaces representing each letter. This feature adds a layer of challenge and mystery to the gameplay, as players must rely on their knowledge, vocabulary, and deduction skills to guess the correct letters and uncover the hidden word. By concealing the word itself, the game stimulates critical thinking and encourages players to explore different possibilities.

## Accept User Input
Hangman allows players to enter their guesses through user input. The game prompts the player to input a letter they believe is part of the hidden word. By accepting user input, the game fosters player engagement and active participation. Players can interact with the game, make decisions, and directly influence the gameplay outcome. This feature gives players a sense of control and involvement, enhancing their overall gaming experience.

## Keeps Track of the Letters Guessed, Correct and Incorrect
To assist players in their word-guessing efforts, Hangman keeps track of the letters they have guessed. The game maintains separate lists or records for correct and incorrect guesses. Whenever the player submits a letter, the game checks whether it is present in the hidden word. If the letter is correct, it is added to the list of correct guesses. If the letter is incorrect, it is added to the list of incorrect guesses. This feature helps players keep track of their progress, identify patterns, and make more informed guesses as they narrow down the possible letters in the word.

## Input Validation and Error Checking
Hangman incorporates input validation and error checking mechanisms to ensure that the user's input is accurate and appropriate. When the player enters a guess, the game validates the input to ensure it meets the required criteria. This includes checking that the input consists of a single letter, is within the allowable range (e.g., alphabetical characters), and has not been previously guessed. If the input fails any of these validation checks, the game provides appropriate error messages or prompts the player to enter a valid guess. This feature promotes a smooth and error-free gameplay experience, preventing incorrect inputs and guiding players towards valid and meaningful guesses.

By implementing these detailed features, the Hangman game offers a dynamic, challenging, and user-friendly word-guessing experience. Players can enjoy the excitement of guessing the hidden word while benefiting from features that enhance gameplay immersion, provide helpful information, and ensure accurate interaction.


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
* Fixed issue where game would crash along with adding a word causing game to crash

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

## Local Deployment

To deploy and run the Hangman game locally on your machine, follow the steps below:

* Clone or download the Hangman game repository from GitHub to your local machine.
* Ensure that you have Python 3.x installed on your system. If not, download and install Python from the official Python website.
* Navigate to the project directory in your terminal or command prompt.
* Install the required dependencies by running the following command:
    pip install gspread
* Create a Google Sheets document and share it with the email address associated with the service account key.
* Obtain a service account key file in JSON format for accessing the Google Sheets API. Save this file as "creds.json" in the project directory.
* Update the necessary configurations in the code, such as the name of the Google Sheets document and the worksheet containing the word list.
* Run the Hangman game by executing the following command:

    python3 run.py


Enjoy playing the Hangman game locally on your machine!

Note: Make sure you have a stable internet connection during the initial setup to authenticate and access the Google Sheets document. Once the game is set up, it can be played offline without an internet connection.

## Credits
* Code institute provided the deployment terminal.
* This module was written by a John-Paul McGrath.

