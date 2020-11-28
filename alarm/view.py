"""The view of an alarm
--------------------

About this Project
------------------
The objective of this project is to recreate an alarm that a user could set
interactively and which will ring back at this preset time.

Project structure
-----------------
*alarm/*
    **__main__.py**:
        The application of an alarm
    **alarm_test.py**:
        The tests of an alarm
    **controller.py**:
        The controller of an alarm
    **model.py**:
        The model of an alarm
    **-->** **view.py**:
        The GUI of an alarm

About this module
-----------------
The objective of our project is to implement an alarm using Python. Python
consists of some very innovative libraries such as logging and tkinter which
helped us to build the project using the current date and time as well as to
provide a user interface to set the alarm according to the requirement in
24-hour format.

File structure
--------------
*imports*
    **tkinter**
        module belongs is a GUI tool that belongs to the Python's Standard
        library. It helped us creating a dialog box with information we want to
        provide/get to/from the users.

*constants*
    ***_ENTRY_ROW**
        Row position of entry objects
    **MIN_***
        Minimum dimension of graphic objects
    **PAD_X**
        Padding columns
    **TITLE**
        The title of the window

*class*
    **AlarmView**
        'The GUI of an alarm using tkinter'
    **__init__(self)**
        'Initialize the tk window, variables, title, geometry'
    **create_gui(self, button_callback)**
        'Creates the content of this tkinter object'
    **create_labels(self)**
        'Creates labels essential to the alarm'
    **def init_entry_vars(self)**
        'Initialize time attributes to a StringVar component'
    **create_entries(self)**
        'Creates the entries essentials to set the alarm on the alarm'
    **create_button(self, button_callback)**
        'Creates the button that activates the alarm on the alarm'
"""
import tkinter
from tkinter import Label, StringVar, Entry, Button
from tkinter.font import Font

# View constants
ENTRY_ROW = 1
ENTRY_WIDTH = 2
LABEL_ENTRY_ROW = 0
MIN_WIDTH = 500
MIN_HEIGHT = 350
PAD_X = 10
TITLE = "LABESOFT Alarm"


class AlarmView(tkinter.Frame):
    """The GUI of an alarm using tkinter"""
    def __init__(self):
        """Initialize the tk window, variables, title, geometry

        :return: None
        """
        self.master = tkinter.Tk()
        self.master.title(TITLE)
        self.master.config(bg="white")
        self.master.minsize(MIN_WIDTH, MIN_HEIGHT)
        super().__init__(self.master)
        self.hour_var = None
        self.min_var = None
        self.sec_var = None
        self.pack(pady=20)
        self.config(bg="white")

    def create_gui(self, button_callback):
        """Creates the content of this tkinter object"""
        frame = tkinter.Frame(self)
        frame.config(bg="white")
        self.create_labels(frame)
        self.init_entry_vars()
        self.create_entries(frame)
        frame.pack(pady=20)
        self.create_button(button_callback)

    def create_labels(self, f):
        """Creates labels essential to the alarm

        :return: None
        """
        f1 = Font(self, font=("Helevetica", 40, "bold"))
        f2 = Font(self, font=("Arial", 25, "italic"))

        l1 = Label(self, text="  When to wake you up ?  ", fg="black", bg="lightgray", font=f1)
        l2 = Label(self, text="Enter time in 24 hour format!", fg="green", bg="white", font=("Arial", 30, "italic"))
        le1 = Label(f, text="Hour", bg="white",  font=f2)
        le2 = Label(f, text="Min", bg="white", font=f2)
        le3 = Label(f, text="Sec", bg="white", font=f2)

        l1.pack(pady=20)
        l2.pack(pady=10)
        le1.grid(row=LABEL_ENTRY_ROW, column=0, padx=PAD_X)
        le2.grid(row=LABEL_ENTRY_ROW, column=1, padx=PAD_X)
        le3.grid(row=LABEL_ENTRY_ROW, column=2, padx=PAD_X)

    def init_entry_vars(self):
        """Initialize time attributes to a StringVar component

        :return: None
        """
        self.hour_var = StringVar()
        self.min_var = StringVar()
        self.sec_var = StringVar()

    def create_entries(self, f):
        """Creates the entries essentials to set the alarm on the alarm

        :return: None
        """
        f1 = Font(self, font=("Arial", 50, "bold"))
        e1 = Entry(f, textvariable=self.hour_var, bg="lightyellow", fg="black", font=f1, justify="center",
                   width=ENTRY_WIDTH)
        e2 = Entry(f, textvariable=self.min_var, bg="lightyellow", fg="black", font=f1, justify="center",
                   width=ENTRY_WIDTH)
        e3 = Entry(f, textvariable=self.sec_var, bg="lightyellow", fg="black", font=f1, justify="center",
                   width=ENTRY_WIDTH)
        e1.grid(row=ENTRY_ROW, column=0, padx=PAD_X)
        e2.grid(row=ENTRY_ROW, column=1, padx=PAD_X)
        e3.grid(row=ENTRY_ROW, column=2, padx=PAD_X)

    def create_button(self, func):
        """Creates the button that activates the alarm on the alarm

        :return: None
        """
        b1 = Button(self, text="Set Alarm", font=("Arial", 30, "bold"), fg="black", bd=17, height=1, width=10, command=func)
        b1.pack(pady=25)
