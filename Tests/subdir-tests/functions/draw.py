import functions.init as init
import pygame, sys
def run():
    init.surface.fill((255, 255, 255))
    init.surface.blit(init.background,(0,0))
    init.surface.blit(init.catapulteArriere, (175, 150))
    init.surface.blit(init.catapulteAvant, (148, 142))
    init.surface.blit(init.bird, (153, 150))
    pygame.display.update()
    pygame.time.wait(150)