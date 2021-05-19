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


class AddressBookView(Tk):
    """The view of an address book using Tkinter"""

    def __init__(self):
        """Initialize and configure the address book view components"""
        super(AddressBookView, self).__init__()
        # Initializing components
        self.frame = Frame(self)
        self.scroll = Scrollbar(self.frame, orient=VERTICAL)
        self.select = Listbox(
            self.frame, yscrollcommand=self.scroll.set, height=12
        )
        self.name = StringVar()
        self.number = StringVar()

        # Configure componenets
        self.configure_parent()
        self.frame.pack(side=RIGHT)
        self.scroll.config(command=self.select.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.select.pack(side=LEFT, fill=BOTH, expand=1)

        # Create content
        self.create_input_lines()
        self.create_buttons()
        self.update_contactlist()

    def configure_parent(self):
        """Configure field properties of the parent tk window"""
        self.geometry('400x400')
        self.config(bg='SlateGray3')
        self.resizable(0, 0)
        self.title('labesoft address book')

    def create_input_lines(self):
        """Create phone entry lines"""
        self.create_input_line(('NAME', 30, 20), (self.name, 100, 20))
        self.create_input_line(('PHONE NO.', 30, 70), (self.number, 130, 70))

    def create_input_line(self, lbl_info, entry_info):
        """Create an address book input line

        :param lbl_info: information used to create and place the label
                        (text, x, y)
        :param entry_info: information used to create and place the entry
                            (textvariable, x, y)
        """
        # Create the label placed to the left
        Label(
            self, text=lbl_info[0], font='arial 12 bold', bg='SlateGray3'
        ).place(x=lbl_info[1], y=lbl_info[2])

        # Create the text field placed to the right
        Entry(
            self, textvariable=entry_info[0]
        ).place(x=entry_info[1], y=entry_info[2])

    def create_buttons(self):
        """Create and place action buttons"""
        self.create_button("ADD", self.add_contact)
        self.create_button("EDIT", self.edit, y=260)
        self.create_button("DELETE", self.delete, y=210)
        self.create_button("VIEW", self.view, y=160)
        self.create_button("EXIT", self.exit_book, bg='tomato', x=300, y=320)
        self.create_button("RESET", self.reset, y=310)

    def create_button(self, text, command, bg="SlateGray4", x=50, y=110):
        """Create an address book button

        :param text: text displayed on a button
        :param command: command trigger by the button
        :param bg: background color of the button
        :param x: x position of the button in the view
        :param y: y position of the button in the view
        """
        Button(
            self, text=text, font='arial 12 bold', bg=bg, command=command
        ).place(x=x, y=y)

    def update_contactlist(self):
        """Sort and fill the managed contactlist"""
        contactlist.sort()
        self.select.delete(0, END)
        for current_name, phone in contactlist:
            self.select.insert(END, current_name)

    def add_contact(self):
        """Defines function used to add new contact"""
        contactlist.append([self.name.get(), self.number.get()])
        self.update_contactlist()

    def delete(self):
        """Defines function will delete selected contact"""
        del contactlist[self.get_selection_index()]
        self.update_contactlist()

    def edit(self):
        """Defines function will edit existing contact"""
        contactlist[self.get_selection_index()] = [self.name.get(),
                                                   self.number.get()]
        self.update_contactlist()

    def exit_book(self):
        """Destroy the mainloop"""
        self.destroy()

    def reset(self):
        """Set the name and number field to empty string"""
        self.name.set('')
        self.number.set('')

    def get_selection_index(self):
        """Defines function used to return selected value"""
        return int(self.select.curselection()[0])

    def view(self):
        """Defines function will view selected contact"""
        current_name, phone = contactlist[self.get_selection_index()]
        self.name.set(current_name)
        self.number.set(phone)


if __name__ == '__main__':
    """Main entry point of addbook"""
    address_book = AddressBookView()
    address_book.mainloop()
