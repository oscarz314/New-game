import pygame

import pygame
class Machine:
    def __init__(self, x, y):
        # Position
        self.x = x
        self.y = y

        # Exterior image
        self.image = pygame.transform.scale(pygame.image.load("machine.png"), (200, 200))
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

        # Interior image

