"""The Simple Calculator Application
-----------------------------

About this Module
------------------
This module is the main entry point of The Simple Calculator Application.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-09"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

# Importing the necessary modules
import math
import parser
from math import factorial
from tkinter import Button, E, END, Entry, N, S, Tk, W


class Calculator(Tk):
    """A simple calsulator class"""
    def __init__(self):
        """Initialize buttons"""
        super(Calculator, self).__init__()
        # Making a window for our calculator
        self.title('labesoft - Calculator')

        # Designing the buttons
        self.display = Entry(self, font='Times 36 bold', width=3)
        self.display.grid(row=1, columnspan=6, sticky=N + E + W + S)
        # i keeps the track of current position on the input text field
        self.i = 0

        # Numbers from 1 to 9
        self.btn_list = [
            (str(num + 1), self.get_variables, num + 1, int(num / 3 + 2),
             num % 3)
            for num in range(9)
        ]
        # Other Buttons
        self.btn_list += [
            ("AC", self.clear_all, (), 5, 0),
            ("0", self.get_variables, 0, 5, 1),
            (".", self.get_variables, ".", 5, 2),
            ("+", self.get_operation, "+", 2, 3),
            ("-", self.get_operation, "-", 3, 3),
            ("*", self.get_operation, "*", 4, 3),
            ("/", self.get_operation, "/", 5, 3),
            ("pi", self.get_operation, str(math.pi), 2, 4),
            ("%", self.get_operation, "%", 3, 4),
            ("(", self.get_operation, "(", 4, 4),
            ("exp", self.get_operation, "**", 5, 4),
            ("<-", self.undo, (), 2, 5),
            ("x!", self.fact, (), 3, 5),
            (")", self.get_operation, ")", 4, 5),
            ("^2", self.get_operation, "**2", 5, 5),
            ("=", self.calculate, (), None, None)
        ]

    def create_buttons(self):
        """Creates and add all buttons to the Calculator"""
        for text, func, arg, row, col in self.btn_list:
            self.create_button(text, func, arg, row, col)

    def create_button(self, text, func, arg, row, col):
        """Create a text button triggering a given function"""
        if arg:
            btn = Button(self, text=text, command=lambda: func(arg), 
                         font='Times 36 bold', width=3)
        else:
            btn = Button(self, text=text, command=lambda: func(), 
                         font='Times 36 bold', width=3)
        if not row:
            btn.grid(columnspan=6, sticky=N + S + E + W)
        else:
            btn.grid(row=row, column=col, sticky=N + S + E + W)

    def get_variables(self, num):
        """Receives the digit as parameter and display it on the input field"""
        self.display.insert(self.i, num)
        self.i += 1

    def get_operation(self, operator):
        """Insert the operator on the display"""
        length = len(operator)
        self.display.insert(self.i, operator)
        self.i += length

    def clear_all(self):
        """Clear the display"""
        self.display.delete(0, END)

    def undo(self):
        """Undo the last character entered on display"""
        entire_string = self.display.get()
        if len(entire_string):
            new_string = entire_string[:-1]
            self.clear_all()
            self.display.insert(0, new_string)
        else:
            self.clear_all()
            self.display.insert(0, "Error")

    def calculate(self):
        """Calculate the value of the expression displayed"""
        entire_string = self.display.get()
        try:
            a = parser.expr(entire_string).compile()
            result = eval(a)
            self.clear_all()
            self.display.insert(0, result)
        except (parser.ParserError, SyntaxError):
            self.clear_all()
            self.display.insert(0, "Error")

    def fact(self):
        """Calculate the factorial of the number displayed"""
        entire_string = self.display.get()
        try:
            result = factorial(int(entire_string))
            self.clear_all()
            self.display.insert(0, result)
        except ValueError:
            self.clear_all()
            self.display.insert(0, "Error")


if __name__ == '__main__':
    """Main entry point of calcprog"""
    calc = Calculator()
    calc.create_buttons()
    calc.mainloop()
