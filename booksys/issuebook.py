"""To issue books from the library
-----------------------------

About this module
-----------------
This modules issue books from the library
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
    return con, con.cursor(), "books_issued", "books", []


def issue(inf, destroy):
    con, cur, issue_table, book_table, all_bid = connect()
    bid = inf[0].get()
    issue_to = inf[1].get()

    extract_bid = f"select bid from {book_table}"
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

            if check == 'avail':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error", "Book ID not present")
    except MySQLError as err:
        messagebox.showinfo("Error", "Can't fetch Book IDs")
        print(err)

    issue_sql = f"insert into {issue_table} values ('{bid}','{issue_to}')"
    up_status = f"update {book_table} set status = 'issued' where bid = '{bid}'"
    try:
        if bid in all_bid and status:
            cur.execute(issue_sql)
            con.commit()
            cur.execute(up_status)
            con.commit()
            messagebox.showinfo('Success', "Book Issued Successfully")
            destroy()
        else:
            all_bid.clear()
            messagebox.showinfo('Message', "Book Already Issued")
            destroy()
            return
    except MySQLError as err:
        messagebox.showinfo(
            "Search Error", "The value entered is wrong, Try again"
        )
        print(err)
    all_bid.clear()


def issue_book():
    issue_book_tk = IssueBook()
    entries_args = [
        ("Book ID : ", 0.2),
        ("Issued To : ", 0.4)
    ]
    issue_book_tk.create_components(entries_args)
    issue_book_tk.mainloop()


class IssueBook(Home, Dialog):
    """This class manages how to issue a book from the library"""
    def create_components(self, args=None):
        self.create_bg(color="#D6ED17")
        self.create_header(title="Issue Book")
        issue_entries = self.create_entries(args)
        func = partial(issue, issue_entries, self.destroy)
        self.create_submit_quit_buttons(func)
