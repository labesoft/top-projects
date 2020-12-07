"""The play rules of The Hangman Game
-----------------------------

About this Project
------------------
The objective of this project is to recreate The Hangman Game that a user could
play interactively trying to guess a word with a limited number of guess attempts
depending on his game level.

Project structure
-----------------
*alarm/*
    **__main__.py**:
        The application of The Hangman Game
    **game.py**:
        The play rules of The Hangman Game
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

*func*
    **greetings()**
        Welcome the user in the game
    **main()**
        Initialize The Hangman Game attributes
    **play_loop()**
        A loop to re-execute the game when the first round ends
    **hanggame()**
        Checking all the conditions required for the game
"""
import logging
import random

from hanggame.greeter import Greeter
from hanggame.hangman import Hangman
from hanggame.level import GameLevel
from hanggame.word import Word


YES_LIST = ['y', 'yes', 'yeah', 'sure', 'ok', 'always', 'positive', 'you bet',
            'give it to me', 'go for it']
NO_LIST = ['n', 'no', 'nope', 'not at all', 'fuck off', 'no fucking way',
           'never', 'negative', 'this is rigged', 'toaster', 'not a chance']
YES_NO_LIST = YES_LIST + NO_LIST

OUT_MSG_GOOD = ['Good guess! Keep it up!!', "Wow! you're strong!!",
                'I want to marry you <3', 'What a genius!!',
                "Dude, you're a machine!!"]
OUT_MSG_LOSER = 'You are out of attempt... Hanged!!'
OUT_MSG_TRY_AGAIN = 'Try another letter plz'
OUT_MSG_WINNER = "Congrats!! You have guessed the word correctly.."
OUT_MSG_WRONG = ['Wrong guess ?! :O', 'Error :(', 'Missed ???',
                 'Sorry, you were wrong :_(']


class HangGame:
    def __init__(self, callback_out=print, callback_in=input, level=GameLevel.BEGINNER,
                 word=Word(), greeter=Greeter()):
        """Initialize The Hangman Game attributes

        We define the main function that initializes the arguments: global
         count, global display, global to_guess, global already_guessed, global
         length and global play_game. They can be used further in other
         functions too depending on how we want to call them.
        Words_to_guess: Contains all the Hangman words we want the user to
         guess in the game.
        self.Word: we use the random module in this variable to randomly choose
         the word from words_to_guess in the game.
        self.Length: len() helps us to get the length of the string.
        Count: is initialized to zero and would increment in the further code.
        self.display: This draws a line for us according to the length of the
         word to guess.
        self.Already_guessed: This would contain the string indices of the
         correctly guessed words.
        """
        self.logger = logging.getLogger(__name__).getChild(self.__class__.__name__)
        self._out = callback_out
        self._in = callback_in
        self.game_level = level
        self.hangman = Hangman(level=self.game_level)
        self.word = word
        self.word.choose()
        self.greeter = greeter
        self.play = True

    def reset(self):
        self.hangman.reset()
        self.word.choose()
        self.play = True

    def play_again(self):
        """A choice made by the user to replay or stop the game

        It loops until the user makes a valid choice which is define in the
        YES_NO_LIST. The obvious choices are y=yes or n=no, but it also
        supports other not obvious choices like 'go for it'=yes
        'this is rigged'=no. If the user chose yes the game reset itself.
        Otherwise, it set play_game to false (which will kick out the user
        out of the play loop) and greets the user
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
        """Checking all the conditions required for the game

        We call all the arguments again under the hanggame() function.
        Limit: It is the maximum guesses we provide to the user to guess a
         particular word.
        Guess: Takes the input from the user for the guessed letter.
         Guess.strip() removes the letter from the given word.
        Checks that if no input is given, or two letters are given at once, or
         a number is entered as an input, it tells the user about the invalid
         input and executes hanggame again.
        If the letter is correctly guessed, index searches for that letter in
         the word. self.display adds that letter in the given space according
         to its index or where it belongs in the given word.
        If we have already guessed the correct letter before and we guess it
         again, It tells the user to try again and
         does not lessen any chances.
        If the user guessed the wrong letter, the hanggame starts to appear
         which also tells us how many guesses are left. Count was initialized
         to zero and so with every wrong guess its value increases with one.
        Limit is set to 5 and so (limit- count) is the guesses left for the
         user with every wrong input. If it reaches the limit, the game ends,
         showing the right guesses (if any) and the word that was supposed to
         be guessed.
        If the word is guessed correctly, matching the self.length of the
         self.display argument, the user has won the game.
        Play_loop asks the user to play the game again or exit.
        Main() and hanggame() would start again if the play_loop executes to
         yes.
        """
        self.greeter.welcome(self.hangman)
        self.hangman.draw()

        while self.play:
            self.greeter.new_attempt(self.hangman, self.word)
            current_letter = self.accept_letter()
            if self.word.unmask(current_letter):
                self.greeter.end_turn(random.choice(OUT_MSG_GOOD))
                if not self.word.is_mask():
                    self.hangman.draw(winner=True)
                    self.greeter.end_game(str(self.hangman), OUT_MSG_WINNER, self.word.reveal)
                    self.play_again()
            else:
                self.hangman.missed = 1
                self.hangman.draw()
                self.greeter.end_turn(random.choice(OUT_MSG_WRONG))
                if not self.hangman.attempt:
                    self.greeter.end_game(str(self.hangman), OUT_MSG_LOSER, self.word.reveal)
                    self.play_again()

    def accept_letter(self):
        result = ''
        while not self.is_valid(result):
            result = self.greeter.new_letter()
            if not self.is_valid(result):
                self.greeter.invalid_letter()
        return result

    def is_valid(self, letter):
        is_alpha_char = len(letter) == 1 and letter.isalpha()
        return is_alpha_char and not self.word.is_unmask(letter)
