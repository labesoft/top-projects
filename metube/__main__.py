"""The Main of MeTube
-----------------------------

About this Module
------------------
This is the main entry point module of the MeTube application
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-09"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

# Import libraries
from tkinter import Button, Entry, Label, StringVar, Tk

from pytube import YouTube

ROOT = Tk()
LINK = StringVar()


def download_video():
    """This start the download from YouTube"""
    url = YouTube(str(LINK.get()))
    video = url.streams.first()
    video.download()
    Label(ROOT, text='DOWNLOADED', font='arial 15').place(x=180, y=210)


if __name__ == '__main__':
    """Main entry point of MeTube"""
    # Create display window
    ROOT.geometry('500x300')
    ROOT.resizable(0, 0)
    ROOT.title("labesoft-youtube video downloader")
    Label(ROOT, text='Metube Video Downloader', font='arial 20 bold').pack()

    # Create field to enter link
    Label(ROOT, text='Paste Link:', font='arial 15 bold').place(x=160, y=60)
    link_enter = Entry(ROOT, width=70, textvariable=LINK).place(x=32, y=90)

    Button(ROOT, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red',
           padx=2, command=download_video).place(x=180, y=150)
    ROOT.mainloop()
    # Add unit tests
