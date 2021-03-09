"""The Model of the Money Changer
-----------------------------

About this module
-----------------
This module is the currency converter model of the money changer application
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-07"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

import requests


class CurrencyConverter:
    """This convert any money amount from currency to a chosen one """
    def __init__(self, url):
        """Creates a converter using the latest conversion schema

        :param url: the url where to get the conversion schema
        """
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        """Convert an amount from a currency to another

        When not the first currency in USD, it first converts to USD
        and then to the destination currency

        :param from_currency: the source currency
        :param to_currency: the destination currency
        :param amount: the amount to convert
        :return:
        """
        # first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD':
            amount /= self.currencies[from_currency]

        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount
