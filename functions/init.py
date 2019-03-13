import pygame, sys
from functions.classes import *

global verif,inMove,coord,assets,background,bird,birdCrush,birdCloud,catapulteAvant,catapulteArriere,surface,clock,coord,backend
# Initialisation global pygame
pygame.init()
WIDTH=1400
HEIGHT=409
surface     = pygame.display.set_mode((WIDTH, HEIGHT))
backend     = pygame.sprite.Group() # groupe de sprites décor du fond
middle      = pygame.sprite.Group() # groupe de sprites décor du fond
front       = pygame.sprite.Group() # groupe de sprites décor du fond

pygame.display.set_caption("Angry Piaf ;)")
clock = pygame.time.Clock()

# Variables globales
verif   = False
inMove  = False
coord   = ()
# Sprites Sheets
assets  = pygame.image.load('image/assets.png').convert_alpha()

# Sprites Simple
pig                         = assets.subsurface(726, 854, 53, 48)
bird                        = assets.subsurface(902, 798, 48, 44)
birdCrush                   = assets.subsurface(904,888, 49, 44)
birdCloud                   = assets.subsurface(908,842,46,44)

imageBird                   = assets.subsurface(902, 798, 48, 44)
imageBirdCrush              = assets.subsurface(904,888, 49, 44)
imageBirdCloud              = assets.subsurface(908,842,46,44)
imagePig                    = assets.subsurface(726, 854, 53, 48)
imageCatapulteAvant         = assets.subsurface(833, 0, 43, 126)
imageCatapulteArriere       = assets.subsurface(0, 0, 38, 200)
imageBackground             = pygame.image.load('image/background.png')
imageBackground             = pygame.transform.scale(imageBackground, (1400, 409))

# Sprites/objets du décor
background                  = decor("background",imageBackground,(0,0))
catapulteArriere            = decor("catapulteArriere",imageCatapulteArriere,(175, 150))
catapulteAvant              = decor("catapulteAvant",imageCatapulteAvant,(148, 142))

# Sprites/objets en mouvement
bird                        = birdObj("bird",imageBird,(177, 172),22,imageBirdCloud,imageBirdCrush)
pig                         = pigObj("pig",imagePig,(1000, 350),24,imageBirdCloud)
line1                       = lineObj((48, 23, 8), (200, 180), (160, 177), 20)
line2                       = lineObj((48, 23, 8), (160, 177), (160, 177), 0)

backend.add(background)
backend.add(catapulteArriere)
backend.add(line1)

middle.add(pig)
middle.add(bird)

front.add(line2)
front.add(catapulteAvant)