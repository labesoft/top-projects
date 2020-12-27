"""The game window of The Hangman Game
-----------------------------

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
    None
"""
__author__ = "Benoit Lapointe"
__date__ = "2020-12-18"
__copyright__ = "Copyright 2020, labesoft"

__version__ = "1.0.0"

import random
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut, QApplication

from hanggame import word, i18n
from hanggame.level import GameLevel
from hanggame.ui.login import Login


class GameWindow(QtWidgets.QMainWindow):
    """This class puts in place the base layout of the game window

    It will show The Hangman Game widgets
    """
    def __init__(self, name):
        """Initializes the game window setting all the boards to their initial values

        It also binds the keyboard and level combo box events to proper methods
        """
        super(GameWindow, self).__init__()
        uic.loadUi('game_window.ui', self)
        self.setWindowTitle(i18n.OUT_MSG_TITLE)
        self.name = name
        self.greeterboard.welcome_player(i18n.OUT_MSG_LUCK.format(self.name))
        self.scoreboard.set_labels()
        self.word_view.setText(i18n.OUT_MSG_NEW_GAME)
        self.init_game_metrics()
        self.keyboard.bind_keys(self.play_turn)
        self.keyboard.bind_space(self.start_game)
        self.scoreboard.bind(self.change_level)
        self.bind('Alt+F4', QApplication.instance().quit)
        self.show()

    def bind(self, seq, action):
        """Binds a shortcut sequence to an action

        :param seq: a str representation of the sequence
        :param action: the app method to connect to
        """
        quit_sc = QShortcut(QKeySequence(seq), self)
        # noinspection PyUnresolvedReferences
        quit_sc.activated.connect(action)

    def change_level(self):
        """Changes the level to the combo value and aborts the current game to restart a new one"""
        self.greeterboard.reset(GameLevel[self.scoreboard.current_level()], '')
        self.word_view.reveal_word()
        self.word_view.setText(i18n.OUT_MSG_NEW_GAME)
        self.init_game_metrics()

    def start_game(self):
        """Start a new game choosing a new word resetting all game components"""
        self.word_view.next_word()
        self.greeterboard.reset(msg=i18n.OUT_MSG_LUCK.format(self.name))
        self.keyboard.reset()
        self.init_game_metrics()

    def out_end_turn(self, end_msg):
        """Presents the states of the game to the player after a turn has ended

        :param w: the word revealed so far
        :param end_msg: the msg provided to end the turn
        """
        self.progress_bar.set_value(self.word_view.word, word.MASK)
        self.greeterboard.greets(end_msg)
        self.scoreboard.set_score(self.greeterboard.hangman.missed, self.greeterboard.hangman.attempt)
        self.word_view.update_word()

    def out_end_game(self, end_msg):
        """Presents the state of the game to the player after a game has ended

        :param w: the word revealed to the player
        :param end_msg: the msg provided to end the game
        :return:
        """
        self.greeterboard.greets(end_msg)
        self.word_view.reveal_word()

    def play_turn(self, letter):
        """Plays this cycle for each letter chosen by the player

        It tries to unmask a letter, but if it fails the player see one of his body part
        being hanged to the gallows until no parts are left which would loose the game.
        The goal is to reveal the whole word.
        :param letter: a letter to try
        """
        if self.word_view.word and self.greeterboard.hangman.attempt:
            if self.word_view.guess(letter.lower()):
                self.out_end_turn(random.choice(i18n.OUT_MSG_CONGRATS))
                if not self.word_view.is_masked():
                    self.greeterboard.saved()
                    self.out_end_game(i18n.OUT_MSG_WINNER)
            else:
                self.greeterboard.missed()
                self.out_end_turn(random.choice(i18n.OUT_MSG_COMPLAINTS))
                if not self.greeterboard.hangman.attempt:
                    self.out_end_game(i18n.OUT_MSG_LOSER)
            self.greeterboard.update_gallows()
            self.keyboard.keys[letter.lower()].setEnabled(False)
        self.keyboard.keys['Space'].setFocus()

    def init_game_metrics(self):
        """Initialize all dynamic content of the game display

        It is usually at the end of a turn, a game or at the beginning.

        :param msg: a message to set at the word view
        """
        self.greeterboard.update_gallows()
        self.scoreboard.set_score(self.greeterboard.hangman.missed, self.greeterboard.hangman.attempt)
        self.progress_bar.set_value(word.MASK, word.MASK)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = GameWindow(login.name.text())
        app.exec_()
