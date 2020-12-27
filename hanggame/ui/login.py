"""The login dialog of The Hangman Game
-------------------------------------

About this module
-----------------
The objective of this module is to create a dialog before The Hangman Game
starts that offers the player to enter his name.

File structure
--------------
*import*
    **PyQt5.***
        provides PyQt 5 GUI component essentials for the main window
"""

__author__ = "Benoit Lapointe"
__date__ = "2020-12-22"
__copyright__ = "Copyright 2020, labesoft"
__version__ = "1.0.0"

from PyQt5 import QtWidgets, uic

from hanggame import i18n


class Login(QtWidgets.QDialog):
    """The login page which will spawn before the game is loaded"""

    def __init__(self, hangman):
        """Initialize the Login while inheriting QtWidget properties

        Also loads the UI from a .ui template file
        """
        super(Login, self).__init__()
        uic.loadUi('login.ui', self)
        self.greeterboard.hangman = hangman
        self.greeterboard.welcome_player(i18n.IN_MSG_NAME)
        self.greeterboard.update_gallows()
        self.start.setText(i18n.START)
        self.start.clicked.connect(self.handle_login)
        self.setWindowTitle(i18n.OUT_MSG_TITLE)
        self.show()

    def handle_login(self):
        """Validate that some text has been entered in

        Otherwise the game will not begin.
        """
        if len(self.name.text()) != 0:
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self,
                i18n.OUT_MSG_ERROR,
                i18n.OUT_MSG_BAD_ENTRY
            )
