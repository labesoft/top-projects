"""The console in the Hangman Game
-------------------------------

About this module
-----------------
This module is intended to manage out/in message to/from the player which will
make the game more interactive in the console.

File structure
--------------
*import*
    **time.sleep**
        the time.sleep module allows delaying the input which is sometime
        printing its output too fast.

*constant*
    **SPACE_STR**
        standard spacing constant
    **IN_SLEEP**
        the delay time of 100ms is usually enough and goes unnoticed to
        the player
    **FORMAT_NEWLINE_**
        used to add new lines to strings
    **YES_NO_LIST**
        lists of yes/no options that the player may use to answer the play again
        question.
"""
__author__ = "Benoit Lapointe"
__date__ = "2020-12-18"
__copyright__ = "Copyright 2020, labesoft"

__version__ = "1.0.0"

from time import sleep

from hanggame import i18n
from hanggame.game import HangGame
from hanggame.hangman import Hangman

SPACE_STR = ' '
IN_SLEEP = 0.1
FORMAT_NEWLINE_PRE = "\n{}".format
FORMAT_NEWLINE_END = "{}\n".format
YES_NO_LIST = i18n.IN_YES_LIST + i18n.IN_NO_LIST


class Console:
    """This class sets up the game interaction with the console"""

    def __init__(self, word, hangman, c_out=print, c_in=input):
        """Initializes the out/in tools used as callbacks

        :param c_out: the callback used as the stdout
        :param c_in: the callback used as the stdin
        """
        self.c_out = c_out
        self.c_in = c_in
        self.player_name = SPACE_STR
        self.word = word
        self.hangman = hangman

    def accept_letter(self, key):
        """Gets the letter from the key typed by the player

        The key is retyped until the chosen letter is available

        :key: the initial key typed by the player
        :return: the letter chosen by the player
        """
        choices = ' '.join(sorted(self.word.available))
        while not self.word.is_masked(key):
            self.c_out('{}: [{}]'.format(i18n.OUT_MSG_CHOICES, choices))
            key = self.in_valid_letter()
        return key

    def ask_play_again(self):
        """Asks the player to play again

        If the answer is yes the game reset itself and is ready to restart.
        Otherwise, the game is triggered to stop and greets the player
        """
        choice = ''
        while choice.lower() not in YES_NO_LIST:
            choice = self.input(FORMAT_NEWLINE_END(i18n.IN_MSG_REPLAY))
        if choice.lower() in i18n.IN_YES_LIST:
            self.hangman.reset()
            self.word.choose()
            return True
        else:
            self.out_farewell()
            return False

    def end_game(self, end_msg):
        """Presents the state of the game to the player after a game has ended

        :param end_msg: a congratulation or a complaint message string
        """
        self.c_out(str(self.hangman))
        self.c_out(end_msg)
        self.c_out(i18n.OUT_MSG_ANSWER.format(self.word.show()))

    def end_turn(self, end_msg):
        """Presents the states of the game to the player after a turn has ended

        :param end_msg: the msg provided to end the turn
        """
        self.c_out(FORMAT_NEWLINE_PRE(end_msg))

    def in_valid_letter(self):
        """Asks the player for a letter which is then returned in lowercase

        :return: the player's choice, a lowercase letter string
        """
        result = self.input(i18n.IN_MSG_LETTER)
        while len(result) != 1 or not result.isalpha():
            self.out_invalid_letter()
            result = self.input(i18n.IN_MSG_LETTER)
        return result.lower()

    def init_game_metrics(self):
        """Informs the player of the state of the game"""
        self.c_out(str(self.hangman))
        self.c_out(i18n.OUT_MSG_NB_ATTEMPT.format(self.hangman.attempt))
        self.c_out(SPACE_STR.join(list(self.word)))

    def input(self, in_msg):
        """Output message that asks the player to type an input

        :param in_msg: the message printed out to the player
        :return: the stripped from space message typed by the player
        """
        sleep(IN_SLEEP)
        return self.c_in(in_msg).strip()

    def out_farewell(self):
        """Says goodbye to the player when the game is over"""
        self.c_out(i18n.OUT_MSG_THANKS)
        self.c_out(i18n.OUT_MSG_GOODBYE.format(self.player_name))

    def out_invalid_letter(self):
        """Informs the player that his choice is invalid"""
        self.c_out(i18n.OUT_MSG_INVALID)

    def welcome_player(self):
        """Welcomes the player in the game

        It prints the welcome message, the image of a hanged man, ask the name
        of the player, greets him and print the start of the game.

        :param hangman: the image of a hanged man
        """
        self.c_out(i18n.OUT_MSG_WELCOME)
        self.c_out(str(self.hangman))
        self.player_name = self.input(i18n.IN_MSG_NAME)
        self.c_out(i18n.OUT_MSG_LUCK.format(self.player_name))
        self.c_out(FORMAT_NEWLINE_PRE(i18n.OUT_MSG_READY))


def main(level, word):
    """Launch the console game

    :param level: the level chosen on the cli
    :param word: the word initialized in the __main__
    """
    hangman = Hangman(level=level)
    ui = Console(word=word, hangman=hangman)
    game = HangGame(level, word, hangman, ui)
    game.run_loop()
