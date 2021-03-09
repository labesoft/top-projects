"""Test the speech function of The Talker
-----------------------------

About this module
-----------------
The objective of this module is to test the speech procedure
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-09"
__copyright__ = "Copyright 2021, Benoit Lapointe"
__version__ = "1.0.0"

from unittest import TestCase
from unittest.mock import MagicMock, call, patch

import talker
from talker.__main__ import SAVE_PATH, play


class TalkerTest(TestCase):
    @patch("talker.__main__.playsound")
    @patch("talker.__main__.gTTS")
    def test_text_to_speech(self, tts, play):
        talker.__main__.entry_field = MagicMock()

        # Run test
        play()

        # Evaluate test
        play.assert_called_once_with(SAVE_PATH)
        calls = [
            call(text=talker.__main__.entry_field.get(), lang='fr'),
            call().save(SAVE_PATH)
        ]
        tts.assert_has_calls(calls)
