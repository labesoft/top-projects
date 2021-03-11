"""The Main of the Dice Rolling Simulator
-----------------------------

About this Module
------------------
The objective of this module is to simulate a dice rolling game
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-07"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

# Importing the required modules: Tkinter, Image, ImageTk, Random
import os
import random
from pathlib import Path
from tkinter import Button, Label, Tk

from PIL import Image, ImageTk

dice = [
    Path(os.path.dirname(__file__), "{}{}{}".format("die", str(i), ".PNG"))
    for i in range(1, 7)]


# function activated by button
def rolling_dice():
    image = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=image)
    # keep a reference
    ImageLabel.image = image


if __name__ == '__main__':
    """Main entry point of dice"""
    # Building a top-level widget to make the main window for our application
    root = Tk()
    # Forming a list of images to be randomly displayed
    ImageLabel = Label(root)
    ImageLabel.image = None

    root.geometry('400x400')
    root.title('labesoft Roll the Dice')

    # Designing the buttons: adding labels into the frame
    BlankLine = Label(root, text="")
    BlankLine.pack()
    HeadingLabel = Label(root, text="Hello from labesoft!",
                         fg="light green",
                         bg="dark green",
                         font="Helvetica 16 bold italic")
    HeadingLabel.pack()

    # Constructing a label for image, adding a button, assigning functionality
    rolling_dice()
    ImageLabel.pack(expand=True)
    button = Button(root, text='Roll the Dice', fg='blue',
                    command=rolling_dice)
    button.pack(expand=True)

    # Launching the main loop
    root.mainloop()
