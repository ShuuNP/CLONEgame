import pygame
class Player:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)  #place holder lang po
        self.color = color
        self.speed = 5  

    def playerInput(self, keys):
        if keys[pygame.K_w]: 
            self.rect.y -= self.speed
        if keys[pygame.K_s]:  
            self.rect.y += self.speed
        if keys[pygame.K_a]: 
            self.rect.x -= self.speed
        if keys[pygame.K_d]:  
            self.rect.x += self.speed

    def playerInputMouse(self, mouse_pos):
        return #wala pa dito hahaha
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def mouseTrack(self):
        return pygame.mouse.get_pos() #nonese nga eh baka sa main.py ko nalang to ilagay
