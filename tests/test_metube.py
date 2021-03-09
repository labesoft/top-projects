"""Test the MeTube application download procedure
-----------------------------

About this module
-----------------
Module to test the download procedure of MeTube
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-09"
__copyright__ = "Copyright 2021, Benoit Lapointe"
__version__ = "1.0.0"

from unittest import TestCase
from unittest.mock import call, patch

from metube.__main__ import download_video


class TestMeTube(TestCase):
    @patch("metube.__main__.YouTube")
    @patch("metube.__main__.LINK")
    def test_download_video(self, link, youtube):
        # Run test
        download_video()

        # Evaluate test
        calls = [
            call(f"{link.get()}"),
            call().streams.first(),
            call().streams.first().download()
        ]
        youtube.assert_has_calls(calls)
