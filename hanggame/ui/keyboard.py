"""The keyboard of The Hangman Game
--------------------------------

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
    **ALPHA_LAYOUT**
        Layout of the keyboard. Each string represents a row of keys
"""
__author__ = "Benoit Lapointe"
__date__ = "2020-12-18"
__copyright__ = "Copyright 2020, labesoft"

__version__ = "1.0.0"

import functools

from PyQt5 import QtCore, QtWidgets, uic

from hanggame import i18n

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
        self.keys['Space'].setShortcut(QtCore.Qt.Key_Space)
        self.keys['Space'].setText(i18n.SPACE_KEY)

    def bind_keys(self, play_turn):
        """Binds every letter keys to a player's guess during the game.

        :param play_turn: method to play a turn
        """
        for k, v in self.keys.items():
            if k != 'Space':
                v.pressed.connect(functools.partial(play_turn, v.text()))

    def bind_space(self, new_game):
        """Binds the space bar to start a new game.

        :param new_game: method to start a new game
        """
        self.keys['Space'].pressed.connect(new_game)
        self.keys['Space'].setFocus()

    def reset(self):
        """Reenables all the keys that were disable during a previous game

        It also sets the focus to the space bar
        """
        for k in self.keys.values():
            k.setEnabled(True)
        self.keys['Space'].setFocus()



