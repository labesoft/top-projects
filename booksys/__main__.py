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

import pymysql as pymysql

from booksys.addbook import add_book
from booksys.deletebook import delete
from booksys.home import Home
from booksys.issuebook import issue_book
from booksys.returnbook import return_book
from booksys.viewbooklist import view_booklist

if __name__ == '__main__':
    """Main entry point of booksys"""
    mypass = "bookuser"
    mydatabase = "db"
    con = pymysql.connect(
        host="localhost", user="bookuser", password=mypass, database=mydatabase
    )
    cur = con.cursor()
    home = Home()
    btn_list = [
        ("Add Book Details", add_book),
        ("Delete Book", delete),
        ("View Book List", view_booklist),
        ("Issue Book to Student", issue_book),
        ("Return Book", return_book)
    ]
    home.create_components(btn_list)
    home.mainloop()
