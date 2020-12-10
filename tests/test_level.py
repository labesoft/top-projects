"""The tests for level.py of The Hangman Game
-----------------------------------------

About this Project
------------------
The objective of this project is to recreate The Hangman Game that a user could
play interactively by attempting to unmask a word one letter at a time using a
limited number of attempts without being hanged by the hangman.

About this module
-----------------
The objective of this module is to test the level module
"""
from unittest import TestCase

from hanggame.level import GameLevel


class TestGameLevel(TestCase):
    def test_level_beginner(self):
        """Tests the max attempts of a beginner is 6"""
        # Evaluate test
        self.assertEqual(GameLevel.BEGINNER.value, 6)

    def test_level_intermediary(self):
        """Tests the max attempts of a intermediary is 5"""
        # Evaluate test
        self.assertEqual(GameLevel.INTERMEDIARY.value, 5)

    def test_level_pro(self):
        """Tests the max attempts of a pro is 4"""
        # Evaluate test
        self.assertEqual(GameLevel.PRO.value, 4)

    def test_level_elite(self):
        """Tests the max attempts of an elite is 3"""
        # Evaluate test
        self.assertEqual(GameLevel.ELITE.value, 3)

    def test_level_inferno(self):
        """Tests the max attempts of an inferno is 2"""
        # Evaluate test
        self.assertEqual(GameLevel.INFERNO.value, 2)

    def test_level_extreme(self):
        """Tests the max attempts of an extreme is 1"""
        # Evaluate test
        self.assertEqual(GameLevel.EXTREME.value, 1)
