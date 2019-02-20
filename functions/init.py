import pygame, sys
global verif,inMove,coord,assets,background,bird,birdCrush,birdCloud,catapulteAvant,catapulteArriere,surface,clock,coord
# Initialisation global pygame
pygame.init()
surface = pygame.display.set_mode((1400, 409), pygame.RESIZABLE)
pygame.display.set_caption("Angry Piaf ;)")
clock = pygame.time.Clock()

# Variables globales
verif = False
inMove = False
coord = ()
# Sprites Sheets
assets = pygame.image.load('image/assets.png').convert_alpha()
background = pygame.image.load('image/background.png')
background = pygame.transform.scale(background, (1400, 409))
# Sprites Simple
bird = assets.subsurface(902, 798, 48, 44)
birdCrush = assets.subsurface(904,888, 49, 44)
birdCloud = assets.subsurface(908,842,46,44)
catapulteAvant = assets.subsurface(833, 0, 43, 126)
catapulteArriere = assets.subsurface(0, 0, 38, 200)

def getPos():
    # Position de la souris affilié à des variables pour la lisibilité (update à chaque tics)
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    return(x,y)