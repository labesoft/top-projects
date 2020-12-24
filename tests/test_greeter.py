"""The tests for greeter.py of The Hangman Game
-----------------------------------------

About this module
-----------------
The objective of this module is to test the greeter module
"""
from unittest import TestCase
from unittest.mock import MagicMock, call, patch

from hanggame.console import *
from hanggame.i18n import IN_MSG_LETTER, IN_MSG_REPLAY, OUT_MSG_ANSWER, OUT_MSG_GOODBYE, OUT_MSG_INVALID, OUT_MSG_LUCK, \
    OUT_MSG_NB_ATTEMPT, OUT_MSG_READY, OUT_MSG_THANKS, OUT_MSG_WELCOME


class TestGreeter(TestCase):
    def setUp(self) -> None:
        self.greeter = Console(c_out=MagicMock(), c_in=MagicMock())
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

    @patch('hanggame.greeter.sleep')
    def test_input(self, sl):
        # Run test
        self.greeter.input(self.message)

        # Evaluate test
        sl.assert_called_once_with(IN_SLEEP)
        self.greeter.c_in.assert_called_once_with(self.message)

    def test_out_farewell(self):
        """Tests the thanks and goodbye message"""
        # Prepare test
        self.greeter.player_name = self.name

        # Run test
        self.greeter.out_farewell()

        # Evaluate test
        calls = [call(OUT_MSG_THANKS), call(OUT_MSG_GOODBYE.format(self.name))]
        self.greeter.c_out.has_call(calls)

    def test_out_end_game(self):
        """Tests the output of image, message and word at the end of the game"""
        # Run test
        self.greeter.end_game(self.image, self.message, self.word)

        # Evaluate test
        calls = [call(self.image), call(self.message), call(OUT_MSG_ANSWER.format(self.word))]
        self.greeter.c_out.has_calls(calls)

    def test_out_end_turn(self):
        """Tests the end turn message"""
        # Run test
        self.greeter.end_turn(self.message)

        # Evaluate test
        self.greeter.c_out.assert_called_once_with(FORMAT_NEWLINE_PRE(self.message))

    def test_out_init_attempt(self):
        """Tests the first msg of each attempt with the image, attempts remaining and masked word"""
        # Prepare test
        attempt_nb = 1

        # Run test
        self.greeter.init_game_metrics(self.image, attempt_nb, self.word)

        # Evaluate test
        calls = [call(self.image), call(OUT_MSG_NB_ATTEMPT.format(attempt_nb)), call(SPACE_STR.join(list(self.word)))]
        self.greeter.c_out.has_calls(calls)

    def test_out_in_welcome(self):
        """Test the format of welcome message and input of his name"""
        # Prepare test
        self.greeter.input = MagicMock(return_value=self.name)

        # Run test
        self.greeter.welcome_player(self.image)

        # Evaluate test
        calls = [call(OUT_MSG_WELCOME), call(self.image), call(OUT_MSG_LUCK.format(self.greeter.player_name)),
                 call(FORMAT_NEWLINE_PRE(OUT_MSG_READY))]
        self.greeter.c_out.has_calls(calls)
        self.assertEqual(self.greeter.player_name, self.name)

    def test_out_invalid_letter(self):
        """Tests message when submitting an invalid letter"""
        # Run test
        self.greeter.out_invalid_letter()

        # Evaluate test
        self.greeter.c_out.assert_called_once_with(OUT_MSG_INVALID)
