import pygame
import sys
from characterMainPlayer import Player

pygame.init()

WIDTH = 1280  
HEIGHT = 720  
fps = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.mouse.set_visible(False)  # Hide the mouse cursor
pygame.display.set_caption("Player AI cloning prototype")
player = Player(x=WIDTH//2, y=HEIGHT//2, size=20, color=(0, 255, 0))

clock = pygame.time.Clock()

#main main
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(fps)
    
    keys = pygame.key.get_pressed()
    player.playerInput(keys)
    mouse_pos = player.mouseTrack()
    #print(mouse_pos)  # Print the mouse position
 
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, 'red', mouse_pos, 5)
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()