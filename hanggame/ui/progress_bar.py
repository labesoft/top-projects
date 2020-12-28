"""The progress bar of The Hangman Game$
-----------------------------

About this module
-----------------
The objective of this module is to view the progress the player has made so far
during The Hangman Game using Python. It uses innovative Python libraries such
as PyQt5 which helps to visually create the UI representation of the progress
during the game.

File structure
--------------
*import*
    **PyQt5.***
        provides PyQt 5 GUI component essentials for the main window
"""

__author__ = "Benoit Lapointe"
__date__ = "2020-12-18"
__copyright__ = "Copyright 2020, labesoft"
__version__ = "1.0.0"

from PyQt5 import QtWidgets

from hanggame.word import MASK_STR


class ProgressBar(QtWidgets.QProgressBar):
    """This is the progress bar usable for The Hangman Game"""

    def set_value(self, w):
        """The progress accomplished based on the completion of the word

        :param w: the word to evaluate
        """
        value = int(100 * (1 - w.count(MASK_STR) / len(w.replace(' ', ''))))
        self.setValue(value)
