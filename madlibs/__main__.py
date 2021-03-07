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

from tkinter import Button, Label, Tk


ADJECTIVE = 'enter adjective : '
ADVERB = 'enter adverb : '
ANIMAL_NAME = 'enter a animal name : '
COLOR_NAME = 'enter a color name : '
ENTER_A_NAME = 'enter a name: '
FOOD_NAME = 'food name: '
INSECT_NAME = 'enter a insect name : '
PERSON_NAME = 'enter a person name : '
PIECE_OF_CLOTH_NAME = 'enter a piece of cloth name: '
PLACE_NAME = 'enter a place name: '
PROFESSION_NAME = 'enter a profession name: '
THING_NAME = 'enter a thing name :'
VERB_NAME = 'enter a verb name : '
VERB_IN_ING_FORM = 'enter a verb in ing form: '

MAD3 = (
    "Today we picked apple from {0}'s Orchard. I had no idea there were\n"
    "so many different varieties of apples. I ate {1} apples straight\n"
    "off the tree that tested like {2}. Then there was a {3} apple that \n"
    "looked like a {4}.When our bag were full, we went on a free hay\n"
    "ride to {5} and back. It ended at a hay pile where we got to {6}\n"
    "{7}. I can hardly wait to get home and cook with the apples. We are\n"
    "going to make appple {8} and {9} pies!.")
MAD2 = (
    "Last night I dreamed I was a {0} butterfly with {1} splocthes that\n"
    "looked like {2} .I flew to {3} with my bestfriend and {4} who was a\n"
    "{5} {6} .We ate some {7} when we got there and then decided to {8}\n"
    "and the dream ended when I said-- lets {9}.")
MAD1 = (
    "Say {0}, the photographer said as the camera flashed! {1} and I had\n"
    "gone to {2} to get our photos taken on my birthday. The first photo\n"
    "we really wanted was a picture of us dressed as {3} pretending to be\n"
    "a {4}. when we saw the second photo, it was exactly what I wanted.\n"
    "We both looked like {5} wearing {6} and {7} --exactly what I had in\n"
    "mind")


def madlib1():
    """First mad lib sentence construct

    :return: None
    """
    animals = input(ANIMAL_NAME)
    profession = input(PROFESSION_NAME)
    cloth = input(PIECE_OF_CLOTH_NAME)
    things = input(THING_NAME)
    name = input(ENTER_A_NAME)
    place = input(PLACE_NAME)
    verb = input(VERB_IN_ING_FORM)
    food = input(FOOD_NAME)
    print(MAD1.format(food, name, place, animals, profession, things, cloth,
                      verb))


def madlib2():
    """Second mad lib sentence construct

    :return: None
    """
    adjective = input(ADJECTIVE)
    color = input(COLOR_NAME)
    thing = input(THING_NAME)
    place = input(PLACE_NAME)
    person = input(PERSON_NAME)
    adjective1 = input(ADJECTIVE)
    insect = input(INSECT_NAME)
    food = input(FOOD_NAME)
    verb = input(VERB_NAME)
    print(MAD2.format(adjective, color, thing, place, person, adjective1,
                      insect, food, verb, verb))


def madlib3():
    """Third mad lib sentence construct

    :return: None
    """
    person = input(PERSON_NAME)
    color = input(COLOR_NAME)
    foods = input(FOOD_NAME)
    adjective = input(ADJECTIVE)
    thing = input(THING_NAME)
    place = input(PLACE_NAME)
    verb = input(VERB_NAME)
    adverb = input(ADVERB)
    food = input(FOOD_NAME)
    things = input(THING_NAME)
    print(MAD3.format(person, color, foods, adjective, thing, place, verb,
                      adverb, food, things))


if __name__ == '__main__':
    """Main entry point of madlibs"""
    root = Tk()
    root.geometry('300x300')
    root.title('DataFlair-Mad Libs Generator')
    Label(root, text='Mad Libs Generator \n Have Fun!', font='arial 20 '
                                                             'bold').pack()
    Label(root, text='Click Any One :', font='arial 15 bold').place(x=40, y=80)
    Button(root, text='The Photographer', font='arial 15', command=madlib1,
           bg='ghost white').place(x=60, y=120)
    Button(root, text='apple and apple', font='arial 15', command=madlib3,
           bg='ghost white').place(x=70, y=180)
    Button(root, text='The Butterfly', font='arial 15', command=madlib2,
           bg='ghost white').place(x=80, y=240)
    root.mainloop()
