import pygame
import functions.init as init
from math import sqrt

g           = 9.81
e           = 5/9
intervalle  = 1/60

def run(obj,orientation):

    if obj.vy >= -0.5 and orientation == "horizontal" : # si la vitesse n'est pas suffisente, pas de rebond en surface plane
        obj.points = obj.points[:obj.pointnb] # on arrete l'objet à ce point d'impact
        return

    elif obj.vy <= -0.5 and orientation == "horizontal": # rebond sur une surface plane

        v0x     = obj.vx
        v0y     = obj.vy
        v0x     *= e                            # coefficient de restitution
        v0y     = -1 * v0y * e                  # coefficient de restitution et inversion sens vitesse
        lastX   = (obj.rect.midbottom[0])/100   # les derniers points sont utilisés comme conditions initiales
        lastY   = (350 - obj.rect.midbottom[1])/100

        def Y(t):
            return -g * 0.5 * t ** 2 + v0y * t + lastY

        def X(t):
            return v0x * t + lastX

        Tf = (v0y + sqrt(v0y ** 2 + 2 * g * lastY)) / g
        T = 0
        P = []
        while T <= Tf: 
            P += [[X(T), Y(T)]]
            T += intervalle
        P += [[X(Tf), Y(Tf)]]

        for i in range(len(P)):
            P[i][0]*=100
            P[i][1]*=100
            P[i][1] = 350 - P[i][1]

        obj.points = P
        obj.pointnb = 0
        
        return



    elif obj.vx <= 0.5 and orientation == "vertical" : # rebond sur un côté
        v0x     = obj.vx
        v0y     = obj.vy
        v0x     = -1 * v0x * e                  # coefficient de restitution et inversion sens vitesse
        v0y     *= e                            # coefficient de restitution
        lastX   = (obj.rect.midbottom[0])/100   # les derniers points sont utilisés comme conditions initiales
        lastY   = (350 - obj.rect.midbottom[1])/100

        def Y(t):
            return -g * 0.5 * t ** 2 + v0y * t + lastY

        def X(t):
            return v0x * t + lastX

        Tf = (v0y + sqrt(v0y ** 2 + 2 * g * lastY)) / g
        T = 0
        P = []
        while T <= Tf: 
            P += [[X(T), Y(T)]]
            T += intervalle
        P += [[X(Tf), Y(Tf)]]

        for i in range(len(P)):
            P[i][0]*=100
            P[i][1]*=100
            P[i][1] = 350 - P[i][1]

        obj.points = P
        obj.pointnb = 0
        
        return

    elif obj.vx >= 0.5 and orientation == "vertical" : # passe a travers mais ralentit ???
        v0x     = obj.vx
        v0y     = obj.vy
        v0x     *= e                            # coefficient de restitution et inversion sens vitesse
        v0y     *= e                            # coefficient de restitution
        lastX   = (obj.rect.midbottom[0])/100   # les derniers points sont utilisés comme conditions initiales
        lastY   = (350 - obj.rect.midbottom[1])/100

        def Y(t):
            return -g * 0.5 * t ** 2 + v0y * t + lastY

        def X(t):
            return v0x * t + lastX

        Tf = (v0y + sqrt(v0y ** 2 + 2 * g * lastY)) / g
        T = 0
        P = []
        while T <= Tf: 
            P += [[X(T), Y(T)]]
            T += intervalle
        P += [[X(Tf), Y(Tf)]]

        for i in range(len(P)):
            P[i][0]*=100
            P[i][1]*=100
            P[i][1] = 350 - P[i][1]

        obj.points = P
        obj.pointnb = 0
        
        return