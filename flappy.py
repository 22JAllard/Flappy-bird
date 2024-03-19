import pygame, sys
from pygame.locals import *
import time
import random

pygame.init()
green = (0, 255, 0)
white = (255, 255, 255)
width = 1360
height = 710

font = pygame.font.SysFont('Ariel', 60)
score = 0
gravity = 0.45
bird_height = 350
birdy = pygame.image.load('bird.png')
bird2 = pygame.transform.scale(birdy, (50,50))

random1 = random.randint(100,(height-100))
speed = 30

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Floppy bird')

def towers():
    tower1x = width 
    tower1 = pygame.Rect(tower1x, 0, 70, random1) 
    pygame.draw.rect(screen, white, tower1)
    tower1x -= speed
    pygame.display.update()

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

    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    towers()

    pygame.display.update()
pygame.quit()
sys.exit()
