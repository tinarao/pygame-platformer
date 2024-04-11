import pygame
from os.path import join

def get_background(name, WIDTH, HEIGHT):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []
    
    for i in range(WIDTH // width + 4):
        for j in range(HEIGHT // height):
            pos = [i*width, j*height]
            tiles.append(pos)
            
    return tiles, image
    
def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)
    
    player.draw(window)
    
    pygame.display.update()
    
