import pygame, sys
from functions.classes import *
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (245,190) #position initiale de la fenêtre

global verif,inMove,coord,assets,background,bird,birdCrush,birdCloud,catapulteAvant,catapulteArriere,surface,clock,coord,backend,running,values,valuesTraj,intervalle,fps

# Variables globales
running     = True
verif       = False
inMove      = False
coord       = [0,0]
valuesTraj  = ""
fps         = 60
intervalle  = 1/fps
e           = 5/9

# Initialisation global pygame
pygame.init()
WIDTH=1400
HEIGHT=409
surface     = pygame.display.set_mode((WIDTH, HEIGHT))
backend     = pygame.sprite.Group() # groupe de sprites décor du fond
middle      = pygame.sprite.Group() # groupe de sprites décor du milieu
front       = pygame.sprite.Group() # groupe de sprites décor du devant
allSprites  = pygame.sprite.Group() # groupe de sprite pour tous les objets du milieu
pygame.display.set_caption("Angry Piaf ;)")
clock = pygame.time.Clock()


# Sprites Sheets
assets  = pygame.image.load('image/assets.png').convert_alpha()
assetsWood  = pygame.image.load('image/ingame_blocks_wood.png').convert_alpha()

# Sprites Simple

imageBird                   = assets.subsurface(902, 798, 48, 44)
imageBirdCrush              = assets.subsurface(904,888, 49, 44)
imageBirdCloud              = assets.subsurface(908,842,46,44)

imagePig                    = assets.subsurface(726, 854, 53, 48)

imageCatapulteAvant         = assets.subsurface(833, 0, 43, 126)
imageCatapulteArriere       = assets.subsurface(0, 0, 38, 200)

imageBackground             = pygame.image.load('image/background.png')
imageBackground             = pygame.transform.scale(imageBackground, (1400, 409))

imageWoodBroken             = assetsWood.subsurface(373,367, 83, 20)
imageWood                   = assetsWood.subsurface(288,345, 83, 20)
imageBigWood             = assetsWood.subsurface(289,169, 203, 20)
imageBigWoodBroken                   = assetsWood.subsurface(289,235, 203, 20)

# Sprites/objets du décor
background                  = decor("background",imageBackground,(0,0))
catapulteArriere            = decor("catapulteArriere",imageCatapulteArriere,(175, 150))
catapulteAvant              = decor("catapulteAvant",imageCatapulteAvant,(148, 142))

# Sprites/objets en mouvement
bird                        = birdObj("bird",imageBird,(177, 172),25,imageBirdCloud,imageBirdCrush)
pig                         = pigObj("pig",imagePig,(1000, 326),24,imageBirdCloud)
line1                       = lineObj((48, 23, 8), (200, 180), (160, 177), 20)
line2                       = lineObj((48, 23, 8), (160, 177), (160, 177), 0)
groundLine                  = lineObj((0,0,0,), (0, 350), (1400, 350), 10)

woodListV                    = [(910,225.5),(910,308.5),(1093,225.5),(1093,308.5)]
woodBigListH                 = [(1000,174)]



backend.add(background)
backend.add(catapulteArriere)
backend.add(groundLine)
backend.add(line1)

for w in woodListV :
    middle.add(woodObj(imageWood,w,"vertical",imageWoodBroken))
    allSprites.add(woodObj(imageWood,w,"vertical",imageWoodBroken))
for w in woodBigListH :
    middle.add(woodObj(imageBigWood,w,"horizontal",imageBigWoodBroken))
    allSprites.add(woodObj(imageBigWood,w,"horizontal",imageBigWoodBroken))
middle.add(pig)
allSprites.add(pig)
middle.add(bird)
allSprites.add(bird)

front.add(line2)
front.add(catapulteAvant)

import functions.infoWindow