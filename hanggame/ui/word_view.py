"""The word UI of The Hangman Game$
-----------------------------

About this Project
------------------
The objective of this project is to recreate The Hangman Game that a user could
play interactively by attempting to unmask a word one letter at a time using a
limited number of attempts without being hanged by the hangman.

Project structure
-----------------
*hanggame/*
    **word_view.py**:
        The word UI design of The Hangman Game
    **word_view.ui**:
        The word UI of The Hangman Game
        
About this module
-----------------
The objective of this module is to view the word to discover of The Hangman
Game using python. It uses innovative Python libraries such as PyQt5 which
helps to visually create the Ui representation of word and its actual state. It
could also display critical messages to the player.

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

from PyQt5 import QtWidgets

from hanggame.word import Word


class WordView(QtWidgets.QLabel):
    """This is the UI of the word that the player has do discover"""

    def __init__(self, parent):
        """Initialize the Word while inheriting QLabel properties
        
        Also loads the UI from a .ui template file
        """
        super(WordView, self).__init__()
        self.word = Word()
        self.word.load_words()
        self.setText(' '.join(list(str(self.word))))
