"""The views of the library application
-----------------------------

About this Module
------------------
The goal of this module is to regroup windows and dialogs of the library.
This includes the home window, the book list dialog, the delete book dialog,
the issue book dialog, the new book dialog and the return book dialog.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-05-18"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from functools import partial
from tkinter import Button, Frame, Label

from booksys.models import Book
from booksys.tktools import Dialog, Window


class NewBookDialog(Window, Dialog):
    """This display the new book form fields and action buttons"""

    def create_components(self, book_form_args=None):
        """Creates UI components of the new book view

        :param book_form_args: new book form content
        """
        self.create_bg(color="#ff6e40")
        self.create_header(title="Add New Book")
        create_book_form = self.create_book_form(book_form_args)
        submit_func = partial(Book().create, create_book_form, self.destroy)
        self.create_submit_quit_buttons(submit_func)


class DeleteBookDialog(Window, Dialog):
    """This class manages how to delete a book from the library"""

    def create_components(self, book_form_args=None):
        """Create UI components of the delete book dialog

        :param book_form_args: delete book form content
        """
        self.create_bg(color="#006B38")
        self.create_header(title="Delete Book")
        delete_book_form = self.create_book_form(book_form_args)
        func = partial(Book().delete, delete_book_form, self.destroy)
        self.create_submit_quit_buttons(func)


class IssueBookDialog(Window, Dialog):
    """This class manages how to issue a book from the library"""

    def create_components(self, book_form_args=None):
        """Create UI component for the issue book dialog

        :param book_form_args: issue book form content
        :return:
        """
        self.create_bg(color="#D6ED17")
        self.create_header(title="Issue Book")
        issue_book_form = self.create_book_form(book_form_args)
        func = partial(Book().update, issue_book_form, self.destroy)
        self.create_submit_quit_buttons(func)


class Home(Window):
    """The home window of the book library system"""

    def create_components(self, btn_list=None):
        """Create UI components of the home window

        It also bind the resize behavior of the page (mostly for background
        image)

        :param btn_list: the list of buttons to create
        """
        self.create_bg("lib.jpg")
        self.create_header(title="Welcome to \n labesoft Library")
        for i, btn_info in enumerate(btn_list):
            self.create_button(btn_info[0], btn_info[1], rely=0.3 + 0.1 * i)
        self.bind("<Configure>", self.on_configure)


class ReturnBookDialog(Window, Dialog):
    """This class manages how to return a book to the library"""

    def create_components(self, book_form_args=None):
        """Creates UI components of the return book dialog

        :param book_form_args: the return book form content
        """
        self.create_bg(color="#006B38")
        self.create_header(title="Return Book")
        return_book_form = self.create_book_form(book_form_args)
        func = partial(Book().update, return_book_form, self.destroy)
        self.create_submit_quit_buttons(func)


class BooklistDialog(Window):
    """This class lists the books in this library"""

    def create_components(self, args=None):
        """Create UI components of the book list dialog

        :param args: unused here
        """
        self.create_bg(color="#12a4d9")
        self.create_header(title="View Books")
        label_frame = Frame(self, bg='black')
        label_frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
        y = 0.25
        Label(label_frame,
              text="%-10s%-40s%-30s%-20s" % (
                  'BID', 'Title', 'Author', 'Status'),
              bg='black', fg='white').place(relx=0.07, rely=0.1)
        Label(
            label_frame,
            text="-------------------------------------------------------------"
                 "---------------",
            bg='black', fg='white'
        ).place(relx=0.05, rely=0.2)
        for i in Book().read():
            Label(label_frame,
                  text="%-10s%-30s%-30s%-20s" % (i[0], i[1], i[2], i[3]),
                  bg='black', fg='white').place(relx=0.07, rely=y)
            y += 0.1

        quit_btn = Button(
            self, text="Quit", bg='#f7f1e3', fg='black', command=self.destroy
        )
        quit_btn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
