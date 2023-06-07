import pygame
import numpy as np
class Obsticle: 
    def __init__(self, x, y, speed):
        super().__init__
        self.image = pygame.image.load("images\Obsticle-1-Sprite.png")
        self.size = self.image.get_size()
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        self.x-=self.speed

    def draw(self, screen):
        #halfsize = self.size/2
        #r,g,b=np.clip(self.speed*10, 0, 255), np.clip(255-self.speed*10, 0, 255), 0
        #pygame.draw.rect(screen, (r,g,b), (self.x-halfsize, self.y-halfsize, self.size, self.size))
        screen.blit(self.image, (self.x, self.y))
        