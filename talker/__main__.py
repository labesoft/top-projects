"""The Main of Talker
-----------------------------

About this Module
------------------
This module is the main entry point of the Talker application.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-09"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

import os
from tkinter import Button, Entry, Label, StringVar, Tk

from gtts import gTTS
from playsound import playsound

SAVE_PATH = 'labesoft.mp3'


def text_to_speech():
    """Convert written text to audio and play the sound in french

    :return: None
    """
    message = entry_field.get()
    speech = gTTS(text=message, lang="fr")
    if os.path.exists(SAVE_PATH):
        os.remove(SAVE_PATH)
    speech.save(SAVE_PATH)
    playsound(SAVE_PATH)


def exit_talker():
    """Destroy the main frame and exit

    :return: None
    """
    root.destroy()


def reset_talker():
    """Reset the message to speech

    :return: None
    """
    msg.set("")


if __name__ == '__main__':
    """Main entry point of talker"""
    root = Tk()
    root.geometry("350x300")
    root.configure(bg='ghost white')
    root.title("labesoft - Talker")
    Label(root, text="Talker", font="arial 20 bold",
          bg='white smoke').pack()
    Label(text="labesoft", font='arial 15 bold', bg='white smoke',
          width='20').pack(side='bottom')

    msg = StringVar()
    Label(root, text="Enter Text", font='arial 15 bold',
          bg='white smoke').place(x=20, y=60)

    entry_field = Entry(root, textvariable=msg, width='50')
    entry_field.place(x=20, y=100)
    Button(root, text="PLAY", font='arial 15 bold', command=text_to_speech,
           width='4').place(x=25, y=140)
    Button(root, font='arial 15 bold', text='EXIT', width='4',
           command=exit_talker,
           bg='OrangeRed1').place(x=100, y=140)
    Button(root, font='arial 15 bold', text='RESET', width='6',
           command=reset_talker).place(x=175, y=140)
    root.mainloop()
