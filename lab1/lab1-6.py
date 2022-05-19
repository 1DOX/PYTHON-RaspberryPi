import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Key Moving Man')

manImg = pygame.image.load('man.bmp')
pos_x = 150
pos_y = 100

while True: # pygame main loop
    DISPLAYSURF.fill((255, 255, 255)) # white background

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP PRESS")
                pos_y -= 5
            elif event.key == pygame.K_DOWN:
                print("DOWN PRESS")
                pos_y += 5
            elif event.key == pygame.K_LEFT:
                print("LEFT PRESS")
                pos_x -= 5
            elif event.key == pygame.K_RIGHT:
                print("RIGHT PRESS")
                pos_x += 5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    DISPLAYSURF.blit(manImg, (pos_x, pos_y))

    pygame.display.update()
    fpsClock.tick(FPS)