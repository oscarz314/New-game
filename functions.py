import pygame
import time
import random
import player


def entropy(player, ship):
    player.sanity -= 1
    ship.health -= 1


def repairing():
    arrows = ["left", "right", "up", "down"]
    time_start = int(time.time())
    arrow_series = []
    input = ""

    # generate series
    for i in range(10):
        arrow_series.append(arrows[random.randint(0, 3)])

    # print series
    i = 1
    while i != len(arrow_series):
        if keys[pygame.K_d]:
            input = "right"
        if keys[pygame.K_a]:
            input = "left"
        if keys[pygame.K_w]:
            input = "up"
        if keys[pygame.K_s]:
            input = "down"
        if int(time.time()) - time_start == 1:
            print(arrow_series[i])
            time_start = int(time.time())
            i += 1





