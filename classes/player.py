import pygame
from img.sprites import load_sprite_sheets

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "VirtualGuy", 32, 32, True)
    
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_velocity = 0
        self.y_velocity = 0
        self.mask = None
        self.anim_count = 0
        self.direction = "left"
        self.fall_count = 0
        
    def move(self, x_dir, y_dir):
        self.rect.x += x_dir
        self.rect.y += y_dir
        
    def move_left(self, vel): 
        self.x_velocity = -vel
        if self.direction != "left":
            self.direction = "left"
            self.anim_count = 0
        
    def move_right(self, vel): 
        self.x_velocity = vel
        if self.direction != "right":
            self.direction = "right"
            self.anim_count = 0
            
    def loop(self, fps):
        # Gravity
        # self.y_velocity += min(1, (self.fall_count / fps) * self.GRAVITY)
        
        self.move(self.x_velocity, self.y_velocity)
        self.fall_count += 1
        
    def draw(self, window):
        self.sprite = self.SPRITES[f'idle_{self.direction}'][0]
        window.blit(self.sprite, (self.rect.x, self.rect.y))