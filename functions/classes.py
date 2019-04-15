import pygame
import functions.init as init
import functions.rebond as rebond
import functions.collision as collision
from math import sqrt

class decor(pygame.sprite.Sprite):
    def __init__(self, name, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.name         = name
        self.image        = image
        self.rect         = self.image.get_rect()
        self.rect.x,self.rect.y  = position

class birdObj(pygame.sprite.Sprite):
    """ Définition d'un objet de type oiseau """
    def __init__(self, name, image, position,radius,cloud,crush,state="normal"):
        pygame.sprite.Sprite.__init__(self)
        self.name         = name
        self.state        = state
        self.image        = image
        self.rect         = self.image.get_rect()
        self.resetPos     = position
        self.rect.center  = position
        self.radius       = radius

        self.imageNormal  = image
        self.imageCloud   = cloud
        self.imageCrush   = crush
        self.pointnb      = -1
        self.points       = []

        self.vitesse      = 0
        self.vx           = 0
        self.vy           = 0

    def update(self):
        if self.state    == "normal":
            self.image    = self.imageNormal
        elif self.state  == "cloud":
            self.image    = self.imageCloud
        elif self.state  == "crush":
            self.image    = self.imageCrush
        if self.pointnb >= 0:
            self.move()
        
        if init.groundLine.rect.collidepoint(self.rect.bottomright) and self.vy < 0 and self.pointnb > 4 and len(self.points) > 18 :
            rebond.run(self,"horizontal")
        

    def move(self):
        if self.pointnb == len(self.points): 
            # Animation : nuage de disparition
            pygame.time.wait(200)
            self.state = "cloud"
            self.pointnb+=1
            return

        if self.pointnb == len(self.points)+1: # si dernier point passé, effacer les listes,numeros...
            pygame.time.wait(650)
            self.state = "normal"
            self.pointnb            = -1
            self.points             = 0
            #init.inMove = False
            return

        i=self.points[self.pointnb]

        if i[0] - 153 >= 0 or i[1] - 150 <= 0:
            init.line1.end_pos = (160, 177)
            init.line1.width = 20
            init.line2.width = 0
        else :
            init.line1.end_pos = (i[0] - 10, i[1] - 2)
            init.line1.width = 7
            init.line2.end_pos = (i[0] - 10, i[1])
            init.line2.width = 7

        if i == self.points[-2]: # On passe a l'état crush à l'avant dernier point            
            self.state = "crush"

        self.vx         = (self.points[self.pointnb][0]-self.points[self.pointnb-1][0]) / (1/60) # vx = dx/dt
        self.vx        *= 1/100 # 100px = 1m
        self.vy         = (self.points[self.pointnb][1]-self.points[self.pointnb-1][1]) / (1/60)
        self.vy        *= -1/100 # 100px = 1m et y vers le haut
        self.vitesse    = sqrt(self.vx**2+self.vy**2)

        self.rect.midbottom    = i
        self.pointnb        += 1

    def reset(self):
        self.rect.center  = self.resetPos
        self.vitesse      = 0
        self.vx           = 0
        self.vy           = 0
        self.pointnb      = -1
        self.points       = []
        self.state        = "normal"


class pigObj(pygame.sprite.Sprite):
    """ Définition d'un objet de type cochon """
    def __init__(self, name, image, position,radius,cloud):
        pygame.sprite.Sprite.__init__(self)
        self.name         = name
        self.image        = image
        self.rect         = self.image.get_rect()
        self.resetPos     = position
        self.rect.center  = position
        self.radius       = radius
        self.imageCloud   = cloud
        self.imageNormal  = image
        self.die          = False
        self.countdown    = 0
    
    def update(self):
        for i in init.middle:
            if i != self and type(i) == birdObj and pygame.sprite.collide_circle(self, i):
                self.disparait()
        if self.die == True and self.countdown < 7:
            self.countdown += 1
        elif self.die == True and self.countdown >= 7:
            self.remove(init.middle)
            # On reset les variables
            self.die        = False
            self.image      = self.imageNormal
            self.countdown  = 0

    def disparait(self):
        self.image    = self.imageCloud
        self.die   = True

    
    def reset(self):
        self.rect.center  = self.resetPos
        self.die   = False
        self.image      = self.imageNormal
        self.countdown  = 0
        init.middle.add(self)


class woodObj(pygame.sprite.Sprite):
    """ Définition d'un objet de type bois """
    def __init__(self, image, position,orientation,broken):
        pygame.sprite.Sprite.__init__(self)
        self.image        = image
        self.rect         = self.image.get_rect()
        self.rect.center  = position
        self.resetPos     = position
        self.die          = False
        self.orientation  = orientation
        self.die          = False
        self.countdown    = 0
        self.vx           = 0
        self.vy           = 0
        self.vitesse      = 0
        self.state        = "normal"
        self.pointnb      = -1
        self.points       = []

        if orientation == "horizontal" :
            self.imageBroken    = broken
            self.imageNormal    = image
        elif orientation == "vertical" :
            self.image          = pygame.transform.rotate(image,90)
            self.rect           = self.image.get_rect()
            self.rect.center    = position
            self.imageBroken    = pygame.transform.rotate(broken,90)
            self.imageNormal    = pygame.transform.rotate(image,90)

    def update(self):
        if self.state    == "normal":
            self.image    = self.imageNormal
        elif self.state  == "broken":
            self.image    = self.imageBroken
        if self.pointnb >= 0:
            self.move()

        for bird in init.middle:                        # Des qu'un oiseau entre en contact avec le bois, on change sa trajectoire
            if type(bird) == birdObj and (self.rect.collidepoint(bird.rect.bottomright) or self.rect.collidepoint(bird.rect.bottomleft)) and bird.pointnb > 3 and len(bird.points) > 17:
                if self.orientation == "horizontal" : # alors arrive sur le dessus
                    if bird.vitesse <= 9 and self.state != "broken" :  # si vitesse faible rebond sauf si déjà fragilisé
                        rebond.run(bird,"horizontal")
                        self.state = "broken"
                    else :                              # si vitesse trop élevée alors casse
                        self.disparait()
                        collision.run(bird)  # collision qui ralentie l'obj
                else:                                   # alors arrive sur le côté
                    if bird.vitesse <= 9 and self.state != "broken" :  # si vitesse faible rebond sauf si déjà fragilisé
                        self.state = "broken"
                        rebond.run(bird,"vertical")     # rebondi sur la paroie et la fragilise
                    else :                              # si vitesse trop élevée alors casse
                        self.state = "broken"
                        self.disparait()
                        collision.run(bird)  # collision qui ralentie l'obj
                        

        if self.die == True and self.countdown < 7:
            self.countdown += 1
        elif self.die == True and self.countdown >= 7:
            self.remove(init.middle)
            # On reset les variables
            self.die        = False
            self.image      = self.imageNormal
            self.countdown  = 0

    
    def disparait(self):
        self.state = "broken"
        self.die   = True

    def move(self):

        if self.pointnb == len(self.points)+1: # si dernier point passé, effacer les listes,numeros...
            self.state = "normal"
            self.pointnb            = -1
            self.points             = 0
            return

        i=self.points[self.pointnb]

        self.vx         = (self.points[self.pointnb][0]-self.points[self.pointnb-1][0]) / (1/60) # vx = dx/dt
        self.vx        *= 1/100 # 100px = 1m
        self.vy         = (self.points[self.pointnb][1]-self.points[self.pointnb-1][1]) / (1/60)
        self.vy        *= -1/100 # 100px = 1m et y vers le haut
        self.vitesse    = sqrt(self.vx**2+self.vy**2)

        self.rect.midbottom    = i
        self.pointnb        += 1

    def reset(self):
        self.rect.center  = self.resetPos
        self.vitesse      = 0
        self.vx           = 0
        self.vy           = 0
        self.pointnb      = -1
        self.points       = []
        self.state        = "normal"
        self.die          = False
        self.countdown    = 0
        init.middle.add(self)

class lineObj(pygame.sprite.Sprite):
    """ Définition d'un objet de type ligne """
    def __init__(self, color, start_pos, end_pos, width=1):
        pygame.sprite.Sprite.__init__(self)
        self.color        = color
        self.start_pos    = start_pos
        self.end_pos      = end_pos
        self.end_posLast  = end_pos
        self.width        = width
        self.widthLast    = width
        self.image        = pygame.Surface([init.WIDTH,init.HEIGHT], pygame.SRCALPHA)
        self.image        = self.image.convert_alpha()
        pygame.draw.line(self.image, self.color, self.start_pos, self.end_pos, self.width)
        self.rect         = pygame.Rect(start_pos[0], start_pos[1],end_pos[0]-start_pos[0] , width)

    def update(self):
        if self.end_pos != self.end_posLast or self.width != self.widthLast: #update only if modification made
            self.image            = pygame.Surface([init.WIDTH,init.HEIGHT], pygame.SRCALPHA)
            self.image            = self.image.convert_alpha()
            pygame.draw.line(self.image, self.color, self.start_pos, self.end_pos, self.width)
            self.rect             = self.image.get_rect()
            self.end_posLast      = self.end_pos
            self.widthLast        = self.width
        
