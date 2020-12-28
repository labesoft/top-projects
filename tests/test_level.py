"""The tests for level.py of The Hangman Game
-----------------------------------------

About this module
-----------------
The objective of this module is to test the level module
"""

__author__ = "Benoit Lapointe"
__date__ = "2020-12-18"
__copyright__ = "Copyright 2020, labesoft"
__version__ = "1.0.0"

from unittest import TestCase

from hanggame import i18n
from hanggame.level import GameLevel


class TestGameLevel(TestCase):
    def test_level_beginner(self):
        """Tests the max attempts of a beginner is 6"""
        # Evaluate test
        self.assertEqual(GameLevel.BEGINNER.value, 6)
        self.assertEqual(GameLevel.BEGINNER.translated_name,
                         i18n.LEVELS['BEGINNER'])

    def test_level_intermediary(self):
        """Tests the max attempts of a intermediary is 5"""
        # Evaluate test
        self.assertEqual(GameLevel.INTERMEDIARY.value, 5)
        self.assertEqual(GameLevel.INTERMEDIARY.translated_name,
                         i18n.LEVELS['INTERMEDIARY'])

    def test_level_pro(self):
        """Tests the max attempts of a pro is 4"""
        # Evaluate test
        self.assertEqual(GameLevel.PRO.value, 4)
        self.assertEqual(GameLevel.PRO.translated_name,
                         i18n.LEVELS['PRO'])

    def test_level_elite(self):
        """Tests the max attempts of an elite is 3"""
        # Evaluate test
        self.assertEqual(GameLevel.ELITE.value, 3)
        self.assertEqual(GameLevel.ELITE.translated_name,
                         i18n.LEVELS['ELITE'])

    def test_level_inferno(self):
        """Tests the max attempts of an inferno is 2"""
        # Evaluate test
        self.assertEqual(GameLevel.INFERNO.value, 2)
        self.assertEqual(GameLevel.INFERNO.translated_name,
                         i18n.LEVELS['INFERNO'])

    def test_level_extreme(self):
        """Tests the max attempts of an extreme is 1"""
        # Evaluate test
        self.assertEqual(GameLevel.EXTREME.value, 1)
        self.assertEqual(GameLevel.EXTREME.translated_name,
                         i18n.LEVELS['EXTREME'])
