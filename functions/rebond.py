import pygame
import functions.init as init
from functions.trajectoire import basicTraj
from math import sqrt


def run(obj,orientation):

    e = init.e
    if obj.vy >= -0.3 and orientation == "horizontal" : # si la vitesse n'est pas suffisante, pas de rebond en surface plane
        obj.points = obj.points[:obj.pointnb] # on arrete l'objet à ce point d'impact
        return

    elif obj.vy <= -0.3 and orientation == "horizontal": # rebond sur une surface plane

        v0x     = obj.vx
        v0y     = obj.vy
        v0x     *= e                            # coefficient de restitution
        v0y     = -1 * v0y * e                  # coefficient de restitution et inversion sens vitesse
        
        lastX   = (obj.rect.midbottom[0])/100   # les derniers points sont utilisés comme conditions initiales
        lastY   = (355 - obj.rect.midbottom[1])/100 # 355 pour aller un peu plus loin et provoquer le rebond sur la groundLine
        
        obj.points  = basicTraj(lastX,lastY,v0x,v0y)
        obj.pointnb = 0
        
        return



    elif orientation == "vertical" : # rebond sur un côté
        v0x     = obj.vx
        v0y     = obj.vy
        v0x     = -1 * v0x * e                  # coefficient de restitution et inversion sens vitesse
        v0y     *= e                            # coefficient de restitution
        lastX   = (obj.rect.midbottom[0])/100   # les derniers points sont utilisés comme conditions initiales
        lastY   = (355 - obj.rect.midbottom[1])/100

        obj.points  = basicTraj(lastX,lastY,v0x,v0y)
        obj.pointnb = 0
        
        return