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
SCISSORS = 'scissors'
PAPER = 'paper'
ROCK = 'rock'
INVALID_CHOICE = 'invalid: choose any one -- rock, paper, scissors'
WIN_GAME_3 = 'you win ,computer select paper'
LOOSE_GAME_3 = 'you loose,computer select rock'
WIN_GAME_2 = 'you win,computer select rock'
LOOSE_GAME_2 = 'you loose,computer select scissors'
WIN_GAME_1 = 'you win,computer select scissors'
LOOSE_GAME_1 = 'you loose,computer select paper'
TIE_GAME = 'tie,you both select same'


def play():
    """Start the game

    :return: None
    """
    comp_pick = pick_comp_choice()
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set(TIE_GAME)
    elif user_pick == ROCK and comp_pick == PAPER:
        Result.set(LOOSE_GAME_1)
    elif user_pick == ROCK and comp_pick == SCISSORS:
        Result.set(WIN_GAME_1)
    elif user_pick == PAPER and comp_pick == SCISSORS:
        Result.set(LOOSE_GAME_2)
    elif user_pick == PAPER and comp_pick == ROCK:
        Result.set(WIN_GAME_2)
    elif user_pick == SCISSORS and comp_pick == ROCK:
        Result.set(LOOSE_GAME_3)
    elif user_pick == SCISSORS and comp_pick == PAPER:
        Result.set(WIN_GAME_3)
    else:
        Result.set(INVALID_CHOICE)


def reset():
    """Reset the game

    :return: None
    """
    Result.set("")
    user_take.set("")


def exit_rps():
    """Exit the game by destroying the root tk

    :return: None
    """
    root.destroy()


def pick_comp_choice():
    """Pick the computer choice and returns it.

    :return: str representation of the randam choosen computer pick
    """
    pick = random.randint(1, 3)
    if pick == 1:
        pick = ROCK
    elif pick == 2:
        pick = PAPER
    else:
        pick = SCISSORS
    return pick


if __name__ == '__main__':
    """Main entry point of rpsgame"""
    # Initialize window
    root = Tk()
    Result = StringVar()
    user_take = StringVar()

    root.geometry('400x400')
    root.resizable(0, 0)
    root.title('DataFlair-Rock,Paper,Scissors')
    root.config(bg='seashell3')
    Label(root, text='Rock, Paper ,Scissors', font='arial 20 bold',
          bg='seashell2').pack()

    # Code for user choice
    Label(root, text='choose any one: rock, paper ,scissors',
          font='arial 15 bold', bg='seashell2').place(x=20, y=70)
    Entry(root, font='arial 15', textvariable=user_take,
          bg='antiquewhite2').place(x=90, y=130)

    # Define buttons
    Entry(root, font='arial 10 bold', textvariable=Result, bg='antiquewhite2',
          width=50, ).place(x=25, y=250)
    Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4',
           command=play).place(x=150, y=190)
    Button(root, font='arial 13 bold', text='RESET', padx=5, bg='seashell4',
           command=reset).place(x=70, y=310)
    Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4',
           command=exit_rps).place(x=230, y=310)
    root.mainloop()
