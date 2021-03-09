"""The Test of the Money Changer
-----------------------------

About this module
-----------------
This module test the currency converter of Money Changer
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-07"
__copyright__ = "Copyright 2021, Benoit Lapointe"
__version__ = "1.0.0"

from unittest import TestCase
from unittest.mock import MagicMock, call

from moneychanger.converter import CurrencyConverter
from moneychanger.ui import CurrencyConverterUI


class TestCurrencyConverter(TestCase):
    """Test the currency converter model"""
    def setUp(self) -> None:
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        self.converter = CurrencyConverter(url)

    def test_convert_symmetry_usd(self):
        """Test the symmetry of the conversion with US dollars"""
        # Prepare test
        orig = 1

        # Run test
        cad = self.converter.convert("USD", "CAD", orig)
        usd = self.converter.convert("CAD", "USD", cad)

        # Evaluate test
        self.assertEqual(orig, usd)

    def test_convert_symmetry_not_usd(self):
        """Test the symmetry of the conversion without US dollars"""
        # Prepare test
        orig = 1

        # Run test
        eur = self.converter.convert("CAD", "EUR", orig)
        cad = self.converter.convert("EUR", "CAD", eur)

        # Evaluate test
        self.assertEqual(orig, cad)


class TestCurrencyConverterUI(TestCurrencyConverter):
    def setUp(self) -> None:
        super(TestCurrencyConverterUI, self).setUp()
        self.converter_ui = CurrencyConverterUI(self.converter)

    def test_perform(self):
        """Tests the display of the result value"""
        # Prepare test
        self.converter_ui.amount_field.get = MagicMock(return_value="1")
        self.converter_ui.converted_amount_field_label = MagicMock()

        # Run test
        self.converter_ui.perform()

        # Evaluate test
        calls = [
            call.config(text=f"{1/self.converter.data['rates']['CAD']:0.2}")
        ]
        self.converter_ui.converted_amount_field_label.assert_has_calls(calls)

    def test_restrict_number_only_false(self):
        """Tests non number passed to the restriction method"""
        # Run test
        is_number = self.converter_ui.restrict_number_only("a")

        # Evaluate test
        self.assertFalse(is_number)

    def test_restrict_number_only_true(self):
        """Tests number passed to the restriction method"""
        # Run test
        is_number = self.converter_ui.restrict_number_only("1")

        # Evaluate test
        self.assertTrue(is_number)
