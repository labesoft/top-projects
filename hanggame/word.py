"""The word handling logic of The Hangman Game
-----------------------------------

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
    **EMPTY_***
        the empty constants
    **MASK**
        the symbol used to mask a letter
    **DEFAULT_WORDS_FILEPATH**
        the default word dictionary
"""
import random
from os.path import dirname
from pathlib import Path

EMPTY_MASK = {}
EMPTY_WORD = ''
MASK = '_'
DEFAULT_WORDS_FILEPATH = Path(dirname(__file__), 'words_alpha.txt')


class Word:
    """The representation of a word for The Hangman Game"""
    def __init__(self, words_file=DEFAULT_WORDS_FILEPATH):
        """Initializes the words bank without choosing one yet

        :param words_file: a file containing all available words
        """
        self.word_bank = self.load_words(words_file)
        self.__word = EMPTY_WORD
        self.__mask = EMPTY_MASK

    def __str__(self):
        """Generates a masked string of the word

        :return: the word masked
        """
        mask_table = str.maketrans(self.__mask)
        return self.__word.translate(mask_table)

    @staticmethod
    def load_words(words_file=DEFAULT_WORDS_FILEPATH):
        """Loads all words from a file with more than 2 letters

        :param words_file: the path of the file to load
        :return: a list with all the words loaded
        """
        with open(words_file) as f:
            all_words = f.readlines()
        return [w.strip('\n') for w in all_words]

    @property
    def word_bank(self):
        """Gets the current list of words"""
        return self.__word_bank

    @word_bank.setter
    def word_bank(self, words):
        """Sets the current list of words"""
        self.__word_bank = [w for w in words if len(w) > 2 and w.isalpha()]

    @property
    def unmasked_set(self):
        """Gets a set with the letters that have been unmasked so far

        :return: a set of unmasked letters from the word
        """
        return set(str(self).replace(MASK, ''))

    def choose(self):
        """Chooses a new word from the word bank and assign it"""
        self.show()
        self.__word = random.choice(self.__word_bank)
        self.__mask = dict.fromkeys(set(self.__word), MASK)

    def is_masked(self):
        """Tells if the word still contains masked letters

        :return: True if 1 or more letter are masked, False otherwise
        """
        return bool(self.__mask)

    def is_unmasked(self, letter):
        """Tells if a letter has already been unmasked

        :return: True if the letter has been unmasked, False otherwise
        """
        return letter in self.unmasked_set

    def show(self):
        """Unmasks all the letters of the word and destroy it

        :return: the word with all letters unmasked
        """
        result = self.__word
        self.__word = EMPTY_WORD
        self.__mask = EMPTY_MASK
        return result

    def unmask(self, letter):
        """Tries to unmask a letter and tells if it worked

        :param letter: the letter to unmask
        :return: True if the word contains the letter and was not unmasked already,
                  False otherwise
        """
        was_unmask = self.is_unmasked(letter)
        if letter in self.__mask:
            del self.__mask[letter]
        return letter in self.__word and not was_unmask
