"""The play logic of The Hangman Game
----------------------------------

About this Project
------------------
The objective of this project is to recreate The Hangman Game that a user could
play interactively by attempting to unmask a word one letter at a time using a
limited number of attempts without being hanged by the hangman.

Project structure
-----------------
*alarm/*
    **__main__.py**:
        The application of The Hangman Game
    **game.py**:
        The play logic of The Hangman Game
    **greeter.py**:
        The greeter of The Hangman Game
    **hangman.py**:
        The drawing logic of the hangman on the gallows
    **level.py**:
        The game levels of The Hangman Game
    **word.py**:
        The word handling logic of The Hangman Game
    **words_alpha.txt**
        The words dictionary provided with The Hangman Game

About this module
-----------------
The objective of this module is to model The Hangman Game using Python. It uses
innovative python libraries such as logging which helped us to build this
module, to setup the logger, to greets the player and to initialize the game
ran from the console.

File structure
--------------
*import*
    **logging**
        provides a logging tool to inform the user of the system state through
        the console.
    **random**
        randomly choose an item from a list or basically a sequence..
    **time**
        import the actual time from the machine to use in the program

*constant*
    *NONE*

*HangGame*
"""
import logging
import random

from hanggame.greeter import Greeter, OUT_MSG_CONGRATS, OUT_MSG_LOSER, OUT_MSG_WINNER, OUT_MSG_COMPLAINTS
from hanggame.hangman import Hangman
from hanggame.level import GameLevel
from hanggame.word import Word


YES_LIST = ['y', 'yes', 'yeah', 'sure', 'ok', 'always', 'positive', 'you bet',
            'give it to me', 'go for it']
NO_LIST = ['n', 'no', 'nope', 'not at all', 'fuck off', 'no fucking way',
           'never', 'negative', 'this is rigged', 'toaster', 'not a chance']
YES_NO_LIST = YES_LIST + NO_LIST


class HangGame:
    def __init__(self, level=GameLevel.BEGINNER, word=Word(), greeter=Greeter()):
        """Initializes The Hangman Game

        :param level: the level of The Hangman Game (default: Beginner)
        :param word: the word to unveil
        :param greeter: i/o tool which interacts with the player
        """
        self.logger = logging.getLogger(__name__).getChild(self.__class__.__name__)
        self.game_level = level
        self.hangman = Hangman(level=self.game_level)
        self.word = word
        self.word.choose()
        self.greeter = greeter
        self.play = True

    def reset(self):
        """Reset The Hangman Game an choose a new word"""
        self.hangman.reset()
        self.word.choose()
        self.play = True

    def play_again(self):
        """Asks the player to play again

        yes: the game is reset and ready to restart
        no: the game is triggered to stop and greets the player
        """
        choice = ''
        while choice.lower() not in YES_NO_LIST:
            choice = self.greeter.new_game()
        if choice.lower() in YES_LIST:
            self.reset()
        else:
            self.play = False
            self.greeter.farewell()

    def run(self):
        """Runs the game until it is over and asked to stop

        This is the running loop which handles each step of The Hangman Game.
        """
        self.hangman.draw(hanged=True)
        self.greeter.welcome(str(self.hangman))
        self.hangman.draw()

        while self.play:
            self.greeter.init_attempt(str(self.hangman), self.hangman.attempt, str(self.word))
            current_letter = self.accept_letter()
            if self.word.unmask(current_letter):
                self.greeter.end_turn(random.choice(OUT_MSG_CONGRATS))
                if not self.word.is_mask():
                    self.hangman.draw(safe=True)
                    self.greeter.end_game(str(self.hangman), OUT_MSG_WINNER, self.word.reveal)
                    self.play_again()
            else:
                self.hangman.missed = 1
                self.hangman.draw()
                self.greeter.end_turn(random.choice(OUT_MSG_COMPLAINTS))
                if not self.hangman.attempt:
                    self.greeter.end_game(str(self.hangman), OUT_MSG_LOSER, self.word.reveal)
                    self.play_again()

    def accept_letter(self):
        """Asks the player to choose a new letter until the choice is valid

        :return: the letter chosen by the player
        """
        result = ''
        while not self.is_valid(result):
            result = self.greeter.new_letter()
            if not self.is_valid(result):
                self.greeter.invalid_letter()
        return result

    def is_valid(self, candidate):
        """Determines if the candidate string is a valid choice

        :param candidate: a candidate letter
        :return: True if the candidate string is an alpha character and an unmasked letter,
         False otherwise.
        """
        is_alpha_char = len(candidate) == 1 and candidate.isalpha()
        return is_alpha_char and not self.word.is_unmask(candidate)
