# represente un oiseau
class Jeu():
    
    def __init__(self):
        self.enVol=False

        #la commande
        self.commande=[0,0]
        self.vMax=50

        #attributs par defaut
        self.x=100
        self.y=300
        self.vx=0
        self.vy=0
        self.ax=0
        self.ay=9
        self.dt=0.1

   

        #trajectoire sauvee
        self.traj=[]


    #modifier commande
    def setCommande(self,x,y):
        vMax=self.vMax
        
        #gere vitesse max
        d=x*x+y*y
        if (d>vMax*vMax):
            from math import sqrt
            d=sqrt(d)
            x=vMax*x/d
            y=vMax*y/d
            
            
        
        self.commande[0]=x
        self.commande[1]=y

        
        

        
    #faire evoluer l'oiseau
    def evoluer(self):
        global mouse

        # si est envol
        if (self.enVol):
            self.vx=self.vx+self.ax*self.dt
            self.vy=self.vy+self.ay*self.dt
            self.x=self.x+self.vx*self.dt
            self.y=self.y+self.vy*self.dt
    
            #met a jour trajectorie faite
            self.traj+=[[self.x,self.y]]       

            #rebond sol
            if (self.y>400)or(self.x>700):
                self.enVol=False
                self.x=100
                self.y=300
        else:
            #si on est en mode souris
            if(mouse):
                souris=pygame.mouse.get_pos()
                self.setCommande(souris[0]-self.x,souris[1]-self.y)
        
        
    #lance l'oiseau avec vitesse
    def lancer(self):

        
        
        #uniquement s'il n'est pas enVol
        if not(self.enVol):
            vitesse=[0,0]
            #met la vitesse Ã  partir de la commande
            vitesse[0]=-self.commande[0]
            vitesse[1]=-self.commande[1]
            
            #met la vitesse Ã  partir de la commande
            self.enVol=True
            self.vx=vitesse[0]
            self.vy=vitesse[1]

            self.commande=[0,0]
            self.traj=[]

    

    
    #dessiner oiseau
    def dessiner(self):
        WHITE = (0xFF, 0xFF, 0xFF)
        RED = (0xFF, 0x00, 0x00)
        BLUE = (0x00, 0x00, 0xFF)
        GREEN = (0x00, 0xFF, 0x00)
        BLACK = (0x00, 0x00, 0x00)
        screen.fill(WHITE)

        #dessine commande
        if (not(self.enVol)):
            #si la commande existe
            if not((self.commande[0]==0)and(self.commande[1]==0)):
                pygame.draw.line(screen,RED,[self.x,self.y],[self.x+self.commande[0],self.y+self.commande[1]],5)       

        #dessine oiseau
        if (not(self.enVol)):
            pygame.draw.rect(screen,BLUE,(jeu.x-5,jeu.y-5,10,10))
        else:
            pygame.draw.rect(screen,RED,(jeu.x-5,jeu.y-5,10,10))

        #dessine sol
        pygame.draw.line(screen,BLACK,[0,400],[700,400],5)

        #dessine trajectoire
        for i in range(len(self.traj)-1):
            pygame.draw.line(screen,GREEN,self.traj[i],self.traj[i+1],2)
           
            
        

import pygame
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moteur")


#boucle de jeu
done = False
mouse=False
jeu=Jeu()
# gestion horloge 
clock = pygame.time.Clock()

# -------- boucle de jeu
while not done:
    # --- Gestion des evenements
    for event in pygame.event.get():

        # quitter
        if event.type == pygame.QUIT: 
            done = True

        # cliquer souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse=True
            
        # lacher souris
        if event.type == pygame.MOUSEBUTTONUP:
            jeu.lancer()
            mouse=False
            
            
    # --- evolution jeu
    jeu.evoluer()
    
    # --- dessin
    jeu.dessiner()
   
    
    # --- mise a jour graphique
    pygame.display.flip()
    # --- attente
    clock.tick(60)

pygame.quit()