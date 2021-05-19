"""The model of the Library Management System
-----------------------------

About this Module
------------------
The goal of this module is to model a book as its data representation
providing an API with its basic operations.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-05-18"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from tkinter import END, messagebox

import pymysql
from pymysql import MySQLError


class Book:
    """The Model for creating a new book"""
    def __init__(self):
        self.con = None
        self.cur = None
        self.book_table = "books"
        self.issued_table = "books_issued"
        self.all_bid = []

    def connect(self):
        self.con = pymysql.connect(
            host="localhost", user="bookuser", password="bookuser",
            database="db"
        )
        self.cur = self.con.cursor()

    def create(self, book_info, destroy):
        """Add a new book to the library based on the book form fields value

        :param book_info: the values of the new book
        :param destroy: a trigger to close the dialog window
        """
        self.connect()
        bid = book_info[0].get()
        title = book_info[1].get()
        author = book_info[2].get()
        status = book_info[3].get()
        status = status.lower()

        q = "insert into {} values ('{}','{}','{}','{}')"
        addbook_query = q.format(self.book_table, bid, title, author, status)
        try:
            self.cur.execute(addbook_query)
            self.con.commit()
            messagebox.showinfo('Success', "Book added successfully")
        except MySQLError as err:
            messagebox.showinfo("Error", "Can't add data into Database")
            print(err)
        destroy()

    def delete(self, book_info, destroy):
        """Delete book of the library based on the book info provided

        :param book_info: the values of the book to delete
        :param destroy: a trigger to close the dialog window
        """
        self.connect()
        bid = book_info[0].get()

        delete_sql = f"delete from {self.book_table} where bid = '{bid}'"
        delete_issue = f"delete from {self.issued_table} where bid = '{bid}'"
        try:
            self.cur.execute(delete_sql)
            self.con.commit()
            self.cur.execute(delete_issue)
            self.con.commit()
            messagebox.showinfo('Success', "Book Record Deleted Successfully")
            book_info[0].delete(0, END)
        except MySQLError as err:
            messagebox.showinfo("Please check Book ID")
            print(err)
        destroy()

    def update(self, book_info, destroy):
        """Update book information based on the book form fields value

        :param book_info: the values of the book to update
        :param destroy: a trigger to close the dialog window
        """
        self.connect()
        is_issue = len(book_info) == 2

        bid = book_info[0].get()
        if is_issue:
            issue_to = book_info[1].get()

        if is_issue:
            extract_bid = f"select bid from {self.book_table}"
        else:
            extract_bid = f"select bid from {self.issued_table}"

        status = False
        try:
            self.cur.execute(extract_bid)
            self.con.commit()
            for i in self.cur:
                self.all_bid.append(i[0])

            if bid in self.all_bid:
                check_avail = f"select status from {self.book_table} where " \
                              f"bid = '{bid}'"
                self.cur.execute(check_avail)
                self.con.commit()
                check = None
                for i in self.cur:
                    check = i[0]

                if (is_issue and check == 'avail'
                        or not is_issue and check == 'issued'):
                    status = True
                else:
                    status = False
            else:
                messagebox.showinfo("Error", "Book ID not present")
        except MySQLError as err:
            messagebox.showinfo("Error", "Can't fetch Book IDs")
            print(err)

        if is_issue:
            issue_sql = f"insert into {self.issued_table} values ('{bid}'," \
                        f"'{issue_to}')"
            up_status = f"update {self.book_table} set status = 'issued' " \
                        f"where bid = '{bid}'"
        else:
            issue_sql = f"delete from {self.issued_table} where bid = '{bid}'"
            up_status = f"update {self.book_table} set status = 'avail' " \
                        f"where bid = '{bid}'"

        try:
            if bid in self.all_bid and status:
                self.cur.execute(issue_sql)
                self.con.commit()
                self.cur.execute(up_status)
                self.con.commit()
                if is_issue:
                    msg = "Book Issued Successfully"
                else:
                    msg = "Book Returned Successfully"
                state = 'Success'
            else:
                if is_issue:
                    msg = "Book Already Issued"
                else:
                    msg = "Please check the book ID"
                state = "Message"
            messagebox.showinfo(state, msg)
        except MySQLError as err:
            messagebox.showinfo(
                "Search Error", "The value entered is wrong, Try again"
            )
            print(err)
        self.all_bid.clear()
        destroy()

    def read(self):
        """Read the db and yield a list of all the books in the library"""
        self.connect()
        get_books = f"select * from {self.book_table}"
        try:
            self.cur.execute(get_books)
            self.con.commit()
            for i in self.cur:
                yield i
        except MySQLError as err:
            messagebox.showinfo("Failed to fetch files from database")
            print(err)
