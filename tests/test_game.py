"""The tests for game.py of The Hangman Game
-----------------------------------------

About this module
-----------------
The objective of this module is to test the game module
"""
import random
from unittest import TestCase
from unittest.mock import patch, MagicMock, call

import hanggame
import hanggame.i18n
from hanggame.game import HangGame


class TestHangGame(TestCase):
    @patch('hanggame.greeter.Greeter')
    @patch('hanggame.hangman.Hangman')
    @patch('hanggame.word.Word')
    def setUp(self, w, hg, g) -> None:
        self.game = HangGame()
        self.game.hangman = hg
        self.game.word = w
        self.game.greeter = g

    def test_reset(self):
        """Test that the game resets its parts"""
        # Run test
        self.game.reset()

        # Evaluate test
        self.game.hangman.reset.assert_called_once()
        self.game.word.choose.assert_called_once()
        self.assertTrue(self.game.is_playing)

    def test_play_again_wrong_yes(self):
        """Test that the game ask play again to player and handles the answer"""
        # Prepare test
        self.game.reset = MagicMock()
        choice = random.choice(hanggame.i18n.YES_LIST)
        self.game.greeter.in_new_game.side_effect = ['WRONG', choice, 'yes', StopIteration]

        # Run test
        self.game.ask_play_again()

        # Evaluate test
        calls = [call.in_new_game(), call.in_new_game()]
        self.game.greeter.assert_has_calls(calls)
        self.assertTrue(self.game.is_playing, f'Bad choice={choice}')
        self.game.reset.assert_called_once()

    def test_play_again_no(self):
        """Test that the game ask play again to player and handles the answer"""
        # Prepare test
        self.game.reset = MagicMock()
        choice = random.choice(hanggame.i18n.NO_LIST)
        self.game.greeter.in_new_game.side_effect = [choice, 'no', StopIteration]

        # Run test
        self.game.ask_play_again()

        # Evaluate test
        self.game.greeter.in_new_game.assert_called_once()
        self.assertFalse(self.game.is_playing, f'Bad choice={choice}')
        self.game.greeter.out_farewell.assert_called_once()

    def test_run_winner_turn(self):
        """Test that the run works properly"""
        # Prepare test
        result = 'a'
        self.game.accept_letter = MagicMock(return_value=result)
        self.game.is_playing = MagicMock()
        self.game.is_playing.__bool__.side_effect = [True, False]

        # Run test
        self.game.run()

        # Evaluate test
        calls = [call.draw({'hanged': True}), call.draw()]
        self.game.hangman.draw.has_calls(calls)
        calls = [call.welcome(str(self.game.hangman)),
                 call.init_attempt(str(self.game.hangman), self.game.hangman.attempt, str(self.game.word))]
        self.game.greeter.has_calls(calls)
        self.game.accept_letter.assert_called_once()
        self.game.greeter.out_end_turn.assert_called_once()
        out_msg = self.game.greeter.out_end_turn.call_args[0][0]
        self.assertIn(out_msg, hanggame.i18n.OUT_MSG_CONGRATS)
        self.game.word.unmask.assert_called_once_with(result)
        self.game.word.is_masked.assert_called_once()

    def test_run_winner_game(self):
        """Test that the run works properly"""
        # Prepare test
        result = 'a'
        self.game.accept_letter = MagicMock(return_value=result)
        self.game.is_playing = MagicMock()
        self.game.is_playing.__bool__.side_effect = [True, False]
        self.game.ask_play_again = MagicMock()
        self.game.word.is_masked.return_value = False

        # Run test
        self.game.run()

        # Evaluate test
        self.game.hangman.draw.assert_any_call(saved=True)
        self.game.greeter.out_end_game.assert_called_once_with(str(self.game.hangman), hanggame.i18n.OUT_MSG_WINNER,
                                                               self.game.word.show())
        self.game.ask_play_again.assert_called_once()

    def test_run_loser_turn(self):
        """Test that the run works properly"""
        # Prepare test
        result = 'a'
        self.game.accept_letter = MagicMock(return_value=result)
        self.game.is_playing = MagicMock()
        self.game.is_playing.__bool__.side_effect = [True, False]
        self.game.word.unmask.return_value = False

        # Run test
        self.game.run()

        # Evaluate test
        self.assertIn(call.missed.__iadd__(1), self.game.hangman.mock_calls)
        self.game.hangman.draw.assert_any_call()
        self.game.greeter.out_end_turn.assert_called_once()
        out_msg = self.game.greeter.out_end_turn.call_args[0][0]
        self.assertIn(out_msg, hanggame.i18n.OUT_MSG_COMPLAINTS)

    def test_run_loser_game(self):
        """Test that the run works properly"""
        # Prepare test
        result = 'a'
        self.game.accept_letter = MagicMock(return_value=result)
        self.game.is_playing = MagicMock()
        self.game.is_playing.__bool__.side_effect = [True, False]
        self.game.ask_play_again = MagicMock()
        self.game.word.unmask.return_value = False
        self.game.hangman.attempt.__bool__.return_value = False

        # Run test
        self.game.run()

        # Evaluate test
        self.game.hangman.attempt.__bool__.assert_called_once()
        self.game.greeter.out_end_game.assert_called_once_with(str(self.game.hangman), hanggame.i18n.OUT_MSG_LOSER,
                                                               self.game.word.show())
        self.game.ask_play_again.assert_called_once()

    def test_accept_letter_valid(self):
        """Test that the game can accept a letter properly"""
        # Prepare test
        letter = 'a'
        self.game.is_valid = MagicMock(side_effect=[False, True, True, StopIteration])
        self.game.greeter.in_new_letter = MagicMock(return_value=letter)

        # Run test
        result = self.game.accept_letter()

        # Evaluate test
        calls = [call(letter), call(letter), call(letter)]
        self.game.is_valid.has_calls(calls)
        self.assertEqual(result, letter)

    def test_accept_letter_invalid_once(self):
        """Test that the game can accept a letter properly"""
        # Prepare test
        self.game.is_valid = MagicMock(side_effect=[False, False, False, True, True, StopIteration])
        letters = ['ah', 'a']
        self.game.greeter.in_new_letter = MagicMock(side_effect=letters)

        # Run test
        result = self.game.accept_letter()

        # Evaluate test
        calls = [call(hanggame.game.EMPTY_STR), call(letters[0]), call(letters[0]), call(letters[1]), call(letters[1])]
        self.game.is_valid.has_calls(calls)
        self.game.greeter.out_invalid_letter.assert_called_once()
        self.assertEqual(result, letters[1])

    def test_is_valid_true(self):
        """Test that the game properly validate the letter candidate"""
        # Prepare test
        candidate = 'a'
        self.game.word.is_unmasked.return_value = False

        # Run test
        result = self.game.is_valid(candidate)

        # Evaluate test
        self.assertTrue(result)

    def test_is_valid_false_not_char(self):
        """Test that the game properly validate the letter candidate"""
        # Prepare test
        candidate = 'ah'
        self.game.word.is_unmasked.return_value = False

        # Run test
        result = self.game.is_valid(candidate)

        # Evaluate test
        self.assertFalse(result)

    def test_is_valid_false_not_alpha(self):
        """Test that the game properly validate the letter candidate"""
        # Prepare test
        candidate = '1'
        self.game.word.is_unmasked.return_value = False

        # Run test
        result = self.game.is_valid(candidate)

        # Evaluate test
        self.assertFalse(result)

    def test_is_valid_false_unmasked(self):
        """Test that the game properly validate the letter candidate"""
        # Prepare test
        candidate = 'a'

        # Run test
        result = self.game.is_valid(candidate)

        # Evaluate test
        self.assertFalse(result)
        self.game.word.is_unmasked.assert_called_once_with(candidate)
