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


def prepare_image(image_filename, same=True, scale=0.25):
    image = Image.open(image_filename)
    width, height = image.size
    modified_width = int(width * scale)

    if same:
        modified_height = int(height * scale)
    else:
        modified_height = int(height / scale)

    image = image.resize((modified_width, modified_height), Image.ANTIALIAS)
    return image


def create_canvas(canvas_root, image_filename):
    image = prepare_image(image_filename)
    background_image = ImageTk.PhotoImage(image)
    canvas = Canvas(canvas_root)
    canvas.create_image(300, 340, image=background_image)
    canvas.config(bg="white", width=image.size[0], height=image.size[1])
    canvas.pack(expand=True, fill=BOTH)


def create_frame(frame_root):
    frame = Frame(frame_root, bg="#FFBB00", bd=5)
    frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    heading_label = Label(frame, text="Welcome to \n labesoft Library",
                          bg='black', fg='white', font=('Courier', 15))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)


def create_root():
    tk_root = Tk()
    tk_root.title("labesoft Library")
    tk_root.minsize(width=400, height=400)
    tk_root.geometry("600x500")
    return tk_root


def create_button(button_root, btn_text, btn_command, y):
    btn = Button(
        button_root, text=btn_text, bg='black', fg='white', command=btn_command
    )
    btn.place(relx=0.28, rely=y, relwidth=0.45, relheight=0.1)


def create_home_page():
    root = create_root()
    create_canvas(root, "lib.jpg")
    create_frame(root)
    create_button(root, "Add Book Details", add_book, 0.4)
    create_button(root, "Delete Book", delete, 0.5)
    create_button(root, "View Book List", view, 0.6)
    create_button(root, "Issue Book to Student", issue_book, 0.7)
    create_button(root, "Return Book", return_book, 0.8)
    root.mainloop()


if __name__ == '__main__':
    """Main entry point of booksys"""
    mypass = "bookuser"
    mydatabase = "db"
    con = pymysql.connect(
        host="localhost", user="bookuser", password=mypass, database=mydatabase
    )
    cur = con.cursor()
    create_home_page()
