#                                                                                            #
##################################### {{{ Angry Piaf }}} #####################################
#                                                                                            #

""" On initialise le jeux et on déclare les variables "globales", plutard accessibles via "init.variable"
    Les images sont chargées, etc...
"""
import functions.init as init

""" Fonction bird_grab :
        Permet de passer la variable init.verif sur True si on clique au bon endroit, c.a.d sur l'oiseau.
        Une fois la variable vraie, les autres programmes se lancent
"""
import functions.bird_grab as bird_grab

""" Fonction graph_catapulte
        Affiche l'élastique et fait suivre l'oiseau avec la souris
"""
import functions.graph_catapulte as graph_catapulte

""" Fonction loop
        Gere touts les événements du jeux :
            - si on appui sur escape ou si on click sur fermé, le jeu se termine
            - si on lache la souris après avoir tiré sur l'élastique on enclenche la fonction move, pour lancer l'oiseau
            - si on appui sur espace pendant un lancé, le lancé est annulé et l'oiseau reviens à son origine
"""
import functions.loop as loop

""" Fonction trajectoire
        Calcule les points que va emprunter l'oiseau avec un intervale de temps donné
        Affiche également la courbe sur l'écran
        Cette fonction est appelée par grap_catapulte avant le lancé pour la courbe
        Cette fonction est appelée par move pour obtenir la liste des points
        Elle n'est toute fois pas chargée ici
"""

""" Fonction move
        Créer l'animation de l'oiseau qui suit point par point sa trajectoire à 120 fps
        Cette fonction est appelée par loop, lorsqu'on lache la souris après avoir visé
        Elle n'est toute fois pas chargée ici
"""

###------------------------------------------------------------------------------------------------------------###
# Boucle draw qui tourne en continu afin de lancer toutes les fonctions à chaque tics

while True:
    # Lancement de toutes les fonctions dans l'ordre
    x,y=init.pygame.mouse.get_pos() # Permet d'avoir les coordonnées de la souris à chacune de ces boucles, variables locales car appelées bcp de fois..
    bird_grab.run(x,y)
    graph_catapulte.run(x,y)
    loop.run()
    