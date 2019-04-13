import pygame,sys
import functions.init as init
import functions.move as move

def run():
    # Fausse boucle for afin de récupérer les évènements
    for event in pygame.event.get():
        # Cas du déclenchement de la croix de la fenêtre
        if event.type == pygame.QUIT:
            init.running = False
            pygame.quit()
            sys.exit()            
        # Si l'utilisateur appuie sur escape
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                init.inMove = False
                init.bird.pointnb = -1
                init.middle.add(init.pig)
                init.addWood()
            if event.key == pygame.K_ESCAPE:
                init.running = False
                pygame.quit()
                sys.exit()
        # Si l'utilisateur redimensionne la fenêtre
        '''elif event.type == pygame.VIDEORESIZE:
            init.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            # On remet à l'échelle l'image de fond
            init.background = pygame.transform.scale(init.background, (event.w, event.h))'''
        # Des qu'on lache la souris après avoir bougé l'oiseau, on lance la simu
        if event.type == pygame.MOUSEBUTTONUP and init.verif and init.inMove == False:
            init.verif = False
            move.run()

    # Fonction pour économiser du CPU quand il ne se passe rien
    if pygame.mouse.get_pressed() != (1, 0, 0) and init.inMove == False:
        # pygame.time.wait(50)
        init.clock.tick(10)