"""A Proof Of Concept for the rolling dice simulation
--------------------------------------------------

Project structure
-----------------
*dice/*
    **dice3d-panda.py**:
        The Proof Of Concept for the rolling dice simulation
        
About this module
-----------------
This module will help us to demonstrate if it developing a game with a
blender/panda3d mix is a viable project

File structure
--------------
*import*
    **direct.showbase.ShowBase.ShowBase**
        Useful modules for a Panda3D module
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-01-09"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase, WindowProperties
from direct.showbase.ShowBaseGlobal import globalClock
from panda3d.core import AmbientLight, Vec4, DirectionalLight, Vec3


class DicePocFrame(ShowBase):
    """This class is the main frame of the game

    This includes its core functionalities setup for:
    - Window size
    - Scene visualization
    - Actor visualization and behaviour
    - Camera placement
    - Lighting
    """

    def __init__(self):
        """Initialize the DicePocFrame while inheriting ShowBase properties"""
        super(DicePocFrame, self).__init__()
        self.prepare_window()
        self.scene = self.prepare_scene("models/craps_table.bam")
        self.dice_actor = self.create_dice_actor("models/dice.bam")
        self.prepare_camera()
        self.set_lighting()
        self.action_map = {
            "up": ["w", False], "down": ["s", False],
            "left": ["a", False], "right": ["d", False],
            "lift": ["q", False], "fall": ["e", False],
            "shoot": ["mouse1", False]
        }
        self.map_keys()
        self.updateTask = self.taskMgr.add(self.update, "update")

    def create_directional_light(self):
        """Creates a directional light and turn it to the scene

        FIXME: This doesn't work as expected
        It turns it by 45 degrees (psy) tilt it down 45 degrees (phi)

        :return: the node created for the light
        """
        main_light = DirectionalLight("main light")
        node = self.render.attachNewNode(main_light)
        node.setHpr(45, -45, 0)
        node.setPos(-20, -20, 20)
        return node

    def create_ambient_light(self):
        """Creates an ambient light with a preset color

        :return: the node created for the light
        """
        ambient_light = AmbientLight("ambient light")
        ambient_light.setColor(Vec4(0.2, 0.2, 0.2, 1))
        node = self.render.attachNewNode(ambient_light)
        return node

    def create_dice_actor(self, actor_file_path):
        """Creates the actor and prepares it to the game

        FIXME: the log print out warning that this is not a charater ?

        :param actor_file_path: the file name of the model
        :return: the actor ready to use
        """
        actor = Actor(actor_file_path)
        actor.reparentTo(self.render)
        actor.setZ(0.3)
        actor.loop("")
        # actor.setShaderAuto()
        return actor

    def map_keys(self):
        """Sets the link between the key pressed events and the action

        It then link the activation state. It also do the same with the
        key release event.
        """
        for action, event_set in self.action_map.items():
            key = event_set[0]
            self.set_key_event(key, action, True)
            self.set_key_event('{}-up'.format(key), action, False)

    def set_key_event(self, event, action, is_activated):
        """Links an event to an action and its activation status

        :param event: an input event (key pressed/released or mouse)
        :param action: the action that the event trigger
        :param is_activated: the activation status of the action
        """
        self.accept(event, self.update_key_map, [action, is_activated])

    def prepare_camera(self):
        """Move the camera to display the table"""
        self.disableMouse()
        self.camera.setZ(3.5)
        self.camera.setP(-90)

    def prepare_scene(self, model_file_path):
        """Prepare the scene from a model file path and then link it to render

        :param model_file_path: the path of the model file
        :return: the scene ready to use
        """
        scene = self.loader.loadModel(model_file_path)
        scene.reparentTo(self.render)
        return scene

    def prepare_window(self):
        """Prepares the window size property"""
        properties = WindowProperties()
        properties.setSize(1700, 700)
        self.win.requestProperties(properties)

    def set_lighting(self):
        """Sets the lighting of the scene

        Tried 2 set of light:
        - One ambient light with a color attribute
        - One directional light to create some shadowing (which doesn't work)
        """
        main_light_node = self.create_directional_light()
        self.render.setLight(main_light_node)
        ambient_light_node = self.create_ambient_light()
        self.render.setLight(ambient_light_node)
        # self.render.setShaderAuto()

    def update(self, task):
        """Updates the actor action following the key event

        It is use as a callback task and instructs a movement to the actor
        following the key pressed by the player which relates to a specific
        type of movement (or other action). The movement is also based on
        the amount of time since the last movement.

        :param task: the task received by the callback

        :return: the priority of the task
        """
        dt = globalClock.getDt()
        result_pos = Vec3(0, 0, 0)

        if self.action_map["up"][1]:
            result_pos = Vec3(0, 5.0 * dt, 0)
        if self.action_map["down"][1]:
            result_pos = Vec3(0, -5.0 * dt, 0)
        if self.action_map["left"][1]:
            result_pos = Vec3(-5.0 * dt, 0, 0)
        if self.action_map["right"][1]:
            result_pos = Vec3(5.0 * dt, 0, 0)
        if self.action_map["shoot"][1]:
            result_pos = Vec3(0, 0, 0)
            print("Zap!")
        if self.action_map["lift"][1]:
            result_pos = Vec3(0, 0, 5.0 * dt)
        if self.action_map["fall"][1]:
            result_pos = Vec3(0, 0, -5.0 * dt)
        self.dice_actor.setPos(self.dice_actor.getPos() + result_pos)
        return task.cont

    def update_key_map(self, key_name, activation_state):
        """Updates the activation state of the current action

        :param key_name: the name of the key pressed
        :param activation_state: the activation state to set
        """
        self.action_map[key_name][1] = activation_state
        print(key_name, "set to", activation_state)


if __name__ == '__main__':
    app = DicePocFrame()
    app.run()
