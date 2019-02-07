import pygame, sys, math

pygame.init()
surface = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
pygame.display.set_caption("Test controle")
clock = pygame.time.Clock()
clock.tick(30)
verif = False

def loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.VIDEORESIZE:
            surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)


while True:

    if pygame.mouse.get_pressed() == (1, 0, 0):
        if verif:
            verif = True
        else:
            if 155 <= pygame.mouse.get_pos()[0] <= 195 and 130 <= pygame.mouse.get_pos()[1] <= 170:
                verif = True
    else:
        verif = False

    if verif:
        if (pygame.mouse.get_pos()[0]-175)**2 + (pygame.mouse.get_pos()[1]-150)**2 <= 10000:
            surface.fill((255, 255, 255))
            pygame.draw.line(surface, (255, 0, 0), (175, 150), (175, 200), 3)
            pygame.draw.line(surface, (0, 255, 0), (175, 150), pygame.mouse.get_pos(), 3)
            pygame.draw.circle(surface, (255, 0, 0), pygame.mouse.get_pos(), 10)
        else:
            surface.fill((255, 255, 255))
            pygame.draw.line(surface, (255, 0, 0), (175, 150), (175, 200), 3)
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            coord = (int(100*((x-175)/(math.sqrt((x-175)**2+(y-150)**2)))+175),
                     (int(100*((y-150)/(math.sqrt((x-175)**2+(y-150)**2)))+150)))
            pygame.draw.line(surface, (0, 255, 0), (175, 150), coord, 3)
            pygame.draw.circle(surface, (255, 0, 0), coord, 10)
    else:
        surface.fill((255, 255, 255))
        pygame.draw.line(surface, (255, 0, 0), (175, 150), (175, 200), 3)
        pygame.draw.circle(surface, (255, 0, 0), (175, 150), 10)

    pygame.display.update()

    loop()
