"""The base windows of the Library application
-----------------------------

About this Module
------------------
The goal of this module is to build the home and dialog view of the Library
application.
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


class Home(Tk):
    def __init__(self):
        super().__init__()
        self.image = None
        self.image_tk = None
        self.background = None
        self.title("labesoft Library")
        self.minsize(width=MIN_WIDTH, height=MIN_HEIGHT)
        self.geometry(f"{WIDTH}x{HEIGHT}")

    def create_components(self, btn_list=None):
        self.create_bg("lib.jpg")
        self.create_header(title="Welcome to \n labesoft Library")
        for i, btn_info in enumerate(btn_list):
            self.create_button(btn_info[0], btn_info[1], rely=0.3 + 0.1 * i)
        self.bind("<Configure>", self.resize_bg)

    def prepare_image(self, image_filename):
        if not self.image:
            self.image = Image.open(image_filename)
        self.image = self.image.resize((WIDTH, HEIGHT), Image.ANTIALIAS)

    def create_bg(self, image_filename=None, color="white"):
        if image_filename:
            self.prepare_image(image_filename)
            self.image_tk = ImageTk.PhotoImage(self.image)
            self.background = Label(self, bg=color, image=self.image_tk)
        else:
            self.background = Canvas(self)
            self.background.config(bg=color)
        self.background.pack(expand=YES, fill=BOTH)

    def create_header(self, title):
        frame = Frame(self, bg="#FFBB00", bd=5)
        frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        header_label = Label(frame, text=title, bg='black', fg='white',
                             font=('Courier', 15))
        header_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    def create_button(self, text, command, relx=0.28, rely=0.9, relw=0.45,
                      relh=0.1, bg='black', fg='white'):
        btn = Button(
            self, text=text, bg=bg, fg=fg, command=command
        )
        btn.place(relx=relx, rely=rely, relwidth=relw, relheight=relh)

    def create_submit_quit_buttons(self, submit_func):
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

    def resize_bg(self, event):
        if event.widget == self.background:
            self.image = self.image.resize((event.width, event.height))
            self.image_tk = ImageTk.PhotoImage(self.image)
            self.background.configure(image=self.image_tk)


class Dialog:
    def __init__(self):
        self.label_frame = None

    def create_entries(self, entries_args):
        self.create_entries_frame()
        book_entries = []
        for input_arg in entries_args:
            book_entries += [
                self.create_bookentry_line(input_arg[0], input_arg[1])
            ]
        return book_entries

    def create_bookentry_line(self, text, rely):
        lb1 = Label(self.label_frame, text=text, bg='black', fg='white')
        lb1.place(relx=0.05, rely=rely, relheight=0.08)
        book_entry = Entry(self.label_frame)
        book_entry.place(relx=0.3, rely=rely, relwidth=0.62, relheight=0.08)
        return book_entry

    def create_entries_frame(self):
        self.label_frame = Frame(self, bg='black')
        self.label_frame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
