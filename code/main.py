import pygame
from os.path import join
import random

# general setup:
pygame.init()
clock = pygame.time.Clock()

# the screen:
WINDOWS_WIDTH, WINDOWS_HEIGHT =  1280, 720
display_surface = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT ))
pygame.display.set_caption("Shooter!!!")
running = True

# plain surface:
surf = pygame.Surface((100,200))
surf.fill('red')
x = 100

# player_aircraft:
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center= (WINDOWS_WIDTH/2, WINDOWS_HEIGHT/2))
player_direction = pygame.math.Vector2(1,-1)
player_speed = 300


# stars :20 randomly on screen:
star_surf = pygame.image.load(join('images','star.png')).convert_alpha()
star_tuples_loc = [(random.randint(1, WINDOWS_WIDTH -1), random.randint(1, WINDOWS_HEIGHT -1)) for _ in range(20)]

# meteor:
meteor_surf = pygame.image.load(join('images','meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center=(WINDOWS_WIDTH/2, WINDOWS_HEIGHT/2))

# laser:
laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOWS_HEIGHT - 20))



# MAINLOOP:
while running:
    # framerate:
    # dt datatime = ce qu'on divise poru avoir la bonn,e vitesse en focntion du framerate:
    # delta time = temps qu'il faut pour creer UNE frame en MILLISCONDS 
    dt = clock.tick(24) / 1000 # pour avoir en secondes


    # event loop
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print(event.key == pygame.K_3)

    # draw the game
        # fond:
    display_surface.fill('darkgrey')
        # stars:
    for coord in star_tuples_loc:
        display_surface.blit(star_surf, (coord))

        # meteor:
    display_surface.blit(meteor_surf, meteor_rect)

         # laser:
    display_surface.blit(laser_surf, laser_rect)

        # player:
    player_rect.center += player_direction * player_speed * dt

            # dvd mvt:
    if player_rect.top <= 0:
        player_rect.top = 0
        player_direction.y *= -1 
    elif player_rect.bottom >= WINDOWS_HEIGHT:
        player_rect.bottom = WINDOWS_HEIGHT
        player_direction.y *= -1

    if player_rect.right >= WINDOWS_WIDTH:
        player_rect.right = WINDOWS_WIDTH
        player_direction.x *= -1
    elif player_rect.left <= 0:
        player_rect.left = 0
        player_direction.x *= -1


    display_surface.blit(player_surf, player_rect )
        
    
      
   

    pygame.display.update()


# prevention : close at the end:
pygame.quit()