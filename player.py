import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.delta = 1

        self.image = pygame.transform.scale(pygame.image.load("player.png"), (100, 100))
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_player(self, direction):
        if direction == "right":
            self.x += self.delta
        if direction == "left":
            self.x -= self.delta
        if direction == "up":
            self.y -= self.delta
        if direction == "down":
            self.y += self.delta

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


def detect_player_motion(player):
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        player.move_player("right")
    if keys[pygame.K_a]:
        player.move_player("left")
    if keys[pygame.K_w]:
        player.move_player("up")
    if keys[pygame.K_s]:
        player.move_player("down")
