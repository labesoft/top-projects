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


class ReturnBook:
    """This class manages how to return a book to the library"""
    pass


def connect():
    con = pymysql.connect(
        host="localhost", user="bookuser", password="bookuser", database="db"
    )
    return con, con.cursor(), "books_issued", "books", []


def a_return(book_info1, root):
    con, cur, issue_table, book_table, all_bid = connect()
    bid = book_info1.get()
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
    print(bid in all_bid)
    print(status)

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
            root.destroy()
            return
    except MySQLError as err:
        messagebox.showinfo(
            "Search Error", "The value entered is wrong, Try again"
        )
        print(err)
    all_bid.clear()
    root.destroy()


def return_book():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    canvas1 = Canvas(root)
    canvas1.config(bg="#006B38")
    canvas1.pack(expand=True, fill=BOTH)

    heading_frame1 = Frame(root, bg="#FFBB00", bd=5)
    heading_frame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    heading_label = Label(heading_frame1, text="Return Book", bg='black',
                          fg='white', font=('Courier', 15))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    label_frame = Frame(root, bg='black')
    label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lbl1 = Label(label_frame, text="Book ID : ", bg='black', fg='white')
    lbl1.place(relx=0.05, rely=0.5)
    book_info1 = Entry(label_frame)
    book_info1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    func = partial(a_return, book_info1, root)
    submit_btn = Button(
        root, text="Return", bg='#d1ccc0', fg='black', command=func
    )
    submit_btn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quit_btn = Button(root, text="Quit", bg='#f7f1e3', fg='black',
                      command=root.destroy)
    quit_btn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    root.mainloop()
