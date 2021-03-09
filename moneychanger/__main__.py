"""The Main of Money Changer
-----------------------------

About this Module
------------------
This module is the main entry point for the money changer application
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-07"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from moneychanger.converter import CurrencyConverter
from moneychanger.ui import CurrencyConverterUI

if __name__ == '__main__':
    """Main entry point of moneychanger"""
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = CurrencyConverter(url)
    CurrencyConverterUI(converter).mainloop()
