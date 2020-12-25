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
    **functools**
        provides useful args addictions when delgating a method
    **PyQt5.***
        provides PyQt 5 GUI component essentials for the main window

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


class Keyboard(QtWidgets.QWidget):
    """This class puts in place a keyboard widget"""

    def __init__(self, parent):
        """Initialize the Keyboard while inheriting QWidget properties
        
        Also loads the UI from a .ui template file and populate a keys dictionnary for convenience. It is also
        setting the shorcut for every key.
        """
        super(Keyboard, self).__init__()
        uic.loadUi(i18n.KEYBOARD_LAYOUT, self)
        self.keys = {}
        for row in i18n.ALPHA_LAYOUT:
            for letter in row:
                self.keys[letter] = self.findChild(QtWidgets.QPushButton, f'Key_{letter.upper()}')
                self.keys[letter].setShortcut(getattr(QtCore.Qt, self.keys[letter].objectName()))
        self.keys['Space'] = self.findChild(QtWidgets.QPushButton, 'Key_Space')
        self.keys['Space'].setText(i18n.SPACE_KEY)

        # Looks like the order is important and like it is a bug in Qt
        #  that setting text after the shortcut voids the shortcut
        self.keys['Space'].setShortcut(QtCore.Qt.Key_Space)

    def connect_keys(self, play_turn, new_game):
        """Binds every keys pressed action to game methods.

        :param play_turn: method to play a turn
        :param new_game: method to set a new game
        """
        for k, v in self.keys.items():
            if k == 'Space':
                v.pressed.connect(new_game)
            else:
                v.pressed.connect(functools.partial(play_turn, v))

    def reset(self):
        """Reenables all the keys that were disable during a previous game

        It also sets the focus to the space bar
        """
        for k in self.keys.values():
            k.setEnabled(True)
        self.set_focus('Space')

    def set_focus(self, key_str):
        """Sets the focus to the specified key

        :param key_str: the name of the key where to set the focus
        """
        self.keys[key_str].setFocus()
