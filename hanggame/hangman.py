"""The drawing logic of the hangman's gallows
-----------------------------

About this Project
------------------
The objective of this project is to recreate The Hangman Game that a user could
play interactively trying to guess a word with a limited number of guess attempts
depending on his game level.

Project structure
-----------------
*alarm/*
    **__main__.py**:
        The application of The Hangman Game
    **game.py**:
        The play rules of The Hangman Game
    **hangman.py**:
        The drawing logic of the hangman on the gallows
    **level.py**:
        The game levels of The Hangman Game
    **word.py**:
        The word handling logic of The Hangman Game
    **words_alpha.txt**
        The words dictionary provided with The Hangman Game

About this module
-----------------
The objective of this module is to draw a hanged man one part at a time.
The drawing is based on how many time the player missed versus its game level.
The player that will reach its max attempts allowed will then be drewn hanged.

File structure
--------------
*import*
    **hanggame.level.GameLevel**
        provide acces to all game levels used during the drawing of the hanged man
*constant*
    **GALLOWS**
        parts list of the gallows without the hanged man
    **GALLOWS_***
        parts of the gallows with the hanged man parts
*class*
    **Hangman**
        'The Hangman draws the state of the hanged player'
    **__init__(self, level)**
        'Initialize the player hanged state'
    **__str__(self)**
        'Provides the string image of the current hanged state of a player'
    **attempt(self)**
        'The getter of the number of guess attempts remaining'
    **missed(self)**
        'The getter of missed counts which is a private attribute'
    **draw(self, hanged=False)**
        'Change the hangman drawing to the current state'
    **reset(self)**
        'Remove the hanged player from the gallows'
"""
from hanggame.level import GameLevel

GALLOWS = [
    "\t   _____",
    "\t  |     |",
    "\t  |     |",
    "\t  |     |",
    "\t  |",
    "\t  |",
    "\t  |",
    "\t__|__"
]
GALLOWS_HEAD = "\t  |     O"
GALLOWS_BODY = "\t  |     |"
GALLOWS_ARM_LEFT = "\t  |    /|"
GALLOWS_ARMS = "\t  |    /|\\"
GALLOWS_LEG_LEFT = "\t  |    /"
GALLOWS_LEGS = "\t  |    / \\"
WINNER_HEAD = "\t  |    \\O/"
WINNER_LEGS = "\t__|__  / \\"


class Hangman:
    """The Hangman draws the state of the hanged player"""
    def __init__(self, level=GameLevel.BEGINNER):
        """Initialize the player hanged state

        Which include the maximum attempts allowed, the count of missed
        attempts and the hanged state drawing. The GALLOWS is cloned to
        prevent operating changes on the original list.

        :param level: current player's game level
        """
        self.max_attempt = level.value
        self.__missed_count = 0
        # Cloning (with list()) the GALLOWS list in order to keep the original list intact
        self.gallows = list(GALLOWS)

    def __str__(self):
        """Provides the string image of the current hanged state of a player

        :return: an image of a hangman
        """
        return "\n".join(self.gallows)

    @property
    def attempt(self):
        """The getter of the number of guess attempts remaining

        :return: the number of attempt(s) remaining
        """
        return self.max_attempt - self.missed

    @property
    def missed(self):
        """The getter of missed counts which is a private attribute

        :return: the number of attempts missed
        """
        return self.__missed_count

    @missed.setter
    def missed(self, increment: int):
        """Add missed attempts number defined by the increment

        :param increment: missed attempt(s) to add
        """
        self.__missed_count += increment

    def draw(self, hanged=False, winner=False):
        """Change the hangman drawing to the current state

        The current state is based on the player misses related to max attempts
        allowed. It is also possible to draw a complete hanged man on the fly
        unrelated with the current state.

        :param hanged: if True, draw a complete hanged man on the fly. Otherwise,
         False will draw the current hanged state.
        """
        self.gallows = list(GALLOWS)
        if winner:
            self.gallows[5] = WINNER_HEAD
            self.gallows[6] = GALLOWS_BODY
            self.gallows[7] = WINNER_LEGS
        elif self.__missed_count == self.max_attempt or hanged:
            self.gallows[4] = GALLOWS_HEAD
            self.gallows[5] = GALLOWS_ARMS
            self.gallows[6] = GALLOWS_LEGS
        elif self.__missed_count == self.max_attempt - GameLevel.EXTREME.value:
            self.gallows[4] = GALLOWS_HEAD
            self.gallows[5] = GALLOWS_ARMS
            self.gallows[6] = GALLOWS_LEG_LEFT
        elif self.__missed_count == self.max_attempt - GameLevel.INFERNO.value:
            self.gallows[4] = GALLOWS_HEAD
            self.gallows[5] = GALLOWS_ARMS
        elif self.__missed_count == self.max_attempt - GameLevel.ELITE.value:
            self.gallows[4] = GALLOWS_HEAD
            self.gallows[5] = GALLOWS_ARM_LEFT
        elif self.__missed_count == self.max_attempt - GameLevel.PRO.value:
            self.gallows[4] = GALLOWS_HEAD
            self.gallows[5] = GALLOWS_BODY
        elif self.__missed_count == self.max_attempt - GameLevel.INTERMEDIARY.value:
            self.gallows[4] = GALLOWS_HEAD

    def reset(self):
        """Remove the hanged player from the gallows"""
        self.__missed_count = 0
        self.draw()
