"""The game window of The Hangman Game
-----------------------------

About this Project
------------------
The objective of this project is to recreate The Hangman Game that a user could
play interactively by attempting to unmask a word one letter at a time using a
limited number of attempts without being hanged by the hangman.

Project structure
-----------------
*hanggame.ui/*
    **game_window.py**:
        The game window of The Hangman Game
        
About this module
-----------------
The objective of this module is to view the main window of The Hangman Game
using Python. It uses innovative python libraries such as PyQt5 which helped
to visually create the UI representation of the game and import directly into
our code. That way we created highly modular, modifiable and testable UI code.

File structure
--------------
*import*

*constant*

*class*
    **GameWindow**
        'This class puts in place the base layout of the game window that will
         show the The Hangman Game widgets'

"""
__author__ = "Benoit Lapointe"
__date__ = "2020-12-18"
__copyright__ = "Copyright 2020, labesoft"

__version__ = "1.0.0"

import random
import sys

from PyQt5 import QtWidgets, uic

from hanggame import greeter, word
from hanggame.level import GameLevel


class GameWindow(QtWidgets.QMainWindow):
    """This class puts in place the base layout of the game window

    It will show The Hangman Game widgets
    """
    def __init__(self):
        """Initializes the game window setting all the boards to their initial values

        It also binds the keyboard and level combo box events to proper methods
        """
        super(GameWindow, self).__init__()
        uic.loadUi('game_window.ui', self)
        self.greeterboard.welcome_player()
        self.scoreboard.set_labels()
        self.update_dynamic_texts(greeter.OUT_NEW_GAME)
        self.keyboard.bind(self.start_game, self.play_turn)
        self.scoreboard.bind(self.change_level)
        self.show()

    def change_level(self):
        """Changes the level to the combo value and aborts the current game to restart a new one"""
        self.greeterboard.reset(GameLevel[self.scoreboard.level_combo.currentText()], '')
        self.word_view.word.show()
        self.update_dynamic_texts(greeter.OUT_NEW_GAME)

    def start_game(self):
        """Start a new game choosing a new word resetting all game components"""
        self.word_view.word.choose()
        self.greeterboard.reset(msg=greeter.OUT_MSG_LUCK)
        self.keyboard.reset()
        msg = greeter.SPACING.join(list(str(self.word_view.word)))
        self.update_dynamic_texts(msg)

    def out_end_turn(self, w, end_msg):
        """Presents the states of the game to the player after a turn has ended

        :param w: the word revealed so far
        :param end_msg: the msg provided to end the turn
        """
        self.progress_bar.set_value(w, word.MASK)
        self.greeterboard.greets(end_msg)
        self.scoreboard.set_score(self.greeterboard.hangman.missed, self.greeterboard.hangman.attempt)
        self.word_view.setText(' '.join(list(w)))

    def out_end_game(self, w, end_msg):
        """Presents the state of the game to the player after a game has ended

        :param w: the word revealed to the player
        :param end_msg: the msg provided to end the game
        :return:
        """
        self.greeterboard.greets(end_msg)
        self.word_view.setText(greeter.OUT_MSG_ANSWER.format(w))

    def play_turn(self, letter):
        """Plays this cycle for each letter chosen by the player

        It tries to unmask a letter, but if it fails the player see one of his body part
        being hanged to the gallows until no parts are left which would loose the game.
        The goal is to reveal the whole word.
        :param letter: a letter to try
        """
        if str(self.word_view.word) and self.greeterboard.hangman.attempt:
            if self.word_view.word.unmask(letter.lower()):
                self.out_end_turn(str(self.word_view.word), random.choice(greeter.OUT_MSG_CONGRATS))
                if not self.word_view.word.is_masked():
                    self.greeterboard.saved()
                    self.out_end_game(self.word_view.word.show(), greeter.OUT_MSG_WINNER)
            else:
                self.greeterboard.missed()
                self.out_end_turn(str(self.word_view.word), random.choice(greeter.OUT_MSG_COMPLAINTS))
                if not self.greeterboard.hangman.attempt:
                    self.out_end_game(self.word_view.word.show(), greeter.OUT_MSG_LOSER)
            self.greeterboard.update_gallows()
            self.keyboard.keys[letter.lower()].setEnabled(False)
        self.keyboard.keys['Space'].setFocus()

    def update_dynamic_texts(self, msg):
        """Updates all dynamic content of the game display

        It is usually at the end of a turn, a game or at the beginning.

        :param msg: a message to set at the word view
        """
        self.word_view.setText(msg)
        self.greeterboard.update_gallows()
        self.scoreboard.set_score(self.greeterboard.hangman.missed, self.greeterboard.hangman.attempt)
        self.progress_bar.set_value(word.MASK, word.MASK)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = GameWindow()
    app.exec_()
