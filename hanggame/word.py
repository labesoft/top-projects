"""The word handling logic of The Hangman Game
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
    **game.py**:
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
This module handle the word behavior of The Hangman Game. It choose a word and
then, masks and unmasks the letters of the word. It is also designed to reveal
a word only once making it impossible to undo when this is done.

File structure
--------------
*import*
    **random**
        provides a way to generate a pseudo random choice of a word in a list
    **os.path.dirname**
        gives the directory path of a file
    **pathlib.Path**
        provides a OS agnostic way of handling paths

*constant*
    **MASK**
        the symbol used to mask a letter
    **DEFAULT_WORDS_FILE**
        the default word dictionary

*class*
    **Word**
        'The representation of a word for The Hangman Game'
    **__init__(self, words_file=DEFAULT_WORDS_FILE)**
        'Initializes the words bank without choosing one yet'
    **__str__(self)**
        'Generates a masked string of the word'
    **reveal(self)**
        'Unmasks all the letters of the word and destroy it'
    **unmask_set(self)**
        'Gets a set with the letters that have been unmasked so far'
    **choose(self)**
        'Chooses a new word from the word bank and assign it'
    **is_mask(self)**
        'Tells if the word still contains masked letters'
    **is_unmask(self, letter)**
        'Tells if a letter has been unmasked'
    **unmask(self, letter)**
        'Unmasked a letter if the word contains it'
"""
import random
from os.path import dirname
from pathlib import Path


MASK = '_'
DEFAULT_WORDS_FILE = Path(dirname(__file__), 'words_alpha.txt')


class Word:
    """The representation of a word for The Hangman Game"""
    def __init__(self, words_file=DEFAULT_WORDS_FILE):
        """Initializes the words bank without choosing one yet

        :param words_file: a file containing all available words
        """
        with open(words_file) as f:
            all_words = f.readlines()
        self.__word_bank = [w.strip('\n') for w in all_words if len(w.strip('\n')) > 2]
        self.__word = ''
        self.__mask = {}

    def __str__(self):
        """Generates a masked string of the word

        :return: the word masked
        """
        mask_table = str.maketrans(self.__mask)
        return self.__word.translate(mask_table)

    @property
    def reveal(self):
        """Unmasks all the letters of the word and destroy it

        :return: the word unmasked
        """
        result = self.__word
        self.__word = ''
        self.__mask = {}
        return result

    @property
    def unmask_set(self):
        """Gets a set with the letters that have been unmasked so far

        :return: a set of unmasked letters from the word
        """
        return set(str(self).replace(MASK, ''))

    def choose(self):
        """Chooses a new word from the word bank and assign it"""
        self.__word = random.choice(self.__word_bank)
        self.__mask = dict.fromkeys(set(self.__word), MASK)

    def is_mask(self):
        """Tells if the word still contains masked letters

        :return: True if 1 or more letter are masked, False otherwise
        """
        return bool(self.__mask)

    def is_unmask(self, letter):
        """Tells if a letter has been unmasked

        :return: True if the letter has been unmasked, False otherwise
        """
        return letter in self.unmask_set

    def unmask(self, letter):
        """Unmasked a letter if the word contains it

        :param letter: the letter to unmask
        :return: True if the word contains the letter and was not unmasked already,
                  False otherwise
        """
        was_unmask = self.is_unmask(letter)
        if letter in self.__mask:
            del self.__mask[letter]
        return letter in self.__word and not was_unmask
