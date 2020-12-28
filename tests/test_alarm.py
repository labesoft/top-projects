"""The test of an alarm
--------------------

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
    **os**
        provides os.name to help check and skip tests based on os under
        scrutiny
    **datetime, time**
        helps working with the time of the current day.
    **unittest**
        A unit testing framework inspired by JUnit that supports automation,
        sharing of setup and shutdown code for tests, aggregation of tests
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
"""

__author__ = "Benoit Lapointe"
__date__ = "2020-12-18"
__copyright__ = "Copyright 2020, labesoft"
__version__ = "1.0.0"

from unittest import TestCase, skipIf
from unittest.mock import patch, MagicMock, call

from alarm.model import *

TEST_DATE = (2020, 1, 1)
TEST_TIME = "00:00:00"


class TestAlarm(TestCase):
    """Test the core functionalities of the alarm"""
    def setUp(self) -> None:
        self.alarm = Alarm()

    def test_time_setter(self):
        """Test the time setter using the namedTuple"""
        # Prepare test
        hours = 1
        mins = 2
        secs = 3
        a_time = A_TIME(hours, mins, secs)

        # Run test
        self.alarm.time = a_time

        # Evaluate test
        self.assertEqual(self.alarm.hour, hours)
        self.assertEqual(self.alarm.min, mins)
        self.assertEqual(self.alarm.sec, secs)

    def test_is_alive(self):
        """Test that the alarm is alive by default"""
        # Run test
        result = self.alarm.is_alive()

        # Evaluate test
        self.assertTrue(result)

    @patch.object(logging.getLogger('alarm.model.Alarm'), 'info')
    @patch('alarm.model.SOUND_CMD')
    @skipIf(os.name == 'nt', f"Not on a posix machine os.name={os.name}")
    def test_ring_posix(self, cmd, logger):
        """Test that the alarm uses the right command to play the sound"""
        # Run test
        self.alarm.ring()

        # Evaluate test
        logger.assert_called_once_with(MSG_INFO_WAKEUP)
        cmd.assert_called_once_with(*ARGS, **KWARGS)

    @patch.object(logging.getLogger('alarm.model.Alarm'), 'info')
    @patch('alarm.model.SOUND_CMD')
    @skipIf(os.name == 'posix', f"Not on a nt machine os.name={os.name}")
    def test_ring_nt(self, cmd, logger):
        """Test that the alarm uses the right command to play the sound"""
        # Run test
        self.alarm.ring()

        # Evaluate test
        logger.assert_called_once_with(MSG_INFO_WAKEUP)
        cmd.assert_called_once_with(*ARGS, **KWARGS)

    @patch.object(logging.getLogger('alarm.model.Alarm'), 'info')
    def test_run(self, logger):
        """Test the basic run behavior: logging and managing the alarm time"""
        # Prepare test
        self.alarm.is_alive = MagicMock(side_effect=[True, False])
        self.alarm.manage_time = MagicMock()
        # Run test
        self.alarm.run()

        # Evaluate test
        calls = [call.info(MSG_INFO_START), call.info(MSG_INFO_STOP)]
        logger.assert_has_calls(calls)
        self.alarm.manage_time.assert_called_once()

    @patch('alarm.model.datetime')
    @patch.object(Alarm, 'ring')
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
        """Test the sleep is at the ideal 1s time internal while not ringing"""
        # Run test
        self.alarm.manage_time()

        # Evaluate test
        msg = MSG_DEBUG_SLEEP.format(self.alarm.time, TIME_INTERVAL)
        logger.assert_called_once_with(msg)
        sleep.assert_called_once_with(TIME_INTERVAL)
