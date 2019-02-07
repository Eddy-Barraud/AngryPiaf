from math import sqrt
from math import asin

def springLenght(x0,y0,x1,y1):
    return sqrt((x1-x0)**2+(y1-y0)**2)
def costheta(x0,y0,x1,y1):
    return (x1-x0)/springLenght(x0,y0,x1,y1)
def sintheta(x0,y0,x1,y1):
    return (y1-y0)/springLenght(x0,y0,x1,y1)
def sign(a):
    return int(a>0) - int(a<0)

### INI
x1,y1=1,1 #emplacement de l'origine de l'élastique
x0,y0=0.5,0.52
m=2
k=2000
L0=0.05
e=5/9

g=9.81
angle=asin(sintheta(x0,y0,x1,y1))


## Avant rebond -> equation de trajectoire parabolique
# On calcule la vitesse initiale avec l'energie potentielle élastique, puis on définie une équation de trajectoire (avec comme seule force le poids)
# On applique l'équation de trajectoire toutes les n ms pour établir une liste de points empruntés par le projectile
# On s'arrete quand on touche le sol, soit y=0 ou t=tfinal

C=sqrt(k/m)*(springLenght(x0,y0,x1,y1)-L0);C

v0x=C*costheta(x0,y0,x1,y1)
v0y=C*sintheta(x0,y0,x1,y1)

def Y(t):
    return -g*0.5*t**2+v0y*t+y0
def X(t):
    return v0x*t+x0

#Tf=solve(Y==0,t)[0].right().n()
Tf=(v0y+sqrt(v0y**2+2*g*y0))/g

T=0
P=[]
while T <= Tf:
    P+=[(X(T),Y(T))]
    T+=0.10

## Après rebond
## On recalcule des equations de trajectoires après application d'un coefficient de restitution
## On répète l'opération jusqu'à ce que le temp de rebond soit inférieur à 0.1s (minimum 2 rebonds)
## Le projectile est alors arreté (on pourrais rajouté des frottement au sol)
r=0


while Tf >= 0.1 or r <= 2 :
    v0x*=e
    v0y*=sign(angle)*e
    lastY=P[-1][1]
    lastX=P[-1][0]
    def Yr(t):
        return -g*0.5*t**2+v0y*t+lastY
    def Xr(t):
        return v0x*t+lastX
    Tf=(v0y+sqrt(v0y**2))/g #On estime que l'on part de l'ordonnée 0 (pas +v0y...)
    
    T=0
    while T <= Tf:
        P+=[(Xr(T),Yr(T))]
        T+=0.010
    r+=1
#On affiche la liste de points et l'élastique

#show(line(P,linestyle='--')+line([(1,1),(x0,y0)],color='red',thickness=3))

print(len(P))
#import matplotlib.pyplot as plt
#plt.plot([P[i][0] for i in range(len(P))], [P[i][1] for i in range(len(P))])
#plt.show()

import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.draw.lines(screen, (0,0,0), False, P, 1)
while True :
    pygame.display.update()
    pygame.time.delay(5000)
