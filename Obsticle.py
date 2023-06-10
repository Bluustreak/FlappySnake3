import pygame
import numpy as np
import os
class Obsticle: 
    def __init__(self, x, y, speed):
        super().__init__
        imgPath = "images/Obsticle-1-Sprite.png"
        self.image = pygame.image.load(os.path.normpath(imgPath)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.size = self.image.get_size()
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        self.x-=self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        #pygame.draw.rect(screen, (0,0,0), (self.x, self.y, self.size[0], self.size[1]))
        