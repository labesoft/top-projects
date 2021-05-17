"""To delete books from the library
-----------------------------

About this module
-----------------
This module manages deleting books from the library
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-11"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from functools import partial
from tkinter import (
    END, messagebox
)

import pymysql
from pymysql import MySQLError

from booksys.home import Dialog, Home


def connect():
    con = pymysql.connect(
        host="localhost", user="bookuser", password="bookuser", database="db"
    )
    return con, con.cursor(), "books_issued", "books"


def delete_book(book_info, destroy):
    con, cur, issue_table, book_table = connect()
    bid = book_info[0].get()

    delete_sql = f"delete from {book_table} where bid = '{bid}'"
    delete_issue = f"delete from {issue_table} where bid = '{bid}'"
    try:
        cur.execute(delete_sql)
        con.commit()
        cur.execute(delete_issue)
        con.commit()
        messagebox.showinfo('Success', "Book Record Deleted Successfully")
        book_info[0].delete(0, END)
    except MySQLError as err:
        messagebox.showinfo("Please check Book ID")
        print(err)
    destroy()


def delete():
    add_book_tk = DeleteBook()
    entries_args = [
        ("Book ID : ", 0.5),
    ]
    add_book_tk.create_components(entries_args)
    add_book_tk.mainloop()


class DeleteBook(Home, Dialog):
    """This class manages how to delete a book from the library"""

    def create_components(self, args=None):
        self.create_bg(color="#006B38")
        self.create_header(title="Delete Book")
        book_entries = self.create_entries(args)
        func = partial(delete_book, book_entries, self.destroy)
        self.create_submit_quit_buttons(func)
