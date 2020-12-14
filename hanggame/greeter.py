"""The greeting in the Hangman Game
--------------------------------

About this Project
------------------
The objective of this project is to recreate The Hangman Game that a player
could play interactively by attempting to unmask a word one letter at a time
using a limited number of attempts without being hanged by the hangman.

Project structure
-----------------
*hanggame/*
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
    **SPACING**
        standard spacing constant
    **IN_SLEEP**
        the delay time of 100ms is usually enough and goes unnoticed to
        the player
    **FORMAT_NEWLINE_**
        used to add new lines to strings
    **IN_MSG_***
        message printed to the player when asked for input
    **OUT_MSG_***
        message printed to the player
"""
import gettext
import logging
import os

from time import sleep


try:
    t = gettext.translation('hanggame', localedir=os.path.join(os.path.dirname(__file__), 'locales'))
except FileNotFoundError as err:
    logger = logging.getLogger(__name__)
    default_lang = 'en_US'
    logger.warning(f'no language set, falling back to default: {default_lang}')
    t = gettext.translation('hanggame', localedir='locales', languages=[default_lang])
    t.install()
_ = t.gettext


SPACING = ' '
IN_SLEEP = 0.1
FORMAT_NEWLINE_PRE = "\n{}".format
FORMAT_NEWLINE_END = "{}\n".format

IN_MSG_LETTER = _('Enter your letter: ')
IN_MSG_NAME = _('Enter your name: ')
IN_MSG_REPLAY = _('Do You want to play again? y = yes, n = no')
OUT_MSG_ANSWER = _("The word was: {}")
OUT_MSG_COMPLAINTS = [_('Wrong guess ?! :O'), _('Error :('), _('Missed ???'), _('Sorry, you were wrong :_(')]
OUT_MSG_CONGRATS = [_('Good guess! Keep it up!!'), _("Wow! you're strong!!"), _('I want to marry you <3'),
                    _('What a genius!!'), _("Dude, you're a machine!!")]
OUT_MSG_GOODBYE = _('See you soon {}!')
OUT_MSG_INVALID = _('Invalid input, try another letter')
OUT_MSG_LOSER = _('You are out of attempt... Hanged!!')
OUT_MSG_LUCK = _("Hello {}! Best of Luck!")
OUT_MSG_NB_ATTEMPT = _("You have {} attempt")
OUT_MSG_READY = _("The game is about to start... let's play Hangman!")
OUT_MSG_THANKS = _('Thanks for playing The Hangman Game!')
OUT_MSG_TRY_AGAIN = _('Try another letter plz')
OUT_MSG_WELCOME = _('Welcome to The Hangman Game by labesoft')
OUT_MSG_WINNER = _("Congrats!! You have guessed the word correctly..")


class Greeter:
    def __init__(self, cb_out=print, cb_in=input):
        """Initializes the out/in tools used as callbacks

        :param cb_out: the callback used as the stdout
        :param cb_in: the callback used as the stdin
        """
        self._out = cb_out
        self._in = cb_in
        self.player_name = SPACING

    def in_new_game(self):
        """Asks the player to play a new game

        :return: the player's choice
        """
        return self.input(FORMAT_NEWLINE_END(IN_MSG_REPLAY))

    def in_new_letter(self):
        """Asks the player for a letter which is then returned

        :return: the player's choice, a stripped letter string
        """
        return self.input(IN_MSG_LETTER).strip()

    def input(self, in_msg):
        sleep(IN_SLEEP)
        return self._in(in_msg)

    def out_end_game(self, hanged_image, end_msg, word):
        """Congratulates or hangs the player at the end of the game

        :param hanged_image: the image of the hanged(or saved) player
        :param end_msg: a congratulation or a complaint message string
        :param word: the whole word revealed
        """
        self._out(hanged_image)
        self._out(end_msg)
        self._out(OUT_MSG_ANSWER.format(word))

    def out_end_turn(self, good_wrong_msg):
        """Congratulates or complains the player's fate at the end of a turn

        :param good_wrong_msg: a congratulation or a complaint message string
        """
        self._out(FORMAT_NEWLINE_PRE(good_wrong_msg))

    def out_farewell(self):
        """Says goodbye to the player when the game is over"""
        self._out(OUT_MSG_THANKS)
        self._out(OUT_MSG_GOODBYE.format(self.player_name))

    def out_invalid_letter(self):
        """Informs the player that his choice is invalid"""
        self._out(OUT_MSG_INVALID)

    def out_init_attempt(self, hangman, attempt_nb, word):
        """Informs the player of the state of the game

        :param hangman: the image of the parts hanged yet
        :param attempt_nb: the number ot attempt outstanding
        :param word: the current status of masked word
        """
        self._out(hangman)
        self._out(OUT_MSG_NB_ATTEMPT.format(attempt_nb))
        self._out(SPACING.join(list(word)))

    def out_in_welcome(self, hangman):
        """Welcomes the player in the game

        It prints the welcome message, the image of a hanged man, ask the name
        of the player, greets him and print the start of the game.

        :param hangman: the image of a hanged man
        """
        self._out(OUT_MSG_WELCOME)
        self._out(hangman)
        self.player_name = self.input(IN_MSG_NAME)
        self._out(OUT_MSG_LUCK.format(self.player_name))
        self._out(FORMAT_NEWLINE_PRE(OUT_MSG_READY))
