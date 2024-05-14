import pygame, sys
from pygame.locals import *
import time
import random

pygame.init()
green = (69, 200, 69)
white = (255, 255, 255)
width = 1360
height = 610

font = pygame.font.SysFont('Arial', 60)
score = 0
gravity = 0.45
bird_height = 350
birdy = pygame.image.load('bird.png')
bird2 = pygame.transform.scale(birdy, (50,50))

sky = pygame.image.load('sky.jpg')
skyimg = pygame.transform.scale(sky, (width, height))
random1 = random.randint(100,(height-100))
speed = 30

gap1 = 0
gap2 = 0
gap3 = 0
pwidth = 100
p1x = height
p2x = height + 300
p3x = height + 600

gap1 = random.randint(100,height - 100)
gap2 = random.randint(100,height - 100)
gap3 = random.randint(100,height - 100)
p1top = pygame.Rect(p1x, 0, pwidth, gap1)
p1bottom = pygame.Rect(p1x, gap1 + 100, pwidth, height - gap1 + 100)

p2top = pygame.Rect(p2x, 0, pwidth, gap2)
p2bottom = pygame.Rect(p2x, gap2 + 100, pwidth, height - gap2 + 100)

p3top = pygame.Rect(p3x, 0, pwidth, gap3)
p3bottom = pygame.Rect(p3x, gap3 + 100, pwidth, height - gap3 + 100)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Floppy bird')

def towers(gap1, gap2, gap3):
    

run = True
while run:
    screen.blit(skyimg, (0,0))
    screen.blit(bird2, (100, bird_height))
    screen.blit(p1top, (p1x, 0))
    screen.blit(p1bottom, (p1x, gap1))
    screen.blit(p2top, (p2x, 0))
    screen.blit(p2bottom, (p2x, gap2))
    screen.blit(p3top, (p3x, 0))
    screen.blit(p3bottom, (p3x, gap3))

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        if bird_height < 0:
            bird_height = 0
        else:
            bird_height -= 4
    if bird_height + bird2.get_height() >= height:
        bird_height = height - bird2.get_height()
    else:        
        bird_height += gravity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if pygame.time.get_ticks() % 500 == 0:
        score += 1

    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    towers(gap1, gap2, gap3)

    pygame.display.update()
pygame.quit()
sys.exit()
