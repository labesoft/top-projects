"""The greeterboard of The Hangman Game$
-----------------------------

About this module
-----------------
The objective of this module is to view most of the messages sent to the player
of The Hangman Game using Python. It uses innovative Python libraries such as
PyQt5 which helps to visually create the UI representation of the welcome
title, the hang state and the greetings

File structure
--------------
*import*
    **PyQt5**
        provides PyQt 5 GUI component essentials for the main window
"""

__author__ = "Benoit Lapointe"
__date__ = "2020-12-18"
__copyright__ = "Copyright 2020, labesoft"
__version__ = "1.0.0"

from PyQt5 import QtWidgets, uic

from hanggame import i18n


class Greeterboard(QtWidgets.QWidget):
    """UI representation of most of the messages intended to the player"""

    def __init__(self, parent):
        """Initialize the Greeterboard while inheriting QWidget properties
        
        Also loads the UI from a .ui template file
        """
        super(Greeterboard, self).__init__()
        self.parent = parent
        uic.loadUi('greeterboard.ui', self)

    def greets(self, msg):
        """Greets the player with a positive comment

        :param msg: the msg presented to the player
        """
        self.greeter.setText(msg)

    def missed(self):
        """Computes the missed attempt and draw the hangman consequently"""
        self.hangman.missed += 1
        self.hangman.draw()

    def reset(self, level=None, msg=''):
        """Resets the hangman to its initial value

        :param level: the level played in the game
        :param msg: the message presented to the player after the reset
        """
        self.hangman.reset(level)
        self.greets(msg)

    def update_gallows(self):
        """Presents the current status of the gallows"""
        self.gallows.setText(str(self.hangman))

    def welcome_player(self, msg):
        """Welcomes the players in the game with a hanged man greetings

        :param msg: the message to greets the player
        """
        self.welcome_title.setText(i18n.OUT_MSG_WELCOME)
        self.hangman.draw(hanged=True)
        self.greets(msg)
