"""The play logic of The Hangman Game
----------------------------------

About this module
-----------------
The objective of this module is to model The Hangman Game using Python. It uses
innovative python libraries such as logging which helped us to build this
module, to setup the logger, to greets the player and to initialize the game
ran from the console.

File structure
--------------
*import*
    **logging**
        provides a logging tool to inform the user of the system state through
        the console.
    **random**
        randomly choose an item from a list or basically a sequence.
"""

__author__ = "Benoit Lapointe"
__date__ = "2020-12-18"
__copyright__ = "Copyright 2020, labesoft"
__version__ = "1.0.0"

import random

from hanggame import i18n


class HangGame:
    """The game play of The Hangman Game

    The course of the game follows the rules defined in this class.
    """
    def __init__(self, level, word, hangman, ui):
        """Initializes The Hangman Game and all of its attributes

        :param level: the level of The Hangman Game
        :param word: the word to unveil and its inner logic
        :param hangman: the hangman that tries to hang the player
        :param ui: the user interface (console
        """
        self.game_level = level
        self.hangman = hangman
        self.word = word
        self.ui = ui

    def run_loop(self):
        """Runs the game until the player does not want to play again

        It includes the running loop which processes The Hangman Game.
        """
        self.hangman.draw(hanged=True)
        self.ui.welcome_player()
        self.hangman.draw()

        self.ui.init_game_metrics()
        while self.play_turn(self.ui.in_valid_letter()):
            self.ui.init_game_metrics()

    def play_turn(self, key):
        """Plays one complete turn with the letter provided

        If the game ended during the turn the player is asked to play again.

        :param key: the letter to test during this turn
        """
        if self.word and self.hangman.attempt:
            letter = self.ui.accept_letter(key)
            if self.word.unmask(letter):
                self.ui.end_turn(random.choice(i18n.OUT_MSG_CONGRATS))
                if not self.word.is_mask():
                    self.hangman.draw(saved=True)
                    self.ui.end_game(i18n.OUT_MSG_WINNER)
                    return self.ui.ask_play_again()
            else:
                self.hangman.missed += 1
                self.hangman.draw()
                self.ui.end_turn(random.choice(i18n.OUT_MSG_COMPLAINTS))
                if not self.hangman.attempt:
                    self.ui.end_game(i18n.OUT_MSG_LOSER)
                    return self.ui.ask_play_again()
        else:
            return False
