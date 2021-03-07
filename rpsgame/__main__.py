"""Main module of The Rock Paper Scissors Game
-----------------------------

About this Module
------------------
This module is the main entry point entry of The Rock Paper Scissor Game
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-06"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

import random
from tkinter import Button, Entry, Label, StringVar, Tk


# Define functions
def play():
    """Start the game

    :return: None
    """
    comp_pick = pick_comp_choice()
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')


def reset():
    """Reset the game

    :return: None
    """
    Result.set("")
    user_take.set("")


def exit():
    """Exit the game by destroying the root tk

    :return: None
    """
    root.destroy()


def pick_comp_choice():
    """Pick the computer choice and returns it.

    :return: the randam choosen computer pick
    """
    pick = random.randint(1, 3)
    if pick == 1:
        pick = 'rock'
    elif pick == 2:
        pick = 'paper'
    else:
        pick = 'scissors'
    return pick


if __name__ == '__main__':
    """Main entry point of rpsgame"""
    # Initialize window
    root = Tk()
    root.geometry('400x400')
    root.resizable(0, 0)
    root.title('DataFlair-Rock,Paper,Scissors')
    root.config(bg='seashell3')
    Label(root, text='Rock, Paper ,Scissors', font='arial 20 bold',
          bg='seashell2').pack()

    # Code for user choice
    user_take = StringVar()
    Label(root, text='choose any one: rock, paper ,scissors',
          font='arial 15 bold', bg='seashell2').place(x=20, y=70)
    Entry(root, font='arial 15', textvariable=user_take,
          bg='antiquewhite2').place(x=90, y=130)
    Result = StringVar()

    # Define buttons
    Entry(root, font='arial 10 bold', textvariable=Result, bg='antiquewhite2',
          width=50, ).place(x=25, y=250)
    Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4',
           command=play).place(x=150, y=190)
    Button(root, font='arial 13 bold', text='RESET', padx=5, bg='seashell4',
           command=reset).place(x=70, y=310)
    Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4',
           command=exit).place(x=230, y=310)
    root.mainloop()
