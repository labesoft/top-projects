"""To returns books to the library
-----------------------------

About this module
-----------------
This module returns books to the library
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-11"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from functools import partial
from tkinter import BOTH, Button, Canvas, Entry, Frame, Label, Tk, messagebox

import pymysql
from pymysql import MySQLError

from booksys.home import Dialog, Home


def connect():
    con = pymysql.connect(
        host="localhost", user="bookuser", password="bookuser", database="db"
    )
    return con, con.cursor(), "books_issued", "books", []


def a_return(book_info, destroy):
    con, cur, issue_table, book_table, all_bid = connect()
    bid = book_info[0].get()
    extract_bid = "select bid from " + issue_table
    status = False
    try:
        cur.execute(extract_bid)
        con.commit()
        for i in cur:
            all_bid.append(i[0])

        if bid in all_bid:
            check_avail = f"select status from {book_table} where bid = '{bid}'"
            cur.execute(check_avail)
            con.commit()
            check = None
            for i in cur:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error", "Book ID not present")
    except MySQLError as err:
        messagebox.showinfo("Error", "Can't fetch Book IDs")
        print(err)
    issue_sql = f"delete from {issue_table} where bid = '{bid}'"

    upstatus = f"update {book_table} set status = 'avail' where bid = '{bid}'"
    try:
        if bid in all_bid and status:
            cur.execute(issue_sql)
            con.commit()
            cur.execute(upstatus)
            con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            all_bid.clear()
            messagebox.showinfo('Message', "Please check the book ID")
            destroy()
            return
    except MySQLError as err:
        messagebox.showinfo(
            "Search Error", "The value entered is wrong, Try again"
        )
        print(err)
    all_bid.clear()
    destroy()


def return_book():
    return_book_tk = ReturnBook()
    entries_args = [
        ("Book ID : ", 0.5),
    ]
    return_book_tk.create_components(entries_args)
    return_book_tk.mainloop()


class ReturnBook(Home, Dialog):
    """This class manages how to return a book to the library"""
    def create_components(self, args=None):
        self.create_bg(color="#006B38")
        self.create_header(title="Return Book")
        return_entries = self.create_entries(args)
        func = partial(a_return, return_entries, self.destroy)
        self.create_submit_quit_buttons(func)
