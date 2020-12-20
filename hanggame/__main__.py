"""The application of The Hangman Game
-----------------------------------

About this module
-----------------
The objective of this module is to run The Hangman Game using Python. It uses
logging, argparse and sys to parse the user arguments, to setup the logger and
to run the application when the hanggame package is called from the console.

File structure
--------------
*import*
    **argparse**
        provides a way to parse arguments and run with debug level mode.
    **logging**
        provides a logging tool to inform the user of the system state through
        the console.
    **sys**
        provides sys utility like to access to the command line args.

*constant*
    **LOG_DATEFORMAT**
        this is how the date will be formatted in the logs which is based on
        ISO 8601.
    **GAMELOG_FORMAT**
        how the logs are formatted including: message.
"""
import argparse
import logging
import sys

from hanggame.game import HangGame
from hanggame.level import GameLevel

# Logging patterns
LOG_DATEFORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FORMAT = "%(asctime)s.%(msecs).05f %(name)-12s [%(levelname)s] %(message)s"

if __name__ == '__main__':
    # Parser
    parser = argparse.ArgumentParser(description='Ring an alarm')
    parser.add_argument('--verbose', '-v', action='store_const', const=logging.DEBUG, default=logging.INFO,
                        help='run in debug mode')
    parser.add_argument('--level', '-l', type=int, choices=range(6), default=0,
                        help=' '.join(f'{i}={l.name}|{l.value}-try' for i, l in enumerate(GameLevel)))
    args = parser.parse_args(sys.argv[1:])

    # Logger
    logging.basicConfig(format=LOG_FORMAT, level=args.verbose)
    logger = logging.getLogger(__name__)
    logger.debug(list(GameLevel)[args.level])

    # Game
    game = HangGame(level=list(GameLevel)[args.level])
    game.run()
