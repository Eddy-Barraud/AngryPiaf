import pygame
WINDOW_WIDTH=400
WINDOW_HEIGHT=400

pygame.init()
WINDOW  = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
SPRITES = pygame.sprite.Group()

class pigSprite(pygame.sprite.Sprite):
    def __init__(self, name, image, position,radius):
        pygame.sprite.Sprite.__init__(self)
        self.name         = name
        self.image        = image
        self.rect         = self.image.get_rect()
        self.rect.center  = position
        self.radius       = radius
        self.move         = False
        self.dir          = [5,5]

    def update(self):
        # Move the sprite
        if self.move == True:
            self.rect.center = (self.rect.center[0]+self.dir[0], self.rect.center[1]+self.dir[1])
        # Have we collided with any sprite?
        #hit_by = pygame.sprite.spritecollide( self, SPRITES, False )
        #hit_by.remove( self ) # other than ourselves
        hit_by=[]
        for i in SPRITES:
            if i != self and pygame.sprite.collide_circle(self, i):
                hit_by +=[i]
                self.move = True
                self.dir[0] *= -1
                self.dir[1] *= -1
                i.move = True

        if self.rect.topright[0] > WINDOW_WIDTH:
            self.dir[0] *= -1
        elif self.rect.bottomright[1] > WINDOW_HEIGHT:
            self.dir[1] *= -1
        elif self.rect.topleft[0] < 0:
            self.dir[0] *= -1
        elif self.rect.topleft[1] < 0:
            self.dir[1] *= -1

        for other_pig in hit_by:
            print( "Sprite [%s] collided with [%s] at x=%s,y=%s" % ( self.name, other_pig.name, self.rect.center[0], self.rect.center[1] ) )


# Make some sprites, including two that overlap
background = pygame.image.load('image/background.png')
assets = pygame.image.load('Tests/assets.png').convert_alpha()
sprite_image = assets.subsurface(726, 854, 52, 46)
pig_01 = pigSprite( "pig01", sprite_image, (30, 30), 23 )
pig_01.move=True
pig_02 = pigSprite( "pig02", sprite_image, (150, 150), 23 )
pig_03 = pigSprite( "pig03", sprite_image, (90, 90), 23 )
pig_04 = pigSprite( "pig04", sprite_image, (200, 90), 23 )
pig_05 = pigSprite( "pig05", sprite_image, (200, 250), 23 )
pig_06 = pigSprite( "pig06", sprite_image, (360, 20), 23 )
pig_06.move=True
# Add them to the global SPRITE group
SPRITES.add(pig_01)
SPRITES.add(pig_02)
SPRITES.add(pig_03)
SPRITES.add(pig_04)
SPRITES.add(pig_05)
SPRITES.add(pig_06)

clock = pygame.time.Clock()
done = False
while not done:

    # Move the sprites (and checks for collisions)
    SPRITES.update()

    # Paint the screen
    WINDOW.fill( ( 255,255,255 ) )
    WINDOW.blit(background,(0,0))
    SPRITES.draw( WINDOW )
    pygame.display.update()
    pygame.display.flip()

    # Check for user-events
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            done = True

    clock.tick_busy_loop(30)