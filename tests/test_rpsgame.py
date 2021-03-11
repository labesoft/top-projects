"""Test the Rock Paper Scissors Game
-----------------------------

About this module
-----------------
This module is testing all the rpsgame functions
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-07"
__copyright__ = "Copyright 2021, Benoit Lapointe"
__version__ = "1.0.0"

from unittest import TestCase
from unittest.mock import MagicMock, call, patch

import rpsgame
from rpsgame.__main__ import (
    INVALID_CHOICE, LOOSE_GAME_1, LOOSE_GAME_2, LOOSE_GAME_3, PAPER, ROCK,
    SCISSORS, TIE_GAME, WIN_GAME_1, WIN_GAME_2, WIN_GAME_3, exit_rps,
    pick_comp_choice, play, reset
)


class TestRpsGame(TestCase):
    def setUp(self) -> None:
        rpsgame.__main__.Result = MagicMock()
        rpsgame.__main__.user_take = MagicMock()

    @patch('rpsgame.__main__.pick_comp_choice', return_value=SCISSORS)
    def test_play_tie(self, comp):
        # Prepare test
        rpsgame.__main__.user_take.get.return_value = SCISSORS

        # Run test
        play()

        # Evaluate test
        for callargs in rpsgame.__main__.Result.set.call_args_list:
            args = callargs.args[0]
            self.assertEqual(args, TIE_GAME,
                             "The tie game was not declare as such")

    @patch('rpsgame.__main__.pick_comp_choice', return_value=PAPER)
    def test_play_loose_1(self, comp):
        # Prepare test
        rpsgame.__main__.user_take.get.return_value = ROCK

        # Run test
        play()

        # Evaluate test
        for callargs in rpsgame.__main__.Result.set.call_args_list:
            args = callargs.args[0]
            self.assertEqual(args, LOOSE_GAME_1,
                             "The lost game was not declare as such")

    @patch('rpsgame.__main__.pick_comp_choice', return_value=SCISSORS)
    def test_play_win_1(self, comp):
        # Prepare test
        rpsgame.__main__.user_take.get.return_value = ROCK

        # Run test
        play()

        # Evaluate test
        for callargs in rpsgame.__main__.Result.set.call_args_list:
            args = callargs.args[0]
            self.assertEqual(args, WIN_GAME_1,
                             "The won game was not declare as such")

    @patch('rpsgame.__main__.pick_comp_choice', return_value=SCISSORS)
    def test_play_loose_2(self, comp):
        # Prepare test
        rpsgame.__main__.user_take.get.return_value = PAPER

        # Run test
        play()

        # Evaluate test
        for callargs in rpsgame.__main__.Result.set.call_args_list:
            args = callargs.args[0]
            self.assertEqual(args, LOOSE_GAME_2, "The lost game was not "
                                                     "declare as such")

    @patch('rpsgame.__main__.pick_comp_choice', return_value=ROCK)
    def test_play_win_2(self, comp):
        # Prepare test
        rpsgame.__main__.user_take.get.return_value = PAPER

        # Run test
        play()

        # Evaluate test
        for callargs in rpsgame.__main__.Result.set.call_args_list:
            args = callargs.args[0]
            self.assertEqual(args, WIN_GAME_2, "The won game was not "
                                                   "declare as such")

    @patch('rpsgame.__main__.pick_comp_choice', return_value=ROCK)
    def test_play_loose_3(self, comp):
        # Prepare test
        rpsgame.__main__.user_take.get.return_value = SCISSORS

        # Run test
        play()

        # Evaluate test
        for callargs in rpsgame.__main__.Result.set.call_args_list:
            args = callargs.args[0]
            self.assertEqual(args, LOOSE_GAME_3, "The lost game was not "
                                                     "declare as such")

    @patch('rpsgame.__main__.pick_comp_choice', return_value=PAPER)
    def test_play_win_3(self, comp):
        # Prepare test
        rpsgame.__main__.user_take.get.return_value = SCISSORS

        # Run test
        play()

        # Evaluate test
        for callargs in rpsgame.__main__.Result.set.call_args_list:
            args = callargs.args[0]
            self.assertEqual(args, WIN_GAME_3, "The won game was not "
                                                   "declare as such")

    def test_play_invalid(self):
        # Prepare test
        rpsgame.__main__.user_take.get.return_value = "Wrong"

        # Run test
        play()

        # Evaluate test
        for callargs in rpsgame.__main__.Result.set.call_args_list:
            args = callargs.args[0]
            self.assertEqual(args, INVALID_CHOICE, "The invalid choice was "
                                                       "not declare as such")

    def test_reset(self):
        # Run test
        reset()

        # Evaluate test
        for callargs in rpsgame.__main__.Result.set.call_args_list:
            args = callargs.args[0]
            self.assertEqual(args, "", "The result was not "
                                                     "resetted")
        for callargs in rpsgame.__main__.user_take.set.call_args_list:
            args = callargs.args[0]
            self.assertEqual(args, "", "The user take was "
                                                        "not resetted")

    def test_exit(self):
        # Prepare test
        rpsgame.__main__.root = MagicMock()

        # Run test
        exit_rps()

        # Evaluate test
        calls = [
            call.destroy(),
        ]
        rpsgame.__main__.root.assert_has_calls(calls)

    def test_pick_comp_choice(self):
        # Run test
        choice = pick_comp_choice()

        # Evaluate test
        self.assertIn(choice, [ROCK, PAPER, SCISSORS])
