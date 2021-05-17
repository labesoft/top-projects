"""To add books to the library
-----------------------------

About this module
-----------------
This module add books to the library
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-11"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from functools import partial
from tkinter import messagebox

import pymysql
from pymysql import MySQLError

from booksys.home import Dialog, Home


def connect():
    con = pymysql.connect(
        host="localhost", user="bookuser", password="bookuser", database="db"
    )
    return con, con.cursor(), "books"


def insert_book_db(book_entries, destroy):
    con, cur, book_table = connect()
    bid = book_entries[0].get()
    title = book_entries[1].get()
    author = book_entries[2].get()
    status = book_entries[3].get()
    status = status.lower()

    q = "insert into {} values ('{}','{}','{}','{}')"
    addbook_query = q.format(book_table, bid, title, author, status)
    try:
        cur.execute(addbook_query)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except MySQLError as err:
        messagebox.showinfo("Error", "Can't add data into Database")
        print(err)
    destroy()


def add_book():
    add_book_tk = AddBook()
    entries_args = [
        ("Book ID : ", 0.2),
        ("Title : ", 0.35),
        ("Author : ", 0.50),
        ("Status(Avail/issued) : ", 0.65)
    ]
    add_book_tk.create_components(entries_args)
    add_book_tk.mainloop()


class AddBook(Home, Dialog):
    def __init__(self):
        super(AddBook, self).__init__()
        self.label_frame = None

    def create_components(self, args=None):
        self.create_bg(color="#ff6e40")
        self.create_header(title="Add Books")
        book_entries = self.create_entries(args)
        submit_func = partial(insert_book_db, book_entries, self.destroy)
        self.create_submit_quit_buttons(submit_func)
