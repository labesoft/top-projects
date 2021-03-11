"""The Library Management System Application
-----------------------------

About this Module
------------------
This module is the main entry point of The Library Management System
Application.

"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-09"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from tkinter import BOTH, Button, Canvas, Frame, Label, Tk

import pymysql as pymysql
from PIL import Image, ImageTk

from booksys.addbook import add_book
from booksys.deletebook import delete
from booksys.issuebook import issue_book
from booksys.returnbook import return_book
from booksys.viewbook import view

if __name__ == '__main__':
    """Main entry point of booksys"""
    # main.py – which does function call to all other python files
    mypass = "bookuser"  # use your own password
    mydatabase = "db"  # The database name
    con = pymysql.connect(host="localhost", user="bookuser", password=mypass,
                          database=mydatabase)
    # root is the username here
    cur = con.cursor()  # cur -> cursor

    root = Tk()
    root.title("labesoft Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    same = True
    n = 0.25
    # Adding a background image
    background_image = Image.open("lib.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth * n)
    if same:
        newImageSizeHeight = int(imageSizeHeight * n)
    else:
        newImageSizeHeight = int(imageSizeHeight / n)

    background_image = background_image.resize(
        (newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)
    Canvas1 = Canvas(root)
    Canvas1.create_image(300, 340, image=img)
    Canvas1.config(bg="white", width=newImageSizeWidth,
                   height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill=BOTH)
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome to \n labesoft Library",
                         bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    btn1 = Button(
        root, text="Add Book Details", bg='black', fg='white', command=add_book
    )
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = Button(
        root, text="Delete Book", bg='black', fg='white', command=delete
    )
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    btn3 = Button(
        root, text="View Book List", bg='black', fg='white', command=view
    )
    btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    btn4 = Button(
        root, text="Issue Book to Student", bg='black', fg='white',
        command=issue_book
    )
    btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

    btn5 = Button(
        root, text="Return Book", bg='black', fg='white', command=return_book
    )
    btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)
    root.mainloop()
