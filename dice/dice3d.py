"""The 3d animation of The Dice Rolling Simulator Game
-----------------------------

About this Project
------------------


Project structure
-----------------
*dice/*
    **dice3d.py**:
        The 3d animation of The Dice Rolling Simulator Game
        
About this module
-----------------
This objective of this module is to animate the rolling of a dice for The Dice
Rolling Simulator Game

File structure
--------------
*import*
    **direct.showbase.ShowBase.ShowBase**
        Useful modules for a Panda3D module

*constant*

"""

__author__ = "Benoit Lapointe"
__date__ = "2020-12-28"
__copyright__ = "Copyright 2020, labesoft"
__version__ = "1.0.0"

from math import sin, pi, cos

from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class Dice3D(ShowBase):
    """Base window of the 3D animation"""

    def __init__(self):
        """Initialize the Dice3D while inheriting ShowBase properties"""
        super(Dice3D, self).__init__()

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont


if __name__ == '__main__':
    app = Dice3D()
    app.run()
