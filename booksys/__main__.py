"""The main app of the Library Management System
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

import pymysql as pymysql

from booksys.views import (
    BooklistDialog, DeleteBookDialog, Home, IssueBookDialog, NewBookDialog,
    ReturnBookDialog
)


def new_book():
    """Creates and displays the new book dialog"""
    new_book_view = NewBookDialog()
    new_book_form_args = [
        ("Book ID : ", 0.2),
        ("Title : ", 0.35),
        ("Author : ", 0.50),
        ("Status(Avail/issued) : ", 0.65)
    ]
    new_book_view.create_components(new_book_form_args)
    new_book_view.mainloop()


def delete():
    """Create and displays delete book dialog"""
    add_book_tk = DeleteBookDialog()
    entries_args = [
        ("Book ID : ", 0.5),
    ]
    add_book_tk.create_components(entries_args)
    add_book_tk.mainloop()


def issue_book():
    """Creates and displays the issue book dialog"""
    issue_book_tk = IssueBookDialog()
    entries_args = [
        ("Book ID : ", 0.2),
        ("Issued To : ", 0.4)
    ]
    issue_book_tk.create_components(entries_args)
    issue_book_tk.mainloop()


def return_book():
    """Creates and displays the return book dialog"""
    return_book_tk = ReturnBookDialog()
    entries_args = [
        ("Book ID : ", 0.5),
    ]
    return_book_tk.create_components(entries_args)
    return_book_tk.mainloop()


def list_books():
    """Creates and displays the book list dialog"""
    view_book_tk = BooklistDialog()
    view_book_tk.create_components()
    view_book_tk.mainloop()


if __name__ == '__main__':
    """Main entry point (Home) of Library Management System"""
    mypass = "bookuser"
    mydatabase = "db"
    con = pymysql.connect(
        host="localhost", user="bookuser", password=mypass, database=mydatabase
    )
    cur = con.cursor()
    home = Home()
    btn_list = [
        ("Add Book Details", new_book),
        ("Delete Book", delete),
        ("View Book List", list_books),
        ("Issue Book to Student", issue_book),
        ("Return Book", return_book)
    ]
    home.create_components(btn_list)
    home.mainloop()
