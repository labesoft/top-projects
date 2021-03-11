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


def create_buttons(root_window):
    """Creates and add all buttons to the Calculator"""
    Button(
        root_window, text="1", command=lambda: get_variables(1),
        font='Times 36 bold',
        width=3
    ).grid(row=2, column=0, sticky=N + S + E + W)
    Button(
        root_window, text="2", command=lambda: get_variables(2),
        font='Times 36 bold',
        width=3
    ).grid(row=2, column=1, sticky=N + S + E + W)
    Button(
        root_window, text="3", command=lambda: get_variables(3),
        font='Times 36 bold',
        width=3
    ).grid(row=2, column=2, sticky=N + S + E + W)
    Button(
        root_window, text="4", command=lambda: get_variables(4),
        font='Times 36 bold',
        width=3
    ).grid(row=3, column=0, sticky=N + S + E + W)
    Button(
        root_window, text="5", command=lambda: get_variables(5),
        font='Times 36 bold',
        width=3
    ).grid(row=3, column=1, sticky=N + S + E + W)
    Button(
        root_window, text="6", command=lambda: get_variables(6),
        font='Times 36 bold',
        width=3
    ).grid(row=3, column=2, sticky=N + S + E + W)
    Button(
        root_window, text="7", command=lambda: get_variables(7),
        font='Times 36 bold',
        width=3
    ).grid(row=4, column=0, sticky=N + S + E + W)
    Button(
        root_window, text="8", command=lambda: get_variables(8),
        font='Times 36 bold',
        width=3
    ).grid(row=4, column=1, sticky=N + S + E + W)
    Button(
        root_window, text="9", command=lambda: get_variables(9),
        font='Times 36 bold',
        width=3
    ).grid(row=4, column=2, sticky=N + S + E + W)
    # adding other buttons to the calculator
    Button(
        root_window, text="AC", command=lambda: clear_all(),
        font='Times 36 bold',
        width=3
    ).grid(row=5, column=0, sticky=N + S + E + W)
    Button(
        root_window, text="0", command=lambda: get_variables(0),
        font='Times 36 bold',
        width=3
    ).grid(row=5, column=1, sticky=N + S + E + W)
    Button(
        root_window, text=".", command=lambda: get_variables("."),
        font='Times 36 bold',
        width=3
    ).grid(row=5, column=2, sticky=N + S + E + W)
    Button(
        root_window, text="+", command=lambda: get_operation("+"),
        font='Times 36 bold',
        width=3
    ).grid(row=2, column=3, sticky=N + S + E + W)
    Button(
        root_window, text="-", command=lambda: get_operation("-"),
        font='Times 36 bold',
        width=3
    ).grid(row=3, column=3, sticky=N + S + E + W)
    Button(
        root_window, text="*", command=lambda: get_operation("*"),
        font='Times 36 bold',
        width=3
    ).grid(row=4, column=3, sticky=N + S + E + W)
    Button(
        root_window, text="/", command=lambda: get_operation("/"),
        font='Times 36 bold',
        width=3
    ).grid(row=5, column=3, sticky=N + S + E + W)
    # adding new operations
    Button(
        root_window, text="pi", command=lambda: get_operation(str(math.pi)),
        font='Times 36 bold',
        width=3
    ).grid(row=2, column=4, sticky=N + S + E + W)
    Button(
        root_window, text="%", command=lambda: get_operation("%"),
        font='Times 36 bold',
        width=3
    ).grid(row=3, column=4, sticky=N + S + E + W)
    Button(
        root_window, text="(", command=lambda: get_operation("("),
        font='Times 36 bold',
        width=3
    ).grid(row=4, column=4, sticky=N + S + E + W)
    Button(
        root_window, text="exp", command=lambda: get_operation("**"),
        font='Times 36 bold',
        width=3
    ).grid(row=5, column=4, sticky=N + S + E + W)
    Button(
        root_window, text="<-", command=lambda: undo(), font='Times 36 bold',
        width=3
    ).grid(row=2, column=5, sticky=N + S + E + W)
    Button(
        root_window, text="x!", command=lambda: fact(), font='Times 36 bold',
        width=3
    ).grid(row=3, column=5, sticky=N + S + E + W)
    Button(
        root_window, text=")", command=lambda: get_operation(")"),
        font='Times 36 bold',
        width=3
    ).grid(row=4, column=5, sticky=N + S + E + W)
    Button(
        root_window, text="^2", command=lambda: get_operation("**2"),
        font='Times 36 bold',
        width=3
    ).grid(row=5, column=5, sticky=N + S + E + W)
    Button(
        root_window, text="=", command=lambda: calculate(),
        font='Times 36 bold',
        width=3
    ).grid(columnspan=6, sticky=N + S + E + W)


def get_variables(num):
    """Receives the digit as parameter and display it on the input field"""
    global i
    display.insert(i, num)
    i += 1


def get_operation(operator):
    """Insert the operator on the display"""
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def clear_all():
    """Clear the display"""
    display.delete(0, END)


def undo():
    """Undo the last character entered on display"""
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")


def calculate():
    """Calculate the value of the expression displayed"""
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except (parser.ParserError, SyntaxError) as err:
        clear_all()
        display.insert(0, "Error")


def fact():
    """Calculate the factorial of the number displayed"""
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0, result)
    except ValueError:
        clear_all()
        display.insert(0, "Error")


if __name__ == '__main__':
    """Main entry point of calcprog"""
    # Making a window for our calculator
    root = Tk()
    root.title('labesoft - Calculator')

    # Designing the buttons
    display = Entry(root, font='Times 36 bold', width=3)
    display.grid(row=1, columnspan=6, sticky=N + E + W + S)
    create_buttons(root)

    # i keeps the track of current position on the input text field
    i = 0
    root.mainloop()
    # Add unit tests
