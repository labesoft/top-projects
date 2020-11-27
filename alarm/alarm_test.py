"""The test of an alarm
--------------------

About this Project
------------------
The objective of this project is to recreate an alarm that a user could set
interactively and which will ring back at this preset time.

Project structure
-----------------
*alarm/*
    **__main__.py**:
        The application of an alarm
    **-->** **alarm_test.py**:
        The tests of an alarm
    **controller.py**:
        The controller of an alarm
    **model.py**:
        The model of an alarm
    **view.py**:
        The GUI of an alarm

About this module
-----------------
The objective of this module is to test the core functionality of the alarm
(the model). Python consists of some very innovative libraries such as
datetime, logging, subprocess, unittest, unittest.mock which helped us to test
the application separating all tests in very specific units.

File structure
--------------
*import*
    **logging**
        provides a logging tool to inform the user of the system
        state through the console.
    **time, datetime**
        helps working with the time of the current day.
    **subprocess**
        provides access to a basic sound playing machinery through the Linux
        system with ffmpeg (ffplay). This was useful to generate the sound
        immediately when the function is called and not waiting for the
        response (async).
    **unittest**
        A unit testing framework inspired by JUnit that supports automation,
        sharing of setup and shutdown code for tests, aggreagation of tests
        into collections and independence of the tests from the reporting
        framework.
    **unittest.mock**
        A library from python.org for testing in Python that allows to replace
        parts of the system under test with mock objects and make assertion on
        how they have been used.

*constant*
    **TEST_DATE**
        The date simulated in the test.
    **TEST_TIME**
        The time string simulated in the test

*class*
    **AlarmTest**
        'Test the core functionalities of the alarm'
    **test_is_alive(self)**
        'Test that the alarm is alive by default'
    **test_ring(self, sleep, popen, logger)**
        'Test that the alarm use the well formed subprocess command to play the
        sound'
    **test_run(self, logger)**
        'Test the basic run behavior: logging and managing the alarm time'
    **test_time_to_ring(self, ring, atime)**
        'Test that the alarm rings at the proper time'
    **test_time_to_sleep(self, logger, sleep)**
        'Test that the alarm sleep at the ideal 1s time internal while not
        ringing'
"""
import logging
from datetime import datetime
from subprocess import DEVNULL

from unittest import TestCase
from unittest.mock import patch, MagicMock, call

import alarm

from alarm.model import Alarm

TEST_DATE = (2020, 1, 1)
TEST_TIME = "00:00:00"


class AlarmTest(TestCase):
    """Test the core functionalities of the alarm"""
    def setUp(self) -> None:
        self.alarm = Alarm()

    def test_is_alive(self):
        """Test that the alarm is alive by default"""
        # Prepare test
        # Run test
        result = self.alarm.is_alive()
        # Evaluate test
        self.assertTrue(result)

    @patch.object(logging.getLogger('alarm.model.Alarm'), 'info')
    @patch.object(alarm.model, 'Popen')
    def test_ring(self, popen, logger):
        """Test that the alarm use the well formed subprocess command to play the sound"""
        # Prepare test
        # Run test
        self.alarm.ring()
        # Evaluate test
        logger.assert_called_once_with(alarm.model.MSG_INFO_WAKEUP)
        popen.assert_called_once_with(alarm.model.FFPLAY_CMD, stdout=DEVNULL, stderr=DEVNULL)

    @patch.object(logging.getLogger('alarm.model.Alarm'), 'info')
    def test_run(self, logger):
        """Test the basic run behavior: logging and managing the alarm time"""
        # Prepare test
        self.alarm.is_alive = MagicMock(side_effect=[True, False])
        self.alarm.manage_time = MagicMock()
        # Run test
        self.alarm.run()
        # Evaluate test
        calls = [call.info(alarm.model.MSG_INFO_START), call.info(alarm.model.MSG_INFO_STOP)]
        logger.assert_has_calls(calls)
        self.alarm.manage_time.assert_called_once()

    @patch('alarm.model.datetime')
    @patch.object(alarm.model.Alarm, 'ring')
    def test_time_to_ring(self, ring, dt):
        """Test that the alarm ring at the proper time"""
        # Prepare test
        dt.now.return_value = datetime(*TEST_DATE)
        # Run test
        self.alarm.manage_time()
        # Evaluate test
        ring.assert_called_once()

    @patch('time.sleep')
    @patch.object(logging.getLogger('alarm.model.Alarm'), 'debug')
    def test_time_to_sleep(self, logger, sleep):
        """Test that the alarm sleep at the ideal 1s time internal while not ringing"""
        # Prepare test
        # Run test
        self.alarm.manage_time()
        # Evaluate test
        msg = alarm.model.MSG_DEBUG_SLEEP.format(self.alarm.time, alarm.model.TIME_INTERVAL)
        logger.assert_called_once_with(msg)
        sleep.assert_called_once_with(alarm.model.TIME_INTERVAL)
