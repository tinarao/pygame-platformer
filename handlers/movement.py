import pygame

def y_collision_handler(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()
                
        collided_objects.append(obj)
    return collided_objects

def movement_handler(player, vel, objects):
    keys = pygame.key.get_pressed()
    
    player.x_velocity = 0
    
    if keys[pygame.K_a]:
        player.move_left(vel)
    if keys[pygame.K_d]:
        player.move_right(vel)
        
    y_collision_handler(player, objects, player.y_velocity)