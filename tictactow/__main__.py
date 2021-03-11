"""The Tic Tac Tow Game Application
-----------------------------

About this Module
------------------
This module is the main entry point of The Tic Tac Tow Game Application.

"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-09"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

# Import modules
import tkinter.messagebox as msg
from functools import partial
from tkinter import Button, Label, Tk

buttons = {}


def check_winner(panel_list, sign):
    """Analyses the grid and tells if a player is winning the game

    :param panel_list: the grid
    :param sign: the sign on the grid
    :return: True if 3 signs align, False otherwise
    """
    return ((panel_list[1] == panel_list[2] == panel_list[3] == sign)
            or (panel_list[1] == panel_list[4] == panel_list[7] == sign)
            or (panel_list[1] == panel_list[5] == panel_list[9] == sign)
            or (panel_list[2] == panel_list[5] == panel_list[8] == sign)
            or (panel_list[3] == panel_list[6] == panel_list[9] == sign)
            or (panel_list[3] == panel_list[5] == panel_list[7] == sign)
            or (panel_list[4] == panel_list[5] == panel_list[6] == sign)
            or (panel_list[7] == panel_list[8] == panel_list[9] == sign))


def check_result(digit):
    """Main switch

    :param digit:
    :return:
    """
    global mark, digits
    if digit in digits:
        turn_count = 9 - len(digits)
        digits.remove(digit)
        if turn_count % 2 == 0:
            mark = 'X'
            panels[digit] = mark
        else:
            mark = 'O'
            panels[digit] = mark
        buttons[digit].config(text=mark)
        end_turn(len(digits), mark)


def end_turn(turn_remaining, sign):
    if check_winner(panels, sign) and sign == 'X':
        msg.showinfo("Result", "Player1 wins")
        root.destroy()
    elif check_winner(panels, sign) and sign == 'O':
        msg.showinfo("Result", "Player2 wins")
        root.destroy()
    elif count == 0:
        msg.showinfo("Result", "Match Tied")
        root.destroy()


def create_buttons():
    for i, index in zip(range(9), range(1, 10)):
        buttons[index] = Button(root, width=15, font='Times 16 bold', height=7)
        buttons[index].configure(command=partial(check_result, index))
        row = int(i / 3) + 1
        col = i % 3 + 1
        buttons[index].grid(row=row, column=col)


if __name__ == '__main__':
    """Main entry point of tictactow"""
    # Initialize window
    root = Tk()
    root.title('TIC-TAC-TOW---labesoft')
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mark = ''
    count = 1
    panels = ["panel"] * 10

    # Function to check result
    # Function to check the winner
    # Define labels and buttons
    Label(root, text="player1 : X", font="times 15").grid(row=0, column=1)
    Label(root, text="player2 : O", font="times 15").grid(row=0, column=2)
    create_buttons()
    root.mainloop()
    # Add unit tests
