import pygame
import time
import random

# make left right up down sprites as well as the UI for maintenance

def repairing():
    arrows = ["left", "right", "up", "down"]
    time_start_r = int(time.time())
    arrow_series = []

    for i in range(10):
        arrow_series.append(arrows[random.randint(0, 3)])

    i = 1
    while i != len(arrow_series):
        if int(time.time()) - time_start_r == 1:
            print(arrow_series[i])
            time_start_r = int(time.time())
            i += 1


