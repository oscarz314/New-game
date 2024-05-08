import pygame
pygame.transform.scale()
class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fuel = 100
        self.velocity = (15, "down")

        self.image = pygame.image.load("spaceship_image.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


