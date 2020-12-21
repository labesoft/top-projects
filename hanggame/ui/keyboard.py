"""The keyboard of The Hangman Game$
-----------------------------

About this Project
------------------
The objective of this project is to recreate The Hangman Game that a user could
play interactively by attempting to unmask a word one letter at a time using a
limited number of attempts without being hanged by the hangman.

Project structure
-----------------
*hanggame.ui/*
    **keyboard.py**:
        The keyboard of The Hangman Game
    **keyboard.ui**:
        The keyboard design of The Hangman Game

About this module
-----------------
The objective of this module is to view the keyboard of The Hangman Game using
python. It uses innovative Python libraries such as PyQt5 which helps to
visually create the keyboard itself that must be easily usable and be able to
change its state during the course of the game (like blocking a key already
used).

File structure
--------------
*import*
    **PyQt5: QtCore, QtGui, QtWidgets, uic**
        Useful modules for a PyQt module

*constant*

"""
__author__ = "Benoit Lapointe"
__date__ = "2020-12-18"
__copyright__ = "Copyright 2020, labesoft"

__version__ = "1.0.0"

import functools

from PyQt5 import QtCore, QtWidgets, uic


ALPHA_LAYOUT = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']


class Keyboard(QtWidgets.QWidget):
    """This class puts in place a keyboard widget"""

    def __init__(self, parent):
        """Initialize the Keyboard while inheriting QWidget properties
        
        Also loads the UI from a .ui template file and populate a keys dictionnary for convenience. It is also
        setting the shorcut for every key.
        """
        super(Keyboard, self).__init__()
        uic.loadUi('keyboard.ui', self)
        self.keys = {}
        for row in ALPHA_LAYOUT:
            for letter in row:
                self.keys[letter] = self.findChild(QtWidgets.QPushButton, f'Key_{letter.upper()}')
                self.keys[letter].setShortcut(getattr(QtCore.Qt, self.keys[letter].objectName()))
        self.keys['Space'] = self.findChild(QtWidgets.QPushButton, 'Key_Space')
        self.keys['Space'].setShortcut(getattr(QtCore.Qt, 'Key_Space'))

    def bind(self, new_game, play_turn):
        """Binds every letter keys to a player's turn in the game.

        Also the space bar is used to start a new game.

        :param new_game: func to start a new game
        :param play_turn: func to play a turn
        """
        for k, v in self.keys.items():
            if k == 'Space':
                # New game
                v.pressed.connect(new_game)
            else:
                # 1 guess
                v.pressed.connect(functools.partial(play_turn, v.text()))

    def reset(self):
        """Reenables all the keys that were disable during a previous game

        It also sets the focus to the space bar
        """
        for k in self.keys.values():
            k.setEnabled(True)
        self.keys['Space'].setFocus()



