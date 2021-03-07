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
from unittest.mock import patch

import pyperclip

from pwdgen.__main__ import copy_password, generator, pass_str


class PwdGenTest(TestCase):
    @patch("pwdgen.__main__.pass_len.get", return_value=8)
    def test_generator(self, plen):
        """Test the pwd generator"""
        # Run test
        generator()
        pwd = pass_str.get()

        # Evaluate test
        self.assertRegex(pwd, r".*[A-Z].*")
        self.assertRegex(pwd, r".*[a-z].*")
        self.assertRegex(pwd, r".*[0-9].*")
        self.assertRegex(pwd, r".*\W.*")

    @patch("pwdgen.__main__.pass_len.get", return_value=8)
    def test_copy_password(self, plen):
        """Test that the password get copied to the clipboard"""
        # Prepare test
        generator()
        pwd = pass_str.get()

        # Run test
        copy_password()

        # Evaluate test
        self.assertEqual(pwd, pyperclip.paste())
