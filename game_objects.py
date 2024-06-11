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


class StatusBar:
    def __init__(self, x, y):
        # Position
        self.x = x
        self.y = y

        # Exterior image
        self.image = pygame.image.load("status_bar.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

class Arrows:
    def __init__(self, x, y, direction):
        # Position
        self.x = x
        self.y = y

        # Exterior image
        if direction == "up":
            self.image = pygame.image.load("up_arrow.png")
        if direction == "left":
            self.image = pygame.image.load("left_arrow.png")
        if direction == "down":
            self.image = pygame.image.load("down_arrow.png")
        if direction == "right":
            self.image = pygame.image.load("right_arrow.png")

        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])