from qibullet import SimulationManager
from qibullet import PepperVirtual
import time

class deplacement():

    def destination_laser(self, x_goal, y_goal, pepper):  

        pepper.subscribeLaser()
        compteur_devant = 0
        compteur_gauche = 0
        compteur_droite = 0

        flag_front = 0
        flag_left = 0
        flag_right = 0

        Oppose = ""
        x_pepper, y_pepper, teta = pepper.getPosition()

        pepper.moveTo(x_goal, y_goal, 0, frame=PepperVirtual.FRAME_WORLD, _async=True)

        while(True):
            print(pepper.getPosition())
            #Si le pepper se trouve à proximité de la position désirée, il arrête la détection par laser
            x_pepper, y_pepper, teta = pepper.getPosition()
            if x_goal - 0.3 < x_pepper < x_goal + 0.3 and y_goal - 0.3 < y_pepper < y_goal + 0.3:
                break
            else:
                #Récupération des valeurs des lasers
                right_scan = pepper.getRightLaserValue()
                front_scan = pepper.getFrontLaserValue()
                left_scan = pepper.getLeftLaserValue()
                print("")
                print(front_scan)
                print("")

                for a in front_scan :
                    if a < 0.5:
                        compteur_devant += 1
                        #Si 5 lasers détectent un obstacle à proximité, on active le flag
                        if compteur_devant == 5:
                            flag_front = 1
                            compteur_devant = 0

                for b in left_scan :
                    if b < 0.5:
                        compteur_gauche += 1
                        #Si 5 lasers détectent un obstacle à proximité, on active le flag
                        if compteur_gauche == 5:
                            flag_left = 1
                            compteur_gauche = 0

                for c in right_scan :
                    if c < 0.5:
                        compteur_droite += 1
                        #Si 5 lasers détectent un obstacle à proximité, on active le flag
                        if compteur_droite == 5:
                            flag_right = 1 
                            compteur_droite = 0  
                

                print(flag_front)
                #Si des obstacles sont détectés à droite et devant, le pepper part dans le sens opposé
                if flag_front and flag_right :
                    Oppose = "Gauche"
                    pepper.moveTo(x_pepper, y_pepper + 1, 0, frame=PepperVirtual.FRAME_WORLD, _async=True)

                #Si des obstacles sont détectés à gauche et devant, le pepper part dans le sens opposé
                if flag_front and flag_left :
                    Oppose = "Droite"
                    pepper.moveTo(x_pepper, y_pepper - 1, 0, frame=PepperVirtual.FRAME_WORLD, _async=True)

                #Si un obstacle est détecté devant, le pepper part à gauche part défaut ou continu sa trajectoire
                #s'il doit sortir d'un coin
                if flag_front:
                    if Oppose == "Gauche":
                        pepper.moveTo(x_pepper, y_pepper + 1, 0, frame=PepperVirtual.FRAME_WORLD, _async=True)
                    if Oppose == "Droite":
                        pepper.moveTo(x_pepper, y_pepper - 1, 0, frame=PepperVirtual.FRAME_WORLD, _async=True)
                    if Oppose == "":
                        pepper.moveTo(x_pepper, y_pepper + 1, 0, frame=PepperVirtual.FRAME_WORLD, _async=True)

                #Si aucun obstacle n'est détecté devant, le pepper continue sur sa lancé pendant 2 secondes afin de sortit convenablement
                #puis il repart tout droit
                if flag_front == 0:
                    time.sleep(2)
                    pepper.moveTo(x_pepper + 1, y_pepper, 0, frame=PepperVirtual.FRAME_WORLD, _async=True)
                    Oppose = ""
                
                flag_front = 0
                flag_right = 0
                flag_left = 0
                
        #Une fois le pepper assez proche de la position finale, il se dirige vers cette position, arrêtant la détection par laser
        pepper.moveTo(x_goal, y_goal, 0, frame=PepperVirtual.FRAME_WORLD, _async=True)
        print(" ")
        print("Goal reached")
        print(" ")
        pepper.unsubscribeLaser()
        return