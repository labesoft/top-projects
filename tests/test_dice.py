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
from unittest.mock import MagicMock

import dice
from dice.__main__ import rolling_dice


class TestDice(TestCase):
    def setUp(self) -> None:
        dice.__main__.ImageLabel = MagicMock()

    """Test the rolling dice function"""

    def test_rolling_dice(self):
        # Prepare test
        rolling_dice()
        previous_image = dice.__main__.ImageLabel.image

        # Run test
        rolling_dice()

        # Evaluate test
        self.assertIsNotNone(previous_image)
        self.assertNotEqual(previous_image, dice.__main__.ImageLabel.image,
                            "The object didn't changed")
