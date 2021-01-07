import pygame, random

BLACK= (0, 0, 0)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 490

SCREEN= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK= pygame.time.Clock()
pygame.display.set_caption("Shingeki No Frogger")
ICON= pygame.image.load("images/wingsOfFreedom.png")
pygame.display.set_icon(ICON)
background = pygame.image.load('images/background1.jpg')

pygame.mixer.music.load('sound/AttackOnTitan.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

class Eren(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/Eren/eren_stands.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect= self.image.get_rect()
        self.rect.centerx = 80
        self.rect.bottom= 420
        self.speed_x = 0
    
    def update(self):
        self.speed_x= 0
        keystate= pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x= -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x= 5
        self.rect.x += self.speed_x

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Titan(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/Titans/annie.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect= self.image.get_rect()
        self.rect.centerx = 800
        self.rect.bottom= 420
        self.speed_x = 0

    def update(self):
        self.rect.centerx -= 3

all_sprites = pygame.sprite.Group()

eren= Eren()
titan_list= pygame.sprite.Group()
all_sprites.add(eren)


for i in range(20):
    titan= Titan()
    titan.rect.x= random.randrange(1,800)
    titan.rect.y= 210

    titan_list.add(titan)
    all_sprites.add(titan)

execute= True

####################################################################################

while execute:

    CLOCK.tick(40)
    SCREEN.blit(background, (0, 0))   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execute= False
        keystate= pygame.key.get_pressed()
        if keystate[pygame.K_ESCAPE]:
            execute= False
    
    titanCollision= pygame.sprite.spritecollide(eren, titan_list, True)

    all_sprites.update()

    all_sprites.draw(SCREEN)
    pygame.display.flip()

pygame.quit()

