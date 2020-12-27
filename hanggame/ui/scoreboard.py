"""The scoreboard of The Hangman Game$
-----------------------------

About this module
-----------------
The objective of this module is to view the score in real time during The
Hangman Game using Python. It uses innovative Python libraries such as PyQt5
which helps to visually create the UI representation of the live score during
the game.

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


from PyQt5 import QtCore, QtWidgets, uic

import hanggame.i18n
from hanggame.level import GameLevel


class Scoreboard(QtWidgets.QWidget):
    """This is the view of the game score regrouped in one widget."""

    def __init__(self, parent):
        """Initializes the Scoreboard while inheriting QWidget properties
        
        Also loads the UI from a .ui template file
        """
        super(Scoreboard, self).__init__()
        uic.loadUi('scoreboard.ui', self)
        self.level_combo.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.level_combo.lineEdit().setReadOnly(True)
        self.level_name_map = {level.translated_name: level.name for level in GameLevel}
        self.level_combo.addItems([level for level in self.level_name_map])

    def bind(self, level_changed):
        """Connects the combo selection to the level settings of the game

        :param level_changed: func that set the new level selected
        """
        self.level_combo.activated.connect(level_changed)

    def set_labels(self):
        """Sets all the labels of the scoreboard

        This would happen one time only, before the game starts
        """
        self.level_label.setText(hanggame.i18n.OUT_MSG_LEVEL)
        self.remaining_label.setText(hanggame.i18n.OUT_MSG_NB_ATTEMPT.format(''))
        self.missed_label.setText(hanggame.i18n.OUT_MSG_ERROR)

    def set_score(self, missed: int, attempt: int):
        """Sets the score at different steps during the game

        :param missed: how many missed shot
        :param attempt: how many attempt remaining
        """
        self.missed_nb.setText(str(missed))
        self.remaining_nb.setText(str(attempt))

    def current_level(self):
        """Returns the level name currently selected in the combo

        The name returned is also translated in the appropriate locale.
        """
        return self.level_name_map[self.level_combo.currentText()]
