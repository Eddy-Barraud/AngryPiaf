import pygame
import functions.init as init
import functions.trajectoire as traj
import functions.loop as loop

def run():
    init.inMove=True
    P,totalTime=traj.run()
    elastique = True
    #print("distance parcourue en m : "+str(P[-1][0]))
    #print("total points :"+str(len(P)))
    #print("total time : "+str(totalTime))

    for i in P:
        init.clock.tick(120)
        init.surface.fill((255, 255, 255))
        init.surface.blit(init.background,(0,0))
        init.surface.blit(init.catapulteArriere, (175, 150))

        if i[0] - 153 <= 0 or i[1] - 150 <= 0:
            elastique = False

        if i == P[-1]: # On affiche l'oiseau mort au dernier point
            pygame.draw.line(init.surface, (48, 23, 8), (200, 180), (160, 177), 20)
            init.surface.blit(init.birdCrush, (i[0] - 24, i[1] - 22))
        else :
            if elastique:
                pygame.draw.line(init.surface, (48, 23, 8), (200, 180), (i[0] - 10, i[1] - 2), 7)
                # On décale le y et le x de 22=hauteur/2 et 24=largeur/2 de l'oiseau
                init.surface.blit(init.bird, (i[0]-24,i[1]-22))
                pygame.draw.line(init.surface, (48, 23, 8), (160, 177), (i[0] - 10, i[1]), 7)
            else:
                pygame.draw.line(init.surface, (48, 23, 8),(200,180),(160,177),20)
                init.surface.blit(init.bird, (i[0]-24,i[1]-22))

        init.surface.blit(init.catapulteAvant, (148, 142))
        pygame.display.update()
        loop.run()
        if init.inMove == False:
            break
    if init.inMove == True :
        # Animation : nuage de disparition
        pygame.time.wait(500)
        init.surface.fill((255, 255, 255))
        init.surface.blit(init.background,(0,0))
        init.surface.blit(init.catapulteArriere, (175, 150))
        init.surface.blit(init.birdCloud,(P[-1][0]-24,P[-1][1]-22))
        init.surface.blit(init.bird, (153, 150))
        init.surface.blit(init.catapulteAvant, (148, 142))
        pygame.display.update()
        pygame.time.wait(150)
        init.inMove=False