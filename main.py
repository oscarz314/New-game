import pygame
import player
import spaceship
import background

# Game settings
screen_height = 800
screen_width = 1280
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# Useful variables
screen_center = (screen_width/2, screen_height/2)

# Initialize
p = player.Player(screen_center[0], screen_center[1])
s = spaceship.Spaceship(0, 0)
bg = background.Background(-100, -100)
sprite_array = [s, bg]
# Start screen


run = True
# -------- Main Program Loop -----------
while run:
    player.detect_player_motion(p, sprite_array)
    ##  ----- NO BLIT ZONE END  ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False


    ## FILL SCREEN, and BLIT here ##
    screen.fill((0, 0, 0))
    screen.blit(bg.image, bg.rect)
    screen.blit(p.image, p.rect)
    screen.blit(s.image, s.rect)
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

