import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.image = pygame.transform.scale(pygame.image.load("player.png"), (100, 100))
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


def move_player():
    print("move")
