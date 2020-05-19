from qibullet import SimulationManager
from random import *
import pybullet
import pybullet_data


class creation():
    
    def generate_world_1(self):
        simulation_manager = SimulationManager()
        client_id = simulation_manager.launchSimulation(gui=True)

        pybullet.setAdditionalSearchPath("/home/tp/Projet/g7_dupuis_dez_flachard")

        StartPosTable = [4,0,0.2]
        StartOrientationTable = pybullet.getQuaternionFromEuler([0,0,0])
        PlaneId = pybullet.loadURDF("table.urdf", StartPosTable, StartOrientationTable)

        StartPosLego = [2,0,0.1]
        PlaneId = pybullet.loadURDF("sofa_2.urdf", StartPosLego, StartOrientationTable)


        StartPosTot1 = [3.7,0,0.75]
        StartPosTot2 = [3.7,0.4,0.75]
        StartPosTot3 = [3.7,-0.4,0.75]
        StartPosBox1 = [-1, 1, -0.3]
        StartPosBox2 = [-1, -1, -0.3]
        StartPosBox3 = [-1, 0, -0.3]

        Box1 = pybullet.loadURDF("box.urdf", StartPosBox1, StartOrientationTable)
        Box2 = pybullet.loadURDF("box2.urdf", StartPosBox2, StartOrientationTable)
        Box3 = pybullet.loadURDF("box3.urdf", StartPosBox3, StartOrientationTable)
        

        Choix = [StartPosTot1,StartPosTot2,StartPosTot3]
        Positions = []
        while (len(Choix)>0):
            pos = choice(Choix)
            Positions.append(pos)
            Choix.remove(pos)

        Tot1_Id = pybullet.loadURDF("duck.urdf", Positions[0], StartOrientationTable)
        Tot2_Id = pybullet.loadURDF("eye.urdf", Positions[1], StartOrientationTable)
        Tot3_Id = pybullet.loadURDF("objet3.urdf", Positions[2], StartOrientationTable)

        pepper = simulation_manager.spawnPepper(client_id, spawn_ground_plane=True)
        pepper.angular_velocity = 1.0
        pepper.goToPosture("Stand", 0.6)
        pepper.setAngles("HeadPitch", 0.27, 0.27)

        return pepper

    def generate_world_2(self):
        simulation_manager = SimulationManager()
        client_id = simulation_manager.launchSimulation(gui=True)

        pybullet.setAdditionalSearchPath("/home/tp/Projet/g7_dupuis_dez_flachard")

        StartPosTable = [5.2,1,0.2]
        StartOrientationTable = pybullet.getQuaternionFromEuler([0,0,0])
        PlaneId = pybullet.loadURDF("table.urdf", StartPosTable, StartOrientationTable)

        StartPosLego = [2,0,0.1]
        PlaneId = pybullet.loadURDF("sofa_2.urdf", StartPosLego, StartOrientationTable)

        StartPosBox1 = [3.55, 1.5, -0.3]
        StartPosBox2 = [3.1, 2, -0.3]
        
        StartOrientationbox2 = pybullet.getQuaternionFromEuler([0,0,1.57])
        Box1 = pybullet.loadURDF("box.urdf", StartPosBox1, StartOrientationTable)
        Box2 = pybullet.loadURDF("box2.urdf", StartPosBox2, StartOrientationbox2)

        pepper = simulation_manager.spawnPepper(client_id, spawn_ground_plane=True)
        pepper.angular_velocity = 1.0
        pepper.goToPosture("Stand", 0.6)
        pepper.setAngles("HeadPitch", 0.27, 0.27)

        return pepper