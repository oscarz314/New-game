import pygame
import time
import player
import spaceship
import background
import functions

# Game settings
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
screen_height = 800
screen_width = 1280
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Useful variables
screen_center = (screen_width/2, screen_height/2)

# Initialize
time_start = int(time.time())
p = player.Player(screen_center[0] - 10, screen_center[1] - 10)
s = spaceship.Spaceship(0, 0)
bg = background.Background(-100, -100)
sprite_array = [s, bg]

# Testing variables
display_sanity = my_font.render(f'Sanity: {p.sanity}', True, (255, 0, 0))


# Start screen


run = True
# -------- Main Program Loop -----------
while run:
    clock.tick(60)
    functions.entropy(p.sanity, time_start)
    player.detect_player_motion(p, sprite_array)

    print(p.sanity)
    ##  ----- NO BLIT ZONE END  ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False


    ## FILL SCREEN, and BLIT here ##
    screen.fill((0, 0, 0))
    screen.blit(bg.image, bg.rect)
    screen.blit(p.image, p.rect)
    screen.blit(s.image, s.rect)
    screen.blit(display_sanity, (1200, 700))
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

