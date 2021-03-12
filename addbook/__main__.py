"""The Address Book Application
-----------------------------

About this Module
------------------
This module is the main entry point of The Address Book Application.

"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-09"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

# Importing module
from tkinter import (
    BOTH, Button, END, Entry, Frame, LEFT, Label, Listbox, RIGHT, Scrollbar,
    StringVar,
    Tk,
    VERTICAL, Y
)

contactlist = [
    ['Paul Henderson', '12121212121'],
    ['Wayne Gretsky', '19999999999'],
    ['Mario Lemieux', '16666666666'],
    ['Sidney Crosby', '18787878787'],
    ['Connor McDavid', '19797979797'],
    ['Auston Matthews', '13434343434'],
]


def add_contact():
    """Defines function used to add new contact"""
    contactlist.append([name.get(), number.get()])
    select_set()


def delete():
    """Defines function will delete selected contact"""
    del contactlist[get_selection_index()]
    select_set()


def edit():
    """Defines function will edit existing contact"""
    contactlist[get_selection_index()] = [name.get(), number.get()]
    select_set()


def exit_book():
    """Destroy the mainloop"""
    root.destroy()


def reset():
    """Set the name and number field to empty string"""
    name.set('')
    number.set('')


def select_set():
    """Sort and fill the managed contactlist"""
    contactlist.sort()
    select.delete(0, END)
    for current_name, phone in contactlist:
        select.insert(END, current_name)


def get_selection_index():
    """Defines function used to return selected value"""
    return int(select.curselection()[0])


def view():
    """Defines function will view selected contact"""
    current_name, phone = contactlist[get_selection_index()]
    name.set(current_name)
    number.set(phone)


if __name__ == '__main__':
    """Main entry point of addbook"""
    # Initializing window
    root = Tk()
    frame = Frame(root)
    scroll = Scrollbar(frame, orient=VERTICAL)
    select = Listbox(frame, yscrollcommand=scroll.set, height=12)
    name = StringVar()
    number = StringVar()

    root.geometry('400x400')
    root.config(bg='SlateGray3')
    root.resizable(0, 0)
    root.title('DataFlair-AddressBook')

    frame.pack(side=RIGHT)

    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH, expand=1)

    # Define buttons
    Label(root, text='NAME', font='arial 12 bold', bg='SlateGray3').place(x=30,
                                                                          y=20)
    Entry(root, textvariable=name).place(x=100, y=20)
    Label(root, text='PHONE NO.', font='arial 12 bold', bg='SlateGray3').place(
        x=30, y=70)
    Entry(root, textvariable=number).place(x=130, y=70)
    Button(root, text="ADD", font='arial 12 bold', bg='SlateGray4',
           command=add_contact).place(x=50, y=110)
    Button(root, text="EDIT", font='arial 12 bold', bg='SlateGray4',
           command=edit).place(x=50, y=260)
    Button(root, text="DELETE", font='arial 12 bold', bg='SlateGray4',
           command=delete).place(x=50, y=210)
    Button(root, text="VIEW", font='arial 12 bold', bg='SlateGray4',
           command=view).place(x=50, y=160)
    Button(root, text="EXIT", font='arial 12 bold', bg='tomato',
           command=exit_book).place(x=300, y=320)
    Button(root, text="RESET", font='arial 12 bold', bg='SlateGray4',
           command=reset).place(x=50, y=310)
    select_set()
    root.mainloop()
