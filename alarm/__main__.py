"""The application of an alarm
---------------------------

About this module
-----------------
The objective of this module is to run an alarm using Python. It uses
innovative python libraries such as logging which helped us to build this
module, to setup the logger and run the controller when the alarm package is
called from the console.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-05-18"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

import argparse
import logging
import sys

from alarm.controller import AlarmController

# Logging patterns
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FORMAT = "%(asctime)s.%(msecs).05f %(name)-12s [%(levelname)s] %(message)s"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ring an alarm')
    parser.add_argument('--verbose', '-v', action='store_const',
                        const=logging.DEBUG, default=logging.INFO,
                        help='run in debug mode')
    args = parser.parse_args(sys.argv[1:])
    logging.basicConfig(format=LOG_FORMAT, level=args.verbose,
                        datefmt=LOG_DATE_FORMAT)
    AlarmController().run()
