import pygame
from math import sqrt
from math import asin
import functions.init as init
import functions.trajectoire as trajectoire

def run(x,y):
    # On vérifie si on "tient" l'oiseau
    if init.verif:
        # On vérifie si l'oiseau n'est pas sur le pilier central
        if 150 <= x <= 225 and y >= 215:
            # Affichage de l'élastique arrière
            init.line1.end_pos          = (init.coord[0] - 10, init.coord[1] - 2)
            init.line1.width            = 15

            # Prise des coordonnées de l'oiseau par rapport à la souris grace à la trigo
            init.coord                  = (int(65 * ((x - 177) / (sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 177),
                                            (int(65 * ((y - 150) / (sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 150)))

            # Modification de l'emplacement de l'oiseau
            init.bird.rect.center       = (init.coord[0], init.coord[1])

            # Affichage de l'élastique avant
            init.line2.end_pos          = (init.coord[0] - 10, init.coord[1])
            init.line2.width            = 15

        else:

            # On regarde si on a pas atteint la fin de la longueur de l'élastique
            if (x - 175) ** 2 + (y - 150) ** 2 <= 22500:
                longueur                = int(sqrt((x - 175) ** 2 + (y - 150) ** 2))

                init.line1.end_pos      = (x - 10, y - 2)
                init.line1.width        = 20 - int(longueur * 13 / 150)

                init.coord              = (x, y)
                init.bird.rect.center   = (init.coord[0], init.coord[1])

                init.line2.end_pos      = (x - 10, y)
                init.line2.width        = 20 - int(longueur * 13 / 150)

            else:                         
                init.line1.end_pos      = (init.coord[0] - 10, init.coord[1] - 2)
                init.line1.width        = 7

                init.coord              = (int(150 * ((x - 177) / (sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 177),
                                            (int(150 * ((y - 150) / (sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 150)))
                init.bird.rect.center   = (init.coord[0], init.coord[1])
                
                init.line2.end_pos      = (init.coord[0] - 10, init.coord[1])
                init.line2.width        = 7
        # Afficher la courbe de trajectoire dans tous les cas
        trajectoire.run()

    else:
        # oiseau au centre de la catapulte
        init.line1.end_pos      = (160, 177)
        init.line1.width        = 20
        init.line2.width        = 0             # on cache la ligne avant
        init.bird.rect.center   = (177, 172)

