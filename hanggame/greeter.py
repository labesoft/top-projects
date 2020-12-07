import time


IN_SLEEP = 0.1
FORMAT_NEWLINE_PRE = "\n{}".format
FORMAT_NEWLINE_END = "{}\n".format

IN_MSG_LETTER = 'Enter your letter: '
IN_MSG_NAME = 'Enter your name: '
IN_MSG_REPLAY = 'Do You want to play again? y = yes, n = no'
OUT_MSG_ANSWER = "The word was: {}"
OUT_MSG_GOODBYE = 'See you soon {}!'
OUT_MSG_INVALID = 'Invalid input, try another letter'
OUT_MSG_LUCK = "Hello {}! Best of Luck!"
OUT_MSG_NB_ATTEMPT = "You have {} attempt"
OUT_MSG_READY = "The game is about to start... let's play Hangman!"
OUT_MSG_THANKS = 'Thanks for playing The Hangman Game!'
OUT_MSG_WELCOME = 'Welcome to The Hangman Game by labesoft'


class Greeter:
    def __init__(self, cb_out=print, cb_in=input):
        self._out = cb_out
        self._in = cb_in
        self.player_name = ''

    def welcome(self, hangman):
        """Welcome the user in the game

        It prints the welcome message, the hanged man drawing, ask the name
        of the player, greets him and print the start of the game.

        :param hangman: the hangman of the current game
        """
        self._out(OUT_MSG_WELCOME)
        hangman.draw(hanged=True)
        self._out(hangman)
        hangman.draw()
        time.sleep(IN_SLEEP)
        self.player_name = self._in(IN_MSG_NAME)
        self._out(OUT_MSG_LUCK.format(self.player_name))
        self._out(FORMAT_NEWLINE_PRE(OUT_MSG_READY))

    def farewell(self):
        """

        :return:
        """
        self._out(OUT_MSG_THANKS)
        self._out(OUT_MSG_GOODBYE.format(self.player_name))

    def end_turn(self, good_wrong_msg):
        self._out(FORMAT_NEWLINE_PRE(good_wrong_msg))

    def end_game(self, hangman, end_msg, word):
        self._out(hangman)
        self._out(end_msg)
        self._out(OUT_MSG_ANSWER.format(word))

    def new_letter(self):
        time.sleep(IN_SLEEP)
        return self._in(IN_MSG_LETTER).strip()

    def new_game(self):
        time.sleep(IN_SLEEP)
        return self._in(FORMAT_NEWLINE_END(IN_MSG_REPLAY))

    def invalid_letter(self):
        return self._out(OUT_MSG_INVALID)

    def new_attempt(self, hangman, word):
        self._out(hangman)
        self._out(OUT_MSG_NB_ATTEMPT.format(hangman.attempt))
        self._out(' '.join(list(str(word))))
