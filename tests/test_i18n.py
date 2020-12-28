"""The test for i18n of The Hangman Game
-----------------------------

Package structure
-----------------
*tests/*
    **test_i18n.py**:
        The test for i18n of The Hangman Game
        
About this module
-----------------
The objective of this module is to test i18n module to get a full coverage

File structure
--------------
*import*

*constant*
"""

__author__ = "Benoit Lapointe"
__date__ = "2020-12-27"
__copyright__ = "Copyright 2020, labesoft"
__version__ = "1.0.0"

import os
from unittest import TestCase
from unittest.mock import patch, call, MagicMock

from hanggame import i18n


class TestI18N(TestCase):
    """This test the i18n module to get a full coverage"""

    @patch('hanggame.i18n.logging')
    @patch('hanggame.i18n.gettext')
    def test_lang_not_found(self, gettext, logger):
        # Prepare test
        gettext.translation.side_effect = [FileNotFoundError, gettext]

        # Run test
        i18n.setup()

        # Evaluate test
        calls = [
            call('hanggame.i18n'),
            call().warning('no language set, falling back to default: en_US')
        ]
        logger.getLogger.assert_has_calls(calls)
        calls = [
            call.translation('hanggame', localedir=i18n.LOCALES_DIR),
            call.translation('hanggame', localedir=i18n.LOCALES_DIR,
                             languages=['en_US']),
            call.install()
        ]
        gettext.assert_has_calls(calls)
