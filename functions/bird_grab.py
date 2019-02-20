import pygame
import functions.init as init
def run(x,y):
    if pygame.mouse.get_pressed() == (1, 0, 0) and (init.verif or 143 <= x <= 206 and 140 <= y <= 204):
        init.verif = True
    else:
        init.verif = False