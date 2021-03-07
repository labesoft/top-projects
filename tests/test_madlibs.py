"""Test the MadLibs Game
-----------------------------

About this module
-----------------
This module is testing all the madlibs functions
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-07"
__copyright__ = "Copyright 2021, Benoit Lapointe"
__version__ = "1.0.0"

import io

from unittest import TestCase
from unittest.mock import call, patch

from madlibs.__main__ import (
    ADJECTIVE, ADVERB, ANIMAL_NAME, COLOR_NAME, ENTER_A_NAME, FOOD_NAME,
    INSECT_NAME,
    MAD1, MAD2,
    MAD3,
    PERSON_NAME, PIECE_OF_CLOTH_NAME,
    PLACE_NAME,
    PROFESSION_NAME, THING_NAME,
    VERB_IN_ING_FORM,
    VERB_NAME, madlib1, madlib2, madlib3
)


class MadLibsTests(TestCase):
    @patch('builtins.input', side_effect=[str(i) for i in range(8)])
    @patch('builtins.print')
    def test_madlib1(self, pyprint, pyinput):
        # Run test
        madlib1()

        # Evaluate test
        calls = [
            call(MAD1.format(7, 4, 5, 0, 1, 3, 2, 6))
        ]
        pyprint.assert_has_calls(calls)
        calls = [
            call(ANIMAL_NAME),
            call(PROFESSION_NAME),
            call(PIECE_OF_CLOTH_NAME),
            call(THING_NAME),
            call(ENTER_A_NAME),
            call(PLACE_NAME),
            call(VERB_IN_ING_FORM),
            call(FOOD_NAME)
        ]
        pyinput.assert_has_calls(calls)

    @patch('builtins.input', side_effect=[str(i) for i in range(10)])
    @patch('builtins.print')
    def test_madlib2(self, pyprint, pyinput):
        # Run test
        madlib2()

        # Evaluate test
        calls = [
            call(MAD2.format(*range(9), 8))
        ]
        pyprint.assert_has_calls(calls)
        calls = [
            call(ADJECTIVE),
            call(COLOR_NAME),
            call(THING_NAME),
            call(PLACE_NAME),
            call(PERSON_NAME),
            call(ADJECTIVE),
            call(INSECT_NAME),
            call(FOOD_NAME),
            call(VERB_NAME)
        ]
        pyinput.assert_has_calls(calls)

    @patch('builtins.input', side_effect=[str(i) for i in range(10)])
    @patch('builtins.print')
    def test_madlib3(self, pyprint, pyinput):
        # Run test
        madlib3()

        # Evaluate test
        calls = [
            call(MAD3.format(*range(10)))
        ]
        pyprint.assert_has_calls(calls)
        calls = [
            call(PERSON_NAME),
            call(COLOR_NAME),
            call(FOOD_NAME),
            call(ADJECTIVE),
            call(THING_NAME),
            call(PLACE_NAME),
            call(VERB_NAME),
            call(ADVERB),
            call(FOOD_NAME),
            call(THING_NAME)
        ]
        pyinput.assert_has_calls(calls)
