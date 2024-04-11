import pygame

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_velocity = 0
        self.y_velocity = 0
        self.mask = None
        self.anim_count = 0
        self.direction = "left"
        
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
        self.move(self.x_velocity, self.y_velocity)
        
    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)