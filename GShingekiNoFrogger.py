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




execute= True

while execute:

    SCREEN.blit(background, (0, 0))   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execute= False

    pygame.display.update()

pygame.quit()

