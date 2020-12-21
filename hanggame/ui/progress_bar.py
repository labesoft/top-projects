"""The progress bar of The Hangman Game$
-----------------------------

About this Project
------------------
The objective of this project is to recreate The Hangman Game that a user could
play interactively by attempting to unmask a word one letter at a time using a
limited number of attempts without being hanged by the hangman.

Project structure
-----------------
*hanggame.ui/*
    **progress_bar.py**:
        The progress bar UI design of The Hangman Game
    **progress_bar.ui**:
        The progress bar of The Hangman Game
        
About this module
-----------------
The objective of this module is to view the progress the player has made so far
during The Hangman Game using Python. It uses innovative Python libraries such
as PyQt5 which helps to visually create the UI representation of the progress
during the game.

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


class ProgressBar(QtWidgets.QProgressBar):
    """This is the progress bar usable for The Hangman Game"""
    def set_value(self, w, mask):
        """Set the current value of the progress based on the completion of the word

        :param w: the word to evaluate
        :param mask: the letter used to mask the word
        """
        value = int(100 * (1 - str(w).count(mask) / len(w)))
        self.setValue(value)

