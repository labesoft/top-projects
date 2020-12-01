"""The application of an alarm
---------------------------

About this Project
------------------
The objective of this project is to recreate an alarm that a user could set
interactively and which will ring back at this preset time.

Project structure
-----------------
*alarm/*
    **-->** **__main__.py**:
        The application of an alarm
    **alarm_test.py**:
        The tests of an alarm
    **controller.py**:
        The controller of an alarm
    **model.py**:
        The model of an alarm
    **view.py**:
        The GUI of an alarm

About this module
-----------------
The objective of this module is to run an alarm using Python. It uses
innovative python libraries such as logging which helped us to build this
module, to setup the logger and run the controller when the alarm package is
called from the console.

File structure
--------------
*import*
    **argparse**
        Provides a way to parse arguments and run with debug level mode.
    **logging**
        Provides a logging tool to inform the user of the system
        state through the console.
    **sys**
        Provides sys utility like the access to the command line args.

*constant*
    **LOG_DATEFORMAT**
        This is how the date will be formatted in the logs which is based on
        ISO 8601.
    **LOG_FORMAT**
        How the logs are formatted including: asctime, msecs, name, level, msg.
"""
import argparse
import logging
import sys

from alarm.controller import AlarmController

# Logging patterns
LOG_DATEFORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FORMAT = "%(asctime)s.%(msecs).05f %(name)-12s [%(levelname)s] %(message)s"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ring an alarm')
    parser.add_argument('--verbose', '-v', action='store_const', const=logging.DEBUG, default=logging.INFO,
                        help='run in debug mode')
    args = parser.parse_args(sys.argv[1:])
    logging.basicConfig(format=LOG_FORMAT, level=args.verbose, datefmt=LOG_DATEFORMAT)
    AlarmController().run()
