import pygame 

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__
        self.image = pygame.image.load("images\PlayerSprite.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.size = self.image.get_size()
        self.x = x
        self.y = y
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
            if self.x + self.size[0] > o.x and self.x < o.x+o.size[0] and self.y + self.size[1] > o.y and self.y < o.y+o.size[1]:
                return True
        return result
    
    def restrictVertical(self, screen_height):
        if self.y <=0:
            self.y=0
        elif self.y+self.size[1] > screen_height:
            self.y = screen_height-self.size[1]