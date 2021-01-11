"""The 3d animation of the panda3d tutorial
----------------------------------------

Project structure
-----------------
*dice/*
    **panda_tuto.py**:
        The 3d animation of the panda3d tutorial
        
About this module
-----------------
This objective of this module is to animate a panda that walk back and forth
to see what panda3d is capable of doing

File structure
--------------
*import*
    **direct.showbase.ShowBase.ShowBase**
        Useful modules for a Panda3D module
"""

__author__ = "Benoit Lapointe"
__date__ = "2020-12-28"
__copyright__ = "Copyright 2020, labesoft"
__version__ = "1.0.0"

from math import sin, pi, cos

from direct.actor.Actor import Actor, Point3
from direct.interval.MetaInterval import Sequence
from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class PandaTuto(ShowBase):
    """Base window of the 3D animation"""

    def __init__(self):
        """Initialize the Dice3D while inheriting ShowBase properties

        This applies:
        - A premade scene with bamboo and mountains transformed for the tuto
        - A spin camera task
        - An panda actor which will walk at a slow pace
        - A start to the sequence
        """
        super(PandaTuto, self).__init__()
        self.scene = self.create_panda_scene()
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        self.panda_actor = self.create_panda_actor()
        self.panda_pace = self.create_panda_pace()
        self.panda_pace.loop()

    def create_panda_scene(self):
        """Creates the panda scene from the model environment and transforms it

        The transformation are:
        - The loading of the environment model
        - The reparent to the render
        - The rescaling of the scene
        - The reposition of the scene

        :return: the scene created and ready to use
        """
        scene = self.loader.loadModel("models/environment")
        scene.reparentTo(self.render)
        scene.setScale(0.25, 0.25, 0.25)
        scene.setPos(-8, 42, 0)
        return scene

    def create_panda_actor(self):
        """Prepare and launch animation (looping) of the actor

        :return: the loaded, transformed and animated panda actor.
        """
        actor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
        actor.setScale(0.005, 0.005, 0.005)
        actor.reparentTo(self.render)
        actor.loop("walk")
        return actor

    def create_panda_pace(self):
        """Create the pace of the panda during the animation

        Using the four Lerp intervals needed for the panda to walk back and
        forth.

        :param actor: the actor (panda) on which to apply the pace
        :return: the pace setted up base on the sequence
        """
        pos_i_1, pos_i_2 = self.create_pos_interval(13)
        hpr_i_1, hpr_i_2 = self.create_hpr_interval(3)
        name = "panda_pace"
        panda_pace = Sequence(pos_i_1, hpr_i_1, pos_i_2, hpr_i_2, name=name)
        return panda_pace

    def create_pos_interval(self, length):
        """Create two x,y,z position interval

        :param length: length of vector
        :return: two x,y,z position interval
        """
        p1 = Point3(0, -10, 0)
        p2 = Point3(0, 10, 0)
        interval1 = self.panda_actor.posInterval(length, p1, startPos=p2)
        interval2 = self.panda_actor.posInterval(length, p2, startPos=p1)
        return interval1, interval2

    def create_hpr_interval(self, length):
        """Create two h,p,r intervals

        :param length: length of vector
        :return: two h,p,r interval
        """
        p1 = Point3(0, 0, 0)
        p2 = Point3(180, 0, 0)
        interval1 = self.panda_actor.hprInterval(length, p1, startHpr=p2)
        interval2 = self.panda_actor.hprInterval(length, p2, startHpr=p1)
        return interval1, interval2

    def spinCameraTask(self, task):
        """Defines a procedure to move the camera around

        This defines:
        - The x,y,z position using angle in rad
        _ The h,p,r position using angle in degree

        :param task: the task received from the callback
        :return: the priority of the task
        """
        angle_deg = task.time * 6.0
        angle_rad = angle_deg * (pi / 180.0)
        self.camera.setPos(20 * sin(angle_rad), -20 * cos(angle_rad), 3)
        self.camera.setHpr(angle_deg, 0, 0)
        return Task.cont


if __name__ == '__main__':
    app = PandaTuto()
    app.run()
