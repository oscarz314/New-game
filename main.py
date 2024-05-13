import pygame
from player import Player

# Game settings
screen_height = 800
screen_width = 1280
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# defining variables
p = Player(0, 0)

# Start screen


run = True
# -------- Main Program Loop -----------
while run:
    ##  ----- NO BLIT ZONE END  ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False




    ## FILL SCREEN, and BLIT here ##
    screen.fill((0, 0, 0))
    screen.blit(p.image, p.rect)
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

