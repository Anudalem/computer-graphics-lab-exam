
##  Create Canvas

import pygame
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("My Canvas")
    screen.fill((255, 255, 255))  

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_F1:
                running = False

        pygame.display.flip()

    pygame.quit()

## Draw Red Line


pygame.draw.line(screen, (255, 0, 0), (50, 50), (250, 50), 3) 


##  Draw Triangles


pygame.draw.polygon(screen, (0, 0, 255), [(50, 50), (100, 150), (0, 150)]) 

## Draw Purple Point


pygame.draw.circle(screen, (128, 0, 128), (250, 200), 5)  

