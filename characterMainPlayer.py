import pygame

class Character:
    def __init__(self, x, y, size, color):
        """
        Initialize the character.

        :param x: X-coordinate of the character.
        :param y: Y-coordinate of the character.
        :param size: Size of the square character.
        :param color: Color of the character (e.g., a tuple like (255, 0, 0) for red).
        """
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, screen):
        """
        Draw the character on the screen.

        :param screen: The pygame screen surface.
        """
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def move(self, dx, dy):
        """
        Move the character by a given amount.

        :param dx: Change in x-coordinate.
        :param dy: Change in y-coordinate.
        """
        self.x += dx
        self.y += dy