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
    **random**
        provides a random choice of congrats/complains message
    **PyQt5.***
        provides PyQt 5 GUI component essentials for the main window
"""

__author__ = "Benoit Lapointe"
__date__ = "2020-12-18"
__copyright__ = "Copyright 2020, labesoft"
__version__ = "1.0.0"

import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut, QApplication

from hanggame import i18n
from hanggame.game import HangGame
from hanggame.hangman import Hangman, SPACE_STR
from hanggame.level import GameLevel
from hanggame.ui.login import Login
from hanggame.word import MASK_STR


class Window(QtWidgets.QMainWindow):
    """This class puts in place the base layout of the game window

    It will show The Hangman Game widgets
    """

    def __init__(self, player_name, word, hangman):
        """Initializes the game window setting all the boards to initial values

        It also binds the keyboard and level combo box events to proper methods

        :param player_name: the name of the player string
        :param word: the Word object of the game
        :param hangman: the Hangman object of the game
        """
        super(Window, self).__init__()
        uic.loadUi('window.ui', self)
        self.setWindowTitle(i18n.OUT_MSG_TITLE)
        self.player_name = player_name
        self.greeterboard.hangman = hangman
        self.scoreboard.hangman = hangman
        self.word_view.word = word
        self.play_again = True

    def prepare(self, level):
        """Prepares UI sub component to the first game startup

        :param level: the level chosen at the beginning
        """
        self.greeterboard.welcome_player(
            i18n.OUT_MSG_LUCK.format(self.player_name)
        )
        self.scoreboard.set_labels()
        self.scoreboard.set_level(level)
        self.word_view.setText(i18n.OUT_MSG_NEW_GAME)
        self.init_game_metrics()

    def accept_letter(self, key):
        """Gets the letter from the key typed by the user

        It also disable it and reset the focus to the space bar

        :param key: the key typed by the player
        :return: the letter took from the key
        """
        letter = key.text()
        key.setEnabled(False)
        self.keyboard.set_focus('Space')
        return letter.lower()

    def ask_play_again(self):
        """Ask the player to play again

        This is not useful in the GUI but needs to be part of the interface for
        the game to work properly

        :return: True
        """
        return self.play_again

    def connect_all(self, play_turn):
        """Connects all actions

        It includes exit, play a turn, start a game, change level

        :param play_turn: plays one turn from the game
        """
        # Exit
        quit_sc = QShortcut(QKeySequence('Alt+F4'), self)
        # noinspection PyUnresolvedReferences
        quit_sc.activated.connect(QApplication.instance().quit)

        # Play turn, start game
        self.keyboard.connect_keys(play_turn, self.start_game)

        # Levels
        self.scoreboard.connect_combo(self.change_level)

    def change_level(self):
        """Changes the level to the combo value and aborts the current game

        It then waits to restart a new one.
        """
        new_level = GameLevel[self.scoreboard.current_level]
        self.greeterboard.reset(level=new_level, msg='')
        self.end_game(i18n.OUT_MSG_NEW_GAME)
        self.init_game_metrics()

    def end_game(self, end_msg):
        """Presents the state of the game to the player after a game has ended

        :param end_msg: the msg provided to end the game
        """
        self.word_view.reveal_word()
        self.greeterboard.update_gallows()
        self.greeterboard.greets(end_msg)

    def end_turn(self, end_msg):
        """Presents the states of the game to the player after a turn has ended

        :param end_msg: the msg provided to end the turn
        """
        self.progress_bar.set_value(self.word_view.word)
        self.greeterboard.greets(end_msg)
        self.scoreboard.update_score()
        self.word_view.update_word()
        self.greeterboard.update_gallows()

    def init_game_metrics(self):
        """Initialize all dynamic content of the game display

        It is usually at the end of a turn, a game or at the beginning.
        """
        self.greeterboard.update_gallows()
        self.scoreboard.update_score()
        self.progress_bar.set_value(MASK_STR)

    def start_game(self):
        """Start a new game choosing a new word resetting all game components

        This method is connected to the space bar
        """
        self.word_view.next_word()
        self.greeterboard.reset(msg=i18n.OUT_MSG_LUCK.format(self.player_name))
        self.keyboard.reset()
        self.init_game_metrics()


def main(level, word):
    """Launch the GUI game

    :param level: the level chosen on the cli
    :param word: the word initialized in the __main__
    """
    hangman = Hangman(
        level=level,
        left_spaces=SPACE_STR * 10,
        middle_spaces=SPACE_STR * 6,
        left_foot=SPACE_STR * 7,
        right_foot=SPACE_STR * 3
    )
    app = QtWidgets.QApplication(sys.argv)
    login = Login(hangman)
    if login.exec_() == QtWidgets.QDialog.Accepted:
        ui = Window(login.name.text(), word, hangman)
        game = HangGame(level, word, hangman, ui)
        ui.connect_all(game.play_turn)
        ui.prepare(level)
        ui.show()
        app.exec_()
