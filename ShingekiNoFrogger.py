import pygame
import sys
import random

pygame.init()

#Pantalla - ventana
W, H = 800, 490
SCREEN = pygame.display.set_mode((W, H))
pygame.display.set_caption('Shingeki No Frogger')
ICON=pygame.image.load('images/wingsOfFreedom.png')
pygame.display.set_icon(ICON)

background = pygame.image.load('images/background1.jpg')

pygame.mixer.music.load('sound/AttackOnTitan.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)


#Personaje
stands = pygame.image.load('images/Eren/eren_stands.png')

run_right = [pygame.image.load('images/Eren/eren_run0.png'),
                 pygame.image.load('images/Eren/eren_run1.png'),
                 pygame.image.load('images/Eren/eren_run2.png')]

run_left = [pygame.image.load('images/Eren/eren_left0.png'),
                   pygame.image.load('images/Eren/eren_left1.png'),
                   pygame.image.load('images/Eren/eren_left2.png')]

jumps = [pygame.image.load('images/Eren/eren_jumps0.png'),
         pygame.image.load('images/Eren/eren_jumps1.png')]

x=0
xTitan= 0
titanVelocity= random.randrange(1, 100)
titancol1 = W + xTitan
titancol2= W + 500 + titanVelocity
titancol3= W + 1500 + titanVelocity
character_x = 50
character_y = 270
velocity = 7

#Titan
titan0 = pygame.image.load('images/Titans/bertholho.png')
titan1= pygame.image.load('images/Titans/annie.png')
titan2= pygame.image.load('images/Titans/reiner1.png')

titans= [titan0, titan1, titan2]

titanArray= []
    
while(len(titanArray) <= 3):
    titanRandom= random.choice(titans)
    titanArray.append(titanRandom)

def titanAttacks():
    
    global xTitan
    global titancol1
    global titancol2
    global titancol3

    SCREEN.blit(titanArray[0], (titancol1, 220))
    SCREEN.blit(titanArray[1], (titancol2, 220))
    SCREEN.blit(titanArray[2], (titancol3, 220))

    titancol1 -= random.randrange(1, 10)
    titancol2 -= random.randrange(1, 10)
    titancol3 -= random.randrange(1, 10)
    xTitan -=  random.randrange(1,10)

CLOCK = pygame.time.Clock()

jumping = False
jumpCount = 10
left = False
right = False
steps = 0

#Movimiento
def screenLoad():
    
    global steps
    global x

    SCREEN.blit(background, (x, 0))
    SCREEN.blit(background, (W + x, 0))

    if x == -W:
        SCREEN.blit(background, (W + x, 0))
        x = 0
    x-= 2

    if steps >= 3:
        steps = 0
    if left:
        SCREEN.blit(run_left[steps], (int(character_x), int(character_y)))
        steps += 1
    elif right:
        SCREEN.blit(run_right[steps], (int(character_x), int(character_y)))
        steps += 1
    elif jumping + 1 >= 2:
        SCREEN.blit(jumps[steps], (int(character_x), int(character_y)))
        steps += 1
    else:
        SCREEN.blit(stands,(int(character_x), int(character_y)))

# def collision():
#     if character_x == titancol1:
#         sys.exit()
    
#     if character_x == titancol2:
#         sys.exit()
    
#     if character_x == titancol3:
#         sys.exit()

execute = True

while execute:

    CLOCK.tick(18)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            execute = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and character_x > velocity:
        character_x -= velocity
        left = True
        right = False
    
    elif keys[pygame.K_RIGHT] and character_x < 650 - velocity:
        character_x += velocity
        left = False
        right = True

    else:
        left = False
        right = False
        steps = 0

    if not (jumping):
        if keys[pygame.K_SPACE]:
            jumping = True
            left = False
            right = False
            steps = 0
    else:
        if jumpCount >= -10:
            character_y -= (jumpCount * abs(jumpCount)) * 0.5
            character_x += 3
            jumpCount -= 1
        else:
            jumpCount = 10
            jumping = False
   
    if keys[pygame.K_ESCAPE]:
        sys.exit()

    # if stands.colliderect(titan0):
    #     sys.exit()
    
    # if character_x == titancol2:
    #     sys.exit()
    
    # if character_x == titancol3:
    #     sys.exit()
        
    titanAttacks()
    # collision()
    pygame.display.update()
    screenLoad()