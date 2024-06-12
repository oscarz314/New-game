import pygame
import time
import random
import player


def entropy(player, ship):
    player.sanity -= 1
    ship.health -= 1
    if ship.health > 100:
        ship.health = 100
    if player.sanity > 100:
        player.sanity = 100







