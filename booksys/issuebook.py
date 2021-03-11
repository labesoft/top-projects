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
from tkinter import BOTH, Button, Canvas, Entry, Frame, Label, Tk, messagebox

import pymysql
from pymysql import MySQLError


class IssueBook:
    """This class manages how to issue a book from the library"""
    pass


def connect():
    con = pymysql.connect(
        host="localhost", user="bookuser", password="bookuser", database="db"
    )
    return con, con.cursor(), "books_issued", "books", []


def issue(inf1, inf2, label_frame, lb1, root):
    con, cur, issue_table, book_table, all_bid = connect()
    bid = inf1.get()
    issue_to = inf2.get()
    label_frame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

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
            root.destroy()
        else:
            all_bid.clear()
            messagebox.showinfo('Message', "Book Already Issued")
            root.destroy()
            return
    except MySQLError as err:
        messagebox.showinfo(
            "Search Error", "The value entered is wrong, Try again"
        )
        print(err)
    print(bid)
    print(issue_to)
    all_bid.clear()


def issue_book():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    canvas1 = Canvas(root)
    canvas1.config(bg="#D6ED17")
    canvas1.pack(expand=True, fill=BOTH)
    heading_frame1 = Frame(root, bg="#FFBB00", bd=5)
    heading_frame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    heading_label = Label(heading_frame1, text="Issue Book", bg='black',
                          fg='white', font=('Courier', 15))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    label_frame = Frame(root, bg='black')
    label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(label_frame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(label_frame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student name
    lb2 = Label(label_frame, text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(label_frame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Issue Button
    func = partial(issue, inf1, inf2, label_frame, lb1, root)
    issue_btn = Button(root, text="Issue", bg='#d1ccc0', fg='black',
                       command=func)
    issue_btn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quit_btn = Button(root, text="Quit", bg='#aaa69d', fg='black',
                      command=root.destroy)
    quit_btn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    root.mainloop()
