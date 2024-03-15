import pygame, sys
from pygame.locals import *

pygame.init()
green = (0, 255, 0)
width = 1360
height = 710

gravity = 0.7
bird_height = 350
birdy = pygame.image.load('bird.png')
bird2 = pygame.transform.scale(birdy, (50,50))

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Floppy bird')

run = True
while run:
    screen.fill(green)
    screen.blit(bird2, (100, bird_height))

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        bird_height -= 4
    bird_height += gravity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
sys.exit()
