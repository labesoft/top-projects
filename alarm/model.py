"""The model of an alarm
---------------------

About this Project
------------------
The objective of this project is to recreate an alarm that a user could set
interactively and which will ring back at this preset time.

Project structure
-----------------
*alarm/*
    **__main__.py**:
        The application of an alarm
    **alarm_test.py**:
        The tests of an alarm
    **controller.py**:
        The controller of an alarm
    **-->** **model.py**:
        The model of an alarm
    **view.py**:
        The GUI of an alarm

About this module
-----------------
The objective of this module is to model an alarm using Python. It uses
innovative Python libraries such as logging, time, datetime and subprocess
which helped to build the application using the current date and time as well
as to provide a user interface to set the alarm according to the requirement in
24-hour format.

File structure
--------------
*import*
    **logging**
        provides a logging tool to inform the user of the system state through
        the console.
    **time, datetime**
        helps working with the time of the current day.
    **subprocess**
        provides access to a basic sound playing machinery through the Linux
        system with ffmpeg (ffplay). This was useful to generate the sound
        immediately when the function is called and not waiting for the
        response (async).

*constant*
    **SOUND_CMD**
        hardcodes the command to launch the sound command (winsound/ffplay)
        directly with the right ARGS/KWARGS depending on the OS (Windows/Linux)
        It also hardcodes the filename to play.
    **MSG_***
        string messages usable by the logger at one point in the code.
    **TIME_INTERVAL**
        keeps the clock polling the alarm set by the user for every 1 second,
        the string format/pattern for the alarm.
    **TIME_FORMAT, TIME_PATTERN**
        useful to compare alarm with actual time.

*class*
    **Alarm**
        'The abstraction of an alarm'
    **alarm_time(self)**
        'Get the current alarm time'
    **is_alive(self)**
        'Determine if the alarm should continue to run or stop'
    **manage_time(self, now)**
        'Manage what the alarm should do between ringing and sleeping'
    **ring(self)**
        'Play the sound WAV_FILENAME using the ffplay command'
    **run(self)**
        'Define the main thread that handle the alarm'
"""
import logging
import os
import time
from collections import namedtuple
from datetime import datetime

# Sound play command constants
if os.name == 'nt':
    import winsound
    SOUND_CMD = winsound.PlaySound
    ARGS = ["sound.wav", winsound.SND_ASYNC]
    KWARGS = {}
elif os.name == 'posix':
    from subprocess import Popen, DEVNULL
    SOUND_CMD = Popen
    ARGS = [['ffplay', '-nodisp', '-autoexit', '-hide_banner', '-v', '0',
             '/usr/share/sounds/purple/login.wav']]
    KWARGS = {'stdout': DEVNULL, 'stderr': DEVNULL}

# Logging messages
MSG_INFO_START = "Starting alarm"
MSG_INFO_STOP = "Stopping alarm"
MSG_DEBUG_SLEEP = "self.alarm_time={}, self.sleep_time={}"
MSG_INFO_WAKEUP = "Wake up Dude"

# Time related
A_TIME = namedtuple('A_TIME', ['hour', 'min', 'sec'])
TIME_INTERVAL = 0.9985
TIME_FORMAT = "{:0>2}:{:0>2}:{:0>2}"
TIME_PATTERN = "%H:%M:%S"

# Misc
ZERO = 0


class Alarm:
    """The abstraction of an alarm

    This includes how to get the time set for the alarm, whether the alarm is
    running, when/how to ring.
    """
    def __init__(self):
        """Initialize the logger and the time to sleep and time parameters"""
        self.logger = logging.getLogger(__name__).getChild(
            self.__class__.__name__
        )
        self.sleep_time = TIME_INTERVAL
        self.hour = ZERO
        self.min = ZERO
        self.sec = ZERO

    @property
    def time(self):
        """Get the current alarm time

        :return: A time string formatted following TIME_PATTERN constant
        """
        return TIME_FORMAT.format(self.hour, self.min, self.sec)

    @time.setter
    def time(self, a_time):
        """Set the current alarm time

        :param a_time: a time that will be set
        """
        self.hour = a_time.hour
        self.min = a_time.min
        self.sec = a_time.sec

    def is_alive(self):
        """Determine is the alarm should continue to run or stop

        :return: True if self.sleep_time greater than 0, False otherwise
        """
        return self.sleep_time > ZERO

    def manage_time(self):
        """Manage what the alarm should do between ringing and sleeping

        The time of sleep is define by a predefined time interval.

        :return: None
        """
        dt_now = datetime.now().strftime(TIME_PATTERN)
        if dt_now == self.time:
            self.ring()
        else:
            self.logger.debug(MSG_DEBUG_SLEEP.format(self.time,
                                                     self.sleep_time))
            time.sleep(self.sleep_time)

    def ring(self):
        """Play the sound WAV_FILENAME using ffplay command as a bell

        :return: None
        """
        self.logger.info(MSG_INFO_WAKEUP)
        SOUND_CMD(*ARGS, **KWARGS)
        time.sleep(self.sleep_time)

    def run(self):
        """Define the main thread that handle the alarm

        Once this is call it set the alarm time and waits for the time of the
        day that will match it.

        :return: None
        """
        self.logger.info(MSG_INFO_START)
        while self.is_alive():
            self.manage_time()
        self.logger.info(MSG_INFO_STOP)
