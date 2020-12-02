"""The application of the hangman game
-----------------------------------

About this Project
------------------
The objective of this project is to recreate the hangman game that a user could
play interactively trying to guess a to_guess with a limited number of guess.

Project structure
-----------------
*alarm/*
    **__main__.py**:
        The application of the hangman game
    **model.py**:
        The model of the hangman game

About this module
-----------------
The objective of this module is to run the hangman game using Python. It uses
innovative python libraries such as logging which helped us to build this
module, to setup the logger and it runs the application when the hangman
package is called from the console.

File structure
--------------
*import*
    **argparse**
        Provides a way to parse arguments and run with debug level mode.
    **logging**
        Provides a logging tool to inform the user of the system state through
        the console.
    **sys**
        Provides sys utility like to access to the command line args.

*constant*
    **LOG_DATEFORMAT**
        This is how the date will be formatted in the logs which is based on
        ISO 8601.
    **GAMELOG_FORMAT**
        How the logs are formatted including: message.
"""
import argparse
import logging
import sys

from hangman.game import greetings, main, hangman

# Logging patterns
LOG_DATEFORMAT = "%Y-%m-%d %H:%M:%S"
GAMELOG_FORMAT = "%(message)s"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ring an alarm')
    parser.add_argument('--verbose', '-v', action='store_const', const=logging.DEBUG, default=logging.INFO,
                        help='run in debug mode')
    args = parser.parse_args(sys.argv[1:])
    logging.basicConfig(format=GAMELOG_FORMAT, level=args.verbose)
    greetings()
    main()
    hangman()
