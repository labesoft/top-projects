"""The tests for game.py of The Hangman Game
-----------------------------------------

About this module
-----------------
The objective of this module is to test the game module
"""
import random
from unittest import TestCase
from unittest.mock import patch, MagicMock, call

from hanggame import i18n
from hanggame.game import HangGame
from hanggame.level import GameLevel


class TestHangGame(TestCase):
    @patch('hanggame.console.Console')
    @patch('hanggame.hangman.Hangman')
    @patch('hanggame.word.Word')
    def setUp(self, w, hg, ui) -> None:
        self.game = HangGame(GameLevel.BEGINNER, w, hg, ui)
        self.game.hangman = hg
        self.game.word = w
        self.game.ui = ui

    @patch('hanggame.game.random.choice')
    def test_play_turn_win(self, ch):
        """Test a turn/game winner"""
        # Prepare test
        ch.return_value = i18n.OUT_MSG_CONGRATS[0]
        key = 'a'
        self.game.ui.accept_letter.return_value = key
        self.game.word.unmask.return_value = True
        self.game.word.is_mask.return_value = False

        # Run test
        self.game.play_turn(key)

        # Evaluate test
        calls = [call.attempt.__bool__(), call.draw(saved=True)]
        self.game.hangman.assert_has_calls(calls)
        calls = [call.accept_letter(key), call.end_turn(i18n.OUT_MSG_CONGRATS[0]), call.end_game(i18n.OUT_MSG_WINNER),
                 call.ask_play_again()]
        self.game.ui.assert_has_calls(calls)
        calls = [call.__bool__(), call.unmask(key), call.is_mask()]
        self.game.word.assert_has_calls(calls)

    @patch('hanggame.game.random.choice')
    def test_play_turn_loose(self, ch):
        """Test a turn/game looser"""
        # Prepare test
        ch.return_value = i18n.OUT_MSG_COMPLAINTS[0]
        key = 'a'
        self.game.hangman.attempt.__bool__.side_effect = [True, False]
        self.game.ui.accept_letter.return_value = key
        self.game.word.unmask.return_value = False

        # Run test
        self.game.play_turn(key)

        # Evaluate test
        calls = [call.attempt.__bool__(), call.missed.__iadd__(1), call.draw(), call.attempt.__bool__()]
        self.game.hangman.assert_has_calls(calls)
        calls = [call.accept_letter(key), call.end_turn(i18n.OUT_MSG_COMPLAINTS[0]), call.end_game(i18n.OUT_MSG_LOSER),
                 call.ask_play_again()]
        self.game.ui.assert_has_calls(calls)
        calls = [call.__bool__(), call.unmask(key)]
        self.game.word.assert_has_calls(calls)

    def test_run_loop(self):
        # Prepare test
        self.game.play_turn = MagicMock(side_effect=[True, False])

        # Run test
        self.game.run_loop()

        # Evaluate test
        calls = [call.draw(hanged=True), call.draw()]
        self.game.hangman.assert_has_calls(calls)
        calls = [call.welcome_player(), call.init_game_metrics(), call.in_valid_letter(), call.init_game_metrics(),
                 call.in_valid_letter()]
        self.game.ui.assert_has_calls(calls)
