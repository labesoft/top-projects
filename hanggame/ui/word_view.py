"""The word view of The Hangman Game
---------------------------------------

About this module
-----------------
The objective of this module is to view the word to discover of The Hangman
Game using python. It uses innovative Python libraries such as PyQt5 which
helps to visually create the Ui representation of word and its actual state. It
could also display critical messages to the player.

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

from hanggame import i18n


class WordView(QtWidgets.QLabel):
    """This is the UI of the word that the player has do discover"""

    @property
    def word(self):
        """Gets the masked word each character spaced

        :return: the masked word for the ui
        """
        return ' '.join(list(str(self.__word)))

    @word.setter
    def word(self, w):
        """Sets the hangman word attribute

        :param w: the hangman word provided
        """
        self.__word = w

    def update_word(self):
        """Sets the text of the label with the current word state"""
        self.setText(self.word)

    def reveal_word(self):
        """Reveal the word and display the answer in the label"""
        w = self.__word.show()
        if w:
            self.setText(i18n.OUT_MSG_ANSWER.format(w))

    def next_word(self):
        """Chooses the next word and displays it"""
        self.__word.choose()
        self.setText(self.word)
