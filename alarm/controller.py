"""The controller of an alarm
--------------------------

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
    **-->** **controller.py**:
        The controller of an alarm
    **model.py**:
        The model of an alarm
    **view.py**:
        The GUI of an alarm

About this module
-----------------
The objective of this module is to bridge the alarm to the view using Python.
It uses innovative Python libraries such as threading which helps to initiate
and run the application using different threads for the alarm model and the
alarm view.

File structure
--------------
*imports*
    **threading**
        this module provides a way to run the model in a different thread than
        the main thread which is associated to the UI thread.

*class*
    **AlarmController**
        'The link between an alarm and its view'
    **__init__(self)**
        'The starting point of the alarm'
    **run(self)**
        'Initiate the model thread in parallel to the main UI thread'
    **set_alarm_time(self)**
        'Propagate the time provided by the user to the model'
"""
import threading

from alarm.model import Alarm, A_TIME, ZERO
from alarm.view import AlarmView


class AlarmController:
    """The link between an alarm and its view"""
    def __init__(self):
        """The starting point of the alarm

        This create both the alarm ahd the alarm view creating the GUI and
        passing to the button a callback to refresh the alarm time.
        """
        self.alarm = Alarm()
        self.alarm_view = AlarmView()
        self.alarm_view.create_gui(self.preset_alarm_time)

    def preset_alarm_time(self):
        """Propagate the time provided by the user to the model

        This method owned by the controller is used as a callback from the view
        to the model.

        :return: None
        """
        a_time = A_TIME(hour=self.alarm_view.hour_var.get(),
                        min=self.alarm_view.min_var.get(),
                        sec=self.alarm_view.sec_var.get())
        self.alarm.time = a_time

    def run(self):
        """Initiate the model thread in parallel to the main UI thread

        :return: None
        """
        alarm_th = threading.Thread(target=self.alarm.run)
        try:
            alarm_th.start()
            self.alarm_view.mainloop()
        finally:
            self.alarm.sleep_time = ZERO
            alarm_th.join()
