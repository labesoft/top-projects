"""The greeting in the Hangman Game
--------------------------------

About this Project
------------------
The objective of this project is to recreate The Hangman Game that a player
could play interactively by attempting to unmask a word one letter at a time
using a limited number of attempts without being hanged by the hangman.

Project structure
-----------------
*alarm/*
    **__main__.py**:
        The application of The Hangman Game
    **game.py**:
        The play logic of The Hangman Game
    **greeter.py**:
        The greeter of The Hangman Game
    **hangman.py**:
        The drawing logic of the hangman on the gallows
    **level.py**:
        The game levels of The Hangman Game
    **word.py**:
        The word handling logic of The Hangman Game
    **words_alpha.txt**
        The words dictionary provided with The Hangman Game

About this module
-----------------
This module is intended to manage out/in message to/from the player which will
make the game more interactive.

File structure
--------------
*import*
    **time.sleep**
        the time.sleep module allows delaying the input which is sometime
        printing its output too fast.

*constant*
    **IN_SLEEP**
        the delay time of 100ms is usually enough and goes unnoticed to
        the player
    **FORMAT_NEWLINE_**
        used to add new lines to strings
    **IN_MSG_***
        message printed to the player when asked for input
    **OUT_MSG_***
        message printed to the player

*class*
    **__init__(self, cb_out=print, cb_in=input)**
        'Initializes the out/in tools used as callbacks'
    **welcome(self, hangman)**
        'Welcomes the player in the game'
    **farewell(self)**
        'Says goodbye to the player when the game is over'
    **end_turn(self, good_wrong_msg)**
        'Congratulates or complains the player choice at the end of a turn'
    **end_game(self, hanged_image, end_msg, word)**
        'Congratulates or hangs the player at the end of the game'
    **new_letter(self)**
        'Asks the player for a letter which is then returned'
    **new_game(self)**
        'Asks the player to play a new game'
    **invalid_letter(self)**
        'Informs the player that his choice is invalid'
    **init_attempt(self, hangman, attempt_nb, word)**
        'Informs the player of the state of the game'
"""
from time import sleep


IN_SLEEP = 0.1

FORMAT_NEWLINE_PRE = "\n{}".format
FORMAT_NEWLINE_END = "{}\n".format

IN_MSG_LETTER = 'Enter your letter: '
IN_MSG_NAME = 'Enter your name: '
IN_MSG_REPLAY = 'Do You want to play again? y = yes, n = no'
OUT_MSG_ANSWER = "The word was: {}"
OUT_MSG_COMPLAINTS = ['Wrong guess ?! :O', 'Error :(', 'Missed ???', 'Sorry, you were wrong :_(']
OUT_MSG_CONGRATS = ['Good guess! Keep it up!!', "Wow! you're strong!!", 'I want to marry you <3', 'What a genius!!',
                    "Dude, you're a machine!!"]
OUT_MSG_GOODBYE = 'See you soon {}!'
OUT_MSG_INVALID = 'Invalid input, try another letter'
OUT_MSG_LOSER = 'You are out of attempt... Hanged!!'
OUT_MSG_LUCK = "Hello {}! Best of Luck!"
OUT_MSG_NB_ATTEMPT = "You have {} attempt"
OUT_MSG_READY = "The game is about to start... let's play Hangman!"
OUT_MSG_THANKS = 'Thanks for playing The Hangman Game!'
OUT_MSG_TRY_AGAIN = 'Try another letter plz'
OUT_MSG_WELCOME = 'Welcome to The Hangman Game by labesoft'
OUT_MSG_WINNER = "Congrats!! You have guessed the word correctly.."


class Greeter:
    def __init__(self, cb_out=print, cb_in=input):
        """Initializes the out/in tools used as callbacks

        :param cb_out: the callback used as the stdout
        :param cb_in: the callback used as the stdin
        """
        self._out = cb_out
        self._in = cb_in
        self.player_name = ''

    def welcome(self, hangman):
        """Welcomes the player in the game

        It prints the welcome message, the image of a hanged man, ask the name
        of the player, greets him and print the start of the game.

        :param hangman: the image of a hanged man
        """
        self._out(OUT_MSG_WELCOME)
        self._out(hangman)
        sleep(IN_SLEEP)
        self.player_name = self._in(IN_MSG_NAME)
        self._out(OUT_MSG_LUCK.format(self.player_name))
        self._out(FORMAT_NEWLINE_PRE(OUT_MSG_READY))

    def farewell(self):
        """Says goodbye to the player when the game is over"""
        self._out(OUT_MSG_THANKS)
        self._out(OUT_MSG_GOODBYE.format(self.player_name))

    def end_turn(self, good_wrong_msg):
        """Congratulates or complains the player's fate at the end of a turn

        :param good_wrong_msg: a congratulation or a complaint message string
        """
        self._out(FORMAT_NEWLINE_PRE(good_wrong_msg))

    def end_game(self, hanged_image, end_msg, word):
        """Congratulates or hangs the player at the end of the game

        :param hanged_image: the image of the hanged(or saved) player
        :param end_msg: a congratulation or a complaint message string
        :param word: the whole word revealed
        """
        self._out(hanged_image)
        self._out(end_msg)
        self._out(OUT_MSG_ANSWER.format(word))

    def new_letter(self):
        """Asks the player for a letter which is then returned

        :return: the player's choice, a stripped letter string
        """
        sleep(IN_SLEEP)
        return self._in(IN_MSG_LETTER).strip()

    def new_game(self):
        """Asks the player to play a new game

        :return: the player's choice
        """
        sleep(IN_SLEEP)
        return self._in(FORMAT_NEWLINE_END(IN_MSG_REPLAY))

    def invalid_letter(self):
        """Informs the player that his choice is invalid"""
        self._out(OUT_MSG_INVALID)

    def init_attempt(self, hangman, attempt_nb, word):
        """Informs the player of the state of the game

        :param hangman: the image of the parts hanged yet
        :param attempt_nb: the number ot attempt outstanding
        :param word: the current status of masked word
        """
        self._out(hangman)
        self._out(OUT_MSG_NB_ATTEMPT.format(attempt_nb))
        self._out(' '.join(list(str(word))))