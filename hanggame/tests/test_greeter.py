"""The tests for greeter.py of The Hangman Game
-----------------------------------------

About this Project
------------------
The objective of this project is to recreate The Hangman Game that a user could
play interactively by attempting to unmask a word one letter at a time using a
limited number of attempts without being hanged by the hangman.

About this module
-----------------
The objective of this module is to test the greeter module
"""
from unittest import TestCase
from unittest.mock import MagicMock, call

from hanggame.greeter import *


class TestGreeter(TestCase):
    def setUp(self) -> None:
        self.greeter = Greeter(cb_out=MagicMock(), cb_in=MagicMock())
        self.message = 'My test message'
        self.image = 'My test image'
        self.input = ' My user input '
        self.word = 'My test word'
        self.name = 'Test Name'

    def test_in_new_game(self):
        """Tests message of replay and return the answer"""
        # Prepare test
        self.greeter.input = MagicMock(return_value=self.input)

        # Run test
        result = self.greeter.in_new_game()

        # Evaluate test
        self.greeter.input.assert_called_once_with(FORMAT_NEWLINE_END(IN_MSG_REPLAY))
        self.assertEqual(self.input, result)

    def test_in_new_letter(self):
        """Tests it ask for new letter and return the stripped answer"""
        # Prepare test
        self.greeter.input = MagicMock(return_value=self.input)

        # Run test
        result = self.greeter.in_new_letter()

        # Evaluate test
        self.greeter.input.assert_called_once_with(IN_MSG_LETTER)
        self.assertEqual(self.input.strip(), result)

    def test_out_farewell(self):
        """Tests the thanks and goodbye message"""
        # Prepare test
        self.greeter.player_name = self.name

        # Run test
        self.greeter.out_farewell()

        # Evaluate test
        calls = [call(OUT_MSG_THANKS), call(OUT_MSG_GOODBYE.format(self.name))]
        self.greeter._out.has_call(calls)

    def test_out_end_game(self):
        """Tests the output of image, message and word at the end of the game"""
        # Run test
        self.greeter.out_end_game(self.image, self.message, self.word)

        # Evaluate test
        calls = [call(self.image), call(self.message), call(OUT_MSG_ANSWER.format(self.word))]
        self.greeter._out.has_calls(calls)

    def test_out_end_turn(self):
        """Tests the end turn message"""
        # Run test
        self.greeter.out_end_turn(self.message)

        # Evaluate test
        self.greeter._out.assert_called_once_with(FORMAT_NEWLINE_PRE(self.message))

    def test_out_init_attempt(self):
        """Tests the first msg of each attempt with the image, attempts remaining and masked word"""
        # Prepare test
        attempt_nb = 1

        # Run test
        self.greeter.out_init_attempt(self.image, attempt_nb, self.word)

        # Evaluate test
        calls = [call(self.image), call(OUT_MSG_NB_ATTEMPT.format(attempt_nb)), call(SPACING.join(list(self.word)))]
        self.greeter._out.has_calls(calls)

    def test_out_in_welcome(self):
        """Test the format of welcome message and input of his name"""
        # Prepare test
        self.greeter.input = MagicMock(return_value=self.name)

        # Run test
        self.greeter.out_in_welcome(self.image)

        # Evaluate test
        calls = [call(OUT_MSG_WELCOME), call(self.image), call(OUT_MSG_LUCK.format(self.greeter.player_name)),
                 call(FORMAT_NEWLINE_PRE(OUT_MSG_READY))]
        self.greeter._out.has_calls(calls)
        self.assertEqual(self.greeter.player_name, self.name)

    def test_out_invalid_letter(self):
        """Tests message when submitting an invalid letter"""
        # Run test
        self.greeter.out_invalid_letter()

        # Evaluate test
        self.greeter._out.assert_called_once_with(OUT_MSG_INVALID)
