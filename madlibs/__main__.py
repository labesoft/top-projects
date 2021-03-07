"""Main module of the Mad Libs Generator Game
-----------------------------

About this Module
------------------
These are the required steps to build Mad Libs generator python project:
- Import modules
- Create a display window
- Define functions
- Create buttons

"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-06"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from tkinter import Tk, Label, Button


def madlib1():
    animals = input('enter a animal name : ')
    profession = input('enter a profession name: ')
    cloth = input('enter a piece of cloth name: ')
    things = input('enter a thing name: ')
    name = input('enter a name: ')
    place = input('enter a place name: ')
    verb = input('enter a verb in ing form: ')
    food = input('food name: ')
    print(
        "say {0}, the photographer said as the camera flashed! {1} and I had\n"
        "gone to {2} to get our photos taken on my birthday. The first photo\n"
        "we really wanted was a picture of us dressed as {3} pretending to be\n"
        "a {4}. when we saw the second photo, it was exactly what I wanted. \n"
        "We both looked like {5} wearing {6} and {7} --exactly what I had in \n"
        "mind".format(
            food, name, place, animals, profession, things, cloth, verb))


def madlib2():
    adjective = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person = input('enter a person name : ')
    adjective1 = input('enter a adjective : ')
    insect = input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')
    print(
        "Last night I dreamed I was a {0} butterfly with {1} splocthes that\n"
        " looked like {2} .I flew to {3} with my bestfriend and {4} who was a\n"
        " {5} {6} .We ate some {7} when we got there and then decided to {8}\n"
        " and the dream ended when I said-- lets {9}.".format(
            adjective, color, thing, place, person, adjective1, insect, food,
            verb, verb))


def madlib3():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')

    print(
        "Today we picked apple from {0}'s Orchard. I had no idea there were\n"
        " so many different varieties of apples. I ate {1} apples straight\n"
        " off the tree that tested like {2}. Then there was a {3} apple that \n"
        " looked like a {4}.When our bag were full, we went on a free hay\n"
        " ride to {5} and back. It ended at a hay pile where we got to {6}\n"
        " {7}. I can hardly wait to get home and cook with the apples. We are\n"
        " going to make appple {8} and {9} pies!.".format(
            person, color, foods, adjective, thing, place, verb, adverb, food,
            things))


if __name__ == '__main__':
    """Main entry point of madlibs"""
    root = Tk()
    root.geometry('300x300')
    root.title('DataFlair-Mad Libs Generator')
    Label(root, text='Mad Libs Generator \n Have Fun!',
          font='arial 20 bold').pack()
    Label(root, text='Click Any One :', font='arial 15 bold').place(x=40, y=80)
    Button(root, text='The Photographer', font='arial 15', command=madlib1,
           bg='ghost white').place(x=60, y=120)
    Button(root, text='apple and apple', font='arial 15', command=madlib3,
           bg='ghost white').place(x=70, y=180)
    Button(root, text='The Butterfly', font='arial 15', command=madlib2,
           bg='ghost white').place(x=80, y=240)
    root.mainloop()
