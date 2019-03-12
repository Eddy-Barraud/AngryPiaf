import pygame
from math import sqrt
from math import asin
import functions.init as init
import functions.trajectoire as trajectoire

def run(x,y):
    # On refill la init.surface en blanc afin d'effacer toutes les images du tic précédent
    init.surface.fill((255, 255, 255))
    init.surface.blit(init.background,(0,0))
    # Catapulte d'arrière plan
    init.surface.blit(init.catapulteArriere, (175, 150))

    # On vérifie si on "tient" l'oiseau
    if init.verif:
        # On vérifie si l'oiseau n'est pas sur le pilier central
        if 150 <= x <= 225 and y >= 215:
            # Prise des init.coordonnées de l'oiseau par rapport à la souris grace à la trigo
            init.coord = (int(65 * ((x - 177) / (sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 177),
                        (int(65 * ((y - 150) / (sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 150)))
            pygame.draw.line(init.surface, (48, 23, 8), (200, 180), (init.coord[0] - 10, init.coord[1] - 2), 15)
            init.surface.blit(init.bird, (init.coord[0] - 24, init.coord[1] - 22))
            pygame.draw.line(init.surface, (48, 23, 8), (160, 177), (init.coord[0] - 10, init.coord[1]), 15)
        else:
            # On regarde si on a pas atteint la fin de la longueur de l'élastique
            if (x - 175) ** 2 + (y - 150) ** 2 <= 22500:
                longueur = int(sqrt((x - 175) ** 2 + (y - 150) ** 2))
                pygame.draw.line(init.surface, (48, 23, 8), (200, 180), (x - 10, y - 2), 20 - int(longueur * 13 / 150))
                init.coord = (x, y)
                init.surface.blit(init.bird, (init.coord[0] - 24, init.coord[1] - 22))
                pygame.draw.line(init.surface, (48, 23, 8), (160, 177), (x - 10, y), 20 - int(longueur * 13 / 150))
            else:
                init.coord = (int(150 * ((x - 177) / (sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 177),
                         (int(150 * ((y - 150) / (sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 150)))
                pygame.draw.line(init.surface, (48, 23, 8), (200, 180), (init.coord[0] - 10, init.coord[1] - 2), 7)
                init.surface.blit(init.bird, (init.coord[0] - 24, init.coord[1] - 22))
                pygame.draw.line(init.surface, (48, 23, 8), (160, 177), (init.coord[0] - 10, init.coord[1]), 7)
        # Catapulte à l'avant
        init.surface.blit(init.catapulteAvant, (148, 142))
        trajectoire.run()

    else:
        pygame.draw.line(init.surface, (48, 23, 8), (200, 180), (160, 177), 20)
        init.surface.blit(init.bird, (153, 150))
        # Catapulte à l'avant
        init.surface.blit(init.catapulteAvant, (148, 142))

    # Affichage sur l'écran de tout ce qu'on a fait précédemment
    pygame.display.update()
