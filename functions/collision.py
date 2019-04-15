import pygame
import functions.init as init
from functions.trajectoire import basicTraj
from math import sqrt


def run(obj): # ralentissement sur une surface plane
    e = init.eCol
    v0x     = obj.vx
    v0y     = obj.vy
    v0x     *= e                                    # coefficient de ralentissement
    v0y     *= e                                    # coefficient de ralentissement et inversion sens vitesse
    lastX   = (obj.rect.midbottom[0])/100           # les derniers points sont utilisés comme conditions initiales
    lastY   = (355 - obj.rect.midbottom[1])/100     # 355 pour aller un peu plus loin et provoquer le rebond sur la groundLine

    obj.points  = basicTraj(lastX,lastY,v0x,v0y)
    obj.pointnb = 0

    return

