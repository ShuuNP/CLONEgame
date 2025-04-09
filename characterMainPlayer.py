# characterMainPlayer.py
import pygame
class Player:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)  # Player's rectangle
        self.color = color
        self.speed = 5  # Speed of movement

    def playerInput(self, keys):
        if keys[pygame.K_w]:  # Move up
            self.rect.y -= self.speed
        if keys[pygame.K_s]:  # Move down
            self.rect.y += self.speed
        if keys[pygame.K_a]:  # Move left
            self.rect.x -= self.speed
        if keys[pygame.K_d]:  # Move right
            self.rect.x += self.speed

    def playerInputMouse(self, mouse_pos):
        return
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def mouseTrack(self):
        return pygame.mouse.get_pos()
