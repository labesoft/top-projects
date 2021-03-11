"""To delete books from the library
-----------------------------

About this module
-----------------
This module manages deleting books from the library

File structure
--------------
*import*

*constant*
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-11"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from functools import partial
from tkinter import (
    BOTH, Button, Canvas, END, Entry, Frame, Label, Tk,
    messagebox
)

import pymysql
from pymysql import MySQLError


class DeleteBook:
    """This class manages how to delete a book from the library"""
    pass


def connect():
    con = pymysql.connect(
        host="localhost", user="bookuser", password="bookuser", database="db"
    )
    return con, con.cursor(), "books_issued", "books"


def delete_book(book_info1, root):
    con, cur, issue_table, book_table = connect()
    bid = book_info1.get()

    delete_sql = f"delete from {book_table} where bid = '{bid}'"
    delete_issue = f"delete from {issue_table} where bid = '{bid}'"
    try:
        cur.execute(delete_sql)
        con.commit()
        cur.execute(delete_issue)
        con.commit()
        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except MySQLError as err:
        messagebox.showinfo("Please check Book ID")
        print(err)

    print(bid)
    book_info1.delete(0, END)
    root.destroy()


def delete():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    canvas1 = Canvas(root)
    canvas1.config(bg="#006B38")
    canvas1.pack(expand=True, fill=BOTH)

    heading_frame1 = Frame(root, bg="#FFBB00", bd=5)
    heading_frame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    heading_label = Label(heading_frame1, text="Delete Book", bg='black',
                          fg='white', font=('Courier', 15))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_frame = Frame(root, bg='black')
    label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(label_frame, text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    book_info1 = Entry(label_frame)
    book_info1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    func = partial(delete_book, book_info1, root)
    submit_btn = Button(
        root, text="SUBMIT", bg='#d1ccc0', fg='black', command=func
    )
    submit_btn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quit_btn = Button(
        root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy
    )
    quit_btn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    root.mainloop()
