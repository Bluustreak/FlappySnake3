import pygame
import numpy as np
class Obsticle: 
    def __init__(self, x, y, speed):
        super().__init__
        self.image = pygame.image.load("images\Obsticle-1-Sprite.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.size = self.image.get_size()
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        self.x-=self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        #pygame.draw.rect(screen, (0,0,0), (self.x, self.y, self.size[0], self.size[1]))
        