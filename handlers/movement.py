import pygame

def movement_handler(player, vel):
    keys = pygame.key.get_pressed()
    
    player.x_velocity = 0
    
    if keys[pygame.K_LEFT]:
        player.move_left(vel)
    if keys[pygame.K_RIGHT]:
        player.move_right(vel)