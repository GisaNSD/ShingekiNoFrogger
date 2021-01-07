import pygame
import sys
import random

W = 800
H = 490
SCREEN = pygame.display.set_mode((W, H))
icon = pygame.image.load('images/wingsOfFreedom.png')
background = pygame.image.load('images/background1.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption('Shingeki No Frogger')

class Eren:
    def __init__(self):

        self.character_x = 50
        self.character_y = 270
        self.velocity = 7
        self.jumping = False
        self.jumpDistance = 8
        self.left = False
        self.right = False
        self.steps = 0

        self.stands = pygame.image.load('images/Eren/eren_stands.png')

        self.run_right = [pygame.image.load('images/Eren/eren_run0.png'),
                        pygame.image.load('images/Eren/eren_run1.png'),
                        pygame.image.load('images/Eren/eren_run2.png')]

        self.run_left = [pygame.image.load('images/Eren/eren_left0.png'),
                        pygame.image.load('images/Eren/eren_left1.png'),
                        pygame.image.load('images/Eren/eren_left2.png')]

        self.jumps = [pygame.image.load('images/Eren/eren_jumps0.png'),
                pygame.image.load('images/Eren/eren_jumps1.png')]

    def update(self):
           
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.character_x > self.velocity:
            self.character_x -= self.velocity
            self.left = True
            self.right = False

        elif keys[pygame.K_RIGHT] and self.character_x < 650 - self.velocity:
            self.character_x += self.velocity
            self.left = False
            self.right = True

        else:
            self.left = False
            self.right = False
            self.steps = 0

        if not (self.jumping):
            if keys[pygame.K_SPACE]:
                self.jumping = True
                self.left = False
                self.right = False
                self.steps = 0
            else:
                if self.jumpDistance >= -8:
                    self.character_y -= (self.jumpDistance * abs(self.jumpDistance)) * 0.5
                    self.jumpDistance -= 1
        else:
            self.jumpDistance = 8
            self.jumping = False

class game():
    def __init__(self):
        pygame.init()
        
        pygame.mixer.music.load('sound/AttackOnTitan.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
        self.SCREEN= pygame.display.set_mode((W, H))
        self.CLOCK = pygame.time.Clock()
        self.gameObjects = []
        self.eren= Eren()
        self.gameObjects.append(self.eren)

        #Movimiento
    def screenLoad(self):
        x = 0
        SCREEN.blit(background, (x, 0))
        SCREEN.blit(background, (W + x, 0))
        if x == -W:
            SCREEN.blit(background, (W + x, 0))
            x = 0    
        x-= 5

    def erenMovement(self):

        if self.eren.steps + 1 >= 3:
            self.eren.steps = 0
            
        if self.eren.left:
            SCREEN.blit(self.eren.run_left[self.eren.steps], (int(self.eren.character_x), int(self.eren.character_y)))
            self.eren.steps += 1

        elif self.eren.right:
            SCREEN.blit(self.eren.run_right[self.eren.steps // 1], (int(self.eren.character_x), int(self.eren.character_y)))
            self.eren.steps += 1

        elif self.eren.jumping + 1 >= 2:
            SCREEN.blit(self.eren.jumps[self.eren.steps], (int(self.eren.character_x), int(self.eren.character_y)))
            self.eren.steps += 1

        else:
            SCREEN.blit(self.eren.stands,(int(self.eren.character_x), int(self.eren.character_y)))
   
    def run(self):
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                              
            for gameObj in self.gameObjects:
                SCREEN.blit(gameObj.stands,(int(gameObj.character_x), int(gameObj.character_y)))
            
            pygame.display.flip()

            self.eren.update()
            self.erenMovement()
            self.screenLoad()
            self.CLOCK.tick(30)

game().run()