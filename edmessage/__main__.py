"""The Encode Decode Message Application
-----------------------------

About this Module
------------------
This module is the main entry point of The Encode Decode Message Application.

"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-09"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

# Import module
import base64
from tkinter import BOTTOM, Button, Entry, Label, StringVar, Tk


def Encode(key, message):
    """Encode a message using a bytes 64 alphabet

    :param key: the key used to encode
    :param message: the message to encode
    :return: the encoded message
    """
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def Decode(key, message):
    """Decode a message using a bytes64 alphabet

    :param key: the key to decode the message
    :param message: the encoded message to decode
    :return: the decoded message
    """
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)


def Mode():
    """Switch between encode of decode mode"""
    if mode.get() == 'e':
        Result.set(Encode(private_key.get(), Text.get()))
    elif mode.get() == 'd':
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')


def Exit():
    """Destroy the Tk window and exit"""
    root.destroy()


def Reset():
    """Reset all text to empty sting"""
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


if __name__ == '__main__':
    """Main entry point of edmessage"""
    # Create display window
    root = Tk()
    root.geometry('500x300')
    root.resizable(0, 0)
    root.title("labesoft - Message Encode and Decode")

    # Define variables
    Text = StringVar()
    private_key = StringVar()
    mode = StringVar()
    Result = StringVar()

    # Define labels and buttons
    Label(root, text='ENCODE DECODE', font='arial 20 bold').pack()
    Label(root, text='labesoft', font='arial 20 bold').pack(side=BOTTOM)
    Label(root, font='arial 12 bold', text='MESSAGE').place(x=60, y=60)
    Entry(root, font='arial 10', textvariable=Text, bg='ghost white').place(
        x=290, y=60)
    Label(root, font='arial 12 bold', text='KEY').place(x=60, y=90)
    Entry(root, font='arial 10', textvariable=private_key,
          bg='ghost white').place(x=290, y=90)
    Label(root, font='arial 12 bold', text='MODE(e-encode, d-decode)').place(
        x=60, y=120)
    Entry(root, font='arial 10', textvariable=mode, bg='ghost white').place(
        x=290, y=120)
    Entry(root, font='arial 10 bold', textvariable=Result,
          bg='ghost white').place(x=290, y=150)
    Button(root, font='arial 10 bold', text='RESULT', padx=2, bg='LightGray',
           command=Mode).place(x=60, y=150)
    Button(root, font='arial 10 bold', text='RESET', width=6, command=Reset,
           bg='LimeGreen', padx=2).place(x=80, y=190)
    Button(root, font='arial 10 bold', text='EXIT', width=6, command=Exit,
           bg='OrangeRed', padx=2, pady=2).place(x=180, y=190)
    root.mainloop()
    # Add unit tests
