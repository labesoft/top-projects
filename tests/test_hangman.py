"""The tests for hangman.py of The Hangman Game
-----------------------------------------

About this module
-----------------
The objective of this module is to test the hangman module
"""

__author__ = "Benoit Lapointe"
__date__ = "2020-12-18"
__copyright__ = "Copyright 2020, labesoft"
__version__ = "1.0.0"

from unittest import TestCase
from unittest.mock import MagicMock

from hanggame.hangman import *
from hanggame.level import GameLevel


class TestHangman(TestCase):
    def setUp(self) -> None:
        self.hangman = Hangman()

    def test___init__(self):
        """Tests that max_attempt default to beginner value"""
        # Evaluate test
        self.assertEqual(self.hangman.max_attempt, GameLevel.BEGINNER.value)

    def test___str__(self):
        # Evaluate test
        lines_result = [line.format(left=self.hangman.left_spaces,
                                    middle=self.hangman.middle_spaces,
                                    left_foot=self.hangman.left_foot,
                                    right_foot=self.hangman.right_foot)
                        for line in self.hangman.gallows]
        result = self.hangman.sep.join(lines_result)

        self.assertEqual(str(self.hangman), result)

    def test_attempt(self):
        """Tests that the attempt is max_attempt - missed"""
        # Run test
        result = self.hangman.attempt

        # Evaluate test
        self.assertEqual(result, self.hangman.max_attempt - self.hangman.missed)

    def test_missed(self):
        """Tests missed getter and properly initialized"""
        # Run test
        result = self.hangman.missed

        # Evaluate test
        self.assertEqual(result, ZERO)

    def test_missed_setter(self):
        """Tests missed setter"""
        # Run test
        self.hangman.missed = 1

        # Evaluate test
        self.assertEqual(self.hangman.missed, 1)

    def test_draw_init(self):
        """Tests the first draw is correct and properly initialized"""
        # Run test
        self.hangman.draw()

        # Evaluate test
        self.assertEqual(self.hangman.gallows, GALLOWS)
        self.assertIsNot(self.hangman.gallows, GALLOWS)

    def test_draw_missed_head(self):
        """Tests the gallows with head hanged"""
        # Prepare test
        self.hangman.missed = 1
        gallows = list(GALLOWS)
        gallows[4] = GALLOWS_PART_HEAD_HANGED

        # Run test
        self.hangman.draw()

        # Evaluate test
        self.assertEqual(self.hangman.gallows, gallows)

    def test_draw_missed_body(self):
        """Tests the gallows with head/body hanged"""
        # Prepare test
        self.hangman.missed = 2
        gallows = list(GALLOWS)
        gallows[4] = GALLOWS_PART_HEAD_HANGED
        gallows[5] = GALLOWS_PART_BODY

        # Run test
        self.hangman.draw()

        # Evaluate test
        self.assertEqual(self.hangman.gallows, gallows)

    def test_draw_missed_left_arm(self):
        """Tests the gallows with head/left arm hanged"""
        # Prepare test
        self.hangman.missed = 3
        gallows = list(GALLOWS)
        gallows[4] = GALLOWS_PART_HEAD_HANGED
        gallows[5] = GALLOWS_PART_ARM_LEFT

        # Run test
        self.hangman.draw()

        # Evaluate test
        self.assertEqual(self.hangman.gallows, gallows)

    def test_draw_missed_arms(self):
        """Tests the gallows with both arms hanged"""
        # Prepare test
        self.hangman.missed = 4
        gallows = list(GALLOWS)
        gallows[4] = GALLOWS_PART_HEAD_HANGED
        gallows[5] = GALLOWS_PART_ARMS_HANGED

        # Run test
        self.hangman.draw()

        # Evaluate test
        self.assertEqual(self.hangman.gallows, gallows)

    def test_draw_missed_left_leg(self):
        """Tests the gallows with left leg hanged"""
        # Prepare test
        self.hangman.missed = 5
        gallows = list(GALLOWS)
        gallows[4] = GALLOWS_PART_HEAD_HANGED
        gallows[5] = GALLOWS_PART_ARMS_HANGED
        gallows[6] = GALLOWS_PART_LEG_LEFT

        # Run test
        self.hangman.draw()

        # Evaluate test
        self.assertEqual(self.hangman.gallows, gallows)

    def test_draw_hanged(self):
        """Tests the gallows with hanged man"""
        # Prepare test
        self.hangman.missed = 6
        gallows = list(GALLOWS)
        gallows[4] = GALLOWS_PART_HEAD_HANGED
        gallows[5] = GALLOWS_PART_ARMS_HANGED
        gallows[6] = GALLOWS_PART_LEGS_HANGED

        # Run test
        self.hangman.draw()

        # Evaluate test
        self.assertEqual(self.hangman.gallows, gallows)

    def test_draw_saved(self):
        """Tests the gallows with saved man"""
        # Prepare test
        gallows = list(GALLOWS)
        gallows[5] = GALLOWS_PART_HEAD_SAVED
        gallows[6] = GALLOWS_PART_BODY
        gallows[7] = GALLOWS_PART_LEGS_SAVED

        # Run test
        self.hangman.draw(saved=True)

        # Evaluate test
        self.assertEqual(self.hangman.gallows, gallows)

    def test_reset(self):
        """Tests the hanged man removal"""
        # Prepare test
        self.hangman.missed = 1
        self.hangman.draw = MagicMock()

        # Run test
        self.hangman.reset()

        # Evaluate test
        self.assertEqual(self.hangman.missed, ZERO)
        self.hangman.draw.assert_called_once()

    def test_reset_new_level(self):
        # Run test
        self.hangman.reset(GameLevel.INFERNO)

        # Evaluate test
        self.assertEqual(GameLevel.INFERNO.value, self.hangman.max_attempt)
