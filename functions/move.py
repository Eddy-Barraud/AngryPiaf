import pygame
import functions.init as init
import functions.trajectoire as traj
import functions.loop as loop

def run():
    init.inMove=True
    P,totalTime=traj.run()
    #print("distance parcourue en m : "+str(P[-1][0]))
    #print("total points :"+str(len(P)))
    #print("total time : "+str(totalTime))
    init.bird.points    = P     # On envoie la liste de points à l'objet bird
    init.bird.pointnb   = 0     # L'oiseau commence au point 0

    