"""The drawing logic of the hangman's gallows
------------------------------------------

About this module
-----------------
The objective of this module is to draw a hanged man one part at a time.
The drawing is intended for the console and represents on how many time the
player missed. Based on its game level, the player that will reach its max
attempts allowed will be hanged (and Hallowed be thy name).

File structure
--------------
*import*
    **hanggame.level.GameLevel**
        provide acces to all game levels used during the drawing of the hanged man
*constant*
    **GALLOWS**
        parts list of the gallows without the hanged man
    **PART_* or PART_*_HANGED***
        parts of the gallows with the hanged man parts
    **PART_* or PART_*_SAVED**
        parts of the gallows with the saved man parts
    **ZERO**
        standard int 0 constant
"""
from hanggame.level import GameLevel


GALLOWS = [
    "    _____",
    "   |       |",
    "   |       |",
    "   |       |",
    "   |",
    "   |",
    "   |",
    "__|__"
]
IMAGE_STRING_SEP = "\n"
PART_ARM_LEFT = "   |      /|"
PART_ARMS_HANGED = "   |      /|\\"
PART_BODY = "   |       |"
PART_HEAD_HANGED = "   |       O"
PART_HEAD_SAVED = "   |     \\O/"
PART_LEG_LEFT = "   |      /"
PART_LEGS_HANGED = "   |      / \\"
PART_LEGS_SAVED = "__|__   / \\"
ZERO = 0


class Hangman:
    """The Hangman draws the state of the hanged player"""
    def __init__(self, level=GameLevel.BEGINNER):
        """Initializes the players gallows

        Which include the maximum attempts allowed. The GALLOWS is cloned to
        prevent operating changes on the original list.

        :param level: current player's game level
        """
        self.max_attempt = level.value
        self.missed = ZERO
        self.gallows = list(GALLOWS)

    def __str__(self):
        """Provides the string image of the current hanged state of a player

        :return: an image of a hangman
        """
        return IMAGE_STRING_SEP.join(self.gallows)

    @property
    def attempt(self):
        """Gets the number of guess attempts remaining

        :return: the number of attempt(s) remaining
        """
        return self.max_attempt - self.missed

    @property
    def missed(self):
        """Gets the number of missed attempts

        :return: the number of attempts missed
        """
        return self.__missed

    @missed.setter
    def missed(self, missed: int):
        """Set last missed attempts to the current missed count

        :param missed: missed attempt(s) to add
        """
        if not hasattr(self, '_Hangman__missed') or self.missed < self.max_attempt or missed == 0:
            self.__missed = missed

    def draw(self, hanged=False, saved=False):
        """Change the hangman drawing to the current state

        The current state is based on the player misses related to max attempts
        allowed. It is also possible to draw a complete man on the fly totally
        unrelated with the current state which could be hanged or saved

        :param saved: if True, the player wins and is happy to be safe. Otherwise,
         False will fall back to the current state
        :param hanged: if True, draw a complete hanged man on the fly. Otherwise,
         False will fall back to the current state.
        """
        self.gallows = list(GALLOWS)
        if saved:
            self.gallows[5] = PART_HEAD_SAVED
            self.gallows[6] = PART_BODY
            self.gallows[7] = PART_LEGS_SAVED
        elif self.missed == self.max_attempt or hanged:
            self.gallows[4] = PART_HEAD_HANGED
            self.gallows[5] = PART_ARMS_HANGED
            self.gallows[6] = PART_LEGS_HANGED
        elif self.missed == self.max_attempt - GameLevel.EXTREME.value:
            self.gallows[4] = PART_HEAD_HANGED
            self.gallows[5] = PART_ARMS_HANGED
            self.gallows[6] = PART_LEG_LEFT
        elif self.missed == self.max_attempt - GameLevel.INFERNO.value:
            self.gallows[4] = PART_HEAD_HANGED
            self.gallows[5] = PART_ARMS_HANGED
        elif self.missed == self.max_attempt - GameLevel.ELITE.value:
            self.gallows[4] = PART_HEAD_HANGED
            self.gallows[5] = PART_ARM_LEFT
        elif self.missed == self.max_attempt - GameLevel.PRO.value:
            self.gallows[4] = PART_HEAD_HANGED
            self.gallows[5] = PART_BODY
        elif self.missed == self.max_attempt - GameLevel.INTERMEDIARY.value:
            self.gallows[4] = PART_HEAD_HANGED

    def reset(self, level=None):
        """Remove the hanged player from the gallows"""
        self.missed = ZERO
        if level:
            self.max_attempt = level.value
        self.draw()
