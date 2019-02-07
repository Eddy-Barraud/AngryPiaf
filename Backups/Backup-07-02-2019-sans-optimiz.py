import pygame, sys, math

# Initialisation global pygame
pygame.init()
surface = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
pygame.display.set_caption("Test controle")
clock = pygame.time.Clock()
clock.tick(30)

# Variables globales
verif = False

# Sprites Sheets
assets = pygame.image.load('image/assets.png').convert_alpha()

# Sprites Simple
bird = assets.subsurface(902, 798, 48, 44)
catapulteAvant = assets.subsurface(833, 0, 43, 126)
catapulteArriere = assets.subsurface(0, 0, 38, 200)


# Pygame loop qui va chercher un évènement (souris, clavier, etc) tous les tics
def loop():
    # Fausse boucle for afin de récupérer les évènements
    for event in pygame.event.get():
        # Cas du déclenchement de la croix de la fenêtre
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Si l'utilisateur appuie sur entrée
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # Si l'utilisateur redimensionne la fenêtre
        if event.type == pygame.VIDEORESIZE:
            surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)


# Fonction qui vérifie si on a "attrapé" l'oiseau
def bird_grab(verif):
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if verif:
            return True
        else:
            if 143 <= x <= 206 and 140 <= y <= 204:
                return True
    else:
        return False


# Fonction qui s'occupe de l'affichage dela catapulte et de l'oiseau avant le lancement
def graph_catapulte(verif):
    # On refill la surface en blanc afin d'effacer toutes les images du tic précédent
    surface.fill((255, 255, 255))
    # Catapulte d'arrière plan
    surface.blit(catapulteArriere, (175, 150))

    # On vérifie si on "tient" l'oiseau
    if verif:
        # On vérifie si l'oiseau n'est pas sur le pilier central
        if 150 <= x <= 230 and y >= 215:
            # Prise des coordonnées de l'oiseau par rapport à la souris grace à la trigo
            coord = (int(65 * ((x - 177) / (math.sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 177),
                     (int(65 * ((y - 150) / (math.sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 150)))
            pygame.draw.line(surface, (48, 23, 8), (200, 180), (coord[0] - 10, coord[1] - 2), 15)
            surface.blit(bird, (coord[0] - 24, coord[1] - 22))
            pygame.draw.line(surface, (48, 23, 8), (160, 177), (coord[0] - 10, coord[1]), 15)
        else:
            # On regarde si on a pas atteint la fin de la longueur de l'élastique
            if (x - 175) ** 2 + (y - 150) ** 2 <= 22500:
                longueur = int(math.sqrt((x - 175) ** 2 + (y - 150) ** 2))
                pygame.draw.line(surface, (48, 23, 8), (200, 180), (x - 10, y - 2), 20 - int(longueur * 13 / 150))
                surface.blit(bird, (x - 24, y - 22))
                pygame.draw.line(surface, (48, 23, 8), (160, 177), (x - 10, y), 20 - int(longueur * 13 / 150))
            else:
                coord = (int(150 * ((x - 177) / (math.sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 177),
                         (int(150 * ((y - 150) / (math.sqrt((x - 177) ** 2 + (y - 150) ** 2))) + 150)))
                pygame.draw.line(surface, (48, 23, 8), (200, 180), (coord[0] - 10, coord[1] - 2), 7)
                surface.blit(bird, (coord[0] - 24, coord[1] - 22))
                pygame.draw.line(surface, (48, 23, 8), (160, 177), (coord[0] - 10, coord[1]), 7)
    else:
        surface.blit(bird, (153, 150))

    # Catapulte à l'avant
    surface.blit(catapulteAvant, (148, 142))

    # Affichage sur l'écran de tout ce qu'on a fait précédemment
    pygame.display.update()


# Boucle draw qui tourne en continu afin de lancer toutes les fonctions à chaque tics
while True:
    # Position de la souris affilié à des variables pour la lisibilité (update à chaque tics)
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    # Lancement de toutes les fonctions dans l'ordre
    verif = bird_grab(verif)
    graph_catapulte(verif)
    loop()