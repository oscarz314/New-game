import pygame
import time
import random
import player
import spaceship
import functions
import game_objects
import world



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
game_win = False
game_lose = False
frame_time = 1

# Initialize
time_start = int(time.time())
p = player.Player(screen_center[0] - 100, screen_center[1] - 100)
s = spaceship.Spaceship(0, 0)
machine = game_objects.Machine(100 , 100)
arrow_object = game_objects.Arrows(100, 550, "up")
floor = world.Floor(0, 0)
world = world.make_world(10, 7)
status_bar = game_objects.StatusBar(940, 550)
sprite_array = [s, machine]
for i in range(len(world)):
    for j in range(len(world)):
        sprite_array.append(world[i][j])

# Text
display_sanity = my_font.render(f'Sanity: {p.sanity}', True, (255, 0, 0))
display_ship_stats = my_font.render(f'fuel: {s.fuel}, velocity:{s.velocity}, health:{s.health}', True, (0, 0 , 255))
display_lose = my_font.render(f'YOU LOST', True, (255, 0, 0))


# functions
# repairing variables and function
repairing = False
arrows = ["left", "right", "up", "down"]
arrow_series = []
arrow_series_index = 0
player_input = ""
display_arrow_sync = my_font.render(f'Frame {arrow_series_index}: Not synced', True, (255, 0, 0))
is_synced = ["not synced", (255, 0, 0)]
sync_score = 0
round_generated = False


def generate_arrow_series():
    for i in range(10):
        arrow_series.append(arrows[random.randint(0, 3)])


# Start screen
run = True
# -------- Main Program Loop -----------
while run:
    clock.tick(60)
    player.detect_player_input(p, sprite_array)
    keys = pygame.key.get_pressed()
    frame_time += 1
    if frame_time > 60:
        frame_time = 1

    # Mechanics

    # Entropy decreasing stats
    if int(time.time()) - time_start >= 1:
        functions.entropy(p, s)
        display_sanity = my_font.render(f'Sanity: {p.sanity}', True, (255, 0, 0))
        display_ship_stats = my_font.render(f'fuel: {s.fuel}, velocity:{s.velocity}, health:{s.health}', True,
                                            (0, 0, 255))
        time_start = int(time.time())

    # Collision:
    if p.rect.colliderect(machine.rect):
        # repair
        if keys[pygame.K_r] == True:
            repairing = True

    # Mechanics
    # repairing
    if repairing == True:
        if round_generated == False:
            generate_arrow_series()
            round_generated = True

        arrow_object = game_objects.Arrows(100, 550, arrow_series[arrow_series_index])
        display_arrow_sync = my_font.render(f'Frame {arrow_series_index}: {is_synced[0]}', True, is_synced[1])

        if arrow_series[arrow_series_index] == "up" and keys[pygame.K_UP]:
            is_synced[0] = "synced"
            is_synced[1] = (0, 255, 0)
            sync_score += 1

        if arrow_series[arrow_series_index] == "left" and keys[pygame.K_LEFT]:
            is_synced[0] = "synced"
            is_synced[1] = (0, 255, 0)
            sync_score += 1

        if arrow_series[arrow_series_index] == "down" and keys[pygame.K_DOWN]:
            is_synced[0] = "synced"
            is_synced[1] = (0, 255, 0)
            sync_score += 1

        if arrow_series[arrow_series_index] == "right" and keys[pygame.K_RIGHT]:
            is_synced[0] = "synced"
            is_synced[1] = (0, 255, 0)
            sync_score += 1

        if frame_time % 30 == 0:
            arrow_series_index += 1
            is_synced[0] = "not synced"
            is_synced[1] = (255, 0, 0)
            sync_score += 1

        if arrow_series_index == len(arrow_series):
            p.health += (sync_score / 10) * 40
            arrow_series = []
            arrow_series_index = 0
            round_generated = False
            repairing = False


    # Win or lose conditions
    if p.sanity == 0 or s.health == 0:
        game_lose = True

    ##  ----- NO BLIT ZONE END  ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False


    ## FILL SCREEN, and BLIT here ##
    screen.fill((0, 0, 0))
    for i in range(len(world)):
        for j in range(len(world)):
            screen.blit(world[i][j].image, world[i][j].rect)
    screen.blit(machine.image, machine.rect)

    if repairing == True:
        screen.blit(arrow_object.image, arrow_object.rect)
        screen.blit(display_arrow_sync, (120, 660))
    screen.blit(p.image, p.rect)
    screen.blit(s.image, s.rect)
    screen.blit(status_bar.image, status_bar.rect)
    screen.blit(display_ship_stats, (950, 600))
    screen.blit(display_sanity, (950, 620))
    if game_lose == True:
        screen.blit(display_lose, (screen_center[0], screen_center[1]))

    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()


# instead of using time to wait I can use frames as timer.
