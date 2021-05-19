"""The tkinter tools of the Library Management System
-----------------------------

About this Module
------------------
The goal of this module is to provide constant and parent classes to the views
of the Library application.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-05-17"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from tkinter import BOTH, Button, Canvas, Entry, Frame, Label, Tk, YES

from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 600
MIN_HEIGHT = 400
MIN_WIDTH = 400


class Window(Tk):
    """The Window view of the Library Management System"""

    def __init__(self):
        """Initialize home window components"""
        super(Window, self).__init__()
        self.image = None
        self.image_tk = None
        self.background = None
        self.title("labesoft Library")
        self.minsize(width=MIN_WIDTH, height=MIN_HEIGHT)
        self.geometry(f"{WIDTH}x{HEIGHT}")

    def prepare_image(self, image_filename):
        """Prepares the proper size for the image loaded

        Only loads the image if it does yet exists

        :param image_filename: the name of the image file
        """
        if not self.image:
            self.image = Image.open(image_filename)
        self.image = self.image.resize((WIDTH, HEIGHT), Image.ANTIALIAS)

    def create_bg(self, image_filename=None, color="white"):
        """Creates a background for the window using label or a canvas

        It uses a canvas when a filename is provided and a canvas otherwise.

        :param image_filename: the file to use as background
        :param color: the color of the background
        """
        if image_filename:
            self.prepare_image(image_filename)
            self.image_tk = ImageTk.PhotoImage(self.image)
            self.background = Label(self, bg=color, image=self.image_tk)
        else:
            self.background = Canvas(self)
            self.background.config(bg=color)
        self.background.pack(expand=YES, fill=BOTH)

    def create_header(self, title):
        """Creates the header frame on top of the window with a title

        :param title: a title string
        """
        frame = Frame(self, bg="#FFBB00", bd=5)
        frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        header_label = Label(frame, text=title, bg='black', fg='white',
                             font=('Courier', 15))
        header_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    def create_button(self, text, command, relx=0.28, rely=0.9, relw=0.45,
                      relh=0.1, bg='black', fg='white'):
        """Utility method to create a button

        :param text: the text of the button
        :param command: the command trigger of the button
        :param relx, rely, relw, relh: positions and dimensions
        :param bg, fg: background and foreground colors
        """
        btn = Button(
            self, text=text, bg=bg, fg=fg, command=command
        )
        btn.place(relx=relx, rely=rely, relwidth=relw, relheight=relh)

    def create_submit_quit_buttons(self, submit_func):
        """Creates both the submit button and the quit button

        :param submit_func: the command trigger of the submit button
        """
        # Submit button
        self.create_button(
            "SUBMIT", submit_func, relw=0.18, relh=0.08, bg='#d1ccc0',
            fg='black'
        )
        # Quit button
        self.create_button(
            "Quit", self.destroy, relx=0.53, relw=0.18, relh=0.08,
            bg='#f7f1e3', fg='black',
        )

    def on_configure(self, event):
        """Resize the background of the window from a configure callback

        :param event: the event args of the callback
        """
        if event.widget == self.background:
            self.image = self.image.resize((event.width, event.height))
            self.image_tk = ImageTk.PhotoImage(self.image)
            self.background.configure(image=self.image_tk)


class Dialog:
    """The dialog view of the Library Management System"""

    def __init__(self):
        """Initialize fields of the dialog view"""
        self.content_frame = None

    def create_book_form(self, entries_args):
        """Create the book form content to embed in the dialog

        :param entries_args:
        :return:
        """
        self.content_frame = self.create_content_frame()
        lines = []
        for input_arg in entries_args:
            lines += [
                self.create_bookform_line(input_arg[0], input_arg[1])
            ]
        return lines

    def create_bookform_line(self, text, rely):
        """Creates a line consisting of a label and an entry

        :param text: the text of the label
        :param rely: the y position of the label
        :return: an initialized and positioned line
        """
        lb1 = Label(self.content_frame, text=text, bg='black', fg='white')
        lb1.place(relx=0.05, rely=rely, relheight=0.08)
        book_entry = Entry(self.content_frame)
        book_entry.place(relx=0.3, rely=rely, relwidth=0.62, relheight=0.08)
        return book_entry

    def create_content_frame(self):
        """Creates the frame embedding the content of the dialog

        :return: an initialized and positioned frame
        """
        frame = Frame(self, bg='black')
        frame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
        return frame
