import pygame
import functions.init as init
import functions.trajectoire as traj
import functions.loop as loop

def run():
    pygame.mixer.Sound.play(init.lancer)
    init.inMove=True
    P=traj.run()
    init.bird.points    = P     # On envoie la liste de points à l'objet bird
    init.bird.pointnb   = 0     # L'oiseau commence au point 0


    