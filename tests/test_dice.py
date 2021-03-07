"""The Test of the Rolling Dice Simulator
-----------------------------

About this module
-----------------
The objective of this module is to test the Rolling Dice Simulator
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-07"
__copyright__ = "Copyright 2021, Benoit Lapointe"
__version__ = "1.0.0"

from unittest import TestCase

from dice.__main__ import ImageLabel, rolling_dice


class TestDice(TestCase):
    """Test the rolling dice function"""
    def test_rolling_dice(self):
        # Prepare test
        rolling_dice()
        previous_image = ImageLabel.image

        # Run test
        rolling_dice()

        # Evaluate test
        self.assertIsNotNone(previous_image)
        self.assertNotEqual(previous_image, ImageLabel.image, "The object "
                                                              "didn't changed")
