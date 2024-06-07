import pygame

class Wall:
    def __init__(self, x, y):
        # Position
        self.x = x
        self.y = y

        # Exterior image
        self.image = pygame.transform.scale(pygame.image.load("wall.png"), (1920, 1080))
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


class Floor:
    def __init__(self, x, y):
        # Position
        self.x = x
        self.y = y

        # Exterior image
        self.image = pygame.image.load("floor.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


world_map = []


def make_world(size_x, size_y):
    tile_x = 0
    tile_y = 0
    for i in range(size_y):
        world_map.append([])
        for j in range(size_x):
            world_map[i].append(Floor(tile_x, tile_y))
            tile_x += 128
        tile_y += 128
        tile_x = 0
    return world_map
