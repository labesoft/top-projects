"""The GUI of the Money Changer
-----------------------------

About this module
-----------------
This module display a GUI that a user can use to convert a money amount of  a
currency to the corresponding amount of another currency
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-07"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

import re
from tkinter import (
    Button, CENTER, Entry, GROOVE, Label, RAISED, RIDGE,
    StringVar, Tk
)
from tkinter.ttk import Combobox


class CurrencyConverterUI(Tk):
    """This display text field and button to interact with to change money"""
    def __init__(self, converter):
        """Creates a window to convert currency

        :param converter: the model of a currency converter
        """
        Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter
        self.geometry("500x200")
        # Label
        self.intro_label = Label(self,
                                 text='Welcome to Real Time Currency Convertor',
                                 fg='blue', relief=RAISED, borderwidth=3)
        self.intro_label.config(font=('Courier', 15, 'bold'))
        self.date_label = Label(
            self,
            text=f"1 Canadian Dollar = "
                 f"{self.currency_converter.convert('CAD', 'USD', 1)}"
                 f" USD \n Date : {self.currency_converter.data['date']}",
            relief=GROOVE, borderwidth=5)
        self.intro_label.place(x=10, y=5)
        self.date_label.place(x=170, y=50)
        # Entry box
        valid = (self.register(self.restrict_number_only), '%P')
        # restric NumberOnly function will restrict this user to enter
        # invavalid number in Amount field. We will define it later in code
        self.amount_field = Entry(self, bd=3, relief=RIDGE,
                                  justify=CENTER, validate='key',
                                  validatecommand=valid)
        self.converted_amount_field_label = Label(self, text='', fg='black',
                                                  bg='white', relief=RIDGE,
                                                  justify=CENTER, width=17,
                                                  borderwidth=3)

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("CAD")  # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD")  # default value

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = Combobox(
            self,
            textvariable=self.from_currency_variable,
            values=list(self.currency_converter.currencies.keys()),
            font=font, state='readonly',
            width=12, justify=CENTER)
        self.to_currency_dropdown = Combobox(
            self,
            textvariable=self.to_currency_variable,
            values=list(
                self.currency_converter.currencies.keys()),
            font=font, state='readonly',
            width=12, justify=CENTER)

        # placing
        self.from_currency_dropdown.place(x=30, y=120)
        self.amount_field.place(x=36, y=150)
        self.to_currency_dropdown.place(x=340, y=120)
        # self.converted_amount_field.place(x = 346, y = 150)
        self.converted_amount_field_label.place(x=346, y=150)

        # Convert button
        self.convert_button = Button(self, text="Convert", fg="black",
                                     command=self.perform)
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x=225, y=135)

    def perform(self):
        """Performs the conversion of a currency to another using the model

        :return: None
        """
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()
        converted_amount = self.currency_converter.convert(from_curr,
                                                           to_curr, amount)
        converted_amount = round(converted_amount, 2)
        self.converted_amount_field_label.config(text=str(converted_amount))

    def restrict_number_only(self, string):
        """Restrict the uses of numbers only in text fields

        :param string: the input to validate
        :return: True if the input is number only, False otherwise
        """
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return string == "" or (string.count('.') <= 1 and result is not None)
