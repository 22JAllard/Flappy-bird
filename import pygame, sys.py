import pygame, sys
from pygame.locals import *

pygame.init()
green = (0, 255, 0)
width = 1360
height = 710

bird = pygame.Rect(height // 2, 100, 50, 50)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Floppy bird')

run = True
while run:
    for event in pygame.event.get():
        screen.fill(green)
        pygame.draw.rect(screen, white, bird)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
