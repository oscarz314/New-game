import pygame
import functions
import asyncio


class Player:
    def __init__(self, x, y):
        # position
        self.x = x
        self.y = y
        self.delta = 5

        # player stats
        self.sanity = 80
        self.health = 100
        self.hunger = 100

        # player image
        self.image = pygame.transform.scale(pygame.image.load("player.png"), (256, 256))
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_player(self, direction, sprite_array):
        if direction == "right":
            for i in range(len(sprite_array)):
                sprite_array[i].x -= self.delta
        if direction == "left":
            for i in range(len(sprite_array)):
                sprite_array[i].x += self.delta
        if direction == "up":
            for i in range(len(sprite_array)):
                sprite_array[i].y += self.delta
        if direction == "down":
            for i in range(len(sprite_array)):
                sprite_array[i].y -= self.delta

        for i in range(len(sprite_array)):
            sprite_array[i].rect = pygame.Rect(sprite_array[i].x, sprite_array[i].y, sprite_array[i].image_size[0], sprite_array[i].image_size[1])

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def health(self, sanity):
        sanity -= 1

def detect_player_input(player, sprite_array):
    # player movement
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        player.move_player("right", sprite_array)
    if keys[pygame.K_a]:
        player.move_player("left", sprite_array)
    if keys[pygame.K_w]:
        player.move_player("up", sprite_array)
    if keys[pygame.K_s]:
        player.move_player("down", sprite_array)

