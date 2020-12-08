"""The game levels of The Hangman Game
-----------------------------------

About this Project
------------------
The objective of this project is to recreate The Hangman Game that a user could
play interactively by attempting to unmask a word one letter at a time using a
limited number of attempts without being hanged by the hangman.

Project structure
-----------------
*alarm/*
    **__main__.py**:
        The application of The Hangman Game
    **game.py**:
        The play logic of The Hangman Game
    **greeter.py**:
        The greeter of The Hangman Game
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


class GameLevel(Enum):
    """The Hangman Game levels defining their maximum number of attempts"""
    BEGINNER = 6
    INTERMEDIARY = 5
    PRO = 4
    ELITE = 3
    INFERNO = 2
    EXTREME = 1
