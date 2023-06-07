import pygame 

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__
        self.image = pygame.image.load("images\PlayerSprite.png")
        self.size = self.image.get_size()
        self.x = x - self.size // 2
        self.y = y - self.size // 2
        self.dy = 0
        self.gravity = 0.5

    def jump(self):
        self.dy = -10

    def update(self):
        self.dy += self.gravity
        self.y += self.dy

    def is_off_screen(self, screen_height):
        return self.y > screen_height or self.y < 0

    def draw(self, screen):
        #pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.size, self.size))
        screen.blit(self.image, (self.x, self.y))

    def has_collided(self, List_of_obsticles):
        result = False                
        for o in List_of_obsticles:
            os2 = o.size/2
            if (self.x+self.size) > (o.x - os2) and self.x < (o.x + os2) and self.y < (o.y + os2) and (self.y+self.size) > (o.y - os2):
                result = True
        return result