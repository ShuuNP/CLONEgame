import pygame
import sys

# Initialize pygame
pygame.init()

WIDTH = 1280  
HEIGHT = 720  
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Player AI cloning prototype")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()