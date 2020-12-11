"""The tests for hangman.py of The Hangman Game
-----------------------------------------

About this Project
------------------
The objective of this project is to recreate The Hangman Game that a user could
play interactively by attempting to unmask a word one letter at a time using a
limited number of attempts without being hanged by the hangman.

About this module
-----------------
The objective of this module is to test the hangman module
"""
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
        self.assertEqual(str(self.hangman), IMAGE_STRING_SEP.join(self.hangman.gallows))

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
        gallows[4] = PART_HEAD_HANGED

        # Run test
        self.hangman.draw()

        # Evaluate test
        self.assertEqual(self.hangman.gallows, gallows)

    def test_draw_missed_body(self):
        """Tests the gallows with head/body hanged"""
        # Prepare test
        self.hangman.missed = 2
        gallows = list(GALLOWS)
        gallows[4] = PART_HEAD_HANGED
        gallows[5] = PART_BODY

        # Run test
        self.hangman.draw()

        # Evaluate test
        self.assertEqual(self.hangman.gallows, gallows)

    def test_draw_missed_left_arm(self):
        """Tests the gallows with head/left arm hanged"""
        # Prepare test
        self.hangman.missed = 3
        gallows = list(GALLOWS)
        gallows[4] = PART_HEAD_HANGED
        gallows[5] = PART_ARM_LEFT

        # Run test
        self.hangman.draw()

        # Evaluate test
        self.assertEqual(self.hangman.gallows, gallows)

    def test_draw_missed_arms(self):
        """Tests the gallows with both arms hanged"""
        # Prepare test
        self.hangman.missed = 4
        gallows = list(GALLOWS)
        gallows[4] = PART_HEAD_HANGED
        gallows[5] = PART_ARMS_HANGED

        # Run test
        self.hangman.draw()

        # Evaluate test
        self.assertEqual(self.hangman.gallows, gallows)

    def test_draw_missed_left_leg(self):
        """Tests the gallows with left leg hanged"""
        # Prepare test
        self.hangman.missed = 5
        gallows = list(GALLOWS)
        gallows[4] = PART_HEAD_HANGED
        gallows[5] = PART_ARMS_HANGED
        gallows[6] = PART_LEG_LEFT

        # Run test
        self.hangman.draw()

        # Evaluate test
        self.assertEqual(self.hangman.gallows, gallows)

    def test_draw_hanged(self):
        """Tests the gallows with hanged man"""
        # Prepare test
        self.hangman.missed = 6
        gallows = list(GALLOWS)
        gallows[4] = PART_HEAD_HANGED
        gallows[5] = PART_ARMS_HANGED
        gallows[6] = PART_LEGS_HANGED

        # Run test
        self.hangman.draw()

        # Evaluate test
        self.assertEqual(self.hangman.gallows, gallows)

    def test_draw_saved(self):
        """Tests the gallows with saved man"""
        # Prepare test
        gallows = list(GALLOWS)
        gallows[5] = PART_HEAD_SAVED
        gallows[6] = PART_BODY
        gallows[7] = PART_LEGS_SAVED

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
