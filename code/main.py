import pygame
from os.path import join
import random

# general setup:
pygame.init()

# the screen:
WINDOWS_WIDTH, WINDOWS_HEIGHT =  1280, 720
display_surface = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT ))
pygame.display.set_caption("Shooter!!!")
running = True

# plain surface:
surf = pygame.Surface((100,200))
surf.fill('red')
x = 100

# importing image:
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()


# stars 20 randomly on screen:
star_surf = pygame.image.load(join('images','star.png')).convert_alpha()
star_tuples_loc = [(random.randint(1, WINDOWS_WIDTH -1), random.randint(1, WINDOWS_HEIGHT -1)) for _ in range(20)]



# MAINLOOP:
while running:
    # event loop
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
        # fond:
    display_surface.fill('darkgrey')
        # stars:
    for coord in star_tuples_loc:
        display_surface.blit(star_surf, (coord))
    x += 0.1
        # player:
    display_surface.blit(player_surf, (x, 150))
    pygame.display.update()


# prevention : close at the end:
pygame.quit()