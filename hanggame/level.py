"""The game levels of The Hangman Game
-----------------------------------

About this module
-----------------
This module enumerates all the levels of The Hangman Game. Each level is also
linked to a predetermined number of attempts.

File structure
--------------
*import*
    **enum.Enum**
        the parent which defines the rules to build enum classes

*class*
    **GameLevel(Enum)**
        'The Hangman Game levels defining their maximum number of attempts'
"""
from enum import Enum
from types import DynamicClassAttribute

from hanggame import i18n


class GameLevel(Enum):
    """The Hangman Game levels defining their maximum number of attempts"""
    BEGINNER = 6
    INTERMEDIARY = 5
    PRO = 4
    ELITE = 3
    INFERNO = 2
    EXTREME = 1

    @DynamicClassAttribute
    def translated_name(self):
        """The translatable name of an enum"""
        return i18n.LEVELS[self.name]
