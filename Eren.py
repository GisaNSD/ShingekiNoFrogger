import pygame

class Eren:

    def __init__(self):
        super().__init__()
        self.stands= pygame.image.load("images/Eren/eren_stands.png").convert()

        self.run_right= [pygame.image.load("images/Eren/eren_run0.png").convert(),
                        pygame.image.load("images/Eren/eren_run1.png").convert(),
                        pygame.image.load("images/Eren/eren_run2.png").convert()]

        self.run_left= [pygame.image.load("images/Eren/eren_left0.png").convert(),
                        pygame.image.load("images/Eren/eren_left1.png").convert(),
                        pygame.image.load("images/Eren/eren_left2.png")]
        
        self.jumps = [pygame.image.load('images/Eren/eren_jumps0.png'),
         pygame.image.load('images/Eren/eren_jumps1.png')]

        self.x = 0
        self.character_x = 50
        self.character_y = 270
        self.velocity = 5
        self.jumpCount= 8
        self.jumps= False
        self.left = False
        self.right = False
        self.steps= 0
        self.jumping = False
        
    
    def update(self):
        
        #Contador de pasos
        if steps + 1 >= 3:
            steps = 0
        #Movimiento a la izquierda
        if left:
            SCREEN.blit(run_left[steps // 1], (int(character_x), int(character_y)))
            steps += 1

        #Movimiento a la derecha
        elif right:
            SCREEN.blit(run_right[steps // 1], (int(character_x), int(character_y)))
            steps += 1

        elif jumping + 1 >= 2:
            SCREEN.blit(jumps[steps // 1], (int(character_x), int(character_y)))
            steps += 1

        else:
            SCREEN.blit(stands,(int(character_x), int(character_y)))

    def movement(self):
        #Opción tecla pulsada
        keys = pygame.key.get_pressed()

        #Tecla A - Moviemiento a la izquierda
        if keys[pygame.K_LEFT] and character_x > velocity:
            character_x -= velocity
            left = True
            right = False

        #Tecla D - Moviemiento a la derecha
        elif keys[pygame.K_RIGHT] and character_x < 650 - velocity:
            character_x += velocity
            left = False
            right = True

        #Personaje quieto
        else:
            left = False
            right = False
            steps = 0

        #Tecla SPACE - Salto
        if not (jumping):
            if keys[pygame.K_SPACE]:
                jumping = True
                left = False
                right = False
                steps = 0
        else:
            if jumpCount >= -8:
                character_y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else:
                jumpCount = 8
                jumping = False

            