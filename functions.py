import pygame
import time
import player



def entropy(sanity, time_start):
    if int(time.time()) == time_start + 4:
        sanity -= 1
        time_start = int(time.time())
