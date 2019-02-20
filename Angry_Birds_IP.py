import functions.init as init
import functions.bird_grab as bird_grab
import functions.graph_catapulte as graph_catapulte
import functions.loop as loop

###------------------------------------------------------------------------------------------------------------###
# Boucle draw qui tourne en continu afin de lancer toutes les fonctions à chaque tics

while True:
    # Lancement de toutes les fonctions dans l'ordre
    x,y=init.getPos()
    bird_grab.run(x,y)
    graph_catapulte.run(x,y)    
    loop.run()