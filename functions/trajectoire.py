import pygame
import functions.init as init
from math import sqrt
from math import asin

def springLenght(x0, y0, x1, y1):
    return sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
def costheta(x0, y0, x1, y1):
    return (x1 - x0) / springLenght(x0, y0, x1, y1)
def sintheta(x0, y0, x1, y1):
    if springLenght(x0, y0, x1, y1) != 0:
        return (y1 - y0) / springLenght(x0, y0, x1, y1)
    else:

        return (y1 - y0) / 0.0001

def run():
    ### INI
    # On enregistre les coordonnées de l'oiseau au moment du laché de la souris
    x0, y0 = init.coord[0], 350 - init.coord[1]  # On inverse les coord Y pour faire les calculs
    x1, y1 = 177, 177  # emplacement de l'origine de l'élastique
    m = 2
    k = 5
    L0 = 10
    e = 5 / 9
    g = 9.81
    intervalle=0.120
    angle = asin(sintheta(x0, y0, x1, y1))
    totalTime = 0

    ## Avant rebond -> equation de trajectoire parabolique
    # On calcule la vitesse initiale avec l'energie potentielle élastique, puis on définie une équation de trajectoire (avec comme seule force le poids)
    # On applique l'équation de trajectoire toutes les n ms pour établir une liste de points empruntés par le projectile
    # On s'arrete quand on touche le sol, soit y=0 ou t=tfinal

    C = sqrt(k / m) * (springLenght(x0, y0, x1, y1) - L0);

    v0x = C * costheta(x0, y0, x1, y1)
    v0y = C * sintheta(x0, y0, x1, y1)

    def Y(t):
        return -g * 0.5 * t ** 2 + v0y * t + y0

    def X(t):
        return v0x * t + x0


    # Tf=solve(Y==0,t)[0].right().n()
    Tf = (v0y + sqrt(v0y ** 2 + 2 * g * y0)) / g
    totalTime += Tf
    T = 0
    P = []
    while T <= Tf:
        P += [[X(T), Y(T)]]
        T += intervalle
    P += [[X(Tf), Y(Tf)]]

    ## Après rebond
    ## On recalcule des equations de trajectoires après application d'un coefficient de restitution
    ## On répète l'opération jusqu'à ce que le temp de rebond soit inférieur à 0.1s (minimum 2 rebonds)
    ## Le projectile est alors arreté (on pourrais rajouté des frottement au sol)

    r = 0
    while Tf >= 0.1 or r <= 2:
        v0x *= e # coefficient de restitution
        v0y = -1 * (v0y - g * Tf) * e
        lastY = P[-1][1]
        lastX = P[-1][0]

        def Yr(t):
            return -g * 0.5 * t ** 2 + v0y * t + lastY

        def Xr(t):
            return v0x * t + lastX

        Tf = (v0y + sqrt(v0y ** 2)) / g  # On estime que l'on part de l'ordonnée 0 (pas +v0y...)
        totalTime += Tf
        T = 0
        while T <= Tf:
            P += [[Xr(T), Yr(T)]]
            T += intervalle
        P += [[Xr(Tf), Yr(Tf)]]
        r += 1

    # On retransforme dans les coord pygame
    for i in range(len(P)):
        P[i][1] = 350 - P[i][1]

    pygame.draw.lines(init.surface, (0, 0, 0), False, P, 3)
    return [P, totalTime / 10]  # 10 px = 1 m

