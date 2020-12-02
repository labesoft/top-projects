"""The model of the hangman game
-----------------------------

About this Project
------------------
The objective of this project is to recreate the hangman game that a user could
play interactively trying to guess a to_guess with a limited number of guess.

Project structure
-----------------
*alarm/*
    **__main__.py**:
        The application of the hangman game
    **game.py**:
        The model of the hangman game

About this module
-----------------
The objective of this module is to model the hangman game using Python. It uses
innovative python libraries such as logging which helped us to build this
module, to setup the logger, to greets the player and to initialize the game
ran from the console.

File structure
--------------
*import*
    **logging**
        Provides a logging tool to inform the user of the system state through
        the console.
    **random**
        Randomly choose an item from a list or basically a sequence..
    **time**
        Import the actual time from the machine to use in the program

*constant*
    *NONE*

*func*
    **greetings()**
        Welcome the user in the game
    **main()**
        Initialize the hangman game
    **play_loop()**
        A loop to re-execute the game when the first round ends
    **hangman()**
        Checking all the conditions required for the game
"""
import logging
import random
import time


def greetings():
    """Welcome the user in the game"""
    # Initial Steps to invite in the game:
    logger = logging.getLogger(__name__)
    logger.info("\nWelcome to Hangman game by labesoft\n")
    time.sleep(1)
    name = input("Enter your name: ")
    logger.info("\nHello " + name + "! Best of Luck!\n")
    logger.info("The game is about to start... Let's play Hangman!\n")


def main():
    """Initialize the hangman game attributes

    We define the main function that initializes the arguments: global count, global display, global to_guess, global
     already_guessed, global length and global play_game. They can be used further in other functions too depending on
     how we want to call them.
    Words_to_guess: Contains all the Hangman words we want the user to guess in the game.
    Word: we use the random module in this variable to randomly choose the to_guess from words_to_guess in the game.
    Length: len() helps us to get the length of the string.
    Count: is initialized to zero and would increment in the further code.
    Display: This draws a line for us according to the length of the to_guess to guess.
    Already_guessed: This would contain the string indices of the correctly guessed words.
    """
    global count
    global display
    global to_guess
    global word
    global already_guessed
    global length
    global play_game
    with open('words_alpha.txt') as f:
        all_words = f.readlines()
        words_to_guess = [w.strip('\n') for w in all_words if len(w) > 2]
    word = to_guess = random.choice(words_to_guess)
    length = len(to_guess)
    count = 0
    display = '_ ' * (length - 1) + '_'
    already_guessed = []
    play_game = ""


def play_loop():
    """A loop to re-execute the game when the first round ends

    Play_loop: This function takes in the argument of play_game.
    Play_game: We use this argument to either continue the game after it is played once or end it according to what the
     user suggests.
    While loop is used to execute the play_game argument. It takes the parameter, y=yes and n=no. If the user gives an
     input of something else other than y/n, it asks the question again for the appropriate answer. If the user inputs
     “y”, the game restarts, otherwise the game ends.

    :return:
    """
    global play_game
    logger = logging.getLogger(__name__)
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
        hangman()
    elif play_game == "n":
        logger.info("Thanks For Playing! We expect you back again!")
        exit()

def hangman():
    """Checking all the conditions required for the game

    We call all the arguments again under the hangman() function.
    Limit: It is the maximum guesses we provide to the user to guess a particular to_guess.
    Guess: Takes the input from the user for the guessed letter. Guess.strip() removes the letter from the given to_guess.
    If loop checks that if no input is given, or two letters are given at once, or a number is entered as an input, it
     tells the user about the invalid input and executes hangman again.
    If the letter is correctly guessed, index searches for that letter in the to_guess.
    Display adds that letter in the given space according to its index or where it belongs in the given to_guess.
    If we have already guessed the correct letter before and we guess it again, It tells the user to try again and does
     not lessen any chances.
    If the user guessed the wrong letter, the hangman starts to appear which also tells us how many guesses are left.
     Count was initialized to zero and so with every wrong guess its value increases with one.
    Limit is set to 5 and so (limit- count) is the guesses left for the user with every wrong input. If it reaches the
     limit, the game ends, showing the right guesses (if any) and the to_guess that was supposed to be guessed.
    If the to_guess is guessed correctly, matching the length of the display argument, the user has won the game.
    Play_loop asks the user to play the game again or exit.
    Main() and hangman() would start again if the play_loop executes to yes.

    """
    global count
    global display
    global to_guess
    global word
    global already_guessed
    global play_game
    limit = 5
    logger = logging.getLogger(__name__)
    logger.info(f"This is the Hangman Word: {display}")
    time.sleep(1)
    guess = input("Enter your guess: ")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        logger.info("Invalid Input, Try a letter\n")
        hangman()
    elif guess in to_guess:
        already_guessed.extend([guess])
        index = to_guess.find(guess)
        to_guess = to_guess[:index] + "_" + to_guess[index + 1:]
        display = display[:index*2] + guess + display[index*2 + 1:]
        logger.info(f"\nGood guess: {display}")

    elif guess in already_guessed:
        logger.info("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            logger.info("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            logger.info("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            logger.info("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |     |\n"
                  "  |      \n"
                  "__|__\n")
            logger.info("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            logger.info("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\ \n"
                  "  |       \n"
                  "__|__\n")
            logger.info("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            logger.info("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\ \n"
                  "  |    / \n"
                  "__|__\n")
            logger.info("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            logger.info("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            logger.info("Wrong guess. You are hanged!!!\n")
            logger.info(f"The word was: {word}")
            logger.debug(f"already_guessed={already_guessed}, display={display}, to_guess={to_guess}")
            time.sleep(1)
            play_loop()

    if to_guess == '_' * length:
        logger.info("Congrats! You have guessed the to_guess correctly!")
        time.sleep(1)
        play_loop()

    elif count != limit:
        hangman()
