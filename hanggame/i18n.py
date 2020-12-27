"""The international strings of The Hangman Game
---------------------------------------------

About this module
-----------------
The objective of this module is to offer The Hangman Game a centralized way of
translating string throughout the whole application.

File structure
--------------
*import*

*constant*
    **IN_MSG_***
        message printed to the player when asked for input
    **OUT_MSG_***
        message printed to the player
    **YES_LIST, NO_LIST**
        lists of yes/no options that the player may use to answer the play again
        question.
    **LEVELS**
        dictionary of possible level in The Hangman Game
    **ALPHA_LAYOUT**
        Layout of the keyboard. Each string represents a row of keys
"""

__author__ = "Benoit Lapointe"
__date__ = "2020-12-21"
__copyright__ = "Copyright 2020, Benoit Lapointe"
__version__ = "1.0.0"

import gettext
import logging
import os

# Setups the gettext used for string translation
LOCALES_DIR = os.path.join(os.path.dirname(__file__), 'locales')
DEFAULT_LANG = 'en_US'
try:
    t = gettext.translation('hanggame', localedir=LOCALES_DIR)
except FileNotFoundError as err:
    logger = logging.getLogger(__name__)
    logger.warning(f'no language set, falling back to default: {DEFAULT_LANG}')
    t = gettext.translation(
        'hanggame',
        localedir='locales',
        languages=[DEFAULT_LANG]
    )
    t.install()
_ = t.gettext

# In UI
IN_MSG_LETTER = _('Enter your letter: ')
IN_MSG_NAME = _('Enter your name: ')
IN_MSG_REPLAY = _('Do You want to play again? y = yes, n = no')
IN_NO_LIST = [
    _('n'), _('no'), _('nope'), _('not at all'),
    _('fuck off'), _('no fucking way'), _('never'), _('negative'),
    _('this is rigged'), _('toaster'), _('not a chance')
]
IN_YES_LIST = [
    _('y'), _('yes'), _('yeah'), _('sure'), _('ok'), _('always'),
    _('positive'), _('you bet'), _('give it to me'), _('go for it')
]

# Out UI
OUT_MSG_ANSWER = _("The word was: {}")
OUT_MSG_BAD_ENTRY = _('You must enter you name to play')
OUT_MSG_CHOICES = _('Letters available')
OUT_MSG_COMPLAINTS = [
    _('Wrong guess ?! :O'),
    _('Error :('),
    _('Missed ???'),
    _('Sorry, you were wrong :_(')
]
OUT_MSG_CONGRATS = [
    _('Good guess! Keep it up!!'),
    _("Wow! you're strong!!"),
    _('I want to marry you <3'),
    _('What a genius!!'),
    _("Dude, you're a machine!!")
]
OUT_MSG_ERROR = _("Errors so far: ")
OUT_MSG_GOODBYE = _('See you soon {}!')
OUT_MSG_INVALID = _('Invalid input, try another letter')
OUT_MSG_LOSER = _('You are out of attempt... Hanged!!')
OUT_MSG_LUCK = _("Hello {}! Best of Luck!")
OUT_MSG_NEW_GAME = _("Hit SPACE bar to begin")
OUT_MSG_NB_ATTEMPT = _("Attempts remaining: {}")
OUT_MSG_READY = _("The game is about to start... let's play Hangman!")
OUT_MSG_THANKS = _('Thanks for playing The Hangman Game!')
OUT_MSG_TITLE = _('The Hangman Game')
OUT_MSG_TRY_AGAIN = _('Try another letter plz')
OUT_MSG_WELCOME = _('Welcome to The Hangman Game by labesoft')
OUT_MSG_WINNER = _("Congrats!! You have guessed correctly...")
OUT_MSG_LEVEL = _("Level: ")

SPACE_KEY = _('Space')
START = _('Start')

# Game levels
LEVELS = {
    'BEGINNER': _('BEGINNER'),
    'INTERMEDIARY': _('INTERMEDIARY'),
    'PRO': _('PRO'),
    'ELITE': _('ELITE'),
    'INFERNO': _('INFERNO'),
    'EXTREME': _('EXTREME')
}

# Words
WORDS_ALPHA_TXT = _('words_alpha.txt')
ALPHA_LAYOUT = [_('qwertyuiop'), _('asdfghjkl'), _('zxcvbnm')]

# GUI
KEYBOARD_LAYOUT = _('keyboard.ui')
