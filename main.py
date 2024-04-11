import os
import pygame
from dotenv import load_dotenv

load_dotenv()
pygame.init()
pygame.display.set_caption("Платформер")

# consts
FPS = 60
PLAYER_VEL = 5
WIDTH = 1000
HEIGHT = 800

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    from img.get_bg import get_background, draw
    from classes.player import Player
    from handlers.movement import movement_handler
    from classes.object import Block
    
    block_size = 96
    clock = pygame.time.Clock()
    background, bg_image = get_background("Pink.png", WIDTH, HEIGHT)
    player = Player(WIDTH / 2 - 25, HEIGHT - 500, 50, 50)

    blocks = []
    
    # Floor
    for i in range(0, (WIDTH // block_size) * 100, block_size):
        blocks.append(
            Block(i, HEIGHT - block_size, block_size)
        )
    
    offset_x = 0
    scroll_area_width = 200
    
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        player.loop(FPS)
        movement_handler(player, PLAYER_VEL, blocks)
        draw(window, background, bg_image, player, blocks, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_velocity > 0) or (
            (player.rect.left - offset_x <= scroll_area_width) and player.x_velocity < 0):
            offset_x += player.x_velocity
            
    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main(window)