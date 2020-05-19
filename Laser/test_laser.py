from qibullet import SimulationManager
from qibullet import PepperVirtual
from qibullet import Camera
from qibullet.base_controller import BaseController
from random import *
from Laser.module.deplacement import deplacement
from Environment.module.creation import creation
import pybullet
import pybullet_data
import cv2
import time


if __name__ == "__main__":

    x_goal = 4.5
    y_goal = 1

    simulation = creation()
    aller = deplacement() 

    #pepper = simulation.generate_world_2()
    pepper = simulation.generate_world_2()
    aller.destination_laser(x_goal, y_goal, pepper)