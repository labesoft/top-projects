"""The Test of the Password Generator
-----------------------------

About this module
-----------------
This module is testing all the pwdgen functions
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-07"
__copyright__ = "Copyright 2021, Benoit Lapointe"
__version__ = "1.0.0"

from unittest import TestCase
from unittest.mock import MagicMock, patch

import pyperclip

import pwdgen
from pwdgen.__main__ import copy_password, generator


class PwdGenTest(TestCase):
    def setUp(self) -> None:
        pwdgen.__main__.pass_str = MagicMock()
        pwdgen.__main__.pass_len = MagicMock()

    def test_generator(self):
        """Test the pwd generator"""
        # Generate test
        pwdgen.__main__.pass_len.get.return_value = 8

        # Run test
        generator()

        # Evaluate test
        for pwd in pwdgen.__main__.pass_str.set.call_args_list:
            self.assertRegex(pwd.args[0], r".*[A-Z].*")
            self.assertRegex(pwd.args[0], r".*[a-z].*")
            self.assertRegex(pwd.args[0], r".*[0-9].*")
            self.assertRegex(pwd.args[0], r".*\W.*")

    def test_copy_password(self):
        """Test that the password get copied to the clipboard"""
        # Prepare test
        old_clip = pyperclip.paste()
        pwdgen.__main__.pass_str.get.return_value = self._testMethodName

        # Run test
        copy_password()

        # Evaluate test
        self.assertEqual(self._testMethodName, pyperclip.paste())
        pyperclip.copy(old_clip)
