import pygame
import functions.init as init
import functions.trajectoire as traj
import functions.loop as loop

def run():
    init.inMove=True
    P,totalTime=traj.run()
    #print("distance parcourue en m : "+str(P[-1][0]))
    #print("total points :"+str(len(P)))
    #print("total time : "+str(totalTime))

    for i in P:
        init.clock.tick(120)
        init.surface.fill((255, 255, 255))
        init.surface.blit(init.background,(0,0))
        init.surface.blit(init.catapulteArriere, (175, 150))
        
        if i == P[-1] : # On affiche l'oiseau mort au dernier point
            init.surface.blit(init.birdCrush, (i[0],i[1]-44)) # On décale le y de 44=hauteur de l'oiseau
        else :
            init.surface.blit(init.bird, (i[0],i[1]-44)) # On décale le y de 42=hauteur de l'oiseau

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
        init.surface.blit(init.birdCloud,(P[-1][0],P[-1][1]-44))
        init.surface.blit(init.bird, (153, 150))
        init.surface.blit(init.catapulteAvant, (148, 142))
        pygame.display.update()
        pygame.time.wait(150)
        init.inMove=False