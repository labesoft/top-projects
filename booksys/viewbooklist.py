"""To view books from the library
-----------------------------

About this module
-----------------
This module manages viewing books from the library
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-11"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from tkinter import Button, Frame, Label, messagebox

import pymysql
from pymysql import MySQLError

from booksys.home import Home


def connect():
    con = pymysql.connect(
        host="localhost", user="bookuser", password="bookuser", database="db"
    )
    return con, con.cursor(), "books"


def booklist():
    con, cur, book_table = connect()
    get_books = "select * from " + book_table
    try:
        cur.execute(get_books)
        con.commit()
        for i in cur:
            yield i
    except MySQLError as err:
        messagebox.showinfo("Failed to fetch files from database")
        print(err)


def view_booklist():
    view_book_tk = ViewBooklist()
    view_book_tk.create_components()
    view_book_tk.mainloop()


class ViewBooklist(Home):
    """This class manages how to issue a book from the library"""

    def create_components(self, args=None):
        self.create_bg(color="#12a4d9")
        self.create_header(title="View Books")
        label_frame = Frame(self, bg='black')
        label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
        y = 0.25
        Label(label_frame,
              text="%-10s%-40s%-30s%-20s" % (
              'BID', 'Title', 'Author', 'Status'),
              bg='black', fg='white').place(relx=0.07, rely=0.1)
        Label(
            label_frame,
            text="--------------------------------------------------------------"
                 "--------------",
            bg='black', fg='white'
        ).place(relx=0.05, rely=0.2)
        for i in booklist():
            Label(label_frame,
                  text="%-10s%-30s%-30s%-20s" % (i[0], i[1], i[2], i[3]),
                  bg='black', fg='white').place(relx=0.07, rely=y)
            y += 0.1

        quit_btn = Button(
            self, text="Quit", bg='#f7f1e3', fg='black', command=self.destroy
        )
        quit_btn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
