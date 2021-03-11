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
from tkinter import BOTH, Button, Canvas, Entry, Frame, Label, Tk, messagebox

import pymysql
from pymysql import MySQLError


def connect():
    con = pymysql.connect(
        host="localhost", user="bookuser", password="bookuser", database="db"
    )
    return con, con.cursor(), "books"


def insert_book_db(book_info1, book_info2, book_info3, book_info4, root):
    con, cur, book_table = connect()
    bid = book_info1.get()
    title = book_info2.get()
    author = book_info3.get()
    status = book_info4.get()
    status = status.lower()

    q = "insert into {} values ('{}','{}','{}','{}')"
    insert_books = q.format(book_table, bid, title, author, status)
    try:
        cur.execute(insert_books)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except MySQLError as err:
        messagebox.showinfo("Error", "Can't add data into Database")
        print(err)
    print(bid)
    print(title)
    print(author)
    print(status)
    root.destroy()


def add_book():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    canvas1 = Canvas(root)

    canvas1.config(bg="#ff6e40")
    canvas1.pack(expand=True, fill=BOTH)

    heading_frame1 = Frame(root, bg="#FFBB00", bd=5)
    heading_frame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    heading_label = Label(heading_frame1, text="Add Books", bg='black',
                          fg='white', font=('Courier', 15))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    label_frame = Frame(root, bg='black')
    label_frame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Book ID
    lb1 = Label(label_frame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    book_info1 = Entry(label_frame)
    book_info1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Title
    lb2 = Label(label_frame, text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    book_info2 = Entry(label_frame)
    book_info2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Book Author
    lb3 = Label(label_frame, text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    book_info3 = Entry(label_frame)
    book_info3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Book Status
    lb4 = Label(label_frame, text="Status(Avail/issued) : ", bg='black',
                fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    book_info4 = Entry(label_frame)
    book_info4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    func = partial(
        insert_book_db, book_info1, book_info2, book_info3, book_info4, root
    )
    submit_btn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black',
                        command=func)
    submit_btn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    quit_btn = Button(root, text="Quit", bg='#f7f1e3', fg='black',
                      command=root.destroy)
    quit_btn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    root.mainloop()
