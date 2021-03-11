"""The Main of the Password Generator
-----------------------------

About this Module
------------------
The objective of this module is to generate a password within the parameters
given by the user
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-07"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

# Import modules
import random
import string
import pyperclip

from tkinter import BOTTOM, Button, Entry, IntVar, Label, Spinbox, StringVar, Tk


# Define Functions
def generator():
    """Generate a new password taking input parameters

    :return: None
    """
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(
            string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits +
            string.punctuation)
    pass_str.set(password)


def copy_password():
    """Copy the password to the clipboard

    :return: None
    """
    pyperclip.copy(pass_str.get())


if __name__ == '__main__':
    """Main entry point of pwdgen"""
    # Initialized Window
    root = Tk()
    pass_str = StringVar()
    pass_len = IntVar()

    root.geometry("400x400")
    root.resizable(0, 0)
    root.title("labesoft - PASSWORD GENERATOR")
    Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
    Label(root, text='labesoft', font='arial 15 bold').pack(side=BOTTOM)

    # Select Password Length
    pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 '
                                                          'bold').pack()
    length = Spinbox(root, from_=8, to_=32, textvariable=pass_len,
                     width=15).pack()

    Button(root, text="GENERATE PASSWORD", command=generator).pack(pady=5)
    Entry(root, textvariable=pass_str).pack()
    Button(root, text='COPY TO CLIPBOARD', command=copy_password).pack(pady=5)

    root.mainloop()
    # Write unit test for every function/class/method
