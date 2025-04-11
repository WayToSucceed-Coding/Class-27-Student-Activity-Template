import pygame
import random

#Initialize PyGame
pygame.init()

#Game Constants
WIDTH,HEIGHT=800,600

#Creating window
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#Title of window
pygame.display.set_caption("Fruit Ninja")

#Load Image
bg=pygame.image.load('assets/background.png')


running=True

while running:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

pygame.quit()




