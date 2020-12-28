"""The tests for greeter.py of The Hangman Game
-----------------------------------------

About this module
-----------------
The objective of this module is to test the greeter module
"""

__author__ = "Benoit Lapointe"
__date__ = "2020-12-18"
__copyright__ = "Copyright 2020, labesoft"
__version__ = "1.0.0"

import random
from unittest import TestCase
from unittest.mock import MagicMock, call, patch

from hanggame.console import *
from hanggame import i18n, console
from hanggame.level import GameLevel


class TestConsole(TestCase):
    @patch('hanggame.hangman.Hangman')
    @patch('hanggame.word.Word')
    def setUp(self, w, h) -> None:
        self.console = Console(word=w, hangman=h, c_out=MagicMock(),
                               c_in=MagicMock())
        w.available.return_value = list(i18n.ALPHA_LAYOUT)
        self.message = 'My test message'
        self.image = 'My test image'
        self.input = ' My user input '
        self.word = 'My test word'
        self.name = 'Test Name'

    def test_accept_letter_masked(self):
        """Test that the game can accept a letter properly"""
        # Prepare test
        letter = 'a'
        self.console.in_valid_letter = MagicMock(return_value='b')
        self.console.word.is_masked.return_value = True

        # Run test
        result = self.console.accept_letter(letter)

        # Evaluate test
        self.assertEqual(letter, result)

    def test_accept_letter_unmasked_masked(self):
        """Test that the game can accept a letter properly"""
        # Prepare test
        letter_a = 'a'
        letter_b = 'b'
        self.console.in_valid_letter = MagicMock(return_value=letter_b)
        self.console.word.is_masked.side_effect = [False, True, StopIteration]

        # Run test
        result = self.console.accept_letter(letter_a)

        # Evaluate test
        self.assertEqual(letter_b, result)

    def test_play_again_wrong_yes(self):
        """Test that the game ask play again to player and handles the answer"""
        # Prepare test
        choice = random.choice(i18n.IN_YES_LIST)
        self.console.input = MagicMock(
            side_effect=['WRONG', choice, StopIteration]
        )

        # Run test
        result = self.console.ask_play_again()

        # Evaluate test
        calls = [call(FORMAT_NEWLINE_END(i18n.IN_MSG_REPLAY)),
                 call(FORMAT_NEWLINE_END(i18n.IN_MSG_REPLAY))]
        self.console.input.assert_has_calls(calls)
        self.console.hangman.reset.assert_called_once()
        self.console.word.choose.assert_called_once()
        self.assertTrue(result, f'Bad choice={choice}')

    def test_play_again_no(self):
        """Test that the game ask play again to player and handles the answer"""
        # Prepare test
        choice = random.choice(i18n.IN_NO_LIST)
        self.console.out_farewell = MagicMock()
        self.console.input = MagicMock(side_effect=[choice, StopIteration])

        # Run test
        self.console.ask_play_again()

        # Evaluate test
        calls = [call(FORMAT_NEWLINE_END(i18n.IN_MSG_REPLAY))]
        self.console.input.assert_has_calls(calls)
        self.console.out_farewell.assert_called_once()

    def test_in_valid_letter(self):
        """Tests it ask for new letter and return the stripped answer"""
        # Prepare test
        letters = ['ah', '1', 'A']
        self.console.input = MagicMock(side_effect=letters)

        # Run test
        result = self.console.in_valid_letter()

        # Evaluate test
        self.assertEqual(letters[2].lower(), result)

    @patch('hanggame.console.sleep')
    def test_input(self, sl):
        letter = ' a'
        self.console.c_in.return_value = letter

        # Run test
        result = self.console.input(self.message)

        # Evaluate test
        sl.assert_called_once_with(IN_SLEEP)
        self.console.c_in.assert_called_once_with(self.message)
        self.assertEqual(letter.strip(), result)

    def test_out_farewell(self):
        """Tests the thanks and goodbye message"""
        # Prepare test
        self.console.player_name = self.name

        # Run test
        self.console.out_farewell()

        # Evaluate test
        calls = [
            call(i18n.OUT_MSG_THANKS),
            call(i18n.OUT_MSG_GOODBYE.format(self.name))
        ]
        self.console.c_out.has_call(calls)

    def test_out_end_game(self):
        """Tests the output of image, message and word at the end of the game"""
        # Run test
        self.console.end_game(self.message)

        # Evaluate test
        calls = [call(str(self.console.hangman)), call(self.message),
                 call(i18n.OUT_MSG_ANSWER.format(self.console.word.show()))]
        self.console.c_out.assert_has_calls(calls)

    def test_out_end_turn(self):
        """Tests the end turn message"""
        # Run test
        self.console.end_turn(self.message)

        # Evaluate test
        self.console.c_out.assert_called_once_with(
            FORMAT_NEWLINE_PRE(self.message)
        )

    def test_out_init_attempt(self):
        """Tests the first msg of each attempt with the image.

        Also attempts remaining and masked word.
        """
        # Run test
        self.console.init_game_metrics()

        # Evaluate test
        calls = [
            call(str(self.console.hangman)),
            call(i18n.OUT_MSG_NB_ATTEMPT.format(self.console.hangman.attempt)),
            call('')
        ]
        self.console.c_out.assert_has_calls(calls)

    def test_out_in_welcome(self):
        """Test the format of welcome message and input of his name"""
        # Prepare test
        self.console.input = MagicMock(return_value=self.name)

        # Run test
        self.console.welcome_player()

        # Evaluate test
        calls = [call(i18n.OUT_MSG_WELCOME), call(str(self.console.hangman)),
                 call(i18n.OUT_MSG_LUCK.format(self.console.player_name)),
                 call(FORMAT_NEWLINE_PRE(i18n.OUT_MSG_READY))]
        self.console.c_out.assert_has_calls(calls)
        self.assertEqual(self.console.player_name, self.name)

    def test_out_invalid_letter(self):
        """Tests message when submitting an invalid letter"""
        # Run test
        self.console.out_invalid_letter()

        # Evaluate test
        self.console.c_out.assert_called_once_with(i18n.OUT_MSG_INVALID)

    @patch('hanggame.console.Hangman')
    @patch('hanggame.console.Console')
    @patch('hanggame.console.HangGame')
    def test_main(self, hg, c, hm):
        # Prepare test


        # Run test
        console.main(GameLevel.BEGINNER, self.console.word)

        # Evaluate test
        calls = [call(level=GameLevel.BEGINNER)]
        hm.assert_has_calls(calls)
        calls = [call(word=self.console.word, hangman=hm())]
        c.assert_has_calls(calls)
        calls = [
            call(GameLevel.BEGINNER, self.console.word, hm(), c()),
            call().run_loop()
        ]
        hg.assert_has_calls(calls)
