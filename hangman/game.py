"""The model of the hangman game
-----------------------------

About this Project
------------------
The objective of this project is to recreate the hangman game that a user could
play interactively trying to guess a word with a limited number of guess.

Project structure
-----------------
*alarm/*
    **__main__.py**:
        The application of the hangman game
    **game.py**:
        The model of the hangman game

About this module
-----------------
The objective of this module is to model the hangman game using Python. It uses
innovative python libraries such as logging which helped us to build this
module, to setup the logger, to greets the player and to initialize the game
ran from the console.

File structure
--------------
*import*
    **logging**
        Provides a logging tool to inform the user of the system state through
        the console.
    **random**
        Randomly choose an item from a list or basically a sequence..
    **time**
        Import the actual time from the machine to use in the program

*constant*
    *NONE*

*func*
    **greetings()**
        Welcome the user in the game
    **main()**
        Initialize the hangman game attributes
    **play_loop()**
        A loop to re-execute the game when the first round ends
    **hangman()**
        Checking all the conditions required for the game
"""
import logging
import random
import re
import time
from enum import Enum
from os.path import dirname
from pathlib import Path

ERROR_LIMIT_EXCEEDED = "Missed count can't exceed the limit: {}>{}"

DEFAULT_WORDS_FILE = Path(dirname(__file__), 'words_alpha.txt')

YES_LIST = ["y", "yes", "yeah", "sure", "ok", "always", "positive", "give it to me"]
NO_LIST = ["n", "no", "nope", "not at all", "fuck off", "no fucking way", "never", "negative", "this is rigged"]
YES_NO_LIST = YES_LIST + NO_LIST

GALLOWS = [
    "   _____",
    "  |     |",
    "  |     |",
    "  |     |",
    "  |",
    "  |",
    "  |",
    "__|__"
]
GALLOWS_HEAD = "  |     O"
GALLOWS_BODY = "  |     |"
GALLOWS_ARM_LEFT = "  |    /|"
GALLOWS_ARMS = "  |    /|\\"
GALLOWS_LEG_LEFT = "  |    /"
GALLOWS_LEGS = "  |    / \\"

IN_MSG_NAME = "Enter your name: "
IN_MSG_REPLAY = "Do You want to play again? y = yes, n = no \n"
IN_MSG_GUESS = "Enter your guess: "

IN_SLEEP = 0.1

LOG_DEBUG_GAME_OVER = "self.already_guessed={}, self.display={}, self.to_guess={}"

OUT_MSG_ANSWER = "The word was: {}"
OUT_MSG_GOOD = "Good guess! Keep it up!!"
OUT_MSG_HANGED = "Wrong guess. You are hanged!!!"
OUT_MSG_INVALID = "Invalid Input, Try a letter"
OUT_MSG_LUCK = "Hello {}! Best of Luck!"
OUT_MSG_READY = "The game is about to start... Let's play Hangman!"
OUT_MSG_THANKS = "Thanks For Playing! We expect you back again!"
OUT_MSG_TRY_AGAIN = "Try another letter."
OUT_MSG_WELCOME = "Welcome to Hangman game by labesoft"
OUT_MSG_WINNER = "Congrats! You have guessed the word correctly: {}!!"
OUT_MSG_WRONG_GUESS = "Wrong guess. {} guesses remaining"


class Level(Enum):
    BEGINNER = 6
    INTERMEDIARY = 5
    PRO = 4
    ELITE = 3
    INFERNO = 2
    EXTREME = 1


class HangGame:
    def __init__(self, callback_out=print, callback_in=input, words_file=DEFAULT_WORDS_FILE,
                 game_level=Level.BEGINNER):
        """Initialize the hangman game attributes

        We define the main function that initializes the arguments: global count, global display, global to_guess, global
         already_guessed, global length and global play_game. They can be used further in other functions too depending on
         how we want to call them.
        Words_to_guess: Contains all the Hangman words we want the user to guess in the game.
        self.Word: we use the random module in this variable to randomly choose the word from words_to_guess in the game.
        self.Length: len() helps us to get the length of the string.
        Count: is initialized to zero and would increment in the further code.
        self.display: This draws a line for us according to the length of the word to guess.
        self.Already_guessed: This would contain the string indices of the correctly guessed words.
        """
        self.logger = logging.getLogger(__name__).getChild(self.__class__.__name__)
        self._out = callback_out
        self._in = callback_in
        self.level = game_level
        self.guess_limit = game_level.value
        self.hangman = Hangman(self.guess_limit)

        with open(words_file) as f:
            all_words = f.readlines()
            words_to_guess = [w.strip('\n')
                              for w in all_words if len(w.strip('\n')) > 2]
        self.to_guess: str = random.choice(words_to_guess)
        self.word = self.to_guess
        self.length = len(self.to_guess)
        self.missed_count = 0
        self.display_word = '_ ' * (self.length - 1) + '_'
        self.already_guessed = []
        self.play_game = True

    def greetings(self):
        """Welcome the user in the game

        Initial Steps to invite in the game
        """
        self._out(OUT_MSG_WELCOME)
        time.sleep(IN_SLEEP)
        name = self._in(IN_MSG_NAME)
        self._out(OUT_MSG_LUCK.format(name))
        self._out(OUT_MSG_READY)

    def play_again(self):
        """A choice made by the user to replay or stop the game

        play_again: This function takes in the user input.
        self.play_game: We use this argument to either continue the game after it is played once or end it according to
         what the user suggests.
        While loop is used to execute the self.play_game argument. It takes the parameter, y=yes and n=no. If the user
         gives an input of something else other than y/n, it asks the question again for the appropriate answer. If the
          user inputs “y”, the game restarts, otherwise the game ends.

        :return:
        """
        time.sleep(IN_SLEEP)
        choice = self._in(IN_MSG_REPLAY)

        while choice.lower() not in YES_NO_LIST:
            time.sleep(IN_SLEEP)
            choice = self._in(IN_MSG_REPLAY)

        if choice.lower() in YES_LIST:
            self.__init__(callback_out=self._out, callback_in=self._in, game_level=self.level)
        else:
            self.play_game = False
            self._out(OUT_MSG_THANKS)
        return self.play_game

    def play(self):
        """Checking all the conditions required for the game

        We call all the arguments again under the hangman() function.
        Limit: It is the maximum guesses we provide to the user to guess a particular word.
        Guess: Takes the input from the user for the guessed letter. Guess.strip() removes the letter from the given
        word.
        Checks that if no input is given, or two letters are given at once, or a number is entered as an input, it
         tells the user about the invalid input and executes hangman again.
        If the letter is correctly guessed, index searches for that letter in the word.
        self.display adds that letter in the given space according to its index or where it belongs in the given word.
        If we have already guessed the correct letter before and we guess it again, It tells the user to try again and
         does not lessen any chances.
        If the user guessed the wrong letter, the hangman starts to appear which also tells us how many guesses are
         left. Count was initialized to zero and so with every wrong guess its value increases with one.
        Limit is set to 5 and so (limit- count) is the guesses left for the user with every wrong input. If it reaches
         the limit, the game ends, showing the right guesses (if any) and the word that was supposed to be guessed.
        If the word is guessed correctly, matching the self.length of the self.display argument, the user has won the
         game.
        Play_loop asks the user to play the game again or exit.
        Main() and hangman() would start again if the play_loop executes to yes.
        """
        while self.play_game:
            guess = self.new_guess()
            if not self.is_valid(guess):
                self._out(OUT_MSG_INVALID)
            elif guess in self.to_guess:
                self.discover(guess)
                if self.to_guess == '_' * self.length:
                    self._out(OUT_MSG_WINNER.format(self.word))
                    self.play_again()
                else:
                    self._out(OUT_MSG_GOOD)
            elif guess in self.already_guessed:
                self._out(OUT_MSG_TRY_AGAIN)
            else:
                self.missed_count += 1
                self.hangman.draw(self.missed_count)
                self._out("\n".join(self.hangman.gallows))
                self.handle_missed()

    def handle_missed(self):
        if self.missed_count < self.guess_limit:
            guess_left = self.guess_limit - self.missed_count
            self._out(OUT_MSG_WRONG_GUESS.format(guess_left))
        else:
            self._out(OUT_MSG_HANGED)
            self._out(OUT_MSG_ANSWER.format(self.word))
            msg_args = (self.already_guessed, self.display_word, self.to_guess)
            self.logger.debug(LOG_DEBUG_GAME_OVER.format(*msg_args))
            self.play_again()

    def discover(self, guess):
        self.already_guessed.extend([guess])
        for _ in re.findall(guess, self.to_guess):
            index = self.to_guess.find(guess)
            self.to_guess = "{}_{}".format(self.to_guess[:index], self.to_guess[index + 1:])
            msg_args = (self.display_word[:index * 2], guess, self.display_word[index * 2 + 1:])
            self.display_word = "{}{}{}".format(*msg_args)

    def new_guess(self):
        self._out(self.display_word)
        time.sleep(IN_SLEEP)
        guess = self._in(IN_MSG_GUESS)
        guess = guess.strip()
        return guess

    def is_valid(self, guess):
        return len(guess.strip()) > 0 and len(guess.strip()) == 1 and guess.isalpha()


class Hangman:
    def __init__(self, guess_limit):
        self.guess_limit = guess_limit
        # Cloning (with list()) the GALLOWS list in order to keep the original list intact
        self.gallows = list(GALLOWS)
        self.gallows[4] = GALLOWS_HEAD

    def draw(self, missed_count):
        if missed_count == self.guess_limit:
            self.gallows[5] = GALLOWS_ARMS
            self.gallows[6] = GALLOWS_LEGS
        elif missed_count == self.guess_limit - 1:
            self.gallows[5] = GALLOWS_ARMS
            self.gallows[6] = GALLOWS_LEG_LEFT
        elif missed_count == self.guess_limit - 2:
            self.gallows[5] = GALLOWS_ARMS
        elif missed_count == self.guess_limit - 3:
            self.gallows[5] = GALLOWS_ARM_LEFT
        elif missed_count == self.guess_limit - 4:
            self.gallows[5] = GALLOWS_BODY

