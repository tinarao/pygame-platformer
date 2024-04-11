import os
import pygame
from dotenv import load_dotenv

load_dotenv()
pygame.init()
pygame.display.set_caption("Платформер")

# consts
FPS = 60
PLAYER_VEL = 5
WIDTH = int(os.getenv("SCREEN_WIDTH"))
HEIGHT = int(os.getenv("SCREEN_HEIGHT"))

window = pygame.display.set_mode((HEIGHT, WIDTH))

def main(window):
    from img.get_bg import get_background, draw
    from classes.player import Player
    from handlers.movement import movement_handler
    
    clock = pygame.time.Clock()
    background, bg_image = get_background("Yellow.png", WIDTH, HEIGHT)
    player = Player(100, 100, 50, 50)
    
    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        player.loop(FPS)
        movement_handler(player, PLAYER_VEL)
        draw(window, background, bg_image, player)
            
    pygame.quit()
    quit()
    

if __name__ == "__main__":
    main(window)