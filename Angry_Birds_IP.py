import pygame, sys
from math import sqrt
from math import asin

# Initialisation global pygame
pygame.init()
surface = pygame.display.set_mode((1400, 500), pygame.RESIZABLE)
pygame.display.set_caption("Angry Piaf ;)")
clock = pygame.time.Clock()

# Variables globales
verif = False
inMove = False
coord= ()
# Sprites Sheets
assets = pygame.image.load('image/assets.png').convert_alpha()

# Sprites Simple
bird = assets.subsurface(902, 798, 48, 44)
birdCrush = assets.subsurface(904,888, 49, 42)

catapulteAvant = assets.subsurface(833, 0, 43, 126)
catapulteArriere = assets.subsurface(0, 0, 38, 200)

###------------------------------------------------------------------------------------------------------------###
# Pygame loop qui va chercher un évènement (souris, clavier, etc) tous les tics et démarrer le lancé
def loop():
    global verif
    global inMove
    # Fausse boucle for afin de récupérer les évènements
    for event in pygame.event.get():
        # Cas du déclenchement de la croix de la fenêtre
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Si l'utilisateur appuie sur entrée
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # Si l'utilisateur redimensionne la fenêtre
        elif event.type == pygame.VIDEORESIZE:
            surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        # Des qu'on lache la souris après avoir bougé l'oiseau, on lance la simu
        elif event.type == pygame.MOUSEBUTTONUP and verif:
            move()

    # Fonction pour économiser du CPU quand il ne se passe rien
    if pygame.mouse.get_pressed() != (1, 0, 0) and inMove == False:
        #pygame.time.wait(50)
        clock.tick(30)

###------------------------------------------------------------------------------------------------------------###
# Fonction qui vérifie si on a "attrapé" l'oiseau
# Passe la variable globale verif à 1 si on click sur l'oiseau et maintient le verif à 1
def bird_grab():
    global verif
    if pygame.mouse.get_pressed() == (1, 0, 0) and (verif or 143 <= x <= 206 and 140 <= y <= 204):
        verif=True
    else:
        verif=False

###------------------------------------------------------------------------------------------------------------###
# Fonction qui s'occupe de l'affichage de la catapulte et de l'oiseau avant le lancement
def graph_catapulte():
    global verif
    global x
    global y
    global coord
    # On refill la surface en blanc afin d'effacer toutes les images du tic précédent
    surface.fill((255, 255, 255))
    # Catapulte d'arrière plan
    surface.blit(catapulteArriere, (175, 150))

    # On vérifie si on "tient" l'oiseau
    if verif:
        # On vérifie si l'oiseau n'est pas sur le pilier central
        if 150 <= x <= 230 and y >= 215:
            # Prise des coordonnées de l'oiseau par rapport à la souris grace à la trigo
            coord = (int(65 * ((x - 177) / (sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 177),
                     (int(65 * ((y - 150) / (sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 150)))
            pygame.draw.line(surface, (48, 23, 8), (200, 180), (coord[0] - 10, coord[1] - 2), 15)
            surface.blit(bird, (coord[0] - 24, coord[1] - 22))
            pygame.draw.line(surface, (48, 23, 8), (160, 177), (coord[0] - 10, coord[1]), 15)
        else:
            # On regarde si on a pas atteint la fin de la longueur de l'élastique
            if (x - 175) ** 2 + (y - 150) ** 2 <= 22500:
                longueur = int(sqrt((x - 175) ** 2 + (y - 150) ** 2))
                pygame.draw.line(surface, (48, 23, 8), (200, 180), (x - 10, y - 2), 20 - int(longueur * 13 / 150))
                coord=(x, y)
                surface.blit(bird, (coord[0] - 24, coord[1] - 22))
                pygame.draw.line(surface, (48, 23, 8), (160, 177), (x - 10, y), 20 - int(longueur * 13 / 150))
            else:
                coord = (int(150 * ((x - 177) / (sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 177),
                         (int(150 * ((y - 150) / (sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 150)))
                pygame.draw.line(surface, (48, 23, 8), (200, 180), (coord[0] - 10, coord[1] - 2), 7)
                surface.blit(bird, (coord[0] - 24, coord[1] - 22))
                pygame.draw.line(surface, (48, 23, 8), (160, 177), (coord[0] - 10, coord[1]), 7)
        trajectoire() 
    else:
        surface.blit(bird, (153, 150))

    # Catapulte à l'avant
    surface.blit(catapulteAvant, (148, 142))

    # Affichage sur l'écran de tout ce qu'on a fait précédemment
    pygame.display.update()
###------------------------------------------------------------------------------------------------------------###
# Quelques fonctions pratiques pour la suite ...
def springLenght(x0,y0,x1,y1):
    return sqrt((x1-x0)**2+(y1-y0)**2)
def costheta(x0,y0,x1,y1):
    return (x1-x0)/springLenght(x0,y0,x1,y1)
def sintheta(x0,y0,x1,y1):
    return (y1-y0)/springLenght(x0,y0,x1,y1)
def sign(a):
    return int(a>0) - int(a<0)
###------------------------------------------------------------------------------------------------------------###
# Fonction qui trace instantannement la courbe que va emprunté l'oiseau
def trajectoire():
    ### INI
    #On enregistre les coordonnées de l'oiseau au moment du laché de la souris
    global coord
    x0,y0=coord[0],350-coord[1] #On inverse les coord Y pour faire les calculs
    x1,y1=153, 150 #emplacement de l'origine de l'élastique
    m=2
    k=5
    L0=10
    e=5/9
    g=9.81
    angle=asin(sintheta(x0,y0,x1,y1))
    totalTime=0

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
    totalTime+=Tf
    T=0
    P=[]
    while T <= Tf:
        P+=[[X(T),Y(T)]]
        T+=0.100
    P+=[[X(Tf),Y(Tf)]]

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
        totalTime+=Tf
        T=0
        while T <= Tf:
            P+=[[Xr(T),Yr(T)]]
            T+=0.100
        P+=[[Xr(Tf),Yr(Tf)]]
        r+=1

    # On retransforme dans les coord pygame
    for i in range(len(P)):
        P[i][1]=350-P[i][1]
    
    pygame.draw.lines(surface, (0,0,0), False, P, 3)
    return [P,totalTime/10] #10 px = 1 m
    
###------------------------------------------------------------------------------------------------------------###
# Fonction éponyme...
def move():
    global inMove
    inMove=True
    P,totalTime=trajectoire()
    #print("distance parcourue en m : "+str(P[-1][0]))
    #print("total points :"+str(len(P)))
    #print("total time : "+str(totalTime))
    fps=1/(totalTime/len(P))
    #print("fps : "+str(fps))

    for i in P:
        clock.tick(fps)
        surface.fill((255, 255, 255))
        surface.blit(catapulteArriere, (175, 150))
        surface.blit(catapulteAvant, (148, 142))
        
        if i[1] <= 349 :
            surface.blit(bird, (i[0],i[1]-44)) # On décale le y de 44=hauteur de l'oiseau
        else :
            surface.blit(birdCrush, (i[0],i[1]-42)) # On décale le y de 42=hauteur de l'oiseau

        pygame.display.update()
        loop()
        #pygame.time.wait(5)
    pygame.time.wait(500)
    inMove=False

###------------------------------------------------------------------------------------------------------------###
# Boucle draw qui tourne en continu afin de lancer toutes les fonctions à chaque tics
while True:
    # Position de la souris affilié à des variables pour la lisibilité (update à chaque tics)
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    # Lancement de toutes les fonctions dans l'ordre
    bird_grab()
    graph_catapulte()
    loop()
